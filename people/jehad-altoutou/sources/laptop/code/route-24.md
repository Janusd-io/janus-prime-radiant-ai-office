---
type: source
source_type: laptop
title: route
slug: route-24
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/sections/[sectionId]/questions/route.ts"
original_size: 2908
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/assessments/[id]/sections/[sectionId]/questions/route.ts` on 2026-05-14._

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

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string; sectionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { sectionId } = await ctx.params;
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
      slug,
      options,
      competencies,
    } = body as {
      title: string;
      prompt: string;
      questionType: string;
      difficulty?: string;
      maxPoints: number;
      weight?: number;
      scoringStrategy?: string;
      correctAnswerKey?: string;
      explanation?: string;
      slug?: string;
      options?: OptionInput[];
      competencies?: { competencyId: string; weight: number }[];
    };

    if (!title || !prompt || !questionType || maxPoints === undefined) {
      return Response.json(
        { error: "title, prompt, questionType, and maxPoints are required" },
        { status: 400 }
      );
    }

    const existingCount = await prisma.question.count({ where: { sectionId } });
    const finalSlug = slug?.trim() || `q-${Date.now()}`;

    const question = await prisma.question.create({
      data: {
        sectionId,
        slug: finalSlug,
        title,
        prompt,
        questionType,
        difficulty: difficulty ?? "medium",
        maxPoints,
        weight: weight ?? 1.0,
        scoringStrategy: scoringStrategy ?? "weighted_options",
        correctAnswerKey: correctAnswerKey ?? null,
        explanation: explanation ?? null,
        sortOrder: existingCount + 1,
        isActive: true,
      },
    });

    if (options && options.length > 0) {
      await prisma.answerOption.createMany({
        data: options.map((opt, i) => ({
          questionId: question.id,
          key: opt.key,
          label: opt.label,
          value: opt.value ?? opt.key,
          points: opt.points,
          isCorrect: opt.isCorrect ?? false,
          sortOrder: i + 1,
        })),
      });
    }

    if (competencies && competencies.length > 0) {
      await prisma.questionCompetency.createMany({
        data: competencies.map((c) => ({
          questionId: question.id,
          competencyId: c.competencyId,
          weight: c.weight,
        })),
      });
    }

    return Response.json({ question }, { status: 201 });
  } catch (error) {
    console.error("POST question error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```