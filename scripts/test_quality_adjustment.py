import pandas as pd
import numpy as np

# Load datasets
bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')
teams = pd.read_csv('DataSet/teams.csv')

# Link matches
matches = matches.merge(comps[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id', how='left')

# Define team tiers
tier1_teams = {
    'Chennai Super Kings', 'Mumbai Indians', 'Rajasthan Royals', 'Punjab Kings', 
    'Royal Challengers Bengaluru', 'Delhi Capitals', 'Kolkata Knight Riders', 
    'Sunrisers Hyderabad', 'Gujarat Titans', 'Lucknow Super Giants',
    'India', 'Australia', 'England', 'South Africa', 'New Zealand', 'Pakistan', 'West Indies'
}

tier2_teams = {
    'Sri Lanka', 'Bangladesh', 'Afghanistan', 'Ireland', 'Zimbabwe', 'Netherlands', 'Scotland', 'United States Of America'
}

def get_team_tier_weight(team_name):
    if team_name in tier1_teams:
        return 1.30
    elif team_name in tier2_teams:
        return 1.05
    else:
        return 0.75

# Map batting_team and bowling_team from matches
# For a delivery:
# batting_team_id -> look up team_name
# bowling_team_id -> look up team_name
team_id_to_name = teams.drop_duplicates('team_id').set_index('team_id')['team_name'].to_dict()

bball['batting_team_name'] = bball['batting_team_id'].map(team_id_to_name)
bball['bowling_team_name'] = bball['bowling_team_id'].map(team_id_to_name)

# For batter: difficulty comes from the bowling team quality!
bball['bowling_team_weight'] = bball['bowling_team_name'].apply(get_team_tier_weight)

# For bowler: difficulty comes from the batting team quality!
bball['batting_team_weight'] = bball['batting_team_name'].apply(get_team_tier_weight)

# Stage / Knockout multiplier
bball = bball.merge(matches[['match_id', 'comp_name', 'knock_out', 'revised_target']], on='match_id', how='left')
bball['stage_mult'] = np.where(bball['knock_out'] == 1, 1.25, 1.0)

# Sort
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# Ball runs and flags
bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0)

bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'
bball['is_bowler_wicket'] = bball['is_wicket'] & (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) & bball['dismissal_type'].notna()

# Running totals
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

# Weight deliveries
# For batters:
bball['bat_ball_wt'] = bball['bowling_team_weight']
bball['bat_runs_wt'] = bball['runs'] * bball['bowling_team_weight']

# For bowlers:
bball['bowl_ball_wt'] = bball['batting_team_weight']
bball['bowl_runs_wt'] = bball['bowler_runs_conceded'] * bball['batting_team_weight']
bball['bowl_wkts_wt'] = bball['is_bowler_wicket'] * bball['batting_team_weight']

# ================= BATTERS =================
b_bat = bball[bball['is_legal_ball_batter']].copy()
b_bat['is_dot'] = (b_bat['runs'] == 0) & (b_bat['extras1_runs'] == 0)

bat_base = b_bat.groupby(['striker_id', 'striker_name']).agg(
    base_balls_wt=('bat_ball_wt', 'sum'),
    base_raw_balls=('runs', 'count'),
    base_runs_wt=('bat_runs_wt', 'sum'),
    base_dismissals=('is_wicket', 'sum')
).reset_index()

bat_press = b_bat[b_bat['is_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls_wt=('bat_ball_wt', 'sum'),
    press_raw_balls=('runs', 'count'),
    press_runs_wt=('bat_runs_wt', 'sum'),
    press_dismissals=('is_wicket', 'sum'),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('comp_name', lambda s: (s.str.contains('IPL', case=False, na=False)).sum())
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

prior_sr = (qual_bat['press_runs_wt'].sum() / qual_bat['press_balls_wt'].sum()) * 100
prior_avg = qual_bat['press_runs_wt'].sum() / qual_bat['press_dismissals'].sum()
prior_dot = (qual_bat['press_dots'].sum() / qual_bat['press_raw_balls'].sum()) * 100
prior_bound = ((qual_bat['press_fours'] + qual_bat['press_sixes']).sum() / qual_bat['press_raw_balls'].sum()) * 100

M0 = 60.0
qual_bat['shrunk_sr'] = (qual_bat['press_balls_wt'] * qual_bat['press_sr'] + M0 * prior_sr) / (qual_bat['press_balls_wt'] + M0)
qual_bat['shrunk_avg'] = (qual_bat['press_balls_wt'] * qual_bat['press_avg'] + M0 * prior_avg) / (qual_bat['press_balls_wt'] + M0)
qual_bat['shrunk_dot'] = (qual_bat['press_raw_balls'] * qual_bat['press_dot_pct'] + M0 * prior_dot) / (qual_bat['press_raw_balls'] + M0)
qual_bat['shrunk_bound'] = (qual_bat['press_raw_balls'] * qual_bat['press_boundary_pct'] + M0 * prior_bound) / (qual_bat['press_raw_balls'] + M0)

def zscore(s):
    return (s - s.mean()) / s.std()

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
qual_bat['brs_score'] = 50 + 15 * raw_bat

print("=== REFINED TOP 15 BATTERS (WITH OPPOSITION ADJUSTMENT) ===")
top_bat = qual_bat.sort_values('brs_score', ascending=False).reset_index(drop=True)
print(top_bat[['striker_name', 'press_raw_balls', 'press_sr', 'press_avg', 'delta_sr', 'press_boundary_pct', 'brs_score']].head(15).to_string())

# ================= BOWLERS =================
b_bowl = bball[bball['is_legal_ball_bowler']].copy()
b_bowl['is_dot'] = (b_bowl['bowler_runs_conceded'] == 0)
b_bowl['is_boundary'] = b_bowl['is_four'] | b_bowl['is_six']

bowl_base = b_bowl.groupby(['bowler_id', 'bowler_name']).agg(
    base_balls_wt=('bowl_ball_wt', 'sum'),
    base_raw_balls=('bowler_runs_conceded', 'count'),
    base_runs_wt=('bowl_runs_wt', 'sum'),
    base_wkts_wt=('bowl_wkts_wt', 'sum')
).reset_index()

bowl_press = b_bowl[b_bowl['is_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls_wt=('bowl_ball_wt', 'sum'),
    press_raw_balls=('bowler_runs_conceded', 'count'),
    press_runs_wt=('bowl_runs_wt', 'sum'),
    press_wkts_wt=('bowl_wkts_wt', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_boundaries=('is_boundary', 'sum'),
    press_matches=('match_id', 'nunique'),
    ipl_balls=('comp_name', lambda s: (s.str.contains('IPL', case=False, na=False)).sum())
).reset_index()

bowl_df = bowl_base.merge(bowl_press, on=['bowler_id', 'bowler_name'], how='inner')
qual_bowl = bowl_df[(bowl_df['press_raw_balls'] >= 100) & (bowl_df['press_matches'] >= 8)].copy()

qual_bowl['base_econ'] = (qual_bowl['base_runs_wt'] / (qual_bowl['base_balls_wt'] / 6.0))
qual_bowl['press_econ'] = (qual_bowl['press_runs_wt'] / (qual_bowl['press_balls_wt'] / 6.0))
qual_bowl['press_avg'] = qual_bowl['press_runs_wt'] / np.maximum(1, qual_bowl['press_wkts_wt'])
qual_bowl['press_sr'] = qual_bowl['press_balls_wt'] / np.maximum(1, qual_bowl['press_wkts_wt'])
qual_bowl['press_dot_pct'] = (qual_bowl['press_dots'] / qual_bowl['press_raw_balls']) * 100
qual_bowl['press_boundary_pct'] = (qual_bowl['press_boundaries'] / qual_bowl['press_raw_balls']) * 100
qual_bowl['delta_econ'] = qual_bowl['base_econ'] - qual_bowl['press_econ']

prior_econ = (qual_bowl['press_runs_wt'].sum() / (qual_bowl['press_balls_wt'].sum() / 6.0))
prior_wkt_rate = qual_bowl['press_wkts_wt'].sum() / qual_bowl['press_balls_wt'].sum()
prior_dot_b = (qual_bowl['press_dots'].sum() / qual_bowl['press_raw_balls'].sum()) * 100
prior_bound_b = (qual_bowl['press_boundaries'].sum() / qual_bowl['press_raw_balls'].sum()) * 100

M0_b = 60.0
qual_bowl['shrunk_econ'] = (qual_bowl['press_balls_wt'] * qual_bowl['press_econ'] + M0_b * prior_econ) / (qual_bowl['press_balls_wt'] + M0_b)
qual_bowl['shrunk_dot'] = (qual_bowl['press_raw_balls'] * qual_bowl['press_dot_pct'] + M0_b * prior_dot_b) / (qual_bowl['press_raw_balls'] + M0_b)
qual_bowl['shrunk_bound'] = (qual_bowl['press_raw_balls'] * qual_bowl['press_boundary_pct'] + M0_b * prior_bound_b) / (qual_bowl['press_raw_balls'] + M0_b)
qual_bowl['wkt_rate'] = qual_bowl['press_wkts_wt'] / qual_bowl['press_balls_wt']
qual_bowl['shrunk_wkt_rate'] = (qual_bowl['press_balls_wt'] * qual_bowl['wkt_rate'] + M0_b * prior_wkt_rate) / (qual_bowl['press_balls_wt'] + M0_b)

qual_bowl['z_econ'] = zscore(-qual_bowl['shrunk_econ'])
qual_bowl['z_wkt'] = zscore(qual_bowl['shrunk_wkt_rate'])
qual_bowl['z_dot'] = zscore(qual_bowl['shrunk_dot'])
qual_bowl['z_bound'] = zscore(-qual_bowl['shrunk_bound'])
qual_bowl['z_delta_econ'] = zscore(qual_bowl['delta_econ'])

raw_bowl = (
    0.35 * qual_bowl['z_econ'] +
    0.25 * qual_bowl['z_wkt'] +
    0.20 * qual_bowl['z_dot'] +
    0.10 * qual_bowl['z_bound'] +
    0.10 * qual_bowl['z_delta_econ']
)
qual_bowl['brs_score'] = 50 + 15 * raw_bowl

print("\n=== REFINED TOP 15 BOWLERS (WITH OPPOSITION ADJUSTMENT) ===")
top_bowl = qual_bowl.sort_values('brs_score', ascending=False).reset_index(drop=True)
print(top_bowl[['bowler_name', 'press_raw_balls', 'press_econ', 'press_dot_pct', 'press_boundary_pct', 'delta_econ', 'brs_score']].head(15).to_string())
