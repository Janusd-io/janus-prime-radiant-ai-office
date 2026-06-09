---
type: blueprint
tags: [blueprint, architecture, folder-structure, conventions]
---

# Folder Structure — Scaffold Skeleton

> The repo skeleton + naming conventions to scaffold a new the SaaS Default Stack (Next.js 15 / Prisma / Clerk / Tailwind+shadcn / Stripe / Resend) project, mirroring Twenty's module discipline. See [[_SaaS Blueprint]].

## Top-level layout (Next.js 15 App Router monorepo-ready)

```
my-saas/
├── CLAUDE.md                  # paste the 7 non-negotiables from [[_SaaS Blueprint]]
├── DESIGN.md                  # from [[DESIGN Templates]]
├── PRODUCT.md                 # from [[DESIGN Templates]]
├── prisma/
│   ├── schema.prisma          # every model has orgId (multi-tenant)
│   └── seed.ts
├── src/
│   ├── app/                   # routes (Server Components by default)
│   │   ├── (marketing)/       # editorial register — landing, pricing
│   │   ├── (app)/             # product register — dashboard, app shell
│   │   │   ├── layout.tsx     # app shell: sidebar + topbar + command menu
│   │   │   └── [object]/      # generic record routes (list + detail)
│   │   ├── api/               # route handlers (webhooks, REST surface)
│   │   └── globals.css        # tokens from [[Design Tokens]]
│   ├── modules/               # FEATURE modules — the core convention
│   │   ├── auth/
│   │   ├── billing/
│   │   ├── records/           # generic record table/board/detail
│   │   ├── views/             # saved views (filters/sorts/visible fields)
│   │   ├── workflow/          # automation builder (if needed)
│   │   └── settings/
│   ├── components/ui/         # shadcn/ui primitives (themed via tokens)
│   ├── lib/                   # cross-cutting: db, auth, events, rbac, queue
│   │   ├── db.ts              # tenant-scoped Prisma client (see [[Code Recipes]])
│   │   ├── events.ts          # event backbone emitter
│   │   ├── rbac.ts            # permission helpers
│   │   └── queue.ts           # BullMQ / Upstash QStash jobs
│   ├── server/                # server-only: services, query runners
│   └── generated/             # codegen output (graphql/types) — gitignored
└── tests/                     # e2e (Playwright)
```

## The module convention (repeat for EVERY feature)

```
modules/<feature>/
├── components/        # React components (.tsx, PascalCase, named export)
├── hooks/             # use*.ts hooks
├── lib/               # feature utilities, pure functions
├── schema/            # Zod schemas + types (input validation)
├── actions/           # Server Actions / mutations
├── states/            # client state (Zustand/Jotai atoms) — only if needed
├── constants/         # SCREAMING_SNAKE_CASE consts
└── __tests__/         # co-located tests
```

Every feature looks identical → a fresh contributor (or Claude) navigates instantly. This consistency is *itself* a quality signal.

## Naming conventions (from Twenty)
- **Files/dirs**: kebab-case with descriptive suffixes — `record-table.tsx`, `billing.service.ts`, `user.schema.ts`.
- **Components**: PascalCase, file name = component name, **named export** (`export const RecordTable = …`). No default exports.
- **Vars/functions**: camelCase, no abbreviations (`fieldMetadata` not `fm`, `user` not `u`).
- **Constants**: SCREAMING_SNAKE_CASE. **Types/Classes**: PascalCase, props suffixed `Props`.
- **Generics**: descriptive (`TData` not `T`).
- **Imports order**: external libs → internal (`@/`) → relative. Barrel `index.ts` for clean public surfaces.

## Size discipline
Components < 300 lines, services/modules < 500 lines. If bigger, split. Comments `//` only, explain WHY not WHAT.

## State management decision
- **Server state** → React Query / Apollo cache (don't duplicate into client state).
- **URL state** (filters, selected record) → searchParams.
- **Ephemeral UI** → `useState`.
- **Cross-tree shared UI state** → Zustand/Jotai. For repeated complex widgets, scope state by an instance id (Twenty's component-family pattern) so two tables don't collide — see [[Code Recipes]].

## Related
- [[_SaaS Blueprint]] · [[Code Recipes]] · [[Twenty CRM Overview]]
