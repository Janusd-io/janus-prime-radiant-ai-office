---
type: source
source_type: laptop
title: Assessify — route
slug: route-34
created: 2026-05-06
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/recruitment/rubrics/[id]/route.ts"
original_size: 4082
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/recruitment/rubrics/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";
import { auditLog } from "@/lib/audit";
import { validateRubricInput } from "../route";

export async function GET(_req: NextRequest, ctx: { params: Promise<{ id: string }> }) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  const { id } = await ctx.params;
  const rubric = await prisma.recruitmentRubric.findUnique({
    where: { id },
    include: { jobRole: { include: { department: true } } },
  });
  if (!rubric) return Response.json({ error: "Rubric not found" }, { status: 404 });
  return Response.json({ rubric });
}

export async function PATCH(req: NextRequest, ctx: { params: Promise<{ id: string }> }) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const existing = await prisma.recruitmentRubric.findUnique({ where: { id } });
    if (!existing) return Response.json({ error: "Rubric not found" }, { status: 404 });

    const body = await req.json();
    const validated = validateRubricInput(body);
    if (validated.error) return Response.json({ error: validated.error }, { status: 400 });

    const rubric = await prisma.recruitmentRubric.update({
      where: { id },
      data: {
        name: validated.name,
        kind: validated.kind,
        jobRoleId: validated.jobRoleId,
        isActive: validated.isActive,
        criteria: JSON.stringify(validated.criteria),
        thresholdStrong: validated.thresholdStrong,
        thresholdMatch: validated.thresholdMatch,
        thresholdConsider: validated.thresholdConsider,
      },
    });

    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "recruitment.rubric.update",
      targetType: "RecruitmentRubric",
      targetId: id,
      details: {
        name: rubric.name,
        kind: rubric.kind,
        jobRoleId: rubric.jobRoleId,
        isActive: rubric.isActive,
      },
    });

    return Response.json({ rubric });
  } catch (error) {
    console.error("PATCH /api/admin/recruitment/rubrics/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(_req: NextRequest, ctx: { params: Promise<{ id: string }> }) {
  // Soft archive by setting isActive=false. Hard delete is refused if any
  // ApplicationScore references this rubric.
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const existing = await prisma.recruitmentRubric.findUnique({
      where: { id },
      include: { _count: { select: { scores: true } } },
    });
    if (!existing) return Response.json({ error: "Rubric not found" }, { status: 404 });

    if (existing._count.scores > 0) {
      // Don't hard-delete — would orphan scoring history. Just deactivate.
      await prisma.recruitmentRubric.update({ where: { id }, data: { isActive: false } });
      await auditLog({
        userId: session.id,
        userEmail: session.email,
        action: "recruitment.rubric.archive",
        targetType: "RecruitmentRubric",
        targetId: id,
        details: { reason: "scores reference this rubric — archived instead of deleted" },
      });
      return Response.json({ ok: true, archived: true });
    }

    await prisma.recruitmentRubric.delete({ where: { id } });
    await auditLog({
      userId: session.id,
      userEmail: session.email,
      action: "recruitment.rubric.delete",
      targetType: "RecruitmentRubric",
      targetId: id,
      details: {},
    });
    return Response.json({ ok: true, archived: false });
  } catch (error) {
    console.error("DELETE /api/admin/recruitment/rubrics/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```