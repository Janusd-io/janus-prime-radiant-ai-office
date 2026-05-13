---
type: vendor
title: OpenClaw
slug: openclaw
created: 2026-05-06
updated: 2026-05-07
departments: [ai-office]
status: active
confidence: medium
sources: [openclaw-assistant-ryancarson, air-39]
related: [agent-skills, agent-memory, agent-harness, nemoclaw]
---

# OpenClaw

Personal/developer-tier AI agent framework. Flexible infrastructure layer evaluated by Janus Digital in April 2026 against [[nemoclaw|NemoClaw]] (NVIDIA's enterprise-hardened derivative). OpenClaw itself is open-source and free for development use; ~$375/month licensing cost applies to production NVIDIA AI Enterprise (NAIE) deployment with SLAs and ISO 42001 certification.

## What it is

- **File-based agent state.** Operates over a folder of markdown task lists, meeting notes, and supporting workspace files (per Ryan Carson's [[openclaw-assistant-ryancarson|Carson implementation]]).
- **Skills + cron + Google Workspace.** Carson's setup uses skills (e.g., `daily-task-manager`, `executive-assistant`), scheduled cron jobs, and a "GOG" tool layer that integrates with Gmail / Calendar / Sheets / Docs.
- **Decentralized, MIT-licensed.** No backend data collection; local `~/.openclaw` folder only. Zero data training policy.
- **Carson-reported value:** "the most effective assistant and chief of staff I've ever worked with" — schedules meetings, parses booking links, follows up on emails, manages a markdown task list, runs an outreach tracker.

## Janus evaluation (April 2026)

Per [[air-39|AIR-39]] (Monitor status), OpenClaw was evaluated alongside NVIDIA's [[nemoclaw|NemoClaw]] for AI agent framework enrollment. **Verdict: NemoClaw approved; OpenClaw deferred.** Rationale:

- **OpenClaw strengths:** Local-only architecture provides strong data privacy for dev/personal use. Low cost. Flexible.
- **OpenClaw limitations:** Lacks runtime isolation (OpenShell), hardware-enforced data privacy (Privacy Router), and ISO 42001 audit trails needed for production compliance.
- **Recommendation:** OpenClaw suitable for internal R&D and personal assistant use; [[nemoclaw|NemoClaw]] chosen as production tier-1 core infrastructure provider for agentic development (per §5.1, §5.5, §5.7 requirements).

## Comparison to Anthropic stack

The pattern (file-based state, skills, cron, Google integrations) overlaps with [[claude|Claude Code]] routines + [[claude|Claude Skills]]. Key differences:

- **OpenClaw:** Local-first, folder-based state, no Anthropic dependencies, fully decentralized.
- **Claude Code:** API-based, cloud-hosted execution, tightly integrated with Claude models, commercial SaaS.

For Janus use cases, [[claude|Claude Code]] is preferred for production agent work (AIR-13); OpenClaw remains as a reference implementation for internal prototyping and personal assistant workflows.

## Memory model

File-based markdown task list + meeting notes. See [[agent-memory]] for broader context.
