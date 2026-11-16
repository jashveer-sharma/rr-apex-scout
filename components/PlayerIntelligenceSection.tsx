'use client';

import React, { useState } from 'react';
import { Sparkles, Activity, Shield, Target, Flame, TrendingUp, AlertCircle, ArrowRight, BarChart2 } from 'lucide-react';

interface PlayerIntelligenceProps {
  batters: any[];
  bowlers: any[];
}

export default function PlayerIntelligenceSection({ batters, bowlers }: PlayerIntelligenceProps) {
  const [selectedRole, setSelectedRole] = useState<'batter' | 'bowler'>('batter');
  
  // Select default featured player
  const [activeBatterIndex, setActiveBatterIndex] = useState(0); // Suryakumar Yadav
  const [activeBowlerIndex, setActiveBowlerIndex] = useState(0); // Hasan Mahmud

  const currentBatter = batters[activeBatterIndex] || batters[0];
  const currentBowler = bowlers[activeBowlerIndex] || bowlers[0];

  return (
    <section id="player-intelligence" className="py-24 border-t border-rr-border bg-rr-offwhite text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 06 / PLAYER BEHAVIOURAL DNA
          </span>
        </div>

        {/* Section Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              BEYOND SURFACE AVERAGES: <br />
              <span className="text-rr-pink">GRANULAR PLAYER MECHANISMS</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Investigating underlying delivery telemetry: shot execution frequencies under high Situational Leverage, 
            innings acceleration velocity, handedness containment, and dismissal vulnerability profiles.
          </p>
        </div>

        {/* Role Selector Tabs */}
        <div className="flex items-center gap-3 mb-8">
          <button
            onClick={() => setSelectedRole('batter')}
            className={`px-5 py-2.5 rounded-[2px] text-xs font-mono font-bold uppercase tracking-wider transition-all border ${
              selectedRole === 'batter'
                ? 'bg-rr-pink text-white border-rr-pink'
                : 'bg-white text-slate-600 hover:text-rr-navy border-rr-border'
            }`}
          >
            🏏 Batting Acceleration & Shot Arsenal
          </button>
          <button
            onClick={() => setSelectedRole('bowler')}
            className={`px-5 py-2.5 rounded-[2px] text-xs font-mono font-bold uppercase tracking-wider transition-all border ${
              selectedRole === 'bowler'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white text-slate-600 hover:text-rr-navy border-rr-border'
            }`}
          >
            🎯 Bowling Repertoires & Matchup Containment
          </button>
        </div>

        {/* BATTER INTELLIGENCE VIEW */}
        {selectedRole === 'batter' && currentBatter && (
          <div className="space-y-6">
            {/* Player Quick Selector Chips */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
              {batters.slice(0, 10).map((b, idx) => (
                <button
                  key={b.playerId || idx}
                  onClick={() => setActiveBatterIndex(idx)}
                  className={`px-3.5 py-1.5 rounded-[2px] text-xs font-mono font-bold shrink-0 transition-all border ${
                    activeBatterIndex === idx
                      ? 'bg-rr-navy text-white border-rr-navy'
                      : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy hover:border-slate-400'
                  }`}
                >
                  #{b.rank} {b.name}
                </button>
              ))}
            </div>

            {/* Main Intelligence Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
              {/* Left 5 Cols: Player Identity & Acceleration Curve */}
              <div className="lg:col-span-5 p-6 rounded-[2px] bg-white border border-rr-border space-y-5 shadow-sm">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-pink-50 text-rr-pink border border-pink-200 uppercase">
                      RANK #{currentBatter.rank} • {currentBatter.dna?.genomePersona || 'Clutch Batter'}
                    </span>
                    <span className="text-xs font-mono text-rr-navy font-black">
                      BRS {currentBatter.brsScore?.toFixed(1)}
                    </span>
                  </div>
                  <h3 className="text-2xl sm:text-3xl font-extrabold text-rr-navy">
                    {currentBatter.name}
                  </h3>
                  <div className="text-xs text-slate-500 font-mono mt-0.5">
                    {currentBatter.archetype} • {currentBatter.nationality || currentBatter.team}
                  </div>
                </div>

                {/* Innings Acceleration Curve */}
                <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-3">
                  <div className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider flex items-center justify-between">
                    <span>Innings Trajectory Curve</span>
                    <span className="text-[10px] text-rr-pink font-semibold">Strike Rate Acceleration</span>
                  </div>
                  
                  {currentBatter.dna?.trajectory && (
                    <div className="grid grid-cols-4 gap-2 text-center">
                      {currentBatter.dna.trajectory.map((t: any) => (
                        <div key={t.bracket} className="p-2 rounded-[2px] bg-white border border-rr-border">
                          <div className="text-[9px] font-mono uppercase text-slate-500">Balls {t.bracket}</div>
                          <div className={`text-sm font-black font-mono mt-1 ${
                            t.sr >= 170 ? 'text-rr-pink' : t.sr >= 140 ? 'text-rr-navy' : 'text-slate-600'
                          }`}>
                            {t.sr > 0 ? t.sr.toFixed(1) : '—'}
                          </div>
                          <div className="text-[9px] text-slate-400 font-mono">{t.balls}b</div>
                        </div>
                      ))}
                    </div>
                  )}
                  <p className="text-[11px] text-slate-600 leading-relaxed">
                    Evaluates whether the batter provides immediate scoring momentum (strike rate &gt;140 from ball 1) 
                    or functions as an innings consolidator requiring an initial anchor phase.
                  </p>
                </div>

                {/* Aggression Index Gauge */}
                <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-2">
                  <div className="flex justify-between text-xs font-mono">
                    <span className="text-slate-600 uppercase">Attacking Shot Index</span>
                    <span className="text-rr-pink font-bold">{currentBatter.dna?.aggressionIndex || 0}%</span>
                  </div>
                  <div className="w-full h-2 rounded-[2px] bg-slate-200 overflow-hidden">
                    <div
                      className="h-full bg-rr-pink"
                      style={{ width: `${Math.min(100, Math.max(0, currentBatter.dna?.aggressionIndex || 0))}%` }}
                    />
                  </div>
                  <div className="text-[10px] text-slate-500">
                    Proportion of high-risk scoring strokes (pulls, slogs, scoops, reverse sweeps) attempted under situational leverage.
                  </div>
                </div>
              </div>

              {/* Right 7 Cols: Shot Arsenal, Pace vs Spin & Dismissals */}
              <div className="lg:col-span-7 space-y-6">
                {/* Pace vs Spin Exploitation */}
                <div className="p-6 rounded-[2px] bg-white border border-rr-border shadow-sm">
                  <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider mb-4">
                    Pace vs Spin Matchup Velocity
                  </h4>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border text-center">
                      <div className="text-[10px] font-mono text-slate-500 uppercase">Vs Pace Bowlers</div>
                      <div className="text-2xl font-black text-rr-navy font-mono mt-1">
                        {currentBatter.dna?.paceVsSpin?.paceSr ? currentBatter.dna.paceVsSpin.paceSr.toFixed(1) : '—'}
                        <span className="text-xs font-normal text-slate-500"> SR</span>
                      </div>
                      <div className="text-[10px] text-slate-500 font-mono mt-0.5">
                        {currentBatter.dna?.paceVsSpin?.paceBalls || 0} deliveries faced
                      </div>
                    </div>
                    <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border text-center">
                      <div className="text-[10px] font-mono text-slate-500 uppercase">Vs Spin Bowlers</div>
                      <div className="text-2xl font-black text-rr-pink font-mono mt-1">
                        {currentBatter.dna?.paceVsSpin?.spinSr ? currentBatter.dna.paceVsSpin.spinSr.toFixed(1) : '—'}
                        <span className="text-xs font-normal text-slate-500"> SR</span>
                      </div>
                      <div className="text-[10px] text-slate-500 font-mono mt-0.5">
                        {currentBatter.dna?.paceVsSpin?.spinBalls || 0} deliveries faced
                      </div>
                    </div>
                  </div>
                </div>

                {/* Signature Stroke Arsenal & Dismissal Modes */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  {/* Top Strokes */}
                  <div className="p-6 rounded-[2px] bg-white border border-rr-border space-y-3 shadow-sm">
                    <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider mb-2">
                      Signature Stroke Arsenal
                    </h4>
                    {currentBatter.dna?.topStrokes?.length > 0 ? (
                      currentBatter.dna.topStrokes.map((s: any) => (
                        <div key={s.stroke} className="flex justify-between items-center text-xs py-1 border-b border-slate-100 last:border-none">
                          <span className="text-slate-700 font-medium">{s.stroke}</span>
                          <span className="font-mono text-rr-navy font-bold">{s.count} shots ({s.pct}%)</span>
                        </div>
                      ))
                    ) : (
                      <div className="text-xs text-slate-400 font-mono">Telemetry aggregate indexed</div>
                    )}
                  </div>

                  {/* Dismissal Breakdown */}
                  <div className="p-6 rounded-[2px] bg-white border border-rr-border space-y-3 shadow-sm">
                    <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider mb-2">
                      Dismissal Vulnerabilities
                    </h4>
                    <div className="text-[11px] text-slate-500 mb-1">
                      Total Wickets Conceded: <span className="text-rr-navy font-bold">{currentBatter.dna?.dismissalProfile?.totalDismissals || 0}</span>
                    </div>
                    {currentBatter.dna?.dismissalProfile?.topModes && Object.keys(currentBatter.dna.dismissalProfile.topModes).length > 0 ? (
                      Object.entries(currentBatter.dna.dismissalProfile.topModes).map(([mode, count]: any) => (
                        <div key={mode} className="flex justify-between items-center text-xs py-1 border-b border-slate-100 last:border-none">
                          <span className="text-slate-700 font-medium">{mode}</span>
                          <span className="font-mono text-rose-600 font-bold">{count} times</span>
                        </div>
                      ))
                    ) : (
                      <div className="text-xs text-slate-400 font-mono">Dismissal pattern clean</div>
                    )}
                  </div>
                </div>

                {/* Tactical Fit Summary Banner */}
                <div className="p-5 rounded-[2px] bg-white border-l-4 border-l-rr-pink border border-rr-border shadow-sm flex items-start gap-3">
                  <Sparkles className="w-5 h-5 text-rr-pink shrink-0 mt-0.5" />
                  <div>
                    <div className="text-xs font-mono font-bold text-rr-pink uppercase mb-1">
                      Rajasthan Royals 2027 Role Suitability:
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-normal">
                      {currentBatter.rrTacticalFit || 'High leverage strike weapon aligned to middle-to-lower order situational requirements.'}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* BOWLER INTELLIGENCE VIEW */}
        {selectedRole === 'bowler' && currentBowler && (
          <div className="space-y-6">
            {/* Player Quick Selector Chips */}
            <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
              {bowlers.slice(0, 10).map((bw, idx) => (
                <button
                  key={bw.playerId || idx}
                  onClick={() => setActiveBowlerIndex(idx)}
                  className={`px-3.5 py-1.5 rounded-[2px] text-xs font-mono font-bold shrink-0 transition-all border ${
                    activeBowlerIndex === idx
                      ? 'bg-rr-navy text-white border-rr-navy'
                      : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy hover:border-slate-400'
                  }`}
                >
                  #{bw.rank} {bw.name}
                </button>
              ))}
            </div>

            {/* Main Intelligence Grid for Bowler */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
              {/* Left 5 Cols: Bowler Identity & Delivery Style Arsenal */}
              <div className="lg:col-span-5 p-6 rounded-[2px] bg-white border border-rr-border space-y-5 shadow-sm">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-amber-50 text-amber-800 border border-amber-200 uppercase">
                      RANK #{currentBowler.rank} • {currentBowler.dna?.genomePersona || 'Clutch Bowler'}
                    </span>
                    <span className="text-xs font-mono text-rr-navy font-black">
                      BRS {currentBowler.brsScore?.toFixed(1)}
                    </span>
                  </div>
                  <h3 className="text-2xl sm:text-3xl font-extrabold text-rr-navy">
                    {currentBowler.name}
                  </h3>
                  <div className="text-xs text-slate-500 font-mono mt-0.5">
                    {currentBowler.archetype} • {currentBowler.nationality || currentBowler.team}
                  </div>
                </div>

                {/* Delivery Style Arsenal */}
                <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-3">
                  <div className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider flex items-center justify-between">
                    <span>Delivery Style Breakdown</span>
                    <span className="text-[10px] text-slate-500 font-semibold">Repertoire %</span>
                  </div>
                  
                  {currentBowler.dna?.topDeliveryStyles && (
                    <div className="grid grid-cols-2 gap-2 text-center">
                      {currentBowler.dna.topDeliveryStyles.map((st: any) => (
                        <div key={st.style} className="p-2 rounded-[2px] bg-white border border-rr-border">
                          <div className="text-[9px] font-mono uppercase text-slate-500">{st.style}</div>
                          <div className="text-base font-black font-mono text-rr-navy mt-1">
                            {st.pct}%
                          </div>
                          <div className="text-[9px] text-slate-400 font-mono">{st.count} balls</div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>

                {/* Dot Ball Induction Gauge */}
                <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-2">
                  <div className="flex justify-between text-xs font-mono">
                    <span className="text-slate-600 uppercase">Dot Ball Pressure Rate</span>
                    <span className="text-emerald-700 font-bold">{currentBowler.dotPct?.toFixed(1)}%</span>
                  </div>
                  <div className="w-full h-2 rounded-[2px] bg-slate-200 overflow-hidden">
                    <div
                      className="h-full bg-emerald-600"
                      style={{ width: `${Math.min(100, Math.max(0, currentBowler.dotPct || 0))}%` }}
                    />
                  </div>
                  <div className="text-[10px] text-slate-500">
                    {currentBowler.pressWickets || 0} wickets taken under pressure; critical for Jaipur SMS boundary defense.
                  </div>
                </div>
              </div>

              {/* Right 7 Cols: RHB vs LHB & Phase Containment */}
              <div className="lg:col-span-7 space-y-6">
                {/* RHB vs LHB Matchup Split */}
                <div className="p-6 rounded-[2px] bg-white border border-rr-border shadow-sm">
                  <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider mb-4">
                    Handedness Matchup Containment (RHB vs LHB)
                  </h4>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border text-center">
                      <div className="text-[10px] font-mono text-slate-500 uppercase">Vs Right-Hand Batters</div>
                      <div className="text-2xl font-black text-rr-navy font-mono mt-1">
                        {currentBowler.dna?.rhbVsLhb?.RHB?.econ ? currentBowler.dna.rhbVsLhb.RHB.econ.toFixed(2) : '—'}
                        <span className="text-xs font-normal text-slate-500"> Econ</span>
                      </div>
                      <div className="text-[10px] text-slate-500 font-mono mt-0.5">
                        {currentBowler.dna?.rhbVsLhb?.RHB?.dotPct || 0}% dots • {currentBowler.dna?.rhbVsLhb?.RHB?.wkts || 0} wkts
                      </div>
                    </div>
                    <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border text-center">
                      <div className="text-[10px] font-mono text-slate-500 uppercase">Vs Left-Hand Batters</div>
                      <div className="text-2xl font-black text-rr-pink font-mono mt-1">
                        {currentBowler.dna?.rhbVsLhb?.LHB?.econ ? currentBowler.dna.rhbVsLhb.LHB.econ.toFixed(2) : '—'}
                        <span className="text-xs font-normal text-slate-500"> Econ</span>
                      </div>
                      <div className="text-[10px] text-slate-500 font-mono mt-0.5">
                        {currentBowler.dna?.rhbVsLhb?.LHB?.dotPct || 0}% dots • {currentBowler.dna?.rhbVsLhb?.LHB?.wkts || 0} wkts
                      </div>
                    </div>
                  </div>
                </div>

                {/* Phase Containment Matrix */}
                <div className="p-6 rounded-[2px] bg-white border border-rr-border space-y-3 shadow-sm">
                  <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider mb-2">
                    Phase Containment Matrix
                  </h4>
                  <div className="grid grid-cols-3 gap-3 text-center">
                    {['Powerplay', 'Middle', 'Death'].map(phase => {
                      const p = currentBowler.dna?.phaseBreakdown?.[phase] || { econ: 0, dotPct: 0, wkts: 0 };
                      return (
                        <div key={phase} className="p-3 rounded-[2px] bg-rr-offwhite border border-rr-border">
                          <div className="text-[10px] font-mono uppercase text-slate-500">{phase}</div>
                          <div className="text-lg font-bold font-mono text-rr-navy mt-1">
                            {p.econ > 0 ? p.econ.toFixed(2) : '—'} RPO
                          </div>
                          <div className="text-[9px] text-slate-500 font-mono">{p.dotPct}% dots • {p.wkts} wkts</div>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* Tactical Fit Summary Banner */}
                <div className="p-5 rounded-[2px] bg-white border-l-4 border-l-rr-navy border border-rr-border shadow-sm flex items-start gap-3">
                  <Sparkles className="w-5 h-5 text-rr-navy shrink-0 mt-0.5" />
                  <div>
                    <div className="text-xs font-mono font-bold text-rr-navy uppercase mb-1">
                      Rajasthan Royals 2027 Role Suitability:
                    </div>
                    <p className="text-xs text-slate-700 leading-relaxed font-normal">
                      {currentBowler.rrTacticalFit || 'Specialized delivery execution profile engineered to restrict run rates in high-leverage phases.'}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}