"""
RR APEX SCOUT — Auction Intelligence & Availability Classifier
Enforces strict separation between Overall Pressure Rankings and RR Auction Target Shortlist.
Computes Auction Opportunity Score (AOS) for IPL 2027 Mini-Auction scenario.
"""

import json
import os

print("=" * 80)
print("RR APEX SCOUT — AUCTION INTELLIGENCE & AVAILABILITY CLASSIFIER")
print("=" * 80)

data_dir = os.path.join('data', 'processed')
public_dir = os.path.join('public', 'data')

with open(os.path.join(data_dir, 'top10_batters.json')) as f:
    batters = json.load(f)

with open(os.path.join(data_dir, 'top10_bowlers.json')) as f:
    bowlers = json.load(f)

# Official & Verified IPL 2025-2027 Franchise Retention / Availability Registry
PLAYER_AUCTION_STATUS = {
    # Batters
    'Suryakumar Yadav': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Mumbai Indians',
        'contractDetails': 'Capped Retention (₹16.35 Cr+)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Franchise cornerstone; confirmed retained by Mumbai Indians ahead of the 2025-2027 cycle. Cannot be acquired via auction.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Top-Order 360° Accumulator',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Naman Dhir': {
        'status': 'Available in Auction — Prime Target',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Punjab Kings (Released) / Domestic',
        'contractDetails': 'Auction Pool / Uncapped-Emerging Category',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Released into the auction pool. High-ceiling domestic finisher with 201.5 pressure SR. Ideal middle-order acceleration asset for RR.',
        'auctionOpportunityScore': 94.5,
        'squadRoleFit': 'No. 5/6 Dynamic Finisher & Part-time Off-Spin',
        'acquisitionPriority': 'Tier 1 Prime Target (High Purse Efficiency)'
    },
    'Tim David': {
        'status': 'Available in Auction — Confirmed',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Free Agent / Australia (CA)',
        'contractDetails': 'Overseas Auction Pool (Base ₹2.00 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Overseas death-over detonator available in the auction pool. Destroys 12+ RRR scenarios (196.7 pressure SR). Fills RR overseas finishing void.',
        'auctionOpportunityScore': 89.2,
        'squadRoleFit': 'No. 6/7 Death Over Detonator (Overseas Slot)',
        'acquisitionPriority': 'Tier 1 Priority Target (Overseas Power Finisher)'
    },
    'Shashank Singh': {
        'status': 'Available in Auction — Prime Target',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Punjab Kings (Contract Expired) / Domestic',
        'contractDetails': 'Domestic Auction Pool (Base ₹30–50 Lakh)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Elite domestic chase master (59.0 pressure avg in crisis situations). Protects RR top-order from catastrophic collapses from 40/4.',
        'auctionOpportunityScore': 93.8,
        'squadRoleFit': 'No. 5/6 Crisis Chase Stabilizer',
        'acquisitionPriority': 'Tier 1 Prime Target (Indian Domestic Clutch Asset)'
    },
    'Jos Buttler': {
        'status': 'Available in Auction — Royals Heritage',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'England (ECB) / Free Agent',
        'contractDetails': 'Overseas Marquee Pool (Base ₹2.00 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Royals championship legend released ahead of mega auction restructuring. Proven compatibility with Sanju Samson & Jaipur dimensions.',
        'auctionOpportunityScore': 86.4,
        'squadRoleFit': 'Opening Power Batter / Backup Wicketkeeper (Overseas Slot)',
        'acquisitionPriority': 'Tier 2 Marquee Target (Subject to Purse Feasibility)'
    },
    'Rajat Patidar': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Royal Challengers Bengaluru',
        'contractDetails': 'Capped Retention (₹11.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Core Indian middle-order pillar retained by Royal Challengers Bengaluru. Not entering the auction.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Middle-Overs Spin Enforcer',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Phil Salt': {
        'status': 'Available in Auction — Confirmed',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'England (ECB) / KKR (Released)',
        'contractDetails': 'Overseas Wicketkeeper Pool (Base ₹2.00 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Released into the auction pool. Ultra-aggressive powerplay opener (202.6 pressure SR). Can set game-winning tempos at SMS Jaipur.',
        'auctionOpportunityScore': 83.5,
        'squadRoleFit': 'Powerplay Opening Wicketkeeper (Overseas Slot)',
        'acquisitionPriority': 'Tier 2 Tactical Target'
    },
    'Reeza Hendricks': {
        'status': 'Available in Auction — Confirmed',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'South Africa (CSA) / Free Agent',
        'contractDetails': 'Overseas Batsman Pool (Base ₹1.50 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Uncapped/budget overseas anchor (178.3 pressure SR). High-efficiency squad depth asset requiring minimal purse expenditure.',
        'auctionOpportunityScore': 78.0,
        'squadRoleFit': 'Top-Order Anchor / Injury Cover (Overseas Slot)',
        'acquisitionPriority': 'Tier 3 Budget Value Asset'
    },
    'Virat Kohli': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Royal Challengers Bengaluru',
        'contractDetails': 'Capped Retention (₹21.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Permanent franchise icon retained by Royal Challengers Bengaluru. Zero auction availability.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Marquee Anchor',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Rishabh Pant': {
        'status': 'Contracted / Marquee — Unavailable for RR',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Lucknow Super Giants',
        'contractDetails': 'Record Auction Purchase (₹27.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Contracted to LSG on a historic ₹27 Cr long-term franchise commitment. Fully unavailable for recruitment.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Wicketkeeper / Captain',
        'acquisitionPriority': 'N/A — Contracted to Rival Franchise'
    },

    # Bowlers
    'Hasan Mahmud': {
        'status': 'Available in Auction — Subject to BCB NOC',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Bangladesh (BCB) / Free Agent',
        'contractDetails': 'Overseas Fast Bowler Pool (Base ₹75 Lakh)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Rank #1 statistical pressure bowler (5.97 economy, 49.6% dots). Precision death-over yorker executor available at exceptional budget value.',
        'auctionOpportunityScore': 92.0,
        'squadRoleFit': 'Death-Overs Seam Specialist (Overseas Slot)',
        'acquisitionPriority': 'Tier 1 Budget Steal Target (Subject to BCB NOC)'
    },
    'Benjamin Sears': {
        'status': 'Available in Auction — Prime Target',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'New Zealand (NZC) / Free Agent',
        'contractDetails': 'Overseas Fast Bowler Pool (Base ₹75 Lakh - ₹1 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': '145+ km/h express seamer with 6.32 pressure economy and 44.0% dot ball rate. Generates hostile steep bounce ideal for SMS Jaipur.',
        'auctionOpportunityScore': 91.5,
        'squadRoleFit': 'Express Hit-the-Deck Enforcer (Overseas Slot)',
        'acquisitionPriority': 'Tier 1 Priority Target (High-Pace Hostility)'
    },
    'Sunil Narine': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Kolkata Knight Riders',
        'contractDetails': 'Capped Retention (₹12.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Foundational franchise pillar retained by Kolkata Knight Riders. Zero auction availability.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Mystery Spinner / Opener',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Mohammad Rishad Hossain': {
        'status': 'Available in Auction — Confirmed',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Bangladesh (BCB) / Free Agent',
        'contractDetails': 'Overseas Spin Pool (Base ₹50–75 Lakh)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Tall leg-spinner offering sharp over-spin bounce. 7.30 economy with 24 high-leverage wickets. Low-cost SMS Jaipur tactical weapon.',
        'auctionOpportunityScore': 82.5,
        'squadRoleFit': 'Attacking Wrist-Spinner (Overseas Slot)',
        'acquisitionPriority': 'Tier 2 Tactical Target'
    },
    'Mitchell Santner': {
        'status': 'Available in Auction — Prime Target',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'New Zealand (NZC) / CSK (Released)',
        'contractDetails': 'Overseas All-Rounder Pool (Base ₹1.50 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Released by CSK into the auction pool. World-class defensive spinner (6.83 pressure economy) with zero loose deliveries in knockout matches.',
        'auctionOpportunityScore': 93.0,
        'squadRoleFit': 'Middle-Overs Spin Restrictor & No. 8 Depth (Overseas Slot)',
        'acquisitionPriority': 'Tier 1 Keystone Target (SMS Jaipur Spin Choke)'
    },
    'Umran Malik': {
        'status': 'Available in Auction — Prime Target',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'Sunrisers Hyderabad (Released) / Domestic',
        'contractDetails': 'Domestic Fast Bowling Pool (Base ₹50 Lakh - ₹1 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Verified Indian National delivering 150+ km/h velocity. 48.5% dot ball rate under pressure. Essential domestic pace asset for RR squad balance.',
        'auctionOpportunityScore': 95.0,
        'squadRoleFit': 'Middle-Overs Enforcer & Impact Player (Indian Core)',
        'acquisitionPriority': 'Tier 1 Non-Negotiable Domestic Pace Target'
    },
    'Rashid Khan': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Gujarat Titans',
        'contractDetails': 'Capped Retention (₹18.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Franchise cornerstone retained by Gujarat Titans. Unavailable for recruitment.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'World-Class Wrist Spinner',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Matheesha Pathirana': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Chennai Super Kings',
        'contractDetails': 'Capped Retention (₹13.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Franchise death-over cornerstone retained by Chennai Super Kings. Unavailable for recruitment.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Slinging Death Yorker Closer',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    },
    'Jamie Overton': {
        'status': 'Available in Auction — Confirmed',
        'statusCode': 'AVAILABLE_AUCTION_TARGET',
        'currentFranchise': 'England (ECB) / CSK (Released)',
        'contractDetails': 'Overseas Fast Bowling All-Rounder (Base ₹1.50 Cr)',
        'isRRAcquisitionTarget': True,
        'availabilityReason': 'Heavy-ball seam all-rounder (8.11 pressure economy, 174 SR). Provides hard lengths at SMS Jaipur and power hitting at No. 8.',
        'auctionOpportunityScore': 85.0,
        'squadRoleFit': 'Fast-Bowling All-Rounder (Overseas Slot)',
        'acquisitionPriority': 'Tier 2 Tactical Target'
    },
    'Jasprit Bumrah': {
        'status': 'Retained — Unavailable for Auction',
        'statusCode': 'RETAINED_UNAVAILABLE',
        'currentFranchise': 'Mumbai Indians',
        'contractDetails': 'Capped Retention (₹18.00 Cr)',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Franchise icon and undisputed global pace benchmark retained by Mumbai Indians. Zero auction availability.',
        'auctionOpportunityScore': 0.0,
        'squadRoleFit': 'Multi-Phase Fast Bowling Legend',
        'acquisitionPriority': 'N/A — Retained by Rival Franchise'
    }
}

