---
type: source
source_type: laptop
title: TrustStats
slug: truststats
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/TrustStats.tsx
original_size: 2807
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# TrustStats

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/TrustStats.tsx` on 2026-05-14._

```tsx
import { Users, Building2, Globe, TrendingUp } from 'lucide-react';

const stats = [
  {
    label: 'Buyer enquiries generated',
    value: '12,000+',
    icon: Users,
  },
  {
    label: 'Active brokers on platform',
    value: '300+',
    icon: Building2,
  },
  {
    label: 'Buyer nationalities',
    value: '40+',
    icon: Globe,
  },
  {
    label: 'Generated last month',
    value: '2,500+',
    icon: TrendingUp,
  },
];

export default function TrustStats() {
  return (
    <section className="py-20 bg-muted/30">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 md:gap-12">
          {stats.map((stat, index) => (
            <div key={index} className="flex flex-col items-center text-center">
              <div className="w-12 h-12 rounded-2xl bg-white shadow-sm border border-border flex items-center justify-center text-primary mb-4">
                <stat.icon className="w-6 h-6" />
              </div>
              <div className="text-3xl md:text-4xl font-heading font-bold text-foreground mb-1">
                {stat.value}
              </div>
              <div className="text-sm text-muted-foreground font-medium">
                {stat.label}
              </div>
            </div>
          ))}
        </div>
        
        <div className="mt-24 border-t border-border pt-16 overflow-hidden">
          <h3 className="text-center text-sm font-semibold text-muted-foreground uppercase tracking-wider mb-12">
            Trusted by agents from leading brokerages
          </h3>
          <div className="relative marquee-mask">
            <div className="flex animate-marquee whitespace-nowrap items-center w-max">
              {/* Duplicate the list for seamless infinite loop */}
              {[...Array(2)].map((_, i) => (
                <div key={i} className="flex gap-x-12 pr-12 items-center opacity-40 grayscale hover:grayscale-0 transition-all duration-500">
                  {[
                    'FAM Properties', 
                    'Betterhomes', 
                    'Haus & Haus', 
                    'Allsopp & Allsopp', 
                    'Espace Real Estate', 
                    'Driven Properties', 
                    'D&B Properties', 
                    'Metropolitan', 
                    'Provident Estate',
                    'Knight Frank',
                    'DAMAC', 
                    'Select Group'
                  ].map((name) => (
                    <span key={name} className="text-xl md:text-2xl font-heading font-bold tracking-tight text-slate-400">
                      {name}
                    </span>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

```