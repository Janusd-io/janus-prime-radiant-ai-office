---
type: vendor
title: Hermes Agent
slug: hermes
created: 2026-06-11
updated: 2026-06-12
departments: [ai-office, it-ops]
status: evaluating
confidence: medium
sources: [2026-06-11-jon-austin-cto-intro]
related: [nanoclaw, janus-prime-radiant-build, jon-austin]
---

# Hermes Agent

Open-source autonomous AI agent framework by NousResearch. Released February 2026. MIT licence, self-hosted by default; FlyHermes is the managed cloud path. 64,000+ GitHub stars. In active evaluation as of 2026-06-11 (Linear AIR-163, Evaluating).

GitHub: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

## What it is

An agent that lives on your server, not an IDE plugin or a chatbot. Core differentiator: persistent memory across sessions — it stores project context in `~/.hermes/` and gets more capable the longer it runs. Not a one-shot tool executor; an always-on agent that accumulates knowledge.

## Key capabilities

- **Provider abstraction** — model-agnostic; works with Anthropic, OpenAI, OpenRouter (200+ models), Ollama, vLLM, and any OpenAI-compatible endpoint. Backend is a config change.
- **SKILL.md skill system** — writes reusable skill documents as it solves problems; shareable via agentskills.io community hub. **Correction (2026-06-12):** despite the shared `SKILL.md` filename, the code-level evaluation found Hermes' skill format is its own ecosystem (skills carry Hermes-specific `metadata.hermes` blocks) and is *not* compatible with the Anthropic Claude Code / Cowork skill format — Janus's existing skills do not port. The original "same format" claim came from the intro-call framing and is superseded by the codebase read.
- **Multi-platform gateway** — Telegram, Discord, Slack, WhatsApp, Signal, CLI in one gateway process. Start a conversation on Telegram, pick it up in terminal.
- **Cron scheduler** — unattended daily/nightly/weekly automations with results delivered to any platform.
- **Parallel sub-agents** — orchestrator/worker model; configurable `max_spawn_depth`; concurrent agents share filesystem state.
- **Browser/web control** — full automation: navigate, click, type, screenshot, vision.
- **MLOps / RL** — Atropos RL integration, batch trajectory generation, ShareGPT export for fine-tuning.

## Commercial model

Self-hosted: free forever (MIT). FlyHermes (flyhermes.ai): managed cloud, pricing shown at signup (API costs included, zero ops overhead). The Supabase model — open source core with a hosted SaaS layer.

## Why it's in evaluation

Recommended by [[jon-austin|Jon Austin]] (incoming CTO) on 11 June 2026, citing active adoption in CTO WhatsApp groups. Evaluation process mirrors [[nanoclaw|NanoClaw]]: clone GitHub repo, test via Claude Code CLI, assess fit for Janus use cases.

**Two strategic angles (as captured from the call):** (1) ~~SKILL.md compatibility means Janus's existing skills may be directly portable~~ — falsified by the code read (see Key capabilities correction); (2) provider abstraction addresses single-model lock-in risk as agent deployments scale — holds, but is of limited value to the Claude-native Prime Radiant stack.

## Evaluation outcome — code-level pass (2026-06-11/12)

Deep code-level evaluation against [[nanoclaw|NanoClaw]] as the Prime Radiant front-end concluded **stay on NanoClaw**. Three findings: (1) Hermes runs its own OpenAI-compatible agent loop with Anthropic as one pluggable provider — it does not read CLAUDE.md, and its skill format is not Anthropic-compatible, so the Prime Radiant rulebook and the AIO skill fleet would need re-implementation; (2) default execution is on-host (containers opt-in), vs NanoClaw's per-session container isolation, mount allowlist, and request-time credential injection; (3) Hermes' autonomous memory/skill self-improvement loop competes with the wiki's human-curated discipline rather than serving it. Hermes' strengths (model-agnosticism, channel breadth, learning loop) point at a different problem than ours.

Verdict is architectural, not yet empirical: a time-boxed hands-on arm (same acceptance tests as NanoClaw, same sandbox vault) is specced in the trial plan. Working docs: `~/Code/hermes/` (assessment, deeper evaluation, trial spec). Jon Austin updated by email 2026-06-12 — see [[2026-06-12-jon-austin-hermes-evaluation-email]]. Linear AIR-163 should move from Evaluating once the hands-on arm completes.

## Watch for

- ~~SKILL.md format compatibility with Janus's existing Claude Code / Cowork skill format~~ — resolved 2026-06-12: it diverges; not compatible (see Evaluation outcome)
- Whether Hermes can run reliably as a background daemon on Hostinger (Prime Radiant scheduled ingest use case)
- NanoClaw vs Hermes: differentiation in practice for the persistent-Slack-agent use case
- FlyHermes pricing when it surfaces
