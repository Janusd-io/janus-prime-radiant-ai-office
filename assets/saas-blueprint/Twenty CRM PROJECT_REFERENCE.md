# PROJECT_REFERENCE.md — Twenty CRM Deep Architecture & Design Reference

> Main knowledge base for the Twenty CRM codebase. Built from direct source inspection (paths cited).
> Read this + `BRAIN.md` before working in this repo or reusing its patterns. `OBSIDIAN_EXPORT.md` is the human-readable companion.
> Source repo: https://github.com/twentyhq/twenty.git · License: AGPL-3.0 · Version at study: 0.2.1

---

## 1. Project Overview

Twenty is an open-source CRM (a modern Salesforce alternative) built as an **Nx monorepo** with **Yarn 4** workspaces. Its defining architectural idea is a **metadata-driven, schema-per-workspace** model: every CRM object (Company, Person, Opportunity…) and every custom field is described by metadata rows, and the GraphQL API + Postgres tables are **generated dynamically** from that metadata. This is what makes the CRM fully customizable per tenant.

- Frontend: React 18 SPA, Vite, Jotai, Linaria CSS-in-JS, Apollo Client v4, Lingui i18n.
- Backend: NestJS, GraphQL Yoga (code-first, dynamically generated), TypeORM + a custom "TwentyORM" layer, PostgreSQL (schema-per-workspace), Redis, BullMQ, ClickHouse (analytics).
- Tooling: Nx 22.5, Oxlint + Oxfmt (Rust, replacing ESLint/Prettier), Jest, Storybook 10, Playwright.

Evidence: `package.json`, `nx.json`, `tsconfig.base.json`, `packages/`.

---

## 2. Repository Structure

Top-level (`/`): `CLAUDE.md`, `DESIGN.md`, `PRODUCT.md`, `README.md`, `nx.json`, `package.json`, `tsconfig.base.json`, `jest.preset.js`, `yarn.config.cjs`, `packages/`.

`packages/` (21 packages):

| Package | Responsibility |
|---|---|
| `twenty-front` | React SPA (Vite + Apollo + Jotai + Linaria) |
| `twenty-server` | NestJS backend, GraphQL + REST, TypeORM, BullMQ |
| `twenty-shared` | Shared types/utils (e.g. `FieldMetadataType`, `isDefined`); dual CJS/MJS/ESM build |
| `twenty-ui` | Component library + **the theme system** (`src/theme/constants/`) |
| `twenty-ui-deprecated` | Legacy UI: still hosts `themeCssVariables`, icon set (Tabler), theme CSS output |
| `twenty-emails` | React Email templates |
| `twenty-docker` | Compose files (dev/prod), k8s, Helm, Spilo Postgres, otel-collector, grafana |
| `twenty-e2e-testing` | Playwright E2E |
| `twenty-website` | Marketing site (Next.js) |
| `twenty-docs` | Docusaurus docs |
| `twenty-sdk` / `twenty-client-sdk` | SDKs (twenty-sdk has 7 vite configs for sub-entries) |
| `twenty-oxlint-rules` | Custom Oxlint rules enforcing architecture |
| `twenty-zapier`, `twenty-codex-plugin`, `twenty-companion`, `twenty-apps`, `create-twenty-app`, `twenty-utils`, `twenty-cli` (deprecated), `twenty-front-component-renderer`, `twenty-claude-skills` | Integrations & tooling |

---

## 3. Full Tech Stack

- **Language**: TypeScript 5.9.3 (pinned via resolutions), target ES2018 base, decorators on. Node ^24.5.0.
- **Package manager / monorepo**: Yarn 4.13.0 (`packageManager` field) + Nx 22.5.4. `.yarnrc.yml`: `enableConstraintsChecks`, `enableHardenedMode`, `enableScripts: false`, `nodeLinker: node-modules`.
- **Frontend**: React 18, Vite 7 (`@vitejs/plugin-react-swc`), Jotai 2.17+, Apollo Client 4, Linaria (`@linaria/react`), Lingui 5 (macro-based), React Router 6 (data API), `@hello-pangea/dnd`, `@floating-ui/react`, react-hook-form + Zod, Mantine 8 primitives.
- **Backend**: NestJS, GraphQL Yoga (`@graphql-yoga/nestjs`), TypeORM (pg driver) + custom TwentyORM, PostgreSQL, Redis, BullMQ, ClickHouse, Passport (JWT/Google/Microsoft/SAML), AI SDKs (`@ai-sdk/anthropic|openai|google|mistral|amazon-bedrock|azure|xai`).
- **Tooling**: Oxlint (type-aware) + Oxfmt (single quotes, trailing commas, LF, 80-col); Jest (`@swc/jest` + Lingui plugin); Storybook 10.3.3 + Vitest CT; Playwright; Sentry; OpenTelemetry.

