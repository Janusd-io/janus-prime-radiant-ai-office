---
type: source
source_type: laptop
title: sections
slug: sections
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/sections.ts
original_size: 9025
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# sections

_Extracted from `[[assessify|assessify]]/src/lib/operations/sections.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertAssessmentExists,
  assertSectionExists,
  assertVersionEditable,
  assertWeightsSumToOne,
  McpValidationError,
} from "@/lib/mcp/validation";

function slugify(s: string): string {
  return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

// ─── add_section ──────────────────────────────────────────────────

export interface AddSectionInput {
  assessmentId: string;
  title: string;
  weight: number;
  description?: string;
  introText?: string;
  /** 0-based; defaults to end */
  sortOrder?: number;
}

export interface SectionRecord {
  id: string;
  title: string;
  slug: string;
  description: string | null;
  weight: number;
  sortOrder: number;
}

export async function addSection(input: AddSectionInput): Promise<SectionRecord> {
  if (input.weight < 0 || input.weight > 1) {
    throw new McpValidationError("section weight must be between 0 and 1");
  }
  const { latestVersionId } = await assertAssessmentExists(input.assessmentId);
  await assertVersionEditable({ versionId: latestVersionId });

  const existing = await prisma.section.findMany({
    where: { versionId: latestVersionId },
    select: { id: true, slug: true, sortOrder: true },
    orderBy: { sortOrder: "asc" },
  });

  // Slug collision guard: append -2/-3/... if needed
  const baseSlug = slugify(input.title);
  const taken = new Set(existing.map((s) => s.slug));
  let slug = baseSlug;
  let n = 2;
  while (taken.has(slug)) slug = `${baseSlug}-${n++}`;

  const insertAt = input.sortOrder ?? existing.length;
  if (insertAt < 0 || insertAt > existing.length) {
    throw new McpValidationError(
      `sortOrder ${insertAt} out of range (0..${existing.length})`
    );
  }

  const section = await prisma.$transaction(async (tx) => {
    // Bump existing sortOrders to make room
    if (insertAt < existing.length) {
      for (const s of existing) {
        if (s.sortOrder >= insertAt) {
          await tx.section.update({ where: { id: s.id }, data: { sortOrder: s.sortOrder + 1 } });
        }
      }
    }
    return tx.section.create({
      data: {
        versionId: latestVersionId,
        title: input.title,
        slug,
        description: input.description ?? null,
        introText: input.introText ?? null,
        weight: input.weight,
        sortOrder: insertAt,
      },
    });
  });

  return {
    id: section.id,
    title: section.title,
    slug: section.slug,
    description: section.description,
    weight: section.weight,
    sortOrder: section.sortOrder,
  };
}

// ─── update_section ───────────────────────────────────────────────

export interface UpdateSectionInput {
  sectionId: string;
  title?: string;
  description?: string;
  introText?: string;
}

export async function updateSection(input: UpdateSectionInput): Promise<SectionRecord> {
  const { versionId } = await assertSectionExists(input.sectionId);
  await assertVersionEditable({ versionId });
  const data: Record<string, unknown> = {};
  if (input.title !== undefined) data.title = input.title;
  if (input.description !== undefined) data.description = input.description;
  if (input.introText !== undefined) data.introText = input.introText;
  const updated = await prisma.section.update({ where: { id: input.sectionId }, data });
  return {
    id: updated.id,
    title: updated.title,
    slug: updated.slug,
    description: updated.description,
    weight: updated.weight,
    sortOrder: updated.sortOrder,
  };
}

// ─── remove_section ───────────────────────────────────────────────

export interface RemoveSectionInput {
  sectionId: string;
}

export async function removeSection(input: RemoveSectionInput): Promise<{ ok: true; removedSectionId: string }> {
  const { versionId } = await assertSectionExists(input.sectionId);
  await assertVersionEditable({ versionId });

  // Reject if any candidate sessions have responses scoring this section
  const responseCount = await prisma.candidateResponse.count({
    where: { sectionId: input.sectionId },
  });
  if (responseCount > 0) {
    throw new McpValidationError(
      `cannot remove section: ${responseCount} candidate response(s) reference it. Archive the assessment instead.`
    );
  }

  await prisma.$transaction(async (tx) => {
    const questions = await tx.question.findMany({
      where: { sectionId: input.sectionId },
      select: { id: true },
    });
    for (const q of questions) {
      await tx.questionCompetency.deleteMany({ where: { questionId: q.id } });
      await tx.answerOption.deleteMany({ where: { questionId: q.id } });
    }
    await tx.question.deleteMany({ where: { sectionId: input.sectionId } });
    await tx.section.delete({ where: { id: input.sectionId } });
  });

  return { ok: true, removedSectionId: input.sectionId };
}

// ─── reorder_sections ─────────────────────────────────────────────

export interface ReorderSectionsInput {
  assessmentId: string;
  /** Section IDs in the desired display order. Must include every section. */
  orderedSectionIds: string[];
}

export async function reorderSections(input: ReorderSectionsInput): Promise<SectionRecord[]> {
  const { latestVersionId } = await assertAssessmentExists(input.assessmentId);
  await assertVersionEditable({ versionId: latestVersionId });
  const existing = await prisma.section.findMany({
    where: { versionId: latestVersionId },
    select: { id: true },
  });
  const existingIds = new Set(existing.map((s) => s.id));
  const inputSet = new Set(input.orderedSectionIds);

  if (input.orderedSectionIds.length !== existing.length || inputSet.size !== existing.length) {
    throw new McpValidationError(
      `orderedSectionIds must contain every section exactly once (have ${existing.length}, got ${input.orderedSectionIds.length} unique=${inputSet.size})`
    );
  }
  for (const id of input.orderedSectionIds) {
    if (!existingIds.has(id)) {
      throw new McpValidationError(`section ${id} does not belong to assessment ${input.assessmentId}`);
    }
  }

  await prisma.$transaction(async (tx) => {
    for (let i = 0; i < input.orderedSectionIds.length; i++) {
      await tx.section.update({
        where: { id: input.orderedSectionIds[i] },
        data: { sortOrder: i },
      });
    }
  });

  const updated = await prisma.section.findMany({
    where: { versionId: latestVersionId },
    orderBy: { sortOrder: "asc" },
  });
  return updated.map((s) => ({
    id: s.id,
    title: s.title,
    slug: s.slug,
    description: s.description,
    weight: s.weight,
    sortOrder: s.sortOrder,
  }));
}

// ─── set_section_weights (validated bulk weight setter) ──────────

export interface SetSectionWeightsInput {
  assessmentId: string;
  /** Must include every section in the latest version exactly once. Sum must = 1.0. */
  weights: Array<{ sectionId: string; weight: number }>;
}

export async function setSectionWeights(input: SetSectionWeightsInput): Promise<SectionRecord[]> {
  const { latestVersionId } = await assertAssessmentExists(input.assessmentId);
  await assertVersionEditable({ versionId: latestVersionId });
  const existing = await prisma.section.findMany({
    where: { versionId: latestVersionId },
    select: { id: true },
  });
  const existingIds = new Set(existing.map((s) => s.id));

  if (input.weights.length !== existing.length) {
    throw new McpValidationError(
      `must provide a weight for every section (have ${existing.length}, got ${input.weights.length})`
    );
  }
  const seen = new Set<string>();
  for (const w of input.weights) {
    if (!existingIds.has(w.sectionId)) {
      throw new McpValidationError(`section ${w.sectionId} does not belong to assessment ${input.assessmentId}`);
    }
    if (seen.has(w.sectionId)) {
      throw new McpValidationError(`section ${w.sectionId} appears more than once`);
    }
    seen.add(w.sectionId);
    if (w.weight < 0 || w.weight > 1) {
      throw new McpValidationError(`weight for section ${w.sectionId} must be 0..1 (got ${w.weight})`);
    }
  }
  assertWeightsSumToOne(input.weights.map((w) => w.weight), "section");

  await prisma.$transaction(async (tx) => {
    for (const w of input.weights) {
      await tx.section.update({ where: { id: w.sectionId }, data: { weight: w.weight } });
    }
  });

  const updated = await prisma.section.findMany({
    where: { versionId: latestVersionId },
    orderBy: { sortOrder: "asc" },
  });
  return updated.map((s) => ({
    id: s.id,
    title: s.title,
    slug: s.slug,
    description: s.description,
    weight: s.weight,
    sortOrder: s.sortOrder,
  }));
}

```