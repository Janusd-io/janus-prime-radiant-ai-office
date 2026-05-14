---
type: source
source_type: laptop
title: SEOPageLayout
slug: seopagelayout
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/SEOPageLayout.tsx
original_size: 1241
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# SEOPageLayout

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/SEOPageLayout.tsx` on 2026-05-14._

```tsx
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import FinalCTA from '@/components/FinalCTA';
import Pricing from '@/components/Pricing';

interface SEOPageProps {
  title: string;
  subtitle: string;
  content: React.ReactNode;
}

export default function SEOPageLayout({ title, subtitle, content }: SEOPageProps) {
  return (
    <main className="min-h-screen">
      <Navbar />
      <section className="pt-32 pb-20 bg-slate-50 border-b border-border">
        <div className="container mx-auto px-4 text-center">
          <h1 className="font-heading text-4xl md:text-6xl font-bold mb-6 italic tracking-tight">{title}</h1>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto italic leading-relaxed">{subtitle}</p>
        </div>
      </section>
      
      <section className="py-20 bg-white">
        <div className="container mx-auto px-4 prose prose-slate max-w-none prose-h2:font-heading prose-h2:text-3xl prose-h3:text-xl prose-p:leading-relaxed prose-p:text-muted-foreground">
          <div className="max-w-4xl mx-auto">
            {content}
          </div>
        </div>
      </section>
      
      <Pricing />
      <FinalCTA />
      <Footer />
    </main>
  );
}

```