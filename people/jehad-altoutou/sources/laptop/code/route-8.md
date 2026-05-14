---
type: source
source_type: laptop
title: route
slug: route-8
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/app/api/assessments/route.ts
original_size: 2134
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/assessments/route.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";

export async function GET() {
  try {
    const templates = await prisma.assessmentTemplate.findMany({
      where: { isActive: true },
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
              select: {
                id: true,
                title: true,
                slug: true,
                description: true,
                sortOrder: true,
                weight: true,
                _count: { select: { questions: { where: { isActive: true } } } },
              },
            },
          },
        },
      },
      orderBy: { createdAt: "desc" },
    });

    const assessments = templates
      .filter((t) => t.versions.length > 0)
      .map((t) => {
        const version = t.versions[0];
        return {
          id: t.id,
          title: t.title,
          slug: t.slug,
          description: t.description,
          jobRole: {
            id: t.jobRole.id,
            title: t.jobRole.title,
            slug: t.jobRole.slug,
            department: t.jobRole.department.name,
          },
          version: {
            id: version.id,
            versionNumber: version.versionNumber,
            passingScore: version.passingScore,
            timeLimit: version.timeLimit,
            publishedAt: version.publishedAt,
          },
          sections: version.sections.map((s) => ({
            id: s.id,
            title: s.title,
            slug: s.slug,
            description: s.description,
            sortOrder: s.sortOrder,
            weight: s.weight,
            questionCount: s._count.questions,
          })),
        };
      });

    return Response.json({ assessments });
  } catch (error) {
    console.error("GET /api/assessments error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```