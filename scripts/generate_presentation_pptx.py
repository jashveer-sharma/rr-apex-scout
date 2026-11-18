"""
RR APEX SCOUT — Master PowerPoint Generator (v6 Master)
Rajasthan Royals SupeRR Selector Season 2

Features:
- Strictly "SupeRR Selector Season 2" (no improper casing)
- Perfectly balanced 24-slide deck with ZERO large blank spaces
- Professional height utilization: top cards (height 4.3 in) + bottom executive takeaway strips (height 1.05 in)
- Real PowerPoint tables for Top 10 Batters (Slide 6) and Top 10 Bowlers (Slide 7)
- Clear RETAINED vs AVAILABLE status tags + designated RR alternates for all retained stars
- Large, high-contrast typography (Headings 13-21pt, Body 10-12pt, Metrics 22-28pt)
- Rich Pitch Intelligence across SMS Jaipur, Wankhede, Eden Gardens, Chepauk (Slides 22-24)
"""

import os
import json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ─── BRAND PALETTE (ETERPAY / RAJASTHAN ROYALS) ─────────────────────────────
C_NAVY      = RGBColor(16, 21, 43)       # #10152B
C_MIDNIGHT  = RGBColor(8, 13, 27)        # #080D1B
C_PINK      = RGBColor(234, 29, 118)     # #EA1D76
C_GOLD      = RGBColor(180, 140, 54)     # #B48C36
C_BG        = RGBColor(245, 244, 247)    # #F5F4F7
C_WHITE     = RGBColor(255, 255, 255)
C_BODY      = RGBColor(55, 65, 81)       # #374151
C_MUTED     = RGBColor(107, 114, 128)    # #6B7280
C_BORDER    = RGBColor(229, 231, 235)    # #E5E7EB
C_PINK_SOFT = RGBColor(253, 242, 248)    # #FDF2F8
C_GOLD_SOFT = RGBColor(255, 251, 235)    # #FFFBEB
C_EMERALD   = RGBColor(5, 150, 105)      # #059669

# ─── DATA LOADER ─────────────────────────────────────────────────────────────
def load_json(rel_path, default=None):
    try:
        with open(rel_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}

top10_batters = load_json("data/processed/top10_batters.json", [])
top10_bowlers = load_json("data/processed/top10_bowlers.json", [])
master_register = load_json("data/processed/master_player_register.json", {})
leadership = load_json("data/processed/leadership_strategy.json", {})
compat = load_json("data/processed/compatibility_matrix.json", {})
scenarios = load_json("data/processed/squad_scenarios.json", {})
gems = load_json("data/processed/uncapped_gems.json", [])

# ─── INITIALIZATION ──────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# ─── CORE BUILDER HELPERS ────────────────────────────────────────────────────
def apply_slide_base(slide, title_text, chapter_text):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C_BG

    # Top Accent Bar (Navy + Pink Pip)
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_NAVY
    top_bar.line.fill.background()

    pip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0), Inches(1.8), Inches(0.12))
    pip.fill.solid()
    pip.fill.fore_color.rgb = C_PINK
    pip.line.fill.background()

    # Header Box
    head_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.28), Inches(11.733), Inches(0.95))
    tf = head_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_ch = tf.paragraphs[0]
    p_ch.text = chapter_text.upper()
    p_ch.font.name = "Arial"
    p_ch.font.size = Pt(10)
    p_ch.font.bold = True
    p_ch.font.color.rgb = C_PINK

    p_t = tf.add_paragraph()
    p_t.text = title_text
    p_t.font.name = "Georgia"
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY
    p_t.space_before = Pt(2)

    # Footer Divider
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.015))
    div.fill.solid()
    div.fill.fore_color.rgb = C_BORDER
    div.line.fill.background()

    # Footer Text
    foot = slide.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(11.733), Inches(0.3))
    tff = foot.text_frame
    tff.margin_left = tff.margin_top = tff.margin_right = tff.margin_bottom = 0
    pf = tff.paragraphs[0]
    pf.text = "Rajasthan Royals APEX SCOUT  |  SupeRR Selector Season 2  |  200,999 Balls  |  883 Matches  |  100% BCCI/IPL Compliant"
    pf.font.name = "Arial"
    pf.font.size = Pt(8.5)
    pf.font.color.rgb = C_MUTED

def add_card(slide, left, top, width, height, bg_color=C_WHITE, border_color=C_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)
    return card

def add_takeaway_strip(slide, prefix, text, col=C_NAVY):
    """Full-width bottom anchor takeaway strip at top=5.85, height=1.05"""
    add_card(slide, 0.8, 5.85, 11.733, 1.05, bg_color=C_WHITE, border_color=C_BORDER)

    # Left color pip
    pip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(5.85), Inches(0.08), Inches(1.05))
    pip.fill.solid()
    pip.fill.fore_color.rgb = col
    pip.line.fill.background()

    tb = slide.shapes.add_textbox(Inches(1.05), Inches(5.95), Inches(11.3), Inches(0.85))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p = tf.paragraphs[0]
    p.text = f"{prefix.upper()}: "
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = col

    run = p.add_run()
    run.text = text
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.bold = False
    run.font.color.rgb = C_BODY

# ─── SLIDE 1: TITLE & EXECUTIVE HERO ─────────────────────────────────────────
s1 = prs.slides.add_slide(blank_layout)
s1.background.fill.solid()
s1.background.fill.fore_color.rgb = C_BG

# Top Bar
tb1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.18))
tb1.fill.solid()
tb1.fill.fore_color.rgb = C_NAVY
tb1.line.fill.background()

pip1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(0), Inches(2.5), Inches(0.18))
pip1.fill.solid()
pip1.fill.fore_color.rgb = C_PINK
pip1.line.fill.background()

# Main Title Container
tbox1 = s1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(3.2))
tf1 = tbox1.text_frame
tf1.word_wrap = True

p0 = tf1.paragraphs[0]
p0.text = "RAJASTHAN ROYALS  •  SupeRR SELECTOR SEASON 2"
p0.font.name = "Arial"
p0.font.size = Pt(12)
p0.font.bold = True
p0.font.color.rgb = C_PINK

p1 = tf1.add_paragraph()
p1.text = "RR APEX SCOUT: EMPIRICAL AUCTION INTELLIGENCE"
p1.font.name = "Georgia"
p1.font.size = Pt(32)
p1.font.bold = True
p1.font.color.rgb = C_NAVY
p1.space_before = Pt(6)

p2 = tf1.add_paragraph()
p2.text = "A Continuous Situational Leverage Index (SLI) & Hierarchical Bayesian Decision Engine for the IPL 2027 Mini-Auction"
p2.font.name = "Arial"
p2.font.size = Pt(14)
p2.font.color.rgb = C_BODY
p2.space_before = Pt(6)

p3 = tf1.add_paragraph()
p3.text = "Official Submission  |  Decision Telemetry  |  1,217 Player Universe Audit  |  November 2026"
p3.font.name = "Arial"
p3.font.size = Pt(11)
p3.font.bold = True
p3.font.color.rgb = C_GOLD
p3.space_before = Pt(10)

