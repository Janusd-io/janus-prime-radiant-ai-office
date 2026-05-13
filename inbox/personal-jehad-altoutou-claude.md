---
type: vendor
title: Claude (Anthropic product family)
slug: claude
created: 2026-05-13
updated: 2026-05-13
departments: [ai-office, engineering]
status: active
confidence: high
sources: [pr-backup-claude]
related: [anthropic-claude]
audience: [department]
captured_by: jehad-altoutou
---

# Claude (Anthropic product family)

Umbrella entry for all of Anthropic's consumer / developer / agent-platform surfaces. Working principle: keep these together because they share a model, a mental model, and a coherent design philosophy; splitting per-product would fragment cross-references without meaningful benefit. Sub-products are listed below; create separate vendor pages only if a sub-product becomes genuinely arms-length.

Note: this vault also has `anthropic-claude.md` (stub from 2026-05-06 meeting). Flagged as dedup risk — the umbrella page (this one) is the broader canonical surface; the existing `anthropic-claude.md` may be retitled or merged.

## Sub-products

| Surface | What it is | Janus use |
|---|---|---|
| **Claude API / models** | The LLM family itself. Available via API and Anthropic SDK. | Powers wiki maintenance and most AIO automation. |
| **Claude (web/desktop chat)** | Consumer chat UI. | General drafting, evaluation, ad-hoc analysis. |
| **Claude Code** | CLI / IDE coding agent for developers. | Active use across engineering. |
| **Claude Code routines** | Scheduled / event-driven Claude Code automations on Anthropic infra. Research preview as of 2026-04-14. | Not yet adopted; Stage 1 candidate when out of preview. |
| **Claude Managed Agents** | Composable APIs for cloud-hosted agents at scale; launched 2026-04-08. File-based memory in public beta from 2026-04-23. | Not yet evaluated. |
| **Cowork mode** | Desktop tool for non-developer file/task automation; provides connectors (Linear, Notion, Fireflies, Slack, Monday, Figma) and a sandboxed Linux shell. | Interface used to maintain this wiki. Plugins (bundles of MCPs + skills + tools) first-class. |
| **Claude in Chrome** | Browser-side agent for navigating web tasks. | Not yet evaluated. |
| **Claude Code on the web** | Web-hosted Claude Code execution surface (substrate routines run on). | Indirectly used — backbone for routines. |

## Cross-cutting properties

- **Skills** are first-class across surfaces (Claude Code, Cowork). Janus operates `ai-registry`, `ai-tool-evaluation`, `standup` skills.
- **Memory** is increasingly first-class — Managed Agents has file-based memory; Claude Code has a memory architecture.
- **MCP** is the ambient connector protocol across all surfaces.

## Posture

Anthropic is moving up the stack from model API → agent platform. The "decoupling the brain from the hands" framing in claude-managed-agents-scaling is the most explicit articulation. Evaluating Claude isn't just "model quality" anymore — it's the quality of harness + memory + skills + routines together.

## Watch for

- Convergence between Claude Code routines and Claude Managed Agents.
- Whether file-based agent memory becomes a portable Anthropic standard or stays Claude-only.
- Pricing rationalisation across surfaces.
- Cowork plugin ecosystem maturity.
