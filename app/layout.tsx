import type { Metadata, Viewport } from 'next';
import './globals.css';

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
};

export const metadata: Metadata = {
  title: 'RR APEX SCOUT | Rajasthan Royals SupeRR Selector S2',
  description: 'Competition-winning sports intelligence platform identifying the Top 10 Batters and Top 10 Bowlers most reliable under pressure for Rajasthan Royals IPL 2027 Auction Strategy.',
  keywords: ['Rajasthan Royals', 'SupeRR Selector', 'IPL 2027', 'Cricket Analytics', 'Pressure Modeling', 'Bayesian Shrinkage', 'Sports Science'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className="min-h-screen bg-rr-offwhite text-slate-800 antialiased selection:bg-rr-pink selection:text-white font-sans overflow-x-hidden">
        {children}
      </body>
    </html>
  );
}
