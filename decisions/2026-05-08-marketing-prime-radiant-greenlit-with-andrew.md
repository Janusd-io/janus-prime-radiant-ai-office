---
type: decision
title: Marketing Prime Radiant greenlit with Andrew
slug: 2026-05-08-marketing-prime-radiant-greenlit-with-andrew
created: 2026-05-08
updated: 2026-05-08
departments: [marketing, ai-office]
status: resolved
owner: michael-bruck
sources: [2026-05-08-andrew-marketing-prime-radiant]
related: [andrew-soane, marketing, marketing-prime-radiant, janus-prime-radiant-build, 2026-05-07-llm-wiki-extends-to-marketing-domain, 2026-05-08-marketing-prime-radiant-as-separate-vault, llm-wiki]
---

# Marketing Prime Radiant greenlit with Andrew

## Decision

Build a Marketing-domain Prime Radiant instance for [[andrew-soane]] (CMO), starting now (2026-05-08), running in parallel with continued AIO Prime Radiant honing. Project hub: [[marketing-prime-radiant]].

## Context

The AIO Prime Radiant prototype was validated 2026-05-07 ([[2026-05-07-llm-wiki-validates-capture-everything|that lesson]]). The 2026-05-07 standup ([[2026-05-07-llm-wiki-extends-to-marketing-domain|see decision]]) anticipated extending the pattern to a marketing-domain instance. On 2026-05-08, Michael walked Andrew through the live AIO Prime Radiant in a working session ([[2026-05-08-andrew-marketing-prime-radiant|raw transcript]]). Andrew's response was unambiguous: yes, build one for me; "if we can have that next Tuesday, that'll be great."

## Options considered

1. **Do nothing** — continue AIO instance honing; defer Marketing instance until AIO is "fully baked." *Rejected* because it implies the AIO instance has a "done" state, which it doesn't (institutional KBs compound continuously). Also forfeits Andrew's engaged-stakeholder energy at a high-leverage moment.

2. **Build full Marketing instance up front** — wait for CRM selection, ICP / Personas / country plans documented, full Signals array online, then ship a complete v1 to Andrew. *Rejected* because it inverts the validated build pattern. The AIO instance succeeded by going live early and letting the schema evolve under load (CLAUDE.md is on its 8th version in 4 days). Trying to design Marketing top-down before letting it run misses the lesson of how the AIO instance actually got good.

3. **Karpathy-gist incremental build with Andrew as engaged stakeholder** — start the instance now with Signals that are immediately available (Fireflies, Slack, curated articles), have Andrew sketch the Infrastructure documents (ICP / Personas / etc.), iterate as inputs come online, let Outputs emerge as Infrastructure firms up. *Selected.* This is how the AIO instance was built and how Karpathy advocates for the LLM Wiki pattern — the gist is a starting point, not a recipe.

## Why this option

- Pattern-matches the validated AIO build sequence (start small, run, iterate under load).
- Captures Andrew's engagement now while it's high — he committed to drawing up an inputs/outputs sketch in the same session.
- The CLAUDE.md v0.8 schema (formalised three-layer architecture, `entities/departments/` federation type) was authored *because* of the Marketing brainstorm — using it for Marketing immediately validates whether the abstractions held up.
- Running the second instance reveals what's truly portable in the schema vs what was AIO-specific; that learning compounds into every subsequent department instance (HR, Finance, IT-Ops, etc.).
- AIO instance honing continues in parallel — kicking off Marketing does not freeze AIO development.

## Constraints + commitments

- **Andrew's "next Tuesday"** is aspirational, not committed. Realistic v0 is a working frame Andrew can react to (Signals partly online, Infrastructure stub-documented), not a fully-instrumented system.
- **CRM selection is the gating dependency for Signals richness** — without a CRM, the Marketing instance is missing one of its highest-value sensor channels. Bonaventure-driven CRM benchmark expansion (Monday, Salesforce, HubSpot, Attio, Zoho on watch) is the upstream blocker.
- **Andrew's hypothesis that AI-first marketing compresses a 10-person team to 2-3 strategic operators** is captured but not endorsed as a Janus claim. Frame as a hypothesis to validate, not a result to repeat outward (per the no-unverified-demand-claims rule).
- **Vault topology** (separate Drive folder vs sub-section of AIO vault) — *resolved later the same day*: separate vault from the start. See follow-up decision [[2026-05-08-marketing-prime-radiant-as-separate-vault]]. The "v0 as sub-section for speed" provisional default is superseded — the federation discipline did demand its own vault.

## Implications

- The Marketing instance becomes the second live Prime Radiant. Federation mechanisms (currently lightweight — `entities/departments/` stubs in each instance) get their first real cross-vault test.
- HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instance kickoffs are now sequenced behind the Marketing pilot, not behind AIO maturity.
- The `projects/janus-prime-radiant-build` program hub now has a second concrete dependent (was: AIO instance only; now: AIO instance + Marketing instance).
- Andrew is now a documented, engaged stakeholder for the rollout — the validation-by-second-adopter signal is in.

## Owner

[[michael-bruck]] for build phase. Hand-off owner to [[andrew-soane]] once the Marketing instance is operational and Andrew is curating it.
