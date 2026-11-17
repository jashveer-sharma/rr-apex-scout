'use client';

import React, { useState } from 'react';
import { ArrowLeftRight, Check, Award, Zap, Shield, Sparkles } from 'lucide-react';

interface PlayerLite {
  name: string;
  type: 'batter' | 'bowler';
  metric1Label: string;
  metric1Val: number;
  metric2Label: string;
  metric2Val: number;
  deltaLabel: string;
  deltaVal: number;
  dotPct: number;
  brsScore: number;
  archetype: string;
}

export default function HeadToHeadComparison() {
  const playerPool: PlayerLite[] = [
    {
      name: 'Suryakumar Yadav',
      type: 'batter',
      metric1Label: 'Pressure SR',
      metric1Val: 188.4,
      metric2Label: 'Pressure Avg',
      metric2Val: 56.3,
      deltaLabel: 'ΔSR (vs Base)',
      deltaVal: 22.5,
      dotPct: 28.2,
      brsScore: 79.0,
      archetype: '360° Game Breaker (824 balls faced)'
    },
    {
      name: 'Naman Dhir',
      type: 'batter',
      metric1Label: 'Pressure SR',
      metric1Val: 201.8,
      metric2Label: 'Pressure Avg',
      metric2Val: 41.8,
      deltaLabel: 'ΔSR (vs Base)',
      deltaVal: 32.0,
      dotPct: 29.1,
      brsScore: 76.5,
      archetype: 'Dynamic High-Ceiling Finisher'
    },
    {
      name: 'Shashank Singh',
      type: 'batter',
      metric1Label: 'Pressure SR',
      metric1Val: 182.5,
      metric2Label: 'Pressure Avg',
      metric2Val: 56.8,
      deltaLabel: 'ΔSR (vs Base)',
      deltaVal: 20.9,
      dotPct: 27.4,
      brsScore: 74.4,
      archetype: 'Crisis Chase Specialist'
    },
    {
      name: 'Jos Buttler',
      type: 'batter',
      metric1Label: 'Pressure SR',
      metric1Val: 187.9,
      metric2Label: 'Pressure Avg',
      metric2Val: 40.7,
      deltaLabel: 'ΔSR (vs Base)',
      deltaVal: 32.6,
      dotPct: 28.6,
      brsScore: 73.4,
      archetype: 'World-Class Championship Opener'
    },
    {
      name: 'Tim David',
      type: 'batter',
      metric1Label: 'Pressure SR',
      metric1Val: 184.2,
      metric2Label: 'Pressure Avg',
      metric2Val: 45.1,
      deltaLabel: 'ΔSR (vs Base)',
      deltaVal: 25.8,
      dotPct: 30.2,
      brsScore: 75.2,
      archetype: 'Death-Overs Power Striker'
    },
    {
      name: 'Umran Malik',
      type: 'bowler',
      metric1Label: 'Pressure Econ',
      metric1Val: 8.19,
      metric2Label: 'Wickets',
      metric2Val: 20,
      deltaLabel: 'Dot Ball %',
      deltaVal: 48.5,
      dotPct: 48.5,
      brsScore: 73.6,
      archetype: '150+ km/h Indian Express Enforcer'
    },
    {
      name: 'Sunil Narine',
      type: 'bowler',
      metric1Label: 'Pressure Econ',
      metric1Val: 6.37,
      metric2Label: 'Wickets',
      metric2Val: 45,
      deltaLabel: 'ΔEcon (Tighter)',
      deltaVal: 0.39,
      dotPct: 40.2,
      brsScore: 73.0,
      archetype: 'Veteran Chokehold Legend'
    },
    {
      name: 'Mitchell Santner',
      type: 'bowler',
      metric1Label: 'Pressure Econ',
      metric1Val: 6.83,
      metric2Label: 'Wickets',
      metric2Val: 24,
      deltaLabel: 'Dot Ball %',
      deltaVal: 41.5,
      dotPct: 41.5,
      brsScore: 71.8,
      archetype: 'Left-Arm Finger Spin Restrictor'
    },
    {
      name: 'Jasprit Bumrah',
      type: 'bowler',
      metric1Label: 'Pressure Econ',
      metric1Val: 7.22,
      metric2Label: 'Wickets',
      metric2Val: 62,
      deltaLabel: 'Dot Ball %',
      deltaVal: 37.9,
      dotPct: 37.9,
      brsScore: 65.2,
      archetype: 'Elite Death-Over Executioner'
    }
  ];

  const [playerA, setPlayerA] = useState<PlayerLite>(playerPool[0]);
  const [playerB, setPlayerB] = useState<PlayerLite>(playerPool[1]);

  return (
    <section id="compare" className="py-16 sm:py-24 border-t border-rr-border bg-white text-slate-800">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-12">
        {/* Section Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-[10px] sm:text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 07 / HEAD-TO-HEAD LAB
          </span>
        </div>

        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-12 gap-4 sm:gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              PLAYER COMPARISON & <span className="text-rr-pink">DELTAS</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Side-by-side comparative diagnostics evaluating situational strike-rate lifts, dot-ball control, 
            and Bayesian Rating Scores across direct tactical alternatives.
          </p>
        </div>

        {/* Quick Selector Presets */}
        <div className="flex flex-wrap items-center gap-1.5 sm:gap-2 mb-6 sm:mb-8">
          <span className="text-xs font-mono text-slate-500 mr-1 sm:mr-2 uppercase">Curated Matchups:</span>
          <button
            onClick={() => { setPlayerA(playerPool[0]); setPlayerB(playerPool[1]); }}
            className="px-2.5 sm:px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold bg-rr-offwhite border border-rr-border hover:border-rr-pink hover:text-rr-pink text-slate-700 transition-all"
          >
            Suryakumar vs Naman Dhir
          </button>
          <button
            onClick={() => { setPlayerA(playerPool[1]); setPlayerB(playerPool[2]); }}
            className="px-2.5 sm:px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold bg-rr-offwhite border border-rr-border hover:border-rr-pink hover:text-rr-pink text-slate-700 transition-all"
          >
            Naman Dhir vs Shashank Singh
          </button>
          <button
            onClick={() => { setPlayerA(playerPool[5]); setPlayerB(playerPool[6]); }}
            className="px-2.5 sm:px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold bg-rr-offwhite border border-rr-border hover:border-rr-pink hover:text-rr-pink text-slate-700 transition-all"
          >
            Umran Malik vs Sunil Narine
          </button>
          <button
            onClick={() => { setPlayerA(playerPool[6]); setPlayerB(playerPool[7]); }}
            className="px-2.5 sm:px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold bg-rr-offwhite border border-rr-border hover:border-rr-pink hover:text-rr-pink text-slate-700 transition-all"
          >
            Sunil Narine vs Mitchell Santner
          </button>
        </div>

        {/* Comparison Arena */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 relative">
          {/* Middle VS Badge */}
          <div className="hidden md:flex absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 rounded-[2px] bg-rr-navy border border-rr-navy items-center justify-center font-black text-xs text-white shadow-md z-20 font-mono">
            VS
          </div>

          {/* Player A Card */}
          <div className="p-4 sm:p-8 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-4 sm:space-y-6">
            <div className="flex justify-between items-start pb-4 border-b border-rr-border">
              <div className="w-full max-w-[65%] sm:max-w-[70%]">
                <span className="text-[10px] font-mono font-bold text-rr-pink uppercase tracking-widest block mb-1">
                  SELECTION A
                </span>
                <select
                  value={playerA.name}
                  onChange={(e) => {
                    const found = playerPool.find(p => p.name === e.target.value);
                    if (found) setPlayerA(found);
                  }}
                  className="w-full bg-white border border-rr-border rounded-[2px] text-xs sm:text-sm font-bold text-rr-navy px-2.5 sm:px-3 py-2 focus:outline-none focus:border-rr-pink"
                >
                  {playerPool.map(p => (
                    <option key={p.name} value={p.name}>{p.name} ({p.type})</option>
                  ))}
                </select>
              </div>
              <div className="text-right">
                <span className="text-[10px] font-mono text-slate-500 uppercase block">BRS SCORE</span>
                <div className="text-xl sm:text-2xl font-black text-rr-navy font-mono">{playerA.brsScore.toFixed(1)}</div>
              </div>
            </div>

            <p className="text-xs text-slate-600 font-mono">{playerA.archetype}</p>

            <div className="space-y-2.5 sm:space-y-3 font-mono text-xs">
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerA.metric1Label}</span>
                <span className="text-sm sm:text-base font-bold text-rr-navy">{playerA.metric1Val}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerA.metric2Label}</span>
                <span className="text-sm sm:text-base font-bold text-rr-navy">{playerA.metric2Val}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerA.deltaLabel}</span>
                <span className="text-sm sm:text-base font-bold text-emerald-700">+{playerA.deltaVal.toFixed(1)}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">Dot Ball Frequency</span>
                <span className="text-sm sm:text-base font-bold text-rr-pink">{playerA.dotPct}%</span>
              </div>
            </div>
          </div>

          {/* Player B Card */}
          <div className="p-4 sm:p-8 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-4 sm:space-y-6">
            <div className="flex justify-between items-start pb-4 border-b border-rr-border">
              <div className="w-full max-w-[65%] sm:max-w-[70%]">
                <span className="text-[10px] font-mono font-bold text-slate-600 uppercase tracking-widest block mb-1">
                  SELECTION B
                </span>
                <select
                  value={playerB.name}
                  onChange={(e) => {
                    const found = playerPool.find(p => p.name === e.target.value);
                    if (found) setPlayerB(found);
                  }}
                  className="w-full bg-white border border-rr-border rounded-[2px] text-xs sm:text-sm font-bold text-rr-navy px-2.5 sm:px-3 py-2 focus:outline-none focus:border-rr-pink"
                >
                  {playerPool.map(p => (
                    <option key={p.name} value={p.name}>{p.name} ({p.type})</option>
                  ))}
                </select>
              </div>
              <div className="text-right">
                <span className="text-[10px] font-mono text-slate-500 uppercase block">BRS SCORE</span>
                <div className="text-xl sm:text-2xl font-black text-rr-navy font-mono">{playerB.brsScore.toFixed(1)}</div>
              </div>
            </div>

            <p className="text-xs text-slate-600 font-mono">{playerB.archetype}</p>

            <div className="space-y-2.5 sm:space-y-3 font-mono text-xs">
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerB.metric1Label}</span>
                <span className="text-sm sm:text-base font-bold text-rr-navy">{playerB.metric1Val}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerB.metric2Label}</span>
                <span className="text-sm sm:text-base font-bold text-rr-navy">{playerB.metric2Val}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">{playerB.deltaLabel}</span>
                <span className="text-sm sm:text-base font-bold text-emerald-700">+{playerB.deltaVal.toFixed(1)}</span>
              </div>
              <div className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-rr-border flex justify-between items-center">
                <span className="text-slate-600">Dot Ball Frequency</span>
                <span className="text-sm sm:text-base font-bold text-rr-pink">{playerB.dotPct}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}