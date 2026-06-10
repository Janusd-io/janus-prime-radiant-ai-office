---
type: reference
tags: [reference, saas, crm, architecture, patterns, design-system]
created: 2026-06-09
---

# SaaS Engineering Patterns

> Stack-agnostic, reusable patterns for building high-quality SaaS / CRM / admin products. Distilled from the deep study of [[twenty-crm|Twenty CRM]]. Apply on ANY stack (Next.js/Prisma/Tailwind as in [[saas-default-stack]], or NestJS/TypeORM as in Twenty).

## Architecture
1. **Metadata-driven objects** — describe entities/fields as data; generate API + tables from metadata → user-customizable products.
2. **Multi-tenancy** — schema-per-tenant (hard isolation) or row-level `workspaceId` scoping. Every data path tenant-scoped.
3. **Shared query runners behind GraphQL AND REST** — one logic path, two surfaces.
4. **Relay pagination** (`edges/node/cursor`, `pageInfo`, `totalCount`) + typed filters + `orderBy`.
5. **Layered RBAC** — auth → workspace guard → permission flags + object + field + row-level predicates.
6. **Custom migration commands** — fast (schema) vs slow (backfill), instance vs per-tenant, dry-run, immutable up/down.
7. **Jobs in a separate worker process** (BullMQ-style) with priorities/retries/backoff.

## Frontend
8. **Module folder convention**: components/hooks/states/types/utils/graphql/__tests__ everywhere.
9. **Component-instance-scoped state** (Context instanceId + scoped state factory) so complex widgets repeat safely.
10. **Polymorphic renderer + type guards** for "one component, many field variants".

## UI/UX & styling (see [[twenty-crm]] for exact token values)
11. **Token theme + lint ban on raw colors** — semantic CSS-variable tokens, 4px spacing grid, light/dark share structure.
12. Display-P3 colors, subtle shadows + glass blur, 75–300ms transitions, consistent focus/disabled/error state styling.


## Event-driven backbone (high-leverage)
Emit one normalized entity-change event from the write path → a single listener fans out to async consumers (audit/timeline, usage analytics → OLAP store, outbound webhooks, automation triggers). Don't scatter side-effects inline across every mutation. (Twenty: `WorkspaceEventEmitter` → `@OnDatabaseBatchEvent('*')` → BullMQ queues.)

## Two design registers — pick deliberately
- **Product register**: dense functional UI on a token system (4px grid, semantic CSS vars, light/dark). See [[twenty-crm]] for exact tokens.
- **Editorial register** (marketing/credibility): restraint. Typography carries hierarchy via **scale + family contrast, not weight** (serif/sans/mono, max weight 500). Tinted neutrals + one accent <=10%, no gradients/glassmorphism. Whitespace as a feature, asymmetric layouts, **one opinionated detail per page**, gentle ease-out motion. Reject generic-SaaS anti-patterns (big-number heroes, icon-grid bento, gradient text, "Trusted by" strips). Anchors: Stripe docs - Linear marketing - print magazine.

## Discipline
13. Named exports only, functional components, no `any`, types over interfaces, string literals over enums (except GraphQL), event handlers over useEffect, no abbreviations.
14. **Custom lint rules enforcing architecture** (module boundaries, guarded endpoints, no hardcoded colors).

## Related
- [[twenty-crm]] — the source study
- [[saas-default-stack]] · [[references]] · [[references|Home]]
