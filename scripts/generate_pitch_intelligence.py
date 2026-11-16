"""
RR APEX SCOUT — Pitch Intelligence Pipeline
Generates venue-level surface analysis from matches.csv + ball_by_ball.csv
"""

import json
import os
import pandas as pd
import numpy as np

# ─── LOAD RAW DATA ────────────────────────────────────────────────────────────
print("Loading raw datasets...")
bbb = pd.read_csv("DataSet/ball_by_ball.csv")
matches = pd.read_csv("DataSet/matches.csv")

print(f"ball_by_ball: {len(bbb)} rows")
print(f"matches: {len(matches)} rows")
print(f"matches columns: {list(matches.columns)}")

# ─── MERGE MATCH CONTEXT ──────────────────────────────────────────────────────
# Actual matches.csv columns: match_id, comp_id, venue_id, venue_country, home_team_id, away_team_id,
# toss_win_team_id, toss_opted, win_team_id, result
# Merge venue_country into ball_by_ball
bbb = bbb.merge(
    matches[['match_id', 'venue_id', 'venue_country', 'home_team_id', 'away_team_id',
             'win_team_id', 'toss_win_team_id', 'toss_opted']],
    on='match_id',
    how='left'
)

# Surface type mapping by country
SURFACE_MAP = {
    'India': 'Slow/Turning (Subcontinental)',
    'Sri Lanka': 'Slow/Turning (Subcontinental)',
    'Bangladesh': 'Slow/Turning (Subcontinental)',
    'UAE': 'Slow/Low (Dust Track)',
    'Australia': 'Hard/Bouncy (WACA/MCG)',
    'South Africa': 'Fast/True (High Altitude)',
    'England': 'Seam/Swing (Green Top)',
    'New Zealand': 'Seam/Bounce (Sporting)',
    'West Indies': 'Flat/Pacy (Caribbean Pitches)',
    'Zimbabwe': 'Hard/Flat (High Bounce)',
    'Pakistan': 'Flat/Low (Dust)',
    'Ireland': 'Swing/Seam (Damp)',
    'Scotland': 'Swing/Seam (Damp)',
}

bbb['surface_type'] = bbb['venue_country'].map(SURFACE_MAP).fillna('Moderate (Standard)')

# ─── LOAD ELIGIBLE PLAYERS (non-PCB) ─────────────────────────────────────────
with open("data/processed/master_player_register.json") as f:
    master = json.load(f)
eligible_ids = set(p['playerId'] for p in master['players'] if p.get('isEligible', True))

# ─── PER-VENUE ANALYSIS ───────────────────────────────────────────────────────
print("Computing venue-level stats...")

venue_groups = bbb.groupby(['venue_id', 'venue_country'])

