---
type: source
source_type: laptop
title: Assessify — departments
slug: departments
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/departments.ts
original_size: 4040
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# departments

_Extracted from `[[assessify|assessify]]/src/lib/operations/departments.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { McpValidationError } from "@/lib/mcp/validation";
import { findByExternalId } from "./external-id";

function slugify(s: string): string {
  return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

export interface DepartmentRecord {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  archivedAt: Date | null;
  externalId: string | null;
}

function toRecord(row: {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  archivedAt: Date | null;
  externalId: string | null;
}): DepartmentRecord {
  return { ...row };
}

// ─── create ─────────────────────────────────────────────────────────

export interface CreateDepartmentInput {
  name: string;
  description?: string;
  externalId?: string;
}

export async function createDepartment(
  input: CreateDepartmentInput
): Promise<{ record: DepartmentRecord; idempotent: boolean }> {
  if (!input.name?.trim()) throw new McpValidationError("name required");

  if (input.externalId) {
    const hit = await findByExternalId("department", input.externalId);
    if (hit) {
      const full = await prisma.department.findUnique({ where: { id: hit.id } });
      if (full) return { record: toRecord(full), idempotent: true };
    }
  }

  const baseSlug = slugify(input.name);
  if (!baseSlug) throw new McpValidationError("name must produce a non-empty slug");
  let slug = baseSlug;
  let n = 2;
  while (await prisma.department.findUnique({ where: { slug } })) {
    slug = `${baseSlug}-${n++}`;
    if (n > 100) throw new McpValidationError(`could not allocate a unique slug for "${input.name}"`);
  }

  const created = await prisma.department.create({
    data: {
      name: input.name,
      slug,
      description: input.description ?? null,
      ...(input.externalId ? { externalId: input.externalId } : {}),
    },
  });
  return { record: toRecord(created), idempotent: false };
}

// ─── update ─────────────────────────────────────────────────────────

export interface UpdateDepartmentInput {
  id: string;
  name?: string;
  description?: string;
}

export async function updateDepartment(input: UpdateDepartmentInput): Promise<DepartmentRecord> {
  const existing = await prisma.department.findUnique({ where: { id: input.id } });
  if (!existing) throw new McpValidationError(`department not found: ${input.id}`);

  const data: { name?: string; description?: string | null } = {};
  if (input.name !== undefined) {
    if (!input.name.trim()) throw new McpValidationError("name cannot be empty");
    data.name = input.name;
  }
  if (input.description !== undefined) data.description = input.description || null;

  const updated = await prisma.department.update({ where: { id: input.id }, data });
  return toRecord(updated);
}

// ─── archive ────────────────────────────────────────────────────────

export async function archiveDepartment(
  id: string
): Promise<{ id: string; archivedAt: Date }> {
  const existing = await prisma.department.findUnique({ where: { id } });
  if (!existing) throw new McpValidationError(`department not found: ${id}`);
  if (existing.archivedAt) return { id, archivedAt: existing.archivedAt };

  const activeRoles = await prisma.jobRole.count({
    where: { departmentId: id, isActive: true },
  });
  if (activeRoles > 0) {
    throw new McpValidationError(
      `cannot archive department "${existing.name}" — ${activeRoles} active job role(s) still belong to it. Archive those roles first.`
    );
  }

  const archivedAt = new Date();
  await prisma.department.update({ where: { id }, data: { archivedAt } });
  return { id, archivedAt };
}

```