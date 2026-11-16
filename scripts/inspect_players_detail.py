import pandas as pd
import numpy as np

# Let's inspect qual_bat and qual_bowl in rank_players.py for these players
from rank_players import qual_bat, qual_bowl

marquee_batters = ['Heinrich Klaasen', 'Rinku Singh', 'Andre Russell', 'Suryakumar Yadav', 'Jos Buttler', 'Tim David', 'Shashank Singh', 'Babar Azam', 'Rajat Patidar', 'Nicholas Pooran', 'Sanju Samson', 'Shimron Hetmyer', 'Liam Livingstone', 'Dinesh Karthik', 'Tristan Stubbs', 'Naman Dhir', 'Riyan Parag']
print("=== MARQUEE BATTERS STATS UNDER PRESSURE ===")
mb = qual_bat[qual_bat['striker_name'].isin(marquee_batters)].copy()
mb = mb.sort_values('brs_score', ascending=False)
print(mb[['striker_name', 'press_raw_balls', 'press_runs', 'press_sr', 'press_avg', 'base_sr', 'delta_sr', 'press_boundary_pct', 'brs_score']].to_string())

marquee_bowlers = ['Jasprit Bumrah', 'Rashid Khan', 'Kuldeep Yadav', 'Arshdeep Singh', 'Matheesha Pathirana', 'Sunil Narine', 'Mohammad Shami', 'Yuzvendra Chahal', 'Sandeep Sharma', 'Anrich Nortje', 'Mitchell Starc', 'Trent Boult', 'Avesh Khan', 'Harshit Rana', 'Mohammad Nawaz', 'Sufiyan Muqeem', 'Hasan Mahmud']
print("\n=== MARQUEE BOWLERS STATS UNDER PRESSURE ===")
m_bowl = qual_bowl[qual_bowl['bowler_name'].isin(marquee_bowlers)].copy()
m_bowl = m_bowl.sort_values('brs_score', ascending=False)
print(m_bowl[['bowler_name', 'press_raw_balls', 'press_wickets', 'press_econ', 'base_econ', 'delta_econ', 'press_dot_pct', 'brs_score']].to_string())
