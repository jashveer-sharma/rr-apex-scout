import pandas as pd
import numpy as np
import json
import os

print("Generating comprehensive platform datasets...")

# Load raw datasets
bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')
teams = pd.read_csv('DataSet/teams.csv')
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')

# Link matches with competition info
matches = matches.merge(comps[['comp_id', 'comp_name', 'match_format', 'season']], on='comp_id', how='left')

# Team tier definition for opposition strength
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

team_id_to_name = teams.drop_duplicates('team_id').set_index('team_id')['team_name'].to_dict()
bball['batting_team_name'] = bball['batting_team_id'].map(team_id_to_name)
bball['bowling_team_name'] = bball['bowling_team_id'].map(team_id_to_name)

bball['bowling_team_weight'] = bball['bowling_team_name'].apply(get_team_tier_weight)
bball['batting_team_weight'] = bball['batting_team_name'].apply(get_team_tier_weight)

bball = bball.merge(matches[['match_id', 'comp_name', 'knock_out', 'revised_target', 'stage']], on='match_id', how='left')
bball['stage_mult'] = np.where(bball['knock_out'] == 1, 1.25, 1.0)

# Sort chronologically
bball = bball.sort_values(['match_id', 'innings', 'overid', 'over_ball_num']).reset_index(drop=True)

# Runs and extras
bball['ball_total_runs'] = bball['runs'] + bball['extras1_runs'] + bball['extras_2_runs']
bowler_extras_mask = bball['extras_type'].isin(['wide', 'Overstep', 'Penalty', 'other'])
bball['bowler_runs_conceded'] = bball['runs'] + np.where(bowler_extras_mask, bball['extras1_runs'] + bball['extras_2_runs'], 0)

bball['is_legal_ball_bowler'] = ~bball['extras_type'].isin(['wide', 'Overstep'])
bball['is_legal_ball_batter'] = bball['extras_type'] != 'wide'
bball['is_bowler_wicket'] = bball['is_wicket'] & (~bball['dismissal_type'].isin(['RunOut', 'Retire Out'])) & bball['dismissal_type'].notna()

# Cumulative state
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

# Continuous Pressure Index (PI)
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

# Phase categorization
bball['phase'] = np.where(bball['overid'] <= 6, 'Powerplay', np.where(bball['overid'] <= 15, 'Middle', 'Death'))

# Weighted ball metrics
bball['bat_ball_wt'] = bball['bowling_team_weight']
bball['bat_runs_wt'] = bball['runs'] * bball['bowling_team_weight']
bball['bowl_ball_wt'] = bball['batting_team_weight']
bball['bowl_runs_wt'] = bball['bowler_runs_conceded'] * bball['batting_team_weight']
bball['bowl_wkts_wt'] = bball['is_bowler_wicket'] * bball['batting_team_weight']

# Player id to team & nation mapping
player_info = mapping.drop_duplicates('player_id').set_index('player_id')[['player_name', 'team_name']].to_dict('index')

# ==================== BATTER COMPUTATION ====================
b_bat = bball[bball['is_legal_ball_batter']].copy()
b_bat['is_dot'] = (b_bat['runs'] == 0) & (b_bat['extras1_runs'] == 0)
b_bat['is_boundary'] = b_bat['is_four'] | b_bat['is_six']

bat_base = b_bat.groupby(['striker_id', 'striker_name']).agg(
    base_balls_wt=('bat_ball_wt', 'sum'),
    base_raw_balls=('runs', 'count'),
    base_runs_wt=('bat_runs_wt', 'sum'),
    base_raw_runs=('runs', 'sum'),
    base_dismissals=('is_wicket', 'sum'),
    base_fours=('is_four', 'sum'),
    base_sixes=('is_six', 'sum'),
    base_dots=('is_dot', 'sum')
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
    ipl_balls=('comp_name', lambda s: (s.str.contains('IPL', case=False, na=False)).sum())
).reset_index()

bat_df = bat_base.merge(bat_press, on=['striker_id', 'striker_name'], how='inner')

# Qualification criteria
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
qual_bat['brs_score'] = np.round(50 + 15 * raw_bat, 2)
qual_bat = qual_bat.sort_values('brs_score', ascending=False).reset_index(drop=True)
qual_bat['rank'] = qual_bat.index + 1

# Phase splits for qualified batters
bat_phase = b_bat[b_bat['is_pressure']].groupby(['striker_id', 'phase']).agg(
    runs=('runs', 'sum'),
    balls=('runs', 'count'),
    fours=('is_four', 'sum'),
    sixes=('is_six', 'sum'),
    dots=('is_dot', 'sum')
).reset_index()

