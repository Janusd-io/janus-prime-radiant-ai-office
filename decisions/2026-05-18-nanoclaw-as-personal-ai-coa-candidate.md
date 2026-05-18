---
type: decision
title: "NanoClaw identified as personal AI chief-of-staff candidate for Slack bot sprawl resolution"
slug: 2026-05-18-nanoclaw-as-personal-ai-coa-candidate
created: 2026-05-18
updated: 2026-05-18
status: active
departments: [ai-office]
countries: [ae, sg]
owner: michael-bruck
decided_by: bonaventure-wong
captured_by: jehad-altoutou
sources: [2026-05-18-ai-native-ceo]
related: [nanoclaw, air-103, slack, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms]
---

# NanoClaw identified as personal AI chief-of-staff candidate for Slack bot sprawl resolution

**Date:** 18 May 2026
**Source:** AI Native CEO meeting ([[2026-05-18-ai-native-ceo]])
**Decided by:** Bonaventure Wong (CEO) — raised the problem; joint decision on candidate

---

## Problem

Slack bot sprawl. Multiple per-person bots create UI clutter and an inconsistent experience — each bot handles one narrow task with no coherent identity or memory. Raised by Bonaventure in the 18 May 2026 CEO meeting.

---

## Decision

One bot per person, acting as a personal AI **chief-of-staff**. The bot routes tasks through a unified Slack interface rather than proliferating per-task bots.

**[[nanoclaw|NanoClaw]]** (by NanocoAI) identified as the technical candidate for this pattern.

AIR-103 created in Linear (AI Registry). Gate 1 assessment completed on 18 May 2026: **PASS on all five criteria.** Status: Evaluating. Gate 2 Technical Qualification to follow.

---

## Why NanoClaw

- **Self-hosted, Docker container isolation per agent** — meets Janus's per-user data control hard requirement ([[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]]). Each agent's data stays in its own container, user-controlled.
- **Native Slack Socket Mode** — direct integration path; listed in Slack App Directory.
- **Anthropic Agent SDK native** — built on Claude Agent SDK; first-class model support. Aligns with AIO's existing toolchain.
- **OneCLI Agent Vault** — credential management keeping secrets out of agent code; solves multi-bot credential sprawl.
- **MIT licence** — no vendor lock-in; full deployment control.
- **Open-source, 29k+ GitHub stars (as of 2026-05-18)** — active community + commercial backing (NanocoAI). Strong vendor viability signal.

---

## Gate 1 summary (2026-05-18)

| Criterion | Result |
|---|---|
| G1.1 Google Workspace | ✅ PASS |
| G1.2 Slack | ✅ PASS |
| G1.3 Data Portability | ✅ PASS |
| G1.4 Training Exclusion | ✅ PASS |
| G1.5 Documented API | ✅ PASS |

Full Gate 1 detail in the [[nanoclaw]] vendor entity page.

---

## Status

**Evaluating (Gate 2 pending).** Linear: AIR-103 in AI Registry team. Gate 1 comment posted (ID: ed1658cc-4571-4a21-b5e2-f27d479f2005).

Gate 2 (Technical Qualification) to be conducted next. No deployment decision made yet; NanoClaw is the candidate, not the confirmed tool.
