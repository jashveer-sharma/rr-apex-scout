import pandas as pd
import numpy as np

# Load preprocessed / run calibration
bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')

# Sort
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# Merge matches
matches_subset = matches[['match_id', 'comp_id', 'knock_out', 'revised_target', 'win_team_id', 'stage']]
bball = bball.merge(matches_subset, on='match_id', how='left')

# Ball runs and bowler runs
bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0)

bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'
bball['is_bowler_wicket'] = bball['is_wicket'] & (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) & bball['dismissal_type'].notna()

# Cumulative stats
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

# Vectorized pressure calculation for speed
# Innings 2 pressure
rrr = bball['current_rrr'].fillna(8.0)
stage_factor = 1.0 + (120 - bball['balls_remaining']) / 120.0
wkt_factor = 1.0 + (10 - bball['wickets_in_hand']) * 0.1
knockout_mult = np.where(bball['knock_out'] == 1, 1.2, 1.0)

inn2_p = (2.5 + 3.0 * ((rrr - 6.0) / 6.0)) * stage_factor * (wkt_factor / 1.2)
inn2_p = np.clip(inn2_p * knockout_mult, 1.0, 10.0)

# Innings 1 pressure
over = bball['overid']
wkts = bball['wickets_in_hand']
inn1_p = np.where(
    over <= 6,
    3.0 + np.maximum(0, 8 - wkts) * 1.5,
    np.where(
        over <= 15,
        4.0 + np.maximum(0, 6 - wkts) * 1.2 + np.where(bball['current_crr'] < 7.0, 1.0, 0.0),
        6.5 + (over - 16) * 0.7 + np.where(wkts <= 4, 1.0, 0.0)
    )
)
inn1_p = np.clip(inn1_p * knockout_mult, 1.0, 10.0)

# Combine
bball['pressure_index'] = np.where(
    bball['innings'].isin([3, 4]), 10.0,
    np.where(bball['innings'] == 2, inn2_p, inn1_p)
)

bball['is_high_pressure'] = bball['pressure_index'] >= 6.5

print(f"High pressure deliveries: {bball['is_high_pressure'].sum()} / {len(bball)} ({bball['is_high_pressure'].mean()*100:.1f}%)")

# Save processed checkpoint or compute player aggregates directly
# BATTERS ANALYSIS
print("\n--- AGGREGATING BATTERS ---")
# Only legal balls for batters
b_legal = bball[bball['is_legal_ball_batter']].copy()
b_legal['is_dot'] = (b_legal['runs'] == 0) & (b_legal['extras1_runs'] == 0)
b_legal['is_boundary'] = b_legal['is_four'] | b_legal['is_six']

# All balls by batter
bat_total = b_legal.groupby(['striker_id', 'striker_name']).agg(
    total_balls=('runs', 'count'),
    total_runs=('runs', 'sum'),
    total_dismissals=('is_wicket', 'sum'),
    total_fours=('is_four', 'sum'),
    total_sixes=('is_six', 'sum'),
    total_dots=('is_dot', 'sum')
).reset_index()