Evidence: root `package.json`, `packages/twenty-front/vite.config.ts`, `.oxfmtrc.jsonc`, `packages/twenty-server` deps.

---

## 4. Frontend Architecture (`packages/twenty-front/src`)

### Folder layout
`src/modules/*` (feature modules — primary structure), `src/pages/*` (lazy route components), `src/hooks`, `src/utils`, `src/types`, `src/generated*` (GraphQL codegen), `src/locales`, `src/testing`.

**Module pattern** — every feature module repeats this internal shape:
```
module-name/
  components/  hooks/  states/  types/  utils/  contexts/  constants/  graphql/  __tests__/
```
Key modules: `object-record/*` (the CRM engine — `record-table/`, `record-board/` (kanban), `record-calendar/`, `record-field/`, `record-filter/`, `record-sort/`, `graphql/`, `hooks/`), `ui/*` (layout, theme, state utilities, feedback), `auth/*`, `settings/*`, `navigation/*`, `apollo/*`, `app/*`.

### Routing
`src/modules/app/hooks/useCreateAppRouter.tsx` — React Router 6 data API (`createBrowserRouter` + `createRoutesFromElements`). Heavy lazy-loading via `lazy()` + a `<LazyRoute>` wrapper. Two layout shells: `DefaultLayout` (auth/onboarding) and `MainAppLayoutWithSidePanel` (main app with side panel + command menu). Core routes: `/objects/:objectNameSingular` (RecordIndexPage), `/objects/:objectNameSingular/:recordId` (RecordShowPage), `/settings/*`. Path constants come from `twenty-shared` `AppPath`.

### State — Jotai (custom factory layer)
Core in `src/modules/ui/utilities/state/jotai/`. Single store (`jotaiStore.ts`, `createStore()`), reset on logout via `resetJotaiStore()`. Factories:
- `createAtomState()` — simple global atom (+ optional localStorage/session/cookie persistence). e.g. `auth/states/currentUserState.ts`.
- `createAtomFamilyState()` — keyed collections.
- `createAtomComponentFamilyState()` — atoms scoped to a component-tree instance via a React Context instanceId (key = `${instanceId}__${familyKey}`). This is how multiple RecordTables/Boards coexist.
- `createAtomComponentFamilySelector()` — memoized derived state, optional `areEqual`.
Hooks: `useAtomStateValue`, `useAtomState`, `useSetAtomState`, `useAtomComponentStateValue`, `useAtomComponentFamilySelectorValue`.
Naming: `xState`, `xAtom`, `xFamilyState`, `xComponentFamilyState`, `xSelector`.

### Data fetching — Apollo
`src/modules/apollo/services/apollo.factory.ts` — factory builds clients; link chain: `UploadHttpLink`, `RestLink`, `RetryLink`, `ErrorLink`, `setContext` (auth token), streaming SSE link, logger link. Multiple clients (graphql + metadata + admin). Record hooks in `object-record/hooks/`: `useFindManyRecords`, `useCreateOneRecord`, `useUpdateOneRecord`, `useDeleteOneRecord`. Field selection built dynamically in `object-record/graphql/record-gql-fields/` based on visible columns. Generated types in `src/generated/`, `src/generated-metadata/`, `src/generated-admin/`.

### Records UI
- **Table** (`object-record/record-table/`): custom virtualization (not react-window). Header / Body / Row / Cell; inline editing, drag-reorder columns, resize, multi-select; component-scoped Jotai state.
- **Board/Kanban** (`object-record/record-board/`): `@hello-pangea/dnd`; Columns → Column → Card; drag between columns, in-column create.
- **Calendar** (`object-record/record-calendar/`).
- **Field rendering**: polymorphic — `record-field/ui/components/FieldInput.tsx` routes via type guards (`isFieldText`, `isFieldDate`, `isFieldRelationManyToOne`) to typed inputs.

### i18n & theming
Lingui (`@lingui/core/macro`, `t\`...\``), locale detection URL→localStorage→navigator→`en` (`src/utils/i18n/`). `useColorScheme()` (`ui/theme/hooks/`) → `'System'|'Dark'|'Light'`, persisted to workspace member settings.

### Conventions
Named exports only; functional components only; `.tsx`/`.ts`; aliases `@/*` → `src/modules/*`, `~/*` → `src/*`. Styling via Linaria `styled.div\`\`` referencing `themeCssVariables`.

---

## 5. Backend Architecture (`packages/twenty-server/src`)

