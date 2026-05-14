---
type: source
source_type: laptop
title: proposals
slug: proposals
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/types/proposals.ts
original_size: 707
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# proposals

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/types/proposals.ts` on 2026-05-14._

```typescript
export interface ProposalClientRecord {
  id: string;
  companyName: string;
  contactName: string;
  email: string;
  role: string | null;
  phone: string | null;
  website: string | null;
  officeAddress: string | null;
  slug: string;
  status: string;
  notes: string | null;
  meetingDate: Date | null;
  createdAt: Date;
  proposal: ProposalDataRecord | null;
}

export interface ProposalDataRecord {
  id: string;
  clientId: string;
  packageVolume: number | null;
  pricingNotes: string | null;
  pricingDisplay: string | null;
  customSections: Record<string, unknown> | null;
  discoveryNotes: string | null;
  ctaMessage: string | null;
  status: string;
  createdAt: Date;
  updatedAt: Date;
}

```