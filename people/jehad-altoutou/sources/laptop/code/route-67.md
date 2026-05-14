---
type: source
source_type: laptop
title: route
slug: route-67
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/sessions/[sessionId]/result/route.ts"
original_size: 2524
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# route

_Extracted from `[[assessify|assessify]]/src/app/api/sessions/[sessionId]/result/route.ts` on 2026-05-14._

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
    if (!session.result) {
      return Response.json(
        { error: "Assessment not yet completed" },
        { status: 404 }
      );
    }

    const r = session.result;

    return Response.json({
      result: {
        id: r.id,
        sessionId,
        candidateName: session.candidateName,
        candidateEmail: session.candidateEmail,
        completedAt: session.completedAt,
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
    console.error("GET /api/sessions/[sessionId]/result error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```