### Layout
- `engine/` — platform core: `api/` (graphql, rest, mcp), `core-modules/` (auth, workspace, user, message-queue, twenty-config, billing…), `metadata-modules/` (object/field metadata + flat caches), `twenty-orm/` (custom ORM), `workspace-datasource/`, `workspace-manager/`, `guards/`, `dataloaders/`, `subscriptions/`, `workspace-cache/`.
- `modules/` — business/CRM domain (company, person, opportunity, workflow, contact-creation-manager…), each with `standard-objects/*.workspace-entity.ts`.
- `database/` — `typeorm/core`, `clickHouse`, `commands/` (migrations).
- `queue-worker/` — separate worker process. `filters/` — global exception filters.

### API — GraphQL code-first, generated from metadata
`engine/api/graphql/workspace-schema.factory.ts` builds the executable schema. Flow: load cached flat metadata (`WorkspaceManyOrAllFlatEntityMapsCacheService`) → generate SDL (`workspace-graphql-schema-sdl/`) → generate resolvers (`WorkspaceResolverFactory`, `workspace-resolver-builder/factories/`) → `makeExecutableSchema`. Endpoints: `/graphql` (workspace data), `/metadata` (CRUD on object/field metadata), `/admin`. Plugins: query-complexity validation, Sentry, error handler. REST mirror at `/rest/*` (`engine/api/rest/core/controllers/rest-api-core.controller.ts`) delegating to the **same common query runners** (`engine/api/common/common-query-runners/`).

Auto-generated resolver ops per object: `createOne/Many`, `findOne/Many`, `updateOne/Many`, `deleteOne/Many`, `destroyOne/Many` (soft), `restoreOne/Many`, `findDuplicates`, `merge`, `groupBy`.

### ORM & multi-tenancy
TypeORM for core/metadata entities; custom **TwentyORM** (`engine/twenty-orm/`) builds dynamic entity classes from metadata at runtime. `BaseWorkspaceEntity` (id, createdAt, updatedAt, deletedAt). **Schema-per-workspace**: each workspace = its own Postgres schema (`WorkspaceDataSourceService.createWorkspaceDBSchema`, name via `get-workspace-schema-name.util`). Core schema (`schema: 'core'`) holds users, workspaces, and all metadata. Request context injects workspace via `GraphQLHydrateRequestFromTokenMiddleware` + `WorkspaceAuthContextMiddleware`. DataLoaders prevent N+1.

### Auth
`engine/core-modules/auth/`. Passport strategies: JWT, Google OAuth, Microsoft OAuth, SAML SSO. Token services: Access / Refresh / Login (one-time) / Transient. `auth.resolver.ts` for signUp/signIn/passwordReset. Connected-account services sync Google/Microsoft mail+calendar.

### Permissions (RBAC, multi-level)
`engine/metadata-modules/permissions/` + `role/`. `RoleEntity`, `PermissionFlagEntity` (feature flags e.g. SETTINGS_READ/WRITE), `ObjectPermissionEntity` (object CRUD), `FieldPermissionEntity` (field read/write), `RowLevelPermissionPredicateEntity` (row-level). `PermissionsService.getUserWorkspacePermissions()` resolves from role + cached workspace perms. Guards (`engine/guards/`): `JwtAuthGuard`, `WorkspaceAuthGuard`, `CustomPermissionGuard`, `SettingsPermissionGuard`, `FeatureFlagGuard`, `ImpersonatePermissionGuard`. Controllers compose them: `@UseGuards(JwtAuthGuard, WorkspaceAuthGuard, CustomPermissionGuard)`.

### Jobs / queue
`engine/core-modules/message-queue/` — BullMQ driver (`drivers/bullmq.driver.ts`), sync driver fallback. `@Process()` handlers discovered by `MessageQueueExplorer`. Priorities, retries+backoff, retention, Sentry, metrics. Worker process: `queue-worker/queue-worker.ts`.

### Errors & config
Global `filters/unhandled-exception.filter.ts`; GraphQL error hook + `ExceptionHandlerService` + Sentry; REST `rest-api-exception.filter.ts`. Domain exceptions carry codes (e.g. `PermissionsException`). Config: `engine/core-modules/twenty-config/twenty-config.service.ts` + `config-variables.ts` (validated with class-validator at startup; type casts via custom decorators). `IS_CONFIG_VARIABLES_IN_DB_ENABLED` allows DB-stored config.

---

## 6. Database & Data Model

### Schemas
- **core** (`database/typeorm/core/core.datasource.ts`, `schema: 'core'`): users, workspaces, billing, and all `objectMetadata`/`fieldMetadata`. Entities glob `engine/core-modules/**/*.entity` + `engine/metadata-modules/**/*.entity`. Migrations table `_typeorm_migrations`; legacy TypeORM migrations frozen in `legacy-typeorm-migrations-do-not-add/`.
- **workspace schemas** (dynamic, one per workspace): actual CRM data tables. `WorkspaceEntity.databaseSchema`.

