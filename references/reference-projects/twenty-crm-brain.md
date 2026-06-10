---
type: reference
title: Twenty CRM — Working Brain (reusable patterns)
slug: twenty-crm-brain
created: 2026-06-10
updated: 2026-06-10
departments: [ai-office, engineering]
captured_by: jehad-altoutou
audience: [department]
related: [twenty-crm, twenty-crm-project-reference, saas-engineering-patterns, saas-blueprint-guide, ims-digital-twin]
source_repo: /Users/jehad/Desktop/Claude Projects/twenty/BRAIN.md
---

# Twenty CRM — Working Brain

> The concise, high-signal brain for the Twenty CRM study — read this first when building anything SaaS/CRM/admin, then pull detail from [[twenty-crm-project-reference]] and the [[saas-blueprint-guide|SaaS Blueprint]]. Mirror of `BRAIN.md` in the Twenty repo, kept here so any model/session can read it from Obsidian.


> Read this FIRST when working in this repo or reusing its patterns. Full detail in `PROJECT_REFERENCE.md`; human-readable note in `OBSIDIAN_EXPORT.md`. Every claim below is backed by paths in PROJECT_REFERENCE.md.

## What Twenty is
Open-source CRM. Nx monorepo + Yarn 4. The killer idea: **metadata-driven objects** — objects/fields are data rows (`objectMetadata`/`fieldMetadata`), and the **GraphQL API + Postgres tables are generated from that metadata**. Multi-tenant via **schema-per-workspace**.

## Core architecture decisions
- Monorepo: Nx 22.5, Yarn 4 workspaces, 21 packages. `twenty-front` (React/Vite), `twenty-server` (NestJS), `twenty-ui`/`twenty-ui-deprecated` (theme + components), `twenty-shared` (types).
- Backend: NestJS + GraphQL Yoga (code-first, dynamically generated from metadata) + TypeORM + custom **TwentyORM**. REST mirrors GraphQL via **shared common query runners** (no logic duplication).
- Multi-tenancy: each workspace = own Postgres schema. `core` schema holds users/workspaces/metadata.
- Jobs: BullMQ in a separate worker process. Analytics: ClickHouse.

## Frontend patterns to reuse
- **Module convention** (repeat everywhere): `components/ hooks/ states/ types/ utils/ contexts/ constants/ graphql/ __tests__/`.
- **Jotai factory layer** (`ui/utilities/state/jotai/`): `createAtomState`, `createAtomFamilyState`, `createAtomComponentFamilyState` (instance-scoped via Context instanceId), `createAtomComponentFamilySelector`. Single store, reset on logout.
- **Component-instance scoping**: React Context (instanceId) + Jotai component-family state → same complex widget (RecordTable/Board) renders many times without state collisions.
- **Polymorphic renderer + type guards**: `FieldInput` routes via `isFieldText`/`isFieldDate`/… to typed inputs.
- Apollo v4, custom link chain (Upload/Rest/Retry/Error/auth/streaming). Record hooks: `useFindManyRecords`, `useCreateOneRecord`, etc. Dynamic field selection from visible columns.
- Routing: React Router 6 data API, lazy + `<LazyRoute>`, two layout shells.
- Records: custom virtualized table; kanban via `@hello-pangea/dnd`; floating-ui for menus.

## ⭐ Event-driven backbone (the unifying pattern)
On record CRUD: `WorkspaceEventEmitter.emitDatabaseBatchEvent()` → `EntityEventsToDbListener` (`@OnDatabaseBatchEvent('*')`) → fan-out to queues: `entityEventsToDbQueue` (timeline activity + event-log→ClickHouse) · `webhookQueue` (match+dispatch, HMAC-signed) · workflow DATABASE_EVENT triggers. **One emit → listener → fan-out gives audit + analytics + webhooks + automation from a single source, all async.** Reuse this on any data-centric product.

## Other resolved internals (detail in PROJECT_REFERENCE §21)
- **isUnique**: not stored — derived from a single-field UNIQUE index at flat-cache build.
- **Materialization**: `*.workspace-entity.ts` → flat metadata → `synchronizeTwentyStandardApplication` → diff vs current → workspace-migration validate/build/run → schema-manager DDL. **Same diff-then-migrate engine serves standard objects, custom objects, AND views.**
- **MORPH_RELATION**: fields sharing a `morphId`, each its own target + one `xId` join column → polymorphic FK without unions.
- **Workflow**: Workflow→Version(trigger+steps)→Run; 4 triggers (DATABASE_EVENT/MANUAL/CRON/WEBHOOK), 14 action types; BullMQ executor re-enqueues every 20 steps; React Flow builder.
- **AI/MCP**: `@ai-sdk` provider abstraction (`provider:model` ids), tool-calling loop, auto-generated per-object CRUD tools (RBAC-filtered) exposed to both in-app agents and external MCP clients.
- **Views**: `ViewEntity` (core schema) + fields/filters/sorts/groups → `ViewQueryParamsService` translates to GraphQL filter/orderBy that drives table/board.
- **Integrations**: connected-account (encrypted tokens) → channel (syncStage/status) → list-fetch then import jobs + cron re-sync; webhooks HMAC-signed, 3 retries.