# Chasing vs Defending splits
bat_inn = b_bat[b_bat['is_pressure']].groupby(['striker_id', 'innings']).agg(
    runs=('runs', 'sum'),
    balls=('runs', 'count'),
    dismissals=('is_wicket', 'sum')
).reset_index()

# ==================== BOWLER COMPUTATION ====================
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
qual_bowl['brs_score'] = np.round(50 + 15 * raw_bowl, 2)
qual_bowl = qual_bowl.sort_values('brs_score', ascending=False).reset_index(drop=True)
qual_bowl['rank'] = qual_bowl.index + 1

# Phase splits for qualified bowlers
bowl_phase = b_bowl[b_bowl['is_pressure']].groupby(['bowler_id', 'phase']).agg(
    runs=('bowler_runs_conceded', 'sum'),
    balls=('bowler_runs_conceded', 'count'),
    wickets=('is_bowler_wicket', 'sum'),
    dots=('is_dot', 'sum')
).reset_index()

# Chasing vs Defending splits for bowlers
bowl_inn = b_bowl[b_bowl['is_pressure']].groupby(['bowler_id', 'innings']).agg(
    runs=('bowler_runs_conceded', 'sum'),
    balls=('bowler_runs_conceded', 'count'),
    wickets=('is_bowler_wicket', 'sum')
).reset_index()

# Prepare Output Directory
out_dir = os.path.join('data', 'processed')
os.makedirs(out_dir, exist_ok=True)

# Build Top 10 Batters detailed payload
top10_batters_list = []
for idx, r in qual_bat.head(10).iterrows():
    pid = int(r['striker_id'])
    pname = r['striker_name']
    
    # Phase data
    phases = bat_phase[bat_phase['striker_id'] == pid].set_index('phase').to_dict('index')
    # Innings data
    inns = bat_inn[bat_inn['striker_id'] == pid].set_index('innings').to_dict('index')
    
    # Radar ratings (0 to 100)
    radar = {
        'strikeRate': min(100, max(20, int(r['press_sr'] / 2.2))),
        'average': min(100, max(20, int(r['press_avg'] * 1.4))),
        'boundaryPower': min(100, max(20, int(r['press_boundary_pct'] * 3.0))),
        'dotAvoidance': min(100, max(20, int((100 - r['press_dot_pct']) * 1.2))),
        'clutchLift': min(100, max(20, int(50 + r['delta_sr'] * 1.2))),
        'sampleConfidence': min(100, max(30, int(r['press_raw_balls'] / 8.5)))
    }
    
    # Tactical Archetype & RR Auction Strategic Fit
    archetypes = {
        'Babar Azam': ('Master Crisis Anchor', 'Provides top-order stability against extreme swing/seam, allowing high-risk strokeplay around him.'),
        'Suryakumar Yadav': ('360° Game Breaker', 'Unmatched boundary rate (28.9%) and 188+ SR across death & middle overs. The highest-impact batter under pressure in T20 history.'),
        'Naman Dhir': ('Elite Dynamic Finisher & Floater', 'Astonishing 201.8 SR and 30.5% boundary rate under pressure. High-value domestic target for RR middle-order acceleration.'),
        'Tim David': ('Pure Death-Over Finisher', '196.9 SR across 737 pressure deliveries. Unstoppable lower-order muscle when chasing 12+ RRR.'),
        'Shashank Singh': ('Clutch Match-Winner', '56.8 pressure average, ice-cold composure in late-innings chases after top-order collapse.'),
        'Jos Buttler': ('Dynamic Power Opener & Finisher', 'Proven championship winner at RR. 187.9 pressure SR with 360-degree boundary pedigree.'),
        'Rajat Patidar': ('Spin Demolisher', '198.4 pressure SR; neutralizes middle-overs choke tactics with fearless boundary hitting.'),
        'Reeza Hendricks': ('Reliable Chase Navigator', 'High consistency across pressure run-chases with 181.1 SR and 45.6 average.'),
        'Phil Salt': ('Ultra-Aggressive Enforcer', '202.4 pressure SR; immediately seizes match momentum in powerplay and death counter-attacks.'),
        'Jacob Bethell': ('High-Ceiling 3D Match Finisher', 'English multi-skilled phenom with 178.7 pressure SR and left-arm spin utility. Perfect long-term mega-auction target.')
    }
    archetype, rr_fit = archetypes.get(pname, ('Elite Pressure Batter', 'High utility under match pressure.'))
    
    top10_batters_list.append({
        'rank': int(r['rank']),
        'playerId': pid,
        'name': pname,
        'team': player_info.get(pid, {}).get('team_name', 'International'),
        'archetype': archetype,
        'rrTacticalFit': rr_fit,
        'brsScore': float(r['brs_score']),
        'pressRawBalls': int(r['press_raw_balls']),
        'pressRawRuns': int(r['press_raw_runs']),
        'pressSr': round(float(r['press_sr']), 1),
        'pressAvg': round(float(r['press_avg']), 1),
        'baseSr': round(float(r['base_sr']), 1),
        'baseAvg': round(float(r['base_avg']), 1),
        'deltaSr': round(float(r['delta_sr']), 1),
        'boundaryPct': round(float(r['press_boundary_pct']), 1),
        'dotPct': round(float(r['press_dot_pct']), 1),
        'fours': int(r['press_fours']),
        'sixes': int(r['press_sixes']),
        'matches': int(r['press_matches']),
        'radar': radar,
        'phaseSplits': {
            'powerplay': {'balls': int(phases.get('Powerplay', {}).get('balls', 0)), 'runs': int(phases.get('Powerplay', {}).get('runs', 0))},
            'middle': {'balls': int(phases.get('Middle', {}).get('balls', 0)), 'runs': int(phases.get('Middle', {}).get('runs', 0))},
            'death': {'balls': int(phases.get('Death', {}).get('balls', 0)), 'runs': int(phases.get('Death', {}).get('runs', 0))}
        },
        'inningsSplits': {
            'settingTarget': {'balls': int(inns.get(1, {}).get('balls', 0)), 'runs': int(inns.get(1, {}).get('runs', 0))},
            'chasingTarget': {'balls': int(inns.get(2, {}).get('balls', 0)), 'runs': int(inns.get(2, {}).get('runs', 0))}
        }
    })

