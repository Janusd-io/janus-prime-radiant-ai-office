---
type: source
source_type: laptop
title: page
slug: page-45
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/real-estate-api/page.tsx
original_size: 4742
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

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/real-estate-api/page.tsx` on 2026-05-14._

```tsx
import { Metadata } from 'next';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import ApiHero from '@/components/ApiHero';
import ApiFeatures from '@/components/ApiFeatures';
import ApiCodeSnippet from '@/components/ApiCodeSnippet';
import ApiUseCases from '@/components/ApiUseCases';
import ApiFAQ from '@/components/ApiFAQ';
import { Mail, ArrowRight } from 'lucide-react';

export const metadata: Metadata = {
  title: "Premium Dubai Real Estate API | Enterprise Off-Plan Data Platform",
  description: "The official developer data layer for Dubai real estate. Access 2,700+ projects, prices, and assets via one unified API. Engineered for PropTech leaders.",
  keywords: [
    "Dubai Real Estate API",
    "Off-plan property data",
    "Developer real estate integration",
    "Premium Dubai Property API",
    "Official Dubai Property Leads API"
  ],
  openGraph: {
    title: "Dubai Real Estate Off-Plan Projects API Platform",
    description: "Official real estate data layer for Developers and Proptech platforms. 2,700+ projects via one unified JSON API.",
    images: [{ url: '/api-dashboard-preview.png' }]
  }
};

export default function ApiLandingPage() {
  return (
    <main className="min-h-screen bg-[#050505]">
      <Navbar />
      
      {/* Redesigned Premium Sections */}
      <ApiHero />
      
      <ApiFeatures />
      
      <ApiCodeSnippet />
      
      <ApiUseCases />
      
      <ApiFAQ />

      {/* Enterprise CTA Section - Redesigned for Premium DX */}
      <section className="py-32 bg-[#050505] relative overflow-hidden animate-in fade-in slide-in-from-bottom-12 duration-1000 ease-out fill-mode-both">
        <div className="container mx-auto px-4 text-center">
          <div className="max-w-5xl mx-auto rounded-[3.5rem] bg-gradient-to-br from-[#0a0c10] to-[#050505] border border-white/10 p-12 md:p-24 relative overflow-hidden group hover:border-cyan-500/20 transition-colors duration-1000">
            {/* Background Glows */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-cyan-500/10 blur-[120px] rounded-full -mr-48 -mt-48 transition-all duration-1000 ease-out group-hover:bg-cyan-500/20 group-hover:scale-110"></div>
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-600/10 blur-[120px] rounded-full -ml-48 -mb-48 opacity-50 transition-all duration-1000 ease-out group-hover:scale-110"></div>
            
            <div className="relative z-10 space-y-12">
              <h2 className="text-5xl md:text-8xl font-black font-heading text-white tracking-tighter leading-[1.1]">
                Scale Your <br />
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500 italic drop-shadow-[0_0_30px_rgba(6,182,212,0.3)]">Vision.</span>
              </h2>
              
              <p className="text-xl md:text-2xl text-slate-400 max-w-2xl mx-auto leading-relaxed font-light">
                Need custom rate limits, private CDN edge cases, or dedicated engineering support? Our Enterprise team is ready to help you scale.
              </p>
              
              <div className="flex flex-col sm:flex-row items-center justify-center gap-6 pt-8">
                <a 
                  href="mailto:dubaipropertylead@gmail.com" 
                  className="w-full sm:w-auto px-12 py-5 bg-white text-black rounded-2xl font-black text-xl hover:scale-[1.03] active:scale-[0.98] transition-all duration-500 ease-out flex items-center justify-center gap-4 shadow-[0_20px_50px_rgba(255,255,255,0.1)] hover:shadow-[0_20px_60px_rgba(255,255,255,0.2)]"
                >
                  <Mail className="w-6 h-6" />
                  Contact Sales
                </a>
                <a 
                  href="https://rapidapi.com/happylife/api/dubai-real-estate-off-plan-projects-api-1"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full sm:w-auto px-12 py-5 bg-cyan-500/5 text-cyan-400 border border-cyan-500/30 rounded-2xl font-bold text-xl hover:bg-cyan-500/10 transition-all duration-500 ease-out flex items-center justify-center gap-3 group/btn"
                >
                  Go to Playground
                  <ArrowRight className="w-6 h-6 group-hover/btn:translate-x-2 transition-transform duration-500 ease-out" />
                </a>
              </div>
              
              <div className="pt-16 text-slate-500 text-sm font-bold tracking-[0.2em] uppercase">
                Trusted by 50+ PropTech Platforms Globally
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}

```