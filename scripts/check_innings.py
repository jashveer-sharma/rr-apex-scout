import pandas as pd

df = pd.read_csv('DataSet/ball_by_ball.csv', usecols=['match_id', 'innings', 'is_wicket', 'runs', 'extras1_runs', 'extras_2_runs', 'extras_type'])
print(f"Total rows in ball_by_ball: {len(df):,}")
print("Innings distribution across all 200,999 rows:")
print(df['innings'].value_counts())