venue_stats = []
for (vid, vcountry), grp in venue_groups:
    n_matches = grp['match_id'].nunique()
    if n_matches < 3:
        continue  # Skip tiny samples

    n_balls = len(grp)
    total_runs = grp['runs'].sum()

    # Innings split
    inn1 = grp[grp['innings'] == 1]
    inn2 = grp[grp['innings'] == 2]

    def safe_mean_score(ig):
        m_scores = ig.groupby('match_id')['runs'].sum()
        return round(float(m_scores.mean()), 1) if len(m_scores) > 0 else 0.0

    avg_1st = safe_mean_score(inn1)
    avg_2nd = safe_mean_score(inn2)

    # Pace vs Spin
    pace_del = grp[grp['pace_or_spin'] == 'pace']
    spin_del = grp[grp['pace_or_spin'] == 'spin']

    def econ(g):
        balls = len(g)
        if balls < 10:
            return None
        return round(g['runs'].sum() / (balls / 6), 2)

    def wkt_rate(g):
        balls = len(g)
        if balls < 10:
            return None
        return round(g['is_wicket'].sum() / balls * 6, 3)

    pace_econ = econ(pace_del)
    spin_econ = econ(spin_del)
    pace_wkt = wkt_rate(pace_del)
    spin_wkt = wkt_rate(spin_del)

    # Powerplay (overs 1-6), Middle (7-15), Death (16-20)
    pp = grp[grp['overid'] <= 6]
    mid = grp[(grp['overid'] >= 7) & (grp['overid'] <= 15)]
    death = grp[grp['overid'] >= 16]

    def run_rate(g):
        b = len(g)
        return round(g['runs'].sum() / (b / 6), 2) if b > 0 else 0.0

    # Boundary % and Dot %
    boundary_pct = round((grp['is_four'].sum() + grp['is_six'].sum()) / max(n_balls, 1) * 100, 1)
    dot_pct = round((grp['runs'] == 0).sum() / max(n_balls, 1) * 100, 1)

    # Bat-first vs Chase win rate
    # toss_opted = 'bat' means toss winner bats first
    match_results = matches[(matches['venue_id'] == vid) & (matches['win_team_id'].notna())]
    if len(match_results) > 0:
        # bat_first team is home_team if they won toss and batted, or away if they won toss and batted
        def bat_first_team(row):
            if str(row.get('toss_opted', '')).lower() in ('bat', 'batting'):
                return row['toss_win_team_id']
            else:
                # chose to field — other team bats first
                return row['home_team_id'] if row['toss_win_team_id'] == row['away_team_id'] else row['away_team_id']
        match_results = match_results.copy()
        match_results['bat_first'] = match_results.apply(bat_first_team, axis=1)
        bat_first_wins = (match_results['win_team_id'] == match_results['bat_first']).sum()
        bat_first_win_pct = round(bat_first_wins / len(match_results) * 100, 1)
    else:
        bat_first_win_pct = 50.0

    surface = SURFACE_MAP.get(vcountry, 'Moderate (Standard)')

    # Pitch Verdict
    if pace_econ is not None and spin_econ is not None:
        if pace_econ < spin_econ - 0.3:
            pitch_verdict = "Spin-Dominant"
        elif spin_econ < pace_econ - 0.3:
            pitch_verdict = "Pace-Dominant"
        else:
            pitch_verdict = "Balanced"
    else:
        pitch_verdict = "Insufficient Data"

    venue_stats.append({
        "venueId": int(vid),
        "country": vcountry,
        "surfaceType": surface,
        "matchCount": int(n_matches),
        "totalBalls": int(n_balls),
        "avg1stInningsScore": avg_1st,
        "avg2ndInningsScore": avg_2nd,
        "paceEconomy": pace_econ,
        "spinEconomy": spin_econ,
        "paceWicketRate": pace_wkt,
        "spinWicketRate": spin_wkt,
        "powerplayRunRate": run_rate(pp),
        "middleRunRate": run_rate(mid),
        "deathRunRate": run_rate(death),
        "boundaryPct": boundary_pct,
        "dotBallPct": dot_pct,
        "batFirstWinPct": bat_first_win_pct,
        "pitchVerdict": pitch_verdict
    })

venue_stats.sort(key=lambda x: x['matchCount'], reverse=True)
print(f"Computed stats for {len(venue_stats)} venues")

# ─── BATTER PITCH SUITABILITY ──────────────────────────────────────────────────
print("Computing batter pitch suitability...")

batter_groups = bbb[bbb['striker_id'].isin(eligible_ids)].groupby(['striker_id', 'striker_name', 'surface_type'])

batter_suitability = {}
for (pid, pname, surface), grp in batter_groups:
    n = len(grp)
    if n < 10:
        continue
    sr = round(grp['runs'].sum() / n * 100, 1)
    dot_pct = round((grp['runs'] == 0).sum() / n * 100, 1)
    bdry_pct = round((grp['is_four'].sum() + grp['is_six'].sum()) / n * 100, 1)
    if pid not in batter_suitability:
        batter_suitability[pid] = {"playerId": int(pid), "name": pname, "surfaces": {}}
    batter_suitability[pid]["surfaces"][surface] = {
        "balls": int(n),
        "strikeRate": sr,
        "dotPct": dot_pct,
        "boundaryPct": bdry_pct
    }

# Pace vs spin split
pace_spin_groups = bbb[bbb['striker_id'].isin(eligible_ids)].groupby(['striker_id', 'pace_or_spin'])
for (pid, ps_type), grp in pace_spin_groups:
    n = len(grp)
    if n < 5 or pid not in batter_suitability:
        continue
    sr = round(grp['runs'].sum() / n * 100, 1)
    dot_pct = round((grp['runs'] == 0).sum() / n * 100, 1)
    key = f"vs_{ps_type}"
    batter_suitability[pid][key] = {"balls": int(n), "strikeRate": sr, "dotPct": dot_pct}

batter_list = list(batter_suitability.values())
print(f"Batter suitability: {len(batter_list)} players")

# ─── BOWLER PITCH SUITABILITY ──────────────────────────────────────────────────
print("Computing bowler pitch suitability...")

bowler_groups = bbb[bbb['bowler_id'].isin(eligible_ids)].groupby(['bowler_id', 'bowler_name', 'surface_type'])

bowler_suitability = {}
for (pid, pname, surface), grp in bowler_groups:
    n = len(grp)
    if n < 12:
        continue
    econ_v = round(grp['runs'].sum() / (n / 6), 2)
    dot_pct = round((grp['runs'] == 0).sum() / n * 100, 1)
    wkt_rate = round(grp['is_wicket'].sum() / n * 6, 3)
    if pid not in bowler_suitability:
        bowler_suitability[pid] = {"playerId": int(pid), "name": pname, "surfaces": {}}
    bowler_suitability[pid]["surfaces"][surface] = {
        "balls": int(n),
        "economy": econ_v,
        "dotPct": dot_pct,
        "wicketRate": wkt_rate
    }

bowler_list = list(bowler_suitability.values())
print(f"Bowler suitability: {len(bowler_list)} players")

# ─── BATTER-BOWLER MATCHUP MATRIX ─────────────────────────────────────────────
print("Computing batter-bowler matchup matrix...")

# Top players by ball count for efficiency
top_batters = bbb.groupby('striker_id')['runs'].count().nlargest(50).index.tolist()
top_bowlers = bbb.groupby('bowler_id')['runs'].count().nlargest(50).index.tolist()

matchup_data = []
for bat_id in top_batters:
    if bat_id not in eligible_ids:
        continue
    for bowl_id in top_bowlers:
        if bowl_id not in eligible_ids:
            continue
        sub = bbb[(bbb['striker_id'] == bat_id) & (bbb['bowler_id'] == bowl_id)]
        if len(sub) < 20:
            continue
        n = len(sub)
        bat_name = sub['striker_name'].iloc[0]
        bowl_name = sub['bowler_name'].iloc[0]
        sr = round(sub['runs'].sum() / n * 100, 1)
        dot_pct = round((sub['runs'] == 0).sum() / n * 100, 1)
        bdry_pct = round((sub['is_four'].sum() + sub['is_six'].sum()) / n * 100, 1)
        wkt_rate = round(sub['is_wicket'].sum() / n * 6, 3)
        matchup_data.append({
            "batterId": int(bat_id), "baterName": bat_name,
            "bowlerId": int(bowl_id), "bowlerName": bowl_name,
            "balls": int(n), "strikeRate": sr,
            "dotPct": dot_pct, "boundaryPct": bdry_pct,
            "wicketRate": wkt_rate
        })

print(f"Matchup pairs: {len(matchup_data)}")

# ─── SAVE ALL OUTPUTS ─────────────────────────────────────────────────────────
os.makedirs("data/processed", exist_ok=True)
os.makedirs("public/data", exist_ok=True)

pitch_output = {
    "generatedAt": "2026-11-16",
    "totalVenues": len(venue_stats),
    "venues": venue_stats
}

with open("data/processed/pitch_intelligence.json", "w") as f:
    json.dump(pitch_output, f, indent=2)

with open("data/processed/pitch_suitability_batters.json", "w") as f:
    json.dump({"players": batter_list}, f, indent=2)

with open("data/processed/pitch_suitability_bowlers.json", "w") as f:
    json.dump({"players": bowler_list}, f, indent=2)

with open("data/processed/matchup_matrix.json", "w") as f:
    json.dump({"matchups": matchup_data}, f, indent=2)

# Copy to public/data
import shutil
for fname in ["pitch_intelligence.json", "pitch_suitability_batters.json",
              "pitch_suitability_bowlers.json", "matchup_matrix.json"]:
    shutil.copy(f"data/processed/{fname}", f"public/data/{fname}")

print("✅ Pitch Intelligence pipeline complete!")
print(f"  Venues: {len(venue_stats)}")
print(f"  Batter suitability: {len(batter_list)}")
print(f"  Bowler suitability: {len(bowler_list)}")
print(f"  Matchup pairs: {len(matchup_data)}")
