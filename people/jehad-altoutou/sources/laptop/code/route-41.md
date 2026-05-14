---
type: source
source_type: laptop
title: Assessify — route
slug: route-41
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/admin/sessions/[sessionId]/route.ts"
original_size: 5148
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/admin/sessions/[sessionId]/route.ts` on 2026-05-14._

```typescript
import { NextRequest, NextResponse } from "next/server";
import { prisma } from "@/lib/db";
import { getSession } from "@/lib/auth";

export async function GET(
  _req: NextRequest,
  ctx: { params: Promise<{ sessionId: string }> }
) {
  const session = await getSession();
  if (!session) return NextResponse.json({ error: "Unauthorized" }, { status: 401 });

  try {
    const { sessionId } = await ctx.params;

    const session = await prisma.candidateSession.findUnique({
      where: { id: sessionId },
      include: {
        version: {
          include: {
            template: {
              include: {
                jobRole: {
                  include: { department: true },
                },
              },
            },
            sections: {
              where: { isActive: true },
              orderBy: { sortOrder: "asc" },
            },
          },
        },
        responses: {
          include: {
            question: {
              select: {
                id: true,
                slug: true,
                title: true,
                questionType: true,
                maxPoints: true,
                knockoutFlag: true,
              },
            },
            section: { select: { id: true, title: true, slug: true } },
          },
          orderBy: { answeredAt: "asc" },
        },
        result: true,
        sectionScores: {
          include: {
            section: { select: { title: true, slug: true } },
          },
        },
        competencyScores: {
          include: {
            competency: { select: { name: true, slug: true } },
          },
        },
      },
    });

    if (!session) {
      return Response.json({ error: "Session not found" }, { status: 404 });
    }

    const r = session.result;

    return Response.json({
      session: {
        id: session.id,
        status: session.status,
        candidateName: session.candidateName,
        candidateEmail: session.candidateEmail,
        startedAt: session.startedAt,
        completedAt: session.completedAt,
        lastActiveAt: session.lastActiveAt,
        ipAddress: session.ipAddress,
        userAgent: session.userAgent,
        createdAt: session.createdAt,
        assessment: {
          title: session.version.template.title,
          slug: session.version.template.slug,
          jobRole: session.version.template.jobRole.title,
          department: session.version.template.jobRole.department.name,
          versionId: session.version.id,
          versionNumber: session.version.versionNumber,
          passingScore: session.version.passingScore,
          timeLimit: session.version.timeLimit,
        },
        responses: session.responses.map((resp) => ({
          id: resp.id,
          questionId: resp.questionId,
          questionTitle: resp.question.title,
          questionType: resp.question.questionType,
          knockoutFlag: resp.question.knockoutFlag,
          sectionId: resp.sectionId,
          sectionTitle: resp.section.title,
          answerPayload: JSON.parse(resp.answerPayload),
          selectedOptions: resp.selectedOptions ? JSON.parse(resp.selectedOptions) : null,
          freeTextResponse: resp.freeTextResponse,
          timeSpent: resp.timeSpent,
          earnedPoints: resp.earnedPoints,
          maxPoints: resp.maxPoints,
          normalizedScore: resp.normalizedScore,
          scoringReason: resp.scoringReason,
          flaggedIndicators: resp.flaggedIndicators ? JSON.parse(resp.flaggedIndicators) : [],
          answeredAt: resp.answeredAt,
        })),
        result: r
          ? {
              id: r.id,
              totalScore: r.totalScore,
              maxScore: r.maxScore,
              normalizedScore: r.normalizedScore,
              recommendation: r.recommendation,
              confidenceRating: r.confidenceRating,
              hiringSummary: r.hiringSummary,
              flags: r.flags ? JSON.parse(r.flags) : [],
              automationLabels: r.automationLabels ? JSON.parse(r.automationLabels) : [],
              riskIndicators: r.riskIndicators ? JSON.parse(r.riskIndicators) : [],
              reviewedBy: r.reviewedBy,
              reviewedAt: r.reviewedAt,
              reviewNotes: r.reviewNotes,
              createdAt: r.createdAt,
            }
          : null,
        sectionScores: session.sectionScores.map((ss) => ({
          sectionId: ss.sectionId,
          title: ss.section.title,
          slug: ss.section.slug,
          score: ss.score,
          maxScore: ss.maxScore,
          normalizedScore: ss.normalizedScore,
          weightedScore: ss.weightedScore,
        })),
        competencyScores: session.competencyScores.map((cs) => ({
          competencyId: cs.competencyId,
          name: cs.competency.name,
          slug: cs.competency.slug,
          score: cs.score,
          maxScore: cs.maxScore,
          normalizedScore: cs.normalizedScore,
        })),
      },
    });
  } catch (error) {
    console.error("GET /api/admin/sessions/[sessionId] error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```