---
type: source
source_type: laptop
title: competencies
slug: competencies
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/competencies.ts
original_size: 4625
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# competencies

_Extracted from `[[assessify|assessify]]/src/lib/operations/competencies.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";
import { McpValidationError } from "@/lib/mcp/validation";
import { findByExternalId } from "./external-id";

function slugify(s: string): string {
  return s.toLowerCase().trim().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

export interface CompetencyRecord {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  category: string | null;
  archivedAt: Date | null;
  externalId: string | null;
}

function toRecord(row: {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  category: string | null;
  archivedAt: Date | null;
  externalId: string | null;
}): CompetencyRecord {
  return { ...row };
}

// ─── create ─────────────────────────────────────────────────────────

export interface CreateCompetencyInput {
  name: string;
  description?: string;
  category?: string;
  externalId?: string;
}

export async function createCompetency(
  input: CreateCompetencyInput
): Promise<{ record: CompetencyRecord; idempotent: boolean }> {
  if (!input.name?.trim()) throw new McpValidationError("name required");

  if (input.externalId) {
    const hit = await findByExternalId("competency", input.externalId);
    if (hit) {
      const full = await prisma.competency.findUnique({ where: { id: hit.id } });
      if (full) return { record: toRecord(full), idempotent: true };
    }
  }

  const baseSlug = slugify(input.name);
  if (!baseSlug) throw new McpValidationError("name must produce a non-empty slug");
  let slug = baseSlug;
  let n = 2;
  while (await prisma.competency.findUnique({ where: { slug } })) {
    slug = `${baseSlug}-${n++}`;
    if (n > 100) throw new McpValidationError(`could not allocate a unique slug for "${input.name}"`);
  }

  const created = await prisma.competency.create({
    data: {
      name: input.name,
      slug,
      description: input.description ?? null,
      category: input.category ?? null,
      ...(input.externalId ? { externalId: input.externalId } : {}),
    },
  });
  return { record: toRecord(created), idempotent: false };
}

// ─── update ─────────────────────────────────────────────────────────

export interface UpdateCompetencyInput {
  id: string;
  name?: string;
  description?: string;
  category?: string;
}

export async function updateCompetency(input: UpdateCompetencyInput): Promise<CompetencyRecord> {
  const existing = await prisma.competency.findUnique({ where: { id: input.id } });
  if (!existing) throw new McpValidationError(`competency not found: ${input.id}`);

  const data: { name?: string; description?: string | null; category?: string | null } = {};
  if (input.name !== undefined) {
    if (!input.name.trim()) throw new McpValidationError("name cannot be empty");
    data.name = input.name;
  }
  if (input.description !== undefined) data.description = input.description || null;
  if (input.category !== undefined) data.category = input.category || null;

  const updated = await prisma.competency.update({ where: { id: input.id }, data });
  return toRecord(updated);
}

// ─── archive ────────────────────────────────────────────────────────

export async function archiveCompetency(
  id: string
): Promise<{ id: string; archivedAt: Date }> {
  const existing = await prisma.competency.findUnique({ where: { id } });
  if (!existing) throw new McpValidationError(`competency not found: ${id}`);
  if (existing.archivedAt) {
    return { id, archivedAt: existing.archivedAt };
  }

  // Refuse if any active question (in any non-archived assessment version) is
  // tagged with this competency. Strict on purpose — admins should retag first.
  const inUse = await prisma.questionCompetency.count({
    where: {
      competencyId: id,
      question: {
        isActive: true,
        section: {
          isActive: true,
          version: { status: { in: ["draft", "published"] } },
        },
      },
    },
  });
  if (inUse > 0) {
    throw new McpValidationError(
      `cannot archive competency "${existing.name}" — it is still tagged on ${inUse} active question(s). Re-tag or archive those questions first.`
    );
  }

  const archivedAt = new Date();
  await prisma.competency.update({ where: { id }, data: { archivedAt } });
  return { id, archivedAt };
}

```