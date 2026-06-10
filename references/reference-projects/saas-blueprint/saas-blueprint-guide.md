---
type: blueprint
tags: [blueprint, saas, crm, architecture, build-kit, twenty]
created: 2026-06-09
---

# 🏗️ SaaS Blueprint — Build a High-End SaaS from Twenty's Patterns

> **READ THIS FIRST when starting any new SaaS / CRM / admin / dashboard project.** This is a self-contained build-kit distilled from a deep study of [[twenty-crm|Twenty CRM]]. It contains paste-ready assets, not just descriptions, so a fresh Claude session can reproduce Twenty-grade quality without access to the original repo.
>
> **Target stack:** the SaaS Default Stack (Next.js 15 / Prisma / Clerk / Tailwind+shadcn / Stripe / Resend) — Next.js 15 App Router + TypeScript · Prisma + Postgres (Neon) · Clerk (orgs = tenants) · Tailwind + shadcn/ui · Stripe · Resend · Upstash Redis · Vercel. The *patterns* below come from Twenty (NestJS/TypeORM/Jotai/Linaria); they are re-expressed for this stack.

## How to use this kit (order matters)

1. **Read this file** — the philosophy + the non-negotiables below.
2. **[[folder-structure]]** — scaffold the repo with this exact skeleton and naming.
3. **[[design-tokens]]** — paste the theme config FIRST, before building any UI. Never hardcode colors/spacing after this.
4. **[[architecture-patterns]]** — the 14 patterns that define quality + when to use each.
5. **[[code-recipes]]** — copy-paste implementations: multi-tenancy, RBAC, event backbone, metadata objects, record table, pagination, jobs.
6. **[[design-templates]]** — drop a `DESIGN.md` + `PRODUCT.md` into the new repo (pick product vs editorial register).
7. **[[twenty-crm-project-reference|Full Twenty Reference]]** — the deep 21-section reference for anything not covered here.

## The quality bar (what "high-end" means here)

Twenty feels polished because of **discipline applied consistently**, not clever tricks. Reproduce these or it won't feel high-end:

- **Design tokens everywhere, zero hardcoded values.** Enforced by lint. (See [[design-tokens]].)
- **One spacing grid (4px), one type scale, semantic color names.** Hierarchy from scale + family, not random sizes.
- **Consistent state styling** — every interactive element has defined hover/focus/active/disabled/loading/empty/error states.
- **Strict TypeScript** — no `any`, named exports only, functional components, types over interfaces.
- **Repeated module convention** — every feature folder looks the same.
- **Tenant isolation on every data path** — never a query that can leak across orgs.
- **Async side-effects via an event backbone** — audit/webhooks/analytics never inline in mutations.

## The 7 non-negotiables (copy into the new repo's CLAUDE.md)

1. **No hardcoded colors/spacing** — only tokens from `theme`/Tailwind config. Add an ESLint rule to enforce.
2. **Multi-tenancy is mandatory** — every Prisma model has `orgId`; every query is scoped; use a tenant-scoped client (see [[code-recipes]]).
3. **Named exports only, functional components only, no `any`, types over interfaces, string-literal unions over enums.**
4. **Module folder convention** — `components/ hooks/ lib/ schema/ actions/ __tests__/` per feature.
5. **Events, not inline side-effects** — emit a domain event on writes; fan out to webhooks/audit/analytics async.
6. **Server Components by default**, `'use client'` only where interactivity is needed; mutations via Server Actions or route handlers with Zod validation.
7. **Pick the design register first** (product vs editorial — [[design-templates]]) before styling anything.

## What makes a CRM/SaaS *customizable* (the Twenty superpower)

If the product needs user-defined objects/fields (custom CRM, no-code tables), use the **metadata-driven** pattern (recipe in [[code-recipes]]): store object/field definitions as data, generate the API/forms/tables from them. If the schema is fixed, skip it — but still use the shared-query, pagination, RBAC, and event patterns.

## Related
- [[architecture-patterns]] · [[design-tokens]] · [[folder-structure]] · [[code-recipes]] · [[design-templates]]
- [[twenty-crm]] · the SaaS Default Stack (Next.js 15 / Prisma / Clerk / Tailwind+shadcn / Stripe / Resend) · [[saas-blueprint|SaaS Blueprint concept]]
