---
type: vendor
title: Viktor
slug: viktor
air_id: AIR-38
status: Rejected
labels: [Functional]
departments: []
url: https://linear.app/janusd/issue/AIR-38/viktor
created: 2026-02-25
updated: 2026-05-04
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Viktor

> AI Registry entry [AIR-38](https://linear.app/janusd/issue/AIR-38/viktor) — status **Rejected** as of 2026-05-04. Departments: —.

**Category:** AI Agent Platform (In-Slack Coworker)
**Status:** REJECTED (2026-04-22) → account deleted 2026-05-04
**Cost:** Free Tier; $50 Pro; ~$250 Enterprise
**Departments:** Technology, AI Policy, Commercial

## Evaluation Summary

* **Gate 1 (Baseline):** PASS (G1.1-G1.5)
* **Gate 2 (Technical):** PASS (Score 23/25)
* **Gate 3 (Sandbox):** Initiated; **failed on per-user data-control architecture**

## Rejection — Per-user data control failure

Sandbox evaluation in #viktor-evaluation Slack channel (2026-04-03, with Michael Bruck, Jehad Altoutou, Andrey Timokhov) surfaced **structural data-control issue:**

* **Integrations connected per-user but used workspace-wide.** Michael connects Drive/Notion/[[linear|Linear]]; once connected, EVERY authorised channel member can invoke those integrations
* **Integration runs under connecting user's permissions, not requesting user's.** Viktor explicitly does NOT enforce source-platform access boundaries. If User C is in channel but has no Notion account, they can still pull Notion data via Viktor.
* **First-line defence is workspace allow-list, not per-tool ACLs.** Per-call approval doesn't scale and doesn't enforce source platform's access model.

Viktor's own direct response: *"Short answer: yes, User C could access Notion data through me."*

This is the **wrong shape of access control** for multi-user, multi-jurisdiction consultancy where Notion/Drive/Linear access boundaries are deliberately differentiated by team and project.

## Account Deletion (2026-05-04)

Triggered by $50 Pro tier payment coming due. Reasons stated:
* Does not fit Janus requirements
* Requires more role-based account controls to data sources

## Lessons Captured (Future Evaluations)

Per-user, source-platform-faithful access control is a **HARD REQUIREMENT** for any AI agent/integration platform at Janus:

1. Integration must run under REQUESTING user's permissions, not connecting user's
2. Source-platform access boundaries (Notion page permissions, Drive ACLs, Linear team membership) must be honoured in full
3. Workspace allow-list + per-tool approval are NOT substitutes for proper per-user data-source ACLs

**Now a Gate 1 / Gate 2 criterion for all future agent platform evaluations.**

*Rejected.*
