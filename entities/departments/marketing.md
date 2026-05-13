---
type: department
title: Marketing
slug: marketing
created: 2026-05-08
updated: 2026-05-11
departments: [marketing]
status: active
owner: andrew-soane
related: [andrew-soane, marketing-prime-radiant, janus-prime-radiant-build, peer-to-peer-mesh-federation-pattern, 2026-05-07-llm-wiki-extends-to-marketing-domain, 2026-05-08-marketing-prime-radiant-as-separate-vault]
---

# Marketing

Janus's marketing department, led by [[andrew-soane]] (CMO). Responsible for positioning, demand generation, employer brand (LinkedIn, Twitter, Instagram, TikTok for HR brand), and external POV across Janus's verticals (real estate, real assets, built environments, asset management, sustainability, private equity, credits).

## People

- **[[andrew-soane]]** — CMO; joined ~four weeks ago (as of 2026-05-08).
- Team scope: deliberately small — Andrew's hypothesis is that an AI-first marketing function compresses operational headcount, so the team is built for strategic depth rather than execution volume. Validation in progress.

## Prime Radiant instance

**Janus Prime Radiant · Marketing** — live as of 2026-05-11 (CLAUDE.md §1 adapted; founding decisions captured; second live Prime Radiant after AIO). See [[marketing-prime-radiant]] for the build project hub. **Vault topology** ([[2026-05-08-marketing-prime-radiant-as-separate-vault]]): the Marketing instance has its own Google Shared Drive folder + its own `CLAUDE.md` derived from the AIO one — not a sub-section of the AIO vault. This sets the federation precedent for HR / ISO / Finance / IT-Ops / Office-of-CEO / Engineering / Training instances.

## Mesh subfolder (AIO × Marketing pairing)

Pairing-specific content lives in `entities/departments/marketing/` (sibling to this file) per [[peer-to-peer-mesh-federation-pattern]]. From the Marketing vault, the same content appears at `entities/departments/ai-office/`. The AIO×Marketing pairing is the **first practical test** of the mesh pattern, set up 2026-05-11 — see `entities/departments/marketing/README.md` and the rolling [[2026-05-11-aio-x-marketing-pairing-notes|pairing notes]] for what lives there and what doesn't.

**Drive-shortcut consolidation pending** — currently two independent folders awaiting Michael's UI op to point them at the same canonical Drive folder.

## Infrastructure layer (per three-layer model)

Required to be made explicit before Outputs can be generated reliably:
- **Ideal Customer Profile (ICP)** — types of companies Janus targets.
- **Target buyer Personas** — CFO, COO, sustainability leads, PE / asset management decision-makers.
- **Mission + multi-year strategy** (sourced from [[bonaventure-wong]] / [[office-of-ceo]]).
- **Country plans** — SGP (W19 launch), GB (W20 launch), expansion targets.
- **Topic taxonomy** — sustainability regulation, AI in real estate, asset management trends, finance verticals.

These documents are pending — the Marketing instance can stand up its Signals layer immediately (Fireflies, Slack, news scraping) but Outputs (briefs, positioning docs, white papers) depend on the Infrastructure being captured first.

## Key projects

[[marketing-prime-radiant]] · [[singapore-news-monitoring]] (originated from a 2026-05-06 Bonaventure / Andrew session; now folded into Marketing PR scope) · [[crm-evaluation-and-selection]] (CRM is upstream blocker for the Signals layer)

## Cross-instance federation

The Marketing instance will federate with [[ai-office]] (vendor evaluations matter for marketing tools), [[office-of-ceo]] (mission and strategy live there), and [[hr]] (employer brand spans both).
