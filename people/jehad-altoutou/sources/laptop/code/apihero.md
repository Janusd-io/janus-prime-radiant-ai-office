---
type: source
source_type: laptop
title: ApiHero
slug: apihero
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiHero.tsx
original_size: 5086
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# ApiHero

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiHero.tsx` on 2026-05-14._

```tsx
'use client';

import { ArrowRight, Code2, Rocket, Terminal, Sparkles, ChevronRight } from 'lucide-react';
import Image from 'next/image';
import { clsx } from 'clsx';

export default function ApiHero() {
  return (
    <section className="relative min-h-screen flex items-center pt-32 pb-20 overflow-hidden bg-[#050505]">
      {/* Dynamic Background */}
      <div className="absolute inset-0 z-0">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[800px] bg-cyan-500/10 blur-[150px] rounded-full opacity-50"></div>
        <div className="absolute top-1/4 right-0 w-[500px] h-[500px] bg-blue-600/5 blur-[120px] rounded-full"></div>
        <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-[0.02] pointer-events-none"></div>
        {/* Grid Pattern */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff05_1px,transparent_1px),linear-gradient(to_bottom,#ffffff05_1px,transparent_1px)] bg-[size:40px_40px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>
      </div>

      <div className="container mx-auto px-4 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          
          {/* Left Content */}
          <div className="text-left space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-1000">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold tracking-widest uppercase">
              <Sparkles className="w-3.5 h-3.5" />
              v3.0 Enterprise Engine
            </div>
            
            <h1 className="font-heading text-6xl md:text-8xl font-black tracking-tighter leading-[0.95] text-white">
              The Official <br />
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">Dubai Real Estate</span> <br />
              Data Layer.
            </h1>
            
            <p className="text-xl md:text-2xl text-slate-400 max-w-2xl leading-relaxed font-light">
              Access 2,700+ off-plan projects and unbranded high-fidelity assets through a single, lightning-fast integration.
            </p>
            
            <div className="flex flex-col sm:flex-row items-center gap-5 pt-4">
              <a 
                href="/real-estate-api/documentation" 
                className="w-full sm:w-auto px-10 py-5 bg-cyan-500 text-black rounded-2xl font-black text-lg hover:bg-cyan-400 transition-all flex items-center justify-center gap-3 shadow-[0_0_40px_-10px_rgba(6,182,212,0.5)] group"
              >
                View Documentation
                <ChevronRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </a>
              <a 
                href="https://rapidapi.com/happylife/api/dubai-real-estate-off-plan-projects-api-1" 
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto px-10 py-5 bg-white/5 text-white border border-white/10 rounded-2xl font-bold text-lg hover:bg-white/10 transition-all flex items-center justify-center gap-3 group"
              >
                Playground
                <Terminal className="w-5 h-5 text-cyan-400 group-hover:rotate-12 transition-transform" />
              </a>
            </div>

            <div className="flex flex-wrap gap-8 pt-8">
              {[
                { label: "Uptime", value: "99.9%", color: "text-emerald-400" },
                { label: "Latency", value: "<500ms", color: "text-cyan-400" },
                { label: "Updates", value: "Real-time", color: "text-blue-400" }
              ].map((stat, i) => (
                <div key={i} className="space-y-1">
                  <div className="text-[10px] uppercase tracking-widest text-slate-500 font-bold">{stat.label}</div>
                  <div className={clsx("text-2xl font-black font-heading", stat.color)}>{stat.value}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Right Visual Asset */}
          <div className="relative">
            <div className="relative animate-in zoom-in-95 duration-1000 delay-300">
              {/* Glow Behind */}
              <div className="absolute -inset-20 bg-cyan-500/20 blur-[120px] rounded-full"></div>
              
              {/* Borderless Image Container */}
              <div className="relative group lg:scale-110 transition-transform duration-700">
                <Image 
                  src="/api-dashboard-preview.png"
                  alt="Dubai Property API Visualization"
                  width={1600}
                  height={1600}
                  className="w-full h-auto drop-shadow-[0_0_50px_rgba(6,182,212,0.15)] transition-transform duration-1000 group-hover:scale-[1.02]"
                />
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

```