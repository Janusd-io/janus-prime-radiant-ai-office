---
type: source
source_type: laptop
title: page
slug: page-61
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/dubai-investor-leads/page.tsx
original_size: 5553
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# page

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/dubai-investor-leads/page.tsx` on 2026-05-14._

```tsx
import SEOPageLayout from '@/components/SEOPageLayout';
import { Metadata } from 'next';
import { Globe, UserCheck, BarChart3, Users } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Dubai Investor Leads | Dubai Property Leads',
  description: 'Bridge the gap to global property investors. Premium Dubai real estate investor leads for serious agents.',
};

export default function DubaiInvestorLeads() {
  return (
    <SEOPageLayout
      title="Access Premium Dubai Investor Leads"
      subtitle="Exclusive high-net-worth buyer enquiries from over 40 nationalities, ready to invest in Dubai."
      content={
        <div className="not-prose mt-12 mb-16 space-y-24">
          
          {/* Main Hero Hook */}
          <div className="text-center max-w-3xl mx-auto">
            <h2 className="text-3xl md:text-5xl font-extrabold text-slate-900 mb-6 font-heading tracking-tight">
              Connecting with <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">Global Real Estate Investors</span>
            </h2>
            <p className="text-xl text-slate-600 leading-relaxed font-medium">
              Dubai remains one of the premier destinations for global capital. Our investor leads are sourced from a highly diverse base of nationalities, specifically targeting affluent buyers from the UK, India, Russia, Europe, and the broader GCC.
            </p>
          </div>

          {/* Value Proposition Grid */}
          <div className="grid md:grid-cols-2 gap-8">
            {/* Card 1 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-purple-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-purple-700 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-purple-500/25">
                <Globe className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-purple-700 transition-colors">
                Deep Investor Profiling
              </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                We don't just capture names. Our leads include detailed profiles of investor intent. We verify budget brackets, nationality, and exact property interests—distinguishing between buyers seeking luxury villas in Palm Jumeirah versus high-yield commercial apartments in Business Bay.
              </p>
            </div>

            {/* Card 2 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-pink-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-pink-500 to-rose-600 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-pink-500/25">
                <BarChart3 className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-pink-600 transition-colors">
                Massive Scalability
              </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                By purchasing bulk investor enquiries, growing brokerages can consistently fuel their entire sales floor. Our automated delivery architecture continuously supplies your team with fresh, high-intent international prospects to consult and convert.
              </p>
            </div>
          </div>

          {/* Stats Bar / Extra Trust Indicators */}
          <div className="bg-slate-900 rounded-3xl p-8 md:p-12 text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 shadow-2xl overflow-hidden relative">
            <div className="absolute top-0 right-0 w-full h-full bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-purple-900/40 via-transparent to-transparent"></div>
            
            <div className="relative z-10 max-w-xl">
              <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">Target Overseas Wealth</h3>
              <p className="text-slate-300 text-lg">Don't wait for international buyers to stumble upon your listings. Connect with global capital instantly.</p>
            </div>
            
            <div className="flex flex-wrap justify-center gap-6 relative z-10">
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <UserCheck className="w-6 h-6 text-purple-400" />
                 <span className="text-white font-medium">Verified Intent</span>
               </div>
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <Users className="w-6 h-6 text-pink-400" />
                 <span className="text-white font-medium">40+ Nationalities</span>
               </div>
            </div>
          </div>

        </div>
      }
    />
  );
}

```