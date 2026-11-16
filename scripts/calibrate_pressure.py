import pandas as pd
import numpy as np

# Load datasets
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

# Innings 1 totals
inn1_totals = bball[bball['innings'] == 1].groupby('match_id')['ball_total_runs'].sum().reset_index()
inn1_totals.rename(columns={'ball_total_runs': 'inn1_total_runs'}, inplace=True)
bball = bball.merge(inn1_totals, on='match_id', how='left')

# Target
bball['target'] = np.where(
    bball['revised_target'].notna() & (bball['revised_target'] > 0),
    bball['revised_target'],
    bball['inn1_total_runs'] + 1
)

bball['balls_remaining'] = np.maximum(0, 120 - bball['prev_legal_balls'])
bball['runs_required'] = np.maximum(0, bball['target'] - bball['prev_cum_runs'])
bball['wickets_in_hand'] = np.maximum(0, 10 - bball['prev_cum_wickets'])

# Required run rate
bball['current_rrr'] = np.where(
    (bball['innings'] == 2) & (bball['balls_remaining'] > 0),
    (bball['runs_required'] / bball['balls_remaining']) * 6.0,
    np.nan
)

# Current run rate
bball['current_crr'] = np.where(
    bball['prev_legal_balls'] > 0,
    (bball['prev_cum_runs'] / bball['prev_legal_balls']) * 6.0,
    8.0
)

# Define Pressure Index (PI) on continuous 0-10 scale
# Let's create components:
# 1. Innings 2 Pressure:
#    Based on RRR, balls remaining, wickets in hand
def calc_pressure(row):
    # Super over
    if row['innings'] in [3, 4]:
        return 10.0
    
    inn = row['innings']
    over = row['overid']
    balls_rem = row['balls_remaining']
    wkts_in_hand = row['wickets_in_hand']
    knockout = 1.2 if row['knock_out'] == 1 else 1.0
    
    if inn == 2:
        rrr = row['current_rrr']
        if pd.isna(rrr) or balls_rem == 0:
            return 5.0
        
        # Base pressure from RRR relative to par (8.5)
        # RRR 6 -> low, RRR 8.5 -> medium, RRR 12 -> high, RRR 15+ -> extreme
        rrr_factor = (rrr - 6.0) / 6.0  # at 6.0 = 0, at 8.5 = 0.41, at 12 = 1.0, at 15 = 1.5
        
        # Closeness / Death factor: later in the innings, each ball matters more
        # balls_rem 120 -> 0.2, balls_rem 30 -> 0.8, balls_rem 12 -> 1.2
        stage_factor = 1.0 + (120 - balls_rem) / 120.0  # 1.0 at start, 2.0 at end
        
        # Wicket pressure factor: fewer wickets in hand = higher pressure
        # 10 wkts -> 0.8, 5 wkts -> 1.1, 2 wkts -> 1.5, 1 wkt -> 1.8
        wkt_factor = 1.0 + (10 - wkts_in_hand) * 0.1
        
        # Combine
        raw_p = (2.5 + 3.0 * rrr_factor) * stage_factor * (wkt_factor / 1.2)
        
        # Cap/bound
        p = np.clip(raw_p * knockout, 1.0, 10.0)
        return p
        
    else: # Innings 1
        # In Innings 1, pressure stems from:
        # 1. Death overs (overs 16-20)
        # 2. Collapse (wickets lost early: e.g. <= 6 wickets in hand before over 10)
        # 3. Slow scoring requiring sudden recovery
        
        # Stage component: Powerplay (1-6)=3, Middle (7-15)=4, Death (16-20)=7
        if over <= 6:
            base = 3.0
            # Early collapse penalty
            if wkts_in_hand <= 7: # lost 3+ in powerplay
                base += (8 - wkts_in_hand) * 1.5
        elif over <= 15:
            base = 4.0
            if wkts_in_hand <= 5: # 5+ down in middle
                base += (6 - wkts_in_hand) * 1.2
            if row['current_crr'] < 7.0:
                base += 1.0
        else: # overs 16-20
            # Death overs base is high
            base = 6.5 + (over - 16) * 0.7  # over 16: 6.5, over 20: 9.3
            if wkts_in_hand <= 4:
                base += 1.0
        
        p = np.clip(base * knockout, 1.0, 10.0)
        return p

bball['pressure_index'] = bball.apply(calc_pressure, axis=1)

print("\n--- PRESSURE INDEX SUMMARY ---")
print(bball['pressure_index'].describe())

bball['pressure_tier'] = pd.cut(
    bball['pressure_index'],
    bins=[0, 4.0, 6.5, 8.5, 10.1],
    labels=['Low', 'Moderate', 'High', 'Extreme']
)
print("\nPressure Tier Distribution:")
print(bball['pressure_tier'].value_counts(normalize=True) * 100)
print("\nPressure Tier Counts:")
print(bball['pressure_tier'].value_counts())
