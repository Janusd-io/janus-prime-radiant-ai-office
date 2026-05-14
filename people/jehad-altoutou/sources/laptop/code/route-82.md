---
type: source
source_type: laptop
title: route
slug: route-82
created: 2026-04-23
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/proposals/auth/logout/route.ts
original_size: 196
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:46Z"
---

# route

_Extracted from `Desktop/Claude Projects/Dubai-Property-Leads/src/app/api/proposals/auth/logout/route.ts` on 2026-05-14._

```typescript
import { NextResponse } from 'next/server';

export async function POST() {
  const response = NextResponse.json({ ok: true });
  response.cookies.delete('proposal_session');
  return response;
}

```