### Core entities (`engine/core-modules/`)
`User` (global, not workspace-scoped), `Workspace` (subdomain, databaseSchema, activationStatus, defaultRoleId, metadataVersion), `UserWorkspace` (junction: roles, permissionFlags, objectPermissions, locale, 2FA), `BillingSubscription`/`BillingCustomer` (Stripe), `ApiKey`, `AppToken`, `FeatureFlag`, `Application`. Most workspace-scoped entities extend `WorkspaceRelatedEntity` (adds `workspaceId`, `deletedAt`).

### Standard objects
Defined as TS classes in `modules/{name}/standard-objects/{name}.workspace-entity.ts` (e.g. `company`, `person`, `opportunity`, `note`, `task`). They declare fields with composite metadata types (FullName, Links, Currency, Address, Phones, Actor) and relations as `EntityRelation<T>`. Each declares `SEARCH_FIELDS_FOR_*` and a `searchVector` (TS_VECTOR) for full-text search. Materialized into `objectMetadata` rows by `TwentyStandardApplicationService.synchronizeTwentyStandardApplicationOrThrow()`.

### Metadata model (the customization engine)
`ObjectMetadataEntity` (`engine/metadata-modules/object-metadata/object-metadata.entity.ts`): nameSingular/Plural, labelSingular/Plural, icon, color, isCustom/isActive/isSystem/isAuditLogged/isSearchable, `labelIdentifierFieldMetadataId`, `standardOverrides` (JSONB), relations to fields/views/permissions. Unique on `(nameSingular, workspaceId)`.

`FieldMetadataEntity` (`field-metadata.entity.ts`): objectMetadataId, `type` (FieldMetadataType), name, label, defaultValue/options/settings (JSONB), isCustom/isActive/isSystem/isNullable/isUnique, relation fields (`relationTargetObjectMetadataId`, `relationTargetFieldMetadataId`, `morphId` for MORPH_RELATION). Unique on `(name, objectMetadataId, workspaceId)`.

**Field types** (`twenty-shared/src/types/FieldMetadataType.ts`): ACTOR, ADDRESS, ARRAY, BOOLEAN, CURRENCY, DATE, DATE_TIME, EMAILS, FILES, FULL_NAME, LINKS, MORPH_RELATION, MULTI_SELECT, NUMBER, NUMERIC, PHONES, POSITION, RATING, RAW_JSON, RELATION, RICH_TEXT, SELECT, TEXT, TS_VECTOR, UUID.

**Flat caches**: `flatObjectMetadataMaps`, `flatFieldMetadataMaps`, `flatIndexMaps`, `flatApplicationMaps` — denormalized metadata for fast schema gen, invalidated by `metadataVersion` bumps.

### Migrations (custom command system, NOT raw TypeORM)
`database/commands/upgrade-version-command/{version}/`. Two kinds:
- `@RegisteredInstanceCommand('x.y.z', ts)` — core/instance schema changes; `fast` (~30s, schema only) vs `slow` (adds `runDataMigration` backfill).
- `@RegisteredWorkspaceCommand('x.y.z', ts)` — per-workspace, iterated via `WorkspaceIteratorService`; support dry-run.
Both `up` and `down` required; **never rewrite committed up/down**. Seed data: `engine/workspace-manager/dev-seeder/`.

### API conventions
Relay-style connections: `{ edges: [{ node, cursor }], pageInfo: { startCursor, endCursor, hasNextPage, hasPreviousPage }, totalCount }`. Args `first/after`, `last/before`. Filters per type (`StringFilter`: eq/neq/gt/gte/lt/lte/in/like/ilike/startsWith/endsWith/regex/iregex/is; plus Number/Date/Uuid/Boolean). `orderBy: [{ field: ASC|DESC }]`. Input types auto-generated per object (create = required-by-nullable, update = all optional, relation connect = `{ id }`).

---

## 7. Authentication & Permissions
See §5. Layered: JWT/OAuth/SAML auth → workspace membership guard → permission flags + object-level + field-level + row-level predicates, all workspace-scoped. Impersonation supported with its own guard. Permissions cached per workspace.

## 8. API Design
Dual surface (GraphQL + REST) sharing common query runners. Schema generated from metadata, not hand-written. Query complexity limits guard against DoS. Soft-delete first-class (destroy/restore). MCP layer (`engine/api/mcp/`) exposes API to AI agents.

## 9. State Management
Jotai with a bespoke factory + component-instance-scoping layer (see §4). Apollo cache for server state. Component-local React state for ephemeral UI. Functional updates (`set(prev => …)`).

---

## 10. UI/UX Design System (token values quoted from source)

