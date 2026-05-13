---
type: decision
title: Marketing Prime Radiant — separate Drive vault + own CLAUDE.md
slug: 2026-05-08-marketing-prime-radiant-as-separate-vault
created: 2026-05-08
updated: 2026-05-13
sources: [jehad-vault-2026-05-08-marketing-prime-radiant-as-separate-vault]
departments: [marketing, ai-office]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
related: [marketing, marketing-prime-radiant, janus-prime-radiant-build, 2026-05-08-marketing-prime-radiant-greenlit-with-andrew, llm-wiki]
---

# Marketing Prime Radiant — separate Drive vault + own CLAUDE.md

## Decision

The Marketing Prime Radiant gets its **own Google Shared Drive folder** and its **own `CLAUDE.md`** derived from the AIO one. It is *not* a sub-section of the AIO vault. The scope is a full Marketing-department Prime Radiant — broader than the originating "Marketing PR project" framing in [[2026-05-08-marketing-prime-radiant-greenlit-with-andrew|the greenlight decision]] suggested. CRM selection remains a Signals-layer dependency but is not a blocker for design and architecture work, which can begin immediately.

## Context

The [[2026-05-08-marketing-prime-radiant-greenlit-with-andrew|greenlight decision]] earlier today left the vault topology as an open question ("separate Drive folder vs sub-section of AIO vault"), with v0 likely starting as a sub-section "for speed." That provisional default is now overridden — Michael's call (same day) is **separate vault from the start**.

## Why separate vault

- **Scope is genuinely department-level, not project-level.** The Marketing instance will be a fully-fledged Prime Radiant for the Marketing department — campaigns, positioning, market intel, content briefs, customer/persona infrastructure, country-specific market analysis. That's not a project sub-effort; it's an institutional knowledge base on equal footing with the AIO one.
- **Federation pattern is set by precedent.** Whatever shape the Marketing instance takes becomes the template for HR, Finance, IT-Ops, Office-of-CEO, Engineering, and Training instances. Sub-section-of-AIO would set a federation pattern where every department instance lived under AIO custody — wrong shape for a digital-knowledge-twin architecture.
- **CLAUDE.md §1 Architecture subsection already anticipated this.** v0.8 schema (landed earlier today) explicitly states: *"Each Prime Radiant instance is its own vault (separate folder, separate `CLAUDE.md` derived from this one)."* Treating Marketing as separate honours the schema's already-stated federation discipline; treating it as sub-section would have created a v0.8 vs v0.9 schema drift before the first sibling instance even existed.
- **Department ownership** — Andrew (CMO) will eventually curate the Marketing instance; AIO custody of a Marketing sub-section would have produced a permission and ownership mess from week one.

## Why not wait for CRM

CRM selection is the gating dependency for the **Signals layer richness** — without a CRM, the Marketing instance can't capture inbound web messages, lead flow, email threads tied to opportunities. But:

- Signals layer is partial-ready without CRM: Fireflies (Andrew's calls), Slack, curated articles via Web Clipper, news scraping per topic taxonomy — all of these can light up immediately.
- **Infrastructure layer design** is fully ready: ICP, Personas, mission framing, country plans, topic taxonomy can be documented now. The Marketing brainstorm with Andrew identified these as the explicit dependencies for Outputs; documenting them is the highest-leverage pre-CRM work.
- **Vault setup, CLAUDE.md derivation, entity vocabulary design, federation linkage to AIO** — all CRM-independent.

Waiting for CRM would forfeit the post-brainstorm momentum with Andrew. Better to design and architect now; flow the CRM-dependent Signals when the CRM lands.

## What happens next (mechanics)

1. **New Google Shared Drive folder** created (Michael) — naming convention TBD; suggested: *Janus Prime Radiant — Marketing*, parallel to *Janus Prime Radiant — AI Office*.
2. **CLAUDE.md derived** from the AIO one (CLAUDE.md v0.8). The schema discipline carries over verbatim; the entity vocabulary is adapted for Marketing per CLAUDE.md §1 Domain generalisability subsection (e.g., `entities/outlets/` for media, `entities/clients/` more prominent, possibly `entities/campaigns/` and `entities/personas/` though the latter might live as Infrastructure layer docs instead).
3. **Folder scaffolding** mirrors AIO: `inbox/`, `sources/{meetings,articles,linear,monday,slack,notion}/`, `entities/{vendors,clients,people,internal,departments}/` + Marketing-specific subfolders, `concepts/`, `processes/`, `projects/`, `decisions/`, `lessons/`, `questions/`, `pulse/`, `briefs/`.
4. **Seed pages**: minimum viable set — Andrew's entity page (Marketing-instance perspective), departments stubs (mirroring AIO's), an initial project hub for the Marketing instance build itself, the originating Andrew transcript filed as a source.
5. **Federation link from AIO**: [[marketing]] department entity page in the AIO instance gets a note pointing at the canonical Marketing Prime Radiant once it exists.

## Implications

- The pattern is now established: **one Prime Radiant per department, each in its own Drive folder with its own derived CLAUDE.md.** HR, Finance, IT-Ops, Office-of-CEO, Engineering, Training instances will follow the same shape when they spin up.
- The "company-wide digital knowledge twin" framing now has concrete federation mechanics: department vaults federate via `entities/departments/` cross-references and (later) skill-driven signal flow at the Outputs ↔ Signals boundary.
- CLAUDE.md derivation is now a recurring artifact pattern — each new instance starts from the AIO CLAUDE.md as a gist (per [[gist-pattern-as-template-replacement]]), adapts entity vocabulary, and runs forward independently.
- AIO CLAUDE.md remains the canonical source for the schema discipline; updates to schema rules that should propagate to other instances need an explicit propagation step (manual for now; eventually skill-driven).

## Constraints

- Andrew is not yet set up to curate his own vault — the build phase remains [[michael-bruck]]-owned; handover to Andrew when the instance is operational enough.
- Cross-vault wikilink resolution doesn't work in Obsidian by default — `[[marketing]]` in one vault doesn't resolve to a page in another vault. Federation across vaults is initially manual (humans/agents read both vaults; cross-reference notes in each).
- Schema drift risk: as AIO CLAUDE.md continues to evolve (it's on v0.8; will keep iterating), the Marketing CLAUDE.md needs explicit re-synchronisation. Mechanism: deferred. Initial discipline: document any deliberate divergence in the Marketing CLAUDE.md status header.

## Open follow-ups

- New Drive folder creation (Michael action).
- Marketing CLAUDE.md authoring — first draft derives from AIO CLAUDE.md v0.8 with entity vocabulary swap. Likely a substantial focused pass.
- Marketing Infrastructure layer docs (ICP, Personas, mission, country plans, topic taxonomy) — Andrew dependency.
- Tier 3 brief on the Marketing PR strategic implication — explicitly held per Michael "pending the refinement of the design per the above."

## Owner

[[michael-bruck]] for build phase. Handover to [[andrew-soane]] when the Marketing instance is operational and Andrew is curating.
