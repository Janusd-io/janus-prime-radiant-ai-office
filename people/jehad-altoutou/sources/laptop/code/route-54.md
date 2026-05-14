---
type: source
source_type: laptop
title: route
slug: route-54
created: 2026-05-12
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/job-roles/[id]/route.ts"
original_size: 2996
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/job-roles/[id]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const body = await req.json() as {
      title?: string;
      description?: string;
      isActive?: boolean;
      jdSummary?: string;
      jdResponsibilities?: string;
      jdRequirements?: string;
      jdNiceToHaves?: string;
      jdYearsExperience?: string;
      interviewerEmail?: string;
    };

    const trimOrNull = (v: string | undefined | null) => {
      if (v === undefined) return undefined;
      if (v === null) return null;
      const t = v.trim();
      return t.length > 0 ? t : null;
    };

    await prisma.jobRole.update({
      where: { id },
      data: {
        ...(body.title !== undefined && { title: body.title.trim() }),
        ...(body.description !== undefined && { description: trimOrNull(body.description) }),
        ...(body.isActive !== undefined && { isActive: body.isActive }),
        ...(body.jdSummary !== undefined && { jdSummary: trimOrNull(body.jdSummary) }),
        ...(body.jdResponsibilities !== undefined && { jdResponsibilities: trimOrNull(body.jdResponsibilities) }),
        ...(body.jdRequirements !== undefined && { jdRequirements: trimOrNull(body.jdRequirements) }),
        ...(body.jdNiceToHaves !== undefined && { jdNiceToHaves: trimOrNull(body.jdNiceToHaves) }),
        ...(body.jdYearsExperience !== undefined && { jdYearsExperience: trimOrNull(body.jdYearsExperience) }),
        ...(body.interviewerEmail !== undefined && { interviewerEmail: trimOrNull(body.interviewerEmail) }),
      },
    });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH /api/admin/job-roles/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;

    // Check if any assessment templates use this role
    const templateCount = await prisma.assessmentTemplate.count({
      where: { jobRoleId: id },
    });
    if (templateCount > 0) {
      return Response.json(
        { error: `Cannot delete: ${templateCount} assessment(s) use this role. Delete or reassign them first.` },
        { status: 400 }
      );
    }

    await prisma.jobRole.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE /api/admin/job-roles/[id] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```