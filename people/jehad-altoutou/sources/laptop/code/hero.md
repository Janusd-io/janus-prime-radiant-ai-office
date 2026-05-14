---
type: source
source_type: laptop
title: Hero
slug: hero
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/Hero.tsx
original_size: 9024
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# Hero

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/Hero.tsx` on 2026-05-14._

```tsx
'use client';

import { useEffect, useState } from 'react';
import { ArrowRight, CheckCircle2, Rocket } from 'lucide-react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export default function Hero() {
  const [buyerCount, setBuyerCount] = useState(0);

  useEffect(() => {
    // Generate random number between 150 and 2500 on mount
    const randomCount = Math.floor(Math.random() * (2500 - 150 + 1)) + 150;
    setBuyerCount(randomCount);
  }, []);

  return (
    <section className="relative overflow-hidden pt-20 pb-16 lg:pt-32 lg:pb-24 hero-gradient">
      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-4xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-100 text-blue-600 text-sm font-medium mb-6 animate-fade-in">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            Fresh buyer enquiries added today
          </div>
          
          <h1 className="font-heading text-4xl md:text-6xl lg:text-7xl font-bold tracking-tight mb-6 leading-tight">
            The #1 Source for Verified <span className="gradient-text">Dubai Property Leads</span>
          </h1>
          
          <p className="text-lg md:text-xl text-muted-foreground mb-10 max-w-2xl mx-auto">
            Exclusive investor and end-user enquiries delivered directly to real estate agents and brokerages. No cold calling. Just high-intent buyers.
          </p>
          
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a 
              href="#pricing" 
              className="w-full sm:w-auto px-8 py-4 bg-primary text-primary-foreground rounded-full font-semibold text-lg hover:bg-blue-700 transition-all flex items-center justify-center gap-2 shadow-lg shadow-blue-500/20"
            >
              Start Receiving Buyer Enquiries
              <ArrowRight className="w-5 h-5" />
            </a>
            <a 
              href="#leads" 
              className="w-full sm:w-auto px-8 py-4 bg-white text-foreground border border-border rounded-full font-semibold text-lg hover:bg-slate-50 transition-all"
            >
              View Lead Packages
            </a>
          </div>
          
          <div className="mt-12 flex flex-wrap justify-center gap-6 text-sm text-muted-foreground">
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-green-500" />
              Verified Phone Numbers
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-green-500" />
              Exclusive to You
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-green-500" />
              Instant Email Delivery
            </div>
          </div>
        </div>
      </div>
      
      {/* Visual representation of inquiries - Live Leads Feed */}
      <div className="mt-16 container mx-auto px-4 max-w-5xl">
        <div className="relative rounded-2xl border border-border bg-white shadow-2xl overflow-hidden">
          <div className="absolute inset-0 bg-grid-slate-100 [mask-image:linear-gradient(0deg,#fff,rgba(255,255,255,0.6))] -z-10"></div>
          
          <div className="bg-slate-50/80 border-b border-border p-4 flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="flex gap-1.5">
                <div className="w-2.5 h-2.5 rounded-full bg-red-400"></div>
                <div className="w-2.5 h-2.5 rounded-full bg-amber-400"></div>
                <div className="w-2.5 h-2.5 rounded-full bg-emerald-400"></div>
              </div>
              <div className="h-4 w-px bg-slate-300 mx-2"></div>
              <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Live Buyers Database v2.4</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-2 w-2 rounded-full bg-green-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
              </span>
              <span className="text-[10px] font-bold text-green-600 uppercase">Live Feed</span>
            </div>
          </div>

          <div className="p-6 md:p-8">
             <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {[
                  { name: "John D***", country: "GB", type: "3BR Villa", location: "Palm Jumeirah", budget: "12.5M - 15.0M", time: "2 mins ago" },
                  { name: "Ahmed K***", country: "AE", type: "Penthouse", location: "Downtown Dubai", budget: "8.2M - 10.5M", time: "14 mins ago" },
                  { name: "Svetlana P***", country: "RU", type: "Plot", location: "Dubai Hills Estate", budget: "25M+", time: "28 mins ago" },
                  { name: "Rajesh M***", country: "IN", type: "2BR Apt", location: "Business Bay", budget: "1.8M - 2.4M", time: "1 hour ago" }
                ].map((lead, i) => (
                  <div key={i} className={cn(
                    "group p-5 rounded-2xl border border-slate-100 bg-white hover:border-blue-200 hover:shadow-xl hover:shadow-blue-500/5 transition-all duration-300 flex flex-col gap-4",
                    i > 1 && "hidden md:flex"
                  )}>
                    <div className="flex justify-between items-start">
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-slate-400 border border-slate-200 group-hover:bg-blue-50 group-hover:text-blue-500 transition-colors">
                          <CheckCircle2 className="w-5 h-5" />
                        </div>
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="text-sm font-bold text-slate-900">{lead.name}</span>
                            <span className="text-[10px] px-1.5 py-0.5 bg-blue-50 text-blue-600 font-bold rounded uppercase">Verified</span>
                          </div>
                          <div className="flex items-center gap-1.5 mt-0.5">
                            <span className="text-[10px] text-muted-foreground uppercase font-medium">{lead.location}</span>
                          </div>
                        </div>
                      </div>
                      <span className="text-[10px] font-medium text-slate-400 italic">{lead.time}</span>
                    </div>

                    <div className="grid grid-cols-2 gap-4 py-3 border-y border-slate-50">
                      <div>
                        <div className="text-[9px] uppercase font-bold text-slate-400 tracking-wider">Interest</div>
                        <div className="text-xs font-bold text-slate-700 mt-0.5">{lead.type}</div>
                      </div>
                      <div>
                        <div className="text-[9px] uppercase font-bold text-slate-400 tracking-wider">Budget (AED)</div>
                        <div className="text-xs font-bold text-blue-600 mt-0.5">{lead.budget}</div>
                      </div>
                    </div>

                    <div className="flex items-center justify-between pt-1">
                      <div className="flex gap-1">
                        {[1, 2, 3, 4, 5].map(s => (
                          <div key={s} className="w-1.5 h-1.5 rounded-full bg-blue-100"></div>
                        ))}
                      </div>
                      <div className="text-[10px] font-bold text-slate-400 group-hover:text-blue-500 transition-colors uppercase flex items-center gap-1">
                        Lead Score: High <Rocket className="w-3 h-3" />
                      </div>
                    </div>
                  </div>
                ))}
             </div>
             
             <div className="mt-8 pt-6 border-t border-slate-100 flex items-center justify-center">
                <p className="text-sm text-muted-foreground flex items-center gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                  There are currently <span className="font-bold text-slate-900">{buyerCount || '...'} verified buyers</span> looking for property in Dubai
                </p>
             </div>
          </div>
        </div>
      </div>
    </section>
  );
}

```