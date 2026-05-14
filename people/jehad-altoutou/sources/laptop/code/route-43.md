---
type: source
source_type: laptop
title: Assessify — route
slug: route-43
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/team/managers/route.ts
original_size: 1873
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/team/managers/route.ts` on 2026-05-14._

```typescript
// Team management — LineManager CRUD (May 2026).

import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { auditLog } from "@/lib/audit";

type Body = {
  name?: string;
  email?: string | null;
  slackUserId?: string | null;
  slackHandle?: string | null;
  isActive?: boolean;
};

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const managers = await prisma.lineManager.findMany({
    include: { _count: { select: { directReports: true } } },
    orderBy: [{ isActive: "desc" }, { name: "asc" }],
  });
  return Response.json({ managers });
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  try {
    const body = (await req.json()) as Body;
    const name = (body.name ?? "").trim();
    if (!name) return Response.json({ error: "name is required" }, { status: 400 });
    const manager = await prisma.lineManager.create({
      data: {
        name,
        email: (body.email ?? "").trim().toLowerCase() || null,
        slackUserId: (body.slackUserId ?? "").trim() || null,
        slackHandle: (body.slackHandle ?? "").trim().replace(/^@/, "") || null,
        isActive: body.isActive ?? true,
      },
    });
    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "team.manager.create",
      targetType: "LineManager",
      targetId: manager.id,
      details: { name, email: manager.email },
    });
    return Response.json({ manager }, { status: 201 });
  } catch (err) {
    console.error("[team/managers POST]", err);
    return Response.json({ error: "Internal error" }, { status: 500 });
  }
}

```