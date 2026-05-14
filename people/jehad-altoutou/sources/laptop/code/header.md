---
type: source
source_type: laptop
title: Desktop Captures — Header
slug: header
created: 2026-04-07
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Form Request/src/components/layout/Header.jsx
original_size: 1502
original_ext: .jsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# Header

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Form Request/src/components/layout/Header.jsx` on 2026-05-14._

```jsx
import { Logo } from '../ui/Logo';
import { cn } from '../../lib/utils';

export const Header = () => {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-white/20 bg-white/70 backdrop-blur-xl shadow-sm transition-all duration-300">
            <div className="container mx-auto flex h-20 items-center justify-between px-6">
                <div className="flex items-center gap-5 group cursor-default">
                    <Logo className="h-10 w-auto transition-transform duration-300 group-hover:scale-105" />
                    <div className="hidden sm:block border-l-2 border-janus-blue-100 pl-5">
                        <h1 className="text-lg font-bold text-janus-blue-900 tracking-tight leading-none group-hover:text-janus-orange-600 transition-colors">
                            HR Request Portal
                        </h1>
                        <p className="text-[10px] text-janus-blue-400 font-bold tracking-[0.2em] uppercase mt-0.5">
                            Internal Portal
                        </p>
                    </div>
                </div>

                {/* Progress Indicator (Simplified) */}
                <div className="hidden md:flex items-center gap-3">
                    <span className="text-xs font-medium text-janus-blue-300">Janus Digital</span>
                    <div className="h-2 w-2 rounded-full bg-janus-orange-500 animate-pulse"></div>
                </div>
            </div>
        </header>
    );
};

```