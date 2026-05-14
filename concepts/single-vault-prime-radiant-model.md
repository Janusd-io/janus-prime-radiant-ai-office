---
type: concept
title: Single-vault Prime Radiant model (2026-05-14 rewrite)
slug: single-vault-prime-radiant-model
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
captured_by: jehad-altoutou
sources: [personal-claude-md, personal-prime-radiant-proposal]
related: [janus-prime-radiant-build, janus-prime-radiant, janus-brain-bootstrap]
audience: [department]
---

# Single-vault Prime Radiant model

As of 2026-05-14, the Prime Radiant rolls out as **one shared GitHub repo per department** (`Janusd-io/janus-prime-radiant-<dept>`), with each employee living in a `people/<slug>/` subtree inside that repo rather than running their own separate Personal Prime Radiant vault. This is a rewrite of the earlier two-vault model proposed in `[[personal-prime-radiant-proposal]]` (2026-05-11), where each employee would have run a private vault that federates upward.

The shift fixes three pain points the two-vault model surfaced once it hit a real laptop:

- **Federation duplication.** Two-vault meant every personal page had to be syncrhonised to a separate dept vault — twice the writes, twice the conflict surface.
- **Discovery cost.** Teammates couldn't see each other's work-in-progress without explicit federation passes.
- **Onboarding friction.** New employees had to clone two repos and learn two CLAUDE.md files.

Under the single-vault model, everything is one repo. Privacy is enforced by a `people/<slug>/private/` folder that is **gitignored**; the enrichment subagent classifies sensitivity (`dept | self | confidential`) per source and routes private items there. Items below 0.7 classification confidence get logged to `.review-queue.md` for the employee to confirm before they ship.

## Why this matters

The single-vault model is what makes Prime Radiant cheap enough to roll to every department — one repo, one Obsidian Git plugin, transparent ongoing sync — instead of requiring custom federation tooling per employee.

## Open questions

- Cross-departmental audience conflicts (meeting with HR + Finance where Finance wants narrower distribution) — not yet specified.
- Personal data retention when someone leaves Janus — open.
- Auto-detecting false-negative sensitivity classifications — open.
