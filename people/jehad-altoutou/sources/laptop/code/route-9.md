---
type: source
source_type: laptop
title: route
slug: route-9
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/assessments/[slug]/route.ts"
original_size: 3681
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/assessments/[slug]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ slug: string }> }
) {
  try {
    const { slug } = await ctx.params;

    const template = await prisma.assessmentTemplate.findUnique({
      where: { slug, isActive: true },
      include: {
        jobRole: {
          include: { department: true },
        },
        versions: {
          where: { status: "published" },
          orderBy: { versionNumber: "desc" },
          take: 1,
          include: {
            sections: {
              where: { isActive: true },
              orderBy: { sortOrder: "asc" },
              include: {
                questions: {
                  where: { isActive: true },
                  orderBy: { sortOrder: "asc" },
                  include: {
                    options: {
                      orderBy: { sortOrder: "asc" },
                      select: {
                        id: true,
                        key: true,
                        label: true,
                        value: true,
                        sortOrder: true,
                        metadata: true,
                        // Omit: points, isCorrect
                      },
                    },
                    competencies: {
                      include: {
                        competency: {
                          select: { id: true, name: true, slug: true },
                        },
                      },
                    },
                  },
                },
              },
            },
          },
        },
      },
    });

    if (!template || template.versions.length === 0) {
      return Response.json({ error: "Assessment not found" }, { status: 404 });
    }

    const version = template.versions[0];

    const assessment = {
      id: template.id,
      title: template.title,
      slug: template.slug,
      description: template.description,
      jobRole: {
        id: template.jobRole.id,
        title: template.jobRole.title,
        slug: template.jobRole.slug,
        department: template.jobRole.department.name,
      },
      version: {
        id: version.id,
        versionNumber: version.versionNumber,
        passingScore: version.passingScore,
        timeLimit: version.timeLimit,
        publishedAt: version.publishedAt,
      },
      sections: version.sections.map((section) => ({
        id: section.id,
        title: section.title,
        slug: section.slug,
        description: section.description,
        introText: section.introText,
        iconName: section.iconName,
        sortOrder: section.sortOrder,
        weight: section.weight,
        questions: section.questions.map((q) => ({
          id: q.id,
          slug: q.slug,
          title: q.title,
          prompt: q.prompt,
          questionType: q.questionType,
          difficulty: q.difficulty,
          sortOrder: q.sortOrder,
          // Omit: maxPoints, weight, scoringStrategy, correctAnswerKey, rubric, knockoutFlag, etc.
          options: q.options,
          competencies: q.competencies.map((qc) => ({
            competencyId: qc.competency.id,
            name: qc.competency.name,
            slug: qc.competency.slug,
          })),
        })),
      })),
    };

    return Response.json({ assessment }, {
      headers: {
        "X-Powered-By-Curiosity": Buffer.from("egg{headers_speak_louder_than_words}").toString("base64"),
      },
    });
  } catch (error) {
    console.error("GET /api/assessments/[slug] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```