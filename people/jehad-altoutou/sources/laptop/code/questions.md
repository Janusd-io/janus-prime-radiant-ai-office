---
type: source
source_type: laptop
title: questions
slug: questions
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/questions.ts
original_size: 16910
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# questions

_Extracted from `assessify/src/lib/operations/questions.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertCompetencyIdsExist,
  assertMcqOptionsHaveCorrect,
  assertQuestionExists,
  assertSectionExists,
  assertVersionEditable,
  McpValidationError,
} from "@/lib/mcp/validation";

const MCQ_TYPES = new Set(["single_select", "multi_select"]);

const QUESTION_TYPES = new Set([
  "single_select",
  "multi_select",
  "scenario",
  "ranking",
  "situational_judgment",
  "short_text",
  "confidence_rating",
  "drag_order",
  "troubleshoot_sim",
  "branching",
]);

function slugify(s: string): string {
  return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

const LETTER_KEYS = "abcdefghijklmnopqrstuvwxyz";

function letterKey(i: number): string {
  return LETTER_KEYS[i] ?? `opt${i}`;
}

export interface QuestionOptionInput {
  label: string;
  points: number;
  /** Optional override; auto-derived from label if omitted. */
  value?: string;
}

export interface QuestionRecord {
  id: string;
  sectionId: string;
  title: string;
  prompt: string;
  questionType: string;
  difficulty: string;
  maxPoints: number;
  sortOrder: number;
  options: Array<{ key: string; label: string; points: number; isCorrect: boolean; sortOrder: number }>;
  competencyIds: string[];
}

async function loadQuestion(id: string): Promise<QuestionRecord> {
  const q = await prisma.question.findUnique({
    where: { id },
    include: {
      options: { orderBy: { sortOrder: "asc" } },
      competencies: { select: { competencyId: true } },
    },
  });
  if (!q) throw new McpValidationError(`question vanished: ${id}`);
  return {
    id: q.id,
    sectionId: q.sectionId,
    title: q.title,
    prompt: q.prompt,
    questionType: q.questionType,
    difficulty: q.difficulty,
    maxPoints: q.maxPoints,
    sortOrder: q.sortOrder,
    options: q.options.map((o) => ({
      key: o.key,
      label: o.label,
      points: o.points,
      isCorrect: o.isCorrect,
      sortOrder: o.sortOrder,
    })),
    competencyIds: q.competencies.map((c) => c.competencyId),
  };
}

function validateQuestionType(t: string): void {
  if (!QUESTION_TYPES.has(t)) {
    throw new McpValidationError(`unknown questionType: ${t}`);
  }
}

// ─── add_question ────────────────────────────────────────────────

export interface AddQuestionInput {
  sectionId: string;
  prompt: string;
  questionType: string;
  title?: string;
  difficulty?: string;
  maxPoints?: number;
  options?: QuestionOptionInput[];
  competencyIds?: string[];
  scoringStrategy?: string;
  explanation?: string;
}

export async function addQuestion(input: AddQuestionInput): Promise<QuestionRecord> {
  const { versionId } = await assertSectionExists(input.sectionId);
  await assertVersionEditable({ versionId });
  validateQuestionType(input.questionType);

  const isMcq = MCQ_TYPES.has(input.questionType);
  const options = input.options ?? [];
  if (isMcq) {
    assertMcqOptionsHaveCorrect(input.questionType, options);
  }
  if (input.competencyIds?.length) {
    await assertCompetencyIdsExist(input.competencyIds);
  }
  if (input.maxPoints !== undefined && input.maxPoints <= 0) {
    throw new McpValidationError("maxPoints must be > 0");
  }

  const title = input.title?.trim() || input.prompt.slice(0, 60);
  const existingCount = await prisma.question.count({ where: { sectionId: input.sectionId } });
  const baseSlug = slugify(`${title}-${existingCount + 1}`);

  // Avoid sectionId+slug unique-constraint collision
  const taken = new Set(
    (await prisma.question.findMany({
      where: { sectionId: input.sectionId },
      select: { slug: true },
    })).map((r) => r.slug)
  );
  let slug = baseSlug;
  let n = 2;
  while (taken.has(slug)) slug = `${baseSlug}-${n++}`;

  const created = await prisma.$transaction(async (tx) => {
    const q = await tx.question.create({
      data: {
        sectionId: input.sectionId,
        slug,
        title,
        prompt: input.prompt,
        questionType: input.questionType,
        difficulty: input.difficulty ?? "medium",
        maxPoints: input.maxPoints ?? 1,
        weight: 1,
        scoringStrategy: input.scoringStrategy ?? (isMcq ? "weighted_options" : "exact"),
        explanation: input.explanation ?? null,
        sortOrder: existingCount,
      },
    });
    if (options.length > 0) {
      await tx.answerOption.createMany({
        data: options.map((o, i) => ({
          questionId: q.id,
          key: letterKey(i),
          label: o.label,
          value: o.value ?? o.label,
          points: o.points,
          isCorrect: o.points > 0,
          sortOrder: i,
        })),
      });
    }
    if (input.competencyIds?.length) {
      await tx.questionCompetency.createMany({
        data: input.competencyIds.map((cid) => ({
          questionId: q.id,
          competencyId: cid,
          weight: 1.0,
        })),
      });
    }
    return q;
  });

  return loadQuestion(created.id);
}

// ─── update_question ─────────────────────────────────────────────

export interface UpdateQuestionInput {
  questionId: string;
  prompt?: string;
  title?: string;
  questionType?: string;
  difficulty?: string;
  maxPoints?: number;
  /** If provided, REPLACES all existing options. Pass [] to clear. */
  options?: QuestionOptionInput[];
  /** If provided, REPLACES all existing competency tags. Pass [] to clear. */
  competencyIds?: string[];
  scoringStrategy?: string;
  explanation?: string;
}

export async function updateQuestion(input: UpdateQuestionInput): Promise<QuestionRecord> {
  const q = await assertQuestionExists(input.questionId);
  if (q.sectionId) {
    const sec = await prisma.section.findUnique({
      where: { id: q.sectionId },
      select: { versionId: true },
    });
    if (sec) await assertVersionEditable({ versionId: sec.versionId });
  }

  // Determine effective questionType (existing or new) for MCQ validation
  const existing = await prisma.question.findUnique({
    where: { id: input.questionId },
    select: { questionType: true },
  });
  const effectiveType = input.questionType ?? existing!.questionType;

  if (input.questionType !== undefined) {
    validateQuestionType(input.questionType);
  }
  if (input.options !== undefined) {
    if (MCQ_TYPES.has(effectiveType)) {
      assertMcqOptionsHaveCorrect(effectiveType, input.options);
    }
  }
  if (input.competencyIds !== undefined) {
    await assertCompetencyIdsExist(input.competencyIds);
  }
  if (input.maxPoints !== undefined && input.maxPoints <= 0) {
    throw new McpValidationError("maxPoints must be > 0");
  }

  await prisma.$transaction(async (tx) => {
    const data: Record<string, unknown> = {};
    if (input.prompt !== undefined) data.prompt = input.prompt;
    if (input.title !== undefined) data.title = input.title;
    if (input.questionType !== undefined) data.questionType = input.questionType;
    if (input.difficulty !== undefined) data.difficulty = input.difficulty;
    if (input.maxPoints !== undefined) data.maxPoints = input.maxPoints;
    if (input.scoringStrategy !== undefined) data.scoringStrategy = input.scoringStrategy;
    if (input.explanation !== undefined) data.explanation = input.explanation;
    if (Object.keys(data).length > 0) {
      await tx.question.update({ where: { id: input.questionId }, data });
    }
    if (input.options !== undefined) {
      await tx.answerOption.deleteMany({ where: { questionId: input.questionId } });
      if (input.options.length > 0) {
        await tx.answerOption.createMany({
          data: input.options.map((o, i) => ({
            questionId: input.questionId,
            key: letterKey(i),
            label: o.label,
            value: o.value ?? o.label,
            points: o.points,
            isCorrect: o.points > 0,
            sortOrder: i,
          })),
        });
      }
    }
    if (input.competencyIds !== undefined) {
      await tx.questionCompetency.deleteMany({ where: { questionId: input.questionId } });
      if (input.competencyIds.length > 0) {
        await tx.questionCompetency.createMany({
          data: input.competencyIds.map((cid) => ({
            questionId: input.questionId,
            competencyId: cid,
            weight: 1.0,
          })),
        });
      }
    }
  });

  return loadQuestion(input.questionId);
}

// ─── reorder_questions ────────────────────────────────────────────

export interface ReorderQuestionsInput {
  sectionId: string;
  /** Question IDs in desired order. Must include every question in the section exactly once. */
  orderedQuestionIds: string[];
}

export async function reorderQuestions(input: ReorderQuestionsInput): Promise<QuestionRecord[]> {
  const { versionId } = await assertSectionExists(input.sectionId);
  await assertVersionEditable({ versionId });
  const existing = await prisma.question.findMany({
    where: { sectionId: input.sectionId },
    select: { id: true },
  });
  const existingIds = new Set(existing.map((q) => q.id));
  const inputSet = new Set(input.orderedQuestionIds);

  if (input.orderedQuestionIds.length !== existing.length || inputSet.size !== existing.length) {
    throw new McpValidationError(
      `orderedQuestionIds must contain every question exactly once (have ${existing.length}, got ${input.orderedQuestionIds.length} unique=${inputSet.size})`
    );
  }
  for (const id of input.orderedQuestionIds) {
    if (!existingIds.has(id)) {
      throw new McpValidationError(`question ${id} does not belong to section ${input.sectionId}`);
    }
  }

  await prisma.$transaction(async (tx) => {
    for (let i = 0; i < input.orderedQuestionIds.length; i++) {
      await tx.question.update({
        where: { id: input.orderedQuestionIds[i] },
        data: { sortOrder: i },
      });
    }
  });

  const ids = input.orderedQuestionIds;
  const out: QuestionRecord[] = [];
  for (const id of ids) out.push(await loadQuestion(id));
  return out;
}

// ─── create_question (Bank standalone) ───────────────────────────

const BANK_SECTIONS: Record<string, { title: string; slug: string }> = {
  "cultural-fit": { title: "Cultural Fit", slug: "cultural-fit" },
  "ai-awareness": { title: "AI Awareness", slug: "ai-awareness" },
  "department-specific": { title: "Department-Specific", slug: "department-specific" },
  general: { title: "General", slug: "library" },
};

export interface CreateBankQuestionInput {
  departmentId: string;
  bankSectionSlug?: keyof typeof BANK_SECTIONS;
  prompt: string;
  questionType: string;
  title?: string;
  difficulty?: string;
  maxPoints?: number;
  options?: QuestionOptionInput[];
  competencyIds?: string[];
  scoringStrategy?: string;
  explanation?: string;
}

/**
 * Creates a question inside the department's hidden "library-<slug>" template,
 * mirroring the existing portal Question Bank pattern. The schema requires
 * sectionId NOT NULL, so standalone Bank items live in a dedicated library
 * template + section.
 */
export async function createBankQuestion(input: CreateBankQuestionInput): Promise<QuestionRecord> {
  validateQuestionType(input.questionType);
  const isMcq = MCQ_TYPES.has(input.questionType);
  if (isMcq) {
    assertMcqOptionsHaveCorrect(input.questionType, input.options ?? []);
  }
  if (input.competencyIds?.length) {
    await assertCompetencyIdsExist(input.competencyIds);
  }

  const dept = await prisma.department.findUnique({ where: { id: input.departmentId } });
  if (!dept) throw new McpValidationError(`department not found: ${input.departmentId}`);

  const target = BANK_SECTIONS[input.bankSectionSlug ?? "general"] ?? BANK_SECTIONS.general;
  const librarySlug = `library-${dept.slug}`;

  // Find or create the library template + version + section
  let libraryTemplate = await prisma.assessmentTemplate.findUnique({
    where: { slug: librarySlug },
    include: { versions: { include: { sections: true } } },
  });

  if (!libraryTemplate) {
    let placeholderRole = await prisma.jobRole.findFirst({ where: { departmentId: dept.id } });
    if (!placeholderRole) {
      placeholderRole = await prisma.jobRole.create({
        data: {
          departmentId: dept.id,
          title: "Question Library",
          slug: `library-role-${dept.slug}-${Date.now()}`,
          description: "Internal — holds standalone bank questions",
          isActive: false,
        },
      });
    }
    libraryTemplate = await prisma.assessmentTemplate.create({
      data: {
        jobRoleId: placeholderRole.id,
        title: `${dept.name} Question Library`,
        slug: librarySlug,
        description: "Standalone questions added to the bank",
        isActive: false,
        versions: {
          create: { versionNumber: 1, status: "draft", passingScore: 0.6 },
        },
      },
      include: { versions: { include: { sections: true } } },
    });
  }

  const version = libraryTemplate.versions[0];
  let section = version.sections.find((s) => s.slug === target.slug);
  if (!section) {
    section = await prisma.section.create({
      data: {
        versionId: version.id,
        title: target.title,
        slug: target.slug,
        sortOrder: version.sections.length,
        weight: 0.33,
      },
    });
  }

  return addQuestion({
    sectionId: section.id,
    prompt: input.prompt,
    questionType: input.questionType,
    title: input.title,
    difficulty: input.difficulty,
    maxPoints: input.maxPoints,
    options: input.options,
    competencyIds: input.competencyIds,
    scoringStrategy: input.scoringStrategy,
    explanation: input.explanation,
  });
}

// ─── attach_question_to_section (clones a Bank question) ────────

export interface AttachQuestionInput {
  /** Source question ID — typically a Bank entry */
  questionId: string;
  /** Target section to copy into */
  sectionId: string;
}

/**
 * Schema is one-to-many (Question.sectionId is NOT NULL and singular), so
 * "attach" actually clones the question (with its options + competency tags)
 * into the target section. The original stays put — useful for reusing Bank
 * items across multiple assessments without coupling.
 */
export async function attachQuestionToSection(input: AttachQuestionInput): Promise<QuestionRecord> {
  const source = await prisma.question.findUnique({
    where: { id: input.questionId },
    include: {
      options: { orderBy: { sortOrder: "asc" } },
      competencies: { select: { competencyId: true } },
    },
  });
  if (!source) throw new McpValidationError(`source question not found: ${input.questionId}`);
  const { versionId } = await assertSectionExists(input.sectionId);
  await assertVersionEditable({ versionId });

  const cloned = await addQuestion({
    sectionId: input.sectionId,
    prompt: source.prompt,
    questionType: source.questionType,
    title: source.title,
    difficulty: source.difficulty,
    maxPoints: source.maxPoints,
    options: source.options.map((o) => ({ label: o.label, points: o.points, value: o.value })),
    competencyIds: source.competencies.map((c) => c.competencyId),
    scoringStrategy: source.scoringStrategy,
    explanation: source.explanation ?? undefined,
  });
  return cloned;
}

// ─── detach_question_from_section (delete) ───────────────────────

export interface DetachQuestionInput {
  questionId: string;
}

/**
 * Removes a question from its section. Hard-deletes the question + options +
 * competency junctions. Distinct from delete_question only in name — same
 * effect. Refuses if any candidate has answered it.
 */
export async function detachQuestionFromSection(input: DetachQuestionInput): Promise<{ ok: true; questionId: string }> {
  const q = await assertQuestionExists(input.questionId);
  if (q.sectionId) {
    const sec = await prisma.section.findUnique({
      where: { id: q.sectionId },
      select: { versionId: true },
    });
    if (sec) await assertVersionEditable({ versionId: sec.versionId });
  }
  const responseCount = await prisma.candidateResponse.count({
    where: { questionId: input.questionId },
  });
  if (responseCount > 0) {
    throw new McpValidationError(
      `cannot detach: question has ${responseCount} candidate response(s).`
    );
  }
  await prisma.$transaction(async (tx) => {
    await tx.questionCompetency.deleteMany({ where: { questionId: input.questionId } });
    await tx.answerOption.deleteMany({ where: { questionId: input.questionId } });
    await tx.question.delete({ where: { id: input.questionId } });
  });
  return { ok: true, questionId: input.questionId };
}

```