---
type: vendor
title: Google Stitch
slug: google-stitch
air_id: AIR-91
status: Backlog
labels: [Functional, Technology]
departments: []
url: https://linear.app/janusd/issue/AIR-91/google-stitch
created: 2026-05-04
updated: 2026-05-11
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
---

# Google Stitch

> AI Registry entry [AIR-91](https://linear.app/janusd/issue/AIR-91/google-stitch) — status **Backlog** as of 2026-05-11. Departments: —.

**Category:** AI UI Design Canvas (design-to-code, "vibe design") — adjacent to chat-to-app cohort
**Status:** Backlog
**Cost:** Free while in Google Labs. ~400 daily design credits, 15 redesign credits/day. Paid plans expected Q4 2026. Speculation: 30-50% below Figma.
**Departments:** Technology (primary), Marketing, Commercial

## Overview

Google Labs product. "AI-native software design canvas" — coined term "vibe design" (distinct from "vibe coding"). Released 2025, substantially relaunched 2026-03-18 with infinite-canvas UI, design agent, agent manager, voice interaction, **DESIGN.md** design-system format. Powered by Gemini. Upstream of chat-to-app cohort: produces high-fidelity interactive UI prototypes, bridges to dev tools (AI Studio, Antigravity, MCP IDEs) for code.

## Capabilities

* **Vibe design canvas** — natural-language → high-fidelity UI; infinite canvas; voice critique/edits
* **Design agent + agent manager** — parallel agents for divergent exploration
* **Interactive prototypes** — stitch screens, hit Play, walk real interactive flow
* **DESIGN.md** — open-source agent-friendly markdown format (open-sourced 2026-04-21)
* **MCP server + SDK + skills** — public skills library (`google-labs-code/stitch-skills`, ~2.4k stars)
* Code export to React; handoff to AI Studio + Antigravity
* **Voice mode** — speak to canvas

## Integrations

* Google account auth
* Gemini models
* AI Studio (AIR-8), Antigravity (AIR-34)
* MCP server for any MCP-compatible client (Cursor, Claude Code, Cline, VS Code)
* GitHub OSS
* DESIGN.md portability

## Security & Compliance

* **Google Labs experiment** — no dedicated trust portal or DPA
* Inherits Google policies — Workspace coverage of Stitch not yet confirmed
* Workspace SSO likely supported
* Data residency/training opt-out NOT separately documented

**Labs-stage product — biggest uncertainty in cohort; pace rollout carefully.**

## Different Category, Same Cohort

Stitch is design-stage, not app-stage. Other five (Hercules/Lovable/Bolt/v0/Replit) output deployable hosted apps. Stitch outputs prototype + code that needs downstream dev tool. **Complementary, not direct replacement.**

## Janus Strategic Position

Janus deep Google footprint (Workspace, Gemini, GCP, AI Studio, Gemini CLI, Antigravity, Firebase). Stitch slots as design-front end of Google-native build pipeline: Stitch → Antigravity/AI Studio → Firebase/GCP. For Marketing/Commercial inside Google identity perimeter — lowest-friction entry point in cohort. Zero incremental cost while in Labs.

*Backlog. Functional tier. Labs-stage adjacent product.*
