'use client';

import React from 'react';
import { Target, Shield, Trophy, CheckCircle2, ArrowRight } from 'lucide-react';

export default function RoyalMandateSection() {
  return (
    <section id="mandate" className="py-28 border-t border-rr-border/60 relative bg-rr-panel/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[1px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 01 / THE ROYAL MANDATE
          </span>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start mb-16">
          <div className="lg:col-span-8">
            <h2 className="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight uppercase font-display leading-[1.05]">
              BUILDING A CHAMPIONSHIP <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-rr-pink via-white to-rr-gold">
                SQUAD FOR IPL 2027.
              </span>
            </h2>
            <p className="mt-6 text-sm sm:text-base text-rr-muted leading-relaxed max-w-2xl">
              Traditional scouting relies on surface averages and boundary percentages accumulated in low-stakes phases. 
              The mandate of SupeRR Selector Season 2 is fundamentally different: to pinpoint players whose performance 
              <span className="text-white font-semibold"> elevates rather than collapses</span> when required run rates spike beyond 10.0, 
              wickets tumble, or playoff elimination looms.
            </p>
          </div>

          <div className="lg:col-span-4 p-6 rounded-2xl bg-rr-midnight border border-rr-border">
            <div className="text-xs font-mono font-bold text-rr-gold uppercase tracking-wider mb-2">
              Rajasthan Royals Retained Core
            </div>
            <p className="text-xs text-rr-muted leading-relaxed mb-4">
              Building around world-class retainers: Sanju Samson, Yashasvi Jaiswal, Riyan Parag, Dhruv Jurel, and Sandeep Sharma.
            </p>
            <div className="space-y-2 font-mono text-xs text-white">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-rr-pink" />
                <span>Top-Order Explosiveness (Secured)</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-rr-pink" />
                <span>Wicketkeeping & Finishing (Secured)</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-rr-gold" />
                <span>Death-Over Seam Hostility (Recruitment Priority)</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-rr-gold" />
                <span>Clutch Lower-Order Anchor (Recruitment Priority)</span>
              </div>
            </div>
          </div>
        </div>

        {/* 3 Pillar Strategic Mandate Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="p-8 rounded-2xl bg-gradient-to-b from-rr-panel to-rr-card border border-rr-border hover:border-rr-pink/60 transition-all duration-300 group">
            <div className="w-12 h-12 rounded-xl bg-rr-pink/15 border border-rr-pink/30 flex items-center justify-center mb-6 text-rr-pink font-mono font-bold text-sm">
              01
            </div>
            <h3 className="text-xl font-bold text-white group-hover:text-rr-pink transition-colors mb-3">
              Crucible Performance Over Reputation
            </h3>
            <p className="text-xs text-rr-muted leading-relaxed">
              Eliminating stat-padding in dead rubbers. Our Situational Leverage Index evaluates deliveries solely based on instantaneous pressure demands, isolating true clutch temperament.
            </p>
          </div>

          <div className="p-8 rounded-2xl bg-gradient-to-b from-rr-panel to-rr-card border border-rr-border hover:border-rr-gold/60 transition-all duration-300 group">
            <div className="w-12 h-12 rounded-xl bg-rr-gold/15 border border-rr-gold/30 flex items-center justify-center mb-6 text-rr-gold font-mono font-bold text-sm">
              02
            </div>
            <h3 className="text-xl font-bold text-white group-hover:text-rr-gold transition-colors mb-3">
              SMS Jaipur Dimension Match
            </h3>
            <p className="text-xs text-rr-muted leading-relaxed">
              Sawai Mansingh Stadium's 70m+ square boundaries punish errant hitting and reward restrictive mystery spin. Players must be anatomically suited to winning 7 home fixtures in Jaipur.
            </p>
          </div>

          <div className="p-8 rounded-2xl bg-gradient-to-b from-rr-panel to-rr-card border border-rr-border hover:border-white transition-all duration-300 group">
            <div className="w-12 h-12 rounded-xl bg-white/10 border border-white/20 flex items-center justify-center mb-6 text-white font-mono font-bold text-sm">
              03
            </div>
            <h3 className="text-xl font-bold text-white group-hover:text-rr-pink transition-colors mb-3">
              BCCI & IPL Regulatory Realism
            </h3>
            <p className="text-xs text-rr-muted leading-relaxed">
              Realism is our competitive edge. We distinguish between theoretical benchmarks and verified auction targets, ensuring Rajasthan Royals receives actionable, rule-compliant recommendations.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
