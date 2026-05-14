---
type: source
source_type: laptop
title: analytics
slug: analytics-2
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/analytics.ts
original_size: 10845
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# analytics

_Extracted from `[[assessify|assessify]]/src/lib/operations/analytics.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertAssessmentExists,
  assertQuestionExists,
} from "@/lib/mcp/validation";

// ─── get_assessment_analytics ─────────────────────────────────────

export interface AssessmentAnalyticsInput {
  assessmentId: string;
  dateFrom?: string;
  dateTo?: string;
}

export interface AssessmentAnalytics {
  assessmentId: string;
  assessmentTitle: string;
  invites: {
    total: number;
    pending: number;
    completed: number;
    expired: number;
  };
  sessions: {
    total: number;
    inProgress: number;
    completed: number;
  };
  completionRate: number;
  avgNormalizedScore: number | null;
  avgDurationMinutes: number | null;
  recommendationBreakdown: Record<string, number>;
  scoreHistogram: { bucket: string; count: number }[];
  perSection: Array<{ sectionId: string; sectionTitle: string; avgNormalizedScore: number | null; count: number }>;
  perCompetency: Array<{ competencyId: string; competencyName: string; avgNormalizedScore: number | null; count: number }>;
  perQuestion: Array<{ questionId: string; prompt: string; pctCorrect: number; avgTimeSeconds: number; sampleSize: number }>;
}

export async function getAssessmentAnalytics(
  input: AssessmentAnalyticsInput
): Promise<AssessmentAnalytics> {
  const { id } = await assertAssessmentExists(input.assessmentId);
  const tpl = await prisma.assessmentTemplate.findUnique({
    where: { id },
    select: { id: true, title: true },
  });

  const dateFilter =
    input.dateFrom || input.dateTo
      ? {
          ...(input.dateFrom ? { gte: new Date(input.dateFrom) } : {}),
          ...(input.dateTo ? { lte: new Date(input.dateTo) } : {}),
        }
      : undefined;

  const [
    inviteTotal, invitePending, inviteCompleted, inviteExpired,
    sessionTotal, sessionInProgress, sessionCompleted,
    sessions, sectionScores, competencyScores, responses,
  ] = await Promise.all([
    prisma.candidateInvite.count({
      where: { templateId: id, ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateInvite.count({
      where: { templateId: id, status: "pending", ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateInvite.count({
      where: { templateId: id, status: "completed", ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateInvite.count({
      where: { templateId: id, status: "expired", ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateSession.count({
      where: { version: { templateId: id }, ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateSession.count({
      where: { version: { templateId: id }, status: "in_progress", ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateSession.count({
      where: { version: { templateId: id }, status: "completed", ...(dateFilter ? { createdAt: dateFilter } : {}) },
    }),
    prisma.candidateSession.findMany({
      where: { version: { templateId: id }, status: "completed", ...(dateFilter ? { createdAt: dateFilter } : {}) },
      include: { result: true },
    }),
    prisma.candidateSectionScore.findMany({
      where: {
        session: {
          version: { templateId: id },
          status: "completed",
          ...(dateFilter ? { createdAt: dateFilter } : {}),
        },
      },
      include: { section: { select: { id: true, title: true } } },
    }),
    prisma.candidateCompetencyScore.findMany({
      where: {
        session: {
          version: { templateId: id },
          status: "completed",
          ...(dateFilter ? { createdAt: dateFilter } : {}),
        },
      },
      include: { competency: { select: { id: true, name: true } } },
    }),
    prisma.candidateResponse.findMany({
      where: {
        session: {
          version: { templateId: id },
          status: "completed",
          ...(dateFilter ? { createdAt: dateFilter } : {}),
        },
      },
      include: { question: { select: { id: true, prompt: true } } },
    }),
  ]);

  const completed = sessions.filter((s) => s.result);
  const avgNormalized =
    completed.length === 0
      ? null
      : completed.reduce((acc, s) => acc + (s.result!.normalizedScore ?? 0), 0) / completed.length;

  const avgDuration = (() => {
    const durations: number[] = [];
    for (const s of completed) {
      if (s.startedAt && s.completedAt) {
        durations.push((s.completedAt.getTime() - s.startedAt.getTime()) / 60000);
      }
    }
    if (durations.length === 0) return null;
    return durations.reduce((a, b) => a + b, 0) / durations.length;
  })();

  const recommendationBreakdown: Record<string, number> = {};
  for (const s of completed) {
    const r = s.result!.recommendation;
    recommendationBreakdown[r] = (recommendationBreakdown[r] ?? 0) + 1;
  }

  const scoreHistogram = [
    { bucket: "0–20%", count: 0 },
    { bucket: "20–40%", count: 0 },
    { bucket: "40–60%", count: 0 },
    { bucket: "60–80%", count: 0 },
    { bucket: "80–100%", count: 0 },
  ];
  for (const s of completed) {
    const n = s.result!.normalizedScore ?? 0;
    const idx = Math.min(4, Math.floor(n * 5));
    scoreHistogram[idx].count++;
  }

  const sectionAggregator = new Map<string, { title: string; sum: number; count: number }>();
  for (const ss of sectionScores) {
    const e = sectionAggregator.get(ss.section.id) ?? { title: ss.section.title, sum: 0, count: 0 };
    e.sum += ss.normalizedScore;
    e.count += 1;
    sectionAggregator.set(ss.section.id, e);
  }
  const perSection = Array.from(sectionAggregator.entries()).map(([sid, e]) => ({
    sectionId: sid,
    sectionTitle: e.title,
    avgNormalizedScore: e.count === 0 ? null : e.sum / e.count,
    count: e.count,
  }));

  const compAggregator = new Map<string, { name: string; sum: number; count: number }>();
  for (const cs of competencyScores) {
    const e = compAggregator.get(cs.competency.id) ?? { name: cs.competency.name, sum: 0, count: 0 };
    e.sum += cs.normalizedScore;
    e.count += 1;
    compAggregator.set(cs.competency.id, e);
  }
  const perCompetency = Array.from(compAggregator.entries()).map(([cid, e]) => ({
    competencyId: cid,
    competencyName: e.name,
    avgNormalizedScore: e.count === 0 ? null : e.sum / e.count,
    count: e.count,
  }));

  const questionAggregator = new Map<
    string,
    { prompt: string; correct: number; total: number; timeSum: number }
  >();
  for (const r of responses) {
    const e =
      questionAggregator.get(r.question.id) ??
      { prompt: r.question.prompt, correct: 0, total: 0, timeSum: 0 };
    e.total += 1;
    if (r.normalizedScore >= 0.5) e.correct += 1;
    e.timeSum += r.timeSpent;
    questionAggregator.set(r.question.id, e);
  }
  const perQuestion = Array.from(questionAggregator.entries()).map(([qid, e]) => ({
    questionId: qid,
    prompt: e.prompt,
    pctCorrect: e.total === 0 ? 0 : e.correct / e.total,
    avgTimeSeconds: e.total === 0 ? 0 : e.timeSum / e.total,
    sampleSize: e.total,
  }));

  return {
    assessmentId: id,
    assessmentTitle: tpl?.title ?? "(missing)",
    invites: {
      total: inviteTotal,
      pending: invitePending,
      completed: inviteCompleted,
      expired: inviteExpired,
    },
    sessions: {
      total: sessionTotal,
      inProgress: sessionInProgress,
      completed: sessionCompleted,
    },
    completionRate: inviteTotal === 0 ? 0 : inviteCompleted / inviteTotal,
    avgNormalizedScore: avgNormalized,
    avgDurationMinutes: avgDuration,
    recommendationBreakdown,
    scoreHistogram,
    perSection,
    perCompetency,
    perQuestion,
  };
}

// ─── get_question_analytics ───────────────────────────────────────

export interface QuestionAnalytics {
  questionId: string;
  prompt: string;
  questionType: string;
  sampleSize: number;
  pctCorrect: number;
  avgTimeSeconds: number;
  optionDistribution: Array<{ key: string; label: string; pickedCount: number; pickedPct: number; isCorrect: boolean }>;
  /** Discrimination index = (top tercile pct correct) − (bottom tercile pct correct). null if sample size < 6. */
  discriminationIndex: number | null;
}

export async function getQuestionAnalytics(questionId: string): Promise<QuestionAnalytics> {
  await assertQuestionExists(questionId);
  const question = await prisma.question.findUnique({
    where: { id: questionId },
    include: { options: { orderBy: { sortOrder: "asc" } } },
  });
  if (!question) throw new Error(`question vanished: ${questionId}`);

  const responses = await prisma.candidateResponse.findMany({
    where: { questionId, session: { status: "completed" } },
    select: {
      selectedOptions: true,
      normalizedScore: true,
      timeSpent: true,
      session: { select: { result: { select: { normalizedScore: true } } } },
    },
  });

  const sampleSize = responses.length;
  const correct = responses.filter((r) => r.normalizedScore >= 0.5).length;
  const pctCorrect = sampleSize === 0 ? 0 : correct / sampleSize;
  const avgTime =
    sampleSize === 0
      ? 0
      : responses.reduce((acc, r) => acc + r.timeSpent, 0) / sampleSize;

  const pickCount = new Map<string, number>();
  for (const r of responses) {
    if (!r.selectedOptions) continue;
    try {
      const opts = JSON.parse(r.selectedOptions) as string[];
      for (const o of opts) pickCount.set(o, (pickCount.get(o) ?? 0) + 1);
    } catch {
      // Ignore malformed payloads
    }
  }

  const optionDistribution = question.options.map((o) => {
    const picked = pickCount.get(o.key) ?? 0;
    return {
      key: o.key,
      label: o.label,
      pickedCount: picked,
      pickedPct: sampleSize === 0 ? 0 : picked / sampleSize,
      isCorrect: o.isCorrect,
    };
  });

  let discriminationIndex: number | null = null;
  if (sampleSize >= 6) {
    const sorted = responses
      .filter((r) => r.session.result)
      .sort((a, b) => (b.session.result!.normalizedScore ?? 0) - (a.session.result!.normalizedScore ?? 0));
    const tercileSize = Math.floor(sorted.length / 3);
    if (tercileSize > 0) {
      const top = sorted.slice(0, tercileSize);
      const bottom = sorted.slice(-tercileSize);
      const topCorrect = top.filter((r) => r.normalizedScore >= 0.5).length / top.length;
      const bottomCorrect = bottom.filter((r) => r.normalizedScore >= 0.5).length / bottom.length;
      discriminationIndex = topCorrect - bottomCorrect;
    }
  }

  return {
    questionId: question.id,
    prompt: question.prompt,
    questionType: question.questionType,
    sampleSize,
    pctCorrect,
    avgTimeSeconds: avgTime,
    optionDistribution,
    discriminationIndex,
  };
}

```