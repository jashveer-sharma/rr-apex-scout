import pandas as pd

mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')
p_map = mapping.drop_duplicates(['player_id', 'player_name']).set_index('player_name')['player_id'].to_dict()

top_10_batters = [
    'Babar Azam', 'Suryakumar Yadav', 'Naman Dhir', 'Tim David', 
    'Shashank Singh', 'Jos Buttler', 'Rajat Patidar', 'Reeza Hendricks', 
    'Phil Salt', 'Jacob Bethell'
]

top_10_bowlers = [
    'Sufiyan Muqeem', 'Mohammad Nawaz', 'Hasan Mahmud', 'Abrar Ahmed', 
    'Ahmed Daniyal', 'Sunil Narine', 'Umran Malik', 'Mitchell Santner', 
    'Spencer Johnson', 'Mark Wood'
]

print("=== BATTER LOOKUP IN MAPPING ===")
for p in top_10_batters:
    pid = p_map.get(p, None)
    matches = mapping[mapping['player_name'].str.contains(p.split()[-1], case=False, na=False)]['player_name'].unique()
    print(f"{p}: ID={pid} (Similar: {matches[:3]})")

print("\n=== BOWLER LOOKUP IN MAPPING ===")
for p in top_10_bowlers:
    pid = p_map.get(p, None)
    matches = mapping[mapping['player_name'].str.contains(p.split()[-1], case=False, na=False)]['player_name'].unique()
    print(f"{p}: ID={pid} (Similar: {matches[:3]})")
