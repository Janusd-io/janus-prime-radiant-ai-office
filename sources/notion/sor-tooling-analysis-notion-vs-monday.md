---
type: source
notion_url: https://www.notion.so/348114fc090c81d79220ef9b4e001c7f
notion_id: 348114fc-090c-81d7-9220-ef9b4e001c7f
title: SOR Tooling Analysis — Notion vs Monday.com
source_type: notion-page
fetched: 2026-05-06
---

# SOR Tooling Analysis — Notion vs Monday.com

**Analysis framing by Claude, 20 April 2026**
**Status:** Analysis in progress — awaiting Simon's ISO requirements before closing.

## Context

Bonaventure reframed the CEO Executive Management System from OKR-driven top-down to task-based bottom-up rollup with ISO-compliant workflow documentation as the foundation. This rebalances the tooling criteria.

**Bonaventure's stated preference:** Task-based, bottom-up work capture per department, with ISO-compliant workflows sitting alongside, such that AI agents can read meeting transcripts and write structured state into the right place.

**Constraint:** Asana is out.

## Head-to-head against criteria

| Criterion | Winner | Notes |
|---|---|---|
| Task-based, bottom-up rollup with CEO pull-up visibility | **Monday.com** | Boards → workspaces → dashboards is the core metaphor; 50-board ceiling on Enterprise covers 12 functions with headroom. |
| ISO-compliant workflow documentation | **Notion** | Workflow documentation, policies, procedures, evidence artefacts — Notion's native territory. Monday Docs is secondary. |
| Agent writability (Fireflies → SOR pipeline) | **Monday.com (slight edge)** | Both capable; Monday has mature REST + GraphQL APIs with good item CRUD semantics and webhooks. |
| Security, IAM, audit | Tie (Monday.com edge at enterprise) | Both: SOC 2 Type II, ISO 27001, SAML SSO, SCIM, audit logs on Enterprise. Monday additionally: ISO 27032, ISO 27701, DORA alignment. |
| Pricing transparency | Tie | Both publish mid-tier; custom at Enterprise. Monday has 3-seat minimum and bucket pricing — inflates small-team costs. |
| Multi-country playbook model | **Monday.com (slight edge)** | Template + board-duplication workflow built-in; Notion less native. |

## Three realistic paths

1. **Path 1 — Monday.com as SOR + Notion as documentation/knowledge plane (two-tool).** Each tool does what it's best at. Agent writes tasks to Monday, narrative and decisions to Notion, cross-links by ID. Matches Bonaventure's reframe most cleanly. Eventual two Enterprise contracts.

2. **Path 2 — Notion for everything.** Works, but task/dashboard UX is weaker. Cheaper, architecturally cleaner. Bets on Notion's 2026 roadmap.

3. **Path 3 — Monday.com for everything.** Works for task-heavy functions, but ISO documentation lives in a tool not designed for it. Risk: documentation plane gets neglected.

## Current lean

**Path 1 (two-tool) is the current lean** — keeps Linear intact for engineering/AI Projects. End state: Linear (engineering) + Monday.com (operations & CEO management) + Notion (documentation, ISO artefacts, knowledge base).

**This is a lean, not a decision.** Precondition: Simon's ISO requirements. If Simon has a preferred specialist ISO tool or wants tight coupling of docs to tasks, the lean shifts.

## Key open questions for Jehad

1. Is the Monday.com capability picture accurate?
2. Any gotchas with agent-driven task creation at scale (rate limits, webhook reliability, status transitions)?
3. OK to mark ClickUp (AIR-44) as Duplicate once tooling is locked in?
4. Your instinct on the path — given Bonaventure's reframe, still lean Monday-primary, or has the documentation-plane weight shifted your view toward two-tool?
