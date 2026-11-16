'use client';

import React, { useState } from 'react';
import { Award, Shield, CheckCircle2, TrendingUp, Users, Target, ChevronRight, Crown } from 'lucide-react';

interface LeadershipData {
  incumbentCaptain: {
    name: string;
    role: string;
    contractStatus: string;
    tenure: string;
    matchesCaptained: number;
    matchesWon: number;
    winPercentage: number;
    chaseWinPct: number;
    defendWinPct: number;
    playoffAppearances: string;
    tacticalProfile: string;
    brsScore: number;
    recommendationStatus: string;
  };
  alternativeCandidates: Array<{
    name: string;
    role: string;
    previousExperience: string;
    leadershipTemperament: string;
    availability: string;
    suitabilityRating: number;
  }>;
  successionRoadmap: {
    cycle2027_2028: string;
    cycle2029_2030: string;
  };
}

interface LeadershipProps {
  data?: LeadershipData;
}

export default function LeadershipStrategySection({ data }: LeadershipProps) {
  const [activeTab, setActiveTab] = useState<'samson' | 'alternatives' | 'succession'>('samson');

  const defaultData: LeadershipData = {
    incumbentCaptain: {
      name: 'Sanju Samson',
      role: 'Captain & Wicketkeeper-Batter',
      contractStatus: 'Retained Core (₹18.00 Cr)',
      tenure: '2021–Present (5 Seasons)',
      matchesCaptained: 53,
      matchesWon: 28,
      winPercentage: 52.8,
      chaseWinPct: 53.8,
      defendWinPct: 51.9,
      playoffAppearances: '2022 (IPL Finalists), 2024 (Qualifier 2)',
      tacticalProfile: 'Calm, unflappable demeanor under extreme situational leverage. Exceptional wicketkeeping perspective provides real-time field angle adjustments and bowler encouragement without emotional volatility.',
      brsScore: 68.2,
      recommendationStatus: 'CONFIRMED PREFERRED CAPTAIN (Continuity Advantage)'
    },
    alternativeCandidates: [
      {
        name: 'Jos Buttler',
        role: 'Vice-Captain / Senior Leader',
        previousExperience: 'England National T20 Captain (2022 T20 World Cup Champions)',
        leadershipTemperament: 'Aggressive tactical mindset; exceptional white-ball pedigree',
        availability: 'Auction Target Candidate (Requires Acquisition Bid)',
        suitabilityRating: 91.5
      },
      {
        name: 'Riyan Parag',
        role: 'Emerging Vice-Captain / Domestic Succession',
        previousExperience: 'Assam State Captain (Record-breaking domestic run-scorer & captain)',
        leadershipTemperament: 'Proactive communicator; exceptional tactical growth in 2024–2026 cycle',
        availability: 'Retained Core (₹14.00 Cr)',
        suitabilityRating: 88.0
      },
      {
        name: 'Mitchell Santner',
        role: 'Senior Bowling Tactician',
        previousExperience: 'New Zealand T20I Captain',
        leadershipTemperament: 'Understated, analytical field strategist; expert in spin chokeholds',
        availability: 'Auction Target Candidate (NZC NOC Cleared)',
        suitabilityRating: 86.5
      }
    ],
    successionRoadmap: {
      cycle2027_2028: 'Sanju Samson continues as undisputed franchise captain, supported by Riyan Parag as designated Vice-Captain and Jos Buttler / Mitchell Santner as senior on-field advisors.',
      cycle2029_2030: 'Structured leadership transition to Riyan Parag or Yashasvi Jaiswal following a 2-year leadership mentorship program.'
    }
  };

  const lData = data || defaultData;
  const inc = lData.incumbentCaptain;

  return (
    <section id="leadership" className="py-24 border-t border-rr-border bg-rr-offwhite text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 09 / CAPTAINCY & LEADERSHIP STRATEGY
          </span>
        </div>

        {/* Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              ON-FIELD COMMAND & <br />
              <span className="text-rr-pink">TACTICAL LEADERSHIP INTEL</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Evaluating captaincy suitability through empirical match decision telemetry across 883 fixtures. 
            Leadership cannot be inferred from batting averages or popularity; it demands composure under high leverage.
          </p>
        </div>

        {/* Tab Controls */}
        <div className="flex items-center gap-2 mb-8">
          <button
            onClick={() => setActiveTab('samson')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'samson'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            01. Incumbent Captain Audit (Sanju Samson)
          </button>
          <button
            onClick={() => setActiveTab('alternatives')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'alternatives'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            02. Leadership Candidates & Vice-Captaincy
          </button>
          <button
            onClick={() => setActiveTab('succession')}
            className={`px-4 py-2 rounded-[2px] text-xs font-mono font-bold transition-all border ${
              activeTab === 'succession'
                ? 'bg-rr-navy text-white border-rr-navy'
                : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
            }`}
          >
            03. 2027–2030 Succession Roadmap
          </button>
        </div>

        {/* TAB 1: SANJU SAMSON EMPIRICAL AUDIT */}
        {activeTab === 'samson' && (
          <div className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
              {/* Left Column: Captain Dossier */}
              <div className="lg:col-span-5 p-6 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-5">
                <div className="flex items-center justify-between pb-3 border-b border-rr-border">
                  <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-pink-50 text-rr-pink border border-pink-200 uppercase">
                    {inc.recommendationStatus}
                  </span>
                  <span className="text-xs font-mono text-slate-500 font-bold">{inc.tenure}</span>
                </div>

                <div>
                  <h3 className="text-2xl sm:text-3xl font-extrabold text-rr-navy font-display">
                    {inc.name}
                  </h3>
                  <div className="text-xs font-mono text-slate-500 mt-0.5">{inc.role} · {inc.contractStatus}</div>
                </div>

                {/* Empirical Stats Grid */}
                <div className="grid grid-cols-2 gap-3 text-center font-mono">
                  <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                    <div className="text-[10px] text-slate-500 uppercase">Matches Captained</div>
                    <div className="text-2xl font-black text-rr-navy mt-1">{inc.matchesCaptained}</div>
                    <div className="text-[9px] text-emerald-700 font-bold">{inc.matchesWon} Victories</div>
                  </div>
                  <div className="p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                    <div className="text-[10px] text-slate-500 uppercase">Overall Win %</div>
                    <div className="text-2xl font-black text-rr-pink mt-1">{inc.winPercentage}%</div>
                    <div className="text-[9px] text-slate-400">Playoffs: {inc.playoffAppearances}</div>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-3 text-center font-mono text-xs">
                  <div className="p-2.5 bg-rr-offwhite border border-rr-border rounded-[2px]">
                    <div className="text-[9px] text-slate-500 uppercase">Win % Chasing</div>
                    <div className="text-base font-bold text-rr-navy mt-0.5">{inc.chaseWinPct}%</div>
                  </div>
                  <div className="p-2.5 bg-rr-offwhite border border-rr-border rounded-[2px]">
                    <div className="text-[9px] text-slate-500 uppercase">Win % Defending</div>
                    <div className="text-base font-bold text-rr-navy mt-0.5">{inc.defendWinPct}%</div>
                  </div>
                </div>

                <div className="p-4 bg-rr-offwhite border border-rr-border rounded-[2px] text-xs leading-relaxed text-slate-600">
                  <span className="font-bold text-rr-navy block mb-1 uppercase font-mono text-[10px]">Wicketkeeper Advantage:</span>
                  {inc.tacticalProfile}
                </div>
              </div>

              {/* Right Column: Tactical Composure Breakdown */}
              <div className="lg:col-span-7 space-y-4">
                <div className="p-6 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-4">
                  <h4 className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider">
                    Four Cornerstones of Samson Captaincy Model:
                  </h4>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs font-mono">
                    <div className="p-3.5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                      <div className="text-rr-pink font-bold uppercase text-[11px]">1. Dressing Room Trust</div>
                      <p className="text-slate-600 font-sans leading-relaxed">
                        Unanimous player loyalty across senior international stars and domestic youngsters. Five-year tenure provides stability.
                      </p>
                    </div>
                    <div className="p-3.5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                      <div className="text-rr-navy font-bold uppercase text-[11px]">2. Crucible Composure</div>
                      <p className="text-slate-600 font-sans leading-relaxed">
                        Refrains from reactive bowling changes when opposition scores 20+ in an over, trusting predetermined matchup plans.
                      </p>
                    </div>
                    <div className="p-3.5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                      <div className="text-rr-navy font-bold uppercase text-[11px]">3. SMS Jaipur Synergy</div>
                      <p className="text-slate-600 font-sans leading-relaxed">
                        Intimate knowledge of Sawai Mansingh Stadium pitch conditions and boundary dimensions; excels at squeezing targets of 170.
                      </p>
                    </div>
                    <div className="p-3.5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-1">
                      <div className="text-emerald-700 font-bold uppercase text-[11px]">4. Batting Under Captaincy</div>
                      <p className="text-slate-600 font-sans leading-relaxed">
                        Performance does not suffer under captaincy burden (BRS 68.2). Consistently averages &gt;35 with strike rate &gt;145 as captain.
                      </p>
                    </div>
                  </div>
                </div>

                <div className="p-5 bg-white border-l-4 border-l-rr-pink border border-rr-border rounded-[2px] shadow-sm flex items-start gap-3 text-xs">
                  <Crown className="w-5 h-5 text-rr-pink shrink-0 mt-0.5" />
                  <div>
                    <div className="font-mono font-bold text-rr-navy uppercase text-[11px]">Franchise Strategy Verdict:</div>
                    <p className="text-slate-600 mt-0.5 leading-relaxed font-normal">
                      Continuity is Rajasthan Royals greatest competitive asset. Replacing Sanju Samson would disrupt squad chemistry 
                      without providing any empirical win-rate upside. Samson remains the cornerstone on-field commander for IPL 2027.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB 2: LEADERSHIP CANDIDATES & VICE-CAPTAINCY */}
        {activeTab === 'alternatives' && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {lData.alternativeCandidates.map((c) => (
              <div
                key={c.name}
                className="p-6 bg-white border border-rr-border rounded-[2px] shadow-sm flex flex-col justify-between space-y-4"
              >
                <div>
                  <div className="flex items-center justify-between pb-3 border-b border-rr-border">
                    <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-rr-offwhite text-rr-navy border border-rr-border uppercase">
                      {c.role}
                    </span>
                    <span className="text-xs font-mono text-rr-pink font-bold">{c.suitabilityRating}% Fit</span>
                  </div>

                  <h3 className="text-xl font-extrabold text-rr-navy font-display mt-3">
                    {c.name}
                  </h3>
                  <div className="text-xs font-mono text-slate-500 mt-0.5">{c.availability}</div>

                  <div className="mt-4 p-3 bg-rr-offwhite border border-rr-border rounded-[2px] text-xs font-mono space-y-1">
                    <div className="text-slate-500 text-[10px] uppercase">Leadership Track Record:</div>
                    <div className="text-slate-700 font-sans leading-relaxed">{c.previousExperience}</div>
                  </div>

                  <div className="mt-3 text-xs text-slate-600 leading-relaxed font-normal">
                    <span className="font-bold text-rr-navy uppercase font-mono text-[10px] block mb-0.5">Temperament Profile:</span>
                    {c.leadershipTemperament}
                  </div>
                </div>

                <div className="p-2.5 bg-rr-offwhite border border-rr-border rounded-[2px] text-center font-mono text-xs font-bold text-rr-navy">
                  Designated Advisory Role
                </div>
              </div>
            ))}
          </div>
        )}

        {/* TAB 3: SUCCESSION ROADMAP */}
        {activeTab === 'succession' && (
          <div className="p-6 sm:p-8 bg-white border border-rr-border rounded-[2px] shadow-sm space-y-6">
            <h3 className="text-xl font-bold text-rr-navy font-display uppercase">
              Rajasthan Royals Leadership Succession Framework (2027–2030)
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-xs font-mono">
              <div className="p-5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-rr-pink font-bold uppercase text-[11px]">Phase I: 2027–2028 Cycle (Continuity & Grooming)</span>
                <p className="text-slate-600 font-sans leading-relaxed">
                  {lData.successionRoadmap.cycle2027_2028}
                </p>
                <div className="pt-2 text-[10px] text-slate-400">
                  Deliverable: Empowers Riyan Parag with tactical match planning and bowling change decisions.
                </div>
              </div>

              <div className="p-5 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2">
                <span className="text-rr-navy font-bold uppercase text-[11px]">Phase II: 2029–2030 Cycle (Generational Transition)</span>
                <p className="text-slate-600 font-sans leading-relaxed">
                  {lData.successionRoadmap.cycle2029_2030}
                </p>
                <div className="pt-2 text-[10px] text-slate-400">
                  Deliverable: Seamless franchise transition avoiding the leadership voids seen in rival franchises.
                </div>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}