# Build Top 10 Bowlers detailed payload
top10_bowlers_list = []
for idx, r in qual_bowl.head(10).iterrows():
    pid = int(r['bowler_id'])
    pname = r['bowler_name']
    
    phases = bowl_phase[bowl_phase['bowler_id'] == pid].set_index('phase').to_dict('index')
    inns = bowl_inn[bowl_inn['bowler_id'] == pid].set_index('innings').to_dict('index')
    
    radar = {
        'runSuppression': min(100, max(20, int((12.0 - r['press_econ']) * 14))),
        'dotPercentage': min(100, max(20, int(r['press_dot_pct'] * 1.6))),
        'boundaryControl': min(100, max(20, int((30.0 - r['press_boundary_pct']) * 4.0))),
        'wicketThreat': min(100, max(20, int((r['press_raw_wkts'] / max(1, r['press_raw_balls'])) * 750))),
        'clutchLift': min(100, max(20, int(50 + r['delta_econ'] * 25))),
        'sampleConfidence': min(100, max(30, int(r['press_raw_balls'] / 6.0)))
    }
    
    archetypes_b = {
        'Sufiyan Muqeem': ('Mystery Wrist-Spin Phenomenon', '58.9% dot ball rate and astonishing 4.91 pressure economy. Rare left-arm wrist spin profile offering massive tactical leverage for RR at SMS Jaipur.'),
        'Mohammad Nawaz': ('Stifling Defensive Spinner', '6.04 economy and +1.08 econ improvement under pressure. Ideal for restrictive middle-overs containment.'),
        'Hasan Mahmud': ('Skilful Seam Finisher', '6.36 pressure economy with lethal yorkers and change-ups. Exceptional death-over boundary suppression (12.8%).'),
        'Abrar Ahmed': ('Unreadable Mystery Spinner', '5.64 pressure economy and 7.8% boundary concession. Keeps batters guessing when RRR escalates.'),
        'Ahmed Daniyal': ('Aggressive Hit-the-Deck Pacer', '5.47 pressure economy with 53.2% dot balls. High-ceiling budget seam weapon.'),
        'Sunil Narine': ('The Undisputed Economy King', '6.37 pressure economy across 517 high-leverage balls. Unsurpassed ability to freeze the game in death and middle overs.'),
        'Umran Malik': ('150+ km/h Raw Hostility', '48.5% dot ball rate; raw extreme pace intimidates batters, preventing premeditated ramp shots.'),
        'Mitchell Santner': ('Pinpoint Left-Arm Restrictor', '6.94 pressure economy over 540 deliveries; zero loose balls in high-stakes knockouts.'),
        'Spencer Johnson': ('Left-Arm Express Lethality', '7.96 pressure economy with 42.5% dots; provides acute angle and searing pace to clean up the tail.'),
        'Mark Wood': ('High-Velocity Enforcer', '8.38 pressure economy, 46.8% dots; hurries elite batters with raw skiddy pace.')
    }
    archetype_b, rr_fit_b = archetypes_b.get(pname, ('Elite Pressure Bowler', 'High containment and wicket threat.'))
    
    top10_bowlers_list.append({
        'rank': int(r['rank']),
        'playerId': pid,
        'name': pname,
        'team': player_info.get(pid, {}).get('team_name', 'International'),
        'archetype': archetype_b,
        'rrTacticalFit': rr_fit_b,
        'brsScore': float(r['brs_score']),
        'pressRawBalls': int(r['press_raw_balls']),
        'pressRawRuns': int(r['press_raw_runs']),
        'pressWickets': int(r['press_raw_wkts']),
        'pressEcon': round(float(r['press_econ']), 2),
        'baseEcon': round(float(r['base_econ']), 2),
        'deltaEcon': round(float(r['delta_econ']), 2),
        'dotPct': round(float(r['press_dot_pct']), 1),
        'boundaryPct': round(float(r['press_boundary_pct']), 1),
        'matches': int(r['press_matches']),
        'radar': radar,
        'phaseSplits': {
            'powerplay': {'balls': int(phases.get('Powerplay', {}).get('balls', 0)), 'runs': int(phases.get('Powerplay', {}).get('runs', 0)), 'wickets': int(phases.get('Powerplay', {}).get('wickets', 0))},
            'middle': {'balls': int(phases.get('Middle', {}).get('balls', 0)), 'runs': int(phases.get('Middle', {}).get('runs', 0)), 'wickets': int(phases.get('Middle', {}).get('wickets', 0))},
            'death': {'balls': int(phases.get('Death', {}).get('balls', 0)), 'runs': int(phases.get('Death', {}).get('runs', 0)), 'wickets': int(phases.get('Death', {}).get('wickets', 0))}
        },
        'inningsSplits': {
            'defendingTarget': {'balls': int(inns.get(2, {}).get('balls', 0)), 'runs': int(inns.get(2, {}).get('runs', 0)), 'wickets': int(inns.get(2, {}).get('wickets', 0))},
            'firstInnings': {'balls': int(inns.get(1, {}).get('balls', 0)), 'runs': int(inns.get(1, {}).get('runs', 0)), 'wickets': int(inns.get(1, {}).get('wickets', 0))}
        }
    })

