'use client';

import React, { useState, useEffect } from 'react';
import { ArrowRight, X, Shield, Download, FileText, CheckCircle2 } from 'lucide-react';

const NAV_CHAPTERS = [
  { num: '01', title: 'Overview', desc: 'Executive briefing, competition mandate & core findings', href: '#overview' },
  { num: '02', title: 'Pressure Intelligence', desc: 'Situational Leverage Index (SLI) & empirical weighting', href: '#pressure-index' },
  { num: '03', title: 'Top 10 Batters', desc: 'Statistical performance rankings & Bayesian reliability', href: '#batters' },
  { num: '04', title: 'Top 10 Bowlers', desc: 'Statistical containment benchmarks & wicket threats', href: '#bowlers' },
  { num: '05', title: 'Master Player Register', desc: '1,217 player universe, data sufficiency & audit breakdown', href: '#master-register' },
  { num: '06', title: 'Player Intelligence (DNA)', desc: 'Player DNA, innings trajectory & dismissal profiles', href: '#player-intelligence' },
  { num: '07', title: 'Player Comparison', desc: 'Head-to-head metrics, clutch lifts & delta differentials', href: '#compare' },
  { num: '08', title: 'Player Compatibility', desc: 'Tandem partnerships, pace/spin complement & Jaipur fit', href: '#compatibility' },
  { num: '09', title: 'Captaincy & Leadership', desc: 'Sanju Samson empirical audit, win rates & succession plan', href: '#leadership' },
  { num: '10', title: 'Auction Shortlist', desc: 'Realistic RR targets, AOS opportunity scores & purse fit', href: '#auction-shortlist' },
  { num: '11', title: 'Squad Scenarios & XI', desc: 'Scenarios A, B, C; Playing XI & Impact Player sub', href: '#squad-construction' },
  { num: '12', title: 'Hidden Gems', desc: 'High-leverage market inefficiencies & budget acquisitions', href: '#gems' },
  { num: '13', title: 'Methodology', desc: 'Empirical Bayesian calibration, sample priors & verification', href: '#methodology' },
  { num: '14', title: 'Download Report', desc: 'Publication PDF whitepaper & franchise pitch deck', href: '#report' },
];

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('overview');

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 30);
      const sectionIds = [
        'overview', 'pressure-index', 'batters', 'bowlers',
        'master-register', 'player-intelligence', 'compare', 'compatibility',
        'leadership', 'auction-shortlist', 'squad-construction', 'gems', 'methodology', 'report'
      ];
      for (const id of sectionIds) {
        const el = document.getElementById(id);
        if (el) {
          const rect = el.getBoundingClientRect();
          if (rect.top <= 220 && rect.bottom >= 180) {
            setActiveSection(id);
            break;
          }
        }
      }
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && menuOpen) setMenuOpen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [menuOpen]);

  useEffect(() => {
    if (menuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, [menuOpen]);

  const handleNavClick = (href: string) => {
    setMenuOpen(false);
    const target = document.querySelector(href);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <>
      {/* ── Fixed Clean Header (EterPay Reference) ────────────────────────── */}
      <header
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
          scrolled
            ? 'bg-[#F5F4F7]/95 backdrop-blur-md border-b border-[#E5E7EB] py-3.5 shadow-sm'
            : 'bg-[#F5F4F7] border-b border-[#E5E7EB]/60 py-5'
        }`}
      >
        <div className="max-w-[1440px] mx-auto px-6 lg:px-12 flex items-center justify-between">
          {/* Brand Logo & Identification */}
          <a
            href="#overview"
            className="flex items-center gap-3 group focus:outline-none"
          >
            <div className="w-8 h-8 rounded-[2px] bg-[#10152B] flex items-center justify-center text-white font-bold text-sm tracking-wider">
              RR
            </div>
            <div className="flex flex-col">
              <span className="font-serif text-lg tracking-tight text-[#10152B] leading-none font-bold">
                APEX SCOUT
              </span>
              <span className="text-[10px] font-mono tracking-widest uppercase text-[#EA1D76] mt-0.5 font-semibold">
                Rajasthan Royals · Season 2
              </span>
            </div>
          </a>

          {/* Quick Jump Links (Desktop) */}
          <nav className="hidden xl:flex items-center gap-6 text-[13px] font-medium text-[#4B5563]">
            <a href="#overview" className={`hover:text-[#10152B] transition-colors ${activeSection === 'overview' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Overview
            </a>
            <a href="#batters" className={`hover:text-[#10152B] transition-colors ${activeSection === 'batters' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Batters
            </a>
            <a href="#bowlers" className={`hover:text-[#10152B] transition-colors ${activeSection === 'bowlers' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Bowlers
            </a>
            <a href="#master-register" className={`hover:text-[#10152B] transition-colors ${activeSection === 'master-register' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Register
            </a>
            <a href="#compatibility" className={`hover:text-[#10152B] transition-colors ${activeSection === 'compatibility' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Compatibility
            </a>
            <a href="#leadership" className={`hover:text-[#10152B] transition-colors ${activeSection === 'leadership' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Leadership
            </a>
            <a href="#auction-shortlist" className={`hover:text-[#10152B] transition-colors ${activeSection === 'auction-shortlist' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Auction Targets
            </a>
            <a href="#squad-construction" className={`hover:text-[#10152B] transition-colors ${activeSection === 'squad-construction' ? 'text-[#EA1D76] font-semibold' : ''}`}>
              Squad Builder
            </a>
          </nav>

          {/* Right Action & Menu Trigger */}
          <div className="flex items-center gap-4">
            <a
              href="#report"
              className="hidden sm:inline-flex items-center gap-2 text-xs font-medium text-[#10152B] hover:text-[#EA1D76] border-b border-[#10152B]/30 hover:border-[#EA1D76] pb-0.5 transition-colors"
            >
              <Download size={13} />
              <span>Download Report</span>
            </a>

            <button
              onClick={() => setMenuOpen(!menuOpen)}
              className="inline-flex items-center gap-2.5 px-4 py-2 rounded-[2px] bg-[#10152B] hover:bg-[#EA1D76] text-white text-xs font-mono font-medium tracking-wider uppercase transition-colors"
              aria-label="Toggle Navigation Menu"
            >
              <span>{menuOpen ? 'CLOSE' : 'MENU'}</span>
              <span className="w-1.5 h-1.5 rounded-full bg-[#EA1D76] group-hover:bg-white" />
            </button>
          </div>
        </div>
      </header>

      {/* ── Fullscreen Editorial Navigation Overlay (EterPay / Baztan Style) ── */}
      <div
        className={`fixed inset-0 z-50 bg-[#10152B] text-white transition-opacity duration-300 flex flex-col justify-between p-8 lg:p-14 ${
          menuOpen ? 'opacity-100 pointer-events-auto' : 'opacity-0 pointer-events-none'
        }`}
      >
        {/* Overlay Top Bar */}
        <div className="flex items-center justify-between pb-6 border-b border-white/10">
          <div className="flex items-center gap-3">
            <div className="w-7 h-7 rounded-[2px] bg-[#EA1D76] flex items-center justify-center text-white font-bold text-xs">
              RR
            </div>
            <span className="font-mono text-xs tracking-widest text-[#EA1D76] uppercase">
              RR APEX SCOUT · CHAPTER INDEX
            </span>
          </div>

          <button
            onClick={() => setMenuOpen(false)}
            className="flex items-center gap-2 px-3 py-1.5 rounded-[2px] border border-white/20 hover:border-[#EA1D76] text-xs font-mono tracking-wider transition-colors"
          >
            <X size={14} />
            <span>CLOSE (ESC)</span>
          </button>
        </div>

        {/* Chapters Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-4 my-auto py-6 max-h-[72vh] overflow-y-auto">
          {NAV_CHAPTERS.map((ch) => (
            <button
              key={ch.num}
              onClick={() => handleNavClick(ch.href)}
              className="group text-left p-3.5 border-b border-white/5 hover:border-[#EA1D76] transition-colors block w-full"
            >
              <div className="flex items-baseline gap-3">
                <span className="font-mono text-xs text-[#EA1D76] group-hover:text-white transition-colors">
                  {ch.num}
                </span>
                <span className="font-serif text-base lg:text-lg font-bold text-white group-hover:text-[#EA1D76] transition-colors">
                  {ch.title}
                </span>
              </div>
              <p className="text-[11px] text-[#A5A9B8] mt-1 line-clamp-1 group-hover:text-white/80 transition-colors pl-7">
                {ch.desc}
              </p>
            </button>
          ))}
        </div>

        {/* Overlay Bottom Status */}
        <div className="pt-6 border-t border-white/10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 text-xs font-mono text-[#A5A9B8]">
          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1.5 text-white">
              <CheckCircle2 size={13} className="text-[#EA1D76]" />
              <span>100% BCCI/IPL Eligible Roster</span>
            </span>
            <span>·</span>
            <span>Mini-Auction: Dec 16, 2026 (Goa)</span>
          </div>
          <div className="text-[11px]">
            Press <kbd className="px-1.5 py-0.5 bg-white/10 rounded text-white">Esc</kbd> to exit index
          </div>
        </div>
      </div>
    </>
  );
}