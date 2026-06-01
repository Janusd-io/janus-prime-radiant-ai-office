---
type: vendor
title: NanoClaw
slug: nanoclaw
created: 2026-05-18
updated: 2026-05-24
departments: [ai-office]
status: active
confidence: high
sources: [2026-05-18-ai-native-ceo, 2026-05-19-aio-standup, 2026-05-20-aio-standup, 2026-05-21-aio-standup, 2026-05-22-aio-standup]
related: [openclaw, nemoclaw, slack, hostinger, github, 2026-05-18-nanoclaw-as-personal-ai-coa-candidate, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms, nanoclaw-prime-radiant-wiring]
migrated_from: entities/vendors/nanoclaw.md
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

## Janus evaluation status

**Linear AIR-103 — Evaluating (Gate 1 PASS 2026-05-18). Gate 2 not yet started in Linear, but install is dogfooded — Linear status lags reality.**

Gate 1 assessment (2026-05-18): ✅ PASS on all five criteria.

| Criterion | Result | Evidence |
|---|---|---|
| G1.1 Google Workspace | ✅ PASS | `@googleworkspace/cli` skill confirmed via GitHub issue #1122 |
| G1.2 Slack | ✅ PASS | Native Slack adapter (`@chat-adapter/slack@4.26.0`); Slack App Directory listing |
| G1.3 Data Portability | ✅ PASS | Self-hosted; all data stays on Janus infrastructure; MIT licence |
| G1.4 Training Exclusion | ✅ PASS | Self-hosted; no SaaS vendor receives data; Anthropic API terms cover model layer |
| G1.5 Documented API | ✅ PASS | REST API documented at nanoclaw.dev; MCP-compatible |

Gate 2 status correction (2026-05-24): the Linear status of "Evaluating" is now stale — the bot is operating in daily dogfood on Michael's MacBook with read-only Prime Radiant access and a scheduled news digest running. The correct pipeline stage is Sandbox. Re-run `/ai-tool-evaluation` against the live install rather than the GitHub README — the install itself is the artefact under test.

## Use case at Janus

Slack bot sprawl — multiple per-person bots creating UI clutter and inconsistent experience — was raised by Bonaventure in the 18 May 2026 AI Native CEO meeting ([[2026-05-18-ai-native-ceo]]). Proposed pattern: one NanoClaw agent per person acting as a personal AI chief-of-staff, routing tasks through a unified Slack interface.

The self-hosted, Docker-isolated architecture directly addresses Janus's per-user data control requirement (per [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]]) — each agent's data stays in its own container, user-controlled.

## Janus deployment (as of 2026-05-24)

Full deployment writeup with cited paths in [[nanoclaw-prime-radiant-wiring]]. Summary:

- **Installed at** `~/Code/nanoclaw-v2/` on Michael Bruck's MacBook. Version pinned to **v2.0.64**. Upstream repo `nanocoai/nanoclaw`.
- **Process model.** Single Node host process (`src/index.ts`, run via `dist/index.js`) orchestrates per-session Bun-runtime Docker containers. No docker-compose, no k8s — orchestration is bespoke in `src/container-runner.ts`. Service managed via macOS launchd (`~/Library/LaunchAgents/com.nanoclaw.plist`, template at `launchd/com.nanoclaw.plist`).
- **Slack reachability.** HTTP webhook mode (`SLACK_BOT_TOKEN` + `SLACK_SIGNING_SECRET`, no Socket Mode app token). Public reachability via Ngrok free-tier tunnel today; [[hostinger]] VPS + Caddy reverse proxy migration planned (Monday 2931866304; AIR-79, AIR-133). Adapter: `@chat-adapter/slack@4.26.0`. Slack channel/DM scoping lives in the `messaging_groups` table in `data/v2.db`.
- **Agent groups on disk.** `dm-with-michaelb` is the one live wired group (agent group ID `ag-1779283681855-gu6whc`, assistantName "Nano" per `groups/dm-with-michaelb/container.json`). `groups/main/` and `groups/_ping-test/` exist as unwired scaffolds. Andrew Soane's NanoClaude install (confirmed verbally 2026-05-21) has not materialised on this host — Andrew's deployment will be on his own Windows machine.
- **Vault access.** Read-only by policy. Vault mounted into containers at `/workspace/agent/vault`, sourced from a **separate git clone** at `~/Code/nanoclaw-v2/groups/dm-with-michaelb/vault/` of [[github|`Janusd-io/janus-prime-radiant-ai-office`]] — *not* the canonical curator clone at `~/janus/prime-radiant/ai-office/`. Host runs `git pull` to refresh; container network egress is OneCLI-gated and cannot reach `github.com`. CLAUDE.local.md for the group explicitly prohibits writes/commits/pushes from the container.
- **Skills wired into the agent.** 7 container skills (`agent-browser`, `frontend-engineer`, `onecli-gateway`, `self-customize`, `slack-formatting`, `vercel-cli`, `welcome`) plus composed CLAUDE.md fragments (`module-agents`, `module-cli`, `module-core`, `module-interactive`, `module-scheduling`, `module-self-mod`, `skill-onecli-gateway`). **Janus Prime Radiant skills (`/standup`, `/ai-registry`, `/ai-tool-evaluation`, lint) are not wired** — they remain Claude Code skills invoked from Michael's terminal.
- **MCP connectors wired.** Zero. Both root `.mcp.json` and `groups/dm-with-michaelb/container.json` show `mcpServers: {}`. Linear, Notion, Monday, Fireflies, Gmail — none connected. Installer skills are available on the host for `add-linear`, `add-gmail-tool`, `add-gcal-tool`, `add-github`, `add-resend`, `add-mnemon`, `add-opencode`, `add-karpathy-llm-wiki`; Notion/Monday/Fireflies need custom MCP wiring (no installer skill).
- **OneCLI Agent Vault — deployed and active.** Local service at `ONECLI_URL`; web UI `http://127.0.0.1:10254`; SDK `@onecli-sh/sdk@^0.5.0`. All non-Slack secrets (Anthropic key, etc.) live in OneCLI and inject per-request, never in container env vars. Known gotcha: agents start in `selective` secret mode with zero secrets — must be flipped to `all` or explicitly assigned via `onecli agents set-secret-mode --mode all`. Approval-gating of credentialed actions is supported by architecture but **not currently configured** for Janus.
- **Per-person isolation.** Architecture supports three tiers (`docs/isolation-model.md`); Janus uses the strongest: one host process per machine, one agent group per user inside the host, one Docker container per active session with private `inbound.db`/`outbound.db`. Because each Janus user has their own machine, the per-machine layer naturally collapses into per-user isolation.
- **Active ingest flows.** Slack-DM vault Q&A (read-only); scheduled 7AM news digest (75 articles tracked in `groups/dm-with-michaelb/newsbot-seen.json`); HTML deck generation (`nano-capabilities.html` demo); Chrome MCP for browser tasks; SQLite working memory per session. **Not yet open:** Slack-as-inbox, conversational-query-filed-back-as-brief, AIO-channel AI eval bot (planned 2026-05-22 but no wired agent group yet).

## Relationship to OpenClaw / NemoClaw

NanoClaw is distinct from [[openclaw]] (the open-source agent foundation) and [[nemoclaw]] (NVIDIA's enterprise-hardened derivative). NanoClaw is a parallel open-source project by NanocoAI, purpose-built for multi-channel personal agent deployment. Not a fork of the OpenClaw lineage.
