---
type: source
source_type: laptop
title: versions
slug: versions
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/versions.ts
original_size: 10013
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# versions

_Extracted from `[[assessify|assessify]]/src/lib/operations/versions.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertAssessmentExists,
  McpValidationError,
} from "@/lib/mcp/validation";

// ─── list_assessment_versions ─────────────────────────────────────

export interface VersionSummary {
  id: string;
  assessmentId: string;
  versionNumber: number;
  status: string;
  publishedAt: Date | null;
  createdAt: Date;
  sessionsCount: number;
}

export async function listAssessmentVersions(assessmentId: string): Promise<VersionSummary[]> {
  await assertAssessmentExists(assessmentId);
  const versions = await prisma.assessmentVersion.findMany({
    where: { templateId: assessmentId },
    orderBy: { versionNumber: "desc" },
    include: { _count: { select: { candidateSessions: true } } },
  });
  return versions.map((v) => ({
    id: v.id,
    assessmentId: v.templateId,
    versionNumber: v.versionNumber,
    status: v.status,
    publishedAt: v.publishedAt,
    createdAt: v.createdAt,
    sessionsCount: v._count.candidateSessions,
  }));
}

// ─── get_assessment_version ───────────────────────────────────────

export async function getAssessmentVersion(versionId: string) {
  const v = await prisma.assessmentVersion.findUnique({
    where: { id: versionId },
    include: {
      template: { select: { id: true, title: true } },
      sections: {
        orderBy: { sortOrder: "asc" },
        include: {
          questions: {
            orderBy: { sortOrder: "asc" },
            include: {
              options: { orderBy: { sortOrder: "asc" } },
              competencies: { include: { competency: true } },
            },
          },
        },
      },
    },
  });
  if (!v) throw new McpValidationError(`version not found: ${versionId}`);
  return {
    id: v.id,
    assessmentId: v.templateId,
    assessmentTitle: v.template.title,
    versionNumber: v.versionNumber,
    status: v.status,
    passingScore: v.passingScore,
    timeLimit: v.timeLimit,
    recommendationThresholds: v.recommendationThresholds ? JSON.parse(v.recommendationThresholds) : null,
    publishedAt: v.publishedAt,
    sections: v.sections.map((s) => ({
      id: s.id,
      title: s.title,
      slug: s.slug,
      weight: s.weight,
      sortOrder: s.sortOrder,
      questions: s.questions.map((q) => ({
        id: q.id,
        title: q.title,
        prompt: q.prompt,
        questionType: q.questionType,
        difficulty: q.difficulty,
        maxPoints: q.maxPoints,
        sortOrder: q.sortOrder,
        options: q.options.map((o) => ({ key: o.key, label: o.label, points: o.points })),
        competencyIds: q.competencies.map((c) => c.competencyId),
      })),
    })),
  };
}

// ─── create_new_version ───────────────────────────────────────────

/** Snapshot a source version's full tree into a new draft on the same template.
 * The source version is unchanged. The new draft is returned. */
export async function createNewVersion(args: {
  assessmentId: string;
  copyFrom?: "latest" | string;
}): Promise<VersionSummary> {
  await assertAssessmentExists(args.assessmentId);

  let source;
  if (args.copyFrom && args.copyFrom !== "latest") {
    source = await prisma.assessmentVersion.findUnique({
      where: { id: args.copyFrom },
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
    });
    if (!source || source.templateId !== args.assessmentId) {
      throw new McpValidationError(
        `version ${args.copyFrom} not found under assessment ${args.assessmentId}`
      );
    }
  } else {
    source = await prisma.assessmentVersion.findFirst({
      where: { templateId: args.assessmentId },
      orderBy: { versionNumber: "desc" },
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
    });
    if (!source) throw new McpValidationError(`assessment ${args.assessmentId} has no versions`);
  }

  const max = await prisma.assessmentVersion.findFirst({
    where: { templateId: args.assessmentId },
    orderBy: { versionNumber: "desc" },
    select: { versionNumber: true },
  });
  const nextVersionNumber = (max?.versionNumber ?? 0) + 1;

  const newVersion = await prisma.$transaction(async (tx) => {
    const v = await tx.assessmentVersion.create({
      data: {
        templateId: args.assessmentId,
        versionNumber: nextVersionNumber,
        status: "draft",
        passingScore: source!.passingScore,
        timeLimit: source!.timeLimit,
        recommendationThresholds: source!.recommendationThresholds,
      },
    });
    for (const s of source!.sections) {
      const newSection = await tx.section.create({
        data: {
          versionId: v.id,
          title: s.title,
          slug: s.slug,
          description: s.description,
          introText: s.introText,
          iconName: s.iconName,
          weight: s.weight,
          sortOrder: s.sortOrder,
        },
      });
      for (const q of s.questions) {
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
            data: q.options.map((o) => ({
              questionId: newQ.id,
              key: o.key,
              label: o.label,
              value: o.value,
              points: o.points,
              isCorrect: o.isCorrect,
              sortOrder: o.sortOrder,
              metadata: o.metadata,
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
      }
    }
    return v;
  });

  return {
    id: newVersion.id,
    assessmentId: args.assessmentId,
    versionNumber: newVersion.versionNumber,
    status: newVersion.status,
    publishedAt: newVersion.publishedAt,
    createdAt: newVersion.createdAt,
    sessionsCount: 0,
  };
}

// ─── publish_version ──────────────────────────────────────────────

export async function publishVersion(versionId: string): Promise<{
  versionId: string;
  publishedAt: Date;
  archivedPreviousId: string | null;
}> {
  const target = await prisma.assessmentVersion.findUnique({
    where: { id: versionId },
    select: { id: true, templateId: true, status: true },
  });
  if (!target) throw new McpValidationError(`version not found: ${versionId}`);
  if (target.status === "archived") {
    throw new McpValidationError(`cannot publish an archived version (${versionId}); revert_to_version instead`);
  }

  const now = new Date();
  let archivedPreviousId: string | null = null;

  await prisma.$transaction(async (tx) => {
    const previouslyPublished = await tx.assessmentVersion.findFirst({
      where: {
        templateId: target.templateId,
        status: "published",
        id: { not: versionId },
      },
      select: { id: true },
    });
    if (previouslyPublished) {
      await tx.assessmentVersion.update({
        where: { id: previouslyPublished.id },
        data: { status: "archived" },
      });
      archivedPreviousId = previouslyPublished.id;
    }
    await tx.assessmentVersion.update({
      where: { id: versionId },
      data: { status: "published", publishedAt: now },
    });
  });

  return { versionId, publishedAt: now, archivedPreviousId };
}

// ─── revert_to_version ────────────────────────────────────────────

/** Clone the target version's tree into a new draft, then publish that draft.
 * The target row stays as a historical record. Returns the new version + the
 * version that got archived as a side-effect of publishing. */
export async function revertToVersion(args: {
  assessmentId: string;
  versionId: string;
}): Promise<{
  newVersionId: string;
  newVersionNumber: number;
  archivedPreviousId: string | null;
}> {
  const fresh = await createNewVersion({ assessmentId: args.assessmentId, copyFrom: args.versionId });
  const published = await publishVersion(fresh.id);
  return {
    newVersionId: fresh.id,
    newVersionNumber: fresh.versionNumber,
    archivedPreviousId: published.archivedPreviousId,
  };
}

```