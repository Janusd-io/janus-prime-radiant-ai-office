---
type: blueprint
tags: [blueprint, recipes, code, multi-tenant, rbac, events, prisma, nextjs]
---

# Code Recipes — Paste-Ready Implementations

> Twenty's core patterns re-expressed as working code for the the SaaS Default Stack (Next.js 15 / Prisma / Clerk / Tailwind+shadcn / Stripe / Resend) (Next.js 15 / Prisma / Clerk / Zod / BullMQ). Copy, rename, adapt. See [[saas-blueprint-guide]] · [[architecture-patterns]].

---

## 1. Multi-tenancy — tenant-scoped Prisma client

Twenty isolates tenants via schema-per-workspace. For most SaaS, **row-level `orgId` scoping** is simpler and enough. The rule: *never* expose the raw Prisma client to feature code — only a client already bound to the current org.

```ts
// prisma/schema.prisma — every tenant model carries orgId + index
model Company {
  id        String   @id @default(cuid())
  orgId     String                       // tenant key
  name      String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  deletedAt DateTime?                     // soft delete (Twenty: destroy/restore)
  @@index([orgId])
}
```

```ts
// src/lib/db.ts
import { PrismaClient } from '@prisma/client';
import { auth } from '@clerk/nextjs/server';

const base = new PrismaClient();

// Returns a client whose every query is forced to the caller's org.
// Uses Prisma $extends so feature code CANNOT forget the orgId filter.
export async function getDb() {
  const { orgId } = await auth();
  if (!orgId) throw new Error('No active organization');

  return base.$extends({
    query: {
      $allModels: {
        async $allOperations({ args, query, operation }) {
          if (['findMany', 'findFirst', 'count', 'updateMany', 'deleteMany'].includes(operation)) {
            args.where = { ...args.where, orgId };
          }
          if (operation === 'create') args.data = { ...args.data, orgId };
          return query(args);
        },
      },
    },
  });
}
```
> Clerk **Organizations** map cleanly to Twenty's workspaces. `orgId` from `auth()` is the tenant boundary; RBAC roles live on Clerk org memberships.

---

## 2. RBAC — layered permission guard

Twenty layers: auth → workspace membership → permission flags + object-level + field-level. Minimal reusable version:

```ts
// src/lib/rbac.ts
import { auth } from '@clerk/nextjs/server';

type Action = 'read' | 'create' | 'update' | 'delete';
type Role = 'admin' | 'member' | 'guest';

const MATRIX: Record<Role, Record<string, Action[]>> = {
  admin:  { '*': ['read', 'create', 'update', 'delete'] },
  member: { '*': ['read', 'create', 'update'] },
  guest:  { '*': ['read'] },
};

export async function can(action: Action, object = '*') {
  const { orgRole } = await auth();
  const role = (orgRole?.replace('org:', '') ?? 'guest') as Role;
  const allowed = MATRIX[role][object] ?? MATRIX[role]['*'] ?? [];
  return allowed.includes(action);
}

export async function assertCan(action: Action, object = '*') {
  if (!(await can(action, object))) throw new Error('Forbidden');
}
```
Call `await assertCan('update', 'company')` at the top of every mutating Server Action / route handler. For field-level control, filter the returned object by a per-role field allowlist before sending to the client.

---

## 3. Event backbone — the #1 pattern (audit + webhooks + analytics from one emit)

This is Twenty's highest-leverage idea: **emit one domain event on every write; fan out to async consumers.** Never call webhook/audit/analytics code inline in a mutation.

```ts
// src/lib/events.ts
import { queue } from './queue';

export type EntityEvent = {
  orgId: string;
  object: string;                       // 'company'
  operation: 'created' | 'updated' | 'deleted';
  recordId: string;
  before?: unknown;
  after?: unknown;
  actorId: string;
  at: string;                           // ISO
};

// Single choke point. Fan out to every consumer queue.
export async function emitEntityEvent(e: EntityEvent) {
  await Promise.all([
    queue('audit').add('timeline', e),       // -> audit/timeline log
    queue('analytics').add('event', e),      // -> ClickHouse/PostHog sink
    queue('webhooks').add('dispatch', e),    // -> match + POST webhooks (HMAC)
    queue('workflows').add('trigger', e),    // -> automation DATABASE_EVENT triggers
  ]);
}
```
```ts
// usage inside any mutation
const after = await db.company.update({ where: { id }, data });
await emitEntityEvent({ orgId, object: 'company', operation: 'updated',
  recordId: id, before, after, actorId, at: new Date().toISOString() });
```
Webhook dispatch should HMAC-sign (`X-Webhook-Signature: sha256(timestamp + body)`), 5s timeout, ~3 retries — exactly Twenty's `CallWebhookJob`.

---

## 4. Metadata-driven objects (only if the product needs user-defined objects/fields)

Twenty's superpower: objects/fields are DATA, and the API/UI are generated. Minimal version:

