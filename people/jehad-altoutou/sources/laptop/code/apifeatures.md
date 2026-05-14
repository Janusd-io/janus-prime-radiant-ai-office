---
type: source
source_type: laptop
title: ApiFeatures
slug: apifeatures
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiFeatures.tsx
original_size: 4654
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# ApiFeatures

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiFeatures.tsx` on 2026-05-14._

```tsx
'use client';

import { Database, Image as ImageIcon, Zap, Globe, Layers, ShieldCheck, Box } from 'lucide-react';
import { clsx } from 'clsx';

const features = [
  {
    title: "Unified Data Layer",
    description: "Deep integration with 2,700+ off-plan projects. Get everything from developer credentials to real-time unit availability in a single JSON query.",
    icon: Database,
    className: "lg:col-span-2",
    accent: "bg-cyan-500/10 text-cyan-400 border-cyan-500/20"
  },
  {
    title: "White-Label CDNs",
    description: "Unbranded high-res brochures and 4K renders served from our global edge network.",
    icon: ImageIcon,
    className: "lg:col-span-1",
    accent: "bg-blue-500/10 text-blue-400 border-blue-500/20"
  },
  {
    title: "500ms Edge Latency",
    description: "Built for speed. Our globally distributed architecture ensures lightning-fast responses no matter where your app is hosted.",
    icon: Zap,
    className: "lg:col-span-1",
    accent: "bg-amber-500/10 text-amber-400 border-amber-500/20"
  },
  {
    title: "Clean JSON Schemas",
    description: "Strictly typed, predictable, and fully documented. Integrate with any modern frontend or backend stack in less than a day.",
    icon: Layers,
    className: "lg:col-span-2",
    accent: "bg-purple-500/10 text-purple-400 border-purple-500/20"
  }
];

export default function ApiFeatures() {
  return (
    <section className="py-40 bg-[#050505] relative overflow-hidden">
      {/* Decorative Glows */}
      <div className="absolute top-1/2 left-0 w-[600px] h-[600px] bg-cyan-600/5 blur-[150px] rounded-full pointer-events-none"></div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="flex flex-col md:flex-row justify-between items-end gap-12 mb-24 animate-in fade-in slide-in-from-bottom-10 duration-1000 ease-out fill-mode-both">
          <div className="max-w-3xl space-y-4">
            <h2 className="text-sm font-bold text-cyan-500 uppercase tracking-[0.4em] mb-4">Core Capabilities</h2>
            <h3 className="text-5xl md:text-7xl font-black font-heading text-white leading-tight tracking-tighter">
              A Powerful Engine for <span className="text-slate-500">Premium Real Estate.</span>
            </h3>
          </div>
          <p className="text-slate-400 text-xl max-w-sm font-light leading-relaxed">
            Stop scraping. Start scaling. Our official API provides the structured data foundation your team needs.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, i) => (
            <div 
              key={i} 
              className={clsx(
                "group relative p-10 md:p-12 rounded-[2.5rem] border border-white/5 bg-white/[0.01] hover:bg-white/[0.02] transition-all duration-700 ease-out flex flex-col justify-between overflow-hidden animate-in fade-in slide-in-from-bottom-12 duration-1000 fill-mode-both hover:-translate-y-2 hover:shadow-[0_20px_40px_rgba(6,182,212,0.05)]",
                feature.className
              )}
              style={{ animationDelay: `${200 + i * 150}ms` }}
            >
              <div className="relative z-10">
                <div className={clsx(
                  "w-14 h-14 rounded-2xl flex items-center justify-center mb-10 border transition-transform duration-700 ease-out group-hover:scale-110 group-hover:rotate-6",
                  feature.accent
                )}>
                  <feature.icon className="w-7 h-7" />
                </div>
                <h4 className="text-3xl font-black text-white mb-5 tracking-tight">{feature.title}</h4>
                <p className="text-slate-400 leading-relaxed font-light text-xl">
                  {feature.description}
                </p>
              </div>
              
              {/* Interaction UI Decoration */}
              <div className="mt-16 flex items-center gap-4 relative z-10">
                <div className="h-1 flex-1 bg-white/5 rounded-full overflow-hidden">
                  <div className="h-full bg-cyan-500/50 w-0 group-hover:w-full transition-all duration-1000 ease-in-out"></div>
                </div>
                <Box className="w-5 h-5 text-slate-700 group-hover:text-cyan-500 transition-colors duration-500" />
              </div>

              {/* Background Accent Gradient */}
              <div className="absolute -right-8 -bottom-8 w-40 h-40 bg-cyan-500/5 blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-1000 ease-out"></div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

```