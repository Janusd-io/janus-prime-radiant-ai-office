---
type: lesson
title: HTML, not PowerPoint, for read-only content — the cost / editability case
slug: 2026-05-11-html-over-powerpoint-for-read-only-content
created: 2026-05-11
updated: 2026-05-12
departments: [ai-office, training]
status: active
sources: [2026-05-11-aio-standup-with-jehad, 2026-05-12-bonaventure-ai-native-call]
related: [michael-bruck, jehad-altoutou, simon-tarskih, bonaventure-wong, 2026-05-11-notebooklm-retirement-html-over-image-outputs, marp, 2026-05-12-html-as-presentation-format-adopted]
---

# HTML, not PowerPoint, for read-only content — the cost / editability case

## What we learned

When [[claude]] produces *read-only* content (presentations, org charts, summaries, reports that won't be edited downstream), reaching for PowerPoint by habit is the wrong default. **HTML is the right default.** Two reasons surfaced concretely in the 11 May 2026 AIO standup:

### 1. Token cost

[[simon-tarskih|Simon]] has been "burning through tokens with a frightening rate" by asking Claude to produce PowerPoints when nearly all of his presentation material is output-only — written once, read many times, never edited. PowerPoint generation through Claude uses substantially more tokens than HTML generation for the same content because the underlying tool-call surface (XML schemas, layout primitives, shape placement) is heavier than emitting markup.

Framing surfaced in the meeting: *"Anthropic are very happy because it uses up a lot of tokens. So for them, it's very good. But [PowerPoint and Word] are not the most efficient surfaces to write to."*

### 2. Editability and downstream value

HTML supports interactivity (a clickable org chart is just `<a>` tags), prints cleanly to PDF when a static artefact is required, plays nicely with the wiki's Markdown / Git discipline, and can be version-controlled meaningfully. PowerPoint, especially when AI-generated, often arrives as image-heavy slides that can't be edited; even when it doesn't, the editing surface is hostile to the version-control workflow this AIO has standardised on.

The aha from the meeting: *"Why are we creating a PowerPoint every time when it's read-only? You can always print an HTML into PDF if you need."*

## Why this is non-obvious

People reach for PowerPoint by habit. The presentation format dominates because it's been the corporate standard for thirty years. The token economics of AI-generated presentations are invisible at the moment of asking — the user sees the artefact, not the bill. And there's a quality association — PowerPoint *feels* polished.

The actual quality result is worse, not better:

- AI-generated PowerPoints often end up as image-heavy slides that are uneditable (the [[2026-05-11-notebooklm-retirement-html-over-image-outputs|NotebookLM case]] is the extreme).
- The "polished" feel is template-driven; HTML can match or exceed it with proper styling.
- Interactivity (filtering, sorting, drill-down) is trivial in HTML and impossible in PowerPoint.

## Operational guidance

Default reach for **HTML**, not PowerPoint, when:

- Content is read-only (no downstream editing expected).
- The artefact lives on-screen or in a browser (org charts, dashboards, references).
- Print-to-PDF is acceptable when a static version is needed.
- Interactivity would add value (search, expand/collapse, filter, link).

Continue reaching for **PowerPoint / [[marp]]** when:

- Live presentation is the primary delivery mode (a deck someone will click through in a meeting).
- The audience expects a deck format specifically.
- Marp Markdown-driven slide generation is a third path that bridges the two — keep on the watch list.

## Training implication

This is the kind of best practice that needs to land with operators across Janus when the [[training]]-department instance and the broader AI-tooling onboarding rolls out. The default tooling choice is a learned habit; AI capability changes which defaults make sense.

## Related supporting signal

Per a reading of an X post by Tariq Hassanaeen (Claude Code team) raised in the meeting, Anthropic is increasingly framing HTML as a presentation-of-information surface for AI outputs, not just as storage. The "unreasonable effectiveness of HTML" framing is worth a closer source ingest when the article is captured — search `inbox/` and `sources/articles/` for next batch. Cross-check against the [[anatomy-of-claude-folder|Anatomy of the .claude folder]] source which makes a related point about HTML as the read surface.

## CEO endorsement (2026-05-12)

Bonaventure approved the HTML direction on the 12 May AI Native CEO call after seeing Michael's HTML briefing and the HTML deck for [[andrew-soane|Andrew]]'s onboarding. His response: *"That's fine. People have a problem with it. They're such a visual species... so as long as you can toddle in and out, they don't care how it's delivered."* And on the dynamic upside: *"You can have dynamic website if you know how to do it right, which is this."*

The lesson is now CEO-endorsed and codified as a decision: [[2026-05-12-html-as-presentation-format-adopted]]. Janus AIO outputs are HTML-by-default; PowerPoint is the exception, not the rule.

## Related

[[2026-05-11-notebooklm-retirement-html-over-image-outputs]] · [[2026-05-12-html-as-presentation-format-adopted]] · [[marp]]
