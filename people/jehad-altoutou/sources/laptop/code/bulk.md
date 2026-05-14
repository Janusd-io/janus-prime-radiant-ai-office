---
type: source
source_type: laptop
title: bulk
slug: bulk
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/bulk.ts
original_size: 8411
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# bulk

_Extracted from `[[assessify|assessify]]/src/lib/operations/bulk.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertCompetencyIdsExist,
  assertVersionEditable,
  McpValidationError,
} from "@/lib/mcp/validation";

// ─── bulk_tag_questions ───────────────────────────────────────────

export type BulkTagMode = "replace" | "add" | "remove";

export interface BulkTagQuestionsInput {
  questionIds: string[];
  competencyIds: string[];
  mode: BulkTagMode;
}

export interface BulkTagQuestionsResult {
  questionsUpdated: number;
  tagsAdded: number;
  tagsRemoved: number;
  mode: BulkTagMode;
}

/**
 * Atomically update competency tags on a set of questions.
 *  - replace: drop all existing tags on each question, then set the new set
 *  - add:     union the new set onto existing tags
 *  - remove:  delete the listed competencyIds from each question
 *
 * Validates that the version owning each question is editable (no in-flight
 * sessions on a published version).
 */
export async function bulkTagQuestions(
  input: BulkTagQuestionsInput
): Promise<BulkTagQuestionsResult> {
  if (!Array.isArray(input.questionIds) || input.questionIds.length === 0) {
    throw new McpValidationError("questionIds must be a non-empty array");
  }
  if (!Array.isArray(input.competencyIds)) {
    throw new McpValidationError("competencyIds must be an array");
  }
  if (!["replace", "add", "remove"].includes(input.mode)) {
    throw new McpValidationError(`invalid mode "${input.mode}" — must be replace, add, or remove`);
  }
  if (input.questionIds.length > 500) {
    throw new McpValidationError("max 500 questionIds per call");
  }
  if (input.mode !== "remove" && input.competencyIds.length === 0) {
    throw new McpValidationError(`mode "${input.mode}" requires at least one competencyId`);
  }
  if (input.competencyIds.length > 0) {
    await assertCompetencyIdsExist(input.competencyIds);
  }

  const questions = await prisma.question.findMany({
    where: { id: { in: input.questionIds } },
    select: { id: true, sectionId: true },
  });
  if (questions.length !== input.questionIds.length) {
    const found = new Set(questions.map((q) => q.id));
    const missing = input.questionIds.filter((id) => !found.has(id));
    throw new McpValidationError(`questions not found: ${missing.join(", ")}`);
  }

  // Resolve unique versions across all touched questions and ensure they're editable.
  const sectionIds = Array.from(new Set(questions.map((q) => q.sectionId)));
  const sections = await prisma.section.findMany({
    where: { id: { in: sectionIds } },
    select: { versionId: true },
  });
  const versionIds = Array.from(new Set(sections.map((s) => s.versionId)));
  for (const versionId of versionIds) {
    await assertVersionEditable({ versionId });
  }

  let tagsAdded = 0;
  let tagsRemoved = 0;

  await prisma.$transaction(async (tx) => {
    for (const q of questions) {
      if (input.mode === "replace") {
        const removed = await tx.questionCompetency.deleteMany({ where: { questionId: q.id } });
        tagsRemoved += removed.count;
        if (input.competencyIds.length > 0) {
          await tx.questionCompetency.createMany({
            data: input.competencyIds.map((cid) => ({
              questionId: q.id,
              competencyId: cid,
              weight: 1.0,
            })),
          });
          tagsAdded += input.competencyIds.length;
        }
      } else if (input.mode === "add") {
        const existing = await tx.questionCompetency.findMany({
          where: { questionId: q.id, competencyId: { in: input.competencyIds } },
          select: { competencyId: true },
        });
        const have = new Set(existing.map((e) => e.competencyId));
        const toAdd = input.competencyIds.filter((cid) => !have.has(cid));
        if (toAdd.length > 0) {
          await tx.questionCompetency.createMany({
            data: toAdd.map((cid) => ({ questionId: q.id, competencyId: cid, weight: 1.0 })),
          });
          tagsAdded += toAdd.length;
        }
      } else {
        // remove
        const removed = await tx.questionCompetency.deleteMany({
          where: { questionId: q.id, competencyId: { in: input.competencyIds } },
        });
        tagsRemoved += removed.count;
      }
    }
  });

  return {
    questionsUpdated: questions.length,
    tagsAdded,
    tagsRemoved,
    mode: input.mode,
  };
}

// ─── bulk_delete_questions ────────────────────────────────────────

export interface BulkDeleteQuestionsResult {
  deletedCount: number;
  deletedIds: string[];
}

/**
 * Delete a set of questions in one call. Refuses the WHOLE batch if any
 * question has candidate responses — partial deletion would be confusing.
 * Also refuses if any question lives on a published version with in-flight
 * sessions.
 */
export async function bulkDeleteQuestions(
  questionIds: string[]
): Promise<BulkDeleteQuestionsResult> {
  if (!Array.isArray(questionIds) || questionIds.length === 0) {
    throw new McpValidationError("questionIds must be a non-empty array");
  }
  if (questionIds.length > 500) {
    throw new McpValidationError("max 500 questionIds per call");
  }

  const questions = await prisma.question.findMany({
    where: { id: { in: questionIds } },
    select: {
      id: true,
      prompt: true,
      sectionId: true,
      _count: { select: { responses: true } },
    },
  });
  if (questions.length !== questionIds.length) {
    const found = new Set(questions.map((q) => q.id));
    const missing = questionIds.filter((id) => !found.has(id));
    throw new McpValidationError(`questions not found: ${missing.join(", ")}`);
  }
  const withAnswers = questions.filter((q) => q._count.responses > 0);
  if (withAnswers.length > 0) {
    throw new McpValidationError(
      `cannot bulk-delete: ${withAnswers.length} question(s) have candidate responses (ids: ${withAnswers
        .map((q) => q.id)
        .join(", ")}). Refuse atomically — re-call with the safe subset.`
    );
  }

  const sectionIds = Array.from(new Set(questions.map((q) => q.sectionId)));
  const sections = await prisma.section.findMany({
    where: { id: { in: sectionIds } },
    select: { versionId: true },
  });
  const versionIds = Array.from(new Set(sections.map((s) => s.versionId)));
  for (const versionId of versionIds) {
    await assertVersionEditable({ versionId });
  }

  await prisma.$transaction(async (tx) => {
    await tx.questionCompetency.deleteMany({ where: { questionId: { in: questionIds } } });
    await tx.answerOption.deleteMany({ where: { questionId: { in: questionIds } } });
    await tx.question.deleteMany({ where: { id: { in: questionIds } } });
  });

  return { deletedCount: questions.length, deletedIds: questions.map((q) => q.id) };
}

// ─── bulk_toggle_assessment_active ────────────────────────────────

export interface BulkToggleAssessmentActiveResult {
  changedCount: number;
  alreadyInStateCount: number;
  notFound: string[];
  changedIds: string[];
}

export async function bulkToggleAssessmentActive(input: {
  assessmentIds: string[];
  isActive: boolean;
}): Promise<BulkToggleAssessmentActiveResult> {
  if (!Array.isArray(input.assessmentIds) || input.assessmentIds.length === 0) {
    throw new McpValidationError("assessmentIds must be a non-empty array");
  }
  if (typeof input.isActive !== "boolean") {
    throw new McpValidationError("isActive must be a boolean");
  }
  if (input.assessmentIds.length > 200) {
    throw new McpValidationError("max 200 assessmentIds per call");
  }

  const found = await prisma.assessmentTemplate.findMany({
    where: { id: { in: input.assessmentIds } },
    select: { id: true, isActive: true },
  });
  const foundIds = new Set(found.map((r) => r.id));
  const notFound = input.assessmentIds.filter((id) => !foundIds.has(id));

  const toChange = found.filter((r) => r.isActive !== input.isActive).map((r) => r.id);
  if (toChange.length > 0) {
    await prisma.assessmentTemplate.updateMany({
      where: { id: { in: toChange } },
      data: { isActive: input.isActive },
    });
  }

  return {
    changedCount: toChange.length,
    alreadyInStateCount: found.length - toChange.length,
    notFound,
    changedIds: toChange,
  };
}

```