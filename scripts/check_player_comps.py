import pandas as pd

bball = pd.read_csv('DataSet/ball_by_ball.csv')
matches = pd.read_csv('DataSet/matches.csv')
comps = pd.read_csv('DataSet/competitions.csv')

bm = bball[bball['striker_name'] == 'Babar Azam'].merge(matches, on='match_id').merge(comps, on='comp_id')
print("Babar Azam competitions:")
print(bm['comp_name'].value_counts())

sm = bball[bball['bowler_name'] == 'Sufiyan Muqeem'].merge(matches, on='match_id').merge(comps, on='comp_id')
print("\nSufiyan Muqeem competitions:")
print(sm['comp_name'].value_counts())
