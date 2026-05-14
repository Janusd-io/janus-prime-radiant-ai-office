---
type: source
source_type: laptop
title: route
slug: route-68
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: "/Users/jehad/assessify/src/app/api/sessions/[sessionId]/answers/route.ts"
original_size: 5417
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# route

_Extracted from `[[assessify|assessify]]/src/app/api/sessions/[sessionId]/answers/route.ts` on 2026-05-14._

```typescript
import { NextRequest } from "next/server";
import { prisma } from "@/lib/db";
import { scoreQuestion } from "@/lib/scoring-engine";
import { trackEvent } from "@/lib/analytics";
import type { AnswerPayload } from "@/types/assessment";

export async function POST(
  req: NextRequest,
  ctx: { params: Promise<{ sessionId: string }> }
) {
  try {
    const { sessionId } = await ctx.params;
    const body = await req.json();
    const { questionId, sectionId, answerPayload } = body as {
      questionId: string;
      sectionId: string;
      answerPayload: AnswerPayload;
    };

    if (!questionId || !sectionId || !answerPayload) {
      return Response.json(
        { error: "questionId, sectionId, and answerPayload are required" },
        { status: 400 }
      );
    }

    const session = await prisma.candidateSession.findUnique({
      where: { id: sessionId },
      select: {
        id: true, status: true, versionId: true, startedAt: true,
        version: { select: { timeLimit: true } },
      },
    });

    if (!session) {
      return Response.json({ error: "Session not found" }, { status: 404 });
    }
    if (session.status === "completed" || session.status === "expired") {
      return Response.json(
        { error: "Session is no longer active" },
        { status: 409 }
      );
    }

    // Enforce time limit
    if (session.version.timeLimit && session.startedAt) {
      const elapsed = Date.now() - new Date(session.startedAt).getTime();
      const limitMs = session.version.timeLimit * 60 * 1000;
      if (elapsed > limitMs) {
        await prisma.candidateSession.update({
          where: { id: sessionId },
          data: { status: "expired" },
        });
        return Response.json(
          { error: "Time limit exceeded. Your session has expired." },
          { status: 409 }
        );
      }
    }

    const question = await prisma.question.findUnique({
      where: { id: questionId },
      include: {
        options: {
          select: { key: true, points: true, isCorrect: true },
        },
        competencies: {
          select: { competencyId: true, weight: true },
        },
      },
    });

    if (!question) {
      return Response.json({ error: "Question not found" }, { status: 404 });
    }

    const questionData = {
      id: question.id,
      questionType: question.questionType,
      maxPoints: question.maxPoints,
      weight: question.weight,
      scoringStrategy: question.scoringStrategy,
      correctAnswerKey: question.correctAnswerKey,
      rubric: question.rubric,
      partialCreditRules: question.partialCreditRules,
      knockoutFlag: question.knockoutFlag,
      knockoutThreshold: question.knockoutThreshold,
      options: question.options,
      competencies: question.competencies,
    };

    const scoringResult = scoreQuestion(questionData, answerPayload);

    const response = await prisma.candidateResponse.upsert({
      where: { sessionId_questionId: { sessionId, questionId } },
      create: {
        sessionId,
        sectionId,
        questionId,
        answerPayload: JSON.stringify(answerPayload),
        selectedOptions: answerPayload.selectedOptions
          ? JSON.stringify(answerPayload.selectedOptions)
          : null,
        freeTextResponse: answerPayload.freeTextResponse ?? null,
        timeSpent: answerPayload.timeSpent ?? 0,
        earnedPoints: scoringResult.earnedPoints,
        maxPoints: scoringResult.maxPoints,
        normalizedScore: scoringResult.normalizedScore,
        scoringReason: scoringResult.scoringReason,
        flaggedIndicators: JSON.stringify(scoringResult.flaggedIndicators),
      },
      update: {
        answerPayload: JSON.stringify(answerPayload),
        selectedOptions: answerPayload.selectedOptions
          ? JSON.stringify(answerPayload.selectedOptions)
          : null,
        freeTextResponse: answerPayload.freeTextResponse ?? null,
        timeSpent: answerPayload.timeSpent ?? 0,
        earnedPoints: scoringResult.earnedPoints,
        maxPoints: scoringResult.maxPoints,
        normalizedScore: scoringResult.normalizedScore,
        scoringReason: scoringResult.scoringReason,
        flaggedIndicators: JSON.stringify(scoringResult.flaggedIndicators),
        updatedAt: new Date(),
      },
    });

    await prisma.candidateSession.update({
      where: { id: sessionId },
      data: {
        lastActiveAt: new Date(),
        currentSectionId: sectionId,
        currentQuestionId: questionId,
      },
    });

    await trackEvent("answer_submitted", {
      sessionId,
      sectionId,
      questionId,
      eventData: {
        earnedPoints: scoringResult.earnedPoints,
        maxPoints: scoringResult.maxPoints,
        normalizedScore: scoringResult.normalizedScore,
        flags: scoringResult.flaggedIndicators,
      },
    });

    return Response.json(
      {
        responseId: response.id,
        questionId,
        earnedPoints: scoringResult.earnedPoints,
        maxPoints: scoringResult.maxPoints,
        normalizedScore: scoringResult.normalizedScore,
        scoringReason: scoringResult.scoringReason,
        flaggedIndicators: scoringResult.flaggedIndicators,
      },
      { status: 201 }
    );
  } catch (error) {
    console.error("POST /api/sessions/[sessionId]/answers error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

```