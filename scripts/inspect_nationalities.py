import pandas as pd
import json

mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')
with open('data/processed/all_players.json') as f:
    all_p = json.load(f)

print('=== BATTERS TEAMS ===')
for b in all_p['batters'][:15]:
    pid = b['striker_id']
    t_list = mapping[mapping['player_id'] == pid]['team_name'].unique().tolist()
    print(f"Rank {b['rank']}: {b['striker_name']} (ID {pid}) -> {t_list}")

print('\n=== BOWLERS TEAMS ===')
for bw in all_p['bowlers'][:15]:
    pid = bw['bowler_id']
    t_list = mapping[mapping['player_id'] == pid]['team_name'].unique().tolist()
    print(f"Rank {bw['rank']}: {bw['bowler_name']} (ID {pid}) -> {t_list}")
