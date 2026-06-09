---
title: Twenty CRM — Reference Architecture
source: https://github.com/twentyhq/twenty.git
tags: [twenty, crm, saas, architecture, frontend, backend, design-system, obsidian-brain]
type: reference-project
created: 2026-06-09
---

# Twenty CRM — Reference Architecture & Design System

> Permanent knowledge note. Twenty is an open-source CRM (Salesforce alternative). Studied as a blueprint for building high-quality SaaS / CRM / admin / dashboard products. All claims verified against source.

## High-level summary

Twenty is an **Nx monorepo** (Yarn 4, 21 packages) whose defining idea is a **metadata-driven, schema-per-tenant** architecture: CRM objects and fields are stored as metadata rows, and the **GraphQL API + PostgreSQL tables are generated dynamically** from that metadata. This is what makes the product fully customizable per workspace. Frontend is a React 18 + Vite SPA with Jotai state and Linaria styling; backend is NestJS + GraphQL Yoga + TypeORM (with a custom TwentyORM layer) + PostgreSQL/Redis/BullMQ/ClickHouse.

## Architecture map

```
twenty (Nx monorepo, Yarn 4)
├── twenty-front     React 18 · Vite · Jotai · Apollo v4 · Linaria · Lingui · React Router 6
├── twenty-server    NestJS · GraphQL Yoga (generated) · TypeORM + TwentyORM · BullMQ
├── twenty-ui        Theme tokens (src/theme/constants) + components
├── twenty-ui-deprecated  themeCssVariables, Tabler icons, theme CSS
├── twenty-shared    Types/utils (FieldMetadataType, isDefined…)
├── twenty-docker    compose, k8s, helm, spilo, otel, grafana
└── emails · website · docs · e2e · sdk · oxlint-rules · zapier …
```

- **Data flow**: metadata (objectMetadata/fieldMetadata) → flat caches → GraphQL SDL + resolvers → executable schema. REST mirrors GraphQL through shared **common query runners**.
- **Multi-tenancy**: one PostgreSQL schema per workspace; `core` schema holds users/workspaces/metadata.

## Frontend lessons

- **Module convention** repeated everywhere: `components/ hooks/ states/ types/ utils/ contexts/ constants/ graphql/ __tests__/`.
- **Jotai factory layer** with **component-instance scoping** (React Context instanceId + atom family) → the same complex widget (record table, kanban) appears many times without state collisions.
- **Polymorphic field renderer**: `FieldInput` uses type guards (`isFieldText`, `isFieldDate`…) to route to typed inputs.
- Apollo v4 with a custom link chain (Upload, Rest, Retry, Error, auth, streaming). Record hooks: `useFindManyRecords`, `useCreateOneRecord`, etc. Field selection built from visible columns.
- Routing: React Router 6 data API, lazy + `<LazyRoute>`, two layout shells (auth vs main-app-with-side-panel).
- Custom virtualized record table; kanban via `@hello-pangea/dnd`; floating-ui menus; forms via react-hook-form + Zod.
- Named exports only, functional components only, `@/`→modules, `~/`→src.

## Backend lessons

- **Generate CRUD from metadata** — don't hand-write resolvers. Auto ops include create/find/update/delete + soft destroy/restore + findDuplicates/merge/groupBy.
- **Relay connections** (`edges/node/cursor`, `pageInfo`, `totalCount`), typed filters (`StringFilter`: eq/ilike/in/…), `orderBy:[{field:ASC}]`.
- **Layered RBAC**: JWT/OAuth/SAML → `WorkspaceAuthGuard` → permission flags + object-level + field-level + row-level predicates. Everything workspace-scoped.
- **Custom migration commands** (not raw TypeORM): `@RegisteredInstanceCommand` (fast/slow) + `@RegisteredWorkspaceCommand` (per-workspace, dry-run). Both up+down; never rewrite committed logic.
- BullMQ jobs in a separate worker process; config via validated `config-variables.ts`.

## Database / data-model lessons

- `ObjectMetadataEntity` + `FieldMetadataEntity` describe everything; `FieldMetadataType` enum covers TEXT, NUMBER, RELATION, MORPH_RELATION, CURRENCY, FULL_NAME, LINKS, ADDRESS, PHONES, SELECT, RICH_TEXT, TS_VECTOR, etc.
- Standard objects declared as `*.workspace-entity.ts`, materialized into metadata rows.
- Flat metadata caches for fast schema generation; `metadataVersion` invalidates. Full-text search via `searchVector` (TS_VECTOR).

## UI/UX design lessons

- **Linaria** (zero-runtime CSS) styled components reading **CSS variables** `--t-{category}-{property}-{variant}` from `twenty-ui/src/theme/constants/`.
- **Never hardcode colors** — semantic tokens, lint-enforced. Light/dark share token structure.
- Colors in **Display-P3** (Radix scales); accent = Indigo. Subtle shadows + glass blur for depth; snappy 75–300ms transitions.
- Consistent state styling: focus→blue border, disabled→tertiary + pointer-events none, error→danger border/bg/text. Tabler icons.

## Styling & spacing lessons (exact tokens)

- **Spacing** (4px grid): 1=4, 2=8, 3=12, 4=16, 5=20, 6=24, 8=32, 10=40, 12=48, 16=64px.
- **Radius**: xs 2, sm 4, md 8, xl 20, xxl 40, pill 999.
- **Typography**: Inter (code: DM Mono); sizes xs 13.6 / sm 14.7 / md 16 / lg 19.7 / xl 24.6px; weights 400/500/600; line-height md 1.1 / lg 1.5.
- **Shadows**: light `0 2px 4px rgba(0,0,0,.04)`; strong `2px 4px 16px rgba(0,0,0,.16)`; superHeavy for modals.
- **Blur**: `blur(6|12|20px) saturate(200%) contrast(50%) brightness(130%)`.
- **Animation**: instant 75ms, fast 150ms, normal 300ms, slow 1.5s.
- **Sizing**: modal sm300/md400/lg53%/xl1200×800; side panel 500px; icons 14/16/20/24, strokes 1.6/2/2.5.

## Reusable SaaS patterns

1. Metadata-driven objects → user-customizable products.
2. Schema-per-tenant isolation (or row-level `workspaceId` for lighter needs).
3. Token-based theme + no-raw-colors lint → consistent polish.
4. Component-instance-scoped state for reusable complex widgets.
5. Shared query runners behind GraphQL **and** REST.
6. Custom fast/slow + instance/workspace migration commands with dry-run.
7. Module folder convention + named exports + strict TS.
8. Custom lint rules enforcing architecture; Nx-affected CI + merge-queue E2E gate.

## Future project blueprint

Start any new SaaS/CRM/admin from: module convention + token theme (reuse exact values above) + Jotai factory + Apollo/record-hook pattern → schema-per-tenant Postgres + NestJS + generated-or-shared query runners + Relay pagination + layered RBAC + BullMQ worker. Storybook-first components, Playwright merge-queue gate, Oxlint custom rules.

## Claude instructions for future usage

- Before building in Twenty or a Twenty-inspired project, read `BRAIN.md` then `PROJECT_REFERENCE.md`; use this note as the human-readable design reference. Build from documented patterns, not assumptions.
- After entity changes generate an instance command; after schema changes run graphql codegen; always lint-diff + typecheck.
- Reuse the exact design tokens to inherit Twenty's visual quality.

## Related
[[CRM Architecture]] · [[Design Systems]] · [[Multi-tenant SaaS]] · [[NestJS Patterns]] · [[React State Management]]
