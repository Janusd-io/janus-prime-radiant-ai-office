---
type: source
source_type: laptop
title: route
slug: route-45
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/admin/team/employees/route.ts
original_size: 2545
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/team/employees/route.ts` on 2026-05-14._

```typescript
// Team management — Employee CRUD (May 2026).
// Sibling of /api/admin/team/managers. Powers the /admin/team page so HR
// can onboard new joiners without DB access.

import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { auditLog } from "@/lib/audit";

type Body = {
  firstName?: string;
  fullName?: string | null;
  email?: string | null;
  slackUserId?: string | null;
  slackHandle?: string | null;
  department?: string | null;
  isActive?: boolean;
  lineManagerId?: string | null;
};

export async function GET() {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const employees = await prisma.employee.findMany({
    include: { lineManager: { select: { id: true, name: true } } },
    orderBy: [{ isActive: "desc" }, { firstName: "asc" }],
  });
  return Response.json({ employees });
}

export async function POST(req: NextRequest) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  try {
    const body = (await req.json()) as Body;
    const firstName = (body.firstName ?? "").trim();
    if (!firstName) return Response.json({ error: "firstName is required" }, { status: 400 });
    if (body.lineManagerId) {
      const mgr = await prisma.lineManager.findUnique({ where: { id: body.lineManagerId } });
      if (!mgr) return Response.json({ error: "lineManagerId not found" }, { status: 400 });
    }
    const employee = await prisma.employee.create({
      data: {
        firstName,
        fullName: (body.fullName ?? "").trim() || null,
        email: (body.email ?? "").trim().toLowerCase() || null,
        slackUserId: (body.slackUserId ?? "").trim() || null,
        slackHandle: (body.slackHandle ?? "").trim().replace(/^@/, "") || null,
        department: (body.department ?? "").trim() || null,
        isActive: body.isActive ?? true,
        lineManagerId: body.lineManagerId || null,
      },
    });
    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "team.employee.create",
      targetType: "Employee",
      targetId: employee.id,
      details: { firstName, fullName: employee.fullName, email: employee.email },
    });
    return Response.json({ employee }, { status: 201 });
  } catch (err) {
    console.error("[team/employees POST]", err);
    return Response.json({ error: "Internal error" }, { status: 500 });
  }
}

```