---
type: source
source_type: laptop
title: pagination
slug: pagination
created: 2026-04-28
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/mcp/pagination.ts
original_size: 2361
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---
<!-- jb:project-callout -->
> Part of [[assessify|Assessify]] — automatically linked by /janus-brain.


# pagination

_Extracted from `[[assessify|assessify]]/src/lib/mcp/pagination.ts` on 2026-05-14._

```typescript
/** Cursor-based pagination over rows ordered by (createdAt DESC, id DESC).
 *
 * Cursors are opaque base64 strings encoding `<createdAtISO>:<id>` so the
 * caller doesn't have to know the underlying scheme. Returns the rows plus
 * the next cursor (null if there are no more rows).
 */

const MAX_LIMIT = 100;
const DEFAULT_LIMIT = 25;

export interface CursorPaged<T> {
  rows: T[];
  nextCursor: string | null;
}

export function decodeCursor(cursor: string | null | undefined): {
  createdAt: Date;
  id: string;
} | null {
  if (!cursor) return null;
  try {
    const raw = Buffer.from(cursor, "base64").toString("utf8");
    const idx = raw.lastIndexOf(":");
    if (idx <= 0) return null;
    const iso = raw.slice(0, idx);
    const id = raw.slice(idx + 1);
    const createdAt = new Date(iso);
    if (Number.isNaN(createdAt.getTime())) return null;
    return { createdAt, id };
  } catch {
    return null;
  }
}

export function encodeCursor(row: { createdAt: Date | string; id: string }): string {
  const iso = row.createdAt instanceof Date ? row.createdAt.toISOString() : row.createdAt;
  return Buffer.from(`${iso}:${row.id}`, "utf8").toString("base64");
}

export function clampLimit(input: number | undefined): number {
  if (!input || input <= 0) return DEFAULT_LIMIT;
  return Math.min(input, MAX_LIMIT);
}

/**
 * Build a Prisma `where` fragment that applies cursor filtering on top of
 * any pre-existing filters. Used with `orderBy: [{ createdAt: "desc" }, { id: "desc" }]`.
 *
 * The fragment selects rows strictly after the cursor row in the (createdAt, id)
 * ordering — i.e. rows with createdAt < cursor.createdAt, OR equal createdAt
 * AND smaller id. Pass null/undefined to skip filtering.
 */
export function cursorWhere(
  cursor: { createdAt: Date; id: string } | null
): Record<string, unknown> | undefined {
  if (!cursor) return undefined;
  return {
    OR: [
      { createdAt: { lt: cursor.createdAt } },
      { createdAt: cursor.createdAt, id: { lt: cursor.id } },
    ],
  };
}

export function pageResult<T extends { id: string; createdAt: Date | string }>(
  rows: T[],
  limit: number
): CursorPaged<T> {
  if (rows.length <= limit) return { rows, nextCursor: null };
  const trimmed = rows.slice(0, limit);
  const last = trimmed[trimmed.length - 1];
  return { rows: trimmed, nextCursor: encodeCursor(last) };
}

```