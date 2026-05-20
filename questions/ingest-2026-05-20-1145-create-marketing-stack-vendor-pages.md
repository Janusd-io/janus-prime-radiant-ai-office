---
type: question
title: Create vendor entity pages for the locked-in marketing stack (Cosmic, Attio, Vercel, Cloudflare, Cookiebot)?
slug: ingest-2026-05-20-1145-create-marketing-stack-vendor-pages
created: 2026-05-20
updated: 2026-05-20
departments: [ai-office, marketing, it-ops]
status: active
owner: michael-bruck
sources: [marketing-stack-technical-writeup, 2026-05-19-aio-mktg-meeting]
related: [agentic-lean-marketing-stack, stack-composition-framework, janus-website-cms, janus-crm-selection, singapore-launch]
---

# Create vendor entity pages for the locked-in marketing stack?

## Context

The 2026-05-19 marketing stack analysis ([[marketing-stack-technical-writeup]] + [[2026-05-19-aio-mktg-meeting]]) locked direction on 5 vendors that don't yet have their own `entities/vendors/` pages in the wiki. They all have AIR-* IDs in Linear (Linear AIR is system of record), but the wiki entity layer is empty for them, which means:

- Cross-references in the new [[agentic-lean-marketing-stack]] brief, [[janus-website-cms]], [[janus-crm-selection]], and [[singapore-launch]] hubs link to dangling slugs.
- Future ingest of meeting transcripts mentioning these vendors will lack a canonical entity to update.

## Proposed action

Create vendor entity stubs for the 5 adopted / in-flight tools:

| Slug | Vendor | AIR ID | Category | Stack Composition score |
|---|---|---|---|---|
| `cosmic` | Cosmic | AIR-117 | CMS (headless) | 3/3 |
| `attio` | Attio | AIR-76 | CRM | 3/3 |
| `vercel` | Vercel | AIR-113 | Hosting | 3/3 |
| `cloudflare` | Cloudflare | AIR-116 | Edge / DNS / WAF | 3/3 |
| `cookiebot` | Cookiebot | AIR-124 | Cookie / consent compliance | TBD (procurement target 2026-06-02) |

Each page would carry:

- Frontmatter: `type: vendor`, `confidence: high` (for the 4 confirmed) / `medium` (Cookiebot), `departments`, `sources`, `related`.
- Body: 1-paragraph summary, Linear AIR status, Stack Composition Framework score with the per-lens reasoning, role in the [[agentic-lean-marketing-stack]], operational status, watch-for list.

## Why this is being escalated (not auto-created)

Per CLAUDE.md §5.1 — creating new vendor entity pages is **high-stakes** (name-collision risk, duplication risk). The escalation captures the proposal so Michael can:

1. Confirm the 5 slugs are the right names.
2. Confirm we want vendor pages for each *now*, vs deferring until each vendor has more operational history (Cookiebot in particular is pre-procurement).
3. Catch any vendors already in the registry under a different slug that I missed.

## Alternative: defer

Wait until each vendor has its first substantive ingest event (Cosmic onboarding, Attio first leads import, Vercel deployment, Cloudflare DNS cutover, Cookiebot installation), then create the page from that ingest. Pro: every page starts with real operational content rather than a stub. Con: dangling wikilinks in the meantime; harder to update [[agentic-lean-marketing-stack]] later when each vendor gets its own page.

**Recommendation:** create all 5 now as stubs with the framework scoring captured (which is already a substantive contribution per page). Operational details accrete with each subsequent ingest.

## Other potentially-orphaned vendors from the same writeup (defer)

The writeup also analyses *rejected* vendors at length: Sanity, Contentful, Payload, Adobe AEM, HubSpot CMS Hub, Salesforce, HubSpot, Klaviyo. Proposed: **defer** creating pages for these unless / until they're referenced in another decision. The analysis lives in the [[agentic-lean-marketing-stack]] brief and the [[stack-composition-framework]] concept page; that's sufficient cross-reference for now.

## Status

Awaiting Michael's confirmation. No action taken yet.
