---
type: decision
title: Retire NotebookLM for org-chart / presentation outputs — HTML over image-based PowerPoint
slug: 2026-05-11-notebooklm-retirement-html-over-image-outputs
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [2026-05-11-aio-standup-with-jehad]
related: [michael-bruck, jehad-altoutou, bonaventure-wong, 2026-05-11-html-over-powerpoint-for-read-only-content]
---

# Retire NotebookLM for org-chart / presentation outputs — HTML over image-based PowerPoint

## Context

[[notebooklm]] was used in Janus's early days — [[bonaventure-wong|Bonaventure]] championed it heavily for podcasts, videos, and presentations when the company was three people; he pushed Michael to use it more often. It produced engaging outputs (auto-generated podcast-style summaries, AI-narrated videos) that played well for an early-stage demo audience.

By 2026-05-11 the limitations have become operationally painful. NotebookLM's "PowerPoint" output is **image-based** rather than text-based: each slide is rendered as a flat image rather than as editable shapes and text. The consequences:

- Slides cannot be edited downstream — fixing a typo or updating a number requires regenerating the whole deck.
- Slides are not version-controllable in any meaningful way.
- The output cannot feed into the Markdown / HTML pipeline the AIO has standardised on.
- The tokens spent producing the image-based deck are disproportionate to the value (a separate issue tracked in [[2026-05-11-html-over-powerpoint-for-read-only-content]]).

The trigger for revisiting was a specific case where an org chart needed updating and the NotebookLM-generated deck was a dead end.

## Decision

Retire NotebookLM as a Janus output format. For all read-only outputs that previously went to NotebookLM (org charts, summaries, presentations), use **HTML** instead. HTML is editable, version-controllable, browser-native, supports interactivity when needed, and can be printed to PDF at any point if a static artefact is required.

The decision applies prospectively. Existing NotebookLM-generated artefacts can be migrated lazily — if someone needs to update one, regenerate as HTML at that point.

## Why HTML

- **Editable.** A diff on an HTML file is meaningful; a diff on an image-based PowerPoint is not.
- **Version-controllable.** Plays cleanly with GitHub, with the wiki's Markdown discipline, and with the [[janus-prime-radiant-build|Prime Radiant]] file substrate generally.
- **Interactive where needed.** An HTML org chart can be a clickable tree; a static PowerPoint cannot.
- **Cheap to produce.** Per [[2026-05-11-html-over-powerpoint-for-read-only-content]], HTML output uses substantially fewer tokens than PowerPoint output.
- **Printable.** HTML → PDF is a one-line operation when a static artefact is required.

## Stakeholder context — Bonaventure

This is a tool-stack change against a tool [[bonaventure-wong|Bonaventure]] previously championed. The retirement is on the merits of the output format (image vs. editable), not a rejection of Bonaventure's earlier advocacy — in 2024-2025 the NotebookLM podcast format was genuinely novel and demo-effective. The 2026 context is different: Janus produces operational artefacts that need to be edited, federated, and version-controlled, and image-based outputs no longer fit.

## Out of scope

- This decision does not say anything about NotebookLM as an *input-side* AI tool (e.g., chatting against a corpus). The output format is the issue.
- Sibling tools that produce image-based outputs (similar AI presentation generators) inherit the same caution. Treat the format, not the brand, as the deciding factor.

## Cross-references

Sibling lesson: [[2026-05-11-html-over-powerpoint-for-read-only-content]] — the broader principle that read-only content should be HTML, not PowerPoint, regardless of which AI tool produces it.
