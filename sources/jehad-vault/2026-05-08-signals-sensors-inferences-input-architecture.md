---
type: lesson
title: Signals → sensors → inferences — design the input array, the AI does the rest
slug: 2026-05-08-signals-sensors-inferences-input-architecture
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
status: active
owner: michael-bruck
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [andrew-soane, prime-radiant-three-layer-architecture, janus-prime-radiant-build, agentic-ai]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `lessons/2026-05-08-signals-sensors-inferences-input-architecture.md` — this file is preserved as a source for divergent framing / additional context._

# Signals → sensors → inferences

## What happened

In the 2026-05-08 brainstorm with Andrew Soane, a real concern surfaced: would a Marketing Prime Radiant, fed only by *internal* signals, be smart enough to recognise an externally-relevant pattern that hadn't been internally discussed yet? Michael's reframe: if you identify the signals you need to collect — think of them as sensors — the AI will find the patterns.

## The lesson

**You cannot design a Prime Radiant for the questions you can predict. You can only design the sensor array — and let the AI find the patterns. Pre-specifying outputs is the failure mode; under-specifying inputs is the second failure mode.**

The shift in framing:
- *Old framing:* "What insights do we want the system to surface?" → leads to top-down design, narrow data, brittle outputs.
- *New framing:* "What signals do we need to capture? What strategic anchors define relevance?" → leads to dense sensor array + clear infrastructure layer → emergent insights.

This maps directly onto the [[prime-radiant-three-layer-architecture]]: Signals (raw inputs) + Infrastructure (the lens that defines relevance) → Outputs (inferences and synthesis emerge).

## The two complementary disciplines

1. **Throw the net wide on Signals.** Include voice/video transcripts, Slack, system-of-record exports, web inbound, emails, articles, news, competitor intel, industry analyst pieces. Don't pre-filter for relevance at the sensor layer.
2. **Be precise on Infrastructure.** Document the strategic anchors (mission, ICP, Personas, country plans, topic taxonomy). The Infrastructure layer tells the system *what relevance looks like*.

## Why this matters for instance design

Every department instance build sequence: **identify Signals → curate Infrastructure → let Outputs emerge.** Outputs cannot be designed top-down. This is why the AIO instance got good fast — its Infrastructure layer was implicit in CLAUDE.md and the SoR map; Signals lit up immediately on Web Clipper / Notion / Linear feeds; Outputs emerged after enough signal accumulated.

## Cross-cutting application

When standing up HR, Finance, IT-Ops, Office-of-CEO, Engineering, or Training instances:
1. What sensors does this department already have or need?
2. What strategic documents define what's relevant for this department?
3. Stand up the Signals; document the Infrastructure; let Outputs emerge.