Theme lives in `packages/twenty-ui/src/theme/constants/` (`ThemeLight.ts`, `ThemeDark.ts`, `THEME_COMMON`), surfaced as CSS variables (`--t-{category}-{property}-{variant}`) via `twenty-ui-deprecated/src/theme-constants/themeCssVariables.ts` and `theme-light.css`/`theme-dark.css`. Styling = Linaria referencing those variables. Colors use **Display-P3** (Radix UI color scales).

- **Font**: `Inter, sans-serif`; code `DM Mono`. Weights 400/500/600. Line heights md 1.1 / lg 1.5.
- **Font sizes**: xxs 10px, xs 13.6px, sm 14.7px, md 16px, lg 19.7px, xl 24.6px, xxl 29.6px.
- **Spacing** (4px base): 1=4, 2=8, 3=12, 4=16, 5=20, 6=24, 8=32, 10=40, 12=48, 16=64, 24=96, 32=128 (+ 0.5=2, 1.5=6).
- **Radius**: xs 2, sm 4, md 8, xl 20, xxl 40, pill 999, rounded 100%.
- **Gray scale (light)**: gray1 #fff → gray12 #333 (12 steps; backgrounds use gray1–5, text uses gray8–12).
- **Font colors (light)**: primary gray12, secondary gray11, tertiary gray9, light gray8, extraLight gray7, inverted gray1, danger red.
- **Backgrounds (light)**: primary white, secondary #FCFCFC, tertiary #F1F1F1, quaternary #EBEBEB; transparent overlays in rgba black.
- **Borders (light)**: strong gray6, medium gray5, light gray4; danger #FCCFCE; blue #AEBAF4.
- **Box shadows**: light `0 2px 4px rgba(0,0,0,.04), 0 0 4px rgba(0,0,0,.08)`; strong `2px 4px 16px rgba(0,0,0,.16)…`; superHeavy for modals.
- **Blur** (glass): light/medium/strong = `blur(6|12|20px) saturate(200%) contrast(50%) brightness(130%)`.
- **Animation durations**: instant 75ms, fast 150ms, normal 300ms, slow 1.5s. Default transition `background 0.1s ease`.
- **Icons**: Tabler (`@tabler/icons-react`); sizes sm14/md16/lg20/xl24; strokes 1.6/2/2.5.
- **Modal sizes**: sm 300px, md 400px, lg 53%, xl 1200×800, fullscreen 100dvw×100dvh. Side panel 500px.
- **Accent**: Radix Indigo scale (primary indigo5, hover accent3570 = indigo8).
- **Snack bar**: success green / error red / warning orange / info blue / default gray, each with tinted bg.
- **Tags**: 24+ color pairs (`--t-tag-text-*` / `--t-tag-background-*`).

Two full themes (light/dark) share token structure; dark inverts gray scale.

### Design principles inferred
4px spacing grid everywhere; P3 colors for vivid yet controlled palette; semantic naming (danger/success/info, primary/secondary/tertiary font & bg) instead of raw hex in components (enforced by a no-hardcoded-colors lint rule); subtle shadows + glass blur for depth; fast (75–300ms) transitions for snappy feel; consistent state styling (focus → blue border, disabled → tertiary color + pointer-events none, error → danger border/bg/text).

---

## 11. Styling, Colors, Padding, Typography, Layout Rules
- Never hardcode colors — use `themeCssVariables` / theme tokens (lint-enforced via `twenty-oxlint-rules/no-hardcoded-colors`).
- All spacing as `spacing[n]` multiples of 4px.
- Component styling = Linaria `styled.x` with props-driven variants; size variants commonly xs/sm/md/lg mapping to fixed heights (e.g. input 20/24/28/32px).
- Theme is light/dark via `ThemeProvider` `colorScheme`; consume via CSS variables so both themes work for free.

## 12. Reusable Component Patterns
- Polymorphic renderer + type guards (FieldInput) for "one component, many variants".
- React Context to pass instance-scoped data (`RecordTableContext`, `FieldContext`) + matching Jotai component-family state for instance-scoped state.
- Container/ContextProvider vs presentational split.
- Effect components (e.g. `RecordTableScrollToFocusedCellEffect`) isolate side effects into dedicated render-null components.
- Barrel `index.ts` exports; named exports only.

## 13. Forms, Tables, Views, Filters, Modals
- Forms: react-hook-form + Zod resolver, composed from field inputs (no monolithic form lib).
- Tables: custom virtualized record table with inline edit, sort/filter/reorder.
- Boards: kanban via `@hello-pangea/dnd`.
- Filters/sorts: typed GraphQL filter inputs surfaced through `record-filter`/`record-sort` UI; advanced-filter module for compound conditions.
- Modals/dropdowns: `@floating-ui/react` positioning; modal size tokens.

