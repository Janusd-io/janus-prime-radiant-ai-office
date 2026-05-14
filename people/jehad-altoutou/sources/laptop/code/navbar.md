---
type: source
source_type: laptop
title: Navbar
slug: navbar
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/Navbar.tsx
original_size: 3033
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# Navbar

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/Navbar.tsx` on 2026-05-14._

```tsx
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Rocket, Terminal } from 'lucide-react';
import { clsx } from 'clsx';

export default function Navbar() {
  const pathname = usePathname();
  const isApiPage = pathname?.startsWith('/real-estate-api');

  return (
    <nav className={clsx(
      "fixed top-0 left-0 w-full z-50 transition-all duration-300 border-b",
      isApiPage 
        ? "bg-[#0a0c10]/80 backdrop-blur-xl border-white/5 text-white" 
        : "glass border-white/20 text-foreground"
    )}>
      <div className="container mx-auto px-4 h-20 flex items-center justify-between">
        <Link href="/" className="flex items-center gap-3 group">
          <img 
            src="/logo.png" 
            alt="Dubai Property Leads" 
            className={clsx(
              "h-10 w-auto object-contain transition-all duration-300",
              isApiPage ? "brightness-125" : "brightness-110"
            )}
            width={40}
            height={40}
          />
          <span className="text-2xl font-heading font-black tracking-tighter uppercase">
            DUBAI<span className={clsx("italic", isApiPage ? "text-cyan-400" : "text-primary")}>LEADS</span>
          </span>
        </Link>
        
        <div className="hidden md:flex items-center gap-8">
          <Link href="/#how-it-works" className="text-sm font-medium hover:text-cyan-400 transition-colors">How It Works</Link>
          <Link href="/#leads" className="text-sm font-medium hover:text-cyan-400 transition-colors">Lead Quality</Link>
          <Link href="/#pricing" className="text-sm font-medium hover:text-cyan-400 transition-colors">Pricing</Link>
          <Link 
            href="/real-estate-api" 
            className={clsx(
              "text-sm font-bold transition-all px-3 py-1 rounded-lg flex items-center gap-1.5",
              isApiPage 
                ? "text-cyan-400 bg-cyan-400/10" 
                : "text-foreground hover:text-primary"
            )}
          >
            <Terminal className="w-4 h-4" />
            Real Estate API
          </Link>
          <Link href="/about" className="text-sm font-medium hover:text-cyan-400 transition-colors">About Us</Link>
        </div>
        
        <div className="flex items-center gap-4">
          <Link 
            href={isApiPage ? "https://rapidapi.com/happylife/api/dubai-real-estate-off-plan-projects-api-1" : "#pricing"}
            target={isApiPage ? "_blank" : undefined}
            className={clsx(
              "px-5 py-2.5 rounded-full font-bold text-sm transition-all flex items-center gap-2 shadow-lg",
              isApiPage 
                ? "bg-cyan-500 text-black hover:bg-cyan-400 shadow-cyan-500/20" 
                : "bg-primary text-white hover:bg-blue-700 shadow-blue-500/10"
            )}
          >
            {isApiPage ? 'API Playground' : 'Get Leads'}
            <Rocket className="w-4 h-4" />
          </Link>
        </div>
      </div>
    </nav>
  );
}

```