# High pressure balls by batter
bat_press = b_legal[b_legal['is_high_pressure']].groupby(['striker_id', 'striker_name']).agg(
    press_balls=('runs', 'count'),
    press_runs=('runs', 'sum'),
    press_dismissals=('is_wicket', 'sum'),
    press_fours=('is_four', 'sum'),
    press_sixes=('is_six', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_matches=('match_id', 'nunique')
).reset_index()

bat_df = bat_total.merge(bat_press, on=['striker_id', 'striker_name'], how='left').fillna(0)

# Filter minimum sample size for reliability: e.g. at least 60 balls faced in high pressure
print(f"Total batters: {len(bat_df)}")
qualified_batters = bat_df[bat_df['press_balls'] >= 60].copy()
print(f"Batters with >= 60 pressure balls: {len(qualified_batters)}")

# Calculate baseline and pressure rates
qualified_batters['base_sr'] = (qualified_batters['total_runs'] / qualified_batters['total_balls']) * 100
qualified_batters['base_avg'] = qualified_batters['total_runs'] / np.maximum(1, qualified_batters['total_dismissals'])

qualified_batters['press_sr'] = (qualified_batters['press_runs'] / qualified_batters['press_balls']) * 100
qualified_batters['press_avg'] = qualified_batters['press_runs'] / np.maximum(1, qualified_batters['press_dismissals'])
qualified_batters['press_dot_pct'] = (qualified_batters['press_dots'] / qualified_batters['press_balls']) * 100
qualified_batters['press_boundary_pct'] = ((qualified_batters['press_fours'] + qualified_batters['press_sixes']) / qualified_batters['press_balls']) * 100

qualified_batters['delta_sr'] = qualified_batters['press_sr'] - qualified_batters['base_sr']
qualified_batters['delta_avg'] = qualified_batters['press_avg'] - qualified_batters['base_avg']

# Population priors for Empirical Bayes
pop_sr = (qualified_batters['press_runs'].sum() / qualified_batters['press_balls'].sum()) * 100
pop_avg = qualified_batters['press_runs'].sum() / np.maximum(1, qualified_batters['press_dismissals'].sum())
pop_dot = (qualified_batters['press_dots'].sum() / qualified_batters['press_balls'].sum()) * 100
pop_bound = ((qualified_batters['press_fours'] + qualified_batters['press_sixes']).sum() / qualified_batters['press_balls'].sum()) * 100

print(f"Population Pressure Priors: SR={pop_sr:.1f}, Avg={pop_avg:.1f}, Dot%={pop_dot:.1f}%, Boundary%={pop_bound:.1f}%")

# Empirical Bayes Shrinkage (M0 = 40 balls prior)
M0_bat = 40.0
qualified_batters['shrunk_sr'] = (qualified_batters['press_balls'] * qualified_batters['press_sr'] + M0_bat * pop_sr) / (qualified_batters['press_balls'] + M0_bat)
qualified_batters['shrunk_avg'] = (qualified_batters['press_balls'] * qualified_batters['press_avg'] + M0_bat * pop_avg) / (qualified_batters['press_balls'] + M0_bat)
qualified_batters['shrunk_dot'] = (qualified_batters['press_balls'] * qualified_batters['press_dot_pct'] + M0_bat * pop_dot) / (qualified_batters['press_balls'] + M0_bat)
qualified_batters['shrunk_bound'] = (qualified_batters['press_balls'] * qualified_batters['press_boundary_pct'] + M0_bat * pop_bound) / (qualified_batters['press_balls'] + M0_bat)

# Z-score normalization helper
def zscore(s):
    return (s - s.mean()) / s.std()

qualified_batters['z_sr'] = zscore(qualified_batters['shrunk_sr'])
qualified_batters['z_avg'] = zscore(qualified_batters['shrunk_avg'])
qualified_batters['z_dot'] = zscore(-qualified_batters['shrunk_dot']) # lower dot is better
qualified_batters['z_bound'] = zscore(qualified_batters['shrunk_bound'])
qualified_batters['z_delta_sr'] = zscore(qualified_batters['delta_sr'])

# Batting Reliability Score (BRS) composite
# Scale 0 to 100
raw_score_bat = (
    0.30 * qualified_batters['z_sr'] +
    0.25 * qualified_batters['z_avg'] +
    0.20 * qualified_batters['z_bound'] +
    0.15 * qualified_batters['z_dot'] +
    0.10 * qualified_batters['z_delta_sr']
)
qualified_batters['brs_score'] = 50 + 15 * raw_score_bat

print("\n--- TOP 15 CANDIDATE BATTERS UNDER PRESSURE ---")
top_batters = qualified_batters.sort_values('brs_score', ascending=False).head(15)
print(top_batters[['striker_name', 'press_balls', 'press_runs', 'press_sr', 'press_avg', 'delta_sr', 'press_boundary_pct', 'brs_score']])

# BOWLERS ANALYSIS
print("\n--- AGGREGATING BOWLERS ---")
# Only legal balls for bowlers count towards balls/overs, but runs include extras conceded
b_bowl_legal = bball[bball['is_legal_ball_bowler']].copy()
b_bowl_legal['is_dot'] = (b_bowl_legal['bowler_runs_conceded'] == 0)
b_bowl_legal['is_boundary'] = b_bowl_legal['is_four'] | b_bowl_legal['is_six']

bowl_total = b_bowl_legal.groupby(['bowler_id', 'bowler_name']).agg(
    total_balls=('bowler_runs_conceded', 'count'),
    total_runs=('bowler_runs_conceded', 'sum'),
    total_wickets=('is_bowler_wicket', 'sum'),
    total_dots=('is_dot', 'sum'),
    total_boundaries=('is_boundary', 'sum')
).reset_index()

bowl_press = b_bowl_legal[b_bowl_legal['is_high_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
    press_balls=('bowler_runs_conceded', 'count'),
    press_runs=('bowler_runs_conceded', 'sum'),
    press_wickets=('is_bowler_wicket', 'sum'),
    press_dots=('is_dot', 'sum'),
    press_boundaries=('is_boundary', 'sum'),
    press_matches=('match_id', 'nunique')
).reset_index()

bowl_df = bowl_total.merge(bowl_press, on=['bowler_id', 'bowler_name'], how='left').fillna(0)
print(f"Total bowlers: {len(bowl_df)}")
qualified_bowlers = bowl_df[bowl_df['press_balls'] >= 60].copy()
print(f"Bowlers with >= 60 pressure balls (10 overs): {len(qualified_bowlers)}")

qualified_bowlers['base_econ'] = (qualified_bowlers['total_runs'] / (qualified_bowlers['total_balls'] / 6.0))
qualified_bowlers['base_sr'] = qualified_bowlers['total_balls'] / np.maximum(1, qualified_bowlers['total_wickets'])

qualified_bowlers['press_econ'] = (qualified_bowlers['press_runs'] / (qualified_bowlers['press_balls'] / 6.0))
qualified_bowlers['press_avg'] = qualified_bowlers['press_runs'] / np.maximum(1, qualified_bowlers['press_wickets'])
qualified_bowlers['press_sr'] = qualified_bowlers['press_balls'] / np.maximum(1, qualified_bowlers['press_wickets'])
qualified_bowlers['press_dot_pct'] = (qualified_bowlers['press_dots'] / qualified_bowlers['press_balls']) * 100
qualified_bowlers['press_boundary_pct'] = (qualified_bowlers['press_boundaries'] / qualified_bowlers['press_balls']) * 100

qualified_bowlers['delta_econ'] = qualified_bowlers['base_econ'] - qualified_bowlers['press_econ'] # positive is better!

pop_econ = (qualified_bowlers['press_runs'].sum() / (qualified_bowlers['press_balls'].sum() / 6.0))
pop_wkt_rate = qualified_bowlers['press_wickets'].sum() / qualified_bowlers['press_balls'].sum()
pop_dot_bowl = (qualified_bowlers['press_dots'].sum() / qualified_bowlers['press_balls'].sum()) * 100
pop_bound_bowl = (qualified_bowlers['press_boundaries'].sum() / qualified_bowlers['press_balls'].sum()) * 100

print(f"Population Pressure Priors (Bowler): Econ={pop_econ:.2f}, Dot%={pop_dot_bowl:.1f}%, Boundary%={pop_bound_bowl:.1f}%")

M0_bowl = 40.0
qualified_bowlers['shrunk_econ'] = (qualified_bowlers['press_balls'] * qualified_bowlers['press_econ'] + M0_bowl * pop_econ) / (qualified_bowlers['press_balls'] + M0_bowl)
qualified_bowlers['shrunk_dot'] = (qualified_bowlers['press_balls'] * qualified_bowlers['press_dot_pct'] + M0_bowl * pop_dot_bowl) / (qualified_bowlers['press_balls'] + M0_bowl)
qualified_bowlers['shrunk_bound'] = (qualified_bowlers['press_balls'] * qualified_bowlers['press_boundary_pct'] + M0_bowl * pop_bound_bowl) / (qualified_bowlers['press_balls'] + M0_bowl)
qualified_bowlers['wkt_per_ball'] = qualified_bowlers['press_wickets'] / qualified_bowlers['press_balls']
qualified_bowlers['shrunk_wkt_rate'] = (qualified_bowlers['press_balls'] * qualified_bowlers['wkt_per_ball'] + M0_bowl * pop_wkt_rate) / (qualified_bowlers['press_balls'] + M0_bowl)

qualified_bowlers['z_econ'] = zscore(-qualified_bowlers['shrunk_econ']) # lower econ is better
qualified_bowlers['z_wkt'] = zscore(qualified_bowlers['shrunk_wkt_rate'])
qualified_bowlers['z_dot'] = zscore(qualified_bowlers['shrunk_dot']) # higher dot is better
qualified_bowlers['z_bound'] = zscore(-qualified_bowlers['shrunk_bound']) # lower boundary is better
qualified_bowlers['z_delta_econ'] = zscore(qualified_bowlers['delta_econ'])

raw_score_bowl = (
    0.30 * qualified_bowlers['z_econ'] +
    0.25 * qualified_bowlers['z_wkt'] +
    0.20 * qualified_bowlers['z_dot'] +
    0.15 * qualified_bowlers['z_bound'] +
    0.10 * qualified_bowlers['z_delta_econ']
)
qualified_bowlers['brs_score'] = 50 + 15 * raw_score_bowl

print("\n--- TOP 15 CANDIDATE BOWLERS UNDER PRESSURE ---")
top_bowlers = qualified_bowlers.sort_values('brs_score', ascending=False).head(15)
print(top_bowlers[['bowler_name', 'press_balls', 'press_runs', 'press_wickets', 'press_econ', 'press_dot_pct', 'delta_econ', 'brs_score']])