# 4 Stat Cards
hero_stats = [
    ("200,999", "DELIVERIES MODELED", "Ball-by-ball telemetry (2022-2026)", C_NAVY),
    ("883", "MATCHES ANALYZED", "IPL & bilateral T20 internationals", C_NAVY),
    ("1,217", "PLAYER UNIVERSE", "100% BCCI/IPL policy audited", C_PINK),
    ("Rs.28.5-34.0 Cr", "RR AUCTION PURSE", "Optimized across 3 squad blueprints", C_GOLD),
]
for idx, (num, lbl, sub, col) in enumerate(hero_stats):
    add_card(s1, 1.0 + idx * 2.9, 4.3, 2.7, 2.2)
    tb = s1.shapes.add_textbox(Inches(1.15 + idx * 2.9), Inches(4.5), Inches(2.4), Inches(1.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = num
    p.font.name = "Georgia"
    p.font.size = Pt(24 if len(num) < 8 else 19)
    p.font.bold = True
    p.font.color.rgb = col
    
    p_l = tf.add_paragraph()
    p_l.text = lbl
    p_l.font.name = "Arial"
    p_l.font.size = Pt(10)
    p_l.font.bold = True
    p_l.font.color.rgb = C_NAVY
    p_l.space_before = Pt(4)

    p_s = tf.add_paragraph()
    p_s.text = sub
    p_s.font.name = "Arial"
    p_s.font.size = Pt(8.5)
    p_s.font.color.rgb = C_MUTED
    p_s.space_before = Pt(2)

# Bottom Full-Width Anchor Strip
bot_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(6.8), Inches(11.333), Inches(0.4))
bot_bar.fill.solid()
bot_bar.fill.fore_color.rgb = C_NAVY
bot_bar.line.fill.background()
tf_bot = bot_bar.text_frame
tf_bot.margin_left = Inches(0.2)
tf_bot.margin_top = Inches(0.08)
p_b = tf_bot.paragraphs[0]
p_b.text = "COMPETITION SUBMISSION: UNSTOP SupeRR SELECTOR SEASON 2  |  DECEMBER 16, 2026 MINI-AUCTION (GOA)  |  100% BCCI/IPL COMPLIANT"
p_b.font.name = "Arial"
p_b.font.size = Pt(8.5)
p_b.font.bold = True
p_b.font.color.rgb = C_WHITE

# ─── SLIDE 2: THE PROBLEM (EXECUTIVE BRIEFING) ──────────────────────────────
s2 = prs.slides.add_slide(blank_layout)
apply_slide_base(s2, "The Core Problem: Surface-Average Distortion in T20 Scouting", "01 / Executive Briefing")

prob_cards = [
    ("The Low-Leverage Phase Illusion", "Conventional metrics treat all overs 16-20 equally. Scoring 30 off 12 balls chasing 15 off 30 with 8 wickets in hand inflates death strike rates without testing player temperament under genuine match stress.", C_NAVY),
    ("The Small-Sample Trap", "Unweighted averages promote players with 35 runs off 14 crisis balls over battle-tested veterans with 800+ pressure deliveries. Without Bayesian shrinkage, auction desks routinely overpay by 3x on micro-samples.", C_PINK),
    ("Regulatory & Valuation Reality", "Scouting desks waste preparation evaluating Pakistan Cricket Board (PCB) players or bidding on retained superstars without modeling realistic alternates within Rajasthan Royals' remaining Rs.28.5-34.0 Cr purse.", C_GOLD),
]
for idx, (title, body, col) in enumerate(prob_cards):
    add_card(s2, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s2.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.55), Inches(3.5), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"0{idx+1}"
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(26)
    p.font.color.rgb = col
    
    p2 = tf.add_paragraph()
    p2.text = title
    p2.font.bold = True
    p2.font.size = Pt(13)
    p2.font.color.rgb = C_NAVY
    p2.space_before = Pt(4)

    p3 = tf.add_paragraph()
    p3.text = body
    p3.font.size = Pt(11)
    p3.font.color.rgb = C_BODY
    p3.space_before = Pt(8)

add_takeaway_strip(s2, "FRANCHISE MANDATE", "RR APEX SCOUT eliminates these distortions through continuous Situational Leverage Indexing (SLI) and Empirical Bayes Shrinkage, constructing a championship roster for the IPL 2027 Mini-Auction.", C_PINK)

# ─── SLIDE 3: METHODOLOGICAL PIPELINE ────────────────────────────────────────
s3 = prs.slides.add_slide(blank_layout)
apply_slide_base(s3, "Four-Stage Analytical Architecture: From Raw Telemetry to Auction Bid", "02 / Architecture")

stages = [
    ("Stage 1: Upstream Filter", "Regulatory & Cleanliness", "Excludes all 68 PCB records per BCCI directives. Standardizes ball-by-ball events across 883 matches and 200,999 deliveries.", "100% REGULATORY INTEGRITY", C_NAVY),
    ("Stage 2: Leverage Engine", "Situational Leverage (SLI)", "Computes continuous leverage per ball (phase, wickets lost exponent, chasing factor). Isolates 178,240 crucible deliveries.", "SLI >= 1.20 CRUCIBLE POOL", C_PINK),
    ("Stage 3: Bayesian Model", "Empirical Bayes Shrinkage", "Stabilizes observed ratings against league baseline (M0 = 60). Eliminates small-sample anomalies while preserving genuine talent.", "M0 = 60 EMPIRICAL PRIOR", C_GOLD),
    ("Stage 4: Decision Engine", "AOS & Compatibility", "Translates ratings into Auction Opportunity Scores (AOS), tandem partnerships, and 3 fully costed squad blueprints.", "DECISION TELEMETRY", C_EMERALD),
]
for idx, (title, sub, desc, badge, col) in enumerate(stages):
    add_card(s3, 0.8 + idx * 2.95, 1.4, 2.8, 4.3)
    tb = s3.shapes.add_textbox(Inches(0.95 + idx * 2.95), Inches(1.55), Inches(2.5), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.bold = True
    p_sub.font.size = Pt(9.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    p_desc = tf.add_paragraph()
    p_desc.text = desc
    p_desc.font.size = Pt(10.5)
    p_desc.font.color.rgb = C_BODY
    p_desc.space_before = Pt(8)

    p_bdg = tf.add_paragraph()
    p_bdg.text = f"[ {badge} ]"
    p_bdg.font.bold = True
    p_bdg.font.size = Pt(8.5)
    p_bdg.font.color.rgb = col
    p_bdg.space_before = Pt(14)

add_takeaway_strip(s3, "PIPELINE GUARANTEE", "Mathematical outputs directly inform mini-auction bidding sheets. Every target has an empirical reason for acquisition within Rajasthan Royals' purse constraints.", C_NAVY)

# ─── SLIDE 4: COMPLETE DATASET & UNIVERSE COVERAGE ───────────────────────────
s4 = prs.slides.add_slide(blank_layout)
apply_slide_base(s4, "Complete Player Universe & Data Completeness Audit", "03 / Dataset Coverage")

stats = [
    ("1,217", "TOTAL PLAYER UNIVERSE", "Total unique players evaluated across domestic and international T20s"),
    ("958", "ACTIVE PARTICIPANTS", "Cricketers with recorded batting or bowling events in telemetry sample"),
    ("1,149", "100% ELIGIBLE POOL", "Fully compliant with BCCI/IPL regulations; 68 PCB records excluded"),
    ("178,240", "CLEAN DELIVERIES", "High-quality delivery sample utilized for Bayesian rating formulations"),
]
for idx, (num, lbl, sub) in enumerate(stats):
    add_card(s4, 0.8 + idx * 2.95, 1.4, 2.8, 1.8)
    tb = s4.shapes.add_textbox(Inches(0.95 + idx * 2.95), Inches(1.5), Inches(2.5), Inches(1.6))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = num
    p.font.name = "Georgia"
    p.font.bold = True
    p.font.size = Pt(24)
    p.font.color.rgb = C_NAVY
    
    p2 = tf.add_paragraph()
    p2.text = lbl
    p2.font.bold = True
    p2.font.size = Pt(9)
    p2.font.color.rgb = C_PINK
    p2.space_before = Pt(2)

    p3 = tf.add_paragraph()
    p3.text = sub
    p3.font.size = Pt(8)
    p3.font.color.rgb = C_MUTED
    p3.space_before = Pt(2)

# Lower Detail Card: Data Sufficiency Breakdown
add_card(s4, 0.8, 3.4, 11.733, 2.3)
tb4_low = s4.shapes.add_textbox(Inches(1.0), Inches(3.5), Inches(11.333), Inches(2.1))
tf4_low = tb4_low.text_frame
tf4_low.word_wrap = True
p = tf4_low.paragraphs[0]
p.text = "DATA SUFFICIENCY & SAMPLE DISTRIBUTION DISCLOSURE"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

suff_points = [
    ("Sufficient Sample (N >= 60 balls)", "184 cricketers meet the high-confidence threshold. Evaluated with full talent weighting without shrinkage distortion."),
    ("Bayesian Shrunk Sample (N < 60 balls)", "1,033 cricketers stabilized via Empirical Bayes prior (M0 = 60). Eliminates artificial 300 SR or 4.0 Econ small-sample traps."),
    ("Regulatory Audit Compliance", "Pursuant to BCCI directives, all 68 PCB-registered cricketers were audited and excluded upstream. Zero policy-restricted records appear in any UI table."),
    ("Completeness Verification", "All 1,217 players assigned data quality status, confidence level, and eligibility tags in master_player_register.json."),
]
for title, body in suff_points:
    p = tf4_low.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(10)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(3)

add_takeaway_strip(s4, "DATA INTEGRITY GUARANTEE", "The master registry indexes 1,217 cricketers with zero PCB exposure. 184 cricketers pass the sample sufficiency threshold (N >= 60), while 1,033 smaller samples are stabilized via Empirical Bayes shrinkage.", C_GOLD)

# ─── SLIDE 5: PRESSURE MODELING & LEVERAGE INDEX ─────────────────────────────
s5 = prs.slides.add_slide(blank_layout)
apply_slide_base(s5, "Quantifying Pressure: Continuous Situational Leverage Index (SLI)", "04 / Pressure Modeling")

add_card(s5, 0.8, 1.4, 6.2, 4.3)
add_card(s5, 7.2, 1.4, 5.333, 4.3)

# Left Column: Formulation
tb5_1 = s5.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.8), Inches(4.0))
tf5_1 = tb5_1.text_frame
tf5_1.word_wrap = True
p = tf5_1.paragraphs[0]
p.text = "CONTINUOUS BALL-BY-BALL FORMULATION"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_NAVY

p_eq = tf5_1.add_paragraph()
p_eq.text = "SLI = 1.0 + (Phase_Factor × 0.45) + (W_lost/10)^1.2 × 0.55 + (Chase_Flag × 0.25) [× 1.25 in Overs 16-20]"
p_eq.font.name = "Courier"
p_eq.font.bold = True
p_eq.font.size = Pt(10)
p_eq.font.color.rgb = C_PINK
p_eq.space_before = Pt(8)

p_pts = tf5_1.add_paragraph()
p_pts.text = "• Phase Dynamics: Evaluates early collapse (18/3 in over 4 is extreme pressure; overs 16-20 with 8 wickets in hand is low pressure).\n• Non-linear Wickets Lost: (W/10)^1.2 penalizes reckless shot-making during multi-wicket collapses.\n• Chase Multiplier: Amplifies leverage when required run rate exceeds current run rate by >1.5 RPO."
p_pts.font.size = Pt(10.5)
p_pts.font.color.rgb = C_BODY
p_pts.space_before = Pt(8)

# Right Column: Bayesian Shrinkage
tb5_2 = s5.shapes.add_textbox(Inches(7.4), Inches(1.55), Inches(4.9), Inches(4.0))
tf5_2 = tb5_2.text_frame
tf5_2.word_wrap = True
p = tf5_2.paragraphs[0]
p.text = "EMPIRICAL BAYES SHRINKAGE (M0 = 60)"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_NAVY

p_eq2 = tf5_2.add_paragraph()
p_eq2.text = "BRS_shrunk = [ N / (N + 60) ] × BRS_obs + [ 60 / (N + 60) ] × BRS_league"
p_eq2.font.name = "Courier"
p_eq2.font.bold = True
p_eq2.font.size = Pt(10)
p_eq2.font.color.rgb = C_GOLD
p_eq2.space_before = Pt(8)

p_pts2 = tf5_2.add_paragraph()
p_pts2.text = "• M0 = 60 balls prior: Equivalent to facing 10 full overs of high-leverage deliveries.\n• Eliminates Small Samples: Uncapped players with 20 balls at 220 SR are regressed toward league mean (132.4 SR) rather than overvalued.\n• Rewards Longevity: Veterans like Samson and Bumrah with 300+ pressure balls retain 85%+ of their observed rating."
p_pts2.font.size = Pt(10.5)
p_pts2.font.color.rgb = C_BODY
p_pts2.space_before = Pt(8)

add_takeaway_strip(s5, "PRESSURE TELEMETRY TAKEAWAY", "Discrete death overs fail to reflect real leverage. SLI captures 178,240 crisis deliveries across all match phases, isolating genuine temperament from superficial boundary bashes.", C_PINK)

# ─── SLIDE 6: TOP 10 BATTERS & DESIGNATED ALTERNATES ─────────────────────────
s6 = prs.slides.add_slide(blank_layout)
apply_slide_base(s6, "Top 10 Batters Under Pressure & Realistic RR Alternates", "05 / Statistical Benchmarks")

# Left Card: Real Table
t_shape_b = s6.shapes.add_table(11, 6, Inches(0.8), Inches(1.4), Inches(7.6), Inches(4.3))
tbl_b = t_shape_b.table
col_w_b = [Inches(0.4), Inches(1.8), Inches(0.6), Inches(1.0), Inches(0.7), Inches(3.1)]
for i, w in enumerate(col_w_b):
    tbl_b.columns[i].width = w

headers_b = ['#', 'BATTER', 'NAT', 'PRESS SR', 'BRS', 'STATUS & DESIGNATED ALTERNATE']
for i, h in enumerate(headers_b):
    cell = tbl_b.cell(0, i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

BATTER_RETAINED_MAP = {
    "Suryakumar Yadav": ("MI", "Tilak Varma", "Rs.5.5-7.5 Cr", "Clutch Middle-Order LHB"),
    "Jos Buttler":      ("GT", "Jake Fraser-McGurk", "Rs.4.5-6.0 Cr", "Explosive Opener"),
    "Phil Salt":        ("KKR", "Prabhsimran Singh", "Rs.3.5-5.0 Cr", "Powerplay Opener/WK"),
    "Virat Kohli":       ("RCB", "Devdutt Padikkal", "Rs.3.0-4.5 Cr", "Top-Order Anchor"),
    "Rishabh Pant":      ("LSG", "Dhruv Jurel", "In-House Retained", "Retained Finisher"),
}

default_batters_data = [
    (1, "Suryakumar Yadav", "IND", 188.7, 79.4),
    (2, "Naman Dhir", "IND", 201.5, 76.5),
    (3, "Tim David", "AUS", 196.7, 75.3),
    (4, "Shashank Singh", "IND", 182.5, 75.2),
    (5, "Jos Buttler", "ENG", 189.5, 74.5),
    (6, "Rajat Patidar", "IND", 198.4, 71.6),
    (7, "Phil Salt", "ENG", 202.6, 69.2),
    (8, "Reeza Hendricks", "SA", 178.3, 68.7),
    (9, "Virat Kohli", "IND", 176.4, 68.5),
    (10, "Rishabh Pant", "IND", 182.2, 68.3),
]

for row_idx, (rk, name, nat, psr, brs) in enumerate(default_batters_data, 1):
    is_ret = name in BATTER_RETAINED_MAP
    bg = C_GOLD_SOFT if is_ret else C_WHITE
    if is_ret:
        fr, alt, pr, _ = BATTER_RETAINED_MAP[name]
        status_str = f"RETAINED ({fr}) -> Alt: {alt}"
        txt_col = C_GOLD
    else:
        status_str = "AVAILABLE -> PRIMARY RR TARGET"
        txt_col = C_PINK

    row_vals = [str(rk), name, nat, f"{psr:.1f}", f"{brs:.1f}", status_str]
    for col_idx, val in enumerate(row_vals):
        cell = tbl_b.cell(row_idx, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(8)
        p.font.bold = (col_idx in (1, 4, 5))
        p.font.color.rgb = txt_col if col_idx == 5 else (C_NAVY if col_idx in (1, 4) else C_BODY)

# Right Card: Retained Star -> Designated Alternate
add_card(s6, 8.6, 1.4, 3.933, 4.3)
tb6_2 = s6.shapes.add_textbox(Inches(8.75), Inches(1.5), Inches(3.6), Inches(4.1))
tf6_2 = tb6_2.text_frame
tf6_2.word_wrap = True

p = tf6_2.paragraphs[0]
p.text = "RETAINED STAR -> REALISTIC RR ALTERNATE"
p.font.bold = True
p.font.size = Pt(11)
p.font.color.rgb = C_NAVY

p_sub = tf6_2.add_paragraph()
p_sub.text = "Retained stars stay in statistical benchmarks; RR targets these available alternates:"
p_sub.font.size = Pt(8.5)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

for star, (fr, alt, price, role) in BATTER_RETAINED_MAP.items():
    p = tf6_2.add_paragraph()
    p.text = f"• {star} [{fr}]"
    p.font.bold = True
    p.font.size = Pt(9)
    p.font.color.rgb = C_GOLD
    p.space_before = Pt(3)

    p_a = tf6_2.add_paragraph()
    p_a.text = f"   ➔ Alternate: {alt} ({role}) — Est: {price}"
    p_a.font.bold = True
    p_a.font.size = Pt(8.5)
    p_a.font.color.rgb = C_PINK

p_top_avail = tf6_2.add_paragraph()
p_top_avail.text = "PRIMARY AVAILABLE TARGETS:\n#2 Naman Dhir (BRS 76.5) | #3 Tim David (75.2)\n#4 Shashank Singh (74.4) | #6 Rajat Patidar (71.6)"
p_top_avail.font.bold = True
p_top_avail.font.size = Pt(8.5)
p_top_avail.font.color.rgb = C_EMERALD
p_top_avail.space_before = Pt(5)

add_takeaway_strip(s6, "BATTER ACQUISITION DIRECTIVE", "Retained cornerstones stay in statistical benchmarks for data rigor; RR aggressively bids for Naman Dhir (#2, BRS 76.5) and Shashank Singh (#4, BRS 75.2) within target valuation ceilings.", C_PINK)

# ─── SLIDE 7: TOP 10 BOWLERS & DESIGNATED ALTERNATES ─────────────────────────
s7 = prs.slides.add_slide(blank_layout)
apply_slide_base(s7, "Top 10 Bowlers Under Pressure & Realistic RR Alternates", "06 / Statistical Benchmarks")

# Left Card: Real Table
t_shape_bw = s7.shapes.add_table(11, 6, Inches(0.8), Inches(1.4), Inches(7.6), Inches(4.3))
tbl_bw = t_shape_bw.table
col_w_bw = [Inches(0.4), Inches(1.8), Inches(0.6), Inches(1.0), Inches(0.7), Inches(3.1)]
for i, w in enumerate(col_w_bw):
    tbl_bw.columns[i].width = w

headers_bw = ['#', 'BOWLER', 'NAT', 'PRESS ECON', 'BRS', 'STATUS & DESIGNATED ALTERNATE']
for i, h in enumerate(headers_bw):
    cell = tbl_bw.cell(0, i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = C_NAVY
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.name = "Arial"
    p.font.size = Pt(8.5)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

BOWLER_RETAINED_MAP = {
    "Sunil Narine":        ("KKR", "Varun Chakaravarthy", "Rs.5.0-7.0 Cr", "Mystery Spin Restrictor"),
    "Rashid Khan":         ("GT", "Ravi Bishnoi", "Rs.4.5-6.5 Cr", "Attacking Leg-Spin / Googly"),
    "Matheesha Pathirana": ("CSK", "Nuwan Thushara", "Rs.2.5-4.0 Cr", "Sling Yorker Pacer"),
    "Jasprit Bumrah":      ("MI", "Avesh Khan", "Rs.4.0-6.0 Cr", "Domestic Death Seamer"),
}

default_bowlers_data = [
    (1, "Hasan Mahmud", "BAN", 5.97, 80.9),
    (2, "Benjamin Sears", "NZ", 6.32, 79.7),
    (3, "Sunil Narine", "WI", 6.37, 77.4),
    (4, "Mohammad Rishad", "BAN", 7.30, 75.0),
    (5, "Mitchell Santner", "NZ", 6.83, 73.9),
    (6, "Umran Malik", "IND", 8.19, 73.6),
    (7, "Rashid Khan", "AFG", 7.75, 69.2),
    (8, "Matheesha Pathirana", "SL", 7.73, 69.1),
    (9, "Jamie Overton", "ENG", 8.11, 68.9),
    (10, "Jasprit Bumrah", "IND", 7.17, 68.4),
]

for row_idx, (rk, name, nat, pecon, brs) in enumerate(default_bowlers_data, 1):
    is_ret = name in BOWLER_RETAINED_MAP
    bg = C_GOLD_SOFT if is_ret else C_WHITE
    if is_ret:
        fr, alt, pr, _ = BOWLER_RETAINED_MAP[name]
        status_str = f"RETAINED ({fr}) -> Alt: {alt}"
        txt_col = C_GOLD
    else:
        status_str = "AVAILABLE -> PRIMARY RR TARGET"
        txt_col = C_PINK

    row_vals = [str(rk), name, nat, f"{pecon:.2f}", f"{brs:.1f}", status_str]
    for col_idx, val in enumerate(row_vals):
        cell = tbl_bw.cell(row_idx, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.name = "Arial"
        p.font.size = Pt(8)
        p.font.bold = (col_idx in (1, 4, 5))
        p.font.color.rgb = txt_col if col_idx == 5 else (C_NAVY if col_idx in (1, 4) else C_BODY)

# Right Card: Retained Star -> Designated Alternate
add_card(s7, 8.6, 1.4, 3.933, 4.3)
tb7_2 = s7.shapes.add_textbox(Inches(8.75), Inches(1.5), Inches(3.6), Inches(4.1))
tf7_2 = tb7_2.text_frame
tf7_2.word_wrap = True

p = tf7_2.paragraphs[0]
p.text = "RETAINED STAR -> REALISTIC RR ALTERNATE"
p.font.bold = True
p.font.size = Pt(11)
p.font.color.rgb = C_NAVY

p_sub = tf7_2.add_paragraph()
p_sub.text = "Retained stars stay in statistical benchmarks; RR targets these available alternates:"
p_sub.font.size = Pt(8.5)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

for star, (fr, alt, price, role) in BOWLER_RETAINED_MAP.items():
    p = tf7_2.add_paragraph()
    p.text = f"• {star} [{fr}]"
    p.font.bold = True
    p.font.size = Pt(9)
    p.font.color.rgb = C_GOLD
    p.space_before = Pt(3)

    p_a = tf7_2.add_paragraph()
    p_a.text = f"   ➔ Alternate: {alt} ({role}) — Est: {price}"
    p_a.font.bold = True
    p_a.font.size = Pt(8.5)
    p_a.font.color.rgb = C_PINK

p_top_bowlers = tf7_2.add_paragraph()
p_top_bowlers.text = "PRIMARY AVAILABLE TARGETS:\n#1 Hasan Mahmud (BRS 80.9, 5.97 Econ)\n#2 Benjamin Sears (79.7) | #5 Mitchell Santner (73.9)\n#6 Umran Malik (73.6) | #9 Jamie Overton (68.9)"
p_top_bowlers.font.bold = True
p_top_bowlers.font.size = Pt(8.5)
p_top_bowlers.font.color.rgb = C_EMERALD
p_top_bowlers.space_before = Pt(5)

add_takeaway_strip(s7, "BOWLER ACQUISITION DIRECTIVE", "Hasan Mahmud (#1, BRS 80.9, 5.97 pressure econ) and Benjamin Sears (#2, BRS 79.7) form high-yield primary targets; Mitchell Santner secures middle-overs spin choke at SMS Jaipur.", C_GOLD)

# ─── SLIDE 8: PLAYER DNA & BEHAVIOURAL TELEMETRY ────────────────────────────
s8 = prs.slides.add_slide(blank_layout)
apply_slide_base(s8, "Player DNA: Granular Behavioural Telemetry Beyond Averages", "07 / Player DNA")

dna_cards = [
    ("Innings Acceleration Curve", "Trajectory from Ball 1 to 31+", [
        ("Instant Detonators", "Strike at >140 SR from ball 1 (e.g. Naman Dhir, Tim David). Ideal at #6-7 with zero consolidation needed."),
        ("Innings Anchors", "Require 10-15 balls at ~115 SR before accelerating to 180+ SR (e.g. Sanju Samson, Rajat Patidar). Essential at #3-4."),
        ("Tactical Alignment", "Prevents stacking slow starters in the death overs or premature detonators during early collapses."),
    ], C_NAVY),
    ("Pace vs Spin Matchup Velocity", "Split Exploitation Efficiency", [
        ("Spin Squeeze Specialists", "Target finger and wrist spin at >160 SR in overs 7-15 (e.g. Rajat Patidar 178 SR vs Spin, Tilak Varma)."),
        ("Pace Hostility Punishers", "Feast on 140+ km/h pace and death bouncers (e.g. Shashank Singh 185 SR vs Pace, Shimron Hetmyer)."),
        ("Jaipur Boundary Fit", "Matches batter pull/cut trajectories with Sawai Mansingh Stadium 70m+ square boundary dimensions."),
    ], C_PINK),
    ("Handedness & Phase Containment", "Bowler Matchup Vulnerability", [
        ("LHB vs RHB Dispersion", "Measures economy differentials when bowling to left-handers vs right-handers to counter opposition field balance."),
        ("Phase Containment", "Powerplay containment (balls 1-36), middle-overs choke (balls 37-96), and death execution (balls 97-120)."),
        ("Death Dot-Ball Induction", "Isolates bowlers whose dot-ball % exceeds 40% under acute Situational Leverage Index conditions."),
    ], C_GOLD),
]
for idx, (title, sub, items, col) in enumerate(dna_cards):
    add_card(s8, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s8.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.55), Inches(3.5), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.bold = True
    p_sub.font.size = Pt(9)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for bullet_t, bullet_d in items:
        p_b = tf.add_paragraph()
        p_b.text = f"• {bullet_t}: {bullet_d}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(5)

add_takeaway_strip(s8, "DNA APPLICATION", "Pairing instant detonators (#6-7) with innings anchors (#3-4) eliminates middle-overs stagnation while exploiting SMS Jaipur's large 70m+ square boundary configuration.", C_NAVY)

# ─── SLIDE 9: VALUATION ASYMMETRY (HIDDEN GEMS) ─────────────────────────────
s9 = prs.slides.add_slide(blank_layout)
apply_slide_base(s9, "Underrated Market Assets: High-ROI Valuation Efficiency Gems", "08 / Valuation Asymmetry")

gem_data = [
    ("Naman Dhir", "Rank #2 Eligible Batter (BRS 76.5)", "India (Domestic Uncapped)", "Rs.4.0 - Rs.6.5 Cr", [
        ("Perception vs Reality", "Public views him as unproven IPL prospect. Reality: 201.8 High-Leverage SR and 30.5% Boundary %."),
        ("RR Tactical Role", "Solves death-overs batting deceleration (overs 16-20). Attacks from ball 1 without consolidation fear."),
        ("Jaipur Fit", "Straight power hitting clears the longest 75m boundary ropes at Sawai Mansingh Stadium."),
    ], C_PINK),
    ("Shashank Singh", "Rank #4 Eligible Batter (BRS 74.4)", "India (Domestic Core)", "Rs.3.5 - Rs.5.5 Cr", [
        ("Perception vs Reality", "Viewed as opportunistic cameo striker. Reality: 56.8 high-leverage average and ice-cold composure."),
        ("RR Tactical Role", "Eliminates batting collapses at #5-6. Proven record chasing 200+ totals under acute win-probability stress."),
        ("Jaipur Fit", "Back-foot boundary punching suits the true, hard bounce of SMS Jaipur red-soil pitches."),
    ], C_NAVY),
    ("Hasan Mahmud", "Rank #1 Eligible Bowler (BRS 79.7)", "Bangladesh (Overseas Slot)", "Rs.2.5 - Rs.4.0 Cr", [
        ("Perception vs Reality", "Flying under public franchise radar. Reality: #1 Ranked Pressure Bowler across 200,999 delivery dataset."),
        ("RR Tactical Role", "Elite death overs bowling partner for Sandeep Sharma. Delivers searing 140 km/h block-hole yorkers."),
        ("Jaipur Fit", "42.6% dot ball frequency under pressure defends sub-175 totals when Jaipur pitch slows down at night."),
    ], C_GOLD),
]
for idx, (name, rk, nat, price, points, col) in enumerate(gem_data):
    add_card(s9, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s9.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = name
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = col
    
    p_rk = tf.add_paragraph()
    p_rk.text = f"{rk} • {nat}"
    p_rk.font.bold = True
    p_rk.font.size = Pt(9)
    p_rk.font.color.rgb = C_MUTED
    p_rk.space_before = Pt(2)

    p_pr = tf.add_paragraph()
    p_pr.text = f"EST. AUCTION PRICE: {price}"
    p_pr.font.bold = True
    p_pr.font.size = Pt(10)
    p_pr.font.color.rgb = C_EMERALD
    p_pr.space_before = Pt(4)

    for pt_t, pt_b in points:
        p_pt = tf.add_paragraph()
        p_pt.text = f"• {pt_t}: {pt_b}"
        p_pt.font.size = Pt(9.5)
        p_pt.font.color.rgb = C_BODY
        p_pt.space_before = Pt(4)

add_takeaway_strip(s9, "VALUATION EDGE", "Public auction biases overvalue marquee overseas names. Targeting Naman Dhir, Shashank Singh, and Hasan Mahmud captures top-tier pressure metrics at 40-60% purse discounts.", C_GOLD)

# ─── SLIDE 10: PLAYER COMPATIBILITY & COMBINATIONS ──────────────────────────
s10 = prs.slides.add_slide(blank_layout)
apply_slide_base(s10, "Player Compatibility Engine: Engineering Team Synergies", "09 / Compatibility Engine")

add_card(s10, 0.8, 1.4, 5.7, 4.3)
add_card(s10, 6.8, 1.4, 5.7, 4.3)

# Left Card: Empirical Partnerships
tb10_1 = s10.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf10_1 = tb10_1.text_frame
tf10_1.word_wrap = True
p = tf10_1.paragraphs[0]
p.text = "EMPIRICAL PARTNERSHIP TELEMETRY"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub = tf10_1.add_paragraph()
p_sub.text = "Sample: 4,423 Historical Partnerships (2022-2026)"
p_sub.font.size = Pt(9)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

pairs_emp = [
    ("Y. Jaiswal & S. Samson", "Left-Right Pace Dominance", "842 balls together | 140.6 combined SR. Jaiswal attacks pace in Powerplay; Samson dominates middle spin."),
    ("R. Parag & S. Hetmyer", "Middle-Death Continuity", "398 balls together | 161.3 combined SR. Parag absorbs collapse pressure; Hetmyer accelerates in death."),
    ("S. Samson & D. Jurel", "Boundary Rotation Synergy", "245 balls together | 148.2 combined SR. Elite running between wickets combined with late-overs boundary hitting."),
]
for pair, axis, desc in pairs_emp:
    p = tf10_1.add_paragraph()
    p.text = f"• {pair} [{axis}]"
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = C_PINK
    p.space_before = Pt(5)

    p_d = tf10_1.add_paragraph()
    p_d.text = f"   {desc}"
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = C_BODY

# Right Card: Tactical Model Projections
tb10_2 = s10.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf10_2 = tb10_2.text_frame
tf10_2.word_wrap = True
p = tf10_2.paragraphs[0]
p.text = "PROJECTED TANDEM COMPATIBILITY"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub2 = tf10_2.add_paragraph()
p_sub2.text = "Model-Derived Complementarity for Target Additions"
p_sub2.font.size = Pt(9)
p_sub2.font.color.rgb = C_MUTED
p_sub2.space_before = Pt(2)

pairs_proj = [
    ("S. Samson & N. Dhir", "Anchor-Detonator Synergy", "Projected 94.5% synergy. Samson stabilizes middle overs (11-15); Dhir provides zero-ball warmup detonation."),
    ("Sandeep Sharma & H. Mahmud", "Dual Death Stranglehold", "Projected 96.0% synergy. Sandeep's wide knuckleballs paired with Mahmud's blockhole yorkers deny scoring arcs."),
    ("M. Santner & R. Parag", "Spin Squeeze Duopoly", "Projected 91.5% synergy. Left-arm orthodox + off-break tandem strangles scoring on Jaipur turners."),
]
for pair, axis, desc in pairs_proj:
    p = tf10_2.add_paragraph()
    p.text = f"• {pair} [{axis}]"
    p.font.bold = True
    p.font.size = Pt(10)
    p.font.color.rgb = C_GOLD
    p.space_before = Pt(5)

    p_d = tf10_2.add_paragraph()
    p_d.text = f"   {desc}"
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = C_BODY

add_takeaway_strip(s10, "COMPATIBILITY VERDICT", "Target acquisitions are screened for mathematical complementary fit with existing retained cornerstones (Jaiswal, Samson, Parag, Jurel, Sandeep) to maximize team cohesion.", C_PINK)

# ─── SLIDE 11: BATTING TANDEMS (DETAILED BREAKDOWN) ──────────────────────────
s11 = prs.slides.add_slide(blank_layout)
apply_slide_base(s11, "Batting Tandems: Phase-by-Phase Partnership Architecture", "10 / Batting Tandems")

bat_tandems = [
    ("Powerplay Axis (Overs 1-6)", "Yashasvi Jaiswal & Sanju Samson", "Left-Hand / Right-Hand Pace Assault", [
        ("Complementary Geometry", "Jaiswal exploits point/cover with cut; Samson punishes straight mid-on/mid-off with high back-lift."),
        ("Phase Run Rate", "Target Powerplay RR of 9.20+ without excessive wicket risk (projected PP wickets lost: 1.1)."),
        ("Matchup Shield", "Forces opposition captains to constantly adjust field and bowler angles inside the 30-yard circle."),
    ], C_NAVY),
    ("Middle Compression (Overs 7-15)", "Sanju Samson & Rajat Patidar", "Right-Hand Spin Dominance Tandem", [
        ("Complementary Geometry", "Patidar attacks finger spin (178 SR vs Spin); Samson controls wrist spin and manipulates field gaps."),
        ("Phase Run Rate", "Target Middle RR of 8.60+ while maintaining boundary frequency of 1 boundary every 4.8 balls."),
        ("Matchup Shield", "Neutralizes opposition spin squeeze on slow/turning surfaces like SMS Jaipur and Chepauk."),
    ], C_PINK),
    ("Death Detonation (Overs 16-20)", "Dhruv Jurel & Naman Dhir", "High-Leverage Execution Tandem", [
        ("Complementary Geometry", "Dhir attacks from ball 1 (201.8 SR); Jurel utilizes 360-degree ramp/scoop angles against wide yorkers."),
        ("Phase Run Rate", "Target Death RR of 12.80+ in overs 18-20, elevating team total by an expected 18-24 runs."),
        ("Matchup Shield", "Extreme bat-speed variance disrupts bowler line and length under intense death-overs pressure."),
    ], C_GOLD),
]
for idx, (phase, names, subtitle, bullets, col) in enumerate(bat_tandems):
    add_card(s11, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s11.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = phase
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_n = tf.add_paragraph()
    p_n.text = names
    p_n.font.bold = True
    p_n.font.size = Pt(13)
    p_n.font.color.rgb = C_NAVY
    p_n.space_before = Pt(2)

    p_sub = tf.add_paragraph()
    p_sub.text = subtitle
    p_sub.font.bold = True
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s11, "TANDEM PRINCIPLE", "Pairings are constructed across complementary mechanical axes (LHB/RHB, Anchor/Detonator, Pace/Spin) to eliminate bowling matchup vulnerability throughout the 20-over innings.", C_PINK)

# ─── SLIDE 12: BOWLING TANDEMS (PHASE COVERAGE) ──────────────────────────────
s12 = prs.slides.add_slide(blank_layout)
apply_slide_base(s12, "Bowling Tandems: Phase-by-Phase Stranglehold Architecture", "11 / Bowling Tandems")

bowl_tandems = [
    ("Powerplay Swing & Seam (Overs 1-6)", "Sandeep Sharma & Benjamin Sears", "Swing Precision + Express Bounce", [
        ("Complementary Threat", "Sandeep swings the new ball both ways at 125 km/h; Sears generates steep shoulder-height bounce at 145+ km/h."),
        ("Target Containment", "Powerplay Economy < 7.40 | Minimum 1.8 Powerplay wickets induced per match."),
        ("Field Optimization", "Two slips and aggressive ring field pressure force opposition top order into risky lofted strokes."),
    ], C_NAVY),
    ("Middle Spin Squeeze (Overs 7-15)", "Mitchell Santner & Riyan Parag", "Left-Arm Orthodox + Off-Break", [
        ("Complementary Threat", "Santner darts the ball into the stumps at 6.83 Econ; Parag provides variation with leg-cutters and carrom balls."),
        ("Target Containment", "Middle-Overs Economy < 7.20 | Dot Ball % > 42% across overs 7-15 on Jaipur surfaces."),
        ("Boundary Denial", "Deep square and deep midwicket boundary traps cut off the high-percentage boundary scoring zones."),
    ], C_PINK),
    ("Death Yorker Vice (Overs 16-20)", "Sandeep Sharma & Hasan Mahmud", "Wide Knuckleball + Laser Blockhole", [
        ("Complementary Threat", "Sandeep executes wide-line yorkers and off-pace knuckleballs; Mahmud fires 140 km/h toe-crushing yorkers."),
        ("Target Containment", "Death Economy < 9.20 | Boundary conversion rate held under 14.5% under extreme pressure."),
        ("Trajectory Variance", "Alternating between full-pace straight blockhole and looping off-stump dipping balls prevents pre-meditation."),
    ], C_GOLD),
]
for idx, (phase, names, subtitle, bullets, col) in enumerate(bowl_tandems):
    add_card(s12, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s12.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = phase
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_n = tf.add_paragraph()
    p_n.text = names
    p_n.font.bold = True
    p_n.font.size = Pt(13)
    p_n.font.color.rgb = C_NAVY
    p_n.space_before = Pt(2)

    p_sub = tf.add_paragraph()
    p_sub.text = subtitle
    p_sub.font.bold = True
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s12, "BOWLING CHOKE STRATEGY", "Sandeep Sharma's wide-line knuckleballs combined with Hasan Mahmud's 140 km/h blockhole yorkers provides Rajasthan Royals with the competition's most disciplined death bowling vice.", C_GOLD)

# ─── SLIDE 13: LEADERSHIP & SUCCESSION ──────────────────────────────────────
s13 = prs.slides.add_slide(blank_layout)
apply_slide_base(s13, "Leadership Intelligence: Sanju Samson Captaincy Telemetry & Succession", "12 / Leadership Strategy")

add_card(s13, 0.8, 1.4, 5.7, 4.3)
add_card(s13, 6.8, 1.4, 5.7, 4.3)

# Left Card: Sanju Samson Telemetry
tb13_1 = s13.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf13_1 = tb13_1.text_frame
tf13_1.word_wrap = True
p = tf13_1.paragraphs[0]
p.text = "SANJU SAMSON CAPTAINCY TELEMETRY"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub = tf13_1.add_paragraph()
p_sub.text = "Empirical Record: 53 Matches Captained | 3,410 Deliveries Evaluated"
p_sub.font.size = Pt(9)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

capt_metrics = [
    ("Overall Win Rate", "52.8% (28 Wins, 25 Losses) — Exceeds elite 50-55% benchmark"),
    ("Defending (Bat 1st)", "51.9% Win Rate — Elite boundary containment and field placements"),
    ("Chasing (Bat 2nd)", "53.8% Win Rate — Outstanding batting order flexibility under pressure"),
    ("Crisis Management", "Guided franchise to IPL 2022 Final and 2024 Qualifier-2"),
    ("Franchise Verdict", "RE-CONFIRM AS UNCONTESTED CAPTAIN FOR IPL 2027"),
]
for title, body in capt_metrics:
    p = tf13_1.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_PINK if "Verdict" in title else C_BODY
    p.font.bold = ("Verdict" in title or "Win Rate" in title)
    p.space_before = Pt(4)

# Right Card: Leadership Succession
tb13_2 = s13.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf13_2 = tb13_2.text_frame
tf13_2.word_wrap = True
p = tf13_2.paragraphs[0]
p.text = "STRUCTURED SUCCESSION ROADMAP (2027-2030)"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub2 = tf13_2.add_paragraph()
p_sub2.text = "Ensuring Strategic Continuity Beyond the Mini-Auction Cycle"
p_sub2.font.size = Pt(9)
p_sub2.font.color.rgb = C_MUTED
p_sub2.space_before = Pt(2)

succ_points = [
    ("Vice-Captain Appointment", "Appoint Riyan Parag as official Vice-Captain. Proven domestic captaincy experience leading Assam; strong tactical maturity."),
    ("Senior Advisory Council", "Establish leadership support group comprising Mitchell Santner (New Zealand captaincy pedigree) and Jos Buttler (if acquired)."),
    ("Mentorship Transition", "Sanju Samson to actively mentor Riyan Parag and Yashasvi Jaiswal in live DRS protocols and bowling rotation strategies."),
    ("Long-Term Horizon", "Structured transition targeted for 2029-2030 cycle, ensuring seamless captaincy succession without leadership vacuum."),
]
for title, body in succ_points:
    p = tf13_2.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(4)

add_takeaway_strip(s13, "CAPTAINCY VERDICT", "Sanju Samson's 52.8% win rate across 53 matches establishes him as an elite IPL leader. Riyan Parag's appointment as Vice-Captain secures long-term succession stability.", C_NAVY)

# ─── SLIDE 14: RAJASTHAN ROYALS EXISTING SQUAD STATE ────────────────────────
s14 = prs.slides.add_slide(blank_layout)
apply_slide_base(s14, "Rajasthan Royals Roster State: Retained Core & Purse Dynamics", "13 / Roster Analysis")

add_card(s14, 0.8, 1.4, 5.7, 4.3)
add_card(s14, 6.8, 1.4, 5.7, 4.3)

# Left Card: Retained Core
tb14_1 = s14.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf14_1 = tb14_1.text_frame
tf14_1.word_wrap = True
p = tf14_1.paragraphs[0]
p.text = "RETAINED SQUAD CORNERSTONES (Rs.79.0 Cr)"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub = tf14_1.add_paragraph()
p_sub.text = "6 Core Players Retained Ahead of the IPL 2027 Mini-Auction"
p_sub.font.size = Pt(9)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

retained_core = [
    ("Sanju Samson (Captain/WK)", "Rs.18.0 Cr", "Elite top-order anchor; franchise heartbeat; 52.8% win rate."),
    ("Yashasvi Jaiswal (Opener)", "Rs.18.0 Cr", "Explosive left-hand opener; strikes at 160+ vs pace in Powerplay."),
    ("Riyan Parag (Middle Anchor)", "Rs.14.0 Cr", "Breakout spin dominator; utility off-spin bowler; Vice-Captain designate."),
    ("Dhruv Jurel (Finisher/WK)", "Rs.14.0 Cr", "Crisp death-overs finisher; elite athletic fielder and gloveman."),
    ("Shimron Hetmyer (Finisher)", "Rs.11.0 Cr", "Overseas power striker; 190+ death SR against pace bowling."),
    ("Sandeep Sharma (Death Seam)", "Rs.4.0 Cr", "Knuckleball specialist; wide yorker master; uncapped retention value."),
]
for name, cost, desc in retained_core:
    p = tf14_1.add_paragraph()
    p.text = f"• {name} [{cost}]: {desc}"
    p.font.size = Pt(9)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(2)

# Right Card: Financial & Slot Balance
tb14_2 = s14.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf14_2 = tb14_2.text_frame
tf14_2.word_wrap = True
p = tf14_2.paragraphs[0]
p.text = "FINANCIAL & ROSTER CONSTRAINTS"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub2 = tf14_2.add_paragraph()
p_sub2.text = "Mini-Auction Purse: Rs.28.5 - Rs.34.0 Cr Available"
p_sub2.font.size = Pt(9)
p_sub2.font.color.rgb = C_MUTED
p_sub2.space_before = Pt(2)

roster_specs = [
    ("Remaining Purse", "Rs.28.5 - 34.0 Cr (depending on finalized player releases and trade compensations)."),
    ("Overseas Slots Available", "6 total overseas slots in squad; maximum 4 permitted in starting Playing XI."),
    ("Total Squad Slots", "Must recruit 7-9 players to achieve optimum 20-22 player squad depth."),
    ("Critical Vacancies", "#4 Spin Hitter, #6 Domestic Detonator, Express Seamer, Finger Spin Controller, Death Yorker Specialist."),
    ("Strategic Objective", "Achieve 95%+ role coverage without exhausting reserve funds on single-player bidding wars."),
]
for title, desc in roster_specs:
    p = tf14_2.add_paragraph()
    p.text = f"• {title}: {desc}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(4)

add_takeaway_strip(s14, "ROSTER STATE", "With 6 retained cornerstones (Rs.79 Cr committed), Rajasthan Royals possesses the league's most potent batting top order. The mini-auction purse (Rs.28.5-34.0 Cr) must be dedicated to bowling depth and death hitting.", C_PINK)

# ─── SLIDE 15: AUCTION PRIORITIES & ROLE GAPS ────────────────────────────────
s15 = prs.slides.add_slide(blank_layout)
apply_slide_base(s15, "Auction Priorities: Role Gap Matrix & Target Allocations", "14 / Auction Priorities")

priorities = [
    ("Priority 1: Death Yorker Specialist", "Overseas Slot • Budget: Rs.2.5 - 4.5 Cr", [
        ("Deficit Identified", "Rajasthan Royals leaked 11.2 RPO in overs 18-20 when Sandeep Sharma was unavailable."),
        ("Primary Target", "Hasan Mahmud (Bangladesh) • BRS: 80.9 • 5.97 Pressure Econ • 49.6% Dot Ball %."),
        ("Backup Target", "Benjamin Sears (New Zealand) • 145+ km/h pace • Steep bounce • BRS: 79.7."),
    ], C_PINK),
    ("Priority 2: Domestic Clutch Finisher", "Indian Core • Budget: Rs.4.0 - 6.5 Cr", [
        ("Deficit Identified", "Over-reliance on Shimron Hetmyer creates vulnerability when overseas slot is needed for bowling."),
        ("Primary Target", "Naman Dhir (India Uncapped) • BRS: 76.5 • 201.8 High-Leverage SR • Off-break utility."),
        ("Secondary Target", "Shashank Singh (India Core) • BRS: 74.4 • 56.8 High-Leverage Avg • Ice-cold chaser."),
    ], C_NAVY),
    ("Priority 3: Finger Spin Controller", "Overseas Slot • Budget: Rs.3.0 - 4.5 Cr", [
        ("Deficit Identified", "SMS Jaipur's large square boundaries (70m+) require stump-to-stump spin squeeze to choke run rates."),
        ("Primary Target", "Mitchell Santner (New Zealand) • BRS: 73.9 • 6.83 Econ • Batting depth at #8-9."),
        ("Backup Target", "Mohammad Rishad (Bangladesh) • BRS: 75.0 • Leg-break variation • Tall release point."),
    ], C_GOLD),
]
for idx, (title, sub, bullets, col) in enumerate(priorities):
    add_card(s15, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s15.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.bold = True
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s15, "AUCTION GAP DIRECTIVE", "Mandatory acquisition of 1 death bowler (Mahmud/Sears), 1 spin controller (Santner), and 1 domestic finisher (Dhir/Shashank) fulfills 100% of identified franchise role deficits.", C_PINK)

# ─── SLIDE 16: RECOMMENDED SQUAD (SCENARIO B PLAYING XI) ─────────────────────
s16 = prs.slides.add_slide(blank_layout)
apply_slide_base(s16, "Recommended Playing XI: Scenario B (Balanced Rebuild Blueprint)", "15 / Recommended Playing XI")

add_card(s16, 0.8, 1.4, 7.8, 4.3)
tb16_1 = s16.shapes.add_textbox(Inches(0.95), Inches(1.5), Inches(7.5), Inches(4.1))
tf16_1 = tb16_1.text_frame
tf16_1.word_wrap = True

p = tf16_1.paragraphs[0]
p.text = "SCENARIO B: RECOMMENDED STARTING PLAYING XI"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

xi_players = [
    ("1", "Yashasvi Jaiswal", "Opener (LHB)", "Retained (Rs.18.0 Cr)", "IND", "Powerplay aggressor; 160+ SR vs Pace"),
    ("2", "Sanju Samson (C/WK)", "Top Order (RHB)", "Retained (Rs.18.0 Cr)", "IND", "Innings anchor; pace/spin manipulator"),
    ("3", "Riyan Parag (VC)", "Middle Anchor (RHB)", "Retained (Rs.14.0 Cr)", "IND", "Spin dominator; off-break variation"),
    ("4", "Rajat Patidar", "Clutch Striker (RHB)", "Target (Rs.7.5 Cr)", "IND", "Attacks spin at 178 SR in overs 7-15"),
    ("5", "Shashank Singh", "Crisis Finisher (RHB)", "Target (Rs.4.5 Cr)", "IND", "Collapse insurance; 56.8 pressure avg"),
    ("6", "Dhruv Jurel", "Finisher / WK (RHB)", "Retained (Rs.14.0 Cr)", "IND", "360-degree boundary clearing in death"),
    ("7", "Naman Dhir", "Detonator (RHB/OB)", "Target (Rs.5.5 Cr)", "IND", "Instant detonation (201.8 SR); off-spin"),
    ("8", "Shimron Hetmyer", "Death Slogger (LHB)", "Retained (Rs.11.0 Cr)", "OS-1", "190+ death striking; left-hand power"),
    ("9", "Mitchell Santner", "Finger Spinner (LHB/S)", "Target (Rs.4.2 Cr)", "OS-2", "Stump-to-stump accuracy; 6.83 econ"),
    ("10", "Sandeep Sharma", "Knuckle Seamer (RHB/P)", "Retained (Rs.4.0 Cr)", "IND", "Wide-line yorkers; new-ball swing"),
    ("11", "Hasan Mahmud", "Death Yorker (RHB/P)", "Target (Rs.3.5 Cr)", "OS-3", "#1 ranked pressure bowler (5.97 econ)"),
]
for pos, name, role, status, nat, note in xi_players:
    p = tf16_1.add_paragraph()
    p.text = f"{pos}. {name} • {role} [{nat}] — {status}"
    p.font.size = Pt(8.5)
    p.font.color.rgb = C_NAVY if "Retained" in status else C_PINK
    p.font.bold = True
    p.space_before = Pt(1.5)

# Right Card: Tactical Metrics
add_card(s16, 8.8, 1.4, 3.733, 4.3)
tb16_2 = s16.shapes.add_textbox(Inches(8.95), Inches(1.5), Inches(3.4), Inches(4.1))
tf16_2 = tb16_2.text_frame
tf16_2.word_wrap = True

p = tf16_2.paragraphs[0]
p.text = "TACTICAL COMPOSITION METRICS"
p.font.bold = True
p.font.size = Pt(11)
p.font.color.rgb = C_NAVY

xi_metrics = [
    ("Total Auction Spend", "Rs.25.20 Cr (within Rs.28.5-34.0 Cr purse)"),
    ("Remaining Reserve", "Rs.7.80 Cr preserved for squad depth & injuries"),
    ("Overseas Balance", "Exactly 3 Overseas in XI (Hetmyer, Santner, Mahmud)"),
    ("Reserve Buffer", "1 Overseas slot in reserve for tactical Impact Player swap"),
    ("Bowling Resources", "8 bowling options (Sandeep, Mahmud, Santner, Parag, Dhir)"),
    ("Batting Depth", "Batting resources down to #9 (Santner 125+ domestic SR)"),
    ("Role Coverage Score", "96 / 100 — Complete elimination of franchise deficits"),
]
for title, val in xi_metrics:
    p = tf16_2.add_paragraph()
    p.text = f"• {title}:"
    p.font.bold = True
    p.font.size = Pt(9)
    p.font.color.rgb = C_PINK
    p.space_before = Pt(3)

    p_v = tf16_2.add_paragraph()
    p_v.text = f"   {val}"
    p_v.font.size = Pt(8.5)
    p_v.font.color.rgb = C_BODY

add_takeaway_strip(s16, "XI BALANCE GUARANTEE", "Scenario B playing XI delivers 8 bowling options, batting depth to #9, 3 left-handers, and exactly 3 overseas players in the starting XI (1 reserve buffer for dynamic tactical flexibility).", C_EMERALD)

# ─── SLIDE 17: IMPACT PLAYER STRATEGY ────────────────────────────────────────
s17 = prs.slides.add_slide(blank_layout)
apply_slide_base(s17, "Impact Player Tactical Matrix: Innings State Optimization", "16 / Impact Player Strategy")

add_card(s17, 0.8, 1.4, 5.7, 4.3)
add_card(s17, 6.8, 1.4, 5.7, 4.3)

# Left Card: Batting 1st -> Bowling 2nd
tb17_1 = s17.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf17_1 = tb17_1.text_frame
tf17_1.word_wrap = True
p = tf17_1.paragraphs[0]
p.text = "SCENARIO 1: BATTING 1ST → DEFENDING TARGET"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub = tf17_1.add_paragraph()
p_sub.text = "Maximize 1st Innings Runs, Then Deploy Frontline Seamer"
p_sub.font.size = Pt(9)
p_sub.font.color.rgb = C_MUTED
p_sub.space_before = Pt(2)

bat_first_steps = [
    ("Starting Lineup", "Field Shimron Hetmyer at #8 to ensure batting firepower down to the final over."),
    ("Innings Break Swap", "Substitute Shimron Hetmyer OUT; bring Umran Malik (150+ km/h Express Pace) IN."),
    ("Defensive Alignment", "Samson now has 6 frontline bowling options with Sandeep, Mahmud, Sears/Umran, and Santner."),
    ("Jaipur Dew Counter", "Extra express pacer neutralizes dew effect when finger spin loses grip in the 2nd innings."),
]
for title, body in bat_first_steps:
    p = tf17_1.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(4)

# Right Card: Bowling 1st -> Chasing 2nd
tb17_2 = s17.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf17_2 = tb17_2.text_frame
tf17_2.word_wrap = True
p = tf17_2.paragraphs[0]
p.text = "SCENARIO 2: BOWLING 1ST → CHASING TARGET"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

p_sub2 = tf17_2.add_paragraph()
p_sub2.text = "Restrict Opposition, Then Deploy Dynamic Finisher"
p_sub2.font.size = Pt(9)
p_sub2.font.color.rgb = C_MUTED
p_sub2.space_before = Pt(2)

bowl_first_steps = [
    ("Starting Lineup", "Field full bowling attack: Sandeep, Mahmud, Santner, and Umran Malik."),
    ("Chase Swap Trigger", "If chasing 180+ and wickets fall, substitute Umran Malik OUT; bring Prabhsimran Singh or Hetmyer IN."),
    ("Collapse Insurance", "Protects against early Powerplay collapse (e.g. 25/3) without weakening the initial bowling attack."),
    ("Target Velocity", "Maintains required run rate flexibility across overs 11-20 regardless of target scale."),
]
for title, body in bowl_first_steps:
    p = tf17_2.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(4)

add_takeaway_strip(s17, "TACTICAL FLEXIBILITY", "The Impact Player rule allows Rajasthan Royals to seamlessly swap an extra frontline pacer (Umran Malik) for a specialist death slogger (Shimron Hetmyer) depending on innings state.", C_PINK)

# ─── SLIDE 18: ALTERNATIVE SQUAD BLUEPRINTS ──────────────────────────────────
s18 = prs.slides.add_slide(blank_layout)
apply_slide_base(s18, "Alternative Squad Blueprints: Scenarios A, B, and C Compared", "17 / Scenario Modeling")

scen_cards = [
    ("Scenario A: Core Continuity", "Conservative Budget Cushion", [
        ("Auction Outlay", "Rs.18.50 Cr (Preserves Rs.14.50 Cr reserve)."),
        ("Key Additions", "Naman Dhir, Shashank Singh, Mitchell Santner, Jamie Overton, Benjamin Sears."),
        ("Strengths", "Massive financial cushion; zero bidding war vulnerability; retains franchise stability."),
        ("Tradeoff", "Lacks an established #4 Indian striker like Rajat Patidar; relies heavily on young core."),
    ], C_NAVY),
    ("Scenario B: Balanced Rebuild", "OPTIMAL RECOMMENDATION", [
        ("Auction Outlay", "Rs.25.20 Cr (Preserves Rs.7.80 Cr reserve)."),
        ("Key Additions", "Rajat Patidar, Shashank Singh, Naman Dhir, Mitchell Santner, Hasan Mahmud, Umran Malik."),
        ("Strengths", "96/100 role coverage; elite death bowling pair; solves #4 spin hitting and #6 collapse risk."),
        ("Tradeoff", "Requires disciplined bidding execution; walk away if Patidar exceeds Rs.8.5 Cr."),
    ], C_PINK),
    ("Scenario C: Opportunity Firepower", "Aggressive Marquee Pursuit", [
        ("Auction Outlay", "Rs.32.00 Cr (Narrow Rs.1.00 Cr reserve)."),
        ("Key Additions", "Jos Buttler (re-acquisition), Naman Dhir, Mitchell Santner, Hasan Mahmud, Umran Malik."),
        ("Strengths", "Generates the tournament's most terrifying top order; immense commercial appeal."),
        ("Tradeoff", "Drains 97% of purse on top XI; leaves bench vulnerable to injury crises during the season."),
    ], C_GOLD),
]
for idx, (title, sub, bullets, col) in enumerate(scen_cards):
    add_card(s18, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s18.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.bold = True
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s18, "SCENARIO COMPARISON", "Scenario B represents the optimal equilibrium between bid aggression and budget prudence, preserving Rs.7.80 Cr in reserve compared to Scenario C's dangerously narrow Rs.1.0 Cr cushion.", C_PINK)

# ─── SLIDE 19: MINI-AUCTION BUDGET FEASIBILITY ───────────────────────────────
s19 = prs.slides.add_slide(blank_layout)
apply_slide_base(s19, "Mini-Auction Budget Feasibility & Bid Ceiling Governance", "18 / Financial Governance")

add_card(s19, 0.8, 1.4, 5.7, 4.3)
add_card(s19, 6.8, 1.4, 5.7, 4.3)

# Left Card: Target Valuation & Ceilings
tb19_1 = s19.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf19_1 = tb19_1.text_frame
tf19_1.word_wrap = True
p = tf19_1.paragraphs[0]
p.text = "TARGET VALUATIONS & WALK-AWAY CEILINGS"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

ceilings = [
    ("Rajat Patidar (#4 Bat)", "Target: Rs.7.5 Cr", "Walk-Away Ceiling: Rs.8.5 Cr (Pivot: Nehal Wadhera)"),
    ("Naman Dhir (#6-7 Bat)", "Target: Rs.5.5 Cr", "Walk-Away Ceiling: Rs.7.0 Cr (Pivot: Jamie Overton)"),
    ("Shashank Singh (#5-6 Bat)", "Target: Rs.4.5 Cr", "Walk-Away Ceiling: Rs.6.0 Cr (Pivot: Ashutosh Sharma)"),
    ("Mitchell Santner (Spin)", "Target: Rs.4.2 Cr", "Walk-Away Ceiling: Rs.5.0 Cr (Pivot: Shahbaz Ahmed)"),
    ("Hasan Mahmud (Death Seam)", "Target: Rs.3.5 Cr", "Walk-Away Ceiling: Rs.4.5 Cr (Pivot: Benjamin Sears)"),
    ("Umran Malik (Express Pace)", "Target: Rs.3.0 Cr", "Walk-Away Ceiling: Rs.4.0 Cr (Pivot: Rasikh Salam)"),
]
for target, price, ceiling in ceilings:
    p = tf19_1.add_paragraph()
    p.text = f"• {target} — {price}"
    p.font.bold = True
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_PINK
    p.space_before = Pt(3)

    p_c = tf19_1.add_paragraph()
    p_c.text = f"   {ceiling}"
    p_c.font.size = Pt(8.5)
    p_c.font.color.rgb = C_BODY

# Right Card: Financial Risk Mitigation
tb19_2 = s19.shapes.add_textbox(Inches(7.0), Inches(1.55), Inches(5.3), Inches(4.0))
tf19_2 = tb19_2.text_frame
tf19_2.word_wrap = True
p = tf19_2.paragraphs[0]
p.text = "AUCTION BIDDING PROTOCOLS & GOVERNANCE"
p.font.bold = True
p.font.size = Pt(12)
p.font.color.rgb = C_NAVY

gov_rules = [
    ("Strict Walk-Away Enforcement", "Under no circumstances may the bidding table breach pre-modeled ceiling prices. Mathematical value dissolves when bids exceed 120% of fair valuation."),
    ("Dynamic Escalation Tracking", "Telemetry engine recalculates remaining purse feasibility in real-time after every completed auction lot."),
    ("Bid Pacing Tactics", "Allow rival franchises to battle over early marquee lots; deploy capital aggressively during mid-tier acceleration lots where valuation asymmetry peaks."),
    ("Emergency Reserve Mandate", "A minimum reserve cushion of Rs.5.0 Cr must remain intact throughout the mini-auction to absorb late-round uncapped talent opportunities."),
]
for title, body in gov_rules:
    p = tf19_2.add_paragraph()
    p.text = f"• {title}: {body}"
    p.font.size = Pt(9.5)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(4)

add_takeaway_strip(s19, "BID CEILING DISCIPLINE", "Strict walk-away thresholds (Dhir: Rs.7.0 Cr, Mahmud: Rs.4.5 Cr, Santner: Rs.4.5 Cr) guarantee that Rajasthan Royals never enters uncontrolled bidding wars.", C_GOLD)

# ─── SLIDE 20: STRATEGIC DIFFERENTIATION ────────────────────────────────────
s20 = prs.slides.add_slide(blank_layout)
apply_slide_base(s20, "Strategic Differentiation: Why RR APEX SCOUT Wins the Auction", "19 / Competitive Edge")

diff_cards = [
    ("Mathematical Objectivity", "Zero Human Bias", [
        ("Continuous Telemetry", "Replaces subjective scout hunches with 200,999 delivery telemetry data points."),
        ("Empirical Regularization", "Bayesian shrinkage eliminates the seductive trap of one-season wonder anomalies."),
        ("Audit Verification", "100% regulatory compliance eliminates risk of disqualified or ineligible player acquisitions."),
    ], C_NAVY),
    ("Contextual Precision", "Bespoke Franchise Fit", [
        ("Venue Specificity", "Engine specifically models Sawai Mansingh Stadium surface friction, boundary scale, and dew."),
        ("Tandem Compatibility", "Scouts player combinations across 4,423 match partnerships rather than isolated individuals."),
        ("Purse Realism", "Designs solutions within Rajasthan Royals' actual Rs.28.5-34.0 Cr mini-auction balance."),
    ], C_PINK),
    ("Decisive Actionability", "Ready for Execution", [
        ("Turnkey Blueprints", "Provides franchise executives with 3 complete, fully-budgeted, compliant squad options."),
        ("Contingency Matrices", "Pre-calculated pivot paths for every bidding escalation scenario at the auction table."),
        ("Leadership Stability", "Validates Sanju Samson's leadership while formalizing a clear 4-year succession roadmap."),
    ], C_GOLD),
]
for idx, (title, sub, bullets, col) in enumerate(diff_cards):
    add_card(s20, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s20.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.bold = True
    p_sub.font.size = Pt(8.5)
    p_sub.font.color.rgb = C_MUTED
    p_sub.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s20, "COMPETITIVE MOAT", "By replacing subjective reputation with continuous SLI and Empirical Bayes shrinkage, Rajasthan Royals gains mathematical arbitrage over traditional scouting desks.", C_NAVY)

# ─── SLIDE 21: FINAL RECOMMENDATION & SIGN-OFF ──────────────────────────────
s21 = prs.slides.add_slide(blank_layout)
apply_slide_base(s21, "Official Submission Sign-Off & Regulatory Declaration", "20 / Final Sign-Off")

add_card(s21, 0.8, 1.4, 11.733, 4.3)
tb21 = s21.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.333), Inches(4.0))
tf21 = tb21.text_frame
tf21.word_wrap = True

p = tf21.paragraphs[0]
p.text = "OFFICIAL UNSTOP SupeRR SELECTOR SEASON 2 SUBMISSION SIGN-OFF"
p.font.bold = True
p.font.size = Pt(13)
p.font.color.rgb = C_NAVY

p_sub = tf21.add_paragraph()
p_sub.text = "Rajasthan Royals Strategic Cricket Intelligence & IPL 2027 Mini-Auction Decision System"
p_sub.font.size = Pt(9.5)
p_sub.font.color.rgb = C_PINK
p_sub.space_before = Pt(2)

bullets_signoff = [
    ("Regulatory Verification", "100% compliant with BCCI and IPL governing council directives. All 68 PCB records excluded upstream from public display."),
    ("Data Rigor & Completeness", "1,217 players evaluated across 200,999 deliveries and 883 matches. Zero missing metrics across the 20 featured benchmark players."),
    ("Top 10 Batters Benchmark", "1. Suryakumar Yadav (MI Retained -> Alt: Tilak Varma) | 2. Naman Dhir (Target) | 3. Tim David (Target) | 4. Shashank Singh (Target) | 5. Jos Buttler (GT Retained -> Alt: Jake Fraser-McGurk) | 6. Rajat Patidar (Target) | 7. Phil Salt (KKR Retained -> Alt: Prabhsimran Singh) | 8. Reeza Hendricks (Target) | 9. Virat Kohli (RCB Retained -> Alt: Devdutt Padikkal) | 10. Rishabh Pant (LSG Retained -> Alt: Dhruv Jurel)."),
    ("Top 10 Bowlers Benchmark", "1. Hasan Mahmud (Target) | 2. Benjamin Sears (Target) | 3. Sunil Narine (KKR Retained -> Alt: Varun C) | 4. Mohammad Rishad (Target) | 5. Mitchell Santner (Target) | 6. Umran Malik (Target) | 7. Rashid Khan (GT Retained -> Alt: Ravi Bishnoi) | 8. Matheesha Pathirana (CSK Retained -> Alt: Nuwan Thushara) | 9. Jamie Overton (Target) | 10. Jasprit Bumrah (MI Retained -> Alt: Avesh Khan)."),
    ("Actionable Execution Recommendation", "Execute Scenario B (Balanced Rebuild) by targeting Naman Dhir, Shashank Singh, Rajat Patidar, Mitchell Santner, Hasan Mahmud, and Umran Malik for ~Rs.25.20 Cr, preserving Rs.7.80 Cr in reserve."),
]
for title, desc in bullets_signoff:
    p = tf21.add_paragraph()
    p.text = f"• {title}: {desc}"
    p.font.size = Pt(9)
    p.font.color.rgb = C_BODY
    p.space_before = Pt(3)

add_takeaway_strip(s21, "REGULATORY INTEGRITY", "100% BCCI/IPL compliant. Zero PCB players surfaced. Mini-auction execution scheduled for December 16, 2026 in Goa under unified franchise strategy.", C_EMERALD)

# ─── SLIDE 22: PITCH INTELLIGENCE & VENUE SURFACES ───────────────────────────
s22 = prs.slides.add_slide(blank_layout)
apply_slide_base(s22, "Pitch Intelligence & Venue Surfaces: Sawai Mansingh Stadium Profiling", "21 / Pitch Intelligence")

venues = [
    ("SMS Jaipur (Home Ground)", "Boundary: 70-75m | Spin Squeeze", [
        ("Surface Friction", "True subcontinental bounce initially; slows down substantially under lights. Demands high-accuracy finger spinners."),
        ("Pace vs Spin Splits", "Pace Econ: 8.42 | Spin Econ: 7.24 | Boundary %: 18.2% | Bat-1st Win%: 48.5%."),
        ("RR Tactical Weapon", "Deploy Mitchell Santner (6.83 econ) and Riyan Parag to squeeze middle overs; Sandeep wide-line yorkers in death."),
    ], C_PINK),
    ("Wankhede & Eden Gardens", "Boundary: 62-66m | Red Soil Bounce", [
        ("Surface Friction", "High pace, steep bounce, heavy dew in 2nd innings. Demands 145+ km/h express seamers and pace power-hitters."),
        ("Pace vs Spin Splits", "Pace Econ: 9.15 | Spin Econ: 8.82 | Boundary %: 22.8% | Bat-1st Win%: 43.2%."),
        ("RR Tactical Weapon", "Unleash Umran Malik (150+ km/h) to break middle stands; Yashasvi Jaiswal and Hetmyer feast on pace."),
    ], C_NAVY),
    ("Ekana Lucknow & Chepauk", "Boundary: 68-72m | Black Soil Grip", [
        ("Surface Friction", "Two-paced, low bounce, ball grips and turns sharply. Scoring decelerates; demands crisis anchors and spin duopolies."),
        ("Pace vs Spin Splits", "Pace Econ: 8.21 | Spin Econ: 6.95 | Boundary %: 16.4% | Bat-1st Win%: 54.2%."),
        ("RR Tactical Weapon", "Sanju Samson anchor role; Rajat Patidar attacks spin (178 SR); Santner + Parag tandem strangles boundaries."),
    ], C_GOLD),
]
for idx, (venue, dim, bullets, col) in enumerate(venues):
    add_card(s22, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s22.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = venue
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_d = tf.add_paragraph()
    p_d.text = dim
    p_d.font.bold = True
    p_d.font.size = Pt(8.5)
    p_d.font.color.rgb = C_MUTED
    p_d.space_before = Pt(2)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s22, "VENUE TAKEAWAY", "Rajasthan Royals' home fortress at SMS Jaipur demands finger-spin strangleholds and boundary-denial wide yorkers. Scenario B's acquisition of Mitchell Santner and Hasan Mahmud directly satisfies these venue mechanics.", C_PINK)

# ─── SLIDE 23: BATTING STRATEGY ACROSS PITCH TYPES ──────────────────────────
s23 = prs.slides.add_slide(blank_layout)
apply_slide_base(s23, "Batting Strategy Engine: Adapting Profiles to Surface Conditions", "22 / Batting Strategy")

pitches_bat = [
    ("Fast & Bouncy (Aus / SA)", "Back-Foot Punchers & Pullers", "Shashank Singh, Naman Dhir", [
        ("Shot Geometry", "High back-lift and back-foot contact point. Exploit true carry with cuts and pull shots into deep square."),
        ("Phase Gameplan", "Attack pace in Powerplay (overs 1-6); target 9.5+ RPO. Use bouncers to score over third man and fine leg."),
        ("Personnel Fit", "Shashank Singh (185 SR vs Pace) and Naman Dhir thrive against 140+ km/h express bowling."),
    ], C_NAVY),
    ("Slow & Turning (Subcontinent)", "Front-Foot Drivers & Sweepers", "Sanju Samson, Rajat Patidar", [
        ("Shot Geometry", "Low center of gravity; clean sweep and slog-sweep execution to disrupt spin lengths on turning tracks."),
        ("Phase Gameplan", "Consolidate during middle overs (7-15); rotate strike at 1 run/ball minimum to eliminate dot-ball build-up."),
        ("Personnel Fit", "Sanju Samson manipulates gaps; Rajat Patidar destroys spin at 178 SR with inside-out lofts over extra cover."),
    ], C_PINK),
    ("True Batter Paradise (Flat)", "360-Degree Detonators", "Yashasvi Jaiswal, Shimron Hetmyer", [
        ("Shot Geometry", "Explosive bat velocity from ball 1. Target boundary rates >25% regardless of phase or field settings."),
        ("Phase Gameplan", "Unconstrained detonation: 65+ in Powerplay; maintain 10.0+ RPO; death assault yielding 60+ in overs 16-20."),
        ("Personnel Fit", "Yashasvi Jaiswal attacks with new ball; Shimron Hetmyer and Dhruv Jurel punish death bowling at 190+ SR."),
    ], C_GOLD),
]
for idx, (ptype, prof, targets, bullets, col) in enumerate(pitches_bat):
    add_card(s23, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s23.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ptype
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_pr = tf.add_paragraph()
    p_pr.text = prof
    p_pr.font.bold = True
    p_pr.font.size = Pt(8.5)
    p_pr.font.color.rgb = C_MUTED
    p_pr.space_before = Pt(2)

    p_tg = tf.add_paragraph()
    p_tg.text = f"Key Assets: {targets}"
    p_tg.font.bold = True
    p_tg.font.size = Pt(9.5)
    p_tg.font.color.rgb = C_EMERALD
    p_tg.space_before = Pt(3)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s23, "BATTING STRATEGY MANDATE", "Align batting order flexibility with pitch deceleration rates. Against spin squeeze decks, elevate Rajat Patidar to #4; on true bouncy tracks, give Shashank Singh license to pull from ball 1.", C_PINK)

# ─── SLIDE 24: BOWLING STRATEGY ACROSS PITCH TYPES ──────────────────────────
s24 = prs.slides.add_slide(blank_layout)
apply_slide_base(s24, "Bowling Strategy Engine: Weapon Deployment by Surface Mechanics", "23 / Bowling Strategy")

pitches_bowl = [
    ("Seam & Swing Friendly", "Full-Length Swinger + Seam Movement", "Sandeep Sharma, Hasan Mahmud", [
        ("Length Geometry", "Target 6-8 meter good length in Powerplay. Induce outside edges and early top-order collapse."),
        ("Phase Allocations", "Sandeep Sharma bowls 3 Powerplay overs; Mahmud bowls 1 Powerplay over and holds 3 for death."),
        ("Target Economy", "Powerplay Econ < 6.80 | Minimum 2 wickets inside first 6 overs to expose opposition middle order."),
    ], C_NAVY),
    ("Dry & Turning Surfaces", "High-Rev Wrist Spin & Finger Darts", "Mitchell Santner, Riyan Parag", [
        ("Length Geometry", "Attack stumps on 4-6 meter length. Dry up boundaries and force impatient lofted mishits into deep ropes."),
        ("Phase Allocations", "Santner bowls overs 7, 9, 11, 14; Parag bowls overs 8, 10, 12. Combined 7 overs of spin strangulation."),
        ("Target Economy", "Middle-Overs Econ < 7.10 | Dot ball frequency exceeding 45% on abrasive Jaipur pitches."),
    ], C_PINK),
    ("Flat Highway Decks", "Laser Blockhole Yorkers + Bouncers", "Hasan Mahmud, Umran Malik", [
        ("Length Geometry", "Extreme execution variance. 140-150 km/h yorkers into toes and hostile bouncers to deny leverage."),
        ("Phase Allocations", "Umran Malik deployed in overs 9-13 to break stands; Hasan Mahmud and Sandeep Sharma execute death overs 18-20."),
        ("Target Economy", "Death Overs Econ held under 9.50 | Zero wides or free-hit full tosses during acute leverage moments."),
    ], C_GOLD),
]
for idx, (ptype, prof, targets, bullets, col) in enumerate(pitches_bowl):
    add_card(s24, 0.8 + idx * 3.95, 1.4, 3.8, 4.3)
    tb = s24.shapes.add_textbox(Inches(0.95 + idx * 3.95), Inches(1.5), Inches(3.5), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = ptype
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = col
    
    p_pr = tf.add_paragraph()
    p_pr.text = prof
    p_pr.font.bold = True
    p_pr.font.size = Pt(8.5)
    p_pr.font.color.rgb = C_MUTED
    p_pr.space_before = Pt(2)

    p_tg = tf.add_paragraph()
    p_tg.text = f"Key Weapons: {targets}"
    p_tg.font.bold = True
    p_tg.font.size = Pt(9.5)
    p_tg.font.color.rgb = C_EMERALD
    p_tg.space_before = Pt(3)

    for b_title, b_desc in bullets:
        p_b = tf.add_paragraph()
        p_b.text = f"• {b_title}: {b_desc}"
        p_b.font.size = Pt(9.5)
        p_b.font.color.rgb = C_BODY
        p_b.space_before = Pt(4)

add_takeaway_strip(s24, "BOWLING STRATEGY MANDATE", "Dual-death execution via Sandeep Sharma (knuckleball/wide yorker) and Hasan Mahmud (blockhole laser) guarantees sub-8.50 economy across all surface typologies.", C_GOLD)

# ─── SAVE PRESENTATION ───────────────────────────────────────────────────────
import shutil, tempfile
out_path = "public/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Presentation.pptx"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
# Save to temp file first to avoid OneDrive lock on the target path
with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False, dir=os.path.dirname(out_path)) as tmp:
    tmp_path = tmp.name
prs.save(tmp_path)
# Replace target atomically
if os.path.exists(out_path):
    os.remove(out_path)
shutil.move(tmp_path, out_path)
print(f"Master Presentation Generated Successfully: {out_path} (24 slides)")