## Backend patterns to reuse
- Generate API from metadata (don't hand-write CRUD). Auto ops: create/find/update/delete/destroy/restore/findDuplicates/merge/groupBy.
- Relay connections: `{ edges{node,cursor}, pageInfo, totalCount }`, `first/after`. Typed filters (StringFilter eq/ilike/in/…), `orderBy:[{field:ASC}]`.
- Layered auth: JWT/OAuth/SAML → `WorkspaceAuthGuard` → permission flags + object + field + row-level perms. All workspace-scoped.
- Config: `twenty-config` service + validated `config-variables.ts`.
- Migrations: **custom command system**, NOT raw TypeORM. `@RegisteredInstanceCommand` (fast/slow) + `@RegisteredWorkspaceCommand` (per-workspace, dry-run). Both up+down; **never rewrite committed up/down**.

## Database/model patterns
- `ObjectMetadataEntity` + `FieldMetadataEntity` describe everything; `FieldMetadataType` enum (TEXT, RELATION, MORPH_RELATION, CURRENCY, FULL_NAME, LINKS, SELECT, TS_VECTOR…). Composite field types.
- Standard objects declared as `*.workspace-entity.ts` then materialized into metadata rows.
- Flat metadata caches for fast schema gen; `metadataVersion` busts cache. Full-text via `searchVector` (TS_VECTOR).

## UI/UX + styling rules (inherit Twenty's polish)
- **Linaria** (zero-runtime) styled components referencing **CSS variables** `--t-{cat}-{prop}-{variant}` from `twenty-ui/src/theme/constants/`.
- **Never hardcode colors** (lint-enforced `no-hardcoded-colors`). Use semantic tokens (primary/secondary/tertiary, danger/success/info).
- **4px spacing grid**: `spacing[n]` (1=4,2=8,4=16,6=24,8=32…). Radius xs2/sm4/md8/xl20/pill999. Font Inter; sizes md=16px etc; weights 400/500/600.
- Colors in **Display-P3** (Radix scales); accent = Indigo. Subtle shadows + glass blur. Transitions 75–300ms (`background 0.1s ease`).
- Icons: Tabler. Light/dark themes share token structure.
- State styling: focus→blue border, disabled→tertiary + pointer-events none, error→danger border/bg/text.

## ⭐ Two design registers (from root DESIGN.md + PRODUCT.md)
Twenty deliberately runs TWO visual systems — know which you're in:
- **Product app** (`twenty-front`): dense, functional, P3 token system, light/dark, Tabler icons (the §10 tokens).
- **Marketing site** (`twenty-website`): **editorial restraint** — serif/sans/mono trio (hierarchy from scale + family contrast, **never weight**; max weight 500, no bold), tinted-neutral palette + ≤10% accent, whitespace as a feature, asymmetric (not bento) layouts, **one opinionated detail per page**, motion = ease-out 250ms hover / quart entrance, no bounce/parallax/gradients/glassmorphism. Anti-references: generic SaaS hero/icon-grid/gradient-text, "Trusted by" logo strips, bento templates. Tonal anchors: Stripe docs (clarity) · Linear marketing (restraint) · print magazine (typography). Tokens in `twenty-website/src/theme/` (OKLCH neutrals, `theme.spacing(n)=n*4px`, `theme.radius(n)=n*2px`).
**Lesson for execution:** pick the register before styling. For credibility/marketing surfaces, restraint + typography beats components + color. For product surfaces, use the dense token system.

## Naming / folder conventions
- Named exports only; functional components only; no `any`; types over interfaces; string literals over enums (except GraphQL enums); no abbreviations.
- camelCase vars, SCREAMING_SNAKE_CASE consts, PascalCase types (Props suffix), kebab-case files (`.component.tsx`/`.service.ts`/`.entity.ts`).
- Aliases `@/*`→`src/modules/*`, `~/*`→`src/*`. Components <300 lines, services <500. Barrel `index.ts`.
- Comments `//` only, explain WHY. Event handlers over useEffect for state updates.

## Mistakes to avoid
Hardcoded colors/spacing · business logic only in resolvers · bypassing workspace scoping · rewriting migration up/down · default exports / class components / enums / `any` · useEffect for event-driven state · skipping instance-command generation after entity changes · global state where instance-scoped fits.

## Instructions for future Claude sessions
1. Read this + PROJECT_REFERENCE.md before acting. Build from documented patterns, not assumptions.
2. After entity changes: `database:migrate:generate --name <n> --type <fast|slow>`. After GraphQL schema changes: `graphql:generate`.
3. Always `lint:diff-with-main` + `typecheck` after edits. Prefer single-file jest runs.
4. For a NEW project: reuse module convention + token theme + Jotai factory + shared-query-runner + schema-per-tenant + layered RBAC + BullMQ worker. Reuse the exact design tokens (PROJECT_REFERENCE §10) to inherit the visual quality.
5. When you discover a new important pattern, update the relevant memory file immediately.
