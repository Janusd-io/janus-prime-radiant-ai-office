---
type: source
source_type: laptop
title: duplicates
slug: duplicates
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/duplicates.ts
original_size: 9449
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# duplicates

_Extracted from `[[assessify|assessify]]/src/lib/operations/duplicates.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { McpValidationError } from "@/lib/mcp/validation";

function slugify(s: string): string {
  return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

const LETTER_KEYS = "abcdefghijklmnopqrstuvwxyz";
const letterKey = (i: number) => LETTER_KEYS[i] ?? `opt${i}`;

// ─── duplicate_assessment ──────────────────────────────────────────

export interface DuplicateAssessmentInput {
  assessmentId: string;
  newTitle: string;
  newJobRoleId?: string;
}

export interface DuplicateAssessmentResult {
  id: string;
  title: string;
  slug: string;
  versionId: string;
  sourceAssessmentId: string;
  sectionCount: number;
  questionCount: number;
}

/**
 * Deep-copies an assessment's latest version (sections, questions, options,
 * competency tags, weights, thresholds) into a NEW draft assessment template.
 * The new template is isActive=false and starts at versionNumber=1.
 *
 * Useful for "I want to spin up a Senior Eng assessment from the Eng one and
 * tweak a few questions" — without entangling the histories.
 */
export async function duplicateAssessment(
  input: DuplicateAssessmentInput
): Promise<DuplicateAssessmentResult> {
  if (!input.newTitle?.trim()) throw new McpValidationError("newTitle required");

  const source = await prisma.assessmentTemplate.findUnique({
    where: { id: input.assessmentId },
    include: {
      versions: {
        orderBy: { versionNumber: "desc" },
        take: 1,
        include: {
          sections: {
            orderBy: { sortOrder: "asc" },
            include: {
              questions: {
                orderBy: { sortOrder: "asc" },
                include: {
                  options: { orderBy: { sortOrder: "asc" } },
                  competencies: { select: { competencyId: true, weight: true } },
                },
              },
            },
          },
        },
      },
    },
  });
  if (!source) throw new McpValidationError(`assessment not found: ${input.assessmentId}`);
  const sourceVersion = source.versions[0];
  if (!sourceVersion) throw new McpValidationError(`source assessment has no version`);

  const targetJobRoleId = input.newJobRoleId ?? source.jobRoleId;
  const targetRole = await prisma.jobRole.findUnique({
    where: { id: targetJobRoleId },
    select: { id: true },
  });
  if (!targetRole) throw new McpValidationError(`job role not found: ${targetJobRoleId}`);

  const baseSlug = slugify(input.newTitle);
  if (!baseSlug) throw new McpValidationError("newTitle must produce a non-empty slug");
  let slug = baseSlug;
  let n = 2;
  // The slug is globally unique on AssessmentTemplate
  while (await prisma.assessmentTemplate.findUnique({ where: { slug } })) {
    slug = `${baseSlug}-${n++}`;
    if (n > 100) throw new McpValidationError(`could not allocate a unique slug for "${input.newTitle}"`);
  }

  let totalQuestions = 0;

  const created = await prisma.$transaction(async (tx) => {
    const tpl = await tx.assessmentTemplate.create({
      data: {
        jobRoleId: targetJobRoleId,
        title: input.newTitle,
        slug,
        description: source.description,
        isActive: false,
      },
    });
    const ver = await tx.assessmentVersion.create({
      data: {
        templateId: tpl.id,
        versionNumber: 1,
        status: "draft",
        passingScore: sourceVersion.passingScore,
        timeLimit: sourceVersion.timeLimit,
        recommendationThresholds: sourceVersion.recommendationThresholds,
      },
    });

    for (const s of sourceVersion.sections) {
      const newSection = await tx.section.create({
        data: {
          versionId: ver.id,
          title: s.title,
          slug: s.slug,
          description: s.description,
          introText: s.introText,
          iconName: s.iconName,
          sortOrder: s.sortOrder,
          weight: s.weight,
          isActive: s.isActive,
        },
      });
      for (let qi = 0; qi < s.questions.length; qi++) {
        const q = s.questions[qi];
        const newQ = await tx.question.create({
          data: {
            sectionId: newSection.id,
            slug: q.slug,
            title: q.title,
            prompt: q.prompt,
            questionType: q.questionType,
            difficulty: q.difficulty,
            maxPoints: q.maxPoints,
            weight: q.weight,
            scoringStrategy: q.scoringStrategy,
            correctAnswerKey: q.correctAnswerKey,
            rubric: q.rubric,
            partialCreditRules: q.partialCreditRules,
            knockoutFlag: q.knockoutFlag,
            knockoutThreshold: q.knockoutThreshold,
            automationLabel: q.automationLabel,
            analyticsLabel: q.analyticsLabel,
            explanation: q.explanation,
            sortOrder: q.sortOrder,
            isActive: q.isActive,
          },
        });
        if (q.options.length > 0) {
          await tx.answerOption.createMany({
            data: q.options.map((o, i) => ({
              questionId: newQ.id,
              key: letterKey(i),
              label: o.label,
              value: o.value,
              points: o.points,
              isCorrect: o.isCorrect,
              sortOrder: o.sortOrder,
            })),
          });
        }
        if (q.competencies.length > 0) {
          await tx.questionCompetency.createMany({
            data: q.competencies.map((c) => ({
              questionId: newQ.id,
              competencyId: c.competencyId,
              weight: c.weight,
            })),
          });
        }
        totalQuestions++;
      }
    }

    return { tpl, ver };
  });

  return {
    id: created.tpl.id,
    title: created.tpl.title,
    slug: created.tpl.slug,
    versionId: created.ver.id,
    sourceAssessmentId: input.assessmentId,
    sectionCount: sourceVersion.sections.length,
    questionCount: totalQuestions,
  };
}

// ─── duplicate_question ────────────────────────────────────────────

export interface DuplicateQuestionInput {
  questionId: string;
  newSectionId?: string;
}

export interface DuplicateQuestionResult {
  id: string;
  sectionId: string;
  sourceQuestionId: string;
}

/**
 * Clones a question (options + competency tags) into the same section, or a
 * different one if `newSectionId` is given. The new question is independent —
 * editing it does not touch the source.
 *
 * Functionally identical to attach_question_to_section; named for the workflow
 * "I have a great question, give me a tweakable copy".
 */
export async function duplicateQuestion(
  input: DuplicateQuestionInput
): Promise<DuplicateQuestionResult> {
  const source = await prisma.question.findUnique({
    where: { id: input.questionId },
    include: {
      options: { orderBy: { sortOrder: "asc" } },
      competencies: { select: { competencyId: true, weight: true } },
    },
  });
  if (!source) throw new McpValidationError(`question not found: ${input.questionId}`);

  const targetSectionId = input.newSectionId ?? source.sectionId;
  const target = await prisma.section.findUnique({
    where: { id: targetSectionId },
    select: { id: true },
  });
  if (!target) throw new McpValidationError(`section not found: ${targetSectionId}`);

  // Allocate a unique slug within the target section.
  const taken = new Set(
    (
      await prisma.question.findMany({
        where: { sectionId: targetSectionId },
        select: { slug: true },
      })
    ).map((r) => r.slug)
  );
  let slug = `${source.slug}-copy`;
  let n = 2;
  while (taken.has(slug)) slug = `${source.slug}-copy-${n++}`;

  const sortOrder = await prisma.question.count({ where: { sectionId: targetSectionId } });

  const created = await prisma.$transaction(async (tx) => {
    const q = await tx.question.create({
      data: {
        sectionId: targetSectionId,
        slug,
        title: source.title,
        prompt: source.prompt,
        questionType: source.questionType,
        difficulty: source.difficulty,
        maxPoints: source.maxPoints,
        weight: source.weight,
        scoringStrategy: source.scoringStrategy,
        correctAnswerKey: source.correctAnswerKey,
        rubric: source.rubric,
        partialCreditRules: source.partialCreditRules,
        knockoutFlag: source.knockoutFlag,
        knockoutThreshold: source.knockoutThreshold,
        automationLabel: source.automationLabel,
        analyticsLabel: source.analyticsLabel,
        explanation: source.explanation,
        sortOrder,
      },
    });
    if (source.options.length > 0) {
      await tx.answerOption.createMany({
        data: source.options.map((o, i) => ({
          questionId: q.id,
          key: letterKey(i),
          label: o.label,
          value: o.value,
          points: o.points,
          isCorrect: o.isCorrect,
          sortOrder: o.sortOrder,
        })),
      });
    }
    if (source.competencies.length > 0) {
      await tx.questionCompetency.createMany({
        data: source.competencies.map((c) => ({
          questionId: q.id,
          competencyId: c.competencyId,
          weight: c.weight,
        })),
      });
    }
    return q;
  });

  return {
    id: created.id,
    sectionId: targetSectionId,
    sourceQuestionId: input.questionId,
  };
}

```