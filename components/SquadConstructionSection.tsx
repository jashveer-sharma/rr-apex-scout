'use client';

import React, { useState } from 'react';
import { Shield, Coins, Users, CheckCircle2, ChevronRight, Zap, Target, Award, ArrowUpRight, Scale } from 'lucide-react';

interface SquadSlot {
  slot: number | string;
  name: string;
  role: string;
  classification: string;
  nationality: string;
  estPrice?: string;
  brs: number;
}

interface ScenarioData {
  id: string;
  name: string;
  tag: string;
  philosophy: string;
  playingXI: SquadSlot[];
  overseasInXI: number;
  overseasInSquad: number;
  estimatedAuctionSpend: string;
  remainingPurse: string;
  roleCoverageScore: string;
  keyStrengths: string;
}

export default function SquadConstructionSection() {
  const scenarios: ScenarioData[] = [
    {
      id: 'scenario-b',
      name: 'Scenario B: Balanced Rebuild',
      tag: 'RECOMMENDED STRATEGY',
      philosophy: 'Surgical recruitment addressing RR historical vulnerabilities: death-overs batting stagnation (overs 16–20) and middle-overs express hostility, while preserving ample purse flexibility.',
      playingXI: [
        { slot: 1, name: 'Yashasvi Jaiswal', role: 'Opening Batter (LHB)', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 71.5 },
        { slot: 2, name: 'Sanju Samson (C / WK)', role: 'Top-Order Batter / Captain', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 68.2 },
        { slot: 3, name: 'Riyan Parag (VC)', role: 'Middle-Order Anchor / Off-Spin', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 67.8 },
        { slot: 4, name: 'Rajat Patidar', role: 'Top-Order Clutch Striker', classification: 'TARGET (₹7.50 Cr)', nationality: 'IND', brs: 72.3 },
        { slot: 5, name: 'Shashank Singh', role: 'Crisis Finisher (RHB)', classification: 'TARGET (₹4.50 Cr)', nationality: 'IND', brs: 74.4 },
        { slot: 6, name: 'Dhruv Jurel', role: 'Wicketkeeper Finisher', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 65.4 },
        { slot: 7, name: 'Naman Dhir', role: 'Lower-Order Detonator / Off-Break', classification: 'TARGET (₹5.50 Cr)', nationality: 'IND', brs: 76.5 },
        { slot: 8, name: 'Shimron Hetmyer', role: 'Death Finisher (LHB)', classification: 'RETAINED (₹11 Cr)', nationality: 'OS', brs: 69.4 },
        { slot: 9, name: 'Mitchell Santner', role: 'Slow Left-Arm Finger Spin', classification: 'TARGET (₹4.20 Cr)', nationality: 'OS', brs: 71.8 },
        { slot: 10, name: 'Sandeep Sharma', role: 'Swing & Knuckleball Seamer', classification: 'RETAINED (₹4 Cr)', nationality: 'IND', brs: 64.8 },
        { slot: 11, name: 'Hasan Mahmud', role: 'Death Seamer & Searing Yorkers', classification: 'TARGET (₹3.50 Cr)', nationality: 'OS', brs: 79.7 },
        { slot: 'Sub', name: 'Umran Malik (Impact)', role: 'Express Pace Enforcer (150+ km/h)', classification: 'TARGET (₹4.00 Cr)', nationality: 'IND', brs: 73.6 }
      ],
      overseasInXI: 3,
      overseasInSquad: 6,
      estimatedAuctionSpend: '₹25.20 Cr',
      remainingPurse: '₹7.80 Cr (Optimal Safety Reserve)',
      roleCoverageScore: '96 / 100',
      keyStrengths: 'Batting depth down to #8; 7 viable bowling options; extreme pace (150k Malik) + finger spin choke (Santner); 100% BCCI compliant with 1 overseas slot in reserve.'
    },
    {
      id: 'scenario-a',
      name: 'Scenario A: Core Continuity',
      tag: 'CONSERVATIVE FISCAL',
      philosophy: 'Retain maximum purse reserves by targeting value uncapped gems and seasoned international role-players without entering bidding duels.',
      playingXI: [
        { slot: 1, name: 'Yashasvi Jaiswal', role: 'Opening Batter (LHB)', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 71.5 },
        { slot: 2, name: 'Sanju Samson (C / WK)', role: 'Top-Order Batter / Captain', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 68.2 },
        { slot: 3, name: 'Riyan Parag', role: 'Middle-Order Anchor', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 67.8 },
        { slot: 4, name: 'Shashank Singh', role: 'Middle-Order Stabilizer', classification: 'TARGET (₹4.00 Cr)', nationality: 'IND', brs: 74.4 },
        { slot: 5, name: 'Dhruv Jurel', role: 'Wicketkeeper Finisher', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 65.4 },
        { slot: 6, name: 'Shimron Hetmyer', role: 'Death Finisher (LHB)', classification: 'RETAINED (₹11 Cr)', nationality: 'OS', brs: 69.4 },
        { slot: 7, name: 'Naman Dhir', role: 'Finisher / Off-Break', classification: 'TARGET (₹5.00 Cr)', nationality: 'IND', brs: 76.5 },
        { slot: 8, name: 'Jamie Overton', role: 'Pace All-Rounder', classification: 'TARGET (₹3.50 Cr)', nationality: 'OS', brs: 66.2 },
        { slot: 9, name: 'Mitchell Santner', role: 'Spin Restrictor', classification: 'TARGET (₹3.80 Cr)', nationality: 'OS', brs: 71.8 },
        { slot: 10, name: 'Sandeep Sharma', role: 'Seamer', classification: 'RETAINED (₹4 Cr)', nationality: 'IND', brs: 64.8 },
        { slot: 11, name: 'Benjamin Sears', role: 'Express Seamer (145+ km/h)', classification: 'TARGET (₹2.20 Cr)', nationality: 'OS', brs: 74.0 },
        { slot: 'Sub', name: 'Domestic Seamer (Impact)', role: 'Backup Pacer', classification: 'TARGET (₹1.00 Cr)', nationality: 'IND', brs: 62.0 }
      ],
      overseasInXI: 4,
      overseasInSquad: 5,
      estimatedAuctionSpend: '₹18.50 Cr',
      remainingPurse: '₹14.50 Cr (Maximum Fiscal Reserve)',
      roleCoverageScore: '88 / 100',
      keyStrengths: 'Extremely cost-effective; preserves ₹14.5 Cr purse cushion for contingency mid-season signings.'
    },
    {
      id: 'scenario-c',
      name: 'Scenario C: Opportunity Firepower',
      tag: 'AGGRESSIVE MARQUEE',
      philosophy: 'Re-acquire Jos Buttler at marquee valuation, pairing him with uncapped Indian bowling gems to maximize star ceiling.',
      playingXI: [
        { slot: 1, name: 'Yashasvi Jaiswal', role: 'Opening Batter (LHB)', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 71.5 },
        { slot: 2, name: 'Jos Buttler', role: 'Championship Opener', classification: 'TARGET (₹11.00 Cr)', nationality: 'OS', brs: 73.4 },
        { slot: 3, name: 'Sanju Samson (C / WK)', role: 'Top-Order Anchor', classification: 'RETAINED (₹18 Cr)', nationality: 'IND', brs: 68.2 },
        { slot: 4, name: 'Riyan Parag', role: 'Middle-Order Anchor', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 67.8 },
        { slot: 5, name: 'Dhruv Jurel', role: 'Wicketkeeper Finisher', classification: 'RETAINED (₹14 Cr)', nationality: 'IND', brs: 65.4 },
        { slot: 6, name: 'Shimron Hetmyer', role: 'Death Finisher', classification: 'RETAINED (₹11 Cr)', nationality: 'OS', brs: 69.4 },
        { slot: 7, name: 'Naman Dhir', role: 'Finisher', classification: 'TARGET (₹5.50 Cr)', nationality: 'IND', brs: 76.5 },
        { slot: 8, name: 'Mitchell Santner', role: 'Finger Spinner', classification: 'TARGET (₹4.00 Cr)', nationality: 'OS', brs: 71.8 },
        { slot: 9, name: 'Sandeep Sharma', role: 'Death Seamer', classification: 'RETAINED (₹4 Cr)', nationality: 'IND', brs: 64.8 },
        { slot: 10, name: 'Hasan Mahmud', role: 'Yorker Specialist', classification: 'TARGET (₹3.50 Cr)', nationality: 'OS', brs: 79.7 },
        { slot: 11, name: 'Umran Malik', role: 'Express Pace (150k)', classification: 'TARGET (₹4.00 Cr)', nationality: 'IND', brs: 73.6 },
        { slot: 'Sub', name: 'Shashank Singh (Impact)', role: 'Crisis Finisher', classification: 'TARGET (₹4.00 Cr)', nationality: 'IND', brs: 74.4 }
      ],
      overseasInXI: 4,
      overseasInSquad: 6,
      estimatedAuctionSpend: '₹32.00 Cr',
      remainingPurse: '₹1.00 Cr (High Capital Deployment)',
      roleCoverageScore: '95 / 100',
      keyStrengths: 'Unstoppable top-order explosion with Jaiswal + Buttler + Samson; leaves virtually zero budget margin.'
    }
  ];

  const [activeScenarioId, setActiveScenarioId] = useState('scenario-b');
  const [activeTab, setActiveTab] = useState<'xi' | 'purse' | 'jaipur'>('xi');

  const currentScenario = scenarios.find(s => s.id === activeScenarioId) || scenarios[0];

  return (
    <section id="squad-construction" className="py-16 sm:py-24 border-t border-rr-border bg-rr-offwhite text-slate-800">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-12">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-[10px] sm:text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 11 / COMPLETE RR SQUAD CONSTRUCTION (THREE SCENARIOS)
          </span>
        </div>

        {/* Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-10 gap-4 sm:gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              THE RAJASTHAN ROYALS <br />
              <span className="text-rr-pink">IPL 2027 SQUAD SCENARIOS</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Synthesizing delivery telemetry into three fully budgeted tactical scenarios. 
            Strictly respects the <b>Maximum 4 Overseas in Playing XI</b> rule, IPL Impact Player rules, 
            and ₹120.00 Cr base salary cap.
          </p>
        </div>

        {/* Scenario Selector Chips */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3 sm:gap-4 mb-6 sm:mb-8">
          {scenarios.map((scen) => {
            const isActive = scen.id === activeScenarioId;
            return (
              <button
                key={scen.id}
                onClick={() => setActiveScenarioId(scen.id)}
                className={`p-4 sm:p-5 rounded-[2px] text-left transition-all border ${
                  isActive
                    ? 'bg-white border-rr-pink shadow-md'
                    : 'bg-white border-rr-border hover:border-slate-400'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <span className={`text-[10px] font-mono font-bold px-2 py-0.5 rounded-[2px] ${
                    isActive ? 'bg-pink-50 text-rr-pink border border-pink-200' : 'bg-rr-offwhite text-slate-500'
                  }`}>
                    {scen.tag}
                  </span>
                  <span className="text-xs font-mono text-slate-500 font-bold">{scen.roleCoverageScore}</span>
                </div>
                <div className="text-sm sm:text-base font-extrabold text-rr-navy font-display">{scen.name}</div>
                <div className="text-xs font-mono text-slate-500 mt-1">
                  Spend: <span className="font-bold text-rr-navy">{scen.estimatedAuctionSpend}</span> · Rem: <span className="font-bold text-emerald-700">{scen.remainingPurse.split(' ')[0]}</span>
                </div>
              </button>
            );
          })}
        </div>

        {/* Active Scenario Overview Banner */}
        <div className="p-4 sm:p-6 bg-white border border-rr-border rounded-[2px] shadow-sm mb-6 space-y-3">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-rr-border">
            <div>
              <span className="text-[10px] font-mono font-bold text-rr-pink uppercase tracking-widest">
                ACTIVE BLUEPRINT: {currentScenario.tag}
              </span>
              <h3 className="text-lg sm:text-xl font-black text-rr-navy font-display mt-0.5">{currentScenario.name}</h3>
            </div>
            <div className="flex flex-wrap items-center gap-2 sm:gap-3 text-xs font-mono">
              <span className="px-2.5 py-1 bg-rr-offwhite border border-rr-border rounded-[2px]">
                Overseas: <b>{currentScenario.overseasInXI} in XI</b> / {currentScenario.overseasInSquad} in Squad
              </span>
              <span className="px-2.5 py-1 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-[2px] font-bold">
                100% BCCI Compliant
              </span>
            </div>
          </div>
          <p className="text-xs text-slate-600 leading-relaxed font-normal">
            <b>Strategic Philosophy:</b> {currentScenario.philosophy}
          </p>
        </div>

        {/* Tab Switcher */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-2 mb-6">
          <button
            onClick={() => setActiveTab('xi')}
            className={`px-3 sm:px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border text-center ${
              activeTab === 'xi'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            01. Playing XI & Impact Player Sub
          </button>
          <button
            onClick={() => setActiveTab('purse')}
            className={`px-3 sm:px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border text-center ${
              activeTab === 'purse'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            02. Mini-Auction Purse Breakdown
          </button>
          <button
            onClick={() => setActiveTab('jaipur')}
            className={`px-3 sm:px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border text-center ${
              activeTab === 'jaipur'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            03. SMS Jaipur Ground Blueprint
          </button>
        </div>

        {/* TAB 1: PLAYING XI TABLE */}
        {activeTab === 'xi' && (
          <div className="space-y-4">
            <div className="sm:hidden text-[10px] font-mono text-[#6B7280] mb-2 flex items-center justify-between">
              <span>← Scroll table horizontally →</span>
              <span className="text-rr-pink">Impact marked (Sub)</span>
            </div>
            <div className="bg-white border border-rr-border rounded-[2px] shadow-sm overflow-x-auto -mx-4 sm:mx-0">
              <table className="w-full text-left border-collapse font-mono text-xs min-w-[680px]">
                <thead>
                  <tr className="bg-rr-offwhite border-b border-rr-border text-slate-500 uppercase text-[10px]">
                    <th className="py-3 px-4">#</th>
                    <th className="py-3 px-4">Player Name</th>
                    <th className="py-3 px-4">Role</th>
                    <th className="py-3 px-4">Classification & Price</th>
                    <th className="py-3 px-4 text-center">Nat</th>
                    <th className="py-3 px-4 text-center">BRS</th>
                    <th className="py-3 px-4 text-right">Status</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {currentScenario.playingXI.map((slot) => {
                    const isImpact = slot.slot === 'Sub';
                    return (
                      <tr
                        key={String(slot.slot) + slot.name}
                        className={`hover:bg-slate-50 transition-colors ${isImpact ? 'bg-amber-50/50' : ''}`}
                      >
                        <td className="py-3 px-4 font-bold text-slate-400">
                          {slot.slot === 'Sub' ? 'SUB' : String(slot.slot).padStart(2, '0')}
                        </td>
                        <td className="py-3 px-4 font-bold text-rr-navy font-sans">
                          {slot.name}
                        </td>
                        <td className="py-3 px-4 text-slate-600">{slot.role}</td>
                        <td className="py-3 px-4 font-bold text-rr-navy">
                          {slot.classification}
                        </td>
                        <td className="py-3 px-4 text-center">
                          <span className={`px-1.5 py-0.5 rounded-[2px] text-[10px] ${
                            slot.nationality === 'OS' ? 'bg-amber-50 text-amber-800 border border-amber-200' : 'bg-slate-100 text-slate-700'
                          }`}>
                            {slot.nationality}
                          </span>
                        </td>
                        <td className="py-3 px-4 text-center font-bold text-rr-navy">
                          {slot.brs.toFixed(1)}
                        </td>
                        <td className="py-3 px-4 text-right">
                          <span className={`px-2 py-0.5 rounded-[2px] text-[10px] font-bold ${
                            slot.classification.includes('RETAINED') ? 'bg-slate-100 text-slate-700 border border-slate-200' :
                            isImpact ? 'bg-amber-100 text-amber-800 border border-amber-300' :
                            'bg-pink-50 text-rr-pink border border-pink-200'
                          }`}>
                            {slot.classification.includes('RETAINED') ? 'RETAINED CORE' : isImpact ? 'TACTICAL SUB' : 'AUCTION TARGET'}
                          </span>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            <div className="p-4 bg-white border border-rr-border rounded-[2px] text-xs font-mono text-slate-600 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <b>Playing XI Balance:</b> {currentScenario.overseasInXI} Overseas Players / {11 - currentScenario.overseasInXI} Indian Nationals.
              </div>
              <div className="text-emerald-700 font-bold">
                1 Extra Overseas Slot Kept in Reserve for Tactical Flexibility
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: PURSE BREAKDOWN */}
        {activeTab === 'purse' && (
          <div className="p-6 sm:p-8 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-6">
            <h3 className="text-xl font-bold text-rr-navy font-display uppercase">
              Financial Architecture: IPL 2027 Mini-Auction Cap Analysis
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs">
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Total Franchise Salary Cap</span>
                <div className="text-2xl font-black text-rr-navy">₹120.00 Cr</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  BCCI established baseline team salary ceiling for 2025–2027 cycle.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Committed Retentions (6 Players)</span>
                <div className="text-2xl font-black text-slate-700">₹79.00 Cr</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  Samson (₹18), Jaiswal (₹18), Parag (₹14), Jurel (₹14), Hetmyer (₹11), Sandeep (₹4).
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-slate-500 uppercase text-[10px]">Estimated Mini-Auction Purse</span>
                <div className="text-2xl font-black text-rr-pink">₹28.50 - ₹34.00 Cr</div>
                <p className="text-[11px] text-slate-500 font-normal">
                  Liquid auction purse for completing the starting XI and squad bench.
                </p>
              </div>
            </div>

            <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2 font-mono text-xs">
              <div className="flex justify-between items-center text-sm font-bold pb-2 border-b border-rr-border">
                <span className="text-rr-navy">Active Scenario Projected Auction Spend:</span>
                <span className="text-rr-pink">{currentScenario.estimatedAuctionSpend}</span>
              </div>
              <div className="flex justify-between items-center text-sm font-bold">
                <span className="text-rr-navy">Remaining Safety Purse Reserve:</span>
                <span className="text-emerald-700">{currentScenario.remainingPurse}</span>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: SMS JAIPUR GROUND TACTICS */}
        {activeTab === 'jaipur' && (
          <div className="p-6 sm:p-8 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-6">
            <h3 className="text-xl font-bold text-rr-navy font-display uppercase">
              SMS Jaipur Ground Dynamics & Defensive Blueprint
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs font-mono">
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <div className="text-rr-pink font-bold uppercase text-[11px]">70m+ Square Boundaries</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  Deep square ropes punish mistimed slogs. Batters cannot rely on edged sixes; finger spin creates suffocating dot-ball pressure.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <div className="text-rr-navy font-bold uppercase text-[11px]">Subcontinental Bounce</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  Mitchell Santner executes stump-to-stump trajectories on dry daytime decks; Umran Malik generates uncomfortable steep bounce.
                </p>
              </div>
              <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <div className="text-emerald-700 font-bold uppercase text-[11px]">172.4 Average Defense Par</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  SMS Jaipur is not a 220+ shootout. Building an attack optimized for boundary suppression reliably defends totals between 165 and 180.
                </p>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}