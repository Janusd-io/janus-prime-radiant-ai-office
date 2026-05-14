---
type: source
source_type: laptop
title: assessments
slug: assessments
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/assessments.ts
original_size: 4405
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# assessments

_Extracted from `assessify/src/lib/operations/assessments.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import {
  assertAssessmentExists,
  assertJobRoleExists,
  assertThresholds,
  assertVersionEditable,
  McpValidationError,
} from "@/lib/mcp/validation";

export interface UpdateAssessmentInput {
  /** AssessmentTemplate id */
  id: string;
  title?: string;
  description?: string;
  jobRoleId?: string;
  /** Minutes; 0 or null = unlimited. Updates the latest version. */
  timeLimit?: number | null;
  /** 0..1 — pass threshold on the latest version. */
  passingScore?: number;
  thresholds?: { strongHire: number; hire: number; consider: number };
  /** Show the egg-hunt CTA on the candidate result page. */
  eggHuntEnabled?: boolean;
}

export interface UpdateAssessmentResult {
  id: string;
  title: string;
  description: string | null;
  jobRoleId: string;
  isActive: boolean;
  eggHuntEnabled: boolean;
  latestVersion: {
    id: string;
    versionNumber: number;
    timeLimit: number | null;
    passingScore: number | null;
    recommendationThresholds: unknown;
  };
}

/**
 * Update assessment metadata + latest-version settings in one atomic step.
 * Used by both the admin portal PATCH endpoint and the MCP `update_assessment` tool.
 */
export async function updateAssessment(input: UpdateAssessmentInput): Promise<UpdateAssessmentResult> {
  const { latestVersionId } = await assertAssessmentExists(input.id);

  // Title, description, jobRoleId, eggHuntEnabled live on the template — those
  // are safe to change even with in-flight sessions. timeLimit, passingScore,
  // and thresholds live on the version, so only gate when those are touched.
  const touchesVersion =
    input.timeLimit !== undefined ||
    input.passingScore !== undefined ||
    input.thresholds !== undefined;
  if (touchesVersion) {
    await assertVersionEditable({ versionId: latestVersionId });
  }

  if (input.jobRoleId !== undefined) {
    await assertJobRoleExists(input.jobRoleId);
  }
  if (input.thresholds !== undefined) {
    assertThresholds(input.thresholds);
  }
  if (input.passingScore !== undefined) {
    if (input.passingScore < 0 || input.passingScore > 1) {
      throw new McpValidationError("passingScore must be between 0 and 1");
    }
  }
  if (input.timeLimit !== undefined && input.timeLimit !== null && input.timeLimit < 0) {
    throw new McpValidationError("timeLimit must be 0 (unlimited) or positive minutes");
  }

  const templateUpdate: Record<string, unknown> = {};
  if (input.title !== undefined) templateUpdate.title = input.title;
  if (input.description !== undefined) templateUpdate.description = input.description;
  if (input.jobRoleId !== undefined) templateUpdate.jobRoleId = input.jobRoleId;
  if (input.eggHuntEnabled !== undefined) templateUpdate.eggHuntEnabled = input.eggHuntEnabled;

  const versionUpdate: Record<string, unknown> = {};
  if (input.timeLimit !== undefined) versionUpdate.timeLimit = input.timeLimit;
  if (input.passingScore !== undefined) versionUpdate.passingScore = input.passingScore;
  if (input.thresholds !== undefined) {
    versionUpdate.recommendationThresholds = JSON.stringify(input.thresholds);
  }

  await prisma.$transaction(async (tx) => {
    if (Object.keys(templateUpdate).length > 0) {
      await tx.assessmentTemplate.update({ where: { id: input.id }, data: templateUpdate });
    }
    if (Object.keys(versionUpdate).length > 0) {
      await tx.assessmentVersion.update({ where: { id: latestVersionId }, data: versionUpdate });
    }
  });

  const updated = await prisma.assessmentTemplate.findUnique({
    where: { id: input.id },
    include: {
      versions: {
        orderBy: { versionNumber: "desc" },
        take: 1,
      },
    },
  });
  if (!updated || !updated.versions[0]) {
    // Should be unreachable — assertAssessmentExists ran above.
    throw new McpValidationError(`assessment vanished mid-update: ${input.id}`);
  }
  const v = updated.versions[0];
  return {
    id: updated.id,
    title: updated.title,
    description: updated.description ?? null,
    jobRoleId: updated.jobRoleId,
    isActive: updated.isActive,
    eggHuntEnabled: updated.eggHuntEnabled,
    latestVersion: {
      id: v.id,
      versionNumber: v.versionNumber,
      timeLimit: v.timeLimit,
      passingScore: v.passingScore,
      recommendationThresholds: v.recommendationThresholds
        ? JSON.parse(v.recommendationThresholds)
        : null,
    },
  };
}

```