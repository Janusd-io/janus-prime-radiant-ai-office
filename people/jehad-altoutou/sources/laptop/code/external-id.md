---
type: source
source_type: laptop
title: external-id
slug: external-id
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/operations/external-id.ts
original_size: 2240
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
---

# external-id

_Extracted from `[[assessify|assessify]]/src/lib/operations/external-id.ts` on 2026-05-14._

```typescript
import { prisma } from "@/lib/db";

/**
 * Entity types that support optional caller-supplied `externalId` for
 * idempotent create_* operations. The string value is what callers (and the
 * lookup tool) pass — keep it stable; admin integrations key on it.
 */
export type ExternalIdType =
  | "assessment"
  | "candidate_invite"
  | "competency"
  | "department"
  | "job_role"
  | "question";

const TABLE_BY_TYPE: Record<ExternalIdType, string> = {
  assessment: "assessmentTemplate",
  candidate_invite: "candidateInvite",
  competency: "competency",
  department: "department",
  job_role: "jobRole",
  question: "question",
};

/**
 * Fetches the existing record for `(type, externalId)` if one exists. Used by
 * create_* handlers to short-circuit duplicate calls — the caller is expected
 * to wrap the response with `{ idempotent: true, ... }` before returning.
 *
 * Returns null if no record matches.
 */
export async function findByExternalId(
  type: ExternalIdType,
  externalId: string
): Promise<{ id: string; record: unknown } | null> {
  const table = TABLE_BY_TYPE[type];
  // Prisma client is dynamically indexed; we cast to keep TS happy without
  // enumerating every model.
  const client = prisma as unknown as Record<
    string,
    { findUnique: (args: { where: { externalId: string } }) => Promise<unknown> }
  >;
  const row = await client[table].findUnique({ where: { externalId } });
  if (!row) return null;
  return { id: (row as { id: string }).id, record: row };
}

/** Public lookup (read-only) used by the `lookup_by_external_id` MCP tool. */
export async function lookupByExternalId(args: {
  type: ExternalIdType;
  externalId: string;
}): Promise<{ type: ExternalIdType; externalId: string; found: boolean; record: unknown | null }> {
  if (!args.type || !args.externalId) {
    throw new Error("type and externalId required");
  }
  if (!(args.type in TABLE_BY_TYPE)) {
    throw new Error(
      `unknown type "${args.type}" — must be one of: ${Object.keys(TABLE_BY_TYPE).join(", ")}`
    );
  }
  const hit = await findByExternalId(args.type, args.externalId);
  return {
    type: args.type,
    externalId: args.externalId,
    found: hit !== null,
    record: hit?.record ?? null,
  };
}

```