---
type: source
source_type: laptop
title: route
slug: route-25
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/sections/[sectionId]/questions/[questionId]/route.ts"
original_size: 3451
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/admin/assessments/[id]/sections/[sectionId]/questions/[questionId]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

interface OptionInput {
  key: string;
  label: string;
  value?: string;
  points: number;
  isCorrect?: boolean;
}

export async function PATCH(
  req: NextRequest,
  ctx: { params: Promise<{ id: string; sectionId: string; questionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { questionId } = await ctx.params;
    const body = await req.json();
    const {
      title,
      prompt,
      questionType,
      difficulty,
      maxPoints,
      weight,
      scoringStrategy,
      correctAnswerKey,
      explanation,
      options,
      competencies,
      sortOrder,
    } = body;

    await prisma.question.update({
      where: { id: questionId },
      data: {
        ...(title !== undefined && { title }),
        ...(prompt !== undefined && { prompt }),
        ...(questionType !== undefined && { questionType }),
        ...(difficulty !== undefined && { difficulty }),
        ...(maxPoints !== undefined && { maxPoints }),
        ...(weight !== undefined && { weight }),
        ...(scoringStrategy !== undefined && { scoringStrategy }),
        ...(correctAnswerKey !== undefined && { correctAnswerKey }),
        ...(explanation !== undefined && { explanation }),
        ...(sortOrder !== undefined && { sortOrder }),
      },
    });

    // Replace options if provided
    if (Array.isArray(options)) {
      await prisma.answerOption.deleteMany({ where: { questionId } });
      if (options.length > 0) {
        await prisma.answerOption.createMany({
          data: (options as OptionInput[]).map((opt, i) => ({
            questionId,
            key: opt.key,
            label: opt.label,
            value: opt.value ?? opt.key,
            points: opt.points,
            isCorrect: opt.isCorrect ?? false,
            sortOrder: i + 1,
          })),
        });
      }
    }

    // Replace competencies if provided
    if (Array.isArray(competencies)) {
      await prisma.questionCompetency.deleteMany({ where: { questionId } });
      if (competencies.length > 0) {
        await prisma.questionCompetency.createMany({
          data: competencies.map((c: { competencyId: string; weight: number }) => ({
            questionId,
            competencyId: c.competencyId,
            weight: c.weight,
          })),
        });
      }
    }

    return Response.json({ ok: true });
  } catch (error) {
    console.error("PATCH question error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

export async function DELETE(
  _req: NextRequest,
  ctx: { params: Promise<{ id: string; sectionId: string; questionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { questionId } = await ctx.params;

    await prisma.questionCompetency.deleteMany({ where: { questionId } });
    await prisma.answerOption.deleteMany({ where: { questionId } });
    await prisma.question.delete({ where: { id: questionId } });

    return Response.json({ ok: true });
  } catch (error) {
    console.error("DELETE question error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```