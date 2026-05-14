---
type: source
source_type: laptop
title: validation
slug: validation
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/validation.ts
original_size: 6478
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# validation

_Extracted from `assessify/src/lib/mcp/validation.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import type { McpSession } from "./auth";

/** Thrown by validation helpers — caught by callTool and surfaced as a tool error. */
export class McpValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "McpValidationError";
  }
}

export class McpPermissionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "McpPermissionError";
  }
}

/** Throws permission_denied if the caller is not an admin. */
export function requireAdmin(session: McpSession): void {
  if (session.role !== "admin") {
    throw new McpPermissionError(
      `permission_denied: this tool requires admin role (caller has role="${session.role}")`
    );
  }
}

/**
 * Section weights must sum to ~1.0 (tolerance 0.001 for float quirks).
 * Pass an array of weights only — caller decides which sections are in scope.
 */
export function assertWeightsSumToOne(weights: number[], context = "sections"): void {
  if (weights.length === 0) {
    throw new McpValidationError(`${context} must have at least one entry`);
  }
  const sum = weights.reduce((a, b) => a + b, 0);
  if (Math.abs(sum - 1.0) > 0.001) {
    throw new McpValidationError(
      `${context} weights must sum to 1.0 (got ${sum.toFixed(3)}). Adjust before retrying.`
    );
  }
}

export async function assertCompetencyIdsExist(ids: string[]): Promise<void> {
  if (ids.length === 0) return;
  const found = await prisma.competency.findMany({
    where: { id: { in: ids } },
    select: { id: true },
  });
  const foundSet = new Set(found.map((c) => c.id));
  const missing = ids.filter((id) => !foundSet.has(id));
  if (missing.length > 0) {
    throw new McpValidationError(`competency not found: ${missing.join(", ")}`);
  }
}

export async function assertJobRoleExists(id: string): Promise<void> {
  const r = await prisma.jobRole.findUnique({ where: { id }, select: { id: true } });
  if (!r) throw new McpValidationError(`jobRole not found: ${id}`);
}

export async function assertAssessmentExists(id: string): Promise<{ id: string; latestVersionId: string }> {
  const t = await prisma.assessmentTemplate.findUnique({
    where: { id },
    include: { versions: { orderBy: { versionNumber: "desc" }, take: 1, select: { id: true } } },
  });
  if (!t) throw new McpValidationError(`assessment not found: ${id}`);
  if (!t.versions[0]) throw new McpValidationError(`assessment ${id} has no version`);
  return { id: t.id, latestVersionId: t.versions[0].id };
}

/** Sessions in these statuses count as "in-flight" — editing the assessment
 * version they reference is unsafe because their experience would shift mid-take. */
const IN_FLIGHT_SESSION_STATUSES = ["not_started", "in_progress", "paused"];

/**
 * Refuse edits to a published assessment version that has in-flight candidate
 * sessions. The caller is expected to call `create_new_version` first; the new
 * draft can be published once edits are reviewed.
 *
 * Pass either the assessmentId (we resolve to its latest version) or a specific
 * versionId. Drafts are always editable. Published versions with no in-flight
 * sessions are also editable (low risk — invites already issued land on a
 * snapshot of the structure they were sent to).
 */
export async function assertVersionEditable(args: {
  assessmentId?: string;
  versionId?: string;
}): Promise<void> {
  const { prisma } = await import("@/lib/db");
  let versionId = args.versionId;
  if (!versionId && args.assessmentId) {
    const latest = await prisma.assessmentVersion.findFirst({
      where: { templateId: args.assessmentId },
      orderBy: { versionNumber: "desc" },
      select: { id: true, status: true },
    });
    if (!latest) throw new McpValidationError(`assessment ${args.assessmentId} has no version`);
    versionId = latest.id;
  }
  if (!versionId) throw new McpValidationError("assertVersionEditable: assessmentId or versionId required");

  const version = await prisma.assessmentVersion.findUnique({
    where: { id: versionId },
    select: { id: true, status: true, templateId: true },
  });
  if (!version) throw new McpValidationError(`version not found: ${versionId}`);

  if (version.status !== "published") return;

  const inFlight = await prisma.candidateSession.count({
    where: { versionId: version.id, status: { in: IN_FLIGHT_SESSION_STATUSES } },
  });
  if (inFlight > 0) {
    throw new McpValidationError(
      `cannot edit a published version with ${inFlight} in-flight session(s). Call create_new_version first; the new draft can be published once edits are reviewed.`
    );
  }
}

export async function assertSectionExists(id: string): Promise<{ id: string; versionId: string }> {
  const s = await prisma.section.findUnique({
    where: { id },
    select: { id: true, versionId: true },
  });
  if (!s) throw new McpValidationError(`section not found: ${id}`);
  return s;
}

export async function assertQuestionExists(id: string): Promise<{ id: string; sectionId: string | null }> {
  const q = await prisma.question.findUnique({
    where: { id },
    select: { id: true, sectionId: true },
  });
  if (!q) throw new McpValidationError(`question not found: ${id}`);
  return q;
}

/**
 * MCQ questions need at least one correct option (points > 0).
 * Free-text / scenario types can pass an empty array.
 */
export function assertMcqOptionsHaveCorrect(
  questionType: string,
  options: Array<{ points: number }>
): void {
  const isMcq = questionType === "single_select" || questionType === "multi_select";
  if (!isMcq) return;
  if (options.length < 2) {
    throw new McpValidationError("MCQ questions need at least 2 options");
  }
  const correct = options.filter((o) => o.points > 0);
  if (correct.length === 0) {
    throw new McpValidationError("MCQ questions need at least one option with points > 0");
  }
}

/**
 * Validate recommendation thresholds: strongHire > hire > consider, all in 0..1.
 */
export function assertThresholds(t: { strongHire: number; hire: number; consider: number }): void {
  for (const [k, v] of Object.entries(t)) {
    if (typeof v !== "number" || v < 0 || v > 1) {
      throw new McpValidationError(`threshold ${k} must be a number between 0 and 1 (got ${v})`);
    }
  }
  if (!(t.strongHire > t.hire && t.hire > t.consider)) {
    throw new McpValidationError(
      `thresholds must satisfy strongHire > hire > consider (got ${t.strongHire} > ${t.hire} > ${t.consider})`
    );
  }
}

```