```ts
// prisma: definitions live in tables, not as static models
model ObjectDef { id String @id @default(cuid()) orgId String nameSingular String namePlural String icon String? isCustom Boolean @default(true) fields FieldDef[] }
model FieldDef  { id String @id @default(cuid()) orgId String objectId String type String /* TEXT|NUMBER|DATE|SELECT|RELATION|... */ name String label String options Json? isRequired Boolean @default(false) object ObjectDef @relation(fields:[objectId],references:[id]) }
// Actual record values stored generically (EAV) or in a JSONB column:
model RecordRow { id String @id @default(cuid()) orgId String objectId String data Json /* { fieldName: value } */ createdAt DateTime @default(now()) deletedAt DateTime? @@index([orgId, objectId]) }
```
- **Generate Zod schema** from `FieldDef[]` at runtime → validate `RecordRow.data`.
- **Generate the form + table columns** from `FieldDef[]` (map type → input component, the polymorphic-renderer pattern below).
- **Field types** to support (Twenty's set): TEXT, NUMBER, BOOLEAN, DATE, DATETIME, SELECT, MULTI_SELECT, RELATION, CURRENCY, EMAIL, PHONE, LINK, RATING, RICH_TEXT, JSON.
- Migrate cautiously: changing a `FieldDef` should be a guarded operation (Twenty's fast/slow migration commands).

---

## 5. Polymorphic field renderer (one component → every field type)

```tsx
// src/modules/records/components/FieldInput.tsx
import { TextField, NumberField, DateField, SelectField, RelationField } from './fields';

export const FieldInput = ({ field, value, onChange }: FieldInputProps) => {
  switch (field.type) {
    case 'TEXT':     return <TextField {...{ field, value, onChange }} />;
    case 'NUMBER':   return <NumberField {...{ field, value, onChange }} />;
    case 'DATE':     return <DateField {...{ field, value, onChange }} />;
    case 'SELECT':   return <SelectField {...{ field, value, onChange }} />;
    case 'RELATION': return <RelationField {...{ field, value, onChange }} />;
    default:         return <TextField {...{ field, value, onChange }} />;
  }
};
```
Same switch drives table cells and detail-view fields. Add a type → add one case, everywhere updates.

---

## 6. Cursor (Relay-style) pagination + typed filters

Twenty uses Relay connections everywhere. Reusable shape:

```ts
// src/server/list-records.ts
export type Connection<T> = {
  edges: { node: T; cursor: string }[];
  pageInfo: { hasNextPage: boolean; endCursor: string | null };
  totalCount: number;
};

export async function listRecords<T>({ db, model, where, orderBy, first = 25, after }: ListArgs): Promise<Connection<T>> {
  const rows = await db[model].findMany({
    where, orderBy,
    take: first + 1,
    ...(after ? { cursor: { id: after }, skip: 1 } : {}),
  });
  const hasNextPage = rows.length > first;
  const nodes = hasNextPage ? rows.slice(0, first) : rows;
  return {
    edges: nodes.map((node) => ({ node, cursor: node.id })),
    pageInfo: { hasNextPage, endCursor: nodes.at(-1)?.id ?? null },
    totalCount: await db[model].count({ where }),
  };
}
```
Typed filter operators to expose (Twenty's set): `eq, neq, gt, gte, lt, lte, in, like, ilike, startsWith, endsWith, isNull`. Build a `where` from `{ field: { op: value } }` filter objects.

---

## 7. Server Action with Zod validation + RBAC + event (the standard mutation shape)

```ts
// src/modules/records/actions/update-company.ts
'use server';
import { z } from 'zod';
import { getDb } from '@/lib/db';
import { assertCan } from '@/lib/rbac';
import { emitEntityEvent } from '@/lib/events';
import { auth } from '@clerk/nextjs/server';

const schema = z.object({ id: z.string(), name: z.string().min(1) });

export async function updateCompany(input: z.infer<typeof schema>) {
  const { id, name } = schema.parse(input);          // validate
  await assertCan('update', 'company');               // authorize
  const db = await getDb();                            // tenant-scoped
  const before = await db.company.findFirstOrThrow({ where: { id } });
  const after = await db.company.update({ where: { id }, data: { name } });
  const { userId, orgId } = await auth();
  await emitEntityEvent({ orgId: orgId!, object: 'company', operation: 'updated',
    recordId: id, before, after, actorId: userId!, at: new Date().toISOString() });
  return after;
}
```
**Every mutation follows this order: validate → authorize → tenant-scope → mutate → emit event.**

---

## 8. Background jobs (separate worker)

```ts
// src/lib/queue.ts — BullMQ; or Upstash QStash for serverless
import { Queue, Worker } from 'bullmq';
const conn = { connection: { url: process.env.REDIS_URL! } };
export const queue = (name: string) => new Queue(name, conn);

// worker.ts — RUN AS A SEPARATE PROCESS (Twenty runs workers separately)
new Worker('webhooks', async (job) => { /* match + POST with HMAC, retry */ }, conn);
new Worker('audit',    async (job) => { /* upsert timeline row */ }, conn);
```
Jobs: priorities, retries with backoff, retention. Keep workers in their own process/deploy.

---

## 9. Saved views → query (filters/sorts/visible fields as data)

Store a `View { type, filters Json, sorts Json, visibleFields String[] }` per object. A `viewToQuery(view)` helper translates it into the `where`/`orderBy`/column-set the record table consumes — exactly Twenty's `ViewQueryParamsService`. This makes list screens user-configurable for free.

## Related
- [[saas-blueprint-guide]] · [[architecture-patterns]] · [[folder-structure]] · [[twenty-crm]]