## 14. Error Handling & Loading States
- Frontend: Apollo `ErrorLink` + `RetryLink`; snack-bar manager for toasts; error boundaries; `<LazyRoute>` fallbacks for code-split loading.
- Backend: global exception filter, GraphQL error hook, REST exception filter, typed domain exceptions with codes, Sentry.

## 15. Testing & Quality Tools
Jest (`@swc/jest` + Lingui plugin) unit/integration; Storybook 10 + Vitest component tests (CI shards: modules/pages/performance × 4); Playwright E2E (merge-queue gate with Postgres 18 + Redis services). Oxlint type-aware + Oxfmt; custom architecture lint rules in `twenty-oxlint-rules` (enforce-module-boundaries, component-props-naming, rest-api-methods-should-be-guarded, inject-workspace-repository, no-hardcoded-colors, upgrade-command-filename, max-consts-per-file). Test pyramid 70/20/10; test behavior not implementation; query by visible text/role.

## 16. Deployment & DevOps
`packages/twenty-docker/`: `docker-compose.yml` (server, worker, db, redis, S3/local storage, encryption keys, OAuth, SMTP, AI keys), `docker-compose.dev.yml`, plus `k8s/`, `helm/`, `twenty-postgres-spilo/`, `otel-collector/`, `grafana/`, `podman/`. 37 GitHub workflows (`.github/workflows/`): `ci-front`, `ci-server`, `ci-ui`, `ci-shared`, `ci-merge-queue` (full E2E), `ci-breaking-changes`, `ci-test-docker-compose`, `cd-deploy-main`, `cd-deploy-tag`, i18n Crowdin sync, visual regression (Argos). Custom actions: `yarn-install`, `restore-cache`/`save-cache`, `nx-affected`. Env via `.env.example` per package; `reset:env` Nx target copies them.

## 17. Important Commands
```bash
yarn start                                  # front + server + worker
npx nx start twenty-front | twenty-server   # individual
npx nx run twenty-server:worker             # worker
# tests
npx jest path/to/test.test.ts --config=packages/PROJECT/jest.config.mjs
npx nx test twenty-front | twenty-server
npx nx run twenty-server:test:integration:with-db-reset
# quality
npx nx lint:diff-with-main twenty-front [--configuration=fix]
npx nx typecheck twenty-front | twenty-server
npx nx fmt twenty-front
# build (shared first)
npx nx build twenty-shared && npx nx build twenty-front && npx nx build twenty-server
# db
npx nx database:reset twenty-server
npx nx run twenty-server:database:migrate:generate --name <name> --type <fast|slow>
# graphql codegen
npx nx run twenty-front:graphql:generate [--configuration=metadata]
# dev env
bash packages/twenty-utils/setup-dev-env.sh [--docker|--down|--reset]
```

## 18. Patterns to Reuse in Future Projects
1. **Metadata-driven objects** — describe entities/fields as data; generate API + schema. Enables user-customizable products.
2. **Schema-per-tenant** multi-tenancy for hard data isolation.
3. **Token theme system** (P3 colors + 4px spacing + semantic CSS variables) + lint rule banning raw colors → consistent polish.
4. **Component-instance-scoped state** (Context instanceId + Jotai family) so the same complex widget can appear many times.
5. **Shared query runners** behind both GraphQL and REST → no logic duplication.
6. **Custom migration commands** (fast/slow, instance/workspace, dry-run, immutable up/down) instead of ad-hoc migrations.
7. **Polymorphic field renderer** via type guards.
8. **Module folder convention** (components/hooks/states/types/utils/graphql/__tests__) repeated everywhere.
9. **Oxlint custom rules** to enforce architecture, not just style.
10. **Nx affected + change-scoped CI** + merge-queue full E2E gate.

## 19. Mistakes to Avoid
- Don't hardcode colors/spacing — always tokens.
- Don't put business logic only in resolvers — share via query runners/services.
- Don't bypass workspace scoping — every data path must be tenant-isolated.
- Don't rewrite committed migration up/down logic.
- Don't use default exports, class components, enums (except GraphQL), or `any`.
- Don't reach for `useEffect` for state updates that belong in event handlers.
- Don't skip generating instance commands after entity changes.
- Don't add global state when component-instance-scoped state fits.

## 20. Using Twenty as a Blueprint for New SaaS/CRM/Admin Projects
1. Start from the **module convention** + **token theme** + **Jotai factory layer**.
2. For customizable data: adopt metadata objects/fields → generated API. For fixed-schema products: keep TypeORM entities but still use the shared-query-runner + connection pagination patterns.
3. Multi-tenant → schema-per-workspace (or row-level `workspaceId` for lighter needs).
4. Layered auth+RBAC (JWT/OAuth/SAML → workspace guard → object/field/row permissions).
5. Dual GraphQL+REST over common runners; Relay connections; typed filters.
6. BullMQ for jobs in a separate worker process.
7. Storybook-first components; Playwright merge-queue gate; Oxlint custom rules.
8. Reuse the exact design tokens (§10) to inherit Twenty's visual polish.

