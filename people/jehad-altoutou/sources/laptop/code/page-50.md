---
type: source
source_type: laptop
title: page
slug: page-50
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/off-plan-leads-dubai/page.tsx
original_size: 5811
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# page

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/off-plan-leads-dubai/page.tsx` on 2026-05-14._

```tsx
import SEOPageLayout from '@/components/SEOPageLayout';
import { Metadata } from 'next';
import { Building2, Gem, Target, TrendingUp, ShieldCheck, Zap } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Off-Plan Buyer Leads Dubai | Dubai Property Leads',
  description: 'Target high-intent off-plan investors in Dubai. Get exclusive buyer enquiries for the latest project launches.',
};

export default function OffPlanLeadsDubai() {
  return (
    <SEOPageLayout
      title="High-Intent Off-Plan Buyer Leads"
      subtitle="Connect with investors actively looking for the next big project launch in Dubai's off-plan market."
      content={
        <div className="not-prose mt-12 mb-16 space-y-24">
          
          {/* Main Hero Hook */}
          <div className="text-center max-w-3xl mx-auto">
            <h2 className="text-3xl md:text-5xl font-extrabold text-slate-900 mb-6 font-heading tracking-tight">
              Targeting <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">Off-Plan Investors</span> in Dubai
            </h2>
            <p className="text-xl text-slate-600 leading-relaxed font-medium">
              The off-plan sector is the absolute heartbeat of Dubai's real estate expansion. With weekly mega-project launches from master developers like <strong className="text-slate-800">Emaar, DAMAC, and Nakheel</strong>, international investors are aggressively hunting for the most lucrative entry points.
            </p>
          </div>

          {/* Value Proposition Grid */}
          <div className="grid md:grid-cols-2 gap-8">
            {/* Card 1 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-blue-700 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-blue-500/25">
                <Gem className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-blue-700 transition-colors">
                Why Off-Plan Leads are Highly Valuable
              </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                Off-plan buyers are sophisticated investors prioritizing massive capital appreciation and secured, high rental yields. Unlike secondary market buyers hampered by mortgages, off-plan investors are highly liquid and ready to execute immediately on launch day, generating massive commission multipliers for brokers.
              </p>
            </div>

            {/* Card 2 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-indigo-500/25">
                <Target className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-indigo-600 transition-colors">
                Our Pre-Launch Capture Strategy
              </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                We do not sell aged data. Our proprietary funnels capture intent <em className="text-slate-800 font-semibold italic">at the exact moment</em> a new project is teased. Our campaigns intercept international buyers actively researching specific Dubai developers, feeding your CRM exclusively with verified, hyper-fresh enquiries while demand is at absolute peak.
              </p>
            </div>
          </div>

          {/* Stats Bar / Extra Trust Indicators */}
          <div className="bg-slate-900 rounded-3xl p-8 md:p-12 text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 shadow-2xl overflow-hidden relative">
            <div className="absolute top-0 right-0 w-full h-full bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-blue-900/40 via-transparent to-transparent"></div>
            
            <div className="relative z-10 max-w-xl">
              <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">Ready to Dominate Launch Day?</h3>
              <p className="text-slate-300 text-lg">Stop competing for shared portal leads. Command the off-plan sector with exclusive international buyer data.</p>
            </div>
            
            <div className="flex flex-wrap justify-center gap-6 relative z-10">
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <ShieldCheck className="w-6 h-6 text-emerald-400" />
                 <span className="text-white font-medium">OTP Verified</span>
               </div>
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <Zap className="w-6 h-6 text-yellow-400" />
                 <span className="text-white font-medium">Instant Delivery</span>
               </div>
            </div>
          </div>

        </div>
      }
    />
  );
}

```