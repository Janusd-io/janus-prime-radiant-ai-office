---
type: source
source_type: laptop
title: ApiFAQ
slug: apifaq
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiFAQ.tsx
original_size: 4989
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# ApiFAQ

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiFAQ.tsx` on 2026-05-14._

```tsx
'use client';

import { Plus, Minus, HelpCircle } from 'lucide-react';
import { useState } from 'react';
import { clsx } from 'clsx';

const faqs = [
  {
    question: "How do I obtain an API key?",
    answer: "API access is managed through RapidAPI. Once you subscribe to a plan, your unique API Key is automatically generated and available in the RapidAPI dashboard for immediate use."
  },
  {
    question: "What is the data update frequency?",
    answer: "The project database is synced daily from core sources. High-priority fields like status and launch updates are processed every 4-6 hours to ensure your platform remains accurate."
  },
  {
    question: "Are the visual assets unbranded?",
    answer: "Yes. Our white-label assets API specifically provides cleaned brochures and renders without third-party source branding, allowing them to be seamlessly integrated into your own UI."
  },
  {
    question: "Can I upgrade to an Enterprise Tier?",
    answer: "We offer custom enterprise quotas, dedicated support channels, and private CDN edge cases for high-volume platforms. Contact sales at dubaipropertylead@gmail.com to discuss custom limits."
  },
  {
    question: "Do you offer SDKs for specific languages?",
    answer: "Through our RapidAPI integration, we provide auto-generated SDK snippets for 15+ environments, including Node.js, Python, PHP, Ruby, and Java."
  }
];

export default function ApiFAQ() {
  const [openIndex, setOpenIndex] = useState<number | null>(0);

  return (
    <section className="py-40 bg-[#050505] relative overflow-hidden">
      {/* Decorative Glow */}
      <div className="absolute top-0 right-1/4 w-[800px] h-[800px] bg-cyan-600/5 blur-[200px] rounded-full pointer-events-none"></div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-24 space-y-6 animate-in fade-in slide-in-from-bottom-10 duration-1000 ease-out fill-mode-both">
            <h2 className="text-sm font-bold text-cyan-500 uppercase tracking-[0.4em]">Support</h2>
            <h3 className="text-5xl md:text-7xl font-black font-heading text-white tracking-tighter leading-[1.1]">
              Developer <span className="text-slate-500 italic">FAQ</span>
            </h3>
          </div>

          <div className="space-y-8">
            {faqs.map((faq, i) => (
              <div 
                key={i} 
                className={clsx(
                  "rounded-[2rem] border transition-all duration-700 ease-out overflow-hidden animate-in fade-in slide-in-from-bottom-10 duration-1000 fill-mode-both",
                  openIndex === i 
                    ? "border-cyan-500/30 bg-cyan-500/[0.04] shadow-[0_20px_40px_rgba(6,182,212,0.05)] scale-[1.01]" 
                    : "border-white/5 bg-white/[0.01] hover:bg-white/[0.03] hover:border-white/10 hover:shadow-xl hover:scale-[1.01]"
                )}
                style={{ animationDelay: `${200 + i * 150}ms` }}
              >
                <button 
                  onClick={() => setOpenIndex(openIndex === i ? null : i)}
                  className="w-full px-10 py-10 flex items-center justify-between text-left group"
                >
                  <div className="flex items-center gap-8">
                    <HelpCircle className={clsx(
                      "w-7 h-7 transition-colors duration-700",
                      openIndex === i ? "text-cyan-500" : "text-slate-700 group-hover:text-slate-500"
                    )} />
                    <span className="text-2xl font-bold text-white tracking-tight leading-snug">{faq.question}</span>
                  </div>
                  <div className={clsx(
                    "w-10 h-10 rounded-full flex items-center justify-center transition-all duration-700 ease-out shrink-0",
                    openIndex === i ? "bg-cyan-500 text-black rotate-180 shadow-[0_0_20px_rgba(6,182,212,0.4)]" : "bg-white/5 text-slate-500 group-hover:bg-white/10 group-hover:text-white"
                  )}>
                    {openIndex === i ? (
                      <Minus className="w-5 h-5" />
                    ) : (
                      <Plus className="w-5 h-5" />
                    )}
                  </div>
                </button>
                <div 
                  className={clsx(
                    "px-10 overflow-hidden transition-all duration-700 ease-in-out origin-top",
                    openIndex === i ? "max-h-[500px] pb-12 opacity-100 scale-y-100" : "max-h-0 opacity-0 scale-y-95"
                  )}
                >
                  <p className="text-slate-400 text-xl leading-relaxed font-light pl-14 border-l-2 border-cyan-500/20 ml-3 bg-gradient-to-r from-cyan-500/5 to-transparent py-4 pl-8 rounded-r-2xl">
                    {faq.answer}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

```