---
type: source
source_type: laptop
title: Desktop Captures — page
slug: page-41
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/page.tsx
original_size: 744
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# page

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/page.tsx` on 2026-05-14._

```tsx
import Navbar from '@/components/Navbar';
import Hero from '@/components/Hero';
import TrustStats from '@/components/TrustStats';
import HowItWorks from '@/components/HowItWorks';
import UrgencyBanner from '@/components/UrgencyBanner';
import Pricing from '@/components/Pricing';
import FAQ from '@/components/FAQ';
import LeadQuality from '@/components/LeadQuality';
import FinalCTA from '@/components/FinalCTA';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <main className="min-h-screen">
      <Navbar />
      <Hero />
      <TrustStats />
      <HowItWorks />
      <UrgencyBanner />
      <Pricing />
      <LeadQuality />
      <FAQ />
      <FinalCTA />
      <Footer />
    </main>
  );
}

```