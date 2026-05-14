---
type: source
source_type: laptop
title: route
slug: route-69
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/sessions/[sessionId]/complete/route.ts"
original_size: 7746
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# route

_Extracted from `assessify/src/app/api/sessions/[sessionId]/complete/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import {
  scoreSections,
  scoreCompetencies,
  calculateRecommendation,
  calculateConfidence,
  generateHiringSummary,
  generateAutomationLabels,
  generateRiskIndicators,
  parseThresholds,
} from "@/lib/scoring-engine";
import { trackEvent } from "@/lib/analytics";
import { dispatchWebhook } from "@/lib/webhooks";

export async function POST(
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
            sections: {
              where: { isActive: true },
              include: {
                questions: {
                  where: { isActive: true },
                  include: {
                    competencies: true,
                  },
                },
              },
            },
          },
        },
        responses: true,
      },
    });

    if (!session) {
      return Response.json({ error: "Session not found" }, { status: 404 });
    }
    if (session.status === "completed") {
      return Response.json({ error: "Session already completed" }, { status: 409 });
    }

    // Build question scores for section scoring
    const questionScores = session.responses.map((r) => ({
      sectionId: r.sectionId,
      earnedPoints: r.earnedPoints,
      maxPoints: r.maxPoints,
    }));

    const sectionData = session.version.sections.map((s) => ({
      id: s.id,
      slug: s.slug,
      title: s.title,
      weight: s.weight,
    }));

    const sectionScores = scoreSections(sectionData, questionScores);

    // Gather all competency impacts from responses
    const allCompetencyImpacts: { competencyId: string; points: number; maxPoints: number }[] = [];

    for (const response of session.responses) {
      // Find the question in version sections
      for (const section of session.version.sections) {
        const question = section.questions.find((q) => q.id === response.questionId);
        if (question) {
          for (const qc of question.competencies) {
            allCompetencyImpacts.push({
              competencyId: qc.competencyId,
              points: response.earnedPoints * qc.weight,
              maxPoints: response.maxPoints * qc.weight,
            });
          }
          break;
        }
      }
    }

    // Fetch unique competencies involved
    const competencyIds = [...new Set(allCompetencyImpacts.map((i) => i.competencyId))];
    const competencies = await prisma.competency.findMany({
      where: { id: { in: competencyIds } },
      select: { id: true, slug: true, name: true },
    });

    const competencyScores = scoreCompetencies(competencies, allCompetencyImpacts);

    // Gather all flags
    const allFlags: string[] = [];
    for (const r of session.responses) {
      if (r.flaggedIndicators) {
        const flags = JSON.parse(r.flaggedIndicators) as string[];
        allFlags.push(...flags);
      }
    }
    const uniqueFlags = [...new Set(allFlags)];

    // Calculate totals
    const totalScore = session.responses.reduce((s, r) => s + r.earnedPoints, 0);
    const maxScore = session.responses.reduce((s, r) => s + r.maxPoints, 0);
    const normalizedScore = maxScore > 0 ? totalScore / maxScore : 0;

    // Count total questions across all sections
    const totalQuestions = session.version.sections.reduce(
      (sum, s) => sum + s.questions.length,
      0
    );
    const answeredQuestions = session.responses.length;

    const thresholds = parseThresholds(session.version.recommendationThresholds);
    const recommendation = calculateRecommendation(normalizedScore, uniqueFlags, thresholds);
    const confidence = calculateConfidence(sectionScores, totalQuestions, answeredQuestions);
    const hiringSummary = generateHiringSummary(recommendation, sectionScores, competencyScores, uniqueFlags);
    const automationLabels = generateAutomationLabels(recommendation, sectionScores, competencyScores, uniqueFlags);
    const riskIndicators = generateRiskIndicators(sectionScores, competencyScores, uniqueFlags);

    const resultPayload = {
      sessionId,
      normalizedScore,
      recommendation,
      confidence,
      sectionScores,
      competencyScores,
      flags: uniqueFlags,
      automationLabels,
      riskIndicators,
      hiringSummary,
    };

    // Persist result and scores in a transaction
    const [result] = await prisma.$transaction([
      prisma.candidateResult.create({
        data: {
          sessionId,
          totalScore,
          maxScore,
          normalizedScore,
          recommendation,
          confidenceRating: confidence,
          flags: JSON.stringify(uniqueFlags),
          automationLabels: JSON.stringify(automationLabels),
          hiringSummary,
          riskIndicators: JSON.stringify(riskIndicators),
          resultPayload: JSON.stringify(resultPayload),
        },
      }),
      ...sectionScores.map((ss) =>
        prisma.candidateSectionScore.upsert({
          where: { sessionId_sectionId: { sessionId, sectionId: ss.sectionId } },
          create: {
            sessionId,
            sectionId: ss.sectionId,
            score: ss.score,
            maxScore: ss.maxScore,
            normalizedScore: ss.normalizedScore,
            weightedScore: ss.weightedScore,
          },
          update: {
            score: ss.score,
            maxScore: ss.maxScore,
            normalizedScore: ss.normalizedScore,
            weightedScore: ss.weightedScore,
          },
        })
      ),
      ...competencyScores.map((cs) =>
        prisma.candidateCompetencyScore.upsert({
          where: { sessionId_competencyId: { sessionId, competencyId: cs.competencyId } },
          create: {
            sessionId,
            competencyId: cs.competencyId,
            score: cs.score,
            maxScore: cs.maxScore,
            normalizedScore: cs.normalizedScore,
          },
          update: {
            score: cs.score,
            maxScore: cs.maxScore,
            normalizedScore: cs.normalizedScore,
          },
        })
      ),
      prisma.candidateSession.update({
        where: { id: sessionId },
        data: {
          status: "completed",
          completedAt: new Date(),
          lastActiveAt: new Date(),
        },
      }),
    ]);

    // Update invite status if this session was created from an invite
    await prisma.candidateInvite.updateMany({
      where: { sessionId },
      data: { status: "completed" },
    });

    await trackEvent("assessment_completed", {
      sessionId,
      eventData: {
        recommendation,
        normalizedScore,
        confidence,
        totalQuestions,
        answeredQuestions,
      },
    });

    await dispatchWebhook("assessment.completed", {
      sessionId,
      candidateName: session.candidateName,
      candidateEmail: session.candidateEmail,
      recommendation,
      normalizedScore,
      confidence,
      automationLabels,
      hiringSummary,
      riskIndicators,
    });

    return Response.json({
      result: {
        id: result.id,
        sessionId,
        totalScore,
        maxScore,
        normalizedScore,
        recommendation,
        confidenceRating: confidence,
        hiringSummary,
        automationLabels,
        riskIndicators,
        flags: uniqueFlags,
        sectionScores,
        competencyScores,
      },
    });
  } catch (error) {
    console.error("POST /api/sessions/[sessionId]/complete error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```