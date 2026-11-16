import pandas as pd
import numpy as np

# Load datasets
bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')

# Link competitions
matches = matches.merge(comps[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id', how='left')

# Classify competition tier
def get_comp_weight(comp_name):
    if pd.isna(comp_name):
        return 1.0
    c_lower = comp_name.lower()
    if 'ipl' in c_lower or 'indian premier league' in c_lower:
        return 1.25
    elif 'world cup' in c_lower or 'asia cup' in c_lower:
        return 1.15
    elif any(top in c_lower for top in ['india', 'australia', 'england', 'south africa', 'new zealand', 'pakistan']):
        return 1.10
    else:
        return 0.90

matches['comp_weight'] = matches['comp_name'].apply(get_comp_weight)

# Sort deliveries
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)
bball = bball.merge(matches[['match_id', 'comp_id', 'comp_name', 'match_format', 'season', 'comp_weight', 'knock_out', 'revised_target', 'win_team_id']], on='match_id', how='left')

# Ball runs
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

# Innings 1 total
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

# Robust Continuous Pressure Metric
# Innings 2:
rrr = bball['current_rrr'].fillna(8.0)
stage_factor = 1.0 + (120 - bball['balls_remaining']) / 120.0
wkt_factor = 1.0 + (10 - bball['wickets_in_hand']) * 0.1
knockout_mult = np.where(bball['knock_out'] == 1, 1.25, 1.0)

inn2_p = (2.5 + 3.0 * ((rrr - 6.0) / 6.0)) * stage_factor * (wkt_factor / 1.2) * knockout_mult
inn2_p = np.clip(inn2_p, 1.0, 10.0)

# Innings 1:
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

# Pressure tier
bball['is_pressure'] = bball['pressure_index'] >= 6.5

# Test various minimum sample thresholds for batters and bowlers
b_legal_bat = bball[bball['is_legal_ball_batter']].copy()
b_legal_bat['is_dot'] = (b_legal_bat['runs'] == 0) & (b_legal_bat['extras1_runs'] == 0)

for min_balls in [100, 150, 200]:
    b_agg = b_legal_bat[b_legal_bat['is_pressure']].groupby(['striker_id', 'striker_name']).agg(
        p_balls=('runs', 'count'),
        p_runs=('runs', 'sum'),
        p_dismissals=('is_wicket', 'sum'),
        p_fours=('is_four', 'sum'),
        p_sixes=('is_six', 'sum'),
        p_dots=('is_dot', 'sum'),
        p_matches=('match_id', 'nunique'),
        ipl_balls=('comp_weight', lambda w: (w >= 1.2).sum())
    ).reset_index()
    q = b_agg[b_agg['p_balls'] >= min_balls]
    print(f"Batters with >= {min_balls} pressure balls: {len(q)}")

b_legal_bowl = bball[bball['is_legal_ball_bowler']].copy()
b_legal_bowl['is_dot'] = (b_legal_bowl['bowler_runs_conceded'] == 0)
for min_balls in [100, 150, 200]:
    bw_agg = b_legal_bowl[b_legal_bowl['is_pressure']].groupby(['bowler_id', 'bowler_name']).agg(
        p_balls=('bowler_runs_conceded', 'count'),
        p_runs=('bowler_runs_conceded', 'sum'),
        p_wickets=('is_bowler_wicket', 'sum'),
        p_dots=('is_dot', 'sum'),
        p_matches=('match_id', 'nunique')
    ).reset_index()
    q_b = bw_agg[bw_agg['p_balls'] >= min_balls]
    print(f"Bowlers with >= {min_balls} pressure balls: {len(q_b)}")
