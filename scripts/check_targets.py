import pandas as pd

matches = pd.read_csv('DataSet/matches.csv')
print("Revised target non-null count:", matches['revised_target'].notna().sum())
print(matches[matches['revised_target'].notna()][['match_id', 'home_team', 'away_team', 'revised_target', 'second_inn_revised_overs', 'result']].head(10))
