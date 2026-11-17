'use client';

import React, { useState } from 'react';
import { Award, Zap, TrendingUp, Shield, ChevronDown, ChevronUp, User, Target, BarChart2, X, CheckCircle2, ArrowRight } from 'lucide-react';

interface BowlerData {
  rank: number;
  playerId: number;
  name: string;
  team: string;
  pool: 'IPL_VERIFIED' | 'IPL_PARTIAL' | 'INTERNATIONAL' | 'EMERGING';
  poolLabel: string;
  nationality?: string;
  cricketBoard?: string;
  isAuctionEligible?: boolean;
  auctionAvailabilityStatus?: string;
  auctionStatusCode?: string;
  currentFranchise?: string;
  contractDetails?: string;
  isRRAcquisitionTarget?: boolean;
  isRetained?: boolean;
  retainedFranchise?: string;
  alternateTarget?: string;
  alternateReason?: string;
  availabilityReason?: string;
  auctionOpportunityScore?: number;
  squadRoleFit?: string;
  acquisitionPriority?: string;
  estimatedPriceRange?: string;
  archetype: string;
  rrTacticalFit: string;
  brsScore: number;
  pressRawBalls: number;
  pressRawRuns: number;
  pressWickets: number;
  pressEcon: number;
  baseEcon: number;
  deltaEcon: number;
  dotPct: number;
  boundaryPct: number;
  matches: number;
  iplBalls: number;
  tier1Balls: number;
  radar: {
    runSuppression: number;
    dotPercentage: number;
    boundaryControl: number;
    wicketThreat: number;
    clutchLift: number;
    sampleConfidence: number;
  };
  phaseSplits: any;
  inningsSplits: any;
  dna?: {
    topDeliveryStyles: Array<{ style: string; count: number; pct: number }>;
    rhbVsLhb: {
      RHB: { balls: number; runs: number; wkts: number; econ: number; dotPct: number };
      LHB: { balls: number; runs: number; wkts: number; econ: number; dotPct: number };
    };
    phaseBreakdown: Record<string, { balls: number; runs: number; wkts: number; econ: number; dotPct: number }>;
    dotRateOverall: number;
    genomePersona: string;
  };
}

interface TopBowlersSectionProps {
  bowlers: BowlerData[];
}

