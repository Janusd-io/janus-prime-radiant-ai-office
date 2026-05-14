---
type: source
source_type: laptop
title: Assessify — route
slug: route-66
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/sessions/[sessionId]/route.ts"
original_size: 4306
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/sessions/[sessionId]/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ sessionId: string }> }
) {
  try {
    const { sessionId } = await ctx.params;

    const session = await prisma.candidateSession.findUnique({
      where: { id: sessionId },
      include: {
        version: {
          include: {
            template: {
              select: {
                id: true,
                title: true,
                slug: true,
                eggHuntEnabled: true,
                jobRole: {
                  select: {
                    title: true,
                    department: { select: { slug: true, name: true } },
                  },
                },
              },
            },
            sections: {
              where: { isActive: true },
              orderBy: { sortOrder: "asc" },
              select: {
                id: true,
                title: true,
                slug: true,
                sortOrder: true,
                _count: { select: { questions: { where: { isActive: true } } } },
              },
            },
          },
        },
        responses: {
          select: {
            questionId: true,
            sectionId: true,
            earnedPoints: true,
            maxPoints: true,
            normalizedScore: true,
            answeredAt: true,
          },
        },
        result: {
          select: {
            recommendation: true,
            normalizedScore: true,
            totalScore: true,
            maxScore: true,
            confidenceRating: true,
          },
        },
      },
    });

    if (!session) {
      return Response.json({ error: "Session not found" }, { status: 404 });
    }

    // Auto-expire if time limit exceeded
    if (
      session.status !== "completed" &&
      session.status !== "expired" &&
      session.version.timeLimit &&
      session.startedAt
    ) {
      const elapsed = Date.now() - new Date(session.startedAt).getTime();
      if (elapsed > session.version.timeLimit * 60 * 1000) {
        await prisma.candidateSession.update({
          where: { id: sessionId },
          data: { status: "expired" },
        });
        session.status = "expired";
      }
    }

    const totalQuestions = session.version.sections.reduce(
      (sum, s) => sum + s._count.questions,
      0
    );
    const answeredQuestions = session.responses.length;

    return Response.json({
      session: {
        id: session.id,
        status: session.status,
        candidateName: session.candidateName,
        candidateEmail: session.candidateEmail,
        startedAt: session.startedAt,
        completedAt: session.completedAt,
        lastActiveAt: session.lastActiveAt,
        currentSectionId: session.currentSectionId,
        currentQuestionId: session.currentQuestionId,
        assessment: {
          title: session.version.template.title,
          slug: session.version.template.slug,
          versionId: session.version.id,
          versionNumber: session.version.versionNumber,
          timeLimit: session.version.timeLimit,
          passingScore: session.version.passingScore,
          jobRole: session.version.template.jobRole?.title ?? null,
          departmentSlug: session.version.template.jobRole?.department?.slug ?? null,
          departmentName: session.version.template.jobRole?.department?.name ?? null,
          eggHuntEnabled: session.version.template.eggHuntEnabled,
        },
        progress: {
          totalQuestions,
          answeredQuestions,
          completionPercent:
            totalQuestions > 0
              ? Math.round((answeredQuestions / totalQuestions) * 100)
              : 0,
          sections: session.version.sections.map((s) => ({
            id: s.id,
            title: s.title,
            slug: s.slug,
            totalQuestions: s._count.questions,
            answeredQuestions: session.responses.filter(
              (r) => r.sectionId === s.id
            ).length,
          })),
        },
        result: session.result ?? null,
      },
    });
  } catch (error) {
    console.error("GET /api/sessions/[sessionId] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```