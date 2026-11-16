'use client';

import React, { useState } from 'react';
import { Target, Coins, ShieldCheck, CheckCircle2, TrendingUp, AlertCircle, Sparkles, Filter, Check } from 'lucide-react';

interface AuctionTarget {
  name: string;
  role: string;
  nationality: string;
  contractStatus: string;
  brsScore: number;
  aosScore: number;
  estPrice: string;
  feasibility: 'Very High' | 'High' | 'Moderate' | 'Aggressive Target';
  squadGap: string;
  jaipurFit: string;
}

export default function AuctionShortlistSection() {
  const [roleFilter, setRoleFilter] = useState<'all' | 'batters' | 'bowlers'>('all');

  const targets: AuctionTarget[] = [
    {
      name: 'Naman Dhir',
      role: 'Lower-Order Detonator / Off-Break',
      nationality: 'India (Domestic Core)',
      contractStatus: 'Mini-Auction Pool (Uncapped / Emerging)',
      brsScore: 76.5,
      aosScore: 92.4,
      estPrice: '₹4.00 - ₹6.50 Cr',
      feasibility: 'Very High',
      squadGap: 'Fixes RR death-overs batting deceleration (overs 16-20); allows Jaiswal & Samson to attack without collapse fear.',
      jaipurFit: 'Straight boundary power matches SMS Jaipur long square dimensions; bowls utility off-spin.'
    },
    {
      name: 'Shashank Singh',
      role: 'Crisis Finisher (RHB)',
      nationality: 'India (Domestic Core)',
      contractStatus: 'Mini-Auction Pool (Available Candidate)',
      brsScore: 74.4,
      aosScore: 90.8,
      estPrice: '₹3.50 - ₹5.50 Cr',
      feasibility: 'Very High',
      squadGap: 'Eliminates collapses when top order misfires; 56.8 high-leverage average guarantees stability.',
      jaipurFit: 'Authentic back-foot boundary punch suits the true subcontinental bounce in Jaipur.'
    },
    {
      name: 'Umran Malik',
      role: 'Express Pace Enforcer (150+ km/h)',
      nationality: 'India (Domestic Core)',
      contractStatus: 'Mini-Auction Pool (Available Candidate)',
      brsScore: 73.6,
      aosScore: 89.2,
      estPrice: '₹3.50 - ₹5.00 Cr',
      feasibility: 'Very High',
      squadGap: 'Middle-overs strike hostility (overs 7-15) to break threatening partnerships; ideal Impact Player.',
      jaipurFit: 'Hostile short balls force mistimed pulls into 70m+ Jaipur outfield for outfield catches.'
    },
    {
      name: 'Mitchell Santner',
      role: 'Slow Left-Arm Orthodox Containment',
      nationality: 'New Zealand (Overseas Slot)',
      contractStatus: 'Mini-Auction Pool (NZC NOC Available)',
      brsScore: 71.8,
      aosScore: 88.5,
      estPrice: '₹3.00 - ₹4.50 Cr',
      feasibility: 'Very High',
      squadGap: 'Pinch-tight spin control (6.83 pressure econ) across middle overs; provides left-arm variety.',
      jaipurFit: 'Stump-to-stump accuracy suffocates visiting batters on Jaipur’s expansive outfield.'
    },
    {
      name: 'Tim David',
      role: 'Death-Overs Power Striker',
      nationality: 'Australia (Overseas Slot)',
      contractStatus: 'Mini-Auction Pool (CA NOC Available)',
      brsScore: 75.2,
      aosScore: 86.8,
      estPrice: '₹6.50 - ₹8.50 Cr',
      feasibility: 'High',
      squadGap: 'Direct overseas finisher paired with Shimron Hetmyer to guarantee 60+ runs in overs 16-20.',
      jaipurFit: 'Elite bat speed clears the longest 75m boundary ropes with effortless leverage.'
    },
    {
      name: 'Hasan Mahmud',
      role: 'Death-Overs Seamer & Yorker Specialist',
      nationality: 'Bangladesh (Overseas Slot)',
      contractStatus: 'Mini-Auction Pool (Subject to BCB NOC)',
      brsScore: 79.7,
      aosScore: 86.2,
      estPrice: '₹2.50 - ₹4.00 Cr',
      feasibility: 'Very High',
      squadGap: 'Frontline death bowling partner for Sandeep Sharma; delivers yorkers under maximum leverage.',
      jaipurFit: 'High dot-ball rate (42.6%) defends sub-175 totals when pitch slows down at night.'
    },
    {
      name: 'Jos Buttler',
      role: 'Championship Explosive Opener (RHB)',
      nationality: 'England (Overseas Slot)',
      contractStatus: 'Mini-Auction Pool (ECB NOC Available)',
      brsScore: 73.4,
      aosScore: 85.0,
      estPrice: '₹9.00 - ₹12.50 Cr',
      feasibility: 'Moderate',
      squadGap: 'Elite pedigree opener alongside Yashasvi Jaiswal; proven championship match-winner.',
      jaipurFit: 'Decade of local experience at SMS Jaipur; exploits powerplay fielding restrictions perfectly.'
    },
    {
      name: 'Benjamin Sears',
      role: 'Express Right-Arm Seamer (145+ km/h)',
      nationality: 'New Zealand (Overseas Slot)',
      contractStatus: 'Mini-Auction Pool (NZC NOC Available)',
      brsScore: 74.0,
      aosScore: 84.6,
      estPrice: '₹1.50 - ₹2.50 Cr',
      feasibility: 'Very High',
      squadGap: 'Ultra-cost-efficient raw pace backup; capable of bowling hostile hard-length spells.',
      jaipurFit: 'Steep release trajectory generates uncomfortable bounce on Jaipur’s dry surfaces.'
    }
  ];

  const filteredTargets = targets.filter(t => {
    if (roleFilter === 'batters') return t.role.toLowerCase().includes('finisher') || t.role.toLowerCase().includes('opener') || t.role.toLowerCase().includes('striker') || t.role.toLowerCase().includes('detonator');
    if (roleFilter === 'bowlers') return t.role.toLowerCase().includes('seamer') || t.role.toLowerCase().includes('spin') || t.role.toLowerCase().includes('pace');
    return true;
  });

  return (
    <section id="auction-shortlist" className="py-24 border-t border-rr-border bg-white text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 10 / AUCTION TARGET SHORTLIST & FEASIBILITY
          </span>
        </div>

        {/* Section Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              REALISTIC AUCTION TARGETS: <br />
              <span className="text-rr-pink">AUCTION OPPORTUNITY SCORE (AOS)</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Distinguishing pure statistical rankings from actionable acquisition targets. 
            Confirmed retained stars remain in statistical benchmarks, while this shortlist 
            evaluates players genuinely available in the IPL 2027 Mini-Auction.
          </p>
        </div>

        {/* RR Squad Context & Mini-Auction Purse Strip */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 p-6 rounded-[2px] bg-rr-offwhite border border-rr-border mb-10 text-xs font-mono">
          <div className="p-3 bg-white border border-rr-border rounded-[2px]">
            <div className="text-slate-500 uppercase text-[10px]">Retained Core (6 Players)</div>
            <div className="text-sm font-bold text-rr-navy mt-1">Samson, Jaiswal, Parag, Jurel, Hetmyer, Sandeep</div>
            <div className="text-[10px] text-slate-400 mt-1">Committed: ₹79.00 Cr</div>
          </div>
          <div className="p-3 bg-white border border-rr-border rounded-[2px]">
            <div className="text-slate-500 uppercase text-[10px]">Available Mini-Auction Purse</div>
            <div className="text-lg font-black text-rr-pink mt-1">₹28.50 – ₹34.00 Cr</div>
            <div className="text-[10px] text-slate-400 mt-1">From ₹120.00 Cr Base Cap</div>
          </div>
          <div className="p-3 bg-white border border-rr-border rounded-[2px]">
            <div className="text-slate-500 uppercase text-[10px]">Overseas Slots Remaining</div>
            <div className="text-lg font-black text-rr-navy mt-1">3 Slots Available</div>
            <div className="text-[10px] text-slate-400 mt-1">Hetmyer locked as OS #1</div>
          </div>
          <div className="p-3 bg-white border border-rr-border rounded-[2px]">
            <div className="text-slate-500 uppercase text-[10px]">Scoring Model</div>
            <div className="text-sm font-bold text-emerald-700 mt-1">AOS (Auction Opportunity)</div>
            <div className="text-[10px] text-slate-400 mt-1">BRS + Gap Fill + Purse Feasibility</div>
          </div>
        </div>

        {/* Filter Controls */}
        <div className="flex items-center gap-2 mb-8">
          <span className="text-xs font-mono text-slate-500 uppercase mr-2">Filter Roles:</span>
          <button
            onClick={() => setRoleFilter('all')}
            className={`px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold transition-all border ${
              roleFilter === 'all'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-rr-offwhite border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            All Shortlist ({targets.length})
          </button>
          <button
            onClick={() => setRoleFilter('batters')}
            className={`px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold transition-all border ${
              roleFilter === 'batters'
                ? 'bg-rr-pink text-white border-rr-pink'
                : 'bg-rr-offwhite border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            Batters & Finishers
          </button>
          <button
            onClick={() => setRoleFilter('bowlers')}
            className={`px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold transition-all border ${
              roleFilter === 'bowlers'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-rr-offwhite border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            Bowlers & Enforcers
          </button>
        </div>

        {/* Shortlist Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {filteredTargets.map((t, idx) => (
            <div
              key={t.name}
              className="p-6 rounded-[2px] bg-rr-offwhite border border-rr-border hover:border-rr-pink transition-all space-y-4"
            >
              {/* Header */}
              <div className="flex items-start justify-between pb-3 border-b border-rr-border">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-white text-rr-pink border border-rr-border uppercase">
                      TARGET #{idx + 1}
                    </span>
                    <span className="text-xs font-mono text-slate-500">{t.nationality}</span>
                  </div>
                  <h3 className="text-xl font-extrabold text-rr-navy">{t.name}</h3>
                  <div className="text-xs text-slate-600 font-mono mt-0.5">{t.role}</div>
                </div>

                <div className="text-right">
                  <div className="text-[10px] font-mono text-slate-500 uppercase">Opportunity Score</div>
                  <div className="text-2xl font-black text-rr-navy font-mono">
                    {t.aosScore.toFixed(1)}
                    <span className="text-xs font-normal text-slate-400">/100</span>
                  </div>
                  <div className="text-[10px] font-mono text-emerald-700 font-bold mt-0.5">
                    BRS {t.brsScore.toFixed(1)}
                  </div>
                </div>
              </div>

              {/* Auction Valuation & Feasibility */}
              <div className="grid grid-cols-2 gap-3 font-mono text-xs">
                <div className="p-2.5 rounded-[2px] bg-white border border-rr-border">
                  <span className="text-[10px] text-slate-500 uppercase block">Estimated Bid Range</span>
                  <span className="text-sm font-bold text-rr-pink">{t.estPrice}</span>
                </div>
                <div className="p-2.5 rounded-[2px] bg-white border border-rr-border">
                  <span className="text-[10px] text-slate-500 uppercase block">Purse Feasibility</span>
                  <span className="text-sm font-bold text-rr-navy">{t.feasibility}</span>
                </div>
              </div>

              {/* Contract & Squad Gap Details */}
              <div className="space-y-2 text-xs">
                <div className="p-2.5 rounded-[2px] bg-white border border-rr-border">
                  <span className="text-[10px] font-mono text-slate-500 uppercase font-semibold block mb-0.5">
                    Specific Rajasthan Royals Gap Addressed:
                  </span>
                  <p className="text-slate-700 leading-relaxed font-normal">{t.squadGap}</p>
                </div>
                <div className="p-2.5 rounded-[2px] bg-white border border-rr-border">
                  <span className="text-[10px] font-mono text-slate-500 uppercase font-semibold block mb-0.5">
                    SMS Jaipur Ground Dynamics Fit:
                  </span>
                  <p className="text-slate-700 leading-relaxed font-normal">{t.jaipurFit}</p>
                </div>
              </div>

              {/* Status footer */}
              <div className="flex items-center justify-between pt-2 text-[11px] font-mono text-slate-500 border-t border-rr-border/60">
                <span className="flex items-center gap-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                  <span>{t.contractStatus}</span>
                </span>
                <span className="text-slate-400">100% BCCI Compliant</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}