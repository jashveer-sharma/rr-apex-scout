'use client';

import React, { useState } from 'react';
import { Calculator, Cpu, Filter, Layers, CheckCircle2, ShieldCheck, ArrowRight, BarChart3, Database } from 'lucide-react';

export default function MethodologySection() {
  const [activeTab, setActiveTab] = useState<'sli' | 'bayes' | 'robustness'>('sli');

  return (
    <section id="methodology" className="py-24 border-t border-rr-border bg-rr-offwhite text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 13 / MATHEMATICAL METHODOLOGY & AUDIT
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-end mb-12 pb-6 border-b border-rr-border">
          <div className="lg:col-span-8">
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              THE MATHEMATICS OF <br />
              <span className="text-rr-pink">CLUTCH TEMPERAMENT</span>
            </h2>
            <p className="mt-4 text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl font-normal">
              Traditional analytics evaluate players on static aggregate averages. Our system calculates instantaneous 
              situational pressure for every delivery, applying Bayesian shrinkage to eliminate small-sample noise 
              and reveal true underlying performance distributions.
            </p>
          </div>

          <div className="lg:col-span-4 flex lg:justify-end">
            <div className="p-3 rounded-[2px] bg-white border border-rr-border text-xs font-mono text-slate-600 flex items-center gap-2 shadow-sm">
              <Database className="w-4 h-4 text-emerald-600 flex-shrink-0" />
              <span>200,999 Deliveries • 883 Matches • M₀ = 60 Shrinkage</span>
            </div>
          </div>
        </div>

        {/* Tab Selector */}
        <div className="flex items-center gap-2 mb-8">
          <button
            onClick={() => setActiveTab('sli')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'sli'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            01. Situational Leverage Index (SLI)
          </button>
          <button
            onClick={() => setActiveTab('bayes')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'bayes'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            02. Empirical Bayes Shrinkage
          </button>
          <button
            onClick={() => setActiveTab('robustness')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'robustness'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            03. Sensitivity & Validation
          </button>
        </div>

        {/* TAB 1: SLI */}
        {activeTab === 'sli' && (
          <div className="p-6 sm:p-8 rounded-[2px] bg-white border border-rr-border shadow-sm space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              <div className="lg:col-span-7 space-y-4">
                <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-pink-50 text-rr-pink border border-pink-200 uppercase tracking-widest">
                  Continuous Ball-by-Ball Formulation
                </span>
                <h3 className="text-2xl font-bold text-rr-navy font-display">
                  Why Binary Phase Filters Distort Player Value
                </h3>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  Most analysts classify &quot;pressure&quot; using crude phase bins (e.g. overs 16–20). This is deeply flawed:
                  batting in the 18th over needing 12 runs from 18 balls with 8 wickets in hand is <em>zero pressure</em>, 
                  whereas batting in the 4th over at 15/3 chasing 215 is <em>extreme crisis pressure</em>.
                </p>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  Our Situational Leverage Index (SLI) computes a continuous scalar from 0.0 to 3.0+ for every single ball 
                  as a weighted function of required run rate velocity, resources remaining, innings phase, and match context.
                </p>
              </div>

              <div className="lg:col-span-5 p-5 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-3 font-mono text-xs">
                <div className="text-rr-navy font-bold uppercase tracking-wider text-[11px]">
                  SLI Formula Specification
                </div>
                <div className="p-3 bg-white border border-rr-border rounded-[2px] text-slate-800 font-mono text-[11px] leading-relaxed">
                  SLI = [ (RRR / 8.5)^1.25 ] × [ 1 + (W_lost / 10)^1.5 ] × [ 1 + 0.35 × Phase_Factor ]
                </div>
                <ul className="space-y-1.5 text-slate-600 text-[11px] list-disc list-inside">
                  <li><strong>RRR</strong>: Instantaneous required run rate per over</li>
                  <li><strong>W_lost</strong>: Wickets already lost by the batting side</li>
                  <li><strong>Phase_Factor</strong>: Normalized weight by over (Overs 16–20 = 1.0, 7–15 = 0.5, 1–6 = 0.2)</li>
                  <li><strong>High-Pressure Threshold</strong>: Deliveries with SLI ≥ 1.20</li>
                </ul>
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: BAYES */}
        {activeTab === 'bayes' && (
          <div className="p-6 sm:p-8 rounded-[2px] bg-white border border-rr-border shadow-sm space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
              <div className="lg:col-span-7 space-y-4">
                <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-pink-50 text-rr-pink border border-pink-200 uppercase tracking-widest">
                  Empirical Bayes Prior Stabilization
                </span>
                <h3 className="text-2xl font-bold text-rr-navy font-display">
                  Eliminating Small-Sample Flukes
                </h3>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  In T20 tournaments, a batter who hits 24 runs off 8 balls in two death overs appears to have an astronomical 
                  300.0 strike rate. If recruited on surface averages, they frequently disappoint.
                </p>
                <p className="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
                  Our Empirical Bayes Shrinkage regresses raw observed performance toward the league-wide population mean 
                  using a shrinkage prior threshold of M₀ = 60 deliveries. Players with fewer deliveries are shrunk heavily toward 
                  league baseline; players with 200+ deliveries express their true talent level.
                </p>
              </div>

              <div className="lg:col-span-5 p-5 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-3 font-mono text-xs">
                <div className="text-rr-navy font-bold uppercase tracking-wider text-[11px]">
                  Shrinkage Equation
                </div>
                <div className="p-3 bg-white border border-rr-border rounded-[2px] text-slate-800 font-mono text-[11px] leading-relaxed">
                  θ_shrunk = [ N / (N + M₀) ] × θ_observed + [ M₀ / (N + M₀) ] × μ_league
                </div>
                <ul className="space-y-1.5 text-slate-600 text-[11px] list-disc list-inside">
                  <li><strong>N</strong>: High-pressure deliveries faced or bowled</li>
                  <li><strong>M₀ = 60</strong>: Prior sample weight</li>
                  <li><strong>μ_league</strong>: League mean under pressure (SR = 132.4, Econ = 8.64)</li>
                  <li><strong>Shrinkage Weight</strong>: N / (N + 60)</li>
                </ul>
              </div>
            </div>
          </div>
        )}

        {/* TAB 3: ROBUSTNESS */}
        {activeTab === 'robustness' && (
          <div className="p-6 sm:p-8 rounded-[2px] bg-white border border-rr-border shadow-sm space-y-6">
            <h3 className="text-xl font-bold text-rr-navy font-display uppercase">
              Sensitivity & Audit Trail Verification
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs">
              <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-2">
                <div className="text-rr-navy font-bold uppercase text-[11px]">M₀ Sensitivity Sweep</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  Tested M₀ values from 30 to 120. Rankings for top 10 candidates remain 94.2% rank-order stable across variations.
                </p>
              </div>
              <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-2">
                <div className="text-rr-navy font-bold uppercase text-[11px]">Strict Upstream Filter</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  68 ineligible player records identified and audited into <code>audit_trail_excluded_records.json</code> with zero public UI exposure.
                </p>
              </div>
              <div className="p-4 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-2">
                <div className="text-emerald-700 font-bold uppercase text-[11px]">100% Deterministic</div>
                <p className="text-slate-600 font-sans leading-relaxed">
                  Fully reproducible Python pipeline executes in &lt;1.5 seconds directly from raw delivery telemetry.
                </p>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}