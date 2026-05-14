---
type: source
source_type: laptop
title: Assessify — route
slug: route-46
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/team/employees/[id]/route.ts"
original_size: 3193
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/team/employees/[id]/route.ts` on 2026-05-14._

```typescript
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

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const { id } = await ctx.params;
  const existing = await prisma.employee.findUnique({ where: { id } });
  if (!existing) return Response.json({ error: "Employee not found" }, { status: 404 });

  const body = (await req.json()) as Body;
  const data: Record<string, unknown> = {};
  if (body.firstName !== undefined) {
    const t = body.firstName.trim();
    if (!t) return Response.json({ error: "firstName cannot be empty" }, { status: 400 });
    data.firstName = t;
  }
  if (body.fullName !== undefined) data.fullName = (body.fullName ?? "").trim() || null;
  if (body.email !== undefined) data.email = (body.email ?? "").trim().toLowerCase() || null;
  if (body.slackUserId !== undefined) data.slackUserId = (body.slackUserId ?? "").trim() || null;
  if (body.slackHandle !== undefined) data.slackHandle = (body.slackHandle ?? "").trim().replace(/^@/, "") || null;
  if (body.department !== undefined) data.department = (body.department ?? "").trim() || null;
  if (body.isActive !== undefined) data.isActive = body.isActive;
  if (body.lineManagerId !== undefined) {
    if (body.lineManagerId === null || body.lineManagerId === "") {
      data.lineManagerId = null;
    } else {
      const mgr = await prisma.lineManager.findUnique({ where: { id: body.lineManagerId } });
      if (!mgr) return Response.json({ error: "lineManagerId not found" }, { status: 400 });
      data.lineManagerId = body.lineManagerId;
    }
  }

  const employee = await prisma.employee.update({ where: { id }, data });
  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "team.employee.update",
    targetType: "Employee",
    targetId: id,
    details: { fields: Object.keys(data) },
  });
  return Response.json({ employee });
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> },
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  const { id } = await ctx.params;
  const existing = await prisma.employee.findUnique({ where: { id } });
  if (!existing) return Response.json({ error: "Employee not found" }, { status: 404 });
  // Soft-archive: never hard-delete (LeaveRequest history would orphan).
  const employee = await prisma.employee.update({
    where: { id },
    data: { isActive: false },
  });
  await auditLog({
    userId: session.id,
    userEmail: session.email,
    action: "team.employee.archive",
    targetType: "Employee",
    targetId: id,
  });
  return Response.json({ employee });
}

```