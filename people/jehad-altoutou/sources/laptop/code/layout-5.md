---
type: source
source_type: laptop
title: Desktop Captures — layout
slug: layout-5
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/proposals/layout.tsx
original_size: 283
original_ext: .tsx
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# layout

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/proposals/layout.tsx` on 2026-05-14._

```tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Dubai Property Leads — Proposal',
  robots: { index: false, follow: false },
};

export default function ProposalsLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}

```