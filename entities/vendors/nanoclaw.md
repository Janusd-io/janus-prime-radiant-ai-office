---
type: vendor
title: NanoClaw
slug: nanoclaw
created: 2026-05-18
updated: 2026-05-18
departments: [ai-office]
status: active
confidence: medium
sources: [2026-05-18-ai-native-ceo]
related: [openclaw, nemoclaw, slack, 2026-05-18-nanoclaw-as-personal-ai-coa-candidate, air-103]
---

# NanoClaw

Open-source, self-hosted AI agent orchestration framework by NanocoAI. MIT licence. At Janus, identified as the technical candidate for the Slack bot consolidation initiative — one personal AI chief-of-staff per person, replacing the current sprawl of per-task Slack bots.

**GitHub:** https://github.com/nanocoai/nanoclaw · **Docs:** https://nanoclaw.dev

## Key characteristics

- **Self-hosted.** Docker container isolation per agent; no SaaS vendor receives customer data. Strong G1.3 (data portability) and G1.4 (training exclusion) by architecture.
- **Anthropic Agent SDK native.** Built on top of the Claude Agent SDK; first-class Anthropic model support; v2.0.63 (May 2026).
- **Native Slack Socket Mode.** Multi-channel support (Slack, WhatsApp, Telegram, Discord, and others). Listed in Slack App Directory.
- **OneCLI Agent Vault.** Credential management system keeping secrets out of agent code; isolation between agents. Solves the multi-bot credential sprawl problem.
- **Google Workspace CLI skill** (`@googleworkspace/cli`): confirmed via GitHub issue #1122 — supports Google Workspace integration/export, satisfying G1.1.
- **Documented REST API and MCP-compatible.** Satisfies G1.5; MCP-native path exists for AI orchestration integration (G2.1).
- 29k+ GitHub stars (as of 2026-05-18). Active community, commercial backing (NanocoAI). Strong vendor viability signal.

## Janus evaluation status (as of 2026-05-18)

**Linear AIR-103 — Evaluating**

Gate 1 assessment: ✅ PASS on all five criteria (2026-05-18).

| Criterion | Result | Evidence |
|---|---|---|
| G1.1 Google Workspace | ✅ PASS | `@googleworkspace/cli` skill confirmed via GitHub issue #1122 |
| G1.2 Slack | ✅ PASS | Native Slack Socket Mode; Slack App Directory listing |
| G1.3 Data Portability | ✅ PASS | Self-hosted; all data stays on Janus infrastructure; MIT licence |
| G1.4 Training Exclusion | ✅ PASS | Self-hosted; no SaaS vendor receives data; Anthropic API terms cover model layer |
| G1.5 Documented API | ✅ PASS | REST API documented at nanoclaw.dev; MCP-compatible |

Gate 2 (Technical Qualification) to be conducted next.

## Use case at Janus

Slack bot sprawl — multiple per-person bots creating UI clutter and inconsistent experience — was raised by Bonaventure in the 18 May 2026 AI Native CEO meeting ([[2026-05-18-ai-native-ceo]]). Proposed pattern: one NanoClaw agent per person acting as a personal AI chief-of-staff, routing tasks through a unified Slack interface.

The self-hosted, Docker-isolated architecture directly addresses Janus's per-user data control requirement (per [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]]) — each agent's data stays in its own container, user-controlled.

## Relationship to OpenClaw / NemoClaw

NanoClaw is distinct from [[openclaw]] (the open-source agent foundation) and [[nemoclaw]] (NVIDIA's enterprise-hardened derivative). NanoClaw is a parallel open-source project by NanocoAI, purpose-built for multi-channel personal agent deployment. Not a fork of the OpenClaw lineage.
