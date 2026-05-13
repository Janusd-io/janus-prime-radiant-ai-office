---
type: decision
title: Per-user, source-platform-faithful access control is a hard requirement for agent/integration platforms
slug: 2026-04-22-per-user-data-control-hard-requirement-agent-platforms
created: 2026-04-22
updated: 2026-05-13
status: resolved
owner: michael
departments: [ai-office]
sources: [air-38, jehad-vault-2026-04-22-per-user-data-control-hard-requirement-agent-platforms]
related: [viktor]
---

# Per-User, Source-Platform-Faithful Access Control is a Hard Requirement for Agent/Integration Platforms

**Date:** 2026-04-22 (Viktor rejected); escalated to decision/policy on 2026-05-07  
**Owner:** Michael Bruck  
**Status:** Resolved  

## Decision

Any AI agent platform or integration tool evaluated for adoption at Janus Digital must enforce **per-user, source-platform-faithful access control**. This is now a **Gate 1 / Gate 2 criterion** and must be checked early in any future evaluation.

## What this means

1. **Integrations run under the requesting user's permissions, not the connecting user's.** If User A connects Google Drive to the agent platform, User B must not be able to access Drive data through the agent unless User B independently has Drive access.

2. **Source-platform access boundaries must be honoured in full.** Access controls from the *source* platform (Notion page permissions, Drive file ACLs, Linear team membership, etc.) must be enforced when the agent reads or writes on a user's behalf.

3. **Workspace-level allow-lists and per-tool approval workflows are not sufficient substitutes** for proper per-user data-source ACLs. They do not enforce the source platform's own permission model.

## Background: Viktor (AIR-38)

Viktor is an AI agent platform designed to live in Slack. During sandbox evaluation (April 2026), the following data-control issue was discovered:

- **Integration architecture flaw:** Integrations (Google Drive, Notion, Linear, etc.) are connected *per user* but then accessible to the *entire workspace*.
- **Example:** Michael connects Notion to Viktor; every person in the Slack workspace can now query Notion data through Viktor, regardless of their Notion account status or permissions.
- **Viktor's own response to direct questioning:** "Short answer: yes, User C could access Notion data through me [even though User C is not a Notion user]."

This creates an unacceptable risk for a multi-user, multi-jurisdiction consultancy where team and project access boundaries are deliberate and load-bearing (e.g., some teams have Notion workspace access, others do not).

**Outcome:** Viktor was rejected on 2026-04-22 and the Pro-tier account was proactively deleted on 2026-05-04.

## Why this matters at Janus

Janus operates across multiple countries, multiple teams, and multiple projects with differentiated access models. Collapsing those boundaries — even for an "AI assistant" — violates our access governance principle that each platform's own permission model is canonical.

Specifically:
- Engineering team members may have Linear access but not Notion access.
- Finance team members may have specific Sheets access but not broader Drive access.
- Country-specific teams (Singapore, UK) may have jurisdiction-locked data access.

An agent that says "my workspace integrations let anyone query anything" breaks all of these boundaries.

## Gate 1 / Gate 2 criteria update

**Gate 1, new criterion G1.6 (tentative):**
- "Per-User Data Access Control: Does the platform enforce per-user, source-platform-faithful access control? Requesting user's permissions must be checked against the source platform."
- Failure = automatic Gate 1 FAIL (no progression).

**Gate 2, scoring criterion (tentative):**
- "Data boundary enforcement" added to "Must Have" section.

## What counts as "passing" this criterion

- ✅ Integration runs under the *requesting* user's credentials / API key
- ✅ Source platform's own access model (ACLs, permissions, roles) is queried at runtime
- ✅ Agent explicitly denies access if the requesting user lacks source-platform permission
- ✅ Audit trail shows which user made the request and whether it was allowed or denied

## Scope

This decision applies to:
- AI agent platforms (e.g., Viktor, future Slack agents)
- Integration platforms designed to allow cross-tool orchestration
- Any tool that acts as a "proxy" or "orchestrator" on behalf of multiple users

This does NOT apply to single-user tools or tools where each user brings their own credentials (e.g., Claude Pro used by individual user).

## Future evaluation guidance

When evaluating agent/integration platforms, ask early:
1. "Does the platform support per-user authentication to integrated data sources?"
2. "Can I verify that User A's permissions on Source X are honoured when User A queries Source X through the agent?"
3. "If User B is in the Slack channel but has no Notion access, can they query Notion through the agent if User A has connected Notion?"
   - Correct answer: "No, we enforce source-platform access boundaries."
   - Wrong answer: "Yes, they can query Notion data even though they're not a Notion user."

## Exceptions

None anticipated. This is a hard requirement, not a scoring criterion subject to trade-offs.
