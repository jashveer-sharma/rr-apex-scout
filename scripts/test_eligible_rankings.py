import pandas as pd
import numpy as np
import json

# 1. Load datasets
bball = pd.read_csv('DataSet/ball_by_ball.csv', low_memory=False)
matches = pd.read_csv('DataSet/matches.csv', low_memory=False)
comps = pd.read_csv('DataSet/competitions.csv', low_memory=False)
teams = pd.read_csv('DataSet/teams.csv', low_memory=False)
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv', low_memory=False)

matches = matches.merge(comps[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id', how='left')

# Excluded categories mapping (e.g. Pakistan national team / Pakistan A)
excluded_pak_players = set(mapping[mapping['team_name'].isin(['Pakistan', 'Pakistan A'])]['player_id'].unique())
print(f"Total PCB-registered excluded players: {len(excluded_pak_players)}")

# Weighting
def get_comp_weight(comp_name):
    if pd.isna(comp_name):
        return 1.0
    c_lower = comp_name.lower()
    if 'ipl' in c_lower or 'indian premier league' in c_lower:
        return 1.25
    elif 'world cup' in c_lower or 'asia cup' in c_lower:
        return 1.15
    elif any(top in c_lower for top in ['india', 'australia', 'england', 'south africa', 'new zealand']):
        return 1.10
    else:
        return 0.90

matches['comp_weight'] = matches['comp_name'].apply(get_comp_weight)
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)
bball = bball.merge(matches[['match_id', 'comp_id', 'comp_name', 'match_format', 'season', 'comp_weight', 'knock_out', 'revised_target', 'win_team_id']], on='match_id', how='left')

bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0)

bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'
bball['is_bowler_wicket'] = bball['is_wicket'] & (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) & bball['dismissal_type'].notna()

bball['cum_runs'] = bball.groupby(['match_id', 'innings'])['ball_total_runs'].cumsum()
bball['cum_wickets'] = bball.groupby(['match_id', 'innings'])['is_wicket'].cumsum()
bball['cum_legal_balls'] = bball.groupby(['match_id', 'innings'])['is_legal_ball_bowler'].cumsum()

bball['prev_cum_runs'] = bball['cum_runs'] - bball['ball_total_runs']
bball['prev_cum_wickets'] = bball['cum_wickets'] - bball['is_wicket'].astype(int)
bball['prev_legal_balls'] = bball['cum_legal_balls'] - bball['is_legal_ball_bowler'].astype(int)

inn1_totals = bball[bball['innings'] == 1].groupby('match_id')['ball_total_runs'].sum().reset_index()
inn1_totals = inn1_totals.rename(columns={'ball_total_runs': 'inn1_total_runs'})
bball = bball.merge(inn1_totals, on='match_id', how='left')

bball['target'] = np.where(
    bball['revised_target'].notna() & (bball['revised_target'] > 0),
    bball['revised_target'],
    bball['inn1_total_runs'] + 1
)

bball['balls_remaining'] = np.maximum(0, 120 - bball['prev_legal_balls'])
bball['runs_required'] = np.maximum(0, bball['target'] - bball['prev_cum_runs'])
bball['wickets_in_hand'] = np.maximum(0, 10 - bball['prev_cum_wickets'])

bball['current_rrr'] = np.where(
    (bball['innings'] == 2) & (bball['balls_remaining'] > 0),
    (bball['runs_required'] / bball['balls_remaining']) * 6.0,
    np.nan
)
bball['current_crr'] = np.where(
    bball['prev_legal_balls'] > 0,
    (bball['prev_cum_runs'] / bball['prev_legal_balls']) * 6.0,
    8.0
)

# Pressure calculation
rrr = bball['current_rrr'].fillna(8.0)
stage_factor = 1.0 + (120 - bball['balls_remaining']) / 120.0
wkt_factor = 1.0 + (10 - bball['wickets_in_hand']) * 0.1
knockout_mult = np.where(bball['knock_out'] == 1, 1.25, 1.0)

