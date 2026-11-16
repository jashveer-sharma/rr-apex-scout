import pandas as pd
import numpy as np

# Let's inspect specific world-class players in the dataset
# and print top 30 batters and bowlers
bball = pd.read_csv('DataSet/ball_by_ball.csv', usecols=['striker_name', 'bowler_name'])
print("Total unique batters:", bball['striker_name'].nunique())
print("Total unique bowlers:", bball['bowler_name'].nunique())

# Check for Klaasen, Rinku, Bumrah, Russell
for p in ['Heinrich Klaasen', 'Rinku Singh', 'Andre Russell', 'Jasprit Bumrah', 'Rashid Khan', 'Kuldeep Yadav', 'Arshdeep Singh', 'Matheesha Pathirana']:
    b_as_striker = (bball['striker_name'] == p).sum()
    b_as_bowler = (bball['bowler_name'] == p).sum()
    print(f"Player: {p} -> Bat balls: {b_as_striker}, Bowl balls: {b_as_bowler}")
