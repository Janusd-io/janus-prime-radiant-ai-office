# AIO × Marketing — shared subfolder

> Mesh-federation subfolder per [[peer-to-peer-mesh-federation-pattern]]. This folder is the canonical home for content the AIO and Marketing Prime Radiant instances share — joint decisions, joint meeting notes, joint synthesis. Both vaults ingest from this folder.

## What this folder is

The AIO×Marketing pairing's shared content surface. From this AIO vault, the path is `entities/departments/marketing/`. From the Marketing vault, the same content appears at `entities/departments/ai-office/`. (Currently those are two independent Drive folders; consolidating them into a single Drive-shortcut'd folder is the next setup step — see "Drive setup status" below.)

The peer department's *entity stub* still lives at `entities/departments/marketing.md` (one level up). The stub describes the Marketing department as a peer; this folder holds the working content the two departments produce together.

## What goes here

- Meetings that materially involve both AIO and Marketing (founding 2026-05-08 brainstorm; future cross-functional reviews; CRM evaluation sessions; tooling demos with both functions present)
- Joint decisions (e.g., "Marketing adopts X CRM after AIO Gate 2 evaluation" — touches both vaults' decision discipline)
- Synthesis artefacts that span both functions (briefs that explicitly bridge AIO bets and Marketing bets — the strategic-aha shape from CLAUDE.md §6)
- Pairing-level reference (this README; the rolling pairing-notes doc)
- Tooling-pipeline status (Marketing's stack — CRM, CMS, email-marketing, social — moving through AIO's evaluation gates)

## What doesn't go here

- Single-side content. AIO-only briefs / decisions / lessons stay in `briefs/`, `decisions/`, `lessons/` in this vault. Marketing-only equivalents stay in the Marketing vault. Federation is for *pairing* content, not for everything.
- The originating raw transcripts. Founding 2026-05-08 brainstorm: each vault retains its `sources/meetings/` copy (this was filed before the mesh pattern was established). Going forward, joint-meeting transcripts can file directly into this shared folder once the Drive-shortcut consolidation is in place.
- Three-way+ content. A meeting that touches AIO + Marketing + ISO doesn't sit cleanly in a pairwise folder; the mesh-pattern concept page flags this as an open design question.

## Drive setup status

**As of 2026-05-11:** Two *independent* Drive folders.

- AIO's `entities/departments/marketing/` (this folder)
- Marketing's `entities/departments/ai-office/` (parallel folder)

These need to become **one Drive folder** appearing at both paths via a Drive shortcut. Setup options:

1. **Canonical in AIO, shortcut from Marketing.** This folder is the canonical Drive folder; Marketing's `entities/departments/ai-office/` is a Drive shortcut pointing here.
2. **Canonical in Marketing, shortcut from AIO.** Inverse.
3. **Canonical in a separate parent.** A `Janus Prime Radiant — Shared — AIO × Marketing` folder somewhere outside both vaults; shortcuts from both.

Pattern preference per the concept page is symmetric — "the same Drive folder viewed from the other side." Until the shortcut is set up, content created in one folder needs manual mirroring to the other; lint will surface drift.

Pending: Michael's Drive-UI action to set up the shortcut. Tracked as a follow-up.

## ACL requirements

Both [[andrew-soane|Andrew]] (Marketing curator) and [[michael-bruck|Michael]] (AIO curator / build-phase facilitator) need read+write. Once the Drive-shortcut consolidation is in place, the ACL applies to the single canonical folder. Drive-folder-level ACL granularity is one of the open design questions on the mesh pattern.

## Initial content

- This README
- `2026-05-11-aio-x-marketing-pairing-notes.md` — rolling pairing notes; the first pairing artefact and a structural test of "does shared content here behave the way the mesh pattern says it should?"
