# RR APEX SCOUT · RAJASTHAN ROYALS STRATEGIC AUCTION INTELLIGENCE
## IPL 2027 Mini-Auction Decision Support System & Decision Telemetry
### Official Entry · Unstop SupeRR Selector Season 2 (Round 1)

> **Live Deployment:** [https://rrapexscout.netlify.app/](https://rrapexscout.netlify.app/)  
> **Target Event:** IPL 2027 Mini-Auction · December 16, 2026 (Goa)  
> **Telemetry Scope:** 883 Matches | 200,999 Deliveries | 1,217 Player Universe | 100% BCCI/IPL Policy Compliant  

---

## 1. Executive Summary & Franchise Mandate

Conventional T20 scouting relies on surface aggregate averages and boundary counts accumulated during low-leverage phases or dead rubbers. This creates dangerous **valuation asymmetry** at the auction table:
1. **The Overs 16–20 Illusion:** Chasing 18 runs off 24 balls with 8 wickets in hand is low leverage, yet runs scored here artificially inflate death-over strike rates. Conversely, arriving at 18/3 in Over 4 chasing 210 represents extreme crisis leverage.
2. **Small-Sample Traps:** Players with 40 runs across 12 high-leverage deliveries command irrational bidding wars despite lacking statistical reliability.
3. **Regulatory Non-Compliance:** Unfiltered datasets risk surfacing ineligible overseas talent, violating BCCI and IPL operational directives.

**RR APEX SCOUT** solves this through a continuous **Situational Leverage Index (SLI)** and **Empirical Bayes Shrinkage ($M_0 = 60$)**, separating genuine high-leverage performers from small-sample illusions to construct a balanced, championship-caliber squad within Rajasthan Royals' remaining **₹28.5–34.0 Cr** mini-auction purse.

---

## 2. Mathematical Framework: SLI & Bayesian Shrinkage

### Continuous Situational Leverage Index (SLI)
Rather than segmenting matches into static phases, leverage is evaluated ball-by-ball ($0.0 \le \text{SLI} \le 3.0+$):

$$\text{SLI} = 1.0 + (\text{Phase Factor} \times 0.45) + \left(\frac{W_{\text{lost}}}{10}\right)^{1.2} \times 0.55 + (\text{Chase Flag} \times 0.25) \times [\text{Death Multiplier: } 1.25]$$

* **Crucible Deliveries:** 178,240 eligible deliveries exceed $\text{SLI} \ge 1.20$.
* **Empirical Bayes Shrinkage ($M_0 = 60$):** Every metric is regressed toward the league baseline ($\mu_{\text{SR}} = 132.4$, $\mu_{\text{Econ}} = 8.64$):

$$\theta_{\text{shrunk}} = \left[\frac{N}{N + 60}\right]\theta_{\text{observed}} + \left[\frac{60}{N + 60}\right]\mu_{\text{league}}$$

* **Bayesian Reliability Score (BRS, 0–100):** Synthesizes shrunk strike rate/economy, delta lift over baseline, dot-ball dominance, and boundary conversion.
* **Auction Opportunity Score (AOS, 0–100):**

$$\text{AOS} = 0.40(\text{BRS}) + 0.25(\text{RR Squad Gap}) + 0.15(\text{Purse Feasibility}) + 0.10(\text{Jaipur Dimension Fit}) + 0.10(\text{NOC Certainty})$$

---

## 3. Official 20-Player Master Selection Register

To maintain complete analytical transparency, pure Bayesian statistical benchmarks include all qualified players. Retained franchise cornerstones are explicitly designated as **RETAINED** with a **Designated RR Alternate Target** matching the identical tactical profile and archetype.

### Top 10 Batters Under Pressure

| # | Batter Name | Nat | Press SR | Press Avg | Clutch ΔSR | Dot % | BRS Score | Auction Availability Status | Designated RR Alternate Target | Alternate Rationale |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| **1** | **Suryakumar Yadav** | IND | 188.7 | 57.3 | +21.3 | 26.2% | **79.4** | **RETAINED (Mumbai Indians)** | **Tilak Varma** | Left-hand 360° strokeplay; 158.6 pressure SR with fearless boundary intent |
| **2** | **Naman Dhir** | IND | 201.5 | 42.1 | +32.2 | 22.9% | **76.5** | **AVAILABLE (Prime RR Target)** | *Primary Target* | Elite domestic finisher (201.5 SR); clears SMS Jaipur 70m+ square ropes |
| **3** | **Tim David** | AUS | 196.7 | 45.8 | +17.6 | 27.5% | **75.3** | **AVAILABLE (Overseas Target)** | *Primary Target* | Pure death-over detonator; obliterates 12+ RRR chase scenarios |
| **4** | **Shashank Singh** | IND | 182.5 | 59.0 | +20.9 | 22.2% | **75.2** | **AVAILABLE (Prime RR Target)** | *Primary Target* | Crisis chase specialist (59.0 pressure avg); collapse insurance from 40/4 |
| **5** | **Jos Buttler** | ENG | 189.5 | 42.3 | +35.0 | 22.5% | **74.5** | **AVAILABLE (Marquee Target)** | *Primary Target* | Royals icon; proven partnership synergy with Sanju Samson |
| **6** | **Rajat Patidar** | IND | 198.4 | 36.6 | +30.5 | 27.2% | **71.6** | **RETAINED (RCB)** | **Nehal Wadhera** | Destructive middle-overs spin demolisher (overs 7–15) |
| **7** | **Phil Salt** | ENG | 202.6 | 31.8 | +31.8 | 20.5% | **69.2** | **AVAILABLE (Overseas Target)** | *Primary Target* | 200+ powerplay SR; fearless boundary-clearing wicketkeeper-opener |
| **8** | **Reeza Hendricks** | RSA | 178.3 | 43.1 | +31.2 | 21.7% | **68.7** | **AVAILABLE (Overseas Target)** | *Primary Target* | High-floor consistency; structured navigation through heavy collapse |
| **9** | **Virat Kohli** | IND | 176.4 | 45.0 | +30.5 | 21.1% | **68.5** | **RETAINED (RCB)** | **Devdutt Padikkal** | High-anchor top-order accumulator with proven Sawai Mansingh Stadium familiarity |
| **10** | **Rishabh Pant** | IND | 182.2 | 36.1 | +38.6 | 29.1% | **68.3** | **RETAINED (LSG)** | **Dhruv Jurel** | In-house retained wicketkeeper-finisher; elite death-over composure |

---

### Top 10 Bowlers Under Pressure

| # | Bowler Name | Nat | Press Econ | Dot % | Wkts | ΔEcon | BRS Score | Auction Availability Status | Designated RR Alternate Target | Alternate Rationale |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| **1** | **Hasan Mahmud** | BAN | 5.97 | 49.6% | 11 | +0.53 | **80.9** | **AVAILABLE (Prime RR Target)** | *Primary Target* | #1 Ranked Pressure Bowler; pinpoint block-hole accuracy under evening dew |
| **2** | **Benjamin Sears** | NZL | 6.32 | 44.0% | 11 | +0.96 | **79.7** | **AVAILABLE (Overseas Target)** | *Primary Target* | Express seamer (145+ km/h); extracts steep bounce on subcontinental tracks |
| **3** | **Sunil Narine** | WI | 6.37 | 40.2% | 36 | +0.39 | **77.4** | **RETAINED (KKR)** | **Varun Chakaravarthy** | Mystery spin variation chokehold; sub-7.20 pressure economy across subcontinental decks |
| **4** | **Mohammad Rishad** | BAN | 7.30 | 41.6% | 24 | +0.90 | **75.0** | **AVAILABLE (Overseas Target)** | *Primary Target* | Rapid wrist-spin; turn away from right-handers in middle overs (overs 7–15) |
| **5** | **Mitchell Santner** | NZL | 6.83 | 38.3% | 37 | +0.42 | **73.9** | **AVAILABLE (Overseas Target)** | *Primary Target* | Pinpoint finger-spin accuracy; suffocates middle overs at SMS Jaipur (6.83 econ) |
| **6** | **Umran Malik** | IND | 8.19 | 48.5% | 20 | +0.95 | **73.6** | **AVAILABLE (Prime RR Target)** | *Primary Target* | 150+ km/h hostile heat; forces mistimed pulls into 70m+ Jaipur outfield |
| **7** | **Rashid Khan** | AFG | 7.75 | 38.3% | 79 | -0.21 | **69.2** | **RETAINED (Gujarat Titans)** | **Ravi Bishnoi** | Rapid skiddy leg-spin and googlies; high dot percentage (38.8%) forcing false shots |
| **8** | **Matheesha Pathirana** | SL | 7.73 | 38.9% | 55 | +0.02 | **69.1** | **RETAINED (CSK)** | **Nuwan Thushara** | Sling-action toe-crusher at 140+ km/h; identical low trajectory release for death overs |
| **9** | **Jamie Overton** | ENG | 8.11 | 39.7% | 21 | +0.28 | **68.9** | **AVAILABLE (Overseas Target)** | *Primary Target* | Hard-length seamer with lower-order hitting utility (160+ SR) |
| **10** | **Jasprit Bumrah** | IND | 7.17 | 37.7% | 48 | -0.35 | **68.4** | **RETAINED (Mumbai Indians)** | **Avesh Khan** | Indian international death specialist; proven yorker and hard-length control |

---

## 4. Rajasthan Royals Squad Construction: Three Tactical Scenarios

Rajasthan Royals enters the IPL 2027 Mini-Auction with **₹79.00 Cr** committed to retained cornerstones (Sanju Samson, Yashasvi Jaiswal, Riyan Parag, Dhruv Jurel, Shimron Hetmyer, Sandeep Sharma) and an estimated **₹28.5–34.0 Cr** purse with **3 Overseas slots** remaining.

### Scenario Comparison Matrix

| Dimension | Scenario A: Core Continuity | Scenario B: Balanced Rebuild *(RECOMMENDED)* | Scenario C: Opportunity Firepower |
| :--- | :--- | :--- | :--- |
| **Strategic Philosophy** | Conservative; fills gaps with uncapped value | Surgical balance; resolves death batting & pace hostility | Aggressive bid for marquee opener (Jos Buttler) |
| **Projected Spend** | ₹18.50 Cr | **₹25.20 Cr** | ₹32.00 Cr |
| **Remaining Purse Cushion**| ₹14.50 Cr *(High reserve)* | **₹7.80 Cr *(Optimal flexibility)*** | ₹1.00 Cr *(Tight margin)* |
| **Overseas Slots (XI / Squad)**| 4 / 5 | **3 / 6 *(1 overseas slot in reserve)*** | 4 / 6 |
| **Role Coverage Score** | 88 / 100 | **96 / 100** | 95 / 100 |
| **Key Acquisitions** | Dhir, Shashank, Santner, Overton, Sears | **Dhir, Shashank, U. Malik, Santner, H. Mahmud** | Buttler, Dhir, Santner, H. Mahmud, Malik |
| **Execution Feasibility** | Very High (>90%) | **High (85% certainty)** | Moderate (Subject to bidding war) |

---

## 5. Recommended Playing XI (Scenario B: Championship Rebuild)

Complies strictly with the **Maximum 4 Overseas Players in Playing XI** rule and optimizes the **IPL Impact Player Rule**:

| # | Player | Role | Status / Valuation | Nat | BRS | Tactical Role in Playing XI |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **1** | **Yashasvi Jaiswal** | Opener (LHB) | Retained (₹18.0 Cr) | IND | 71.5 | Powerplay aggressor; 160+ strike rate vs pace |
| **2** | **Sanju Samson (C/WK)**| Top-Order Anchor | Retained (₹18.0 Cr) | IND | 68.2 | Pace-spin manipulator; captaincy composure & game reading |
| **3** | **Riyan Parag (VC)** | Middle-Order Anchor | Retained (₹14.0 Cr) | IND | 67.8 | Spin enforcer in overs 7–15; utility off-break |
| **4** | **Rajat Patidar / Alt** | Aggressive Striker | Target / Alt (₹7.5 Cr) | IND | 72.3 | Spin acceleration at #4; neutralizes middle-overs choke |
| **5** | **Shashank Singh** | Crisis Finisher | Target (₹4.5 Cr) | IND | 74.4 | Collapse stabilizer (59.0 avg); ice-cold chase navigator |
| **6** | **Dhruv Jurel** | Finisher / WK | Retained (₹14.0 Cr) | IND | 65.4 | Boundary conversion in overs 18–20; lightning wicketkeeping |
| **7** | **Naman Dhir** | Dynamic Detonator | Target (₹5.5 Cr) | IND | 76.5 | Instant strike weapon (201.5 SR from ball 1); utility off-spin |
| **8** | **Shimron Hetmyer** | Death Slogger (LHB)| Retained (₹11.0 Cr) | OS | 69.4 | **Overseas Slot #1:** 190+ death striking against fast bowling |
| **9** | **Mitchell Santner** | Finger Spinner | Target (₹4.2 Cr) | OS | 73.9 | **Overseas Slot #2:** 6.83 economy chokehold; batting depth at #9 |
| **10**| **Sandeep Sharma** | Knuckleball Seamer | Retained (₹4.0 Cr) | IND | 64.8 | Wide-line yorkers; powerplay swing and death-overs deception |
| **11**| **Hasan Mahmud** | Death Specialist | Target (₹3.5 Cr) | OS | 80.9 | **Overseas Slot #3:** #1 pressure bowler; toe-crushing yorker precision |
| **Sub**| **Umran Malik** | Express Pace Sub | Target (₹4.0 Cr) | IND | 73.6 | **Tactical Impact Player:** 150+ km/h hostility in middle overs |

---

## 6. Player Compatibility & Tandem Synergies

Cricket matches are won through complementary combinations rather than isolated aggregates. We categorize tandems into **Empirical Partnerships** (verified from 4,423 real match partnerships) and **Tactical Projections**:

* **Yashasvi Jaiswal & Sanju Samson (Empirical — 842 balls, 140.6 SR):** Left-Right top-order engine. Jaiswal attacks pace in Powerplay; Samson controls spin through overs 7–15. Alternates boundary targeting to exploit uneven ground geometry.
* **Sanju Samson & Naman Dhir (Tactical Projection — 94.5% Synergy):** Anchor-Detonator axis. Samson absorbs situational leverage, liberating Dhir to strike at 180+ from ball 1 without innings-building burden.
* **Riyan Parag & Shimron Hetmyer (Empirical — 398 balls, 161.3 SR):** Middle-Spin + Death-Pace split. Parag eliminates finger spin; Hetmyer punishes pacers at 190+ SR in overs 17–20.
* **Sandeep Sharma & Hasan Mahmud (Tactical Projection — 96.0% Synergy):** Dual Death Vice. Extreme variance in delivery angle, trajectory, and release speed: Sandeep wide knuckleballs paired with Mahmud 140 km/h block-hole missiles under evening dew.

---

## 7. Pitch Intelligence & Sawai Mansingh Stadium Dynamics

Venue telemetry across 73 grounds reveals critical surface traits:
* **The SMS Jaipur Dimension:** Expansive **70m+ square boundaries** punish reckless slogging. Spinners operating stump-to-stump concede significantly fewer boundaries (40.2% dot-ball rate).
* **Defending Totals:** Spin economy (6.83) significantly outperforms pace economy (8.42) on dry surfaces. Pairing Mitchell Santner with Riyan Parag locks down overs 7–14, forcing batters into mistimed lofted shots toward deep midwicket.
* **Evening Dew Protocol:** Under heavy dew, Sandeep Sharma and Hasan Mahmud utilize wet-ball seam grips and wide-line yorkers outside the off-stump to neutralize boundary access.

---

## 8. Captaincy & Leadership Intelligence

Empirical evaluation of **883 match logs** confirms:
* **Sanju Samson (Captained 53 Matches · 52.8% Win Rate):** Guided RR to IPL Final (2022) and Qualifier 2 (2024). Exhibits balanced win rates defending (51.9%) and chasing (53.8%). His wicketkeeping vantage point enables calm field realignments without emotional volatility.
* **Leadership Structure:**
  1. **Franchise Captain:** Sanju Samson *(Re-confirmed)*
  2. **Vice-Captain:** Riyan Parag *(Assam domestic captain; proven leadership maturity)*
  3. **Senior Advisory Council:** Mitchell Santner *(NZ international captain)* and Sandeep Sharma.
  4. **Succession Roadmap (2028–2030):** Mentorship pathway preparing Parag or Jaiswal for long-term franchise transition.

---

## 9. Upstream Regulatory Audit & BCCI Compliance

Before any mathematical modeling was executed, an automated regulatory audit evaluated the player universe:
* **1,217 Unique Players Evaluated:** Indexed across international and domestic competitions.
* **1,149 Players Certified Eligible:** 100% compliant with BCCI and IPL player registration regulations.
* **68 Policy-Restricted Players Audited:** Pursuant to standing BCCI policy in effect since 2009, all 68 PCB-registered cricketers were audited and excluded upstream. Zero policy-restricted records appear in any public ranking, table, comparison, or squad blueprint. An internal audit trail is preserved at `data/internal/audit_trail_excluded_records.json`.
* **Overseas Cap:** Maximum 4 overseas players in the Playing XI strictly enforced across all 3 squad blueprints.

---

### Official Unstop Submission Sync Summary

* **Top 10 Batters:** Suryakumar Yadav *(Retained: MI → Alt: Tilak Varma)*, Naman Dhir *(Target)*, Tim David *(Target)*, Shashank Singh *(Target)*, Jos Buttler *(Target)*, Rajat Patidar *(Retained: RCB → Alt: Nehal Wadhera)*, Phil Salt *(Target)*, Reeza Hendricks *(Target)*, Virat Kohli *(Retained: RCB → Alt: Devdutt Padikkal)*, Rishabh Pant *(Retained: LSG → Alt: Dhruv Jurel)*.
* **Top 10 Bowlers:** Hasan Mahmud *(Target)*, Benjamin Sears *(Target)*, Sunil Narine *(Retained: KKR → Alt: Varun Chakaravarthy)*, Mohammad Rishad *(Target)*, Mitchell Santner *(Target)*, Umran Malik *(Target)*, Rashid Khan *(Retained: GT → Alt: Ravi Bishnoi)*, Matheesha Pathirana *(Retained: CSK → Alt: Nuwan Thushara)*, Jamie Overton *(Target)*, Jasprit Bumrah *(Retained: MI → Alt: Avesh Khan)*.
* **Audit Signature:** `RR-APEX-V5-20261116` · Verified for Mini-Auction Execution (Dec 16, 2026).
