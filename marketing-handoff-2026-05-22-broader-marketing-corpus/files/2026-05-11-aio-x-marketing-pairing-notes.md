---
type: brief
title: AIO × Marketing pairing notes (rolling)
slug: 2026-05-11-aio-x-marketing-pairing-notes
created: 2026-05-11
updated: 2026-05-11
departments: [ai-office, marketing]
status: active
confidence: high
sources: [2026-05-08-andrew-marketing-prime-radiant]
related: [peer-to-peer-mesh-federation-pattern, marketing, ai-office, 2026-05-08-marketing-prime-radiant-greenlit-with-andrew, 2026-05-08-marketing-prime-radiant-as-separate-vault, andrew-soane, michael-bruck]
---

# AIO × Marketing pairing notes (rolling)

> Rolling notes for the AIO × Marketing pairing. Lives in the shared subfolder per [[peer-to-peer-mesh-federation-pattern]]. Visible from both vaults: AIO sees it at `entities/departments/marketing/2026-05-11-aio-x-marketing-pairing-notes.md`; Marketing sees it at `entities/departments/ai-office/2026-05-11-aio-x-marketing-pairing-notes.md`. Filed dated despite the rolling-notes intent so chronology stays clear if it gets superseded by a fresh `YYYY-MM-DD-...` version later.

## Origin

The pairing was formalised at the 2026-05-08 founding brainstorm between [[michael-bruck|Michael]] (AIO) and [[andrew-soane|Andrew]] (Marketing). Founding-source transcripts:

- AIO copy: `Janus Prime Radiant — AI Office/sources/meetings/2026-05-08-andrew-marketing-prime-radiant.md`
- Marketing copy: `Janus Prime Radiant — Marketing/sources/meetings/2026-05-08-marketing-prime-radiant-brainstorm.md`

(The duplicate filing pre-dates the mesh pattern. Going forward, joint-meeting transcripts can file once into this shared folder rather than twice — once the Drive-shortcut consolidation is in place.)

The pairing's two founding decisions live in both vaults (AIO under `decisions/2026-05-08-marketing-prime-radiant-greenlit-with-andrew.md` and `decisions/2026-05-08-marketing-prime-radiant-as-separate-vault.md`; Marketing under parallel slugs).

## Active joint work as of 2026-05-11

**Marketing Prime Radiant instance build.** AIO (Michael) is the build-phase facilitator; Marketing (Andrew) is the eventual curator. Schema evolutions propagate across both vaults via the [janus-prime-radiant-template](https://github.com/Janusd-io/janus-prime-radiant-template) repo. The 2026-05-11 `iso` schema addition (template v0.8.0 → v0.9.0) was the first cross-vault schema-evolution pass — see Marketing's `questions/iso-department-aio-and-template-propagation.md` for how the parity work landed.

**Marketing tooling-stack evaluation.** Marketing's CRM, CMS, email-marketing, and event-management selections all flow through AIO's tool-evaluation gates (`/ai-tool-evaluation`). Tracked in AIO's AI Tools Registry (Linear AIR). CRM benchmark shortlist: Monday Salesforce, HubSpot, Attio, possibly Zoho. CRM is Marketing's Signals-layer blocker; AIO is the evaluation throughput.

**Mesh-federation pattern validation.** The AIO×Marketing pairing is the first practical test of [[peer-to-peer-mesh-federation-pattern]] per the concept page's queued-amendment note. This shared folder *is* the test. Success criteria, broadly: (a) content created here is meaningfully visible to both vaults' ingest passes; (b) the two-vault redundancy goes away once the Drive-shortcut consolidation lands; (c) the schema rule "department stubs live as `.md`; pairing content lives in `<slug>/`" doesn't break existing tooling.

## Active joint surfaces

- **Signals flowing AIO → Marketing.** AI-tool-vendor news; AIO tool-evaluation decisions that affect the Marketing stack; AIO concept pages that have marketing-implications (e.g., the mesh pattern itself; the LLM Wiki methodology).
- **Signals flowing Marketing → AIO.** Industry-signal briefs that implicate AI tooling (sustainability regulation affecting AI use in real estate; AI-in-asset-management trends); competitor moves in the AI-marketing space; analyst commentary that shifts AIO's tool-evaluation criteria.
- **Joint Outputs.** Briefs that explicitly bridge — none yet; first candidate is a CRM-selection brief once Andrew's requirements and AIO's evaluation framework converge.

## Pending build-phase items that involve both sides

- **Andrew's Drive-side access** to the Marketing vault's `inbox/` (so Web Clipper deposits land in his vault, not Michael's). AIO knows the Cowork-mount mechanics; Marketing knows the curator handoff timeline. Joint action.
- **CRM benchmark dossier** — AIO produced HubSpot evaluation already (2026-05-08 brainstorm, transcript line 109–113); Andrew owes the full requirements list; AIO owes Monday Salesforce / Attio / Zoho parallel runs.
- **Cross-vault federation note in AIO's `entities/departments/marketing.md`** pointing at Marketing's canonical home page — addressed in this turn alongside the mesh-subfolder creation.
- **Internal-entity stubs** owed by Marketing for `andrew-soane`, `michael-bruck`, `bonaventure-wong`, `simon-tarskih`. Andrew + Michael have full pages in AIO; mirroring those into Marketing is part of the federation work.

## Open questions for this pairing (per the mesh-pattern concept's open-design-questions)

- **Meeting-transcript filing.** When a meeting touches both, does it file in `<vault>/sources/meetings/` (each side keeps a copy) OR here in the shared folder (single source of truth)? Concept page leaves this open. **Working answer for now:** file in the shared folder once the Drive-shortcut consolidation lands; until then, dual-file as we've been doing.
- **Derived synthesis routing.** A brief that bridges both vaults' bets — does it land in this shared folder, or in each vault's `briefs/` with cross-references? **Working answer for now:** the brief that's *primarily* about one side's bet lives in that vault's `briefs/`; only true-pairing synthesis lives here. The mesh-pattern test will refine this.
- **Conflict semantics if both vaults ingest the same shared doc.** Concept page flags this. **Working answer for now:** each vault's downstream is independent; lint will surface drift; no canonical-owner annotation yet.
- **ACL.** Both Andrew and Michael need write access. Drive-UI setup is Michael's action.

## Drive-setup status (as of 2026-05-11)

- AIO's `entities/departments/marketing/` created (this folder).
- Marketing's `entities/departments/ai-office/` created (parallel folder; see Marketing log).
- **Pending: Drive shortcut** to make both paths resolve to the same Drive folder. Michael's UI action.
- **Pending: ACL** — Andrew added as editor on whichever side becomes canonical.

Until the shortcut lands, content created on one side needs manual mirroring to the other. The first lint pass will surface drift.
