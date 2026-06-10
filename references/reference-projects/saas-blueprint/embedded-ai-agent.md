---
type: reference
title: Embedded AI Agent — In-Platform RBAC-Scoped Tool Execution
slug: embedded-ai-agent
created: 2026-06-10
updated: 2026-06-10
departments: [ai-office, engineering]
captured_by: jehad-altoutou
audience: [department]
related: [saas-blueprint-guide, code-recipes, twenty-crm-project-reference, ims-digital-twin, saas-engineering-patterns]
---

# Embedded AI Agent — In-Platform RBAC-Scoped Tool Execution

> How to put an **AI chat inside your own product** that lets a logged-in user perform real actions (create/update/delete) on the platform — safely scoped to *that user's* permissions. Distilled from Twenty CRM's in-app agent + MCP, and the Assessify build. Part of the [[saas-blueprint-guide|SaaS Blueprint]]; pairs with the RBAC recipe in [[code-recipes]].

## When to use this (vs. external MCP)
- **Embedded (this doc):** an AI chat *field inside the app*, serving only this platform, acting as the logged-in user. Easier for end-users, you control auth/tools/scoping, no external client to configure. **Default for "let our users do things via chat."**
- **External MCP server:** expose your platform to *outside* AI clients (Claude Desktop, Cursor, n8n). Use when third-party agents must operate your platform. More surface area, OAuth, token management.
- They share the **same tool layer** — build tools once, expose to both. (Twenty does exactly this.)

## The golden rule
> **The agent acts AS the requesting user, with that user's permissions — never a shared god/service identity.** An admin chatting can do admin things; a scoped user can only do what their role allows. The agent must never exceed the human's own access.

This is the #1 thing teams get wrong (Assessify shipped scopes that were *stored but never enforced* → every admin token was god-mode). Permissions must be checked **at execution time, per tool call, against the acting user.**

## Architecture
```
Chat UI (client component, streaming)
  → POST /api/agent/chat   (auth: the user's existing SESSION, not a service key)
     → resolve actingUser { id, role, scopes, tenantId, office/dept scope }
     → AI SDK tool-calling loop (streamText with tools)
        → each tool, before executing:
             1. assertCan(actingUser, action, entity)      ← RBAC gate
             2. apply scope filters (tenant/office/dept)    ← row scoping
             3. field-level redaction on outputs            ← PII control
             4. validate input (Zod)
             5. run (service layer / Prisma)
             6. emit audit event { actingUser, tool, args, before/after }
     → stream tokens + tool results back to the UI
```

## Five non-negotiable controls
1. **Identity = the session user.** Derive permissions from the logged-in session, not from a token that carries fixed scopes. (If you reuse an MCP-token path, load the token's *user* and apply *their* live role/scope.)
2. **Per-tool authorization.** Every write tool calls `assertCan(user, 'update'|'delete'|'create', entity)` first. Don't rely on "the model won't call it."
3. **Scope filters actually applied.** Tenant/org/office/department filters must be in the Prisma `where` of *every* tool — not imported-and-forgotten. Read tools too (don't leak cross-scope data).
4. **An "automation-allowed" flag per entity.** Mark sensitive entities (PII, audit logs, money) as not-agent-writable even for admins (Twenty's `canBeManagedByAutomation`). Agent writes check it.
5. **Audit every tool call** (who, which tool, args, before/after) — via your event backbone ([[code-recipes]] §3). Distinguish agent-initiated from UI-initiated.

## Tool registry pattern (generate once, gate per call)
```ts
// lib/agent/tools.ts — one tool per (entity, op), gated at execution
type ActingUser = { id: string; role: Role; scopes: string[]; orgId: string; office?: string|null; deptIds?: string[]|null };

export function buildToolsForUser(user: ActingUser) {
  const tools: Record<string, Tool> = {};
  for (const entity of AGENT_ENTITIES) {
    // READ
    if (can(user, 'read', entity)) {
      tools[`find_${entity.plural}`] = tool({
        description: `Search ${entity.label} …`,
        parameters: entity.findSchema,            // Zod
        execute: async (args) => {
          const where = applyScope(user, entity, toWhere(args));   // tenant/office/dept
          const rows = await db[entity.model].findMany({ where, take: 50 });
          return redactFields(user, entity, rows);                 // field-level PII
        },
      });
    }
    // WRITE — only if role allows AND entity is automation-manageable AND token has 'write' scope
    if (can(user, 'update', entity) && entity.canBeManagedByAutomation && user.scopes.includes('write')) {
      tools[`create_one_${entity.singular}`] = tool({
        description: `Create a ${entity.label} …`,
        parameters: entity.createSchema,
        execute: async (args) => {
          assertCan(user, 'create', entity);                       // belt + suspenders
          const data = applyScopeOnCreate(user, entity, args);     // force orgId/office
          const row = await db[entity.model].create({ data });
          await emitEvent({ actor: user.id, via: 'agent', op: 'create', entity: entity.model, after: row });
          return row;
        },
      });
      // …update_*, delete_* similarly, each gated + audited
    }
  }
  return tools;
}
```

## The chat endpoint (streaming + tool loop)
```ts
// app/api/agent/chat/route.ts
import { streamText } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';

export async function POST(req: Request) {
  const user = await getActingUserFromSession();          // session, NOT a god key
  if (!user) return new Response('Unauthorized', { status: 401 });
  const { messages } = await req.json();
  const result = streamText({
    model: anthropic('claude-sonnet-4-6'),
    system: buildSystemPrompt(user),                      // includes the user's scope + schema + "only act within permissions"
    messages,
    tools: buildToolsForUser(user),                       // tools the user is allowed to use
    maxSteps: 8,                                          // bound the tool loop
  });
  return result.toDataStreamResponse();
}
```

## Guardrails worth adding
- **Confirmation gates** for destructive ops: tool returns a "proposed action" the UI confirms before a second call executes it (Twenty's "search before create; present before delete").
- **Rate limit + step cap** (`maxSteps`) to bound runaway loops.
- **Read-only mode** option (build a token/session flag → only read tools registered).
- **Server-side input validation (Zod)** on every tool — never trust model args.
- **Redact PII** in tool outputs by the user's field permissions before they reach the model/UI.

## Anti-patterns (the exact mistakes to avoid)
- Scopes/permissions *stored but never checked at execution* (looks secure, isn't).
- Scope-filter helpers *imported but never called* → cross-tenant/cross-dept leakage.
- A single shared full-access service token behind the chat → every user inherits god-mode.
- Letting the model's tool call run without a server-side `assertCan`.
- No audit distinction between agent actions and human actions.
- Exposing destructive tools on PII/audit/financial entities with no automation-allowed gate.

## See also
- [[twenty-crm-project-reference]] §21.5 (Twenty's MCP + in-app agent + RBAC tool registry — the reference implementation).
- [[code-recipes]] §2 (RBAC guard), §3 (event backbone / audit), §7 (validate→authorize→scope→mutate→emit).
- [[saas-blueprint-guide]] · [[saas-engineering-patterns]].
