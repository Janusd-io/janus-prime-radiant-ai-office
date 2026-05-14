---
type: source
source_type: laptop
title: route
slug: route-23
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/sections/[sectionId]/route.ts"
original_size: 2132
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/assessments/[id]/sections/[sectionId]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string; sectionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { sectionId } = await ctx.params;
    const body = await req.json();
    const { title, description, introText, iconName, weight, sortOrder } = body;

    await prisma.section.update({
      where: { id: sectionId },
      data: {
        ...(title !== undefined && { title }),
        ...(description !== undefined && { description }),
        ...(introText !== undefined && { introText }),
        ...(iconName !== undefined && { iconName }),
        ...(weight !== undefined && { weight }),
        ...(sortOrder !== undefined && { sortOrder }),
      },
    });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH section error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string; sectionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { sectionId } = await ctx.params;

    // Cascade: delete question competencies, options, questions, then section
    const questions = await prisma.question.findMany({ where: { sectionId } });
    for (const q of questions) {
      await prisma.questionCompetency.deleteMany({ where: { questionId: q.id } });
      await prisma.answerOption.deleteMany({ where: { questionId: q.id } });
    }
    await prisma.question.deleteMany({ where: { sectionId } });
    await prisma.section.delete({ where: { id: sectionId } });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE section error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```