---

## 21. Deep-Dive Findings (previously unclear — now resolved)

### 21.0 The event-driven backbone (the unifying pattern)
Almost every cross-cutting feature hangs off one pipeline. On record CRUD, `WorkspaceEventEmitter.emitDatabaseBatchEvent()` (`engine/workspace-event-emitter/`) fires; `EntityEventsToDbListener` catches **all** events via `@OnDatabaseBatchEvent('*', action)` (`engine/api/graphql/workspace-query-runner/listeners/entity-events-to-db.listener.ts`) and fans out to queues:
- `entityEventsToDbQueue` → `UpsertTimelineActivityFromInternalEvent` (timeline) **and** `CreateEventLogFromInternalEvent` (→ ClickHouse sink).
- `webhookQueue` → `CallWebhookJobsJob` (match webhooks → dispatch).
- Workflow `DATABASE_EVENT` triggers also subscribe here.
**Reusable lesson:** one emit → listener → fan-out-to-queues backbone gives you audit, analytics, webhooks, and automation triggers from a single source of truth, all async.

### 21.1 `isUnique` derivation (computed, not stored)
`FieldMetadata.isUnique` is **not** a DB column (dropped by migration `1798300000000-drop-field-metadata-is-unique-column.ts`). It is derived at flat-cache build by `compute-unique-field-metadata-ids-from-indexes.util.ts`: a field is unique iff a UNIQUE `IndexMetadataEntity` exists whose `indexFieldMetadatas` has exactly **one** entry with `subFieldName === null`. The DTO sets `isUnique: uniqueFieldMetadataIds.has(entity.id)` (`from-field-metadata-entity-to-field-metadata-dto.util.ts`).

### 21.2 Standard-object materialization flow
TS classes in `modules/{name}/standard-objects/*.workspace-entity.ts` extend `BaseWorkspaceEntity` (type-level). Field builders in `workspace-manager/twenty-standard-application/utils/field-metadata/*` produce `FlatFieldMetadata`. Then: `TwentyStandardApplicationService.synchronizeTwentyStandardApplicationOrThrow()` computes desired flat maps, compares to current (workspace cache) → `WorkspaceMigrationValidateBuildAndRunService.validateBuildAndRunWorkspaceMigrationFromTo()` (orchestrator diffs into CREATE/UPDATE/DELETE actions) → `WorkspaceMigrationRunnerService.runWorkspaceMigration()` dispatches per-action handlers → `WorkspaceSchemaManagerService` executes DDL via sub-managers (table/column/index/foreignKey/enum) on the workspace datasource. **Same diff-then-migrate engine is reused for user-created custom objects and for Views.**

