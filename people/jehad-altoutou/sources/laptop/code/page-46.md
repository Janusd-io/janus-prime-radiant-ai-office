---
type: source
source_type: laptop
title: page
slug: page-46
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/real-estate-api/documentation/page.tsx
original_size: 16461
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

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/real-estate-api/documentation/page.tsx` on 2026-05-14._

```tsx
import { Metadata } from 'next';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import { Book, Shield, Zap, Terminal, Copy, List, Layers, Code2 } from 'lucide-react';

export const metadata: Metadata = {
  title: "Technical Documentation | Dubai Real Estate API Platform",
  description: "Official API documentation for Dubai off-plan real estate data. Integrate project feeds, floor plans, and developer data in minutes.",
};

const navigation = [
  { group: "Concepts", items: [
    { title: "Introduction", href: "#introduction" },
    { title: "Authentication", href: "#authentication" }
  ]},
  { group: "Endpoints", items: [
    { title: "List Projects", href: "#v1-projects" },
    { title: "Project Details", href: "#v1-projects-id" },
    { title: "Developers", href: "#v1-developers" },
    { title: "Districts", href: "#v1-districts" },
    { title: "Image Proxy", href: "#v1-proxy-image" }
  ]}
];

export default function DocPage() {
  return (
    <main className="min-h-screen bg-[#050505]">
      <Navbar />
      
      <div className="pt-32 pb-24 container mx-auto px-4">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-16">
          
          {/* Enhanced Sticky Sidebar */}
          <aside className="hidden lg:col-span-3 lg:block">
            <div className="sticky top-32 space-y-12 animate-in fade-in slide-in-from-left-8 duration-1000 ease-out">
              <div className="p-8 rounded-[2rem] bg-white/[0.02] border border-white/5 space-y-10 shadow-2xl backdrop-blur-xl">
                {navigation.map((group, i) => (
                  <div key={i}>
                    <h4 className="text-[11px] font-black text-cyan-500 uppercase tracking-[0.3em] mb-6">{group.group}</h4>
                    <ul className="space-y-5 border-l border-white/5 pl-5">
                      {group.items.map((item, j) => (
                        <li key={j}>
                          <a href={item.href} className="text-sm font-medium text-slate-400 hover:text-cyan-400 hover:translate-x-1 transition-all block">
                            {item.title}
                          </a>
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
              </div>
              
              <div className="p-6 rounded-3xl border border-cyan-500/10 bg-cyan-500/[0.02] flex items-center gap-4 hover:bg-cyan-500/[0.05] transition-colors group cursor-pointer">
                <div className="w-12 h-12 rounded-2xl bg-cyan-500/10 flex items-center justify-center text-cyan-500 group-hover:scale-110 transition-transform">
                  <Terminal className="w-5 h-5" />
                </div>
                <div>
                  <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Need help?</div>
                  <a href="mailto:dubaipropertylead@gmail.com" className="text-[13px] font-bold text-white group-hover:text-cyan-400 transition-colors tracking-wide">Contact Support</a>
                </div>
              </div>
            </div>
          </aside>

          {/* Premium Content Area */}
          <div className="lg:col-span-9 space-y-32 max-w-4xl pb-20">
            
            {/* Header section */}
            <div className="relative p-16 rounded-[3rem] bg-gradient-to-br from-white/[0.03] to-transparent border border-white/5 overflow-hidden animate-in fade-in slide-in-from-bottom-8 duration-1000 ease-out">
              <div className="absolute top-0 right-0 w-80 h-80 bg-cyan-500/10 blur-[120px] rounded-full -mr-32 -mt-32"></div>
              <div className="relative z-10">
                <div className="flex items-center gap-3 text-cyan-500 mb-8">
                  <Code2 className="w-8 h-8" />
                  <span className="font-bold uppercase tracking-[0.4em] text-sm">Official API v1.0</span>
                </div>
                <h1 className="text-5xl md:text-7xl font-black font-heading text-white mb-8 tracking-tighter">Documentation</h1>
                <p className="text-2xl text-slate-400 font-light leading-relaxed max-w-2xl">
                  Build the next generation of PropTech with the most accurate Dubai real estate data feed.
                </p>
              </div>
            </div>

            {/* Introduction Section */}
            <section id="introduction" className="space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-1000 delay-150 ease-out fill-mode-both">
              <div className="flex items-center gap-4 mb-6">
                <div className="h-0.5 w-12 bg-cyan-500"></div>
                <h2 className="text-3xl font-black text-white tracking-tight">Introduction</h2>
              </div>
              <p className="text-xl text-slate-400 leading-relaxed font-light">
                Our platform provides a RESTful architecture for querying refined off-plan project data. We bridge the gap between complex developer databases and your high-performance frontend applications by merging data from top platforms like GenieMap and ReellyAI into a single, unified structure.
              </p>
            </section>

            {/* Authentication Section */}
            <section id="authentication" className="animate-in fade-in slide-in-from-bottom-8 duration-1000 delay-300 ease-out fill-mode-both">
              <div className="flex items-center gap-4 mb-8">
                <div className="h-0.5 w-12 bg-blue-500"></div>
                <h2 className="text-3xl font-black text-white tracking-tight">Authentication</h2>
              </div>
              <p className="text-lg text-slate-400 leading-relaxed font-light mb-10">
                Secure access is handled via Headers. You must provide your API Key with every request.
              </p>
              
              {/* Lighter Glassmorphism Window */}
              <div className="rounded-[2rem] border border-white/20 bg-white/5 backdrop-blur-2xl shadow-2xl shadow-blue-900/10 overflow-hidden group">
                <div className="bg-white/5 px-6 py-4 flex items-center gap-3 border-b border-white/10 text-slate-200 font-bold uppercase tracking-widest text-[10px]">
                   <Shield className="w-4 h-4 text-cyan-400" /> Security Headers
                </div>
                <div className="p-8 font-mono text-sm leading-loose">
                  <div className="flex gap-6">
                     <span className="text-white/20 select-none w-6 text-right font-mono">1</span>
                     <div><span className="text-rose-300">X-API-Key</span><span className="text-slate-400">: </span><span className="text-cyan-200">"sk_live_YOUR_KEY"</span></div>
                  </div>
                </div>
              </div>
            </section>

            <div className="h-px bg-gradient-to-r from-transparent via-white/10 to-transparent my-16"></div>

            {/* Endpoints Documentation */}
            <div className="space-y-32">
              
              <section id="v1-projects" className="space-y-10">
                <div className="flex items-center gap-3 mb-4">
                  <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-lg text-xs font-black uppercase tracking-widest">GET</span>
                  <code className="text-white text-2xl font-mono">/v1/projects</code>
                </div>
                <h2 className="text-3xl font-black text-white tracking-tight">List Projects</h2>
                <p className="text-lg text-slate-400 font-light leading-relaxed">
                  Returns a paginated list of all off-plan projects currently in the database. Supports filtering by source, name, and district.
                </p>

                <div className="rounded-2xl border border-white/10 bg-white/[0.02] overflow-hidden">
                  <table className="w-full text-left">
                    <thead>
                      <tr className="border-b border-white/5 text-[11px] uppercase tracking-widest text-slate-500 bg-white/[0.02]">
                        <th className="px-8 py-5">Parameter</th>
                        <th className="px-8 py-5">Type</th>
                        <th className="px-8 py-5">Description</th>
                      </tr>
                    </thead>
                    <tbody className="text-sm font-light">
                      <tr className="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td className="px-8 py-5 font-mono text-cyan-400 font-medium">limit</td>
                        <td className="px-8 py-5 text-slate-500">int (default 50)</td>
                        <td className="px-8 py-5 text-slate-300">Items per page.</td>
                      </tr>
                      <tr className="border-b border-white/5 hover:bg-white/[0.02] transition-colors">
                        <td className="px-8 py-5 font-mono text-cyan-400 font-medium">source</td>
                        <td className="px-8 py-5 text-slate-500">string</td>
                        <td className="px-8 py-5 text-slate-300">Filter by data source (e.g. 'geniemap', 'reelly').</td>
                      </tr>
                      <tr className="hover:bg-white/[0.02] transition-colors">
                        <td className="px-8 py-5 font-mono text-cyan-400 font-medium">q</td>
                        <td className="px-8 py-5 text-slate-500">string</td>
                        <td className="px-8 py-5 text-slate-300">Fuzzy search query on project name.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </section>

              <section id="v1-projects-id" className="space-y-10">
                <div className="flex items-center gap-3 mb-4">
                  <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-lg text-xs font-black uppercase tracking-widest">GET</span>
                  <code className="text-white text-2xl font-mono">/v1/projects/{"{id}"}</code>
                </div>
                <h2 className="text-3xl font-black text-white tracking-tight">Project Details</h2>
                <p className="text-lg text-slate-400 font-light leading-relaxed">
                  Returns a <strong>Unified Project Object</strong> regardless of the data source. Includes floor plans, rewritten proxy image urls, pricing, and developer details.
                </p>
                <div className="rounded-[2rem] border border-white/20 bg-white/5 backdrop-blur-2xl shadow-2xl overflow-hidden">
                  <div className="bg-white/5 px-6 py-4 border-b border-white/10 text-cyan-100/60 uppercase tracking-[0.2em] font-medium text-[11px] font-mono">Response Payload</div>
                  <div className="p-8 overflow-x-auto custom-scrollbar font-mono text-sm leading-loose">
                    <pre><code className="text-white">
{`{
  "id": "123",
  "source": "reelly",
  "name": "Luxury Tower",
  "location": {
    "lat": 25.123,
    "lng": 55.123,
    "address": "Downtown Dubai"
  },
  "cover_image": "https://api.dubaipropertyleads.ae/v1/proxy/image?...",
  "floor_plans": [...],
  "price": { "from": 1500000, "currency": "AED" },
  "developer": { "name": "Emaar", "logo": "..." }
}`}
                    </code></pre>
                  </div>
                </div>
              </section>

              <section id="v1-developers" className="space-y-10">
                <div className="flex items-center gap-3 mb-4">
                  <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-lg text-xs font-black uppercase tracking-widest">GET</span>
                  <code className="text-white text-2xl font-mono">/v1/developers</code>
                </div>
                <h2 className="text-3xl font-black text-white tracking-tight">List Developers</h2>
                <p className="text-lg text-slate-400 font-light leading-relaxed">
                  Fetch a paginated list of all real estate developers. Data is cleaned and deduplicated from multiple sources.
                </p>
                <div className="rounded-[2rem] border border-white/20 bg-white/5 backdrop-blur-2xl overflow-hidden">
                  <div className="bg-white/5 px-6 py-4 flex items-center gap-3 border-b border-white/10 text-slate-200 font-bold uppercase tracking-widest text-[10px]">
                     Example Request
                  </div>
                  <div className="p-8 font-mono text-sm leading-loose">
                    <div className="flex gap-6">
                       <span className="text-white/20 select-none w-6 text-right font-mono">1</span>
                       <div><span className="text-cyan-200">curl</span> <span className="text-blue-300">"https://api.dubaipropertyleads.ae/v1/developers?q=emaar&limit=10"</span></div>
                    </div>
                  </div>
                </div>
              </section>

              <section id="v1-districts" className="space-y-10">
                <div className="flex items-center gap-3 mb-4">
                  <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-lg text-xs font-black uppercase tracking-widest">GET</span>
                  <code className="text-white text-2xl font-mono">/v1/districts</code>
                </div>
                <h2 className="text-3xl font-black text-white tracking-tight">List Districts</h2>
                <p className="text-lg text-slate-400 font-light leading-relaxed">
                  Retrieve standard area and district mappings used across all project locations.
                </p>
              </section>

              <section id="v1-proxy-image" className="space-y-10">
                <div className="flex items-center gap-3 mb-4">
                  <span className="px-3 py-1 bg-emerald-500/20 text-emerald-400 rounded-lg text-xs font-black uppercase tracking-widest">GET</span>
                  <code className="text-white text-2xl font-mono">/v1/proxy/image</code>
                </div>
                <h2 className="text-3xl font-black text-white tracking-tight">White-Label Image Proxy</h2>
                <p className="text-lg text-slate-400 font-light leading-relaxed">
                  All external assets (brochures, floor plans, cover images) returned in project details use this proxy endpoint. It prevents hotlinking issues and obfuscates the original data source.
                </p>
              </section>

            </div>

            {/* CTA Final */}
            <section className="pt-32">
               <div className="p-20 rounded-[3.5rem] bg-gradient-to-br from-cyan-600 to-blue-700 relative overflow-hidden group hover:scale-[1.02] transition-transform duration-700">
                 <div className="relative z-10 text-center space-y-10">
                   <Terminal className="w-20 h-20 text-white mb-2 mx-auto transition-transform duration-1000 group-hover:scale-110 group-hover:rotate-12" />
                   <h3 className="text-5xl md:text-7xl font-black text-white tracking-tighter">Ship in Records.</h3>
                   <p className="text-white/90 text-2xl font-light max-w-2xl mx-auto leading-relaxed">
                     Don't wait for internal reviews. Start testing the API live in our playground immediately.
                   </p>
                   <a 
                     href="https://rapidapi.com/happylife/api/dubai-real-estate-off-plan-projects-api-1"
                     target="_blank"
                     rel="noopener noreferrer"
                     className="inline-flex items-center gap-4 px-14 py-6 bg-white text-black rounded-full font-black text-xl hover:bg-slate-100 transition-all shadow-[0_20px_50px_rgba(0,0,0,0.3)] hover:shadow-[0_20px_60px_rgba(0,0,0,0.4)]"
                   >
                     Launch Playground
                   </a>
                 </div>
                 {/* Visual Effects */}
                 <div className="absolute top-0 right-0 w-96 h-96 bg-white/20 blur-[120px] rounded-full -mr-40 -mt-40 transition-transform duration-1000 group-hover:scale-150"></div>
                 <div className="absolute bottom-0 left-0 w-96 h-96 bg-black/20 blur-[120px] rounded-full -ml-40 -mb-40 transition-transform duration-1000 group-hover:scale-150"></div>
               </div>
            </section>

          </div>
        </div>
      </div>

      <Footer />
    </main>
  );
}

```