---
type: vendor
title: OpenClaw
slug: openclaw
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office]
status: active
confidence: medium
sources: [pr-backup-openclaw]
related: [nemoclaw, claude]
audience: [department]
captured_by: jehad-altoutou
---

# OpenClaw

Personal/developer-tier AI agent framework. Flexible infrastructure layer evaluated by Janus Digital in April 2026 against [[nemoclaw|NemoClaw]] (NVIDIA's enterprise-hardened derivative). OpenClaw itself is open-source and free for dev use; ~$375/month licensing applies to production NVIDIA AI Enterprise (NAIE) deployment with SLAs and ISO 42001 certification.

## What it is

- **File-based agent state.** Operates over a folder of markdown task lists, meeting notes, and supporting workspace files (per Ryan Carson's implementation).
- **Skills + cron + Google Workspace.** Carson's setup uses skills (`daily-task-manager`, `executive-assistant`), scheduled cron, and a "GOG" tool layer integrating with Gmail / Calendar / Sheets / Docs.
- **Decentralized, MIT-licensed.** No backend data collection; local `~/.openclaw` only. Zero data training policy.
- **Carson-reported value:** "the most effective assistant and chief of staff I've ever worked with" — schedules meetings, parses booking links, follows up on emails, manages a markdown task list, runs an outreach tracker.

## Janus evaluation (April 2026)

Per AIR-39 (Monitor status), OpenClaw was evaluated alongside [[nemoclaw|NemoClaw]] for AI agent framework enrollment. **Verdict: NemoClaw approved; OpenClaw deferred.** Rationale:

- **OpenClaw strengths:** Local-only architecture provides strong data privacy for dev/personal use. Low cost. Flexible.
- **OpenClaw limitations:** Lacks runtime isolation (OpenShell), hardware-enforced data privacy (Privacy Router), ISO 42001 audit trails needed for production compliance.
- **Recommendation:** OpenClaw suitable for internal R&D and personal assistant use; NemoClaw chosen as production tier-1.

## Comparison to Anthropic stack

The pattern (file-based state, skills, cron, Google integrations) overlaps with [[claude|Claude Code]] routines + Claude Skills. Key differences:

- **OpenClaw:** Local-first, folder-based state, no Anthropic dependencies, fully decentralized.
- **Claude Code:** API-based, cloud-hosted execution, tightly integrated with Claude models, commercial SaaS.

For Janus use cases, [[claude|Claude Code]] is preferred for production agent work (AIR-13); OpenClaw remains as a reference implementation for internal prototyping and personal assistant workflows.

## Memory model

File-based markdown task list + meeting notes.
