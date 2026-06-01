---
type: vendor
title: Obsidian
slug: obsidian
air_id: AIR-74
status: Sandbox
labels: [Functional, AI Policy, Technology]
departments: [ai-office]
url: https://linear.app/janusd/issue/AIR-74/obsidian
created: 2026-04-07
updated: 2026-05-12
captured_by: jehad-altoutou
audience: department
sensitivity: dept
sensitivity_confidence: 0.9
confidence: high
sources: [karpathy-llm-wiki]
related: [llm-wiki, janus-prime-radiant-build]
migrated_from: entities/vendors/obsidian.md
---
<!-- jb:air-vendor-callout -->
> Part of [[ai-registry|AI Registry]]


# Obsidian

> AI Registry entry [AIR-74](https://linear.app/janusd/issue/AIR-74/obsidian) — status **Sandbox** as of 2026-05-08. Departments: —.

**Category:** Knowledge Management
**Cost per User/Month:** Free (personal) / $50 (commercial)
**Departments:** AI Policy, Technology, Office of CEO, Marketing

## Overview

Local-first, Markdown-based KM and note-taking application. Originally evaluated as context backup for [[claude|Claude]] CoWork outputs; has become foundational layer of AI Office knowledge stack, heavy active use.

## Current Use at Janus Digital (AIO 8 May 2026 standup)

* **Jehad's personal vault** — running since day one. Captures skills, projects (SSFI, BrightBean, Graphify), tech stack, design system, AI Office brain. Personal source-of-truth feeding downstream tooling.
* **Michael's Prime Radiant LLM Wiki prototype** — Obsidian is the read interface, CLAUDE.md as meta-skill brain. Actively iterating.
* **Web Clipper** adopted for external knowledge ingestion.
* **Forward plan:** roll out across departments via personal → department → CEO vault hierarchy. Variants planned for Andrew (Marketing) and Bonaventure (CEO master view), with cron-driven distillation between layers.

## Strengths

* Local-first (no cloud dependency)
* Markdown-native
* Extensible via plugins
* Strong community
* Excellent fit as read-layer for Prime Radiant LLM wiki

## Considerations

* Standalone tool — no native multi-user collaboration
* Hierarchy/sync between personal/dept/CEO vaults needs custom distillation pipeline (cron + LLM)
* Provisioning narrative owned by IT (Andre / Euclid)

## Cross-references

* Prime Radiant (LLM Wiki) — Obsidian is the chosen read interface
* Notion — complementary; Obsidian is local Markdown layer, Notion remains collaborative database

*Status note (8 May 2026): Promoted from Evaluating → Sandbox reflecting heavy active use across AI Office.*

## Merged from `entities/vendors/obsidian.md`

# Obsidian

Local-first markdown editor and notes app. Operates over a folder of plain `.md` files; supports double-bracket wikilink syntax for cross-page references, YAML frontmatter, a graph view, and a plugin ecosystem (Dataview, Web Clipper, etc.).

## Use in this wiki

The browsing/editing interface for the [[llm-wiki]]. Per Karpathy's framing: Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.

Relevant Obsidian features for this setup:
- **Web Clipper** — Karpathy's recommended ingest path for articles; will replace Mivory once configured.
- **Graph view** — visualises wiki shape; surfaces hubs and orphans during lint.
- **Dataview** — queries YAML frontmatter to render filtered tables (e.g., "all vendors with `confidence: high` in `departments: ai-office`").

## Merged from `entities/vendors/obsidian.md`

# Obsidian

Local-first markdown editor and notes app. Operates over a folder of plain `.md` files; supports double-bracket wikilink syntax for cross-page references, YAML frontmatter, a graph view, and a plugin ecosystem (Dataview, Web Clipper, etc.).

## Use in this wiki

The browsing/editing interface for the [[llm-wiki]]. Per Karpathy's framing: Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.

Relevant Obsidian features for this setup:
- **Web Clipper** — Karpathy's recommended ingest path for articles; will replace Mivory once configured.
- **Graph view** — visualises wiki shape; surfaces hubs and orphans during lint.
- **Dataview** — queries YAML frontmatter to render filtered tables (e.g., "all vendors with `confidence: high` in `departments: ai-office`").
