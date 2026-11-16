'use client';

import React from 'react';
import { Download, FileText, Presentation, CheckCircle, ShieldCheck, ArrowUpRight, Trophy, Sparkles } from 'lucide-react';

export default function ReportDownloadSection() {
  return (
    <section id="report" className="py-24 border-t border-rr-border bg-white text-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Editorial Chapter Header */}
        <div className="flex items-center gap-3 mb-4">
          <span className="w-8 h-[2px] bg-rr-pink" />
          <span className="text-xs font-mono font-bold tracking-widest text-rr-pink uppercase">
            CHAPTER 14 / DELIVERABLES & UNSTOP SUBMISSION
          </span>
        </div>

        <div className="p-8 sm:p-12 rounded-[2px] bg-rr-offwhite border border-rr-border space-y-8">
          <div className="max-w-3xl">
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-black text-rr-navy tracking-tight uppercase font-display mb-4">
              DOWNLOAD METHODOLOGY <br />
              <span className="text-rr-pink">WHITEPAPER & SLIDE DECK</span>
            </h2>
            <p className="text-xs sm:text-sm text-slate-600 leading-relaxed">
              In accordance with Unstop Round 1 submission specifications, our comprehensive methodology whitepaper 
              details all mathematical formulations, Bayesian prior derivations, ball-by-ball leverage thresholds, 
              and Rajasthan Royals IPL 2027 auction recruitment blueprints.
            </p>
          </div>

          {/* Download Buttons */}
          <div className="flex flex-wrap items-center gap-4">
            <a
              href="/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Methodology_Report.pdf"
              download
              className="inline-flex items-center gap-3 px-6 py-3.5 rounded-[2px] bg-rr-pink hover:bg-rr-pinkLight text-white font-bold text-xs font-mono transition-all uppercase tracking-wider"
            >
              <FileText className="w-4 h-4 flex-shrink-0" />
              <span>Download Official Methodology Whitepaper (.pdf)</span>
            </a>

            <a
              href="/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Presentation.pptx"
              download
              className="inline-flex items-center gap-3 px-6 py-3.5 rounded-[2px] bg-white border border-rr-navy hover:bg-rr-navy hover:text-white text-rr-navy font-bold text-xs font-mono transition-all uppercase tracking-wider"
            >
              <Presentation className="w-4 h-4 flex-shrink-0" />
              <span>Download Presentation Deck (.pptx)</span>
            </a>
          </div>

          {/* Official Submission Dropdown Synchronization Checklist */}
          <div className="p-6 rounded-[2px] bg-white border border-rr-border space-y-4">
            <div className="text-xs font-mono font-bold text-rr-navy uppercase tracking-wider flex items-center gap-2">
              <Trophy className="w-4 h-4 text-rr-pink" />
              <span>Unstop Submission Portal Dropdown Sync (Top 10 Selections - 100% Eligible)</span>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs font-mono">
              <div className="space-y-2 p-4 rounded-[2px] bg-rr-offwhite border border-rr-border">
                <div className="text-rr-pink font-bold text-[11px] uppercase tracking-wider mb-2 flex items-center justify-between border-b border-rr-border pb-1.5">
                  <span>Top 10 Batters (Official Register)</span>
                  <span className="text-[10px] text-slate-500 font-normal">20 Total Ranked</span>
                </div>
                <div className="space-y-1.5 text-[11px]">
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">1. Suryakumar Yadav (IND)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: MI → Alt: Tilak Varma</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">2. Naman Dhir (IND)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Prime Target</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">3. Tim David (AUS)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Overseas Finisher</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">4. Shashank Singh (IND)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Crisis Chase</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">5. Jos Buttler (ENG)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Marquee Opener</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">6. Rajat Patidar (IND)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: RCB → Alt: Nehal Wadhera</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">7. Phil Salt (ENG)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Explosive Keeper</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">8. Reeza Hendricks (RSA)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Top-Order Striker</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">9. Virat Kohli (IND)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: RCB → Alt: Devdutt Padikkal</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">10. Rishabh Pant (IND)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: LSG → Alt: Dhruv Jurel</span></div>
                </div>
              </div>

              <div className="space-y-2 p-4 rounded-[2px] bg-rr-offwhite border border-rr-border">
                <div className="text-rr-navy font-bold text-[11px] uppercase tracking-wider mb-2 flex items-center justify-between border-b border-rr-border pb-1.5">
                  <span>Top 10 Bowlers (Official Register)</span>
                  <span className="text-[10px] text-slate-500 font-normal">20 Total Ranked</span>
                </div>
                <div className="space-y-1.5 text-[11px]">
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">1. Hasan Mahmud (BAN)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · #1 Death Yorker</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">2. Benjamin Sears (NZL)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · 145+ Express Pace</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">3. Sunil Narine (WI)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: KKR → Alt: Varun Chakaravarthy</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">4. Mohammad Rishad (BAN)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Wrist-Spin Weapon</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">5. Mitchell Santner (NZL)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Finger-Spin Choke</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">6. Umran Malik (IND)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · 150+ km/h Heat</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">7. Rashid Khan (AFG)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: GT → Alt: Ravi Bishnoi</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">8. Matheesha Pathirana (SL)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: CSK → Alt: Nuwan Thushara</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">9. Jamie Overton (ENG)</span><span className="text-emerald-800 text-[10px] bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded font-bold">Available · Seam All-Rounder</span></div>
                  <div className="flex items-center justify-between"><span className="text-slate-800 font-semibold">10. Jasprit Bumrah (IND)</span><span className="text-amber-800 text-[10px] bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">Retained: MI → Alt: Avesh Khan</span></div>
                </div>
              </div>
            </div>
          </div>

          {/* Verification checklist */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-4 border-t border-rr-border text-xs text-slate-500 font-mono">
            <div className="flex items-center gap-2">
              <CheckCircle className="w-3.5 h-3.5 text-emerald-600" />
              <span>100% BCCI/IPL Eligible Roster</span>
            </div>
            <div className="flex items-center gap-2">
              <CheckCircle className="w-3.5 h-3.5 text-emerald-600" />
              <span>Full Internal Audit Trail Documented</span>
            </div>
            <div className="flex items-center gap-2">
              <CheckCircle className="w-3.5 h-3.5 text-emerald-600" />
              <span>Deterministic Bayesian Formulation</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}