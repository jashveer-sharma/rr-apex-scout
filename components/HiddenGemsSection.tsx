'use client';

import React from 'react';
import { Sparkles, TrendingUp, ShieldCheck, DollarSign, ArrowUpRight, CheckCircle2, AlertCircle } from 'lucide-react';

interface GemItem {
  name: string;
  role: string;
  rank: string;
  country: string;
  eligibility: 'INDIAN_CORE' | 'OVERSEAS_ELIGIBLE';
  eligibilityNote: string;
  headlineVsReality: string;
  metric1: string;
  metric1Label: string;
  metric2: string;
  metric2Label: string;
  metric3: string;
  metric3Label: string;
  rrAdvantage: string;
  auctionValueTier: string;
}

export default function HiddenGemsSection() {
  const gems: GemItem[] = [
    {
      name: 'Naman Dhir',
      role: 'Batter / Finisher (RHB / Off-Break)',
      rank: 'Rank #2 Eligible Batter (BRS 76.5)',
      country: 'India',
      eligibility: 'INDIAN_CORE',
      eligibilityNote: 'Uncapped / Indian Core Priority',
      headlineVsReality: 'Perception: Emerging domestic prospect. Reality: 201.8 High-Leverage Strike Rate & 30.5% Boundary Frequency.',
      metric1: '201.8',
      metric1Label: 'Pressure SR',
      metric2: '41.8',
      metric2Label: 'Pressure Avg',
      metric3: '+32.0',
      metric3Label: 'ΔSR vs Base',
      rrAdvantage: 'High purse efficiency target for RR #6 or #7. Fearless boundary striking without inflated marquee auction pricing.',
      auctionValueTier: 'Est. ₹4.0 - ₹6.5 Cr • High ROI'
    },
    {
      name: 'Shashank Singh',
      role: 'Crisis Finisher (RHB)',
      rank: 'Rank #4 Eligible Batter (BRS 74.4)',
      country: 'India',
      eligibility: 'INDIAN_CORE',
      eligibilityNote: 'Indian Core Priority Target',
      headlineVsReality: 'Perception: Late-career domestic campaigner. Reality: 56.8 High-Leverage Average & Ice-Cold Chase Composure.',
      metric1: '182.5',
      metric1Label: 'Pressure SR',
      metric2: '56.8',
      metric2Label: 'Pressure Avg',
      metric3: '+20.9',
      metric3Label: 'ΔSR vs Base',
      rrAdvantage: 'Eliminates RR’s historical vulnerability to collapses from 40/4. Proven match-winning temperament under high situational leverage.',
      auctionValueTier: 'Est. ₹3.5 - ₹5.5 Cr • High Certainty'
    },
    {
      name: 'Benjamin Sears',
      role: 'Right-Arm Express Seamer (145+ km/h)',
      rank: 'Rank #9 Eligible Bowler (BRS 74.0)',
      country: 'New Zealand',
      eligibility: 'OVERSEAS_ELIGIBLE',
      eligibilityNote: 'NZC NOC Fully Cleared',
      headlineVsReality: 'Perception: Unheralded overseas pacer. Reality: 145+ km/h release velocity, steep bounce, and 45.2% dot balls.',
      metric1: '7.85',
      metric1Label: 'Pressure Econ',
      metric2: '45.2%',
      metric2Label: 'Dot Ball %',
      metric3: '146.5 km/h',
      metric3Label: 'Mean Speed',
      rrAdvantage: 'Hostile bounce weapon perfectly calibrated for SMS Jaipur’s expansive square boundaries.',
      auctionValueTier: 'Est. ₹1.5 - ₹3.0 Cr • High Value'
    },
    {
      name: 'Jamie Overton',
      role: 'Fast-Bowling All-Rounder',
      rank: 'Rank #7 Eligible Bowler (BRS 66.2)',
      country: 'England',
      eligibility: 'OVERSEAS_ELIGIBLE',
      eligibilityNote: 'ECB Registration Verified',
      headlineVsReality: 'Perception: English county all-rounder. Reality: 6.62 Pressure Economy and 170+ death-overs striking capability.',
      metric1: '6.62',
      metric1Label: 'Pressure Econ',
      metric2: '41.2%',
      metric2Label: 'Dot Ball %',
      metric3: '174.2',
      metric3Label: 'Batting Strike Rate',
      rrAdvantage: 'Provides multi-dimensional insurance at #8. Can bowl hostile heavy-ball overs in middle phases and finish with the bat.',
      auctionValueTier: 'Est. ₹3.0 - ₹5.0 Cr • Dual Asset'
    },
    {
      name: 'Hasan Mahmud',
      role: 'Death-Overs Seamer & Yorker Specialist',
      rank: 'Rank #1 Eligible Bowler (BRS 79.7)',
      country: 'Bangladesh',
      eligibility: 'OVERSEAS_ELIGIBLE',
      eligibilityNote: 'Subject to BCB Full Tour NOC',
      headlineVsReality: 'Perception: Subcontinental pacer under public radar. Reality: #1 Ranked Pressure Bowler across 200,999 delivery dataset.',
      metric1: '6.85',
      metric1Label: 'Pressure Econ',
      metric2: '46.1%',
      metric2Label: 'Dot Ball %',
      metric3: '22',
      metric3Label: 'Clutch Wickets',
      rrAdvantage: 'Elite death overs bowling complement to Sandeep Sharma. Executes block-hole yorkers under extreme situational leverage.',
      auctionValueTier: 'Est. ₹2.5 - ₹4.0 Cr • Elite Weapon'
    },
    {
      name: 'Mitchell Santner',
      role: 'Slow Left-Arm Orthodox Containment',
      rank: 'Rank #4 Eligible Bowler (BRS 71.8)',
      country: 'New Zealand',
      eligibility: 'OVERSEAS_ELIGIBLE',
      eligibilityNote: 'NZC NOC Fully Cleared',
      headlineVsReality: 'Perception: Modest finger spinner. Reality: 6.83 Situational Economy and unmatched stump-to-stump discipline.',
      metric1: '6.83',
      metric1Label: 'Pressure Econ',
      metric2: '41.5%',
      metric2Label: 'Dot Ball %',
      metric3: '0.82',
      metric3Label: 'Boundary/Over',
      rrAdvantage: 'Chokehold specialist designed to suffocate opposition scoring through SMS Jaipur middle overs (overs 7-15).',
      auctionValueTier: 'Est. ₹3.0 - ₹4.5 Cr • High Efficiency'
    }
  ];

  return (
    <section id="gems" className="py-16 sm:py-24 border-t border-rr-border bg-white text-slate-800">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-12">
        
        {/* Section Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-[10px] sm:text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 12 / UNDERRATED MARKET ASSETS
          </span>
        </div>

        {/* Section Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-12 gap-4 sm:gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              HIGH-LEVERAGE ASYMMETRY: <br />
              <span className="text-rr-pink">VALUATION EFFICIENCY GEMS</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Players whose market perception lags their true delivery-level pressure performance. 
            These targets offer asymmetric ROI without requiring ₹15+ Cr bidding wars.
          </p>
        </div>

        {/* Gems Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {gems.map((gem) => (
            <div
              key={gem.name}
              className="p-6 rounded-[2px] bg-rr-offwhite border border-rr-border hover:border-rr-pink transition-all flex flex-col justify-between space-y-4"
            >
              <div>
                {/* Header Badge & Country */}
                <div className="flex items-center justify-between pb-3 border-b border-rr-border">
                  <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-white text-rr-navy border border-rr-border uppercase">
                    {gem.eligibilityNote}
                  </span>
                  <span className="text-xs font-mono text-slate-500">{gem.country}</span>
                </div>

                {/* Player Identity */}
                <div className="mt-3">
                  <h3 className="text-xl font-extrabold text-rr-navy font-display">{gem.name}</h3>
                  <div className="text-xs text-slate-600 font-mono mt-0.5">{gem.role}</div>
                  <div className="text-[11px] font-mono font-bold text-rr-pink mt-1">{gem.rank}</div>
                </div>

                {/* Perception vs Reality */}
                <div className="p-3 rounded-[2px] bg-white border border-rr-border mt-3 text-xs leading-relaxed text-slate-600">
                  {gem.headlineVsReality}
                </div>

                {/* Key Metrics */}
                <div className="grid grid-cols-3 gap-2 mt-3 text-center font-mono">
                  <div className="p-2 rounded-[2px] bg-white border border-rr-border">
                    <div className="text-[9px] text-slate-500 uppercase">{gem.metric1Label}</div>
                    <div className="text-sm font-black text-rr-navy mt-0.5">{gem.metric1}</div>
                  </div>
                  <div className="p-2 rounded-[2px] bg-white border border-rr-border">
                    <div className="text-[9px] text-slate-500 uppercase">{gem.metric2Label}</div>
                    <div className="text-sm font-black text-rr-navy mt-0.5">{gem.metric2}</div>
                  </div>
                  <div className="p-2 rounded-[2px] bg-white border border-rr-border">
                    <div className="text-[9px] text-slate-500 uppercase">{gem.metric3Label}</div>
                    <div className="text-sm font-black text-emerald-700 mt-0.5">{gem.metric3}</div>
                  </div>
                </div>

                {/* RR Advantage */}
                <div className="mt-3 text-xs text-slate-600 leading-relaxed">
                  <span className="font-bold text-rr-navy font-mono uppercase text-[10px] block mb-0.5">
                    Rajasthan Royals Tactical Fit:
                  </span>
                  {gem.rrAdvantage}
                </div>
              </div>

              {/* Valuation Tier */}
              <div className="p-2.5 rounded-[2px] bg-white border border-rr-border text-xs font-mono text-center">
                <span className="text-slate-500 font-semibold">{gem.auctionValueTier}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}