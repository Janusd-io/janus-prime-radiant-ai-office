---
type: decision
title: Monday.com + Hostinger + Notion Tech Stack Adopted as Janus Operations Foundation
slug: 2026-04-23-monday-hostinger-notion-stack-adopted
created: 2026-05-06
updated: 2026-05-12
status: resolved
owner: michael
departments: [ai-office, it-ops, office-of-ceo]
countries: [sg, gb, us]
confidence: high
sources: [aio-completed-action-items-archive, sor-tooling-analysis-notion-vs-monday, aio-weekly-status-2026-04-20-24]
related: [monday, notion, hostinger, janus-prime-radiant-build]
---

# Decision: Monday.com + Hostinger + Notion Stack Adopted

**Date:** 23 April 2026  
**Owner:** Michael Bruck  
**Status:** Resolved  
**Confidence:** High  

## What

Janus AI Office and operations adopted a three-tool stack for system-of-record and infrastructure:

1. **[[monday]] — Operations and CEO executive management system of record.** Pro plan, 3 seats, MCP connector operational.
2. **Hostinger — Self-hosted infrastructure platform.** Malaysian data centre, flat monthly pricing ($920–1,020/2yr), Docker-ready, replaced GCP for cost and operational control.
3. **[[notion]] — Documentation, ISO artefacts, knowledge base.** Remains canonical for written processes, ISO compliance documentation, and team knowledge.

[[linear]] remains focused on engineering delivery and AI Projects (AIR).

## Why

### Monday.com over Notion for operations SoR

- **Task-based rollup:** Monday's boards → workspaces → dashboards metaphor matches Bonaventure's reframe (task-based, bottom-up).
- **Agent writability:** Mature REST + GraphQL APIs, good item CRUD semantics, webhooks. Better than Notion for writing structured operational state.
- **Ceiling:** 50-board Enterprise plan covers 12 functions with headroom.

### Hostinger over GCP for self-hosting

- **Metered billing complexity:** GCP showed unpredictable per-cron costs during pilot setup. ($13–30 spikes; total trajectory $4,290–5,000/2yr).
- **Hostinger wins on:** flat pricing (~$920–1,020/2yr for 2 CPU / 8GB RAM / 100GB), Docker-ready, root access, one-click N8N, simpler DNS/subdomain.
- **GCP narrowed:** managed-service and departmental use cases only (HR, Marketing, Cloud SQL/TPU needs). Not the default for AI Office tooling.

### Notion remains documentation

- **Workflow documentation, ISO evidence, policies, procedures.** Notion's native territory.
- **ISO compliance gap:** [[monday]] Docs is secondary, not a knowledge system. Two-tool keeps documentation-first for ISO readiness.

## Impact on operations

- **Daily standup logging moved to [[monday]]** (via `/standup` skill). Notion remains narrative and decision journal.
- **AI agents write tasks to [[monday]]**, narrative/decisions to Notion.
- **ClickUp discontinued.** Asana rollout for CEO weekly killed (Monday replaces need).
- **Weekly PowerPoint reporting killed** in favour of Monday dashboards.

## Lock-in considerations

- [[monday]] provides managed hosting; [[hostinger]] provides self-hosted infrastructure flexibility for AI Office-owned tools ([[n8n]]).
- Neither introduces vendor lock-in relative to custom build-out. Both are third-party best-of-breed per Bonaventure's philosophy.

## Related decisions

- **2026-04-20 — ISO-first stack architectural pivot** (enables this choice).
- **2026-04-22 — Notion confirmed as ISO repository** (Simon meeting).
- **2026-04-23 — Assessify production support ownership established** (ops SoR impact).

## Timing

- **Monday.com Pro plan activated 23 Apr.** MCP connector operational. 3 seats approved pending user count.
- **Hostinger setup completed 20 Apr.** Malaysian DC, payment processed, company account established.
- **GCP scope narrowed 20 Apr.** Managed-service only; self-hosted default moves to Hostinger.

## Open items

- **IT-approved tools list v3:** Cloud (Cowork) + Cloud Code to be added; browser-mode restricted to app-only (token-spike control).
- **Sandbox → IT-production handoff SOP:** Needs formal SOP/README, sign-off, test-vs-deployment criteria.
- **[[monday]] multi-workspace strategy:** Awaiting Javin (Monday consultant) call 7 May, 3pm — per-department/per-branch structure and corporate discount.

## Confidence and dependencies

**Confidence:** High. Both Monday and Hostinger are locked based on a week of evaluation and live pilot use (Monday 20–23 Apr, Hostinger selection 20 Apr, setup by 23 Apr).

**Dependencies:** Simon's ISO programme pace (determines when departments can document workflows and gate automation). Bonaventure's executive-system requirements (shapes Monday dashboard design).
