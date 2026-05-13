---
type: vendor
title: Claude (Anthropic product family)
slug: claude
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office, engineering]
status: active
confidence: high
sources: [karpathy-llm-wiki, anthropic-building-effective-agents, claude-managed-agents-launch, claude-managed-agents-quickstart, claude-managed-agents-scaling, claude-managed-agents-memory, claude-managed-agents-memory-rlancemartin, claude-code-routines, claude-code-prompt-caching-lessons, claude-code-limits-harness-pawelhuryn, himanshustwts-claude-code-memory-architecture, jehad-vault-claude]
related: [anthropic, llm-wiki, janus-prime-radiant-build, agent-memory, agent-harness, agent-skills, model-context-protocol, 2026-05-06-skills-stay-as-skills-not-plugins]
---

# Claude (Anthropic product family)

Umbrella entry for all of [[anthropic]]'s consumer / developer / agent-platform surfaces. Janus's working principle: keep these together because they share a model, a mental model, and a coherent design philosophy; splitting them into one-vendor-page-per-product would fragment cross-references without meaningful benefit. Sub-products are listed below; create separate vendor pages only if a sub-product becomes genuinely arms-length.

## Sub-products

| Surface | What it is | Janus use |
|---|---|---|
| **Claude API / models** | The LLM family itself. Available via API and Anthropic SDK. | Powers the maintenance of this wiki and most AI Office automation. |
| **Claude (web/desktop chat)** | Consumer chat UI. | General drafting, evaluation, ad-hoc analysis. |
| **Claude Code** | CLI / IDE coding agent for developers. | Active use across engineering. Subject of its own deep-dive sources: harness framing ([[claude-code-limits-harness-pawelhuryn]]), prompt caching lessons ([[claude-code-prompt-caching-lessons]]), memory architecture ([[himanshustwts-claude-code-memory-architecture]]). |
| **Claude Code routines** | Scheduled / event-driven Claude Code automations on Anthropic-hosted infrastructure. Research preview as of 2026-04-14. | Not yet adopted; candidate for Stage 1 evaluation when out of preview. See [[2026-04-14-claude-code-routines]]. |
| **Claude Managed Agents** | Composable APIs for cloud-hosted agents at scale; launched 2026-04-08. File-based memory in public beta from 2026-04-23. | Not yet evaluated; relevant against Janus's broader agent-platform decisions. See [[2026-04-08-claude-managed-agents-launch]] and [[agent-memory]]. |
| **Cowork mode** | Claude desktop tool for non-developer file/task automation; provides connectors (Linear, Notion, Fireflies, Slack, Monday, Figma, etc.) and a sandboxed Linux shell. | The interface Michael uses to maintain this wiki. Plugins (bundles of MCPs + skills + tools) are first-class. |
| **Claude in Chrome** | Browser-side agent for navigating web tasks. | Not yet evaluated for Janus workflows. |
| **Claude Code on the web** | Web-hosted Claude Code execution surface (the substrate that routines run on). | Indirectly used — backbone for routines. |

## Cross-cutting properties

- **Skills** are first-class across surfaces (Claude Code, Cowork). See [[agent-skills]]. Janus already operates the `ai-registry`, `ai-tool-evaluation`, and `standup` skills. AIO tooling stays as Claude skills, not Cowork plugins — see [[2026-05-06-skills-stay-as-skills-not-plugins]] for the decision.
- **Memory** is increasingly first-class — Managed Agents has file-based memory; Claude Code has a memory architecture (per [[himanshustwts-claude-code-memory-architecture]]). See [[agent-memory]].
- **MCP** is the ambient connector protocol across all surfaces. See [[model-context-protocol]].

## Posture

Anthropic is moving up the stack from model API → agent platform. The "decoupling the brain from the hands" framing in [[claude-managed-agents-scaling]] is the most explicit articulation of this. For Janus, this means evaluating Claude isn't just "model quality" anymore — it's the quality of the surrounding harness, memory, skills, and routines together.

## Watch for

- Convergence between Claude Code routines and Claude Managed Agents — at some point these may merge.
- Whether file-based agent memory becomes a portable Anthropic standard or stays Claude-only.
- Pricing rationalisation across surfaces (currently a mix of API consumption, Claude Code subscription tiers, and Managed Agents with its own model).
- Cowork plugin ecosystem maturity — important for Janus's wiki + skills setup.
