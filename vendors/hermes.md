---
type: vendor
title: Hermes Agent
slug: hermes
created: 2026-06-11
updated: 2026-06-12
departments: [ai-office, it-ops]
status: rejected
confidence: high
sources: [2026-06-11-jon-austin-cto-intro]
related: [nanoclaw, janus-prime-radiant-build, jon-austin]
---

# Hermes Agent

Open-source autonomous AI agent framework by NousResearch. Released February 2026. MIT licence, self-hosted by default; FlyHermes is the managed cloud path. 64,000+ GitHub stars. Evaluated 2026-06-11/12 and **rejected** as a fit for Janus (Linear AIR-163 moved to Rejected on 2026-06-12); [[nanoclaw|NanoClaw]] (AIR-103) remains the chosen Prime Radiant front-end. Kept in the toolkit as awareness, not adoption.

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

The verdict from the code-level pass was architectural; a time-boxed hands-on arm (same acceptance tests as NanoClaw, same sandbox vault) was specced in the trial plan. Working docs: `~/Code/hermes/` (assessment, deeper evaluation, trial spec). Jon Austin updated by email 2026-06-12 — see [[2026-06-12-jon-austin-hermes-evaluation-email]].

**Ratified at the AIO standup, 12 June 2026.** Michael confirmed the rejection without waiting on the hands-on arm: "I'm not sure I have a use case for Hermes now that I understand it better" — it's "not for us": OpenAI-based rather than Claude-based, its own database rather than plain markdown files and folders, no CLAUDE.md awareness, and a much bigger piece of software than NanoClaw. Linear AIR-163 moved Evaluating → **Rejected** on 2026-06-12 (cross-referenced to AIR-103 NanoClaw, which remains the chosen front-end in Sandbox). Two positives stand: it's still an impressive piece of software ("keep in our toolkit" as awareness), and its automated continual learning — unlike Prime Radiant's human-curated discipline — is worth watching as a viable option for people who don't want to do the human curation thing. The previously-specced hands-on trial arm is now optional/dormant rather than a gate on the registry status.

## Watch for

- ~~SKILL.md format compatibility with Janus's existing Claude Code / Cowork skill format~~ — resolved 2026-06-12: it diverges; not compatible (see Evaluation outcome)
- ~~Whether Hermes can run reliably as a background daemon on Hostinger~~ — moot as of 2026-06-12 rejection
- ~~NanoClaw vs Hermes: differentiation in practice~~ — resolved 2026-06-12: NanoClaw chosen; AIR-163 Rejected
- **Automated continual learning** — Hermes' autonomous memory/skill self-improvement loop, vs Prime Radiant's human-curated model. Watch whether it proves a viable option for teams that don't want to do human curation (per Michael, AIO standup 2026-06-12). This is the one live watch item.
- FlyHermes pricing when it surfaces (low priority post-rejection)
