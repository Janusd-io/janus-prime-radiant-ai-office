---
type: vendor
title: Marp
slug: marp
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, marketing]
status: active
confidence: high
sources: [karpathy-llm-wiki, marp-homepage]
related: [obsidian]
migrated_from: entities/vendors/marp.md
---
# Marp

Open-source Markdown Presentation Ecosystem. Lets you write slide decks in plain markdown and render them to HTML, PDF, or PowerPoint. Tooling includes a CLI (`marp-cli`) and a VS Code extension.

## Why it's relevant

Karpathy mentioned Marp in the [[llm-wiki]] gist as the path he uses to generate slide decks from wiki content. Same insight applies here: anything we synthesise into a brief or a status page can be rendered as a deck without a parallel deck-authoring workflow. Markdown stays canonical; slides become a view.

## Janus relevance

Speculative until adopted. Plausible uses:
- Auto-generating quarterly recap decks from `briefs/`.
- Letting AI Office produce stakeholder updates from `pulse/` entries.
- Reducing the slide-authoring tax for teams that already write in markdown.

Reconsider as a Stage 1 candidate in the [[ai-tool-evaluation]] framework if marketing or any operational team starts hitting the slide-production-volume threshold.

## Watch for

- Whether the VS Code extension matures into a usable presenter mode (replacing the need for Keynote/PowerPoint review passes).
- Rendering fidelity vs. native slide tools — currently good for engineering decks, less polished for sales/marketing surfaces.
