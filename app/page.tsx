import fs from 'fs';
import path from 'path';
import Navbar from '@/components/Navbar';
import HeroSection from '@/components/HeroSection';
import MethodologyOverview from '@/components/MethodologyOverview';
import TopBattersSection from '@/components/TopBattersSection';
import TopBowlersSection from '@/components/TopBowlersSection';
import MasterPlayerRegisterSection from '@/components/MasterPlayerRegisterSection';
import PlayerIntelligenceSection from '@/components/PlayerIntelligenceSection';
import HeadToHeadComparison from '@/components/HeadToHeadComparison';
import PlayerCompatibilitySection from '@/components/PlayerCompatibilitySection';
import LeadershipStrategySection from '@/components/LeadershipStrategySection';
import AuctionShortlistSection from '@/components/AuctionShortlistSection';
import SquadConstructionSection from '@/components/SquadConstructionSection';
import HiddenGemsSection from '@/components/HiddenGemsSection';
import MethodologySection from '@/components/MethodologySection';
import ReportDownloadSection from '@/components/ReportDownloadSection';
import Footer from '@/components/Footer';

// Load precomputed data
function getData() {
  const dataDir = path.join(process.cwd(), 'data', 'processed');
  const battersRaw = fs.readFileSync(path.join(dataDir, 'top10_batters.json'), 'utf-8');
  const bowlersRaw = fs.readFileSync(path.join(dataDir, 'top10_bowlers.json'), 'utf-8');
  const statsRaw = fs.readFileSync(path.join(dataDir, 'summary_stats.json'), 'utf-8');
  const registerRaw = fs.readFileSync(path.join(dataDir, 'master_player_register.json'), 'utf-8');
  const leadershipRaw = fs.readFileSync(path.join(dataDir, 'leadership_strategy.json'), 'utf-8');

  return {
    batters: JSON.parse(battersRaw),
    bowlers: JSON.parse(bowlersRaw),
    summaryStats: JSON.parse(statsRaw),
    masterRegister: JSON.parse(registerRaw),
    leadershipData: JSON.parse(leadershipRaw)
  };
}

export default function Home() {
  const { batters, bowlers, summaryStats, masterRegister, leadershipData } = getData();

  return (
    <main className="min-h-screen bg-rr-offwhite text-slate-800 selection:bg-rr-pink selection:text-white font-sans">
      {/* Fixed Clean Header & Fullscreen Navigation Overlay */}
      <Navbar />

      {/* Chapter 01: Overview & Executive Briefing */}
      <HeroSection summaryStats={summaryStats} />

      {/* Chapter 02: Pressure Intelligence & Stress-Load Index */}
      <MethodologyOverview />

      {/* Chapter 03: Top 10 Batters (Pure Statistical Ranking + Availability Status) */}
      <TopBattersSection batters={batters} />

      {/* Chapter 04: Top 10 Bowlers (Pure Statistical Ranking + Availability Status) */}
      <TopBowlersSection bowlers={bowlers} />

      {/* Chapter 05: Master Player-Selection Register (1,217 Player Universe Audit) */}
      <MasterPlayerRegisterSection initialData={masterRegister} />

      {/* Chapter 06: Player Intelligence (Behavioural DNA, Innings Trajectory & Repertoires) */}
      <PlayerIntelligenceSection batters={batters} bowlers={bowlers} />

      {/* Chapter 07: Head-to-Head Comparison & Deltas */}
      <HeadToHeadComparison />

      {/* Chapter 08: Player Compatibility & Tandem Synergies (Empirical & Projected) */}
      <PlayerCompatibilitySection />

      {/* Chapter 09: Captaincy & Leadership Intelligence (Sanju Samson Audit & Succession) */}
      <LeadershipStrategySection data={leadershipData} />

      {/* Chapter 10: Realistic Auction Target Shortlist & Auction Opportunity Score (AOS) */}
      <AuctionShortlistSection />

      {/* Chapter 11: Squad Construction & Scenarios (Scenarios A, B, C; Playing XI) */}
      <SquadConstructionSection />

      {/* Chapter 12: Hidden Gems & Market Valuation Asymmetries */}
      <HiddenGemsSection />

      {/* Chapter 13: The Mathematical Methodology & Bayesian Formulation */}
      <MethodologySection />

      {/* Chapter 14: Deliverables, PDF Report & Pitch Deck Downloads */}
      <ReportDownloadSection />

      {/* High-Contrast Professional Footer */}
      <Footer />
    </main>
  );
}