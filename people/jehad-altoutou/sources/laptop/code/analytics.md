---
type: source
source_type: laptop
title: analytics
slug: analytics
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/analytics.ts
original_size: 5042
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# analytics

_Extracted from `assessify/src/lib/analytics.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import type { AnalyticsEventType } from "@/types/assessment";

// ─── Event Tracking ──────────────────────────────────────────

export async function trackEvent(
  eventType: AnalyticsEventType,
  data: {
    sessionId?: string;
    sectionId?: string;
    questionId?: string;
    eventData?: Record<string, unknown>;
    metadata?: Record<string, unknown>;
  }
) {
  return prisma.analyticsEvent.create({
    data: {
      eventType,
      sessionId: data.sessionId ?? null,
      sectionId: data.sectionId ?? null,
      questionId: data.questionId ?? null,
      eventData: data.eventData ? JSON.stringify(data.eventData) : null,
      metadata: data.metadata ? JSON.stringify(data.metadata) : null,
    },
  });
}

// ─── Analytics Queries ───────────────────────────────────────

export async function getSessionAnalytics(sessionId: string) {
  const events = await prisma.analyticsEvent.findMany({
    where: { sessionId },
    orderBy: { timestamp: "asc" },
  });

  return events.map((e) => ({
    ...e,
    eventData: e.eventData ? JSON.parse(e.eventData) : null,
    metadata: e.metadata ? JSON.parse(e.metadata) : null,
  }));
}

export async function getAssessmentFunnel(versionId: string) {
  const sessions = await prisma.candidateSession.findMany({
    where: { versionId },
    select: {
      id: true,
      status: true,
      startedAt: true,
      completedAt: true,
    },
  });

  const total = sessions.length;
  const started = sessions.filter((s) => s.startedAt).length;
  const completed = sessions.filter((s) => s.status === "completed").length;

  return {
    total,
    started,
    completed,
    completionRate: total > 0 ? completed / total : 0,
    dropOffRate: started > 0 ? 1 - completed / started : 0,
  };
}

export async function getQuestionAnalytics(versionId: string) {
  const responses = await prisma.candidateResponse.findMany({
    where: {
      session: { versionId },
    },
    include: {
      question: { select: { id: true, slug: true, title: true, maxPoints: true } },
    },
  });

  const byQuestion = new Map<
    string,
    { slug: string; title: string; scores: number[]; times: number[]; attempts: number }
  >();

  for (const r of responses) {
    const key = r.questionId;
    const existing = byQuestion.get(key) ?? {
      slug: r.question.slug,
      title: r.question.title,
      scores: [],
      times: [],
      attempts: 0,
    };
    existing.scores.push(r.normalizedScore);
    existing.times.push(r.timeSpent);
    existing.attempts++;
    byQuestion.set(key, existing);
  }

  return Array.from(byQuestion.entries()).map(([questionId, data]) => {
    const avgScore =
      data.scores.reduce((a, b) => a + b, 0) / (data.scores.length || 1);
    const avgTime =
      data.times.reduce((a, b) => a + b, 0) / (data.times.length || 1);
    const failRate = data.scores.filter((s) => s < 0.5).length / (data.scores.length || 1);

    return {
      questionId,
      slug: data.slug,
      title: data.title,
      avgScore: Math.round(avgScore * 1000) / 1000,
      avgTime: Math.round(avgTime),
      failRate: Math.round(failRate * 1000) / 1000,
      attempts: data.attempts,
    };
  });
}

export async function getCompetencyHeatmap(versionId: string) {
  const scores = await prisma.candidateCompetencyScore.findMany({
    where: {
      session: { versionId },
    },
    include: {
      competency: { select: { name: true, slug: true } },
    },
  });

  const byCompetency = new Map<
    string,
    { name: string; scores: number[] }
  >();

  for (const s of scores) {
    const key = s.competency.slug;
    const existing = byCompetency.get(key) ?? {
      name: s.competency.name,
      scores: [],
    };
    existing.scores.push(s.normalizedScore);
    byCompetency.set(key, existing);
  }

  return Array.from(byCompetency.entries()).map(([slug, data]) => ({
    slug,
    name: data.name,
    avgScore:
      Math.round(
        (data.scores.reduce((a, b) => a + b, 0) / (data.scores.length || 1)) *
          1000
      ) / 1000,
    count: data.scores.length,
  }));
}

export async function getResultDistribution(versionId: string) {
  const results = await prisma.candidateResult.findMany({
    where: {
      session: { versionId },
    },
    select: {
      recommendation: true,
      normalizedScore: true,
    },
  });

  const distribution: Record<string, number> = {
    strong_hire: 0,
    hire: 0,
    consider: 0,
    weak_fit: 0,
    reject: 0,
  };

  for (const r of results) {
    distribution[r.recommendation] = (distribution[r.recommendation] ?? 0) + 1;
  }

  const avgScore =
    results.length > 0
      ? results.reduce((sum, r) => sum + r.normalizedScore, 0) / results.length
      : 0;

  return {
    distribution,
    totalCandidates: results.length,
    avgScore: Math.round(avgScore * 1000) / 1000,
  };
}

```