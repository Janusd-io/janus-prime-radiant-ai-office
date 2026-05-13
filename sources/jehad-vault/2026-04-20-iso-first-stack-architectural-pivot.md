---
type: decision
title: ISO-First Stack Architectural Pivot — CEO Executive Management System Reframe
slug: 2026-04-20-iso-first-stack-architectural-pivot
created: 2026-05-06
updated: 2026-05-13
status: resolved
owner: michael-bruck
departments: [ai-office, office-of-ceo]
countries: [sg, gb, us]
confidence: high
sources: [jehad-vault-import-2026-05-13]
related: [iso-compliance-programme, simon-tarskih, michael-bruck, bonaventure-wong]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/2026-04-20-iso-first-stack-architectural-pivot.md` — this file is preserved as a source for divergent framing / additional context._

# Decision: ISO-First Stack Architectural Pivot

**Date:** 20 April 2026. **Owner:** [[michael-bruck]]. **Status:** resolved. **Confidence:** high.

## What

Bonaventure reordered the CEO Executive Management System project. Primary deliverable is no longer the weekly CEO meeting and executive dashboard. It is the **ISO-driven workflow and automation foundation across all twelve functions**, with the management system as a natural byproduct.

## Options considered

1. **Original (v2):** OKR-driven, top-down. CEO meeting → strategic initiatives → quarterly objectives → weekly status. Executive dashboard is the primary outcome.
2. **ISO-first (chosen):** Task-based, bottom-up. Simon defines ISO standards → departments document workflows → AI identifies automation gaps → agents orchestrate cross-workflows → real-time continuous compliance. Executive visibility is the byproduct.

## Why

1. Task-based framing resonates more than OKR hierarchy. [[bonaventure-wong]]: *"I'm more on task right now on the project level. Seeing where everyone is right now, that's really it."*
2. ISO compliance is now the gating constraint. [[simon-tarskih]] in motion on ISO 9001 + 27001 + 42001. Every automation must sit on documented, signed-off workflows.
3. Real-time compliance is a strategic commercial play — the "Janus standard" sellable back to the industry.
4. Standardisation unlocks automation: *"You can't automate what isn't standardised — Simon's work unblocks the AI Office's work."*

## Impact on design

- Phase 1 is no longer "stand up the CEO Monday meeting." Phase 1 is "work with Simon to define ISO standards, then per-department workflow documentation with agent assist, then automation identification, then rollup visibility."
- Every department is Layer 1 simultaneously. Not top-down rollout from CEO. Parallel workflows per department; CEO aggregation emerges naturally.
- Tooling decision becomes a precondition: Notion alone, Monday alone, or two-tool (Monday ops SoR + Notion docs layer).
- [[simon-tarskih]] is critical path for ~1 week (ISO scope, standards selection, workflow-documentation tool preference).

## Related decisions

- 2026-04-22 — Notion + Markdown confirmed as ISO repository format (Simon meeting outcome).
- 2026-04-20 — Tooling analysis kicked off: Notion vs Monday (dependent on this reframe).
- 2026-04-23 — Tool-purchase approval workflow identified as first cross-department pilot for ISO-based automation.

## Key quote

*"Don't worry about me at this time. Worry about applying this for everyone to see what you've done. That's where I'm trying to get."* — [[bonaventure-wong]], 20 Apr 2026.