### 21.3 MORPH_RELATION (polymorphism)
A group of relation fields sharing one `morphId` (e.g. attachment's `targetTask`/`targetNote`/`targetPerson`/…). Each field is `type=MORPH_RELATION`, has its own `relationTargetObjectMetadataId`, and creates **one** UUID join column (`targetTaskId`, …). DB check: MORPH_RELATION ⇒ `morphId IS NOT NULL`. Runtime groups by `morphId` to know which object types are targeted. Simulates a polymorphic FK without union types. Evidence: `compute-attachment-standard-flat-field-metadata.util.ts`, `field-metadata.entity.ts`.

### 21.4 Workflow / automation builder
Entities (`modules/workflow/common/standard-objects/`): `Workflow` (status DRAFT/ACTIVE/DEACTIVATED) → `WorkflowVersion` (one `trigger` + `steps[]`, status incl. ARCHIVED) → `WorkflowRun` (`state`, `status`, `stepLogs`, `stepInfos`). Triggers (`workflow-trigger/types/`): DATABASE_EVENT, MANUAL, CRON, WEBHOOK. Actions (14, `workflow-executor/workflow-actions/types/`): CODE, LOGIC_FUNCTION, SEND_EMAIL/DRAFT_EMAIL, CREATE/UPDATE/DELETE/UPSERT/FIND_RECORD(S), FORM, FILTER, IF_ELSE, HTTP_REQUEST, AI_AGENT, ITERATOR, DELAY, EMPTY. Execution: `RunWorkflowJob` (BullMQ `workflowQueue`) → `WorkflowExecutorWorkspaceService.executeFromSteps()`; steps parallelized, variable-interpolated input, action factory dispatch, re-enqueue after `MAX_EXECUTED_STEPS_COUNT` (20) to bound job length; IF_ELSE/ITERATOR route `nextStepIds`. Frontend: React Flow (`@xyflow/react`) in `modules/workflow/workflow-diagram/` with editable vs readonly canvases, Jotai component state for diagram/selected-node/insert-point.

### 21.5 AI modules & MCP
AI lives in `engine/metadata-modules/ai/`. `AgentEntity` (assigned a role for permissions). Providers abstracted via `@ai-sdk` — `AiModelRegistryService` builds `{provider}:{modelId}` ids, `SdkProviderFactoryService` instantiates clients per `npm` package; config schema supports apiKey/baseUrl/region/dataResidency/authType (incl. AWS_STS for Bedrock). `AgentAsyncExecutorService.executeAgent()` runs a **tool-calling loop** (`generateText`/`streamText`), tools from a registry incl. auto-generated **Database CRUD tools per object** (permission-filtered) + native tools (search). Used as: AI chat, the `AI_AGENT` workflow step, REST `POST /rest/ai/generate-text`. All LLM calls metered for billing.
**MCP** (`engine/api/mcp/`): JSON-RPC + SSE server exposing the same CRUD tools plus `list_object_metadata_names`, `list_skills`, `get_tool_catalog`, `load_skill`. Auth via API key (Bearer) or JWT, tool access role-filtered; `mcp-instruction-builder` auto-generates the system prompt with the workspace's object schema. Purpose: external AI agents operate on the CRM safely within RBAC.

### 21.6 ClickHouse analytics
`database/clickHouse` + `engine/core-modules/event-logs`. Four tables: `workspaceEvent`, `objectEvent` (record CRUD), `usageEvent` (metering/credits/billing), `applicationLog` (logic-function logs, 30-day TTL; others 3-year). Ingest: events → `entityEventsToDbQueue` → `CreateEventLogFromInternalEvent` → `WorkspaceEventSinkService` → `ClickHouseEventSink` → batched `ClickHouseService.insert()` (chunked, async_insert). Per-workspace clients.

### 21.7 Audit / timeline
`TimelineActivityWorkspaceEntity` (workspace object): `happensAt`, `name` (e.g. `note.created`), `properties` (before/after diff), `workspaceMemberId`, many `targetXId` relations. Built by `UpsertTimelineActivityFromInternalEvent` job off the same `entityEventsToDbQueue`; only objects in `SYSTEM_OBJECTS_WITH_TIMELINE_ACTIVITIES`; notes/tasks auto-link to their targets. `ObjectMetadata.isAuditLogged` gates it. Consumed in UI as ordinary GraphQL records.

### 21.8 Views (and dashboards)
`ViewEntity` (**core** schema, per workspace): `type` (TABLE/KANBAN/BOARD/CALENDAR/GALLERY), `visibility`, kanban/calendar/grouping config, relations `viewFields`/`viewFilters`/`viewFilterGroups`/`viewSorts`/`viewGroups`/`viewFieldGroups`. Hydrated to `FlatView` cache. `ViewQueryParamsService` translates a saved view → GraphQL `{ filter (AND/OR AST), orderBy, objectNameSingular }` (timezone-aware) which drives the record table/board fetch. Views are CRUD'd through the **same** workspace-migration validate/build/run pipeline as objects. `DashboardWorkspaceEntity` exists (timeline target) but no dashboard CRUD service was found — likely nascent.

### 21.9 Webhooks & integrations
`WebhookEntity` (core): `targetUrl`, `secret` (HMAC), `operations` patterns (`company.created`, `*.updated`, `*.*`). Dispatch: `webhookQueue` → `CallWebhookJobsJob` (pattern-match, chunk 20) → `CallWebhookJob` (HMAC-SHA256 signature headers `X-Twenty-Webhook-*`, 5s timeout, 3 retries; response logged to ClickHouse). **Messaging** (`modules/messaging`): `ConnectedAccountEntity` (encrypted tokens, google/microsoft), `MessageChannelEntity` (syncStage/syncStatus, folders) → `MessagingMessageListFetchJob` then `MessagingMessagesImportJob` on `messagingQueue`; OAuth refresh drivers. **Calendar** (`modules/calendar`): mirror pattern — `CalendarChannelEntity`, list-fetch → import jobs + an import **cron** for periodic re-sync; blocklist manager.

## Still genuinely unclear / shallow
- Analytics **dashboard read path** (no GraphQL resolver over ClickHouse found; likely separate/observability or nascent), `DashboardWorkspaceEntity` CRUD, webhook manual replay, exact frontend subscription path for live timeline updates.
- `AgentEntity.definition` schema contents; AI "field suggestions" mechanism; how `load_skill` skills tie into workflows.
- Frontend `advanced-filter`, `layout-customization`, `record-merge`, `spreadsheet-import` and Apollo cache-invalidation examined only superficially.