inn2_p = (2.5 + 3.0 * ((rrr - 6.0) / 6.0)) * stage_factor * (wkt_factor / 1.2) * knockout_mult
inn2_p = np.clip(inn2_p, 1.0, 10.0)

over = bball['overid']
wkts = bball['wickets_in_hand']
inn1_p = np.where(
    over <= 6,
    3.0 + np.maximum(0, 8 - wkts) * 1.5,
    np.where(
        over <= 15,
        4.0 + np.maximum(0, 6 - wkts) * 1.2 + np.where(bball['current_crr'] < 7.0, 1.0, 0.0),
        6.5 + (over - 16) * 0.7 + np.where(wkts <= 4, 1.2, 0.0)
    )
) * knockout_mult
inn1_p = np.clip(inn1_p, 1.0, 10.0)

bball['pressure_index'] = np.where(
    bball['innings'].isin([3, 4]), 10.0,
    np.where(bball['innings'] == 2, inn2_p, inn1_p)
)

bball['is_pressure'] = bball['pressure_index'] >= 6.5
bball['weighted_ball'] = bball['comp_weight']
bball['weighted_runs_bat'] = bball['runs'] * bball['comp_weight']
bball['weighted_runs_bowl'] = bball['bowler_runs_conceded'] * bball['comp_weight']
bball['weighted_wkts_bowl'] = bball['is_bowler_wicket'] * bball['comp_weight']

# ==================== CRITICAL UPSTREAM ELIGIBILITY FILTER ====================
# Filter out excluded players BEFORE ranking
print("\n--- Applying Upstream Player Eligibility Filter ---")
bball_eligible_bat = bball[~bball['striker_id'].isin(excluded_pak_players)].copy()
bball_eligible_bowl = bball[~bball['bowler_id'].isin(excluded_pak_players)].copy()

print(f"Deliveries before batter filter: {len(bball)}, after: {len(bball_eligible_bat)}")
print(f"Deliveries before bowler filter: {len(bball)}, after: {len(bball_eligible_bowl)}")

# ==================== BATTER RANKINGS (ELIGIBLE ONLY) ====================
b_bat = bball_eligible_bat[bball_eligible_bat['is_legal_ball_batter']].copy()
b_bat['is_dot'] = (b_bat['runs'] == 0) & (b_bat['extras1_runs'] == 0)
b_bat['is_boundary'] = b_bat['is_four'] | b_bat['is_six']

bat_base = b_bat.groupby(['striker_id', 'striker_name']).agg(
    base_balls=('weighted_ball', 'sum'),
    base_raw_balls=('runs', 'count'),
    base_runs=('weighted_runs_bat', 'sum'),
    base_dismissals=('is_wicket', 'sum')
).reset_index()

