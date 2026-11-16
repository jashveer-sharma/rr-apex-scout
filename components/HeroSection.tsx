'use client';

import React from 'react';
import { ArrowRight, Download, ShieldCheck, Database, Award, ArrowUpRight } from 'lucide-react';

interface HeroSectionProps {
  summaryStats: any;
}

export default function HeroSection({ summaryStats }: HeroSectionProps) {
  return (
    <section id="overview" className="min-h-screen pt-36 pb-20 flex flex-col justify-between bg-[#F5F4F7] relative border-b border-[#E5E7EB]">
      <div className="max-w-[1440px] mx-auto px-6 lg:px-12 w-full my-auto">
        {/* Eyebrow / Category Tag (EterPay Reference) */}
        <div className="flex items-center gap-3 mb-8">
          <span className="w-6 h-px bg-[#EA1D76]" />
          <span className="text-[11px] font-mono font-semibold tracking-[0.18em] uppercase text-[#EA1D76]">
            Rajasthan Royals · SupeRR Selector Season 2
          </span>
        </div>

        {/* Two-Column Editorial Hero Layout */}
        <div className="grid lg:grid-cols-12 gap-12 lg:gap-16 items-start">
          {/* Left Column: Bold Headline & Context */}
          <div className="lg:col-span-8">
            <h1
              className="font-serif font-normal text-[#10152B] tracking-tight mb-8"
              style={{
                fontSize: 'clamp(3rem, 6vw, 5.5rem)',
                lineHeight: '1.05',
                letterSpacing: '-0.03em'
              }}
            >
              Pressure reveals champions.
              <br />
              <span className="text-[#EA1D76]">Data discovers them.</span>
            </h1>

            <p className="text-[1.125rem] text-[#4B5563] leading-relaxed mb-10 max-w-2xl font-normal">
              An empirical cricket intelligence platform evaluating <strong className="text-[#10152B]">883 matches</strong> and <strong className="text-[#10152B]">200,999 deliveries</strong>. 
              We identify the Top 10 most reliable batters and bowlers under acute leverage, then rigorously filter by <strong className="text-[#10152B]">BCCI regulations</strong> and <strong className="text-[#10152B]">IPL 2027 mini-auction squad mechanics</strong> to engineer championship acquisitions for Rajasthan Royals.
            </p>

            {/* CTAs — Clean Sharp Rectangular (Zero Gradients / Pill AI Slop) */}
            <div className="flex flex-wrap items-center gap-4 mb-14">
              <a
                href="#auction-shortlist"
                className="inline-flex items-center gap-2.5 px-7 py-3.5 bg-[#EA1D76] hover:bg-[#D01566] text-white text-xs font-mono font-semibold tracking-wider uppercase rounded-[2px] transition-colors"
              >
                <span>Explore Auction Shortlist</span>
                <ArrowRight size={14} />
              </a>

              <a
                href="#batters"
                className="inline-flex items-center gap-2 px-6 py-3.5 bg-[#10152B] hover:bg-[#1C2548] text-white text-xs font-mono font-semibold tracking-wider uppercase rounded-[2px] transition-colors"
              >
                <span>Top 10 Rankings</span>
              </a>

              <a
                href="#report"
                className="inline-flex items-center gap-2 text-xs font-mono font-semibold text-[#10152B] hover:text-[#EA1D76] border-b border-[#10152B]/30 hover:border-[#EA1D76] pb-1 transition-colors ml-2"
              >
                <span>Download Methodology PDF</span>
                <Download size={13} />
              </a>
            </div>
          </div>

          {/* Right Column: Key Mandate Summary Card (Solid White, Thin Border) */}
          <div className="lg:col-span-4">
            <div className="bg-white border border-[#E5E7EB] p-7 rounded-[2px] shadow-sm">
              <div className="text-[11px] font-mono tracking-widest uppercase text-[#6B7280] mb-4 pb-3 border-b border-[#E5E7EB]">
                EXECUTIVE BRIEFING · ROUND 1
              </div>
              
              <div className="space-y-4 text-xs text-[#4B5563] leading-relaxed">
                <div>
                  <span className="font-semibold text-[#10152B] block mb-0.5">Problem Statement</span>
                  Identify the Top 10 most reliable batters and Top 10 most reliable bowlers under pressure from domestic and international leagues.
                </div>

                <div className="w-full h-px bg-[#E5E7EB]" />

                <div>
                  <span className="font-semibold text-[#10152B] block mb-0.5">Crucial Differentiation</span>
                  Separate statistical performance from real auction availability. Never recommend unavailable or retained players for recruitment.
                </div>

                <div className="w-full h-px bg-[#E5E7EB]" />

                <div>
                  <span className="font-semibold text-[#10152B] block mb-0.5">Venue Tailoring</span>
                  Optimized for Sawai Mansingh Stadium (Jaipur) boundary dimensions (70m+) and middle-over spin squeeze.
                </div>
              </div>

              <div className="mt-6 pt-4 border-t border-[#E5E7EB] flex items-center justify-between text-[11px] font-mono">
                <span className="text-[#6B7280]">Target Cycle</span>
                <span className="font-bold text-[#EA1D76]">IPL 2027 Mini-Auction</span>
              </div>
            </div>
          </div>
        </div>

        {/* Clean Stat Strip (EterPay Horizontal Dividing Row) */}
        <div className="pt-12 border-t border-[#E5E7EB] grid grid-cols-2 md:grid-cols-4 gap-8">
          <div>
            <div className="font-serif text-3xl sm:text-4xl text-[#10152B] font-normal" style={{ letterSpacing: '-0.02em' }}>
              200,999
            </div>
            <div className="text-xs font-mono text-[#6B7280] mt-1 uppercase tracking-wider">
              Deliveries Modeled (2022–2026)
            </div>
          </div>

          <div>
            <div className="font-serif text-3xl sm:text-4xl text-[#10152B] font-normal" style={{ letterSpacing: '-0.02em' }}>
              883
            </div>
            <div className="text-xs font-mono text-[#6B7280] mt-1 uppercase tracking-wider">
              Matches (IPL & Bilateral T20I)
            </div>
          </div>

          <div>
            <div className="font-serif text-3xl sm:text-4xl text-[#EA1D76] font-normal" style={{ letterSpacing: '-0.02em' }}>
              67,728
            </div>
            <div className="text-xs font-mono text-[#6B7280] mt-1 uppercase tracking-wider">
              High-Pressure Balls (SLI ≥ 6.5)
            </div>
          </div>

          <div>
            <div className="font-serif text-3xl sm:text-4xl text-[#D6B36A] font-normal" style={{ letterSpacing: '-0.02em' }}>
              100%
            </div>
            <div className="text-xs font-mono text-[#6B7280] mt-1 uppercase tracking-wider">
              Verified Eligible Player Pool
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
