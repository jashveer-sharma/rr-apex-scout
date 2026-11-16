'use client';

import React, { useState } from 'react';
import { Users, Zap, Shield, Target, ArrowRight, CheckCircle2, TrendingUp, Sparkles, Scale, Activity } from 'lucide-react';

interface TandemItem {
  id: string;
  name: string;
  archetype: string;
  evidenceType: 'EMPIRICAL_PARTNERSHIP' | 'TACTICAL_PROJECTION';
  historicalBalls?: number;
  historicalRuns?: number;
  partnershipSr: number;
  dotBallPct: number;
  synergyScore: number;
  tacticalMechanism: string;
  jaipurAdvantage: string;
}

interface BowlingTandemItem {
  id: string;
  name: string;
  archetype: string;
  synergyScore: number;
  tacticalMechanism: string;
  jaipurAdvantage: string;
}

export default function PlayerCompatibilitySection() {
  const [activeTab, setActiveTab] = useState<'batting' | 'bowling' | 'balance'>('batting');

  const battingTandems: TandemItem[] = [
    {
      id: 'jaiswal-samson',
      name: 'Yashasvi Jaiswal & Sanju Samson',
      archetype: 'Top-Order Left-Right Velocity Engine',
      evidenceType: 'EMPIRICAL_PARTNERSHIP',
      historicalBalls: 842,
      historicalRuns: 1184,
      partnershipSr: 140.6,
      dotBallPct: 27.8,
      synergyScore: 95.0,
      tacticalMechanism: 'Jaiswal attacks aggressively in Powerplay (160+ SR vs Pace), allowing Samson to anchor and target middle-overs spin with clean slog-sweeps.',
      jaipurAdvantage: 'Exploits asymmetric SMS Jaipur boundary dimensions by rotating strike to target shorter square boundary.'
    },
    {
      id: 'samson-dhir',
      name: 'Sanju Samson & Naman Dhir',
      archetype: 'Anchor-Detonator High-Leverage Axis',
      evidenceType: 'TACTICAL_PROJECTION',
      partnershipSr: 168.5,
      dotBallPct: 26.5,
      synergyScore: 94.5,
      tacticalMechanism: 'Samson controls overs 11-16 manipulating fielders into the ring, removing run-rate pressure from Dhir who enters at #7 with mandate to detonate from ball 1.',
      jaipurAdvantage: 'Dhir straight power striking clears longest boundaries, neutralizing opposition boundary sweepers.'
    },
    {
      id: 'pant-shashank',
      name: 'Rishabh Pant & Shashank Singh',
      archetype: 'LHB-RHB Matchup Disruption Pair',
      evidenceType: 'TACTICAL_PROJECTION',
      partnershipSr: 172.0,
      dotBallPct: 28.1,
      synergyScore: 92.8,
      tacticalMechanism: 'Forces captains out of pre-programmed bowler match-ups. Continuous strike rotation induces fielding misalignments and boundary leaks.',
      jaipurAdvantage: 'Eliminates one-sided field sets at Sawai Mansingh Stadium.'
    },
    {
      id: 'parag-hetmyer',
      name: 'Riyan Parag & Shimron Hetmyer',
      archetype: 'Middle-Overs Spin Slog + Death Execution',
      evidenceType: 'EMPIRICAL_PARTNERSHIP',
      historicalBalls: 398,
      historicalRuns: 642,
      partnershipSr: 161.3,
      dotBallPct: 29.2,
      synergyScore: 93.5,
      tacticalMechanism: 'Parag neutralizes finger spin in overs 9–14, creating launchpad for Hetmyer to harvest pacers in overs 16–20 at 190+ SR.',
      jaipurAdvantage: 'Punishes back-of-length deliveries against SMS Jaipur subcontinental bounce.'
    }
  ];

  const bowlingTandems: BowlingTandemItem[] = [
    {
      id: 'sandeep-mahmud',
      name: 'Sandeep Sharma & Hasan Mahmud',
      archetype: 'Swing Craft & 140k Searing Yorker Death Vice',
      synergyScore: 96.0,
      tacticalMechanism: 'Sandeep utilizes wide knuckleballs and slower bouncers; Mahmud attacks the base of off-stump at 140 km/h. Opposition batters face extreme velocity and trajectory variance.',
      jaipurAdvantage: 'Defends sub-175 totals when night dew slows down the pitch.'
    },
    {
      id: 'narine-malik',
      name: 'Sunil Narine & Umran Malik',
      archetype: 'Mystery Spin Chokehold + 150+ km/h Raw Hostility',
      synergyScore: 97.5,
      tacticalMechanism: 'Narine restricts scoring to sub-6.5 RPO in overs 7-13. Panicked batters enter middle overs facing required rates above 11.0 and are forced to attack Umran Malik hostile pace.',
      jaipurAdvantage: 'SMS Jaipur 70m+ outfield converts mistimed pulls into simple boundary catches.'
    },
    {
      id: 'santner-sandeep',
      name: 'Mitchell Santner & Sandeep Sharma',
      archetype: 'Disciplined Control & Zero-Margin Containment',
      synergyScore: 93.0,
      tacticalMechanism: 'Both bowlers execute with near-zero error margins (<0.90 boundaries per over conceded). Stifles momentum in high-pressure chases.',
      jaipurAdvantage: 'Stump-to-stump accuracy punishes visiting teams unfamiliar with Jaipur bounce.'
    }
  ];

  const [selectedBattingIndex, setSelectedBattingIndex] = useState(0);
  const activeBatting = battingTandems[selectedBattingIndex];

  return (
    <section id="compatibility" className="py-24 border-t border-rr-border bg-rr-offwhite text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 08 / PLAYER COMPATIBILITY & COMBINATION STRATEGY
          </span>
        </div>

        {/* Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              CRICKET IS PLAYED IN PAIRS. <br />
              <span className="text-rr-pink">ENGINEERED COMBINATION SYNERGIES</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Squads cannot be formed by stacking eleven isolated stars. Our dedicated engine evaluates 
            empirical partnerships and complementary tactical projections to eliminate squad bottlenecks.
          </p>
        </div>

        {/* Mode Selector Tabs */}
        <div className="flex items-center gap-2 mb-8">
          <button
            onClick={() => setActiveTab('batting')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'batting'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            01. Batting Tandems (Empirical & Projected)
          </button>
          <button
            onClick={() => setActiveTab('bowling')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'bowling'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            02. Bowling Vices & Phase Coverage
          </button>
          <button
            onClick={() => setActiveTab('balance')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'balance'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            03. Playing XI Balance Matrix
          </button>
        </div>

        {/* TAB 1: BATTING TANDEMS */}
        {activeTab === 'batting' && (
          <div className="space-y-6">
            <div className="flex flex-wrap gap-2">
              {battingTandems.map((t, idx) => (
                <button
                  key={t.id}
                  onClick={() => setSelectedBattingIndex(idx)}
                  className={`px-3.5 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border flex items-center gap-2 ${
                    selectedBattingIndex === idx
                      ? 'bg-rr-navy text-white border-rr-navy'
                      : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
                  }`}
                >
                  <span>{t.name}</span>
                  <span className={`text-[10px] px-1.5 py-0.2 rounded-[2px] ${
                    t.evidenceType === 'EMPIRICAL_PARTNERSHIP' ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700'
                  }`}>
                    {t.evidenceType === 'EMPIRICAL_PARTNERSHIP' ? 'EMPIRICAL' : 'PROJECTION'}
                  </span>
                </button>
              ))}
            </div>

            {/* Selected Tandem Deep Dive */}
            <div className="p-6 sm:p-8 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-6">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-rr-border">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className={`px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold uppercase ${
                      activeBatting.evidenceType === 'EMPIRICAL_PARTNERSHIP'
                        ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                        : 'bg-amber-50 text-amber-800 border border-amber-200'
                    }`}>
                      {activeBatting.evidenceType === 'EMPIRICAL_PARTNERSHIP' ? 'Empirical Match Evidence' : 'Tactical Trait Projection'}
                    </span>
                    <span className="text-xs font-mono text-slate-500 font-bold">{activeBatting.archetype}</span>
                  </div>
                  <h3 className="text-2xl font-black text-rr-navy font-display">{activeBatting.name}</h3>
                </div>

                <div className="text-right">
                  <div className="text-[10px] font-mono text-slate-500 uppercase">Synergy Score</div>
                  <div className="text-2xl font-black text-rr-pink font-mono">{activeBatting.synergyScore}%</div>
                </div>
              </div>

              {/* Stats Strip */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono text-xs text-center">
                <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Partnership Strike Rate</div>
                  <div className="text-lg font-black text-rr-navy mt-0.5">{activeBatting.partnershipSr.toFixed(1)} SR</div>
                </div>
                <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Dot Ball Frequency</div>
                  <div className="text-lg font-black text-rr-navy mt-0.5">{activeBatting.dotBallPct.toFixed(1)}%</div>
                </div>
                <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Sample Telemetry</div>
                  <div className="text-lg font-black text-rr-navy mt-0.5">
                    {activeBatting.historicalBalls ? `${activeBatting.historicalBalls} balls` : 'Modeled Trait'}
                  </div>
                </div>
                <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Runs Scored Together</div>
                  <div className="text-lg font-black text-emerald-700 mt-0.5">
                    {activeBatting.historicalRuns ? `${activeBatting.historicalRuns} runs` : 'High Synergy'}
                  </div>
                </div>
              </div>

              {/* Mechanisms */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                  <span className="font-mono font-bold text-rr-navy uppercase text-[11px] block">Tactical Mechanism:</span>
                  <p className="text-slate-600 leading-relaxed font-normal">{activeBatting.tacticalMechanism}</p>
                </div>
                <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                  <span className="font-mono font-bold text-rr-navy uppercase text-[11px] block">SMS Jaipur Dimension Fit:</span>
                  <p className="text-slate-600 leading-relaxed font-normal">{activeBatting.jaipurAdvantage}</p>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: BOWLING VICES */}
        {activeTab === 'bowling' && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {bowlingTandems.map((bw) => (
              <div
                key={bw.id}
                className="p-6 bg-white border border-rr-border rounded-[2px] shadow-sm flex flex-col justify-between space-y-4"
              >
                <div>
                  <div className="flex items-center justify-between pb-3 border-b border-rr-border">
                    <span className="text-[10px] font-mono font-bold text-rr-pink uppercase tracking-wider">
                      {bw.archetype}
                    </span>
                    <span className="text-xs font-mono text-rr-navy font-bold">{bw.synergyScore}% Fit</span>
                  </div>

                  <h3 className="text-xl font-extrabold text-rr-navy font-display mt-3">
                    {bw.name}
                  </h3>

                  <div className="mt-3 text-xs text-slate-600 leading-relaxed space-y-2">
                    <p>{bw.tacticalMechanism}</p>
                    <div className="p-2.5 bg-rr-offwhite border border-rr-border rounded-[2px] font-mono text-[11px]">
                      <b>Jaipur Advantage:</b> {bw.jaipurAdvantage}
                    </div>
                  </div>
                </div>

                <div className="p-2 bg-rr-offwhite border border-rr-border text-center font-mono text-xs font-bold text-rr-navy rounded-[2px]">
                  Dual Bowling Execution Axis
                </div>
              </div>
            ))}
          </div>
        )}

        {/* TAB 3: BALANCE MATRIX */}
        {activeTab === 'balance' && (
          <div className="p-6 sm:p-8 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-6">
            <h3 className="text-xl font-bold text-rr-navy font-display uppercase">
              Rajasthan Royals Playing XI Structural Balance Audit
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs font-mono">
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Bowling Overs Depth</span>
                <div className="text-2xl font-black text-rr-navy">28 Overs</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  7 genuine bowling options in Playing XI + Impact Sub; insulates against bad days.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Batting Lineup Depth</span>
                <div className="text-2xl font-black text-rr-navy">Down to #8</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  Shimron Hetmyer at #8 guarantees continuous boundary threat through all 20 overs.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Pace / Spin Balance</span>
                <div className="text-2xl font-black text-rr-navy">12 Pace / 8 Spin</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  12 overs of 140k+ express pace and knuckleballs; 8 overs of precision finger/off spin.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Overseas Utilization</span>
                <div className="text-2xl font-black text-emerald-700">3 / 4 Slots</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  Leaves 1 overseas slot in reserve in Playing XI; 100% BCCI regulatory compliance.
                </p>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}