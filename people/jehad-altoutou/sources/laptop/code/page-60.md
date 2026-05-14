---
type: source
source_type: laptop
title: Desktop Captures — page
slug: page-60
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/dubai-property-leads-database/page.tsx
original_size: 5607
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

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/dubai-property-leads-database/page.tsx` on 2026-05-14._

```tsx
import SEOPageLayout from '@/components/SEOPageLayout';
import { Metadata } from 'next';
import { Database, Search, ShieldCheck, Download } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Dubai Property Leads Database | Verified Real Estate Leads',
  description: 'Access the most comprehensive Dubai property leads database. Download verified real estate enquiries from high-intent buyers and international investors.',
};

export default function DubaiPropertyLeadsDatabase() {
  return (
    <SEOPageLayout
      title="The Ultimate Dubai Property Leads Database"
      subtitle="Instantly access our verified database of high-intent property buyers, investors, and end-users looking for Dubai real estate."
      content={
        <div className="not-prose mt-12 mb-16 space-y-24">
          
          {/* Main Hero Hook */}
          <div className="text-center max-w-3xl mx-auto">
            <h2 className="text-3xl md:text-5xl font-extrabold text-slate-900 mb-6 font-heading tracking-tight">
              Scale Your Agency With A <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-indigo-600">Verified Leads Database</span>
            </h2>
            <p className="text-xl text-slate-600 leading-relaxed font-medium">
              Sourcing your own leads takes time and burns through marketing budgets. By tapping into our continuously updated Dubai property leads database, your team can start closing deals today instead of waiting for campaigns to optimize.
            </p>
          </div>

          {/* Value Proposition Grid */}
          <div className="grid md:grid-cols-2 gap-8">
            {/* Card 1 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-blue-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-blue-700 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-blue-500/25">
                <Database className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-blue-700 transition-colors">
                Unmatched Database Depth
               </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                Our Dubai property leads database isn't just a list of cold numbers. It contains rich profiles covering exact budgets, preferred areas (like Downtown or Palm Jumeirah), and timelines—giving your brokers the perfect conversation starter.
              </p>
            </div>

            {/* Card 2 */}
            <div className="bg-white rounded-3xl p-8 md:p-10 shadow-[0_8px_30px_rgb(0,0,0,0.04)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.08)] transition-all duration-300 border border-slate-100 group relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-50 rounded-bl-full -z-10 transition-transform group-hover:scale-110"></div>
              <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-indigo-700 text-white rounded-2xl flex items-center justify-center mb-8 shadow-lg shadow-indigo-500/25">
                <ShieldCheck className="w-7 h-7" />
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-4 font-heading group-hover:text-indigo-700 transition-colors">
                Manually Verified Profiles
              </h3>
              <p className="text-slate-600 leading-relaxed text-lg">
                We scrub our real estate databases daily. Any duplicate contacts, fake numbers, or unresponsive profiles are filtered out. You are paying for a premium database of active property buyers in the UAE.
              </p>
            </div>
          </div>

          {/* Stats Bar / Extra Trust Indicators */}
          <div className="bg-slate-900 rounded-3xl p-8 md:p-12 text-center md:text-left flex flex-col md:flex-row items-center justify-between gap-8 shadow-2xl overflow-hidden relative">
            <div className="absolute top-0 right-0 w-full h-full bg-[radial-gradient(circle_at_top_right,_var(--tw-gradient-stops))] from-blue-900/40 via-transparent to-transparent"></div>
            
            <div className="relative z-10 max-w-xl">
              <h3 className="text-2xl md:text-3xl font-bold text-white mb-4">Export Direct to Your CRM</h3>
              <p className="text-slate-300 text-lg">Download your allocation from our lead database securely. CSV and API integrations ensure your floor is calling within minutes.</p>
            </div>
            
            <div className="flex flex-wrap justify-center gap-6 relative z-10">
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <Search className="w-6 h-6 text-blue-400" />
                 <span className="text-white font-medium">Hyper-Targeted</span>
               </div>
               <div className="flex items-center gap-3 bg-white/10 backdrop-blur-md px-5 py-3 rounded-2xl border border-white/10">
                 <Download className="w-6 h-6 text-indigo-400" />
                 <span className="text-white font-medium">Instant Export</span>
               </div>
            </div>
          </div>

        </div>
      }
    />
  );
}

```