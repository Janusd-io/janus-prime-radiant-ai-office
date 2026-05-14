---
type: source
source_type: laptop
title: auth-scope
slug: auth-scope
created: 2026-05-01
captured_by: jehad-altoutou
audience: personal
sensitivity: dept
sensitivity_confidence: 0.5
original_path: /Users/jehad/assessify/src/lib/auth-scope.ts
original_size: 2576
original_ext: .ts
category: code
extracted_with: code-fenced
extracted_at: "2026-05-14T09:51:33Z"
project: assessify

---

# auth-scope

_Extracted from `[[assessify|assessify]]/src/lib/auth-scope.ts` on 2026-05-14._

```typescript
// Recruitment auth scoping helpers (Phase 1.A).
// AdminUser may carry an `office` (Dubai/Singapore) and `scopedDepartments`
// (JSON array of Department.id). null on either field = global access.

export type ScopedSession = {
  id: string;
  role: string;
  office: string | null;
  scopedDepartments: string | null;
};

/** Decode AdminUser.scopedDepartments JSON. Returns null when unrestricted. */
export function parseScopedDepartments(raw: string | null | undefined): string[] | null {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) return null;
    const ids = parsed.filter((x): x is string => typeof x === "string" && x.length > 0);
    return ids.length > 0 ? ids : null;
  } catch {
    return null;
  }
}

/**
 * Restrict a Prisma `where` clause by the session's office. The target model
 * must have an `office` field. Rows with `office=null` (global) are always
 * visible — only office-tagged rows are filtered.
 *
 * No-op when the session is global (office is null).
 */
export function applyOfficeScope<T extends Record<string, unknown>>(
  session: Pick<ScopedSession, "office">,
  where: T,
): T {
  if (!session.office) return where;
  return {
    ...where,
    OR: [{ office: session.office }, { office: null }],
  } as T;
}

/**
 * Restrict a Prisma `where` clause by the session's scoped department list.
 * `field` defaults to `"departmentId"` but recruitment uses
 * `"jobRole"`-relation pathing instead — pass a custom path or precompose.
 *
 * No-op when the session is unrestricted (scopedDepartments is null/empty).
 */
export function applyDepartmentScope<T extends Record<string, unknown>>(
  session: Pick<ScopedSession, "scopedDepartments">,
  where: T,
  field: string = "departmentId",
): T {
  const scoped = parseScopedDepartments(session.scopedDepartments);
  if (!scoped) return where;
  return {
    ...where,
    [field]: { in: scoped },
  } as T;
}

/**
 * Compose office + department scope. For recruitment lists where the model
 * has an `office` column AND a `jobRole.departmentId` relation. Returns the
 * Prisma `where` shape directly.
 */
export function applyRecruitmentScope<T extends Record<string, unknown>>(
  session: ScopedSession,
  where: T,
): T {
  const scoped = parseScopedDepartments(session.scopedDepartments);
  const next: Record<string, unknown> = { ...where };

  if (session.office) {
    next.OR = [{ office: session.office }, { office: null }];
  }
  if (scoped) {
    next.jobRole = { departmentId: { in: scoped } };
  }
  return next as T;
}

```