import pandas as pd
import json

mapping = pd.read_csv('DataSet/competition_team_player_mapping.csv')
print(f"Total mapping rows: {len(mapping)}")
print(f"Unique players in mapping: {mapping['player_id'].nunique()}")

# Identify players mapped to Pakistan or Pakistan A
pak_mapping = mapping[mapping['team_name'].isin(['Pakistan', 'Pakistan A'])]
pak_player_ids = set(pak_mapping['player_id'].unique())
print(f"Total players associated with Pakistan / Pakistan A: {len(pak_player_ids)}")

# Print sample of these players
sample = pak_mapping[['player_id', 'player_name', 'team_name']].drop_duplicates('player_id')
print("Sample excluded players:")
print(sample.head(20).to_string(index=False))

# Check who among them appeared in our previous rankings
with open('data/processed/top10_batters.json') as f:
    batters = json.load(f)
with open('data/processed/top10_bowlers.json') as f:
    bowlers = json.load(f)

excluded_batters_found = [b['name'] for b in batters if b.get('playerId') in pak_player_ids or b.get('nationality') == 'Pakistan']
excluded_bowlers_found = [bw['name'] for bw in bowlers if bw.get('playerId') in pak_player_ids or bw.get('nationality') == 'Pakistan']

print("\nExcluded players previously in top 10 batters:", excluded_batters_found)
print("Excluded players previously in top 10 bowlers:", excluded_bowlers_found)