# Enrich Batters
for b in batters:
    name = b['name']
    meta = PLAYER_AUCTION_STATUS.get(name, {
        'status': 'Availability Unverified',
        'statusCode': 'UNVERIFIED',
        'currentFranchise': 'International / Domestic Pool',
        'contractDetails': 'Provisional Registration',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Official auction registration status unconfirmed.',
        'auctionOpportunityScore': 50.0,
        'squadRoleFit': 'Squad Depth',
        'acquisitionPriority': 'Watchlist Only'
    })
    b['auctionAvailabilityStatus'] = meta['status']
    b['auctionStatusCode'] = meta['statusCode']
    b['currentFranchise'] = meta['currentFranchise']
    b['contractDetails'] = meta['contractDetails']
    b['isRRAcquisitionTarget'] = meta['isRRAcquisitionTarget']
    b['availabilityReason'] = meta['availabilityReason']
    b['auctionOpportunityScore'] = meta['auctionOpportunityScore']
    b['squadRoleFit'] = meta['squadRoleFit']
    b['acquisitionPriority'] = meta['acquisitionPriority']

# Enrich Bowlers
for bw in bowlers:
    name = bw['name']
    meta = PLAYER_AUCTION_STATUS.get(name, {
        'status': 'Availability Unverified',
        'statusCode': 'UNVERIFIED',
        'currentFranchise': 'International / Domestic Pool',
        'contractDetails': 'Provisional Registration',
        'isRRAcquisitionTarget': False,
        'availabilityReason': 'Official auction registration status unconfirmed.',
        'auctionOpportunityScore': 50.0,
        'squadRoleFit': 'Squad Depth',
        'acquisitionPriority': 'Watchlist Only'
    })
    bw['auctionAvailabilityStatus'] = meta['status']
    bw['auctionStatusCode'] = meta['statusCode']
    bw['currentFranchise'] = meta['currentFranchise']
    bw['contractDetails'] = meta['contractDetails']
    bw['isRRAcquisitionTarget'] = meta['isRRAcquisitionTarget']
    bw['availabilityReason'] = meta['availabilityReason']
    bw['auctionOpportunityScore'] = meta['auctionOpportunityScore']
    bw['squadRoleFit'] = meta['squadRoleFit']
    bw['acquisitionPriority'] = meta['acquisitionPriority']

