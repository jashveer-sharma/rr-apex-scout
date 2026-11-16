import pandas as pd

comps = pd.read_csv('DataSet/competitions.csv')
matches = pd.read_csv('DataSet/matches.csv')
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')

print("Competitions breakdown:")
m_c = matches.merge(comps, on='comp_id')
print(m_c.groupby(['match_format', 'season']).agg(
    matches=('match_id', 'count'),
    comps=('comp_name', 'nunique')
))

# Look at IPL vs T20I teams
teams = pd.read_csv('DataSet/teams.csv')
ipl_comps = comps[comps['comp_name'].str.contains('IPL', case=False, na=False)]
print("\nIPL competitions:")
print(ipl_comps)

ipl_matches = matches[matches['comp_id'].isin(ipl_comps['comp_id'])]
print(f"\nTotal IPL matches in dataset: {len(ipl_matches)}")

# Check players in IPL
ipl_teams = teams[teams['comp_id'].isin(ipl_comps['comp_id'])]
print("IPL teams sample:")
print(ipl_teams['team_name'].value_counts())

# Check how many players played in IPL vs T20I
bball = pd.read_csv('DataSet/ball_by_ball.csv', usecols=['match_id', 'striker_id', 'bowler_id'])
bball = bball.merge(matches[['match_id', 'comp_id']], on='match_id')
bball['is_ipl'] = bball['comp_id'].isin(ipl_comps['comp_id'])

ipl_batters = set(bball[bball['is_ipl']]['striker_id'].unique())
all_batters = set(bball['striker_id'].unique())
print(f"\nTotal batters: {len(all_batters)}, IPL batters: {len(ipl_batters)}")

ipl_bowlers = set(bball[bball['is_ipl']]['bowler_id'].unique())
all_bowlers = set(bball['bowler_id'].unique())
print(f"Total bowlers: {len(all_bowlers)}, IPL bowlers: {len(ipl_bowlers)}")
