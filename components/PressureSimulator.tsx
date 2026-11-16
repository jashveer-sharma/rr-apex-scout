'use client';

import React, { useState } from 'react';
import { Flame, Shield, ArrowRight, Zap, Target, CheckCircle2 } from 'lucide-react';

interface BatterData {
  rank: number;
  name: string;
  pressSr: number;
  pressAvg: number;
  boundaryPct: number;
  archetype: string;
  rrTacticalFit: string;
}

interface BowlerData {
  rank: number;
  name: string;
  pressEcon: number;
  dotPct: number;
  archetype: string;
  rrTacticalFit: string;
}

interface SimulatorProps {
  batters: BatterData[];
  bowlers: BowlerData[];
}

export default function PressureSimulator({ batters, bowlers }: SimulatorProps) {
  const scenarios = [
    {
      id: 'jaipur-chase',
      title: 'THE JAIPUR CHASE',
      context: 'Chasing 185 at Sawai Mansingh Stadium',
      situation: 'Needs 45 runs off 20 balls • 5 wickets down • Required Run Rate: 13.5 RPO',
      piScore: 9.4,
      tier: 'Extreme Pressure',
      recommendedBatter: batters.find(b => b.name === 'Naman Dhir') || batters[2],
      alternateBatter: batters.find(b => b.name === 'Tim David') || batters[3],
      recommendedBowler: bowlers.find(bw => bw.name === 'Sunil Narine') || bowlers[5],
      tacticalAdvice: 'At SMS Jaipur with 70m square boundaries, batters must possess 360-degree ground-clearing power without accumulating dots. Naman Dhir (201.8 SR under pressure) provides instant boundary release.'
    },
    {
      id: 'death-defense',
      title: 'DEFENDING 12 IN THE 20TH OVER',
      context: 'Defending 172 at Wankhede / Eden Gardens in Playoff',
      situation: 'Opposition needs 13 off 6 balls • Set power-hitter on strike • Final over',
      piScore: 9.8,
      tier: 'Extreme Pressure',
      recommendedBatter: batters.find(b => b.name === 'Shashank Singh') || batters[3],
      alternateBatter: batters.find(b => b.name === 'Tim David') || batters[2],
      recommendedBowler: bowlers.find(bw => bw.name === 'Hasan Mahmud') || bowlers[0],
      tacticalAdvice: 'Hasan Mahmud maintains a 5.97 pressure economy and 49.6% dot ball frequency under extreme leverage, executing laser-guided block-hole yorkers.'
    },
    {
      id: 'early-collapse',
      title: 'TOP-ORDER RECOVERY FROM COLLAPSE',
      context: '1st Innings: 31/3 in Over 5.2 on a responsive pitch',
      situation: 'Top 3 back in pavilion • Ball moving under lights • Par score 175',
      piScore: 7.8,
      tier: 'High Pressure',
      recommendedBatter: batters.find(b => b.name === 'Suryakumar Yadav') || batters[0],
      alternateBatter: batters.find(b => b.name === 'Jos Buttler') || batters[4],
      recommendedBowler: bowlers.find(bw => bw.name === 'Mitchell Santner') || bowlers[4],
      tacticalAdvice: 'Requires elite crisis stabilization without allowing scoring momentum to halt. Suryakumar Yadav averages 57.3 with an 188.7 strike rate in high-pressure rebuilds, converting defensive consolidation into late acceleration.'
    },
    {
      id: 'middle-spin-choke',
      title: 'MIDDLE-OVERS CONTAINMENT (OVERS 7-15)',
      context: 'Opposition cruising at 68/1, targeting 200',
      situation: 'Set top-order batters accelerating • Deep boundaries in play',
      piScore: 7.2,
      tier: 'High Pressure',
      recommendedBatter: batters.find(b => b.name === 'Rajat Patidar') || batters[5],
      alternateBatter: batters.find(b => b.name === 'Rishabh Pant') || batters[9],
      recommendedBowler: bowlers.find(bw => bw.name === 'Sunil Narine') || bowlers[2],
      tacticalAdvice: 'Sunil Narine concedes just 6.37 economy under pressure with 40.2% dot balls. Unrivaled middle-overs chokehold that dries up boundaries and breaks threatening partnerships.'
    }
  ];

  const [activeScenario, setActiveScenario] = useState(scenarios[0]);

  return (
    <section id="simulator" className="py-24 border-t border-rr-border relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
          <div>
            <div className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase mb-2">
              CHAPTER 04 / MATCH SITUATION LAB
            </div>
            <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
              PRESSURE SIMULATOR
            </h2>
          </div>
          <p className="text-sm text-rr-muted max-w-md">
            Evaluate how our Bayesian-ranked players deploy into real match scenarios to solve high-stakes crises.
          </p>
        </div>

        {/* Scenario Selection Tabs */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 mb-8">
          {scenarios.map((sc) => (
            <button
              key={sc.id}
              onClick={() => setActiveScenario(sc)}
              className={`p-4 rounded-xl text-left border transition-all ${
                activeScenario.id === sc.id
                  ? 'bg-rr-card border-rr-pink shadow-lg shadow-rr-pink/15'
                  : 'bg-rr-panel/60 border-rr-border hover:border-rr-borderLight hover:bg-rr-card/40'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-mono font-bold text-rr-pink uppercase">
                  PI {sc.piScore}
                </span>
                <span className="text-[10px] font-mono text-rr-muted">
                  {sc.tier}
                </span>
              </div>
              <div className="text-sm font-bold text-white mb-1">
                {sc.title}
              </div>
              <div className="text-xs text-rr-muted line-clamp-1">
                {sc.context}
              </div>
            </button>
          ))}
        </div>

        {/* Active Scenario Display Panel */}
        <div className="p-6 sm:p-8 rounded-2xl bg-gradient-to-b from-rr-panel to-rr-card border border-rr-border shadow-2xl">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between pb-6 mb-6 border-b border-rr-border gap-4">
            <div>
              <div className="flex items-center gap-2 text-xs font-mono font-bold text-rr-pink uppercase mb-1">
                <Flame className="w-4 h-4 text-rr-pink" />
                <span>Simulated Situation: {activeScenario.title}</span>
              </div>
              <div className="text-xl sm:text-2xl font-extrabold text-white">
                {activeScenario.situation}
              </div>
              <div className="text-xs text-rr-muted mt-1">
                Context: {activeScenario.context}
              </div>
            </div>

            <div className="flex items-center gap-3">
              <div className="p-3 rounded-xl bg-rr-midnight border border-rr-border text-center">
                <div className="text-[10px] font-mono text-rr-muted uppercase">CALCULATED PI</div>
                <div className="text-2xl font-extrabold text-rr-pink font-display">
                  {activeScenario.piScore} <span className="text-xs text-rr-muted">/ 10</span>
                </div>
              </div>
            </div>
          </div>

          {/* Recommended Personnel Columns */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            {/* Batter Recommendation */}
            <div className="p-5 rounded-xl bg-rr-midnight/90 border border-rr-border">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-bold text-rr-pink uppercase">
                  OPTIMAL CLUTCH BATTER
                </span>
                <span className="text-xs font-mono text-rr-gold font-bold">
                  RANK #{activeScenario.recommendedBatter.rank}
                </span>
              </div>
              <h4 className="text-xl font-bold text-white mb-1">
                {activeScenario.recommendedBatter.name}
              </h4>
              <p className="text-xs text-rr-muted mb-4">
                {activeScenario.recommendedBatter.archetype}
              </p>

              <div className="grid grid-cols-3 gap-2 p-3 rounded-lg bg-rr-panel/60 border border-rr-border/60 text-center mb-3">
                <div>
                  <div className="text-[9px] text-rr-muted font-mono uppercase">Pressure SR</div>
                  <div className="text-sm font-bold text-white font-mono">{activeScenario.recommendedBatter.pressSr.toFixed(1)}</div>
                </div>
                <div>
                  <div className="text-[9px] text-rr-muted font-mono uppercase">Pressure Avg</div>
                  <div className="text-sm font-bold text-rr-gold font-mono">{activeScenario.recommendedBatter.pressAvg.toFixed(1)}</div>
                </div>
                <div>
                  <div className="text-[9px] text-rr-muted font-mono uppercase">Boundary %</div>
                  <div className="text-sm font-bold text-emerald-400 font-mono">{activeScenario.recommendedBatter.boundaryPct.toFixed(1)}%</div>
                </div>
              </div>

              <div className="text-xs text-rr-muted">
                <span className="text-white font-semibold">Backup Option:</span> {activeScenario.alternateBatter.name} (Rank #{activeScenario.alternateBatter.rank})
              </div>
            </div>

            {/* Bowler Recommendation */}
            <div className="p-5 rounded-xl bg-rr-midnight/90 border border-rr-border">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-mono font-bold text-rr-gold uppercase">
                  OPTIMAL CLUTCH BOWLER
                </span>
                <span className="text-xs font-mono text-rr-pink font-bold">
                  RANK #{activeScenario.recommendedBowler.rank}
                </span>
              </div>
              <h4 className="text-xl font-bold text-white mb-1">
                {activeScenario.recommendedBowler.name}
              </h4>
              <p className="text-xs text-rr-muted mb-4">
                {activeScenario.recommendedBowler.archetype}
              </p>

              <div className="grid grid-cols-2 gap-2 p-3 rounded-lg bg-rr-panel/60 border border-rr-border/60 text-center mb-3">
                <div>
                  <div className="text-[9px] text-rr-muted font-mono uppercase">Pressure Econ</div>
                  <div className="text-sm font-bold text-white font-mono">{activeScenario.recommendedBowler.pressEcon.toFixed(2)}</div>
                </div>
                <div>
                  <div className="text-[9px] text-rr-muted font-mono uppercase">Dot Ball %</div>
                  <div className="text-sm font-bold text-sky-400 font-mono">{activeScenario.recommendedBowler.dotPct.toFixed(1)}%</div>
                </div>
              </div>

              <div className="text-xs text-rr-muted">
                <span className="text-white font-semibold">Tactical Weapon:</span> High boundary suppression in high-leverage overs.
              </div>
            </div>
          </div>

          {/* Tactical Coaching Advice */}
          <div className="p-4 rounded-xl bg-rr-panel border border-rr-border flex items-start gap-3">
            <CheckCircle2 className="w-5 h-5 text-rr-pink flex-shrink-0 mt-0.5" />
            <div>
              <div className="text-xs font-bold text-white uppercase font-mono mb-1">
                Data Science Scouting Verdict:
              </div>
              <p className="text-xs text-rr-muted leading-relaxed">
                {activeScenario.tacticalAdvice}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
