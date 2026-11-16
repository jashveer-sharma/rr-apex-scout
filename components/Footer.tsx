'use client';

import React from 'react';
import { Shield, ArrowUp, ArrowUpRight } from 'lucide-react';

export default function Footer() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const navChapters = [
    { num: '01', title: 'OVERVIEW', href: '#overview' },
    { num: '02', title: 'PRESSURE INDEX', href: '#pressure-index' },
    { num: '03', title: 'TOP BATTERS', href: '#batters' },
    { num: '04', title: 'TOP BOWLERS', href: '#bowlers' },
    { num: '05', title: 'REGISTER', href: '#master-register' },
    { num: '06', title: 'INTELLIGENCE (DNA)', href: '#player-intelligence' },
    { num: '07', title: 'COMPARISON', href: '#compare' },
    { num: '08', title: 'COMPATIBILITY', href: '#compatibility' },
    { num: '09', title: 'LEADERSHIP', href: '#leadership' },
    { num: '10', title: 'AUCTION SHORTLIST', href: '#auction-shortlist' },
    { num: '11', title: 'SQUAD SCENARIOS', href: '#squad-construction' },
    { num: '12', title: 'HIDDEN GEMS', href: '#gems' },
    { num: '13', title: 'METHODOLOGY', href: '#methodology' },
    { num: '14', title: 'REPORT DOWNLOAD', href: '#report' },
  ];

  return (
    <footer className="py-16 bg-rr-navy text-slate-400 text-xs border-t border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 pb-12 border-b border-slate-800">
          {/* Brand Col */}
          <div className="lg:col-span-5 space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-[2px] bg-rr-pink flex items-center justify-center text-white font-black text-sm">
                RR
              </div>
              <div>
                <div className="font-extrabold text-white text-base tracking-wider font-display">
                  RR APEX SCOUT
                </div>
                <div className="text-[11px] font-mono text-rr-pink">
                  Rajasthan Royals SupeRR Selector Season 2
                </div>
              </div>
            </div>
            <p className="text-xs text-slate-400 leading-relaxed max-w-sm font-normal">
              Empirical cricket intelligence platform designed to isolate true clutch temperament from domestic delivery telemetry for Rajasthan Royals’ IPL 2027 auction strategy.
            </p>
          </div>

          {/* Chapters Grid */}
          <div className="lg:col-span-7">
            <div className="text-[10px] font-mono font-bold uppercase tracking-widest text-slate-500 mb-4">
              EDITORIAL CHAPTERS
            </div>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px]">
              {navChapters.map((c) => (
                <a
                  key={c.num}
                  href={c.href}
                  className="p-2 rounded-[2px] bg-slate-900/60 border border-slate-800 hover:border-rr-pink hover:text-white transition-all flex items-center justify-between"
                >
                  <span className="text-rr-pink text-[10px]">{c.num}</span>
                  <span className="truncate text-slate-300">{c.title}</span>
                </a>
              ))}
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 font-mono text-[11px]">
          <div className="text-slate-400">
            200,999 Deliveries · 883 Matches · 1,217 Player Universe · M₀ = 60 Empirical Bayes Prior · 100% BCCI/IPL Eligible
          </div>

          <div className="flex items-center gap-4">
            <span className="text-slate-500">
              SupeRR Selector Round 1 · November 2026
            </span>
            <button
              onClick={scrollToTop}
              className="p-2 rounded-[2px] bg-slate-800 border border-slate-700 hover:border-rr-pink text-slate-300 hover:text-white transition-all flex items-center gap-1 text-xs font-mono"
              title="Back to Top"
            >
              <ArrowUp className="w-3.5 h-3.5" />
              <span>TOP</span>
            </button>
          </div>
        </div>
      </div>
    </footer>
  );
}