export default function TopBowlersSection({ bowlers }: TopBowlersSectionProps) {
  const [selectedPlayer, setSelectedPlayer] = useState<BowlerData | null>(null);
  const [activeTab, setActiveTab] = useState<'all' | 'available' | 'retained'>('all');

  const filteredBowlers = bowlers.filter(bw => {
    if (activeTab === 'available') return bw.isRRAcquisitionTarget === true;
    if (activeTab === 'retained') return bw.isRRAcquisitionTarget === false;
    return true;
  });

  return (
    <section id="bowlers" className="py-16 sm:py-28 border-b border-[#E5E7EB] bg-[#F5F4F7]">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-12">
        
        {/* Eyebrow */}
        <div className="flex items-center gap-3 mb-5">
          <span className="w-6 h-px bg-[#EA1D76]" />
          <span className="text-[10px] sm:text-[11px] font-mono font-semibold tracking-[0.18em] uppercase text-[#EA1D76]">
            CHAPTER 04 / STATISTICAL PERFORMANCE RANKINGS
          </span>
        </div>

        {/* Section Heading & Subtitle */}
        <div className="grid lg:grid-cols-12 gap-6 lg:gap-8 items-end mb-10 sm:mb-12">
          <div className="lg:col-span-8">
            <h2
              className="font-serif font-normal text-[#10152B] tracking-tight"
              style={{ fontSize: 'clamp(1.75rem, 4vw, 3.75rem)', lineHeight: '1.1' }}
            >
              Top 10 Most Reliable Bowlers
            </h2>
          </div>
          <div className="lg:col-span-4">
            <p className="text-xs sm:text-sm text-[#4B5563] leading-relaxed">
              Empirical Bayesian containment and wicket-taking models under high leverage (SLI ≥ 6.5). Statistical performance is separated from verified mini-auction availability.
            </p>
          </div>
        </div>

        {/* Filter Navigation Tabs (EterPay Reference) */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6 pb-4 border-b border-[#E5E7EB]">
          <div className="flex flex-wrap items-center border border-[#E5E7EB] rounded-[2px] bg-white p-1 gap-1">
            <button
              onClick={() => setActiveTab('all')}
              className={`px-3 sm:px-4 py-1.5 text-xs font-mono font-semibold uppercase tracking-wider rounded-[2px] transition-colors ${
                activeTab === 'all'
                  ? 'bg-[#10152B] text-white shadow-sm'
                  : 'text-[#6B7280] hover:text-[#10152B]'
              }`}
            >
              All Top 10 Bowlers
            </button>
            <button
              onClick={() => setActiveTab('available')}
              className={`px-3 sm:px-4 py-1.5 text-xs font-mono font-semibold uppercase tracking-wider rounded-[2px] transition-colors ${
                activeTab === 'available'
                  ? 'bg-[#EA1D76] text-white shadow-sm'
                  : 'text-[#6B7280] hover:text-[#10152B]'
              }`}
            >
              RR Targets ({bowlers.filter(b => b.isRRAcquisitionTarget).length})
            </button>
            <button
              onClick={() => setActiveTab('retained')}
              className={`px-3 sm:px-4 py-1.5 text-xs font-mono font-semibold uppercase tracking-wider rounded-[2px] transition-colors ${
                activeTab === 'retained'
                  ? 'bg-[#10152B] text-white shadow-sm'
                  : 'text-[#6B7280] hover:text-[#10152B]'
              }`}
            >
              Retained ({bowlers.filter(b => !b.isRRAcquisitionTarget).length})
            </button>
          </div>

          <div className="text-xs font-mono text-[#6B7280]">
            Showing <strong className="text-[#10152B]">{filteredBowlers.length}</strong> qualified bowlers
          </div>
        </div>

        {/* Mobile Horizontal Scroll Indicator */}
        <div className="sm:hidden text-[10px] font-mono text-[#6B7280] mb-2 flex items-center justify-between">
          <span>← Scroll table horizontally →</span>
          <span className="text-[#EA1D76]">Tap row for DNA dossier</span>
        </div>

        {/* ── Professional Data Table (Clean White Table on Off-White Surface) ─ */}
        <div className="overflow-x-auto border border-[#E5E7EB] rounded-[2px] bg-white -mx-4 sm:mx-0">
          <table className="w-full text-left border-collapse min-w-[700px]">
            <thead>
              <tr className="bg-[#F9FAFB] border-b border-[#E5E7EB] text-[11px] font-mono uppercase tracking-wider text-[#6B7280]">
                <th className="py-3.5 px-4 font-semibold w-14">Rank</th>
                <th className="py-3.5 px-4 font-semibold">Bowler & Profile</th>
                <th className="py-3.5 px-4 font-semibold">Nationality & Board</th>
                <th className="py-3.5 px-4 font-semibold text-right">Pressure Econ</th>
                <th className="py-3.5 px-4 font-semibold text-right">Wickets</th>
                <th className="py-3.5 px-4 font-semibold text-right">Dot Ball %</th>
                <th className="py-3.5 px-4 font-semibold text-right">ΔEcon Lift</th>
                <th className="py-3.5 px-4 font-semibold text-right">Pressure Balls</th>
                <th className="py-3.5 px-4 font-semibold text-right">BRS Score</th>
                <th className="py-3.5 px-4 font-semibold">Auction Availability</th>
                <th className="py-3.5 px-4 font-semibold text-center w-24">Intelligence</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#E5E7EB] text-xs">
              {filteredBowlers.map((bw) => {
                const isTarget = bw.isRRAcquisitionTarget === true;
                return (
                  <tr
                    key={bw.playerId}
                    className="hover:bg-[#F9FAFB] transition-colors group cursor-pointer"
                    onClick={() => setSelectedPlayer(bw)}
                  >
                    <td className="py-4 px-4 font-mono font-bold text-[#10152B]">
                      #{bw.rank}
                    </td>

                    <td className="py-4 px-4">
                      <div className="font-serif text-sm font-bold text-[#10152B] group-hover:text-[#EA1D76] transition-colors">
                        {bw.name}
                      </div>
                      <div className="text-[11px] text-[#6B7280]">
                        {bw.archetype}
                      </div>
                    </td>

                    <td className="py-4 px-4 text-[11px] font-mono text-[#4B5563]">
                      <div>{bw.nationality}</div>
                      <div className="text-[10px] text-[#9CA3AF]">{bw.cricketBoard}</div>
                    </td>

                    <td className="py-4 px-4 text-right font-mono font-bold text-[#10152B]">
                      {bw.pressEcon.toFixed(2)}
                    </td>

                    <td className="py-4 px-4 text-right font-mono text-[#4B5563]">
                      {bw.pressWickets}
                    </td>

                    <td className="py-4 px-4 text-right font-mono text-[#10152B]">
                      {bw.dotPct.toFixed(1)}%
                    </td>

                    <td className="py-4 px-4 text-right font-mono">
                      <span className={bw.deltaEcon >= 0 ? 'text-emerald-700 font-semibold' : 'text-rose-700'}>
                        {bw.deltaEcon >= 0 ? `-${bw.deltaEcon.toFixed(2)}` : `+${Math.abs(bw.deltaEcon).toFixed(2)}`}
                      </span>
                    </td>

                    <td className="py-4 px-4 text-right font-mono text-[#6B7280]">
                      {bw.pressRawBalls} <span className="text-[10px] text-[#9CA3AF]">({bw.iplBalls}b IPL)</span>
                    </td>

                    <td className="py-4 px-4 text-right">
                      <span className="font-serif font-bold text-sm text-[#EA1D76]">
                        {bw.brsScore.toFixed(1)}
                      </span>
                    </td>

                    <td className="py-4 px-4">
                      {isTarget ? (
                        <div className="space-y-1">
                          <div className="flex items-center gap-1.5">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                            <span className="text-[11px] font-mono font-semibold text-emerald-800">
                              Available · AOS {bw.auctionOpportunityScore?.toFixed(0)}
                            </span>
                          </div>
                          <span className="inline-block px-1.5 py-0.5 rounded-[2px] bg-emerald-50 border border-emerald-200 text-[9.5px] font-mono text-emerald-700">
                            RR Auction Target
                          </span>
                        </div>
                      ) : (
                        <div className="space-y-1">
                          <div className="flex items-center gap-1.5">
                            <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
                            <span className="text-[11px] font-mono font-semibold text-amber-900">
                              Retained ({bw.retainedFranchise || bw.currentFranchise || 'Franchise'})
                            </span>
                          </div>
                          {bw.alternateTarget && (
                            <div className="flex items-center gap-1 text-[10px] font-mono text-[#EA1D76]">
                              <span>Alt:</span>
                              <strong className="underline underline-offset-2">{bw.alternateTarget}</strong>
                            </div>
                          )}
                        </div>
                      )}
                    </td>

                    <td className="py-4 px-4 text-center">
                      <button
                        onClick={(e) => { e.stopPropagation(); setSelectedPlayer(bw); }}
                        className="px-2.5 py-1 text-[11px] font-mono font-semibold rounded-[2px] border border-[#E5E7EB] hover:border-[#10152B] hover:bg-[#10152B] hover:text-white transition-colors"
                      >
                        Inspect
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {/* Table Footnote */}
        <div className="mt-4 flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs text-[#6B7280] gap-2">
          <div>*Minimum threshold: 100 pressure deliveries across ≥8 professional matches. Normalized via empirical Bayesian shrinkage (M0=60).</div>
          <div className="font-mono text-[11px] text-[#EA1D76]">Click any player row to view complete DNA profile & auction feasibility</div>
        </div>

      </div>

      {/* ── Bowler Detail Dossier Modal (Clean Structured Design) ────────── */}
      {selectedPlayer && (
        <div className="fixed inset-0 z-50 bg-[#10152B]/80 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4">
          <div className="bg-white border border-[#E5E7EB] rounded-[2px] max-w-3xl w-full max-h-[92vh] overflow-y-auto p-4 sm:p-8 shadow-2xl">
            {/* Modal Header */}
            <div className="flex items-start justify-between border-b border-[#E5E7EB] pb-4 sm:pb-5 mb-5 sm:mb-6">
              <div>
                <div className="flex flex-wrap items-center gap-1.5 sm:gap-2 mb-1.5">
                  <span className="text-[11px] sm:text-xs font-mono font-bold text-[#EA1D76]">RANK #{selectedPlayer.rank} BOWLER</span>
                  <span className="text-xs text-[#9CA3AF]">·</span>
                  <span className="text-[11px] sm:text-xs font-mono text-[#6B7280]">{selectedPlayer.nationality} ({selectedPlayer.cricketBoard})</span>
                </div>
                <h3 className="font-serif text-xl sm:text-2xl lg:text-3xl font-bold text-[#10152B]">
                  {selectedPlayer.name}
                </h3>
                <p className="text-[11px] sm:text-xs text-[#6B7280] mt-0.5">
                  {selectedPlayer.archetype} · Pool: {selectedPlayer.poolLabel}
                </p>
              </div>

              <button
                onClick={() => setSelectedPlayer(null)}
                className="p-1.5 rounded-[2px] border border-[#E5E7EB] hover:bg-[#F5F4F7] text-[#4B5563] ml-2 flex-shrink-0"
              >
                <X size={18} />
              </button>
            </div>

            {/* Core Metrics Grid */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4 p-3 sm:p-4 rounded-[2px] bg-[#F5F4F7] border border-[#E5E7EB] mb-5 sm:mb-6">
              <div>
                <div className="text-[10px] font-mono uppercase text-[#6B7280]">BRS Reliability</div>
                <div className="font-serif text-xl sm:text-2xl font-bold text-[#EA1D76]">{selectedPlayer.brsScore.toFixed(1)}</div>
              </div>
              <div>
                <div className="text-[10px] font-mono uppercase text-[#6B7280]">Pressure Econ</div>
                <div className="font-mono text-lg sm:text-xl font-bold text-[#10152B]">{selectedPlayer.pressEcon.toFixed(2)}</div>
              </div>
              <div>
                <div className="text-[10px] font-mono uppercase text-[#6B7280]">Dot Ball %</div>
                <div className="font-mono text-lg sm:text-xl font-bold text-[#10152B]">{selectedPlayer.dotPct.toFixed(1)}%</div>
              </div>
              <div>
                <div className="text-[10px] font-mono uppercase text-[#6B7280]">Wickets</div>
                <div className="font-mono text-lg sm:text-xl font-bold text-emerald-700">{selectedPlayer.pressWickets}</div>
              </div>
            </div>

            {/* Auction Availability & Franchise Status */}
            <div className={`p-3 sm:p-4 rounded-[2px] border mb-5 sm:mb-6 ${
              selectedPlayer.isRRAcquisitionTarget
                ? 'bg-emerald-50 border-emerald-200'
                : 'bg-amber-50 border-amber-200'
            }`}>
              <div className="flex flex-wrap items-center justify-between gap-1.5 mb-1.5">
                <div className="text-xs font-mono font-bold uppercase tracking-wider text-[#10152B]">
                  AUCTION AVAILABILITY & FEASIBILITY AUDIT
                </div>
                <span className={`text-xs font-mono font-semibold px-2 py-0.5 rounded-[2px] ${
                  selectedPlayer.isRRAcquisitionTarget
                    ? 'bg-emerald-100 text-emerald-800'
                    : 'bg-amber-100 text-amber-800'
                }`}>
                  {selectedPlayer.auctionAvailabilityStatus}
                </span>
              </div>
              <p className="text-xs text-[#4B5563] leading-relaxed mb-3">
                {selectedPlayer.availabilityReason}
              </p>

              {/* Designated Alternate RR Target for Retained Players */}
              {selectedPlayer.alternateTarget && (
                <div className="p-3 mb-3 rounded-[2px] bg-white border border-[#EA1D76]/40 space-y-1">
                  <div className="flex items-center gap-1.5 text-xs font-mono font-bold text-[#EA1D76]">
                    <Target size={14} />
                    <span>DESIGNATED RR ALTERNATE TARGET: {selectedPlayer.alternateTarget}</span>
                  </div>
                  <p className="text-[11px] text-[#4B5563] leading-normal">
                    {selectedPlayer.alternateReason || `Direct role-equivalent replacement for ${selectedPlayer.name} with verified auction availability.`}
                  </p>
                </div>
              )}

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 sm:gap-3 text-xs pt-2 border-t border-[#E5E7EB]/60">
                <div>
                  <span className="text-[#6B7280]">Contract Status: </span>
                  <span className="font-semibold text-[#10152B]">{selectedPlayer.contractDetails}</span>
                </div>
                <div>
                  <span className="text-[#6B7280]">Estimated Price: </span>
                  <span className="font-semibold text-[#10152B]">{selectedPlayer.estimatedPriceRange || 'N/A'}</span>
                </div>
              </div>
            </div>

            {/* RHB vs LHB Matchup Breakdown */}
            {selectedPlayer.dna?.rhbVsLhb && (
              <div className="mb-5 sm:mb-6">
                <div className="text-xs font-mono font-bold uppercase text-[#6B7280] mb-3">
                  BATTER HANDEDNESS MATCHUPS (RHB VS LHB)
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
                  <div className="p-3 sm:p-3.5 rounded-[2px] bg-[#F5F4F7] border border-[#E5E7EB]">
                    <div className="text-[10px] font-mono uppercase text-[#6B7280]">vs Right-Hand Batters (RHB)</div>
                    <div className="font-mono text-base sm:text-lg font-bold text-[#10152B] mt-1">
                      {selectedPlayer.dna.rhbVsLhb.RHB.econ.toFixed(2)} <span className="text-xs font-normal text-[#6B7280]">Econ ({selectedPlayer.dna.rhbVsLhb.RHB.dotPct}% dots)</span>
                    </div>
                    <div className="text-[10px] text-[#6B7280] mt-0.5">{selectedPlayer.dna.rhbVsLhb.RHB.wkts} wkts in {selectedPlayer.dna.rhbVsLhb.RHB.balls} balls</div>
                  </div>
                  <div className="p-3 sm:p-3.5 rounded-[2px] bg-[#F5F4F7] border border-[#E5E7EB]">
                    <div className="text-[10px] font-mono uppercase text-[#6B7280]">vs Left-Hand Batters (LHB)</div>
                    <div className="font-mono text-base sm:text-lg font-bold text-[#10152B] mt-1">
                      {selectedPlayer.dna.rhbVsLhb.LHB.econ.toFixed(2)} <span className="text-xs font-normal text-[#6B7280]">Econ ({selectedPlayer.dna.rhbVsLhb.LHB.dotPct}% dots)</span>
                    </div>
                    <div className="text-[10px] text-[#6B7280] mt-0.5">{selectedPlayer.dna.rhbVsLhb.LHB.wkts} wkts in {selectedPlayer.dna.rhbVsLhb.LHB.balls} balls</div>
                  </div>
                </div>
              </div>
            )}

            {/* Phase Breakdown */}
            {selectedPlayer.dna?.phaseBreakdown && (
              <div className="mb-5 sm:mb-6">
                <div className="text-xs font-mono font-bold uppercase text-[#6B7280] mb-3">
                  MATCH PHASE CONTAINMENT
                </div>
                <div className="grid grid-cols-3 gap-2 sm:gap-3">
                  {['Powerplay', 'Middle', 'Death'].map((phase) => {
                    const st = selectedPlayer.dna?.phaseBreakdown[phase] || { econ: 0, dotPct: 0, balls: 0, wkts: 0 };
                    return (
                      <div key={phase} className="p-2.5 sm:p-3 rounded-[2px] bg-white border border-[#E5E7EB] text-center">
                        <div className="text-[10px] font-mono text-[#6B7280] uppercase">{phase}</div>
                        <div className="font-mono text-sm sm:text-base font-bold text-[#10152B] mt-1">{st.econ > 0 ? st.econ.toFixed(2) : '-'} <span className="text-[10px] text-[#6B7280]">Econ</span></div>
                        <div className="text-[10px] text-[#6B7280]">{st.dotPct}% dots · {st.wkts}w</div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* RR Tactical Recommendation */}
            <div className="p-3 sm:p-4 rounded-[2px] bg-[#F5F4F7] border border-[#E5E7EB]">
              <div className="text-xs font-mono font-bold uppercase text-[#10152B] mb-1">
                RAJASTHAN ROYALS TACTICAL RECOMMENDATION
              </div>
              <p className="text-xs text-[#4B5563] leading-relaxed">
                {selectedPlayer.rrTacticalFit}
              </p>
            </div>

            {/* Close Button */}
            <div className="mt-5 sm:mt-6 flex justify-end">
              <button
                onClick={() => setSelectedPlayer(null)}
                className="w-full sm:w-auto px-5 py-2.5 bg-[#10152B] text-white text-xs font-mono font-semibold rounded-[2px]"
              >
                Close Dossier
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
