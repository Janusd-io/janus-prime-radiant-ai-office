---
type: source
source_type: laptop
title: Pricing
slug: pricing
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/Pricing.tsx
original_size: 5866
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Pricing

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/Pricing.tsx` on 2026-05-14._

```tsx
'use client';

import { LEAD_PACKAGES } from '@/lib/stripe';
import { Check, Info, Rocket, ShieldCheck, Zap, Loader2 } from 'lucide-react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';
import { useState } from 'react';
import Toast from './Toast';

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export default function Pricing() {
  const [loading, setLoading] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handlePurchase = (packageName: string) => {
    const emailRecipient = 'dubaipropertylead@gmail.com';
    const subject = encodeURIComponent(`${packageName} Plan Purchase Enquiry`);
    const body = encodeURIComponent(
      `Hi Dubai Leads Team,\n\nI've been reviewing your verified property buyer lead packages and I'm interested in moving forward with the ${packageName} package.\n\nCould you please provide the available payment options and the next steps to activate my lead delivery?\n\nLooking forward to your reply.\n\nBest regards,`
    );
    
    window.location.href = `mailto:${emailRecipient}?subject=${subject}&body=${body}`;
  };

  return (
    <section id="pricing" className="py-24 bg-slate-50 relative overflow-hidden">
      {error && (
        <Toast 
          message={error} 
          type="error" 
          onClose={() => setError(null)} 
        />
      )}
      <div className="container mx-auto px-4">
        <div className="max-w-3xl mx-auto text-center mb-16">
          <h2 className="font-heading text-3xl md:text-5xl font-bold mb-4">Choose Your Growth Plan</h2>
          <p className="text-muted-foreground text-lg">
            High-intent leads delivered immediately to your inbox. 
            Select the package that fits your team's capacity.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 items-start">
          {LEAD_PACKAGES.map((pkg) => (
            <div 
              key={pkg.id}
              className={cn(
                "relative flex flex-col p-6 rounded-2xl border transition-all duration-300",
                pkg.popular 
                  ? "border-primary shadow-2xl shadow-blue-500/10 scale-105 lg:scale-110 z-10 bg-white" 
                  : "border-border hover:border-slate-300 bg-white"
              )}
            >
              {pkg.popular && (
                <div className="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 bg-primary text-white text-[10px] font-bold uppercase tracking-widest rounded-full shadow-lg">
                  Most Popular
                </div>
              )}

              <div className="mb-8">
                <h3 className="font-heading text-xl font-bold mb-2">{pkg.name}</h3>
                <div className="flex items-baseline gap-1 mb-1">
                  <span className="text-3xl font-bold">{pkg.isEnterprise ? 'Custom' : pkg.price.toLocaleString()}</span>
                  {!pkg.isEnterprise && <span className="text-sm font-semibold text-muted-foreground uppercase">AED</span>}
                </div>
                {!pkg.isEnterprise && (
                  <p className="text-sm text-primary font-semibold">
                    {pkg.pricePerLead} AED / lead
                  </p>
                )}
                <p className="text-xs text-muted-foreground mt-2 min-h-8">
                  {pkg.description}
                </p>
              </div>

              <div className="space-y-4 mb-8 flex-grow">
                <div className="flex items-start gap-3">
                  <div className="mt-1 flex-shrink-0 w-4 h-4 rounded-full bg-blue-50 flex items-center justify-center">
                    <Check className="w-3 h-3 text-primary" />
                  </div>
                  <span className="text-sm font-medium">
                    {pkg.isEnterprise ? '2,000+ Enquiries' : `${pkg.leads} Verified Enquiries`}
                  </span>
                </div>
                <div className="flex items-start gap-3">
                  <div className="mt-1 flex-shrink-0 w-4 h-4 rounded-full bg-blue-50 flex items-center justify-center">
                    <Zap className="w-3 h-3 text-primary" />
                  </div>
                  <span className="text-sm">Instant automation</span>
                </div>
                <div className="flex items-start gap-3">
                  <div className="mt-1 flex-shrink-0 w-4 h-4 rounded-full bg-blue-50 flex items-center justify-center">
                    <ShieldCheck className="w-3 h-3 text-primary" />
                  </div>
                  <span className="text-sm">Quality guarantee</span>
                </div>
              </div>

              <button 
                onClick={() => handlePurchase(pkg.name)}
                className={cn(
                  "w-full py-3 px-4 rounded-xl font-bold transition-all flex items-center justify-center gap-2",
                  pkg.popular 
                    ? "bg-primary text-white hover:bg-blue-700 shadow-lg shadow-blue-500/25" 
                    : "bg-secondary text-secondary-foreground hover:bg-slate-200"
                )}
              >
                {pkg.cta}
                <Rocket className="w-4 h-4" />
              </button>
            </div>
          ))}
        </div>
        
        <div className="mt-16 max-w-2xl mx-auto p-4 rounded-2xl bg-blue-50 border border-blue-100 flex gap-4">
          <Info className="w-6 h-6 text-primary flex-shrink-0 mt-0.5" />
          <p className="text-sm text-blue-900 leading-relaxed">
            <strong>Risk Reversal:</strong> If a lead contains invalid contact information, it will be replaced. 
            All enquiries are processed on a first-paid, first-fulfilled basis.
          </p>
        </div>
      </div>
    </section>
  );
}

```