---
type: source
source_type: laptop
title: Assessify — route
slug: route-44
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/team/managers/[id]/route.ts"
original_size: 2857
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/team/managers/[id]/route.ts` on 2026-05-14._

```typescript
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

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const { id } = await ctx.params;
  const existing = await prisma.lineManager.findUnique({ where: { id } });
  if (!existing) return Response.json({ error: "LineManager not found" }, { status: 404 });

  const body = (await req.json()) as Body;
  const data: Record<string, unknown> = {};
  if (body.name !== undefined) {
    const t = body.name.trim();
    if (!t) return Response.json({ error: "name cannot be empty" }, { status: 400 });
    data.name = t;
  }
  if (body.email !== undefined) data.email = (body.email ?? "").trim().toLowerCase() || null;
  if (body.slackUserId !== undefined) data.slackUserId = (body.slackUserId ?? "").trim() || null;
  if (body.slackHandle !== undefined) data.slackHandle = (body.slackHandle ?? "").trim().replace(/^@/, "") || null;
  if (body.isActive !== undefined) data.isActive = body.isActive;

  const manager = await prisma.lineManager.update({ where: { id }, data });
  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "team.manager.update",
    targetType: "LineManager",
    targetId: id,
    details: { fields: Object.keys(data) },
  });
  return Response.json({ manager });
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const { id } = await ctx.params;
  const existing = await prisma.lineManager.findUnique({ where: { id } });
  if (!existing) return Response.json({ error: "LineManager not found" }, { status: 404 });

  // If employees still report to this manager, unlink them first to avoid
  // dangling FKs after archive.
  const reportCount = await prisma.employee.count({ where: { lineManagerId: id } });
  if (reportCount > 0) {
    await prisma.employee.updateMany({
      where: { lineManagerId: id },
      data: { lineManagerId: null },
    });
  }
  const manager = await prisma.lineManager.update({
    where: { id },
    data: { isActive: false },
  });
  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "team.manager.archive",
    targetType: "LineManager",
    targetId: id,
    details: { unlinkedReports: reportCount },
  });
  return Response.json({ manager, unlinkedReports: reportCount });
}

```