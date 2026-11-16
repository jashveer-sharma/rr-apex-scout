import pandas as pd
import numpy as np

teams = pd.read_csv('DataSet/teams.csv')
comps = pd.read_csv('DataSet/competitions.csv')
matches = pd.read_csv('DataSet/matches.csv')

print("All unique teams in dataset:")
print(teams['team_name'].value_counts())

# Check how teams are mapped in matches
print("\nUnique home teams in matches:")
print(matches['home_team'].value_counts())
