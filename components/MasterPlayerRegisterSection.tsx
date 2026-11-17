'use client';

import React, { useState, useMemo } from 'react';
import { Search, Filter, ShieldCheck, CheckCircle2, AlertCircle, Info, ChevronRight, X, Database } from 'lucide-react';

interface PlayerRecord {
  playerId: number;
  name: string;
  nationality: string;
  classification: string;
  role: string;
  competitions: string[];
  teamsRepresented: string[];
  highPressureDeliveries: number;
  pressureSr: number | null;
  pressureAvg: number | null;
  pressureEcon: number | null;
  dotPct: number | null;
  brsScore: number;
  confidenceLevel: string;
  dataQualityStatus: string;
  iplEligibilityStatus: string;
  auctionAvailabilityStatus: string;
  selectionCategory: string;
  selectionExplanation: string;
}

interface MasterRegisterProps {
  initialData: {
    totalUniquePlayers: number;
    eligiblePlayersCount: number;
    excludedPlayersCount: number;
    sufficientSampleCount: number;
    insufficientSampleCount: number;
    shortlistedCandidatesCount: number;
    limitationsDisclosure: string;
    players: PlayerRecord[];
  };
}

export default function MasterPlayerRegisterSection({ initialData }: MasterRegisterProps) {
  const [searchTerm, setSearchTerm] = useState('');
  const [categoryFilter, setCategoryFilter] = useState('ALL');
  const [roleFilter, setRoleFilter] = useState('ALL');
  const [selectedPlayer, setSelectedPlayer] = useState<PlayerRecord | null>(null);

  const players = initialData?.players || [];

  const filteredPlayers = useMemo(() => {
    return players.filter((p) => {
      // Exclude policy restricted players from public display
      if (p.iplEligibilityStatus === 'Policy Restricted') return false;

      // Category filter
      if (categoryFilter === 'SHORTLIST' && p.selectionCategory !== 'RR Auction Shortlist') return false;
      if (categoryFilter === 'GEMS' && p.selectionCategory !== 'Hidden Gem') return false;
      if (categoryFilter === 'TOP_PRESSURE' && !p.selectionCategory.includes('Top Pressure')) return false;
      if (categoryFilter === 'BACKUP' && p.selectionCategory !== 'Backup Candidate') return false;

      // Role filter
      if (roleFilter !== 'ALL' && !p.role.toLowerCase().includes(roleFilter.toLowerCase())) return false;

      // Search term
      if (searchTerm.trim() !== '') {
        const term = searchTerm.toLowerCase();
        return p.name.toLowerCase().includes(term) || p.nationality.toLowerCase().includes(term);
      }

      return true;
    });
  }, [players, categoryFilter, roleFilter, searchTerm]);

  return (
    <section id="master-register" className="py-16 sm:py-24 border-t border-rr-border bg-white text-slate-800">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-12">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-[10px] sm:text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 05 / MASTER PLAYER-SELECTION REGISTER
          </span>
        </div>

        {/* Title & Description */}
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-8 sm:mb-10 gap-4 sm:gap-6 pb-6 border-b border-rr-border">
          <div>
            <h2 className="text-2xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display leading-[1.05]">
              COMPLETE PLAYER UNIVERSE & <br />
              <span className="text-rr-pink">SELECTION AUDIT REGISTER</span>
            </h2>
          </div>
          <p className="text-xs sm:text-sm text-slate-600 max-w-md font-normal leading-relaxed">
            Transparent disclosure of all analyzed players across the dataset universe. 
            Audited for data sufficiency, BCCI eligibility, franchise retentions, and realistic auction availability.
          </p>
        </div>

        {/* Dataset Completeness & Audit Metrics Strip */}
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 sm:gap-3 mb-6 sm:mb-8 text-xs font-mono">
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">Player Universe</div>
            <div className="text-lg sm:text-xl font-black text-rr-navy mt-0.5">{initialData?.totalUniquePlayers || 1217}</div>
            <div className="text-[9px] text-slate-400">Total Unique Players</div>
          </div>
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">100% Eligible Pool</div>
            <div className="text-lg sm:text-xl font-black text-emerald-700 mt-0.5">{initialData?.eligiblePlayersCount || 1149}</div>
            <div className="text-[9px] text-emerald-600 font-semibold">BCCI/IPL Verified</div>
          </div>
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">Audit Excluded</div>
            <div className="text-lg sm:text-xl font-black text-slate-700 mt-0.5">{initialData?.excludedPlayersCount || 68}</div>
            <div className="text-[9px] text-slate-400">PCB (Zero UI Exposure)</div>
          </div>
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">Sufficient Sample</div>
            <div className="text-lg sm:text-xl font-black text-rr-navy mt-0.5">{initialData?.sufficientSampleCount || 184}</div>
            <div className="text-[9px] text-slate-400">N ≥ 60 Pressure Balls</div>
          </div>
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">Bayes Shrunk</div>
            <div className="text-lg sm:text-xl font-black text-slate-700 mt-0.5">{initialData?.insufficientSampleCount || 1033}</div>
            <div className="text-[9px] text-slate-400">N &lt; 60 Prior Stabilized</div>
          </div>
          <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
            <div className="text-[10px] text-slate-500 uppercase">RR Target Shortlist</div>
            <div className="text-lg sm:text-xl font-black text-rr-pink mt-0.5">{initialData?.shortlistedCandidatesCount || 12}</div>
            <div className="text-[9px] text-rr-pink font-semibold">Actionable Candidates</div>
          </div>
        </div>

        {/* Filter & Search Bar */}
        <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3 sm:gap-4 p-3 sm:p-4 rounded-[2px] bg-rr-offwhite border border-rr-border mb-6">
          <div className="relative flex-1 max-w-md">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
            <input
              type="text"
              placeholder="Search by player name or nationality..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-white border border-rr-border rounded-[2px] pl-9 pr-3 py-2 text-xs font-mono text-rr-navy placeholder:text-slate-400 focus:outline-none focus:border-rr-pink"
            />
          </div>

          <div className="flex flex-wrap items-center gap-1.5 sm:gap-2">
            <span className="text-xs font-mono text-slate-500 uppercase mr-1">Category:</span>
            {[
              { id: 'ALL', label: 'All' },
              { id: 'SHORTLIST', label: 'RR Shortlist' },
              { id: 'GEMS', label: 'Hidden Gems' },
              { id: 'TOP_PRESSURE', label: 'Top Pressure' },
              { id: 'BACKUP', label: 'Backups' }
            ].map((cat) => (
              <button
                key={cat.id}
                onClick={() => setCategoryFilter(cat.id)}
                className={`px-2.5 sm:px-3 py-1.5 rounded-[2px] text-xs font-mono font-semibold transition-all border ${
                  categoryFilter === cat.id
                    ? 'bg-rr-navy text-white border-rr-navy'
                    : 'bg-white border-rr-border text-slate-600 hover:text-rr-navy'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        {/* Mobile Horizontal Scroll Indicator */}
        <div className="sm:hidden text-[10px] font-mono text-[#6B7280] mb-2 flex items-center justify-between">
          <span>← Scroll table horizontally →</span>
          <span className="text-rr-pink">Tap row for full audit</span>
        </div>

        {/* Master Table */}
        <div className="bg-white border border-rr-border rounded-[2px] overflow-x-auto shadow-sm -mx-4 sm:mx-0">
          <table className="w-full text-left border-collapse font-mono text-xs min-w-[760px]">
            <thead>
              <tr className="bg-rr-offwhite border-b border-rr-border text-slate-500 uppercase text-[10px]">
                <th className="py-3 px-4">#</th>
                <th className="py-3 px-4">Player Name</th>
                <th className="py-3 px-4">Role</th>
                <th className="py-3 px-4">Nationality</th>
                <th className="py-3 px-4 text-center">Sample (Balls)</th>
                <th className="py-3 px-4 text-center">Pressure SR/Econ</th>
                <th className="py-3 px-4 text-center">BRS Score</th>
                <th className="py-3 px-4">Data Quality</th>
                <th className="py-3 px-4">Selection Category</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {filteredPlayers.slice(0, 50).map((player, idx) => {
                const isShortlisted = player.selectionCategory === 'RR Auction Shortlist';
                const isGem = player.selectionCategory === 'Hidden Gem';
                const isRetained = player.selectionCategory.includes('Retained');

                return (
                  <tr
                    key={player.playerId}
                    onClick={() => setSelectedPlayer(player)}
                    className="hover:bg-slate-50 transition-colors cursor-pointer"
                  >
                    <td className="py-3 px-4 text-slate-400 font-bold">{idx + 1}</td>
                    <td className="py-3 px-4 font-bold text-rr-navy font-sans">
                      {player.name}
                    </td>
                    <td className="py-3 px-4 text-slate-600">{player.role}</td>
                    <td className="py-3 px-4 text-slate-600">
                      <span className="flex items-center gap-1.5">
                        <span>{player.nationality}</span>
                        <span className="text-[9px] text-slate-400">({player.classification === 'Overseas' ? 'OS' : 'IND'})</span>
                      </span>
                    </td>
                    <td className="py-3 px-4 text-center text-slate-600 font-bold">
                      {player.highPressureDeliveries}
                    </td>
                    <td className="py-3 px-4 text-center font-bold text-rr-navy">
                      {player.pressureSr ? `${player.pressureSr} SR` : player.pressureEcon ? `${player.pressureEcon} RPO` : '—'}
                    </td>
                    <td className="py-3 px-4 text-center font-black text-rr-navy">
                      <span className={`px-2 py-0.5 rounded-[2px] ${
                        player.brsScore >= 75 ? 'bg-pink-50 text-rr-pink border border-pink-200' :
                        player.brsScore >= 65 ? 'bg-slate-100 text-rr-navy' : 'text-slate-500'
                      }`}>
                        {player.brsScore.toFixed(1)}
                      </span>
                    </td>
                    <td className="py-3 px-4">
                      <span className={`text-[10px] font-semibold ${
                        player.dataQualityStatus.includes('Sufficient') ? 'text-emerald-700' : 'text-slate-400'
                      }`}>
                        {player.dataQualityStatus.includes('Sufficient') ? 'Sufficient' : 'Bayes Shrunk'}
                      </span>
                    </td>
                    <td className="py-3 px-4">
                      <span className={`px-2 py-0.5 rounded-[2px] text-[10px] font-bold ${
                        isShortlisted ? 'bg-pink-50 text-rr-pink border border-pink-200' :
                        isGem ? 'bg-amber-50 text-amber-800 border border-amber-200' :
                        isRetained ? 'bg-slate-100 text-slate-700 border border-slate-200' :
                        'bg-slate-50 text-slate-500'
                      }`}>
                        {player.selectionCategory}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-right">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          setSelectedPlayer(player);
                        }}
                        className="px-2.5 py-1 rounded-[2px] bg-rr-offwhite hover:bg-rr-navy hover:text-white text-rr-navy text-[10px] font-mono font-bold transition-all border border-rr-border"
                      >
                        Dossier
                      </button>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        <div className="flex flex-col sm:flex-row items-center justify-between gap-3 p-4 rounded-[2px] bg-rr-offwhite border border-rr-border mt-4 text-xs font-mono text-slate-500">
          <div>
            Showing <b>{Math.min(filteredPlayers.length, 50)}</b> of <b>{filteredPlayers.length}</b> eligible records matching active filters.
          </div>
          <div className="text-[11px] text-slate-400">
            *Excludes 68 policy-restricted PCB records preserved in internal regulatory audit.
          </div>
        </div>

        {/* Detailed Player Dossier Modal */}
        {selectedPlayer && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/60 backdrop-blur-sm animate-in fade-in duration-200">
            <div className="bg-white border border-rr-border rounded-[2px] shadow-2xl max-w-2xl w-full p-4 sm:p-6 space-y-4 sm:space-y-5 relative max-h-[92vh] overflow-y-auto">
              
              <button
                onClick={() => setSelectedPlayer(null)}
                className="absolute top-4 right-4 p-1.5 rounded-[2px] bg-rr-offwhite hover:bg-slate-200 text-slate-500 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>

              <div className="pr-8">
                <div className="flex flex-wrap items-center gap-1.5 sm:gap-2 mb-1.5">
                  <span className="px-2 py-0.5 rounded-[2px] text-[10px] font-mono font-bold bg-pink-50 text-rr-pink border border-pink-200 uppercase">
                    ID #{selectedPlayer.playerId} · {selectedPlayer.classification}
                  </span>
                  <span className="text-xs font-mono text-slate-500">{selectedPlayer.nationality}</span>
                </div>
                <h3 className="text-xl sm:text-2xl lg:text-3xl font-extrabold text-rr-navy font-display">
                  {selectedPlayer.name}
                </h3>
                <div className="text-[11px] sm:text-xs font-mono text-slate-500 mt-1">
                  {selectedPlayer.role} · Competitions: {selectedPlayer.competitions?.join(', ') || 'Domestic T20'}
                </div>
              </div>

              {/* Core Metrics Grid */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 sm:gap-3 font-mono text-xs text-center">
                <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">BRS Score</div>
                  <div className="text-lg sm:text-xl font-black text-rr-pink mt-1">{selectedPlayer.brsScore.toFixed(1)}</div>
                </div>
                <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Pressure Sample</div>
                  <div className="text-lg sm:text-xl font-black text-rr-navy mt-1">{selectedPlayer.highPressureDeliveries} b</div>
                </div>
                <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Pressure Output</div>
                  <div className="text-sm sm:text-base font-bold text-rr-navy mt-1">
                    {selectedPlayer.pressureSr ? `${selectedPlayer.pressureSr} SR` : selectedPlayer.pressureEcon ? `${selectedPlayer.pressureEcon} RPO` : '—'}
                  </div>
                </div>
                <div className="p-2.5 sm:p-3 bg-rr-offwhite border border-rr-border rounded-[2px]">
                  <div className="text-[10px] text-slate-500 uppercase">Dot Ball Rate</div>
                  <div className="text-sm sm:text-base font-bold text-rr-navy mt-1">{selectedPlayer.dotPct ? `${selectedPlayer.dotPct}%` : '—'}</div>
                </div>
              </div>

              {/* Status and Classification Details */}
              <div className="p-3 sm:p-4 bg-rr-offwhite border border-rr-border rounded-[2px] space-y-2 text-xs font-mono">
                <div className="flex justify-between">
                  <span className="text-slate-500">BCCI Eligibility:</span>
                  <span className="font-bold text-emerald-700">{selectedPlayer.iplEligibilityStatus}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Auction Availability:</span>
                  <span className="font-bold text-rr-navy">{selectedPlayer.auctionAvailabilityStatus}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Data Quality & Confidence:</span>
                  <span className="font-bold text-slate-700">{selectedPlayer.dataQualityStatus} ({selectedPlayer.confidenceLevel})</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-500">Selection Category:</span>
                  <span className="font-bold text-rr-pink">{selectedPlayer.selectionCategory}</span>
                </div>
              </div>

              {/* Selection Explanation */}
              <div className="space-y-1.5">
                <div className="text-xs font-mono font-bold text-rr-navy uppercase">
                  Technical Selection Justification:
                </div>
                <p className="text-xs text-slate-600 leading-relaxed font-normal">
                  {selectedPlayer.selectionExplanation}
                </p>
              </div>

              <div className="pt-2 border-t border-rr-border flex justify-end">
                <button
                  onClick={() => setSelectedPlayer(null)}
                  className="w-full sm:w-auto px-4 py-2.5 rounded-[2px] bg-rr-navy text-white text-xs font-mono font-bold uppercase tracking-wider"
                >
                  Close Dossier
                </button>
              </div>
            </div>
          </div>
        )}

      </div>
    </section>
  );
}