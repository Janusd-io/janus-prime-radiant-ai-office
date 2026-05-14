---
type: source
source_type: laptop
title: ApiCodeSnippet
slug: apicodesnippet
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiCodeSnippet.tsx
original_size: 6486
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# ApiCodeSnippet

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/ApiCodeSnippet.tsx` on 2026-05-14._

```tsx
'use client';

import { Copy, Terminal, Check, Globe, Code2 } from 'lucide-react';
import { useState } from 'react';

const codeContent = `{
  "status": "success",
  "data": {
    "project_id": "DXB-OP-8821",
    "name": "Azure Towers Dubai",
    "developer": {
      "id": "Emaar",
      "name": "Emaar Properties PJSC"
    },
    "location": {
      "district_id": 54,
      "address": "Dubai Marina"
    },
    "starting_price": 7850000,
    "currency": "AED",
    "units": [
      {
        "type": "2BR Apartment",
        "availability": "Selling Fast"
      }
    ],
    "assets": {
      "brochure_url": "https://api.dubaipropertyleads.ae/v1/proxy/image?url=...",
      "floor_plan_url": "https://api.dubaipropertyleads.ae/v1/proxy/image?url=..."
    }
  }
}`;

export default function ApiCodeSnippet() {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(codeContent);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <section className="py-32 bg-[#050505]">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
          
          <div className="flex-1 space-y-10 animate-in fade-in slide-in-from-bottom-8 duration-1000 ease-out">
            <div className="space-y-4">
              <h2 className="text-sm font-bold text-cyan-500 uppercase tracking-[0.4em]">Developer Experience</h2>
              <h3 className="text-4xl md:text-6xl font-black font-heading text-white tracking-tight leading-[1.1]">
                Ready in <span className="text-slate-500">60 Seconds.</span>
              </h3>
            </div>
            
            <p className="text-slate-400 text-xl leading-relaxed font-light font-sans max-w-xl">
              Don't waste time parsing PDFs. Our engine delivers structured, production-ready JSON data directly to your application layers.
            </p>
            
            <div className="space-y-8 pt-4">
              {[
                { icon: Globe, text: "Global Asset Content Delivery Network (CDN)" },
                { icon: Code2, text: "Type-safe JSON schemas and error handling" },
                { icon: Check, text: "Automated daily project catalog sync" }
              ].map((item, i) => (
                <div key={i} className="flex items-center gap-5 text-slate-300">
                  <div className="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400 shrink-0">
                    <item.icon className="w-6 h-6" />
                  </div>
                  <span className="text-lg font-light tracking-wide">{item.text}</span>
                </div>
              ))}
            </div>

            <div className="pt-8">
              <a 
                href="https://rapidapi.com/happylife/api/dubai-real-estate-off-plan-projects-api-1"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-3 px-8 py-4 bg-white/5 border border-white/10 rounded-2xl font-bold text-white hover:bg-white/10 transition-all text-sm tracking-wider uppercase group"
              >
                Open RapidAPI Playground
                <Terminal className="w-4 h-4 text-cyan-400 group-hover:translate-x-1 transition-transform" />
              </a>
            </div>
          </div>

          <div className="relative animate-in fade-in slide-in-from-right-10 duration-1000 ease-out delay-300">
            {/* Glow Effect */}
            <div className="absolute -inset-10 bg-cyan-500/20 blur-[100px] rounded-full pointer-events-none"></div>
            
            {/* Lighter Glassmorphism Window */}
            <div className="relative rounded-[2rem] border border-white/20 bg-white/5 backdrop-blur-2xl shadow-2xl shadow-cyan-900/20 overflow-hidden group">
              {/* MacOS Style Header */}
              <div className="bg-white/5 px-6 py-5 flex items-center justify-between border-b border-white/10">
                <div className="flex gap-2.5">
                  <div className="w-3.5 h-3.5 rounded-full bg-[#ff5f56] border border-black/10"></div>
                  <div className="w-3.5 h-3.5 rounded-full bg-[#ffbd2e] border border-black/10"></div>
                  <div className="w-3.5 h-3.5 rounded-full bg-[#27c93f] border border-black/10"></div>
                </div>
                <div className="text-[11px] font-mono text-cyan-100/60 uppercase tracking-[0.2em] font-medium bg-black/20 px-3 py-1 rounded-full">
                  GET /v1/projects/DXB-OP-8821
                </div>
                <button 
                  onClick={copyToClipboard}
                  className="text-slate-300 hover:text-white transition-all flex items-center gap-2 bg-white/5 hover:bg-white/10 px-3 py-1.5 rounded-lg"
                >
                  <span className="text-[10px] uppercase font-bold tracking-widest">{copied ? 'COPIED!' : 'COPY'}</span>
                  {copied ? <Check className="w-3.5 h-3.5 text-cyan-400" /> : <Copy className="w-3.5 h-3.5" />}
                </button>
              </div>
              
              <div className="p-8 overflow-x-auto custom-scrollbar">
                <pre className="font-mono text-[14px] leading-loose">
                  <code className="text-white">
                    {codeContent.split('\n').map((line, i) => {
                      const highlighted = line
                        .replace(/"(\w+)":/g, '<span class="text-cyan-200 opacity-80">"$1"</span>:')
                        .replace(/"([^"]+)"/g, '<span class="text-blue-200">"$1"</span>')
                        .replace(/\b(\d+)\b/g, '<span class="text-emerald-300">$1</span>')
                        .replace(/[{}[\]]/g, '<span class="text-white/60">$&</span>');
                      
                      return (
                        <div key={i} className="flex gap-6 hover:bg-white/5 transition-colors -mx-4 px-4 rounded">
                          <span className="text-white/20 select-none w-6 text-right font-mono">{i + 1}</span>
                          <span dangerouslySetInnerHTML={{ __html: highlighted }} />
                        </div>
                      );
                    })}
                  </code>
                </pre>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}

```