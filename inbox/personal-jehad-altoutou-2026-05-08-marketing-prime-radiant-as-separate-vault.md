---
type: decision
title: Marketing Prime Radiant — separate Drive vault + own CLAUDE.md
slug: 2026-05-08-marketing-prime-radiant-as-separate-vault
created: 2026-05-08
updated: 2026-05-13
departments: [marketing, ai-office]
status: resolved
owner: michael-bruck
confidence: high
sources: [pr-backup-2026-05-11-decision-marketing-pr-separate-vault]
related: [prime-radiant-marketing-rollout, janus-prime-radiant, marketing, andrew-soane, michael-bruck, llm-wiki, prime-radiant-three-layer-architecture, 2026-05-08-per-department-prime-radiant-instances]
audience: [department]
captured_by: jehad-altoutou
---

# Marketing Prime Radiant — separate Drive vault + own CLAUDE.md

## Decision

The Marketing Prime Radiant gets its **own Google Shared Drive folder** and its **own `CLAUDE.md`** derived from the AIO one. It is *not* a sub-section of the AIO vault. Scope is a full Marketing-department Prime Radiant — broader than the originating "Marketing PR project" framing in the greenlight decision. CRM selection remains a Signals-layer dependency but is not a blocker for design and architecture work, which can begin immediately.

## Context

The greenlight decision earlier today left the vault topology as an open question ("separate Drive folder vs sub-section of AIO vault"), with v0 likely starting as a sub-section "for speed." That provisional default is now overridden — Michael's call (same day) is **separate vault from the start**.

## Why separate vault

- **Scope is genuinely department-level, not project-level.** The Marketing instance will be a fully-fledged Prime Radiant for the Marketing department — campaigns, positioning, market intel, content briefs, customer/persona infrastructure, country-specific market analysis. Institutional knowledge base on equal footing with the AIO one.
- **Federation pattern is set by precedent.** Whatever shape the Marketing instance takes becomes the template for HR, Finance, IT-Ops, Office-of-CEO, Engineering, Training instances. Sub-section-of-AIO would set a federation pattern where every department instance lived under AIO custody — wrong shape for a digital-knowledge-twin architecture.
- **CLAUDE.md §1 Architecture subsection already anticipated this.** v0.8 schema (landed earlier today) explicitly states: *"Each Prime Radiant instance is its own vault (separate folder, separate `CLAUDE.md` derived from this one)."*
- **Department ownership** — [[andrew-soane]] (CMO) will eventually curate the Marketing instance; AIO custody of a Marketing sub-section would have produced a permission and ownership mess from week one.

## Why not wait for CRM

CRM selection is the gating dependency for **Signals layer richness** — without a CRM, the Marketing instance can't capture inbound web messages, lead flow, email threads tied to opportunities. But:

- Signals layer is partial-ready without CRM: Fireflies (Andrew's calls), Slack, curated articles via Web Clipper, news scraping per topic taxonomy — all of these can light up immediately.
- **Infrastructure layer design** is fully ready: ICP, Personas, mission framing, country plans, topic taxonomy can be documented now. The Marketing brainstorm with Andrew identified these as the explicit dependencies for Outputs.
- Vault setup, CLAUDE.md derivation, entity vocabulary design, federation linkage to AIO — all CRM-independent.

Waiting for CRM would forfeit post-brainstorm momentum with Andrew. Better to design and architect now; flow the CRM-dependent Signals when the CRM lands.

## What happens next (mechanics)

1. **New Google Shared Drive folder** created — naming convention TBD; suggested: *Janus Prime Radiant — Marketing*, parallel to *Janus Prime Radiant — AI Office*.
2. **CLAUDE.md derived** from the AIO v0.8 one. Schema discipline carries over verbatim; entity vocabulary adapted (e.g., `entities/outlets/` for media, `entities/clients/` more prominent, possibly `entities/campaigns/` and `entities/personas/`).
3. **Folder scaffolding** mirrors AIO: `inbox/`, `sources/{meetings,articles,linear,monday,slack,notion}/`, `entities/{vendors,clients,people,internal,departments}/` + Marketing-specific subfolders, `concepts/`, `processes/`, `projects/`, `decisions/`, `lessons/`, `questions/`, `pulse/`, `briefs/`.
4. **Seed pages**: Andrew's entity page (Marketing-instance perspective), departments stubs, an initial project hub for the Marketing instance build itself, the originating Andrew transcript filed as a source.
5. **Federation link from AIO**: the [[marketing]] department entity page in the AIO instance gets a note pointing at the canonical Marketing Prime Radiant once it exists.

## Implications

- The pattern is now established: **one Prime Radiant per department, each in its own Drive folder with its own derived CLAUDE.md.** HR, Finance, IT-Ops, Office-of-CEO, Engineering, Training to follow the same shape.
- The "company-wide digital knowledge twin" framing now has concrete federation mechanics: department vaults federate via `entities/departments/` cross-references and (later) skill-driven signal flow at the Outputs ↔ Signals boundary.
- CLAUDE.md derivation is now a recurring artifact pattern — each new instance starts from the AIO CLAUDE.md as a gist, adapts entity vocabulary, runs forward independently.
- AIO CLAUDE.md remains the canonical source for the schema discipline; updates to schema rules that should propagate need an explicit propagation step (manual for now; eventually skill-driven).

## Constraints

- Andrew is not yet set up to curate his own vault — build phase remains [[michael-bruck]]-owned; handover when operational.
- Cross-vault wikilink resolution doesn't work in Obsidian by default. Federation across vaults is initially manual.
- Schema drift risk: as AIO CLAUDE.md continues to evolve (on v0.8), the Marketing CLAUDE.md needs explicit re-synchronisation. Initial discipline: document any deliberate divergence in the Marketing CLAUDE.md status header.

## Open follow-ups

- New Drive folder creation (Michael action).
- Marketing CLAUDE.md authoring — first draft derives from AIO CLAUDE.md v0.8 with entity vocabulary swap.
- Marketing Infrastructure layer docs (ICP, Personas, mission, country plans, topic taxonomy) — Andrew dependency.
- Tier 3 brief on the Marketing PR strategic implication — held pending design refinement.

## Owner

[[michael-bruck]] for build phase. Handover to [[andrew-soane]] when the Marketing instance is operational and Andrew is curating.
