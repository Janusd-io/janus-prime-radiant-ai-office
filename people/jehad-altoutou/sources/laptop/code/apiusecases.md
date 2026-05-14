---
type: source
source_type: laptop
title: ApiUseCases
slug: apiusecases
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiUseCases.tsx
original_size: 3496
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# ApiUseCases

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiUseCases.tsx` on 2026-05-14._

```tsx
'use client';

import { Monitor, Smartphone, Cpu, PieChart, Users, Cloud } from 'lucide-react';

const useCases = [
  {
    title: "Agency Portals",
    description: "Launch a white-label off-plan search portal for your agency in days with a fully populated project database.",
    icon: Monitor
  },
  {
    title: "Mobile Broker Apps",
    description: "Give your brokers instant access to floor plans and brochures on-site via your custom mobile application.",
    icon: Smartphone
  },
  {
    title: "PropTech AI Agents",
    description: "Feed high-fidelity, structured project data into LLMs to build next-gen property advisors and chatbots.",
    icon: Cpu
  },
  {
    title: "Market Intelligence",
    description: "Analyze supply trends and pricing across 2,700+ projects to build advanced market analytics dashboards.",
    icon: PieChart
  },
  {
    title: "Enterprise CRM Sync",
    description: "Sync project inventory directly into Salesforce, HubSpot, or custom CRMs to keep sales teams aligned.",
    icon: Users
  },
  {
    title: "Headless Real Estate",
    description: "Build lightning-fast frontend experiences while we handle the complex multi-source data backend.",
    icon: Cloud
  }
];

export default function ApiUseCases() {
  return (
    <section className="py-40 bg-[#050505] border-t border-white/5 relative">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-end gap-12 mb-24 animate-in fade-in slide-in-from-bottom-10 duration-1000 ease-out fill-mode-both">
          <div className="max-w-3xl space-y-4">
            <h2 className="text-sm font-bold text-cyan-500 uppercase tracking-[0.4em] mb-4">Infinite Integration</h2>
            <h3 className="text-5xl md:text-7xl font-black font-heading text-white leading-tight tracking-tighter">
              One API. <span className="text-slate-500">Endless Use Cases.</span>
            </h3>
          </div>
          <p className="text-slate-400 text-xl max-w-sm font-light leading-relaxed">
            Our data layer powers the most innovative property technology platforms in the Middle East.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {useCases.map((useCase, i) => (
            <div 
              key={i} 
              className="p-12 rounded-[2.5rem] border border-white/5 bg-gradient-to-br from-white/[0.02] to-transparent hover:border-cyan-500/30 hover:bg-cyan-500/[0.02] transition-all duration-700 ease-out group relative overflow-hidden animate-in fade-in slide-in-from-bottom-12 duration-1000 fill-mode-both hover:-translate-y-2 hover:shadow-[0_20px_40px_rgba(6,182,212,0.05)]"
              style={{ animationDelay: `${200 + i * 100}ms` }}
            >
              <div className="absolute top-0 right-0 w-40 h-40 bg-cyan-500/5 blur-3xl group-hover:bg-cyan-500/15 transition-colors duration-1000"></div>
              
              <useCase.icon className="w-12 h-12 text-cyan-500 mb-10 transition-transform duration-700 ease-out group-hover:scale-110 group-hover:-rotate-6 drop-shadow-[0_0_15px_rgba(6,182,212,0.3)]" />
              <h4 className="text-3xl font-black text-white mb-5 tracking-tight">{useCase.title}</h4>
              <p className="text-slate-400 leading-relaxed font-light text-xl">
                {useCase.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

```