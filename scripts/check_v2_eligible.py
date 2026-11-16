import pandas as pd
import numpy as np

# Load datasets
bball = pd.read_csv('DataSet/ball_by_ball.csv', low_memory=False)
matches = pd.read_csv('DataSet/matches.csv', low_memory=False)
comps = pd.read_csv('DataSet/competitions.csv', low_memory=False)
teams = pd.read_csv('DataSet/teams.csv', low_memory=False)
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv', low_memory=False)

# Link matches
matches = matches.merge(comps[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id', how='left')

# Exclude Pakistan / Pakistan A
pak_players = set(mapping[mapping['team_name'].isin(['Pakistan', 'Pakistan A'])]['player_id'].unique())
print(f"Total PCB-registered players excluded: {len(pak_players)}")

# Team tiers
TIER_1A_TEAMS = {
    'Chennai Super Kings', 'Mumbai Indians', 'Rajasthan Royals', 'Punjab Kings',
    'Royal Challengers Bengaluru', 'Delhi Capitals', 'Kolkata Knight Riders',
    'Sunrisers Hyderabad', 'Gujarat Titans', 'Lucknow Super Giants'
}
TIER_1_NATIONS = {
    'India', 'Australia', 'England', 'South Africa', 'New Zealand', 'West Indies'
}
TIER_2_NATIONS = {
    'Sri Lanka', 'Bangladesh', 'Afghanistan', 'Ireland', 'Zimbabwe',
    'Netherlands', 'Scotland', 'United States Of America'
}

def get_tier_weight(team_name):
    if team_name in TIER_1A_TEAMS:
        return 1.35
    elif team_name in TIER_1_NATIONS:
        return 1.20
    elif team_name in TIER_2_NATIONS:
        return 1.00
    else:
        return 0.65

def is_tier1_opposition(team_name):
    return team_name in TIER_1A_TEAMS or team_name in TIER_1_NATIONS

team_id_to_name = teams.drop_duplicates('team_id').set_index('team_id')['team_name'].to_dict()
bball['batting_team_name'] = bball['batting_team_id'].map(team_id_to_name)
bball['bowling_team_name'] = bball['bowling_team_id'].map(team_id_to_name)

bball['bowling_team_weight'] = bball['bowling_team_name'].apply(get_tier_weight)
bball['batting_team_weight'] = bball['batting_team_name'].apply(get_tier_weight)

bball['vs_tier1_bat'] = bball['bowling_team_name'].apply(is_tier1_opposition)
bball['vs_tier1_bowl'] = bball['batting_team_name'].apply(is_tier1_opposition)

bball = bball.merge(
    matches[['match_id', 'comp_name', 'knock_out', 'revised_target', 'stage']],
    on='match_id', how='left'
)
bball['stage_mult'] = np.where(bball['knock_out'] == 1, 1.25, 1.0)
bball['is_ipl_ball'] = bball['comp_name'].str.contains('IPL', case=False, na=False)

# UPSTREAM EXCLUSION
bball = bball[~bball['striker_id'].isin(pak_players) & ~bball['bowler_id'].isin(pak_players)].copy()

# Sort & calculate
bball = bball.sort_values(['match_id', 'innings', 'innings_ball_num']).reset_index(drop=True)
bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(
    bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0
)

bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'
bball['is_dot'] = (bball['runs'] == 0) & (bball['extras1_runs'] == 0)
bball['is_bowler_wicket'] = (
    bball['is_wicket'] &
    (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) &
    bball['dismissal_type'].notna()
)

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

rrr = bball['current_rrr'].fillna(8.0)
stage_factor = 1.0 + (120 - bball['balls_remaining']) / 120.0
wkt_factor = 1.0 + (10 - bball['wickets_in_hand']) * 0.1

inn2_p = (2.5 + 3.0 * ((rrr - 6.0) / 6.0)) * stage_factor * (wkt_factor / 1.2) * bball['stage_mult']
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
) * bball['stage_mult']
inn1_p = np.clip(inn1_p, 1.0, 10.0)

bball['pressure_index'] = np.where(
    bball['innings'].isin([3, 4]), 10.0,
    np.where(bball['innings'] == 2, inn2_p, inn1_p)
)
bball['is_pressure'] = bball['pressure_index'] >= 6.5

bball['bat_ball_wt'] = bball['bowling_team_weight']
bball['bat_runs_wt'] = bball['runs'] * bball['bowling_team_weight']
bball['bowl_ball_wt'] = bball['batting_team_weight']
bball['bowl_runs_wt'] = bball['bowler_runs_conceded'] * bball['batting_team_weight']
bball['bowl_wkts_wt'] = bball['is_bowler_wicket'] * bball['batting_team_weight']

# Batters
b_bat = bball[bball['is_legal_ball_batter']].copy()
b_bat['is_dot'] = (b_bat['runs'] == 0) & (b_bat['extras1_runs'] == 0)
b_bat['is_boundary'] = b_bat['is_four'] | b_bat['is_six']

bat_base = b_bat.groupby(['striker_id', 'striker_name']).agg(
    base_balls_wt=('bat_ball_wt', 'sum'),
    base_raw_balls=('runs', 'count'),
    base_runs_wt=('bat_runs_wt', 'sum'),
    base_raw_runs=('runs', 'sum'),
    base_dismissals=('is_wicket', 'sum'),
).reset_index()

bat_press = b_bat[b_bat['is_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls_wt=('bat_ball_wt', 'sum'),
    press_raw_balls=('runs', 'count'),
    press_runs_wt=('bat_runs_wt', 'sum'),
    press_raw_runs=('runs', 'sum'),
    press_dismissals=('is_wicket', 'sum'),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('is_ipl_ball', 'sum'),
    tier1_balls=('vs_tier1_bat', 'sum'),
).reset_index()

bat_df = bat_base.merge(bat_press, on=['striker_id', 'striker_name'], how='inner')
qual_bat = bat_df[(bat_df['press_raw_balls'] >= 100) & (bat_df['press_matches'] >= 8)].copy()

qual_bat['base_sr'] = (qual_bat['base_runs_wt'] / qual_bat['base_balls_wt']) * 100
qual_bat['base_avg'] = qual_bat['base_runs_wt'] / np.maximum(1, qual_bat['base_dismissals'])
qual_bat['press_sr'] = (qual_bat['press_runs_wt'] / qual_bat['press_balls_wt']) * 100
qual_bat['press_avg'] = qual_bat['press_runs_wt'] / np.maximum(1, qual_bat['press_dismissals'])
qual_bat['press_dot_pct'] = (qual_bat['press_dots'] / qual_bat['press_raw_balls']) * 100
qual_bat['press_boundary_pct'] = ((qual_bat['press_fours'] + qual_bat['press_sixes']) / qual_bat['press_raw_balls']) * 100
qual_bat['delta_sr'] = qual_bat['press_sr'] - qual_bat['base_sr']

def tag_batter_pool(row):
    if row['ipl_balls'] >= 100:
        return 'IPL_VERIFIED'
    elif row['ipl_balls'] >= 20:
        return 'IPL_PARTIAL'
    elif row['tier1_balls'] >= 50:
        return 'INTERNATIONAL'
    else:
        return 'EMERGING'

qual_bat['pool'] = qual_bat.apply(tag_batter_pool, axis=1)

ipl_bat = qual_bat[qual_bat['ipl_balls'] >= 50]
prior_sr  = (ipl_bat['press_runs_wt'].sum() / ipl_bat['press_balls_wt'].sum()) * 100
prior_avg = ipl_bat['press_runs_wt'].sum() / ipl_bat['press_dismissals'].sum()
prior_dot = (ipl_bat['press_dots'].sum() / ipl_bat['press_raw_balls'].sum()) * 100
prior_bound = ((ipl_bat['press_fours'] + ipl_bat['press_sixes']).sum() / ipl_bat['press_raw_balls'].sum()) * 100

M0 = 60.0
qual_bat['shrunk_sr'] = (qual_bat['press_balls_wt'] * qual_bat['press_sr'] + M0 * prior_sr) / (qual_bat['press_balls_wt'] + M0)
qual_bat['shrunk_avg'] = (qual_bat['press_balls_wt'] * qual_bat['press_avg'] + M0 * prior_avg) / (qual_bat['press_balls_wt'] + M0)
qual_bat['shrunk_dot'] = (qual_bat['press_raw_balls'] * qual_bat['press_dot_pct'] + M0 * prior_dot) / (qual_bat['press_raw_balls'] + M0)
qual_bat['shrunk_bound'] = (qual_bat['press_raw_balls'] * qual_bat['press_boundary_pct'] + M0 * prior_bound) / (qual_bat['press_raw_balls'] + M0)

def zscore(s):
    std = s.std()
    return (s - s.mean()) / std if std > 0 else s * 0

qual_bat['z_sr'] = zscore(qual_bat['shrunk_sr'])
qual_bat['z_avg'] = zscore(qual_bat['shrunk_avg'])
qual_bat['z_dot'] = zscore(-qual_bat['shrunk_dot'])
qual_bat['z_bound'] = zscore(qual_bat['shrunk_bound'])
qual_bat['z_delta_sr'] = zscore(qual_bat['delta_sr'])

raw_bat = (
    0.35 * qual_bat['z_sr'] +
    0.25 * qual_bat['z_avg'] +
    0.20 * qual_bat['z_bound'] +
    0.10 * qual_bat['z_dot'] +
    0.10 * qual_bat['z_delta_sr']
)
qual_bat['brs_score'] = np.round(50 + 15 * raw_bat, 2)
# Exclude emerging from top 10 list
qual_bat_top = qual_bat[qual_bat['pool'] != 'EMERGING'].sort_values('brs_score', ascending=False).reset_index(drop=True)
qual_bat_top['global_rank'] = qual_bat_top.index + 1

print("=== TOP 12 QUALIFIED ELIGIBLE BATTERS ===")
for idx, r in qual_bat_top.head(12).iterrows():
    print(f"#{r['global_rank']} {r['striker_name']} ({r['pool']}) | BRS: {r['brs_score']} | Press SR: {r['press_sr']:.1f} | Avg: {r['press_avg']:.1f} | Balls: {r['press_raw_balls']}")

# Bowlers
b_bowl = bball[bball['is_legal_ball_bowler']].copy()
b_bowl['is_dot'] = (b_bowl['bowler_runs_conceded'] == 0)
b_bowl['is_boundary'] = b_bowl['is_four'] | b_bowl['is_six']

bowl_base = b_bowl.groupby(['bowler_id', 'bowler_name']).agg(
    base_balls_wt=('bowl_ball_wt', 'sum'),
    base_raw_balls=('bowler_runs_conceded', 'count'),
    base_runs_wt=('bowl_runs_wt', 'sum'),
    base_raw_runs=('bowler_runs_conceded', 'sum'),
    base_wkts_wt=('bowl_wkts_wt', 'sum'),
    base_raw_wkts=('is_bowler_wicket', 'sum')
).reset_index()

bowl_press = b_bowl[b_bowl['is_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls_wt=('bowl_ball_wt', 'sum'),
    press_raw_balls=('bowler_runs_conceded', 'count'),
    press_runs_wt=('bowl_runs_wt', 'sum'),
    press_raw_runs=('bowler_runs_conceded', 'sum'),
    press_wkts_wt=('bowl_wkts_wt', 'sum'),
    press_raw_wkts=('is_bowler_wicket', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_boundaries=('is_boundary', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('is_ipl_ball', 'sum'),
    tier1_balls=('vs_tier1_bowl', 'sum'),
).reset_index()

bowl_df = bowl_base.merge(bowl_press, on=['bowler_id', 'bowler_name'], how='inner')
qual_bowl_all = bowl_df[(bowl_df['press_raw_balls'] >= 100) & (bowl_df['press_matches'] >= 8)].copy()

qual_bowl_all['base_econ'] = qual_bowl_all['base_runs_wt'] / (qual_bowl_all['base_balls_wt'] / 6.0)
qual_bowl_all['press_econ'] = qual_bowl_all['press_runs_wt'] / (qual_bowl_all['press_balls_wt'] / 6.0)
qual_bowl_all['press_avg'] = qual_bowl_all['press_runs_wt'] / np.maximum(1, qual_bowl_all['press_wkts_wt'])
qual_bowl_all['press_sr_bowl'] = qual_bowl_all['press_balls_wt'] / np.maximum(1, qual_bowl_all['press_wkts_wt'])
qual_bowl_all['press_dot_pct'] = (qual_bowl_all['press_dots'] / qual_bowl_all['press_raw_balls']) * 100
qual_bowl_all['press_boundary_pct'] = (qual_bowl_all['press_boundaries'] / qual_bowl_all['press_raw_balls']) * 100
qual_bowl_all['delta_econ'] = qual_bowl_all['base_econ'] - qual_bowl_all['press_econ']

def tag_bowler_pool(row):
    if row['ipl_balls'] >= 100:
        return 'IPL_VERIFIED'
    elif row['ipl_balls'] >= 20:
        return 'IPL_PARTIAL'
    elif row['tier1_balls'] >= 50:
        return 'INTERNATIONAL'
    else:
        return 'EMERGING'

qual_bowl_all['pool'] = qual_bowl_all.apply(tag_bowler_pool, axis=1)

ipl_bowl = qual_bowl_all[qual_bowl_all['ipl_balls'] >= 50]
prior_econ = ipl_bowl['press_runs_wt'].sum() / (ipl_bowl['press_balls_wt'].sum() / 6.0)
prior_wkt_rate = ipl_bowl['press_wkts_wt'].sum() / ipl_bowl['press_balls_wt'].sum()
prior_dot_b = (ipl_bowl['press_dots'].sum() / ipl_bowl['press_raw_balls'].sum()) * 100
prior_bound_b = (ipl_bowl['press_boundaries'].sum() / ipl_bowl['press_raw_balls'].sum()) * 100

M0_b = 60.0
qual_bowl_all['shrunk_econ'] = (qual_bowl_all['press_balls_wt'] * qual_bowl_all['press_econ'] + M0_b * prior_econ) / (qual_bowl_all['press_balls_wt'] + M0_b)
qual_bowl_all['shrunk_dot'] = (qual_bowl_all['press_raw_balls'] * qual_bowl_all['press_dot_pct'] + M0_b * prior_dot_b) / (qual_bowl_all['press_raw_balls'] + M0_b)
qual_bowl_all['shrunk_bound'] = (qual_bowl_all['press_raw_balls'] * qual_bowl_all['press_boundary_pct'] + M0_b * prior_bound_b) / (qual_bowl_all['press_raw_balls'] + M0_b)
qual_bowl_all['wkt_rate'] = qual_bowl_all['press_wkts_wt'] / qual_bowl_all['press_balls_wt']
qual_bowl_all['shrunk_wkt_rate'] = (qual_bowl_all['press_balls_wt'] * qual_bowl_all['wkt_rate'] + M0_b * prior_wkt_rate) / (qual_bowl_all['press_balls_wt'] + M0_b)

qual_bowl_all['z_econ'] = zscore(-qual_bowl_all['shrunk_econ'])
qual_bowl_all['z_wkt'] = zscore(qual_bowl_all['shrunk_wkt_rate'])
qual_bowl_all['z_dot'] = zscore(qual_bowl_all['shrunk_dot'])
qual_bowl_all['z_bound'] = zscore(-qual_bowl_all['shrunk_bound'])
qual_bowl_all['z_delta_econ'] = zscore(qual_bowl_all['delta_econ'])

raw_bowl = (
    0.35 * qual_bowl_all['z_econ'] +
    0.25 * qual_bowl_all['z_wkt'] +
    0.20 * qual_bowl_all['z_dot'] +
    0.10 * qual_bowl_all['z_bound'] +
    0.10 * qual_bowl_all['z_delta_econ']
)
qual_bowl_all['brs_score'] = np.round(50 + 15 * raw_bowl, 2)
qual_bowl = qual_bowl_all[qual_bowl_all['pool'] != 'EMERGING'].sort_values('brs_score', ascending=False).reset_index(drop=True)
qual_bowl['global_rank'] = qual_bowl.index + 1

print("\n=== TOP 12 QUALIFIED ELIGIBLE BOWLERS ===")
for idx, r in qual_bowl.head(12).iterrows():
    print(f"#{r['global_rank']} {r['bowler_name']} ({r['pool']}) | BRS: {r['brs_score']} | Press Econ: {r['press_econ']:.2f} | Wkts: {r['press_raw_wkts']} | Dots%: {r['press_dot_pct']:.1f}% | Balls: {r['press_raw_balls']}")
