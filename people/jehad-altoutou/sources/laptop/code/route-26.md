---
type: source
source_type: laptop
title: route
slug: route-26
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/assessments/[id]/duplicate/route.ts"
original_size: 5251
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/assessments/[id]/duplicate/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ id: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { id } = await ctx.params;
    const { jobRoleId, title } = await req.json() as {
      jobRoleId?: string;
      title?: string;
    };

    // Load the source template with everything
    const source = await prisma.assessmentTemplate.findUnique({
      where: { id },
      include: {
        versions: {
          orderBy: { versionNumber: "desc" },
          take: 1,
          include: {
            sections: {
              orderBy: { sortOrder: "asc" },
              include: {
                questions: {
                  orderBy: { sortOrder: "asc" },
                  include: {
                    options: { orderBy: { sortOrder: "asc" } },
                    competencies: true,
                  },
                },
              },
            },
          },
        },
      },
    });

    if (!source) {
      return Response.json({ error: "Source assessment not found" }, { status: 404 });
    }

    const sourceVersion = source.versions[0];
    if (!sourceVersion) {
      return Response.json({ error: "Source has no version to duplicate" }, { status: 404 });
    }

    // Generate a unique slug
    const newTitle = title?.trim() || `${source.title} (Copy)`;
    const baseSlug = newTitle.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
    let finalSlug = baseSlug;
    let counter = 1;
    while (await prisma.assessmentTemplate.findUnique({ where: { slug: finalSlug } })) {
      finalSlug = `${baseSlug}-${counter}`;
      counter++;
    }

    // Create the new template (always starts as draft)
    const newTemplate = await prisma.assessmentTemplate.create({
      data: {
        title: newTitle,
        slug: finalSlug,
        description: source.description,
        jobRoleId: jobRoleId ?? source.jobRoleId,
        isActive: true,
        versions: {
          create: {
            versionNumber: 1,
            status: "draft",
            passingScore: sourceVersion.passingScore,
            timeLimit: sourceVersion.timeLimit,
          },
        },
      },
      include: { versions: true },
    });

    const newVersionId = newTemplate.versions[0].id;

    // Clone sections, questions, options, and competency links
    for (const srcSection of sourceVersion.sections) {
      const newSection = await prisma.section.create({
        data: {
          versionId: newVersionId,
          title: srcSection.title,
          slug: srcSection.slug,
          description: srcSection.description,
          introText: srcSection.introText,
          iconName: srcSection.iconName,
          sortOrder: srcSection.sortOrder,
          weight: srcSection.weight,
          isActive: srcSection.isActive,
        },
      });

      for (const srcQuestion of srcSection.questions) {
        const newQuestion = await prisma.question.create({
          data: {
            sectionId: newSection.id,
            slug: srcQuestion.slug,
            title: srcQuestion.title,
            prompt: srcQuestion.prompt,
            questionType: srcQuestion.questionType,
            difficulty: srcQuestion.difficulty,
            maxPoints: srcQuestion.maxPoints,
            weight: srcQuestion.weight,
            scoringStrategy: srcQuestion.scoringStrategy,
            correctAnswerKey: srcQuestion.correctAnswerKey,
            rubric: srcQuestion.rubric,
            partialCreditRules: srcQuestion.partialCreditRules,
            knockoutFlag: srcQuestion.knockoutFlag,
            knockoutThreshold: srcQuestion.knockoutThreshold,
            automationLabel: srcQuestion.automationLabel,
            analyticsLabel: srcQuestion.analyticsLabel,
            explanation: srcQuestion.explanation,
            sortOrder: srcQuestion.sortOrder,
            isActive: srcQuestion.isActive,
            version: 1,
          },
        });

        if (srcQuestion.options.length > 0) {
          await prisma.answerOption.createMany({
            data: srcQuestion.options.map((opt) => ({
              questionId: newQuestion.id,
              key: opt.key,
              label: opt.label,
              value: opt.value,
              points: opt.points,
              isCorrect: opt.isCorrect,
              sortOrder: opt.sortOrder,
              metadata: opt.metadata,
            })),
          });
        }

        if (srcQuestion.competencies.length > 0) {
          await prisma.questionCompetency.createMany({
            data: srcQuestion.competencies.map((qc) => ({
              questionId: newQuestion.id,
              competencyId: qc.competencyId,
              weight: qc.weight,
            })),
          });
        }
      }
    }

    return Response.json({ template: newTemplate }, { status: 201 });
  } catch (error) {
    console.error("POST /api/admin/assessments/[id]/duplicate error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```