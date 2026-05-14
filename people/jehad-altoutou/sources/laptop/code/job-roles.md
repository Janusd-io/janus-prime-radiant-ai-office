---
type: source
source_type: laptop
title: job-roles
slug: job-roles
created: 2026-05-05
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/job-roles.ts
original_size: 4118
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# job-roles

_Extracted from `assessify/src/lib/operations/job-roles.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { McpValidationError } from "@/lib/mcp/validation";

export interface JobRoleRecord {
  id: string;
  title: string;
  slug: string;
  description: string | null;
  departmentId: string;
  isActive: boolean;
  externalId: string | null;
  jdSummary: string | null;
  jdResponsibilities: string | null;
  jdRequirements: string | null;
  jdNiceToHaves: string | null;
  jdYearsExperience: string | null;
}

function toRecord(row: JobRoleRecord): JobRoleRecord {
  return { ...row };
}

// ─── update ─────────────────────────────────────────────────────────

export interface UpdateJobRoleInput {
  id: string;
  title?: string;
  description?: string;
  departmentId?: string;
  jdSummary?: string;
  jdResponsibilities?: string;
  jdRequirements?: string;
  jdNiceToHaves?: string;
  jdYearsExperience?: string;
}

export async function updateJobRole(input: UpdateJobRoleInput): Promise<JobRoleRecord> {
  const existing = await prisma.jobRole.findUnique({ where: { id: input.id } });
  if (!existing) throw new McpValidationError(`job role not found: ${input.id}`);

  if (input.departmentId) {
    const dept = await prisma.department.findUnique({
      where: { id: input.departmentId },
      select: { id: true, archivedAt: true },
    });
    if (!dept) throw new McpValidationError(`department not found: ${input.departmentId}`);
    if (dept.archivedAt) {
      throw new McpValidationError(`cannot reassign to archived department ${input.departmentId}`);
    }
  }

  const trimOrNull = (v: string | undefined) => {
    if (v === undefined) return undefined;
    const t = v.trim();
    return t.length > 0 ? t : null;
  };

  const data: {
    title?: string;
    description?: string | null;
    departmentId?: string;
    jdSummary?: string | null;
    jdResponsibilities?: string | null;
    jdRequirements?: string | null;
    jdNiceToHaves?: string | null;
    jdYearsExperience?: string | null;
  } = {};
  if (input.title !== undefined) {
    if (!input.title.trim()) throw new McpValidationError("title cannot be empty");
    data.title = input.title;
  }
  if (input.description !== undefined) data.description = input.description || null;
  if (input.departmentId !== undefined) data.departmentId = input.departmentId;
  if (input.jdSummary !== undefined) data.jdSummary = trimOrNull(input.jdSummary);
  if (input.jdResponsibilities !== undefined) data.jdResponsibilities = trimOrNull(input.jdResponsibilities);
  if (input.jdRequirements !== undefined) data.jdRequirements = trimOrNull(input.jdRequirements);
  if (input.jdNiceToHaves !== undefined) data.jdNiceToHaves = trimOrNull(input.jdNiceToHaves);
  if (input.jdYearsExperience !== undefined) data.jdYearsExperience = trimOrNull(input.jdYearsExperience);

  const updated = await prisma.jobRole.update({ where: { id: input.id }, data });
  return toRecord(updated as JobRoleRecord);
}

// ─── archive ────────────────────────────────────────────────────────
//
// JobRole uses isActive (no archivedAt column). "Archive" sets isActive=false.
// Refuses if any AssessmentTemplate.isActive=true is tied to this role.

export async function archiveJobRole(id: string): Promise<{ id: string; isActive: false }> {
  const existing = await prisma.jobRole.findUnique({ where: { id } });
  if (!existing) throw new McpValidationError(`job role not found: ${id}`);
  if (!existing.isActive) return { id, isActive: false };

  const activeAssessments = await prisma.assessmentTemplate.count({
    where: { jobRoleId: id, isActive: true },
  });
  if (activeAssessments > 0) {
    throw new McpValidationError(
      `cannot archive job role "${existing.title}" — ${activeAssessments} active assessment(s) reference it. Deactivate those first.`
    );
  }

  await prisma.jobRole.update({ where: { id }, data: { isActive: false } });
  return { id, isActive: false };
}

```