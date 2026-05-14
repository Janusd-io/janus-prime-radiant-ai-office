---
type: source
source_type: laptop
title: FinalCTA
slug: finalcta
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/FinalCTA.tsx
original_size: 1492
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# FinalCTA

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/FinalCTA.tsx` on 2026-05-14._

```tsx
import { Rocket } from 'lucide-react';

export default function FinalCTA() {
  return (
    <section className="py-24 bg-slate-900 overflow-hidden relative">
      <div className="absolute top-0 left-0 w-full h-full opacity-10 pointer-events-none">
        <div className="absolute top-[10%] left-[5%] w-64 h-64 bg-blue-500 rounded-full blur-[120px]"></div>
        <div className="absolute bottom-[10%] right-[5%] w-64 h-64 bg-blue-400 rounded-full blur-[120px]"></div>
      </div>
      
      <div className="container mx-auto px-4 relative z-10 text-center">
        <h2 className="font-heading text-3xl md:text-5xl font-bold text-white mb-6">
          Start Receiving Dubai Buyer Enquiries Today
        </h2>
        <p className="text-blue-100 text-lg md:text-xl mb-10 max-w-2xl mx-auto opacity-80">
          Stop chasing cold leads. Join over 300 brokers getting verified, high-intent buyer inquiries delivered daily.
        </p>
        
        <a 
          href="#pricing" 
          className="inline-flex items-center gap-2 px-10 py-5 bg-primary text-white rounded-full font-bold text-xl hover:bg-blue-700 transition-all shadow-xl shadow-blue-500/20 active:scale-95"
        >
          Reserve Your Leads
          <Rocket className="w-6 h-6" />
        </a>
        
        <p className="mt-8 text-slate-400 text-sm italic font-medium">
          Limited lead volume available. Secured on a first-come, first-served basis.
        </p>
      </div>
    </section>
  );
}

```