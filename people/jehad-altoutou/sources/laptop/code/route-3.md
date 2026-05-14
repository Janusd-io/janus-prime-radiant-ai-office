---
type: source
source_type: laptop
title: route
slug: route-3
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/easter/resume/route.ts
original_size: 784
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/easter/resume/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function GET(req: NextRequest) {
  const email = new URL(req.url).searchParams.get("email");

  if (!email) {
    return Response.json({ error: "email is required" }, { status: 400 });
  }

  // Find the most recent session for this email
  const session = await prisma.candidateSession.findFirst({
    where: { candidateEmail: email },
    orderBy: { createdAt: "desc" },
    select: { id: true, candidateName: true, candidateEmail: true },
  });

  if (!session) {
    return Response.json({ error: "No session found" }, { status: 404 });
  }

  return Response.json({
    sessionId: session.id,
    candidateName: session.candidateName,
    candidateEmail: session.candidateEmail,
  });
}

```