'use client';

import React, { useState } from 'react';
import { Sliders, Calculator, Info } from 'lucide-react';

export default function MethodologyOverview() {
  const [rrr, setRrr] = useState(11.5);
  const [ballsRemaining, setBallsRemaining] = useState(24);
  const [wicketsInHand, setWicketsInHand] = useState(4);
  const [isKnockout, setIsKnockout] = useState(true);

  // Compute live PI
  const rrrFactor = (rrr - 6.0) / 6.0;
  const stageFactor = 1.0 + (120 - ballsRemaining) / 120.0;
  const wktFactor = 1.0 + (10 - wicketsInHand) * 0.1;
  const knockoutMult = isKnockout ? 1.25 : 1.0;

  const rawPI = (2.5 + 3.0 * rrrFactor) * stageFactor * (wktFactor / 1.2) * knockoutMult;
  const livePI = Math.min(10.0, Math.max(1.0, rawPI)).toFixed(1);

  const getTier = (val: number) => {
    if (val < 4.0) return { name: 'Low Pressure Tier', color: 'text-emerald-700', bg: 'bg-emerald-50', border: 'border-emerald-200' };
    if (val < 6.5) return { name: 'Moderate Pressure Tier', color: 'text-sky-700', bg: 'bg-sky-50', border: 'border-sky-200' };
    if (val < 8.5) return { name: 'High Pressure Tier', color: 'text-amber-800', bg: 'bg-amber-50', border: 'border-amber-200' };
    return { name: 'Extreme Pressure Crucible', color: 'text-[#EA1D76]', bg: 'bg-pink-50', border: 'border-pink-200' };
  };

  const currentTier = getTier(parseFloat(livePI));

  return (
    <section id="pressure-index" className="py-28 border-b border-[#E5E7EB] bg-[#F5F4F7]">
      <div className="max-w-[1440px] mx-auto px-6 lg:px-12">
        
        {/* Section Eyebrow & Rule */}
        <div className="w-full h-px bg-[#E5E7EB] mb-12" />
        <div className="flex items-center gap-3 mb-5">
          <span className="w-6 h-px bg-[#EA1D76]" />
          <span className="text-[11px] font-mono font-semibold tracking-[0.18em] uppercase text-[#EA1D76]">
            CHAPTER 02 / PRESSURE INTELLIGENCE
          </span>
        </div>

        {/* Section Header */}
        <div className="grid lg:grid-cols-12 gap-8 items-end mb-16">
          <div className="lg:col-span-8">
            <h2
              className="font-serif font-normal text-[#10152B] tracking-tight"
              style={{ fontSize: 'clamp(2.25rem, 4.5vw, 3.75rem)', lineHeight: '1.1' }}
            >
              The Situational Leverage Index (SLI)
            </h2>
          </div>
          <div className="lg:col-span-4">
            <p className="text-sm text-[#4B5563] leading-relaxed">
              Pressure is not a subjective label applied to death overs. It is an instantaneous rate of change of win probability computed ball-by-ball.
            </p>
          </div>
        </div>

        {/* 2-Column Clean Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-start">
          
          {/* Left Column: The 4 Mathematical Levers */}
          <div className="lg:col-span-7 space-y-4">
            <div className="text-xs font-mono font-semibold uppercase tracking-wider text-[#6B7280] mb-2">
              THE FOUR PRESSURE MULTIPLIERS
            </div>

            <div className="bg-white border border-[#E5E7EB] p-5 rounded-[2px]">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-serif text-base text-[#10152B] font-medium">1. Run Rate Differential (ΔRR)</span>
                <span className="text-xs font-mono text-[#EA1D76] font-semibold">Weight: 35%</span>
              </div>
              <p className="text-xs text-[#6B7280] leading-relaxed">
                In 2nd innings chases, calculates instantaneous Required Run Rate minus Baseline Run Rate. Every +1.5 RRR deviation above par score exponentially compounds batting stress.
              </p>
            </div>

            <div className="bg-white border border-[#E5E7EB] p-5 rounded-[2px]">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-serif text-base text-[#10152B] font-medium">2. Resource Depletion Ratio (Wickets in Hand)</span>
                <span className="text-xs font-mono text-[#EA1D76] font-semibold">Weight: 30%</span>
              </div>
              <p className="text-xs text-[#6B7280] leading-relaxed">
                Scales inversely with remaining wickets. 40/4 in over 5.2 triggers acute early-innings crisis index equal to death-overs chases, isolating genuine crisis anchors.
              </p>
            </div>

            <div className="bg-white border border-[#E5E7EB] p-5 rounded-[2px]">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-serif text-base text-[#10152B] font-medium">3. Phase Progression Decay (120 - Balls Remaining)</span>
                <span className="text-xs font-mono text-[#EA1D76] font-semibold">Weight: 20%</span>
              </div>
              <p className="text-xs text-[#6B7280] leading-relaxed">
                Error margin vanishes as balls decay towards zero. Overs 17–20 inherently carry base multiplier 1.7× to 2.0× as each dot ball causes severe win probability drops.
              </p>
            </div>

            <div className="bg-white border border-[#E5E7EB] p-5 rounded-[2px]">
              <div className="flex items-center justify-between mb-1.5">
                <span className="font-serif text-base text-[#10152B] font-medium">4. Tournament Stakes Multiplier</span>
                <span className="text-xs font-mono text-[#D6B36A] font-semibold">Scale: 1.00× – 1.25×</span>
              </div>
              <p className="text-xs text-[#6B7280] leading-relaxed">
                IPL Playoffs, Qualifiers, Finals, and World Cup knockouts receive a 1.25× scalar multiplier. Bilateral series receive standard baseline weighting.
              </p>
            </div>
          </div>

          {/* Right Column: Live Interactive SLI Calculator */}
          <div className="lg:col-span-5 bg-white border border-[#E5E7EB] p-7 rounded-[2px] shadow-sm">
            <div className="flex items-center justify-between mb-6 pb-4 border-b border-[#E5E7EB]">
              <div className="flex items-center gap-2">
                <Calculator size={15} className="text-[#EA1D76]" />
                <span className="text-xs font-mono font-semibold uppercase tracking-wider text-[#10152B]">
                  LIVE SITUATIONAL LEVERAGE CALCULATOR
                </span>
              </div>
              <span className="text-[10px] font-mono text-[#6B7280]">Interactive Simulator</span>
            </div>

            {/* Calculated Output Display */}
            <div className={`p-5 rounded-[2px] border ${currentTier.border} ${currentTier.bg} mb-6 flex items-center justify-between`}>
              <div>
                <div className="text-[10px] font-mono uppercase tracking-wider text-[#6B7280]">
                  COMPUTED PRESSURE INDEX (1.0 – 10.0)
                </div>
                <div className={`font-serif text-4xl font-normal mt-1 ${currentTier.color}`}>
                  {livePI} <span className="text-sm font-sans text-[#6B7280]">/ 10.0</span>
                </div>
              </div>
              <div className="text-right">
                <span className={`inline-block px-2.5 py-1 text-xs font-mono font-semibold rounded-[2px] bg-white border ${currentTier.border} ${currentTier.color}`}>
                  {currentTier.name}
                </span>
                <div className="text-[10px] font-mono text-[#6B7280] mt-1">
                  {parseFloat(livePI) >= 6.5 ? 'Qualifies as High-Pressure Event' : 'Filtered into Baseline Benchmark'}
                </div>
              </div>
            </div>

            {/* Slider Controls */}
            <div className="space-y-5 text-xs">
              <div>
                <div className="flex justify-between font-mono text-[#4B5563] mb-1.5">
                  <span>Required Run Rate (RRR)</span>
                  <span className="font-bold text-[#10152B]">{rrr.toFixed(1)} RPO</span>
                </div>
                <input
                  type="range"
                  min="6.0"
                  max="18.0"
                  step="0.5"
                  value={rrr}
                  onChange={(e) => setRrr(parseFloat(e.target.value))}
                  className="w-full accent-[#EA1D76] cursor-pointer"
                />
              </div>

              <div>
                <div className="flex justify-between font-mono text-[#4B5563] mb-1.5">
                  <span>Balls Remaining</span>
                  <span className="font-bold text-[#10152B]">{ballsRemaining} Balls</span>
                </div>
                <input
                  type="range"
                  min="6"
                  max="60"
                  step="6"
                  value={ballsRemaining}
                  onChange={(e) => setBallsRemaining(parseInt(e.target.value))}
                  className="w-full accent-[#EA1D76] cursor-pointer"
                />
              </div>

              <div>
                <div className="flex justify-between font-mono text-[#4B5563] mb-1.5">
                  <span>Wickets in Hand</span>
                  <span className="font-bold text-[#10152B]">{wicketsInHand} Wickets</span>
                </div>
                <input
                  type="range"
                  min="1"
                  max="8"
                  step="1"
                  value={wicketsInHand}
                  onChange={(e) => setWicketsInHand(parseInt(e.target.value))}
                  className="w-full accent-[#EA1D76] cursor-pointer"
                />
              </div>

              <div className="pt-2 flex items-center justify-between border-t border-[#E5E7EB]">
                <span className="font-mono text-[#4B5563]">Knockout / Playoff Multiplier</span>
                <button
                  onClick={() => setIsKnockout(!isKnockout)}
                  className={`px-3 py-1 font-mono text-xs font-semibold rounded-[2px] transition-colors ${
                    isKnockout ? 'bg-[#10152B] text-white' : 'bg-[#E5E7EB] text-[#4B5563]'
                  }`}
                >
                  {isKnockout ? '1.25× ACTIVE' : '1.00× REGULAR'}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
