---
type: source
source_type: laptop
title: UrgencyBanner
slug: urgencybanner
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/components/UrgencyBanner.tsx
original_size: 1569
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---

# UrgencyBanner

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/components/UrgencyBanner.tsx` on 2026-05-14._

```tsx
'use client';

import { useEffect, useState } from 'react';
import { Timer, AlertTriangle, TrendingUp } from 'lucide-react';

export default function UrgencyBanner() {
  const [inquiryCount, setInquiryCount] = useState(0);

  useEffect(() => {
    // Generate random number between 150 and 2500 on mount
    const randomCount = Math.floor(Math.random() * (2500 - 150 + 1)) + 150;
    setInquiryCount(randomCount);

    // Subtle countdown effect to create urgency
    const interval = setInterval(() => {
      setInquiryCount((prev) => (prev > 100 ? prev - 1 : randomCount));
    }, 45000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-blue-600 py-3 overflow-hidden">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap items-center justify-center gap-x-8 gap-y-2 text-white text-sm font-medium">
          <div className="flex items-center gap-2">
            <TrendingUp className="w-4 h-4 text-blue-200" />
            <span>High demand today</span>
          </div>
          
          <div className="flex items-center gap-2">
            <Timer className="w-4 h-4 text-blue-200" />
            <span>{inquiryCount} buyer enquiries remaining for fulfillment</span>
          </div>
          
          <div className="flex items-center gap-2">
            <AlertTriangle className="w-4 h-4 text-blue-200" />
            <span className="hidden sm:inline italic opacity-90">Packages sold first-paid, first-fulfilled</span>
          </div>
        </div>
      </div>
    </div>
  );
}

```