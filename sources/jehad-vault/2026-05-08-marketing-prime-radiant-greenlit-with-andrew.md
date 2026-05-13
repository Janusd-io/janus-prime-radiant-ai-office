---
type: decision
title: Marketing Prime Radiant greenlit with Andrew
slug: 2026-05-08-marketing-prime-radiant-greenlit-with-andrew
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
status: resolved
owner: michael-bruck
sources: [jehad-vault-import-2026-05-13]
related: [andrew-soane, prime-radiant-marketing-rollout, janus-prime-radiant, llm-wiki]
captured_by: jehad-altoutou
---

> _Jehad's personal-vault articulation of this topic, imported 2026-05-13. The canonical wiki page is at `decisions/2026-05-08-marketing-prime-radiant-greenlit-with-andrew.md` — this file is preserved as a source for divergent framing / additional context._

# Marketing Prime Radiant greenlit with Andrew

## Decision

Build a Marketing-domain Prime Radiant instance for [[andrew-soane]] (CMO), starting now (2026-05-08), running in parallel with continued AIO Prime Radiant honing. Project hub: [[prime-radiant-marketing-rollout]].

## Context

The AIO Prime Radiant prototype was validated 2026-05-07. The 2026-05-07 standup anticipated extending the pattern to a marketing-domain instance. On 2026-05-08, Michael walked Andrew through the live AIO Prime Radiant in a working session. Andrew's response was unambiguous: yes, build one for me; "if we can have that next Tuesday, that'll be great."

## Options considered

1. **Do nothing** — continue AIO instance honing; defer Marketing instance until AIO is "fully baked." *Rejected* because it implies the AIO instance has a "done" state, which it doesn't (institutional KBs compound continuously). Also forfeits Andrew's engaged-stakeholder energy at a high-leverage moment.

2. **Build full Marketing instance up front** — wait for CRM selection, ICP / Personas / country plans documented, full Signals array online, then ship a complete v1 to Andrew. *Rejected* because it inverts the validated build pattern. The AIO instance succeeded by going live early and letting the schema evolve under load (CLAUDE.md is on its 8th version in 4 days).

3. **Karpathy-gist incremental build with Andrew as engaged stakeholder** — start the instance now with Signals that are immediately available (Fireflies, Slack, curated articles), have Andrew sketch the Infrastructure documents (ICP / Personas / etc.), iterate as inputs come online, let Outputs emerge as Infrastructure firms up. *Selected.*

## Why this option

- Pattern-matches the validated AIO build sequence (start small, run, iterate under load).
- Captures Andrew's engagement now while it's high — he committed to drawing up an inputs/outputs sketch in the same session.
- The CLAUDE.md v0.8 schema (formalised three-layer architecture, `entities/departments/` federation type) was authored *because* of the Marketing brainstorm — using it for Marketing immediately validates whether the abstractions held up.
- Running the second instance reveals what's truly portable in the schema vs what was AIO-specific.
- AIO instance honing continues in parallel — kicking off Marketing does not freeze AIO development.

## Constraints + commitments

- **Andrew's "next Tuesday"** is aspirational, not committed. Realistic v0 is a working frame Andrew can react to.
- **CRM selection is the gating dependency for Signals richness** — without a CRM, the Marketing instance is missing one of its highest-value sensor channels.
- **Andrew's hypothesis that AI-first marketing compresses a 10-person team to 2-3 strategic operators** is captured but not endorsed as a Janus claim. Frame as a hypothesis to validate.
- **Vault topology** — resolved later the same day: separate vault from the start.

## Implications

- The Marketing instance becomes the second live Prime Radiant. Federation mechanisms get their first real cross-vault test.
- HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instance kickoffs are now sequenced behind the Marketing pilot.
- Andrew is now a documented, engaged stakeholder for the rollout — validation-by-second-adopter signal is in.

## Owner

[[michael-bruck]] for build phase. Hand-off owner to [[andrew-soane]] once the Marketing instance is operational and Andrew is curating it.
