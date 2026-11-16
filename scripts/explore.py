import pandas as pd
import numpy as np

matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')
mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')
p11 = pd.read_csv('DataSet/playing_eleven.csv')
teams = pd.read_csv('DataSet/teams.csv')

print("=== COMPETITIONS ===")
print(comps.info())
print(comps.head(10))

print("\n=== MATCHES ===")
print(f"Total matches in matches.csv: {len(matches)}")
print(f"Date range: {matches['match_date'].min()} to {matches['match_date'].max()}")
m_comp = matches.merge(comps, on='comp_id', how='left')
print("Matches by competition format & season:")
print(m_comp.groupby(['match_format', 'season']).size())

print("\nCompetitions list:")
print(comps['comp_name'].value_counts())

print("\n=== BALL-BY-BALL CHUNK SCAN ===")
# read sample or inspect columns
bball_head = pd.read_csv('DataSet/ball_by_ball.csv', nrows=1000)
print(bball_head[['match_id', 'innings', 'overid', 'over_ball_num', 'striker_name', 'bowler_name', 'runs', 'extras1_runs', 'is_wicket']].head(10))

print("\n=== PLAYERS IN MAPPING ===")
print(f"Unique players in mapping: {mapping['player_id'].nunique()}")
print(f"Unique player names in mapping: {mapping['player_name'].nunique()}")

print("\n=== PLAYING 11 ===")
print(f"Total entries in playing_eleven: {len(p11)}")
print(f"Matches in playing_eleven: {p11['match_id'].nunique()}")
