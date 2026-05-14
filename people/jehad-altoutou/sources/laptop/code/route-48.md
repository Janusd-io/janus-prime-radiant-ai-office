---
type: source
source_type: laptop
title: Assessify — route
slug: route-48
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/competencies/[id]/route.ts"
original_size: 1724
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/competencies/[id]/route.ts` on 2026-05-14._

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
    const { name, description, category } = await req.json();

    await prisma.competency.update({
      where: { id },
      data: {
        ...(name !== undefined && { name }),
        ...(description !== undefined && { description }),
        ...(category !== undefined && { category }),
      },
    });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH competency error:", error);
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

    const linkCount = await prisma.questionCompetency.count({ where: { competencyId: id } });
    if (linkCount > 0) {
      return Response.json(
        { error: `Cannot delete: competency is used by ${linkCount} question(s). Remove those first.` },
        { status: 400 }
      );
    }

    await prisma.competency.delete({ where: { id } });
    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE competency error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```