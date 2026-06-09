---
type: concept
title: SaaS Blueprint
slug: saas-blueprint
created: 2026-06-09
updated: 2026-06-09
departments: [ai-office, engineering]
captured_by: jehad-altoutou
audience: [department]
confidence: high
sources: [twenty-crm-deep-study]
related: [agent-harness, platform-development-process, 5-area-stress-test, html-as-deliverable]
---

# SaaS Blueprint

A self-contained **build-kit** for shipping a high-end SaaS / CRM / admin / dashboard product, distilled from a deep study of **Twenty CRM** (open-source CRM; github.com/twentyhq/twenty). It captures the architecture, design-system, and engineering discipline that make Twenty feel polished, re-expressed as paste-ready assets so a fresh Claude session can reproduce that quality **without access to the original repo**.

Target stack: Next.js 15 App Router + TypeScript · Prisma + Postgres · Clerk (orgs = tenants) · Tailwind + shadcn/ui · Stripe · Resend · Upstash Redis · Vercel. The *patterns* originate in Twenty (NestJS / TypeORM / Jotai / Linaria) and are translated to this stack.

## The kit (lives in `assets/saas-blueprint/`)

Read in order:
1. [[_SaaS Blueprint]] — philosophy, the 7 non-negotiables, build order (read first).
2. [[Folder Structure]] — repo skeleton + module convention + naming.
3. [[Design Tokens]] — paste-ready `globals.css` CSS vars + `tailwind.config.ts` (real Twenty-derived values) + the state-styling contract.
4. [[Architecture Patterns]] — 14 patterns each with a "use when" + the anti-patterns to avoid.
5. [[Code Recipes]] — working code: tenant-scoped Prisma, layered RBAC, the **event-driven backbone**, metadata-driven objects, polymorphic field renderer, cursor pagination, the standard Server-Action mutation shape, jobs, saved views.
6. [[DESIGN Templates]] — drop-in `DESIGN.md` for the **product register** and the **editorial register**.
7. [[Twenty CRM PROJECT_REFERENCE]] — the full 21-section deep reference for anything not covered.

## Why it matters here

The AIO ships platforms ([[platform-development-process]]); this is the reusable quality substrate for the build phase. Its two highest-leverage ideas:
- **Event-driven backbone** — emit one domain event per write, fan out to audit / webhooks / analytics / automation asynchronously (never inline side-effects).
- **Pick the design register before styling** — dense token-based *product* UI vs restraint-based *editorial* UI; mixing them is what makes work read as generic.

It also encodes the discipline behind the [[5-area-stress-test]] handover gate: tokens-not-hardcoding, tenant isolation everywhere, strict TS, repeated module convention.

## Provenance
Produced 2026-06-09 by Jehad from a multi-agent deep study of the Twenty CRM codebase. Mirror of the same kit in Jehad's personal Obsidian vault.
