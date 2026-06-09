---
type: blueprint
tags: [blueprint, architecture, patterns]
---

# Architecture Patterns — The 14 + when to use each

> The patterns that define Twenty-grade quality, each with a "use when" so a fresh chat applies them correctly (not cargo-cult). Implementations in [[Code Recipes]]. See [[_SaaS Blueprint]].

## Backend / data
1. **Tenant isolation on every path** — *always.* Row-level `orgId` (recipe 1) or schema-per-tenant for hard isolation/compliance. Never an unscoped query.
2. **Event-driven backbone** — *whenever a write has side-effects* (audit, webhooks, analytics, automation). Emit one event, fan out async (recipe 3). The single highest-leverage pattern.
3. **Shared query runner / service layer** — *when the same read/write logic is reached from >1 surface* (UI + API + webhook). One implementation, many entry points. Avoids drift.
4. **Cursor pagination + typed filters** — *for every list endpoint.* Relay connection shape (recipe 6). Future-proofs infinite scroll + consistent filtering.
5. **Soft delete (destroy/restore)** — *for user-facing records.* `deletedAt` + restore path, not hard delete.
6. **Custom migration discipline** — *for schema/data changes.* Reversible (up/down), fast (schema) vs slow (backfill); never rewrite committed migrations.
7. **Metadata-driven objects** — *only when users define their own objects/fields* (custom CRM, no-code tables). Otherwise skip — it's complexity you don't need (recipe 4).
8. **Jobs in a separate worker process** — *for anything slow/async* (email, sync, webhooks, AI). Priorities + retries + backoff (recipe 8).

## Frontend
9. **Module folder convention** — *every feature.* Identical shape → instant navigation ([[Folder Structure]]).
10. **Polymorphic renderer + type guards** — *when one concept has many variants* (field types, block types). One switch, everywhere updates (recipe 5).
11. **Instance-scoped state** — *when a complex widget can appear >1× on a page* (two tables/boards). Scope state by instance id so they don't collide.
12. **Server Components by default** — *always start server*; `'use client'` only for interactivity. Mutations = Server Actions/route handlers with Zod (recipe 7).

## Quality / discipline
13. **Tokens + lint enforcement** — *from day one.* Tokens in config, ESLint bans raw colors ([[Design Tokens]]). Discipline you don't enforce decays.
14. **Pick the design register first** — *before styling any surface.* Product vs editorial ([[DESIGN Templates]]).

## Anti-patterns (the "issues & unacceptable code" to avoid)
- Hardcoded colors/spacing; inconsistent type scale.
- Side-effects inline in mutations (webhook/audit calls scattered everywhere).
- Unscoped queries that can leak across tenants.
- `any`, default exports, class components, deep prop-drilling, god components >300 lines.
- `useEffect` for state that belongs in an event handler.
- Business logic living only in route handlers/resolvers (untestable, un-reusable).
- Blank empty states, layout shift on load, color-only state signals.
- One-off bespoke UI instead of the shared themed primitives.

## Related
- [[_SaaS Blueprint]] · [[Code Recipes]] · [[Design Tokens]] · [[Twenty CRM Overview]]
