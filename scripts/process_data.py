import pandas as pd
import numpy as np

print("Loading datasets...")
bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')

print(f"Loaded {len(bball)} deliveries, {len(matches)} matches.")

# Sort chronologically and by match/innings/ball
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# Merge match context
matches_subset = matches[['match_id', 'comp_id', 'knock_out', 'revised_target', 'win_team_id', 'stage']]
bball = bball.merge(matches_subset, on='match_id', how='left')

# Calculate runs on delivery
# For team total: runs + extras1_runs + extras_2_runs
bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']

# Bowler runs conceded: runs + extras (wide, no-ball/Overstep, penalty, other)
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0)

# Legal ball flags
bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'

# Bowler wicket: is_wicket == True AND dismissal_type not in ['RunOut', 'Retire Out']
bball['is_bowler_wicket'] = bball['is_wicket'] & (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) & bball['dismissal_type'].notna()

# Cumulative innings stats
print("Computing cumulative match states...")
# Group by match and innings to compute running score and running wickets
bball['cum_runs'] = bball.groupby(['match_id', 'innings'])['ball_total_runs'].cumsum()
bball['cum_wickets'] = bball.groupby(['match_id', 'innings'])['is_wicket'].cumsum()
bball['cum_legal_balls'] = bball.groupby(['match_id', 'innings'])['is_legal_ball_bowler'].cumsum()

# Prior state BEFORE the delivery is bowled
bball['prev_cum_runs'] = bball['cum_runs'] - bball['ball_total_runs']
bball['prev_cum_wickets'] = bball['cum_wickets'] - bball['is_wicket'].astype(int)
bball['prev_legal_balls'] = bball['cum_legal_balls'] - bball['is_legal_ball_bowler'].astype(int)

# Total match innings 1 score to compute target for innings 2
inn1_totals = bball[bball['innings'] == 1].groupby('match_id')['ball_total_runs'].sum().reset_index()
inn1_totals.rename(columns={'ball_total_runs': 'inn1_total_runs'}, inplace=True)

bball = bball.merge(inn1_totals, on='match_id', how='left')

# Calculate target for innings 2
# If revised_target exists and > 0, use it. Otherwise inn1_total_runs + 1
bball['target'] = np.where(
    bball['revised_target'].notna() & (bball['revised_target'] > 0),
    bball['revised_target'],
    bball['inn1_total_runs'] + 1
)

# For innings 2, compute runs required and balls remaining
# Max scheduled overs is typically 20 overs = 120 legal balls
# Let's verify max balls in innings
bball['balls_remaining'] = np.maximum(0, 120 - bball['prev_legal_balls'])
bball['runs_required'] = np.maximum(0, bball['target'] - bball['prev_cum_runs'])
bball['wickets_in_hand'] = np.maximum(0, 10 - bball['prev_cum_wickets'])

# Required run rate (RRR)
bball['current_rrr'] = np.where(
    (bball['innings'] == 2) & (bball['balls_remaining'] > 0),
    (bball['runs_required'] / bball['balls_remaining']) * 6.0,
    np.nan
)

# Current run rate (CRR)
bball['current_crr'] = np.where(
    bball['prev_legal_balls'] > 0,
    (bball['prev_cum_runs'] / bball['prev_legal_balls']) * 6.0,
    0.0
)

print("Sample innings 2 situations:")
print(bball[bball['innings'] == 2][['match_id', 'overid', 'over_ball_num', 'prev_cum_runs', 'prev_cum_wickets', 'target', 'runs_required', 'balls_remaining', 'current_rrr']].head(15))
