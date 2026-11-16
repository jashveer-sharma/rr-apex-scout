import pandas as pd
import numpy as np

df = pd.read_csv('DataSet/ball_by_ball.csv', nrows=50000)
print("extras_type values:")
print(df['extras_type'].value_counts(dropna=False))

print("\nSample extras rows:")
print(df[df['extras_type'].notna()][['extras_type', 'runs', 'extras1_runs', 'extras_2_runs', 'is_wicket']].head(10))

print("\nDismissal types:")
print(df['dismissal_type'].value_counts(dropna=False))

print("\nOverid range:", df['overid'].min(), "to", df['overid'].max())
print("Over_ball_num range:", df['over_ball_num'].min(), "to", df['over_ball_num'].max())
print("Innings range:", df['innings'].value_counts().to_dict())

# Check total match runs computation
sample_match = df[df['match_id'] == 13511]
inn1 = sample_match[sample_match['innings'] == 1]
print("\nMatch 13511 Innings 1 total runs off bat:", inn1['runs'].sum())
print("Match 13511 Innings 1 total extras1:", inn1['extras1_runs'].sum())
print("Match 13511 Innings 1 total extras2:", inn1['extras_2_runs'].sum())
print("Match 13511 Innings 1 wickets:", inn1['is_wicket'].sum())