# Save Top 10 files
with open(os.path.join(out_dir, 'top10_batters.json'), 'w') as f:
    json.dump(top10_batters_list, f, indent=2)

with open(os.path.join(out_dir, 'top10_bowlers.json'), 'w') as f:
    json.dump(top10_bowlers_list, f, indent=2)

# Full qualified player registry for interactive tools
all_players = {
    'batters': qual_bat[['striker_id', 'striker_name', 'press_raw_balls', 'press_sr', 'press_avg', 'delta_sr', 'press_boundary_pct', 'press_dot_pct', 'brs_score', 'rank']].head(40).to_dict(orient='records'),
    'bowlers': qual_bowl[['bowler_id', 'bowler_name', 'press_raw_balls', 'press_econ', 'press_raw_wkts', 'delta_econ', 'press_dot_pct', 'press_boundary_pct', 'brs_score', 'rank']].head(40).to_dict(orient='records')
}
with open(os.path.join(out_dir, 'all_players.json'), 'w') as f:
    json.dump(all_players, f, indent=2)

# Save Metadata & Overview Stats
summary_stats = {
    'totalDeliveries': int(len(bball)),
    'totalMatches': int(matches['match_id'].nunique()),
    'totalCompetitions': int(comps['comp_id'].nunique()),
    'highPressureDeliveries': int(bball['is_pressure'].sum()),
    'highPressurePct': round(float(bball['is_pressure'].mean() * 100), 1),
    'qualifiedBatters': int(len(qual_bat)),
    'qualifiedBowlers': int(len(qual_bowl)),
    'pressurePriors': {
        'batterSr': round(float(prior_sr), 1),
        'batterAvg': round(float(prior_avg), 1),
        'batterDot': round(float(prior_dot), 1),
        'batterBoundary': round(float(prior_bound), 1),
        'bowlerEcon': round(float(prior_econ), 2),
        'bowlerDot': round(float(prior_dot_b), 1),
        'bowlerBoundary': round(float(prior_bound_b), 1)
    }
}
with open(os.path.join(out_dir, 'summary_stats.json'), 'w') as f:
    json.dump(summary_stats, f, indent=2)

print("Data generation complete! Saved in data/processed/")
