---
type: source
source_type: laptop
title: sessions
slug: sessions
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/sessions.ts
original_size: 11420
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# sessions

_Extracted from `[[assessify|assessify]]/src/lib/operations/sessions.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  clampLimit,
  cursorWhere,
  decodeCursor,
  pageResult,
  type CursorPaged,
} from "@/lib/mcp/pagination";
import { McpValidationError } from "@/lib/mcp/validation";

// ─── get_session ──────────────────────────────────────────────────

export interface SessionDetail {
  id: string;
  status: string;
  candidateName: string;
  candidateEmail: string;
  startedAt: Date | null;
  completedAt: Date | null;
  lastActiveAt: Date | null;
  createdAt: Date;
  ipAddress: string | null;
  userAgent: string | null;
  assessment: {
    id: string;
    title: string;
    versionId: string;
    versionNumber: number;
  };
  totals: {
    answered: number;
    total: number;
  };
  result: {
    totalScore: number;
    maxScore: number;
    normalizedScore: number;
    recommendation: string;
    confidenceRating: number | null;
  } | null;
  sectionScores: Array<{ sectionId: string; sectionTitle: string; normalizedScore: number }>;
  competencyScores: Array<{ competencyId: string; competencyName: string; normalizedScore: number }>;
  responses: Array<{
    questionId: string;
    questionPrompt: string;
    sectionId: string;
    earnedPoints: number;
    maxPoints: number;
    normalizedScore: number;
    timeSpent: number;
    selectedOptions: string[] | null;
    freeTextResponse: string | null;
    answeredAt: Date;
  }>;
}

export async function getSession(sessionId: string): Promise<SessionDetail> {
  const s = await prisma.candidateSession.findUnique({
    where: { id: sessionId },
    include: {
      version: {
        include: {
          template: { select: { id: true, title: true } },
          sections: { select: { id: true, title: true, _count: { select: { questions: true } } } },
        },
      },
      result: true,
      sectionScores: {
        include: { section: { select: { id: true, title: true } } },
      },
      competencyScores: {
        include: { competency: { select: { id: true, name: true } } },
      },
      responses: {
        include: { question: { select: { id: true, prompt: true } } },
        orderBy: { answeredAt: "asc" },
      },
    },
  });
  if (!s) throw new McpValidationError(`session not found: ${sessionId}`);

  const totalQuestions = s.version.sections.reduce((acc, sec) => acc + sec._count.questions, 0);

  return {
    id: s.id,
    status: s.status,
    candidateName: s.candidateName,
    candidateEmail: s.candidateEmail,
    startedAt: s.startedAt,
    completedAt: s.completedAt,
    lastActiveAt: s.lastActiveAt,
    createdAt: s.createdAt,
    ipAddress: s.ipAddress,
    userAgent: s.userAgent,
    assessment: {
      id: s.version.template.id,
      title: s.version.template.title,
      versionId: s.version.id,
      versionNumber: s.version.versionNumber,
    },
    totals: { answered: s.responses.length, total: totalQuestions },
    result: s.result
      ? {
          totalScore: s.result.totalScore,
          maxScore: s.result.maxScore,
          normalizedScore: s.result.normalizedScore,
          recommendation: s.result.recommendation,
          confidenceRating: s.result.confidenceRating,
        }
      : null,
    sectionScores: s.sectionScores.map((ss) => ({
      sectionId: ss.section.id,
      sectionTitle: ss.section.title,
      normalizedScore: ss.normalizedScore,
    })),
    competencyScores: s.competencyScores.map((cs) => ({
      competencyId: cs.competency.id,
      competencyName: cs.competency.name,
      normalizedScore: cs.normalizedScore,
    })),
    responses: s.responses.map((r) => ({
      questionId: r.question.id,
      questionPrompt: r.question.prompt,
      sectionId: r.sectionId,
      earnedPoints: r.earnedPoints,
      maxPoints: r.maxPoints,
      normalizedScore: r.normalizedScore,
      timeSpent: r.timeSpent,
      selectedOptions: r.selectedOptions ? (JSON.parse(r.selectedOptions) as string[]) : null,
      freeTextResponse: r.freeTextResponse,
      answeredAt: r.answeredAt,
    })),
  };
}

// ─── get_session_results (scoring-only view) ──────────────────────

export interface SessionResults {
  sessionId: string;
  status: string;
  candidateName: string;
  candidateEmail: string;
  completedAt: Date | null;
  durationMinutes: number | null;
  totalScore: number;
  maxScore: number;
  normalizedScore: number;
  recommendation: string;
  confidenceRating: number | null;
  sectionScores: Array<{ sectionId: string; sectionTitle: string; normalizedScore: number }>;
  competencyScores: Array<{ competencyId: string; competencyName: string; normalizedScore: number }>;
}

export async function getSessionResults(sessionId: string): Promise<SessionResults> {
  const detail = await getSession(sessionId);
  if (!detail.result) {
    throw new McpValidationError(
      `session ${sessionId} has no result yet (status=${detail.status})`
    );
  }
  const duration =
    detail.startedAt && detail.completedAt
      ? Math.round(
          (detail.completedAt.getTime() - detail.startedAt.getTime()) / 60000
        )
      : null;
  return {
    sessionId: detail.id,
    status: detail.status,
    candidateName: detail.candidateName,
    candidateEmail: detail.candidateEmail,
    completedAt: detail.completedAt,
    durationMinutes: duration,
    totalScore: detail.result.totalScore,
    maxScore: detail.result.maxScore,
    normalizedScore: detail.result.normalizedScore,
    recommendation: detail.result.recommendation,
    confidenceRating: detail.result.confidenceRating,
    sectionScores: detail.sectionScores,
    competencyScores: detail.competencyScores,
  };
}

// ─── list_sessions ────────────────────────────────────────────────

export interface ListSessionsInput {
  assessmentId?: string;
  candidateEmail?: string;
  jobRoleId?: string;
  status?: string;
  recommendation?: string;
  dateFrom?: string;
  dateTo?: string;
  limit?: number;
  cursor?: string;
}

export interface SessionSummary {
  id: string;
  status: string;
  candidateName: string;
  candidateEmail: string;
  startedAt: Date | null;
  completedAt: Date | null;
  createdAt: Date;
  assessmentId: string;
  assessmentTitle: string;
  recommendation: string | null;
  normalizedScore: number | null;
}

export async function listSessions(
  input: ListSessionsInput
): Promise<CursorPaged<SessionSummary>> {
  const limit = clampLimit(input.limit);
  const cursor = decodeCursor(input.cursor);
  const where: Record<string, unknown> = {};

  if (input.status) where.status = input.status;
  if (input.candidateEmail) where.candidateEmail = input.candidateEmail;
  if (input.assessmentId) {
    where.version = { templateId: input.assessmentId };
  } else if (input.jobRoleId) {
    where.version = { template: { jobRoleId: input.jobRoleId } };
  }
  if (input.dateFrom || input.dateTo) {
    where.createdAt = {
      ...(input.dateFrom ? { gte: new Date(input.dateFrom) } : {}),
      ...(input.dateTo ? { lte: new Date(input.dateTo) } : {}),
    };
  }
  if (input.recommendation) {
    where.result = { recommendation: input.recommendation };
  }

  const cw = cursorWhere(cursor);
  const finalWhere = cw ? { AND: [where, cw] } : where;

  const rows = await prisma.candidateSession.findMany({
    where: finalWhere,
    take: limit + 1,
    orderBy: [{ createdAt: "desc" }, { id: "desc" }],
    include: {
      version: { include: { template: { select: { id: true, title: true } } } },
      result: { select: { recommendation: true, normalizedScore: true } },
    },
  });

  const summaries = rows.map((s) => ({
    id: s.id,
    status: s.status,
    candidateName: s.candidateName,
    candidateEmail: s.candidateEmail,
    startedAt: s.startedAt,
    completedAt: s.completedAt,
    createdAt: s.createdAt,
    assessmentId: s.version.template.id,
    assessmentTitle: s.version.template.title,
    recommendation: s.result?.recommendation ?? null,
    normalizedScore: s.result?.normalizedScore ?? null,
  }));

  return pageResult(summaries, limit);
}

// ─── export_sessions ──────────────────────────────────────────────

export interface ExportSessionsInput {
  assessmentId: string;
  format?: "json" | "csv";
  dateFrom?: string;
  dateTo?: string;
}

export interface ExportRow {
  sessionId: string;
  inviteCode: string | null;
  candidateName: string;
  candidateEmail: string;
  status: string;
  startedAt: string | null;
  completedAt: string | null;
  durationMinutes: number | null;
  totalScore: number | null;
  normalizedScore: number | null;
  recommendation: string | null;
}

export async function exportSessions(
  input: ExportSessionsInput
): Promise<{ format: "json"; data: ExportRow[] } | { format: "csv"; data: string }> {
  const where: Record<string, unknown> = {
    version: { templateId: input.assessmentId },
  };
  if (input.dateFrom || input.dateTo) {
    where.createdAt = {
      ...(input.dateFrom ? { gte: new Date(input.dateFrom) } : {}),
      ...(input.dateTo ? { lte: new Date(input.dateTo) } : {}),
    };
  }

  const sessions = await prisma.candidateSession.findMany({
    where,
    orderBy: { createdAt: "desc" },
    include: { result: true },
  });

  const inviteByEmail = new Map<string, string>();
  const invites = await prisma.candidateInvite.findMany({
    where: {
      templateId: input.assessmentId,
      candidateEmail: { in: Array.from(new Set(sessions.map((s) => s.candidateEmail))) },
    },
    select: { code: true, candidateEmail: true },
  });
  for (const i of invites) inviteByEmail.set(i.candidateEmail, i.code);

  const rows: ExportRow[] = sessions.map((s) => {
    const duration =
      s.startedAt && s.completedAt
        ? Math.round((s.completedAt.getTime() - s.startedAt.getTime()) / 60000)
        : null;
    return {
      sessionId: s.id,
      inviteCode: inviteByEmail.get(s.candidateEmail) ?? null,
      candidateName: s.candidateName,
      candidateEmail: s.candidateEmail,
      status: s.status,
      startedAt: s.startedAt?.toISOString() ?? null,
      completedAt: s.completedAt?.toISOString() ?? null,
      durationMinutes: duration,
      totalScore: s.result?.totalScore ?? null,
      normalizedScore: s.result?.normalizedScore ?? null,
      recommendation: s.result?.recommendation ?? null,
    };
  });

  if ((input.format ?? "json") === "json") {
    return { format: "json", data: rows };
  }

  const headers = [
    "sessionId",
    "inviteCode",
    "candidateName",
    "candidateEmail",
    "status",
    "startedAt",
    "completedAt",
    "durationMinutes",
    "totalScore",
    "normalizedScore",
    "recommendation",
  ];
  const escape = (v: unknown): string => {
    if (v === null || v === undefined) return "";
    const s = String(v);
    if (s.includes(",") || s.includes('"') || s.includes("\n")) {
      return `"${s.replace(/"/g, '""')}"`;
    }
    return s;
  };
  const lines = [headers.join(",")];
  for (const r of rows) {
    lines.push(
      headers
        .map((h) => escape((r as unknown as Record<string, unknown>)[h]))
        .join(",")
    );
  }
  return { format: "csv", data: lines.join("\n") };
}

```