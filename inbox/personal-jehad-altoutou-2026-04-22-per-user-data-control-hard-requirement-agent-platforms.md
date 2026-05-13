---
type: decision
title: Per-user, source-platform-faithful access control is a hard requirement for agent/integration platforms
slug: 2026-04-22-per-user-data-control-hard-requirement-agent-platforms
created: 2026-04-22
updated: 2026-05-13
status: resolved
owner: michael-bruck
departments: [ai-office]
confidence: high
sources: [pr-backup-2026-05-11-decision-per-user-data-control]
related: [viktor, ai-tool-evaluation-framework, ai-policy-gate]
audience: [department]
captured_by: jehad-altoutou
---

# Per-user, source-platform-faithful access control is a hard requirement

**Date:** 2026-04-22 (Viktor rejected); escalated to decision/policy on 2026-05-07. **Owner:** [[michael-bruck]]. **Status:** resolved.

## Decision

Any AI agent platform or integration tool evaluated for adoption at Janus Digital must enforce **per-user, source-platform-faithful access control**. This is now a **Gate 1 / Gate 2 criterion** and must be checked early in any future evaluation.

## What this means

1. **Integrations run under the requesting user's permissions**, not the connecting user's. If User A connects Google Drive to the agent platform, User B must not be able to access Drive data through the agent unless User B independently has Drive access.
2. **Source-platform access boundaries must be honoured in full.** ACLs from the source platform (Notion page permissions, Drive ACLs, Linear team membership) must be enforced when the agent reads or writes on a user's behalf.
3. **Workspace-level allow-lists and per-tool approval workflows are NOT sufficient substitutes** for proper per-user data-source ACLs.

## Background: Viktor (AIR-38)

Viktor is an AI agent platform designed to live in Slack. During sandbox evaluation (April 2026), the integration architecture flaw surfaced: integrations connected *per user* but accessible to the entire workspace. Example: Michael connects Notion to Viktor; every person in the Slack workspace can now query Notion data through Viktor, regardless of their Notion account status or permissions. Viktor's own response under direct questioning: *"Short answer: yes, User C could access Notion data through me [even though User C is not a Notion user]."*

Unacceptable risk for a multi-user, multi-jurisdiction consultancy. Viktor rejected 2026-04-22; Pro-tier account deleted 2026-05-04.

## Why this matters at Janus

Janus operates across multiple countries, multiple teams, and multiple projects with differentiated access models. Specifically:
- Engineering team members may have Linear access but not Notion access.
- Finance team members may have specific Sheets access but not broader Drive access.
- Country-specific teams (SG, UK) may have jurisdiction-locked data access.

An agent that says "my workspace integrations let anyone query anything" breaks all of these boundaries.

## Gate criteria update

**Gate 1, new criterion G1.6 (tentative):** Per-User Data Access Control — does the platform enforce per-user, source-platform-faithful access control? Failure = automatic Gate 1 FAIL.

**Gate 2, scoring criterion (tentative):** "Data boundary enforcement" added to Must Have.

## What counts as passing

- Integration runs under the *requesting* user's credentials / API key.
- Source platform's own access model (ACLs, permissions, roles) is queried at runtime.
- Agent explicitly denies access if the requesting user lacks source-platform permission.
- Audit trail shows which user made the request and whether it was allowed or denied.

## Scope

Applies to AI agent platforms (e.g., [[viktor]], future Slack agents), integration platforms designed to allow cross-tool orchestration, any tool acting as a proxy or orchestrator on behalf of multiple users.

Does NOT apply to single-user tools or tools where each user brings their own credentials (e.g., Claude Pro used by an individual).

## Future evaluation guidance

Ask early:
1. Does the platform support per-user authentication to integrated data sources?
2. Can I verify User A's permissions on Source X are honoured when User A queries Source X through the agent?
3. If User B is in a Slack channel but has no Notion access, can they query Notion through the agent if User A has connected Notion? Correct answer: no.

Hard requirement, not subject to trade-offs.