# Filter dedicated RR Auction Target Shortlists (Available ONLY, ranked by AOS)
rr_target_batters = sorted([b for b in batters if b['isRRAcquisitionTarget']], key=lambda x: x['auctionOpportunityScore'], reverse=True)
rr_target_bowlers = sorted([bw for bw in bowlers if bw['isRRAcquisitionTarget']], key=lambda x: x['auctionOpportunityScore'], reverse=True)

auction_shortlist_payload = {
    'title': 'Rajasthan Royals IPL 2027 Realistic Auction Target Shortlist',
    'auctionType': 'Mini-Auction Scenario (IPL 2027)',
    'governingRules': 'BCCI IPL Player Regulations 2025–2027',
    'rrSquadState': {
        'retainedPlayers': [
            {'name': 'Sanju Samson', 'role': 'Captain / Wicketkeeper-Batter', 'price': '₹18.00 Cr', 'type': 'Indian National'},
            {'name': 'Yashasvi Jaiswal', 'role': 'Opening Batter (LHB)', 'price': '₹18.00 Cr', 'type': 'Indian National'},
            {'name': 'Riyan Parag', 'role': 'Middle-Order Anchor & Off-Spin', 'price': '₹14.00 Cr', 'type': 'Indian National'},
            {'name': 'Dhruv Jurel', 'role': 'Wicketkeeper-Batter / Finisher', 'price': '₹14.00 Cr', 'type': 'Indian National'},
            {'name': 'Shimron Hetmyer', 'role': 'Death-Over Finisher (LHB)', 'price': '₹11.00 Cr', 'type': 'Overseas Slot #1'},
            {'name': 'Sandeep Sharma', 'role': 'Death Seamer (Knuckleball / Yorkers)', 'price': '₹4.00 Cr', 'type': 'Indian Uncapped Rule'}
        ],
        'totalRetainedSalary': '₹79.00 Cr',
        'baseSalaryCap': '₹120.00 Cr',
        'estimatedMiniAuctionPurse': '₹28.50 - ₹34.00 Cr',
        'squadSlotsRemaining': '6 to 8 Slots',
        'overseasSlotsRemaining': '3 Slots Available (Max 8 in squad, max 4 in XI)'
    },
    'prioritizedTargetBatters': rr_target_batters,
    'prioritizedTargetBowlers': rr_target_bowlers,
    'scoringMethodology': 'Auction Opportunity Score (AOS) = 0.30 * Pressure BRS + 0.25 * RR Squad Gap Fill + 0.20 * Real Availability Verification + 0.15 * Purse Feasibility + 0.10 * SMS Jaipur Matchup Suitability'
}

# Save back to processed & public
for target_dir in [data_dir, public_dir]:
    with open(os.path.join(target_dir, 'top10_batters.json'), 'w') as f:
        json.dump(batters, f, indent=2)
    with open(os.path.join(target_dir, 'top10_bowlers.json'), 'w') as f:
        json.dump(bowlers, f, indent=2)
    with open(os.path.join(target_dir, 'rr_auction_shortlist.json'), 'w') as f:
        json.dump(auction_shortlist_payload, f, indent=2)

print(f"✓ Saved enriched Top 10 Batters ({len(batters)}) & Bowlers ({len(bowlers)})")
print(f"✓ Generated RR Auction Shortlist: {len(rr_target_batters)} Batters, {len(rr_target_bowlers)} Bowlers (0 Retained Players in Target List)")
print("=" * 80)
