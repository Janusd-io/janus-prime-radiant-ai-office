---
type: source
source_type: laptop
title: route
slug: route-2
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/easter/track/route.ts
original_size: 582
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/easter/track/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { sessionId, candidateName, candidateEmail, event, data } = body;

    await prisma.analyticsEvent.create({
      data: {
        eventType: event ?? "egg_hunt_started",
        sessionId: sessionId ?? null,
        eventData: JSON.stringify({ candidateName, candidateEmail, ...data }),
      },
    });

    return Response.json({ ok: true });
  } catch {
    return Response.json({ ok: true });
  }
}

```