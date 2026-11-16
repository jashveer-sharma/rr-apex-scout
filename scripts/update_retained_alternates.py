"""
Enrich top10_batters.json and top10_bowlers.json with explicit retention status and alternate target assignments.
Ensures 10 batters + 10 bowlers = 20 total players, with designated alternates for every retained star.
"""

import json
import shutil

# Load batters
with open("data/processed/top10_batters.json", "r", encoding="utf-8") as f:
    batters = json.load(f)

# Load bowlers
with open("data/processed/top10_bowlers.json", "r", encoding="utf-8") as f:
    bowlers = json.load(f)

# Batting alternates
BATTER_ALTERNATES = {
    "Suryakumar Yadav": {
        "isRetained": True,
        "retainedFranchise": "Mumbai Indians",
        "alternateTarget": "Tilak Varma",
        "alternateReason": "Left-hand dynamic 360° strokeplay; 158.6 pressure SR with fearless boundary intent."
    },
    "Rajat Patidar": {
        "isRetained": True,
        "retainedFranchise": "Royal Challengers Bengaluru",
        "alternateTarget": "Nehal Wadhera",
        "alternateReason": "Destructive spin demolisher in middle overs (overs 7-15); high-boundary upside."
    },
    "Virat Kohli": {
        "isRetained": True,
        "retainedFranchise": "Royal Challengers Bengaluru",
        "alternateTarget": "Devdutt Padikkal",
        "alternateReason": "High-anchor top-order accumulator with proven Sawai Mansingh Stadium domestic familiarity."
    },
    "Rishabh Pant": {
        "isRetained": True,
        "retainedFranchise": "Lucknow Super Giants",
        "alternateTarget": "Dhruv Jurel",
        "alternateReason": "RR in-house retained wicketkeeper-finisher; elite composure at 180+ death SR."
    }
}

# Bowling alternates
BOWLER_ALTERNATES = {
    "Sunil Narine": {
        "isRetained": True,
        "retainedFranchise": "Kolkata Knight Riders",
        "alternateTarget": "Varun Chakaravarthy",
        "alternateReason": "Mystery spin variation chokehold; sub-7.20 pressure economy across subcontinental surfaces."
    },
    "Rashid Khan": {
        "isRetained": True,
        "retainedFranchise": "Gujarat Titans",
        "alternateTarget": "Ravi Bishnoi",
        "alternateReason": "Rapid skiddy leg-spin and googlies; high dot-ball percentage (38.8%) forcing false shots."
    },
    "Matheesha Pathirana": {
        "isRetained": True,
        "retainedFranchise": "Chennai Super Kings",
        "alternateTarget": "Nuwan Thushara",
        "alternateReason": "Sling-action toe-crusher at 140+ km/h; identical trajectory variance for death-over defence."
    },
    "Jasprit Bumrah": {
        "isRetained": True,
        "retainedFranchise": "Mumbai Indians",
        "alternateTarget": "Avesh Khan",
        "alternateReason": "Indian international death specialist; proven block-hole accuracy and hard-length discipline."
    }
}

# Update batters
for b in batters:
    name = b["name"]
    if name in BATTER_ALTERNATES:
        info = BATTER_ALTERNATES[name]
        b["isRetained"] = True
        b["retainedFranchise"] = info["retainedFranchise"]
        b["alternateTarget"] = info["alternateTarget"]
        b["alternateReason"] = info["alternateReason"]
        b["auctionAvailabilityStatus"] = f"Retained — Unavailable ({info['retainedFranchise']})"
        b["isRRAcquisitionTarget"] = False
    else:
        b["isRetained"] = False
        b["retainedFranchise"] = None
        b["alternateTarget"] = None
        b["alternateReason"] = None
        b["isRRAcquisitionTarget"] = True
        b["auctionAvailabilityStatus"] = "Available in Auction — Prime Target"

# Update bowlers
for bw in bowlers:
    name = bw["name"]
    if name in BOWLER_ALTERNATES:
        info = BOWLER_ALTERNATES[name]
        bw["isRetained"] = True
        bw["retainedFranchise"] = info["retainedFranchise"]
        bw["alternateTarget"] = info["alternateTarget"]
        bw["alternateReason"] = info["alternateReason"]
        bw["auctionAvailabilityStatus"] = f"Retained — Unavailable ({info['retainedFranchise']})"
        bw["isRRAcquisitionTarget"] = False
    else:
        bw["isRetained"] = False
        bw["retainedFranchise"] = None
        bw["alternateTarget"] = None
        bw["alternateReason"] = None
        bw["isRRAcquisitionTarget"] = True
        bw["auctionAvailabilityStatus"] = "Available in Auction — Prime Target"

# Save updated data
with open("data/processed/top10_batters.json", "w", encoding="utf-8") as f:
    json.dump(batters, f, indent=2)

with open("data/processed/top10_bowlers.json", "w", encoding="utf-8") as f:
    json.dump(bowlers, f, indent=2)

# Copy to public/data
shutil.copy("data/processed/top10_batters.json", "public/data/top10_batters.json")
shutil.copy("data/processed/top10_bowlers.json", "public/data/top10_bowlers.json")

print(f"Updated {len(batters)} batters and {len(bowlers)} bowlers with explicit retention and alternate targets!")