bat_press = b_bat[b_bat['is_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls=('weighted_ball', 'sum'),
    press_raw_balls=('runs', 'count'),
    press_runs=('weighted_runs_bat', 'sum'),
    press_dismissals=('is_wicket', 'sum'),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('comp_name', lambda s: (s.str.contains('IPL', case=False, na=False)).sum())
).reset_index()

bat_df = bat_base.merge(bat_press, on=['striker_id', 'striker_name'], how='inner')
qual_bat = bat_df[(bat_df['press_raw_balls'] >= 100) & (bat_df['press_matches'] >= 8)].copy()

qual_bat['base_sr'] = (qual_bat['base_runs'] / qual_bat['base_balls']) * 100
qual_bat['base_avg'] = qual_bat['base_runs'] / np.maximum(1, qual_bat['base_dismissals'])

qual_bat['press_sr'] = (qual_bat['press_runs'] / qual_bat['press_balls']) * 100
qual_bat['press_avg'] = qual_bat['press_runs'] / np.maximum(1, qual_bat['press_dismissals'])
qual_bat['press_dot_pct'] = (qual_bat['press_dots'] / qual_bat['press_raw_balls']) * 100
qual_bat['press_boundary_pct'] = ((qual_bat['press_fours'] + qual_bat['press_sixes']) / qual_bat['press_raw_balls']) * 100
qual_bat['delta_sr'] = qual_bat['press_sr'] - qual_bat['base_sr']

prior_sr = (qual_bat['press_runs'].sum() / qual_bat['press_balls'].sum()) * 100
prior_avg = qual_bat['press_runs'].sum() / qual_bat['press_dismissals'].sum()
prior_dot = (qual_bat['press_dots'].sum() / qual_bat['press_raw_balls'].sum()) * 100
prior_bound = ((qual_bat['press_fours'] + qual_bat['press_sixes']).sum() / qual_bat['press_raw_balls'].sum()) * 100

M0 = 50.0
qual_bat['shrunk_sr'] = (qual_bat['press_balls'] * qual_bat['press_sr'] + M0 * prior_sr) / (qual_bat['press_balls'] + M0)
qual_bat['shrunk_avg'] = (qual_bat['press_balls'] * qual_bat['press_avg'] + M0 * prior_avg) / (qual_bat['press_balls'] + M0)
qual_bat['shrunk_dot'] = (qual_bat['press_raw_balls'] * qual_bat['press_dot_pct'] + M0 * prior_dot) / (qual_bat['press_raw_balls'] + M0)
qual_bat['shrunk_bound'] = (qual_bat['press_raw_balls'] * qual_bat['press_boundary_pct'] + M0 * prior_bound) / (qual_bat['press_raw_balls'] + M0)

def zscore(s):
    return (s - s.mean()) / s.std()

qual_bat['z_sr'] = zscore(qual_bat['shrunk_sr'])
qual_bat['z_avg'] = zscore(qual_bat['shrunk_avg'])
qual_bat['z_dot'] = zscore(-qual_bat['shrunk_dot'])
qual_bat['z_bound'] = zscore(qual_bat['shrunk_bound'])
qual_bat['z_delta_sr'] = zscore(qual_bat['delta_sr'])

raw_bat_score = (
    0.35 * qual_bat['z_sr'] +
    0.25 * qual_bat['z_avg'] +
    0.20 * qual_bat['z_bound'] +
    0.10 * qual_bat['z_dot'] +
    0.10 * qual_bat['z_delta_sr']
)
qual_bat['brs_score'] = 50 + 15 * raw_bat_score
top_batters = qual_bat.sort_values('brs_score', ascending=False).reset_index(drop=True)

print("\n=== TOP 10 100% ELIGIBLE BATTERS ===")
for i, r in top_batters.head(10).iterrows():
    print(f"Rank {i+1}: {r['striker_name']} | BRS: {r['brs_score']:.1f} | Pressure SR: {r['press_sr']:.1f} | Avg: {r['press_avg']:.1f} | Balls: {r['press_raw_balls']}")

# ==================== BOWLER RANKINGS (ELIGIBLE ONLY) ====================
b_bowl = bball_eligible_bowl[bball_eligible_bowl['is_legal_ball_bowler']].copy()
b_bowl['is_dot'] = (b_bowl['bowler_runs_conceded'] == 0)
b_bowl['is_boundary'] = b_bowl['is_four'] | b_bowl['is_six']

bowl_base = b_bowl.groupby(['bowler_id', 'bowler_name']).agg(
    base_balls=('weighted_ball', 'sum'),
    base_raw_balls=('bowler_runs_conceded', 'count'),
    base_runs=('weighted_runs_bowl', 'sum'),
    base_wickets=('weighted_wkts_bowl', 'sum')
).reset_index()

bowl_press = b_bowl[b_bowl['is_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('weighted_ball', 'sum'),
    press_raw_balls=('bowler_runs_conceded', 'count'),
    press_runs=('weighted_runs_bowl', 'sum'),
    press_wickets=('weighted_wkts_bowl', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_boundaries=('is_boundary', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('comp_name', lambda s: (s.str.contains('IPL', case=False, na=False)).sum())
).reset_index()

bowl_df = bowl_base.merge(bowl_press, on=['bowler_id', 'bowler_name'], how='inner')
qual_bowl = bowl_df[(bowl_df['press_raw_balls'] >= 100) & (bowl_df['press_matches'] >= 8)].copy()

qual_bowl['base_econ'] = (qual_bowl['base_runs'] / (qual_bowl['base_balls'] / 6.0))
qual_bowl['press_econ'] = (qual_bowl['press_runs'] / (qual_bowl['press_balls'] / 6.0))
qual_bowl['press_avg'] = qual_bowl['press_runs'] / np.maximum(1, qual_bowl['press_wickets'])
qual_bowl['press_sr'] = qual_bowl['press_balls'] / np.maximum(1, qual_bowl['press_wickets'])
qual_bowl['press_dot_pct'] = (qual_bowl['press_dots'] / qual_bowl['press_raw_balls']) * 100
qual_bowl['press_boundary_pct'] = (qual_bowl['press_boundaries'] / qual_bowl['press_raw_balls']) * 100
qual_bowl['delta_econ'] = qual_bowl['base_econ'] - qual_bowl['press_econ']

prior_econ = (qual_bowl['press_runs'].sum() / (qual_bowl['press_balls'].sum() / 6.0))
prior_wkt_rate = qual_bowl['press_wickets'].sum() / qual_bowl['press_balls'].sum()
prior_dot_b = (qual_bowl['press_dots'].sum() / qual_bowl['press_raw_balls'].sum()) * 100
prior_bound_b = (qual_bowl['press_boundaries'].sum() / qual_bowl['press_raw_balls'].sum()) * 100

M0_b = 50.0
qual_bowl['shrunk_econ'] = (qual_bowl['press_balls'] * qual_bowl['press_econ'] + M0_b * prior_econ) / (qual_bowl['press_balls'] + M0_b)
qual_bowl['shrunk_dot'] = (qual_bowl['press_raw_balls'] * qual_bowl['press_dot_pct'] + M0_b * prior_dot_b) / (qual_bowl['press_raw_balls'] + M0_b)
qual_bowl['shrunk_bound'] = (qual_bowl['press_raw_balls'] * qual_bowl['press_boundary_pct'] + M0_b * prior_bound_b) / (qual_bowl['press_raw_balls'] + M0_b)
qual_bowl['wkt_rate'] = qual_bowl['press_wickets'] / qual_bowl['press_balls']
qual_bowl['shrunk_wkt_rate'] = (qual_bowl['press_balls'] * qual_bowl['wkt_rate'] + M0_b * prior_wkt_rate) / (qual_bowl['press_balls'] + M0_b)

qual_bowl['z_econ'] = zscore(-qual_bowl['shrunk_econ'])
qual_bowl['z_wkt'] = zscore(qual_bowl['shrunk_wkt_rate'])
qual_bowl['z_dot'] = zscore(qual_bowl['shrunk_dot'])
qual_bowl['z_bound'] = zscore(-qual_bowl['shrunk_bound'])
qual_bowl['z_delta_econ'] = zscore(qual_bowl['delta_econ'])

raw_bowl_score = (
    0.35 * qual_bowl['z_econ'] +
    0.25 * qual_bowl['z_wkt'] +
    0.20 * qual_bowl['z_dot'] +
    0.10 * qual_bowl['z_bound'] +
    0.10 * qual_bowl['z_delta_econ']
)
qual_bowl['brs_score'] = 50 + 15 * raw_bowl_score
top_bowlers = qual_bowl.sort_values('brs_score', ascending=False).reset_index(drop=True)

print("\n=== TOP 10 100% ELIGIBLE BOWLERS ===")
for i, r in top_bowlers.head(10).iterrows():
    print(f"Rank {i+1}: {r['bowler_name']} | BRS: {r['brs_score']:.1f} | Pressure Econ: {r['press_econ']:.2f} | Wkts: {r['press_wickets']} | Dots%: {r['press_dot_pct']:.1f}% | Balls: {r['press_raw_balls']}")
