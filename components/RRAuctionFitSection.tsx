'use client';

import React from 'react';
import { Shield, Target, Landmark, Coins, CheckCircle, ArrowRight } from 'lucide-react';

export default function RRAuctionFitSection() {
  return (
    <section id="auction-fit" className="py-24 border-t border-rr-border relative bg-rr-midnight/40">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-4">
          <div>
            <div className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase mb-2">
              CHAPTER 07 / IPL 2027 MEGA-AUCTION TACTICAL BLUEPRINT
            </div>
            <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
              RAJASTHAN ROYALS SQUAD FIT
            </h2>
          </div>
          <p className="text-sm text-rr-muted max-w-md">
            Directly translating delivery-level pressure findings into actionable auction bids for Sawai Mansingh Stadium (SMS Jaipur).
          </p>
        </div>

        {/* SMS Jaipur Ground Dynamics Banner */}
        <div className="p-6 sm:p-8 rounded-2xl bg-gradient-to-r from-rr-panel via-rr-card to-rr-panel border border-rr-border shadow-xl mb-12">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="max-w-3xl">
              <span className="px-3 py-1 rounded-full text-xs font-mono font-bold bg-rr-pink/20 text-rr-pink border border-rr-pink/30 mb-3 inline-block">
                SMS JAIPUR GROUND INTELLIGENCE
              </span>
              <h3 className="text-xl sm:text-2xl font-bold text-white mb-2">
                Why Sawai Mansingh Stadium Demands Unique Pressure Archetypes
              </h3>
              <p className="text-xs sm:text-sm text-rr-muted leading-relaxed">
                SMS Jaipur possesses large square boundaries (70m+) and true subcontinental bounce. 
                Batters cannot survive on miscued edge-boundaries; they require authentic 360-degree power and strike-rotation. 
                Conversely, defensive spinners who induce high dot-ball frequencies (such as Sunil Narine and Mitchell Santner) 
                create suffocating chokeholds as opposition required run rates climb above 10.5 RPO.
              </p>
            </div>
            <div className="p-4 rounded-xl bg-rr-midnight border border-rr-border text-center flex-shrink-0 min-w-[160px]">
              <div className="text-[10px] font-mono text-rr-muted uppercase">JAIPUR PAR DEFENSE</div>
              <div className="text-3xl font-extrabold text-rr-gold font-display mt-0.5">172.4</div>
              <div className="text-[11px] text-emerald-400 mt-1">Rewarding High-Dot Spinners</div>
            </div>
          </div>
        </div>

        {/* 3 Core Tactical Priorities */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          {/* Priority 1 */}
          <div className="p-6 rounded-2xl bg-rr-panel border border-rr-pink/40 shadow-xl flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-rr-pink/20 border border-rr-pink/40 flex items-center justify-center text-rr-pink mb-4">
                <Target className="w-5 h-5" />
              </div>
              <div className="text-xs font-mono text-rr-pink font-bold uppercase mb-1">
                PRIORITY 01
              </div>
              <h4 className="text-lg font-bold text-white mb-2">
                Domestic Finishing Firepower
              </h4>
              <p className="text-xs text-rr-muted leading-relaxed mb-4">
                RR has historically suffered when early wickets fell and required run rates exceeded 12.0 RPO. 
                Targeting <b>Naman Dhir</b> (Rank 3) and <b>Shashank Singh</b> (Rank 5) gives RR clutch finishers 
                averaging over 40 with strike rates &gt;180 under fire, protecting top-order stars like Yashasvi Jaiswal and Sanju Samson.
              </p>
            </div>
            <div className="p-3 rounded-xl bg-rr-midnight border border-rr-border text-xs">
              <span className="text-rr-gold font-bold">Target Bid Allocation:</span> 4.0 - 7.5 Cr
            </div>
          </div>

          {/* Priority 2 */}
          <div className="p-6 rounded-2xl bg-rr-panel border border-rr-gold/40 shadow-xl flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-rr-gold/20 border border-rr-gold/40 flex items-center justify-center text-rr-gold mb-4">
                <Shield className="w-5 h-5" />
              </div>
              <div className="text-xs font-mono text-rr-gold font-bold uppercase mb-1">
                PRIORITY 02
              </div>
              <h4 className="text-lg font-bold text-white mb-2">
                The SMS Jaipur Spin Chokehold
              </h4>
              <p className="text-xs text-rr-muted leading-relaxed mb-4">
                As Ravichandran Ashwin and Yuzvendra Chahal reach veteran transition phases, RR requires next-generation spin containment. 
                <b>Sunil Narine</b> (Rank 3 Bowler, 6.37 economy, 40.2% dots) and <b>Mitchell Santner</b> (Rank 5, 6.83 economy, zero loose balls) 
                provide pinpoint control that forces mistimed aerial shots into Jaipur’s expansive outfield.
              </p>
            </div>
            <div className="p-3 rounded-xl bg-rr-midnight border border-rr-border text-xs">
              <span className="text-rr-gold font-bold">Target Bid Allocation:</span> 2.5 - 5.0 Cr (High Value)
            </div>
          </div>

          {/* Priority 3 */}
          <div className="p-6 rounded-2xl bg-rr-panel border border-rr-borderLight shadow-xl flex flex-col justify-between">
            <div>
              <div className="w-10 h-10 rounded-xl bg-rr-midnight border border-rr-border flex items-center justify-center text-rr-white mb-4">
                <Landmark className="w-5 h-5" />
              </div>
              <div className="text-xs font-mono text-rr-white font-bold uppercase mb-1">
                PRIORITY 03
              </div>
              <h4 className="text-lg font-bold text-white mb-2">
                Express Hostility & Angles
              </h4>
              <p className="text-xs text-rr-muted leading-relaxed mb-4">
                <b>Spencer Johnson</b> (Rank 9) and <b>Mark Wood</b> (Rank 10) generate 145–150 km/h raw velocity 
                and acute left-arm trajectory. They eliminate lower-order resistance and prevent batters from premeditating 
                scoop and ramp boundaries in overs 18–20.
              </p>
            </div>
            <div className="p-3 rounded-xl bg-rr-midnight border border-rr-border text-xs">
              <span className="text-rr-gold font-bold">Target Bid Allocation:</span> 6.0 - 9.0 Cr
            </div>
          </div>
        </div>

        {/* Hypothetical Playing XI Blueprint */}
        <div className="p-6 rounded-2xl bg-rr-panel border border-rr-border">
          <div className="flex items-center justify-between mb-4 pb-3 border-b border-rr-border">
            <h4 className="text-sm font-bold text-white flex items-center gap-2 font-display">
              <CheckCircle className="w-4 h-4 text-emerald-400" />
              <span>Rajasthan Royals Pressure-Hardened Playing XI Template</span>
            </h4>
            <span className="text-xs font-mono text-rr-muted">IPL 2027 Simulation</span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2 text-xs">
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">01. POWER OPENER</div>
              <div className="font-bold text-white mt-0.5">Yashasvi Jaiswal</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">02. CLUTCH OPENER</div>
              <div className="font-bold text-rr-pink mt-0.5">Jos Buttler / Salt</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">03. ANCHOR / CAPT</div>
              <div className="font-bold text-white mt-0.5">Sanju Samson</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">04. SPIN DESTROYER</div>
              <div className="font-bold text-rr-gold mt-0.5">Rajat Patidar</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">05. DYNAMIC HITTER</div>
              <div className="font-bold text-rr-pink mt-0.5">Naman Dhir</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">06. ICE FINISHER</div>
              <div className="font-bold text-rr-pink mt-0.5">Shashank Singh</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">07. FINISHER (OS #2)</div>
              <div className="font-bold text-emerald-400 mt-0.5">Shimron Hetmyer / Tim David</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">08. SPIN CHOKE (OS #3)</div>
              <div className="font-bold text-rr-gold mt-0.5">Mitchell Santner / Narine</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">09. CONTROL SEAM (IND)</div>
              <div className="font-bold text-white mt-0.5">Sandeep Sharma</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center">
              <div className="text-[10px] text-rr-muted font-mono">10. 150+ EXPRESS (IND)</div>
              <div className="font-bold text-sky-400 mt-0.5">Umran Malik</div>
            </div>
            <div className="p-2.5 rounded-lg bg-rr-midnight border border-rr-border text-center col-span-2">
              <div className="text-[10px] text-rr-muted font-mono">11. DEATH CLOSER (OS #4)</div>
              <div className="font-bold text-rr-gold mt-0.5">Hasan Mahmud / Pathirana</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
