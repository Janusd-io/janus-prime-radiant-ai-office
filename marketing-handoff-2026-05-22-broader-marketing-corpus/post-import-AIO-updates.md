# Post-import AIO-side updates

Apply on the **AIO** vault after the Marketing vault confirms successful import of bundle #2. Same federation-pointer-stub pattern as the Singapore-monitoring bundle's post-import. Sequence: verify Marketing-side imports → apply these AIO-side rewrites → commit both vaults → log.

## Files that get replaced with federation-pointer stubs (24 total)

These are the **canonical-to-Marketing** files in this bundle. Replace each AIO-side file with a thin pointer stub. The stub preserves inbound wikilinks from AIO strategic-context pages without dual-canonical drift.

### Briefs (1)

- `briefs/agentic-lean-marketing-stack.md`

### Projects (11)

- `projects/janus-website.md`
- `projects/janus-website-cms.md`
- `projects/janus-crm-selection.md`
- `projects/crm-evaluation-and-selection.md`
- `projects/singapore-launch.md`
- `projects/janus-thought-leadership.md`
- `projects/janus-careers-page.md`
- `projects/janus-marketing-capabilities.md`
- `projects/janus-brand-guidelines-refresh.md`
- `projects/janus-prime-radiant-marketing.md`
- `projects/apply-standup-methodology-to-andrew-work-stream.md`

### Decisions (12 — the Marketing-canonical ones in this bundle that weren't already org-wide)

Apply pointer stubs to all 2026-05-05 marketing decisions, 2026-05-07 llm-wiki-extends, 2026-05-08 marketing-PR decisions, 2026-05-12 marketing-specific decisions, 2026-05-13 andrew-soane decisions, 2026-05-18 marketing/website decisions. The 5 org-wide decisions stay AIO-canonical (those are dual-location, not federated).

## Stub template — apply to each replaced file

Replace the body with:

```markdown
---
type: <project | brief | decision>
title: <original title> (federated to Marketing)
slug: <original slug>
created: <original date>
updated: 2026-05-22
departments: [marketing, ai-office]
status: federated
owner: andrew-soane
canonical_location: marketing-prime-radiant
related: [marketing-prime-radiant, peer-to-peer-mesh-federation-pattern, <prior related list>]
---

# <original title> — federated to Marketing

**Canonical location: [[marketing-prime-radiant|Janus Prime Radiant · Marketing]] vault.** This page was incubated in the AIO Prime Radiant and migrated to the Marketing instance on 2026-05-22 as part of the broader-marketing-corpus federation handoff (bundle #2 of the 2026-05-22 federation work).

For current state, owners, methodology, and updates, see the Marketing vault's `<original path>`.
```

For decision pages specifically, the stub can be shorter — just the date, slug, title, status:federated, canonical_location, and a one-line pointer.

## Files that stay AIO-canonical but get their `departments:` expanded

The 5 org-wide decisions transferred as dual-location — confirm `departments:` includes both `ai-office` and `marketing`. Most already do:

- `decisions/2026-05-12-html-as-presentation-format-adopted.md` — verify
- `decisions/2026-05-13-prefer-html-over-powerpoint-for-claude-generated-decks.md` — verify
- `decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md` — verify
- `decisions/2026-05-08-per-department-prime-radiant-instances.md` — verify
- `decisions/2026-05-13-github-canonical-prime-radiant-substrate.md` — verify

## Files that stay AIO-canonical, no change

- `briefs/ai-native-janus-positioning.md` — dual-location with Marketing; both vaults carry; updates flow via the mesh. Do not flip to pointer.
- All 5 concepts (`stack-composition-framework`, `builders-sellers-measurers`, `buyer-personas`, `messaging-pillars`, `ai-washing`) — dual-location, no AIO-side change.
- `processes/janus-html-deck-brand-guideline.md` — dual-location, no change.
- All 7 vendor entities — dual-location, no change.
- Both internal entities (Andrew, Bonaventure) — dual-location, no change.
- Brand assets (logo SVGs, skill bundle snapshots) — dual-location, no AIO-side change.
- Brand book source (PDF + md twin) — dual-location, no AIO-side change.
- Marketing-stack technical writeup — dual-location, no change. The source file stays in AIO for the audit trail; Marketing carries a copy because it informs Marketing decisions going forward.
- All 5 meeting sources — dual-location, no change. AIO retains its meeting-source audit trail; Marketing carries copies because the meetings produced Marketing-canonical decisions.

## File a federation-handoff pairing decision

New decision in the AIO×Marketing mesh subfolder:

**Filename:** `entities/departments/marketing/2026-05-22-broader-marketing-corpus-federation-handoff.md`

```markdown
---
type: decision
title: Broader marketing corpus federation handoff — AIO → Marketing (bundle #2)
slug: 2026-05-22-broader-marketing-corpus-federation-handoff
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, marketing]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: []
related: [marketing-prime-radiant, peer-to-peer-mesh-federation-pattern, 2026-05-22-singapore-monitoring-federation-handoff, agentic-lean-marketing-stack, ai-native-janus-positioning, janus-html-deck-brand-guideline]
---

# Broader marketing corpus federation handoff — AIO → Marketing (bundle #2)

Decision: the broader marketing-domain knowledge body the AIO has accumulated from 2026-05-04 onward moves canonically to the Marketing Prime Radiant. Companion to the Singapore-monitoring federation handoff (bundle #1). The two bundles together complete the marketing-domain federation handoff event of 2026-05-22.

## Why

The AI Office incubated the marketing-domain knowledge because the AIO instance was the only Prime Radiant live during the 2026-05-04 → 2026-05-19 period. Now that Andrew's Marketing instance is set up and operational, the canonical home for the marketing-domain content moves with it. The AIO continues to reference all of it via federation pointers and the mesh.

## What moved canonically (24 files)

See `marketing-handoff-2026-05-22-broader-marketing-corpus/migration-manifest.md` for the file-by-file list.

## What stayed dual-location

The marketing-stack vendor entities, the brand guideline process, the ai-native-janus-positioning brief, the marketing-Infrastructure concepts (stack-composition-framework, builders-sellers-measurers, buyer-personas, messaging-pillars, ai-washing), and the two internal entities (Andrew, Bonaventure).

## What stayed AIO-canonical

The Coordination Leverage Model framework + concepts, the AI Policy + governance machinery, the ai-native-enterprise-restructuring brief, the Principle 10 escalation, all AIO operational pages.

## Federation hygiene

Transfer bundle preserved at `marketing-handoff-2026-05-22-broader-marketing-corpus/` (AIO side) for the audit trail. Marketing-side import log mirrors this decision.

This handoff plus the Singapore-monitoring handoff together set the precedent for future federation events: HR (recruitment pipeline + leave + Assessify), IT/Ops (IAM + sandbox + production handover), Engineering (HGTFT + websites), Office of CEO (when that instance stands up).
```

## Update AIO `index.md`

The Projects and Briefs sections lose substantive entries; flip them to "federated" markers. Decisions section flips many entries to "federated" — the index may want a separate "Marketing decisions (federated to Marketing vault)" sub-section as a one-liner pointer rather than 24 individual federated lines.

Suggested terse pattern:

```
### Marketing decisions (federated 2026-05-22)

All marketing-domain decision records from 2026-05-04 onward are now canonical in the Marketing Prime Radiant vault. AIO retains federation-pointer stubs; cross-vault wikilinks resolve via the [[peer-to-peer-mesh-federation-pattern|mesh]]. Browse: [[marketing-prime-radiant|Marketing Prime Radiant]] → `decisions/`.
```

## Append AIO `log.md`

```markdown
## [2026-05-22 HH:MM] federation-handoff-package | broader marketing corpus → Marketing Prime Radiant | bundle #2
- driver: Michael — "What about all the other marketing related knowledge we have curated in the AIO vault beyond just the Singapore framing concept?" Companion to the Singapore-monitoring handoff (bundle #1) earlier the same day. Together these two bundles complete the marketing-domain federation handoff event of 2026-05-22.
- bundle: marketing-handoff-2026-05-22-broader-marketing-corpus/ — 66 markdown + 2 SVG + 1 PDF.
- canonical-to-Marketing (24 files): 1 brief, 11 projects, 24 decisions (deduplicated from the AIO record), 8 sources (3 articles + 5 meetings). AIO-side becomes federation pointers per the post-import doc.
- dual-location (29 items): 1 brief (ai-native-janus-positioning), 5 concepts (stack-composition-framework, builders-sellers-measurers, buyer-personas, messaging-pillars, ai-washing), 1 process (janus-html-deck-brand-guideline), 5 org-wide decisions, 2 internal entities (Andrew, Bonaventure), 7 vendor entities, 5 asset files.
- stays AIO-canonical (referenced from Marketing via mesh): the entire Coordination Leverage Model framework, the AI Policy + governance machinery, ai-native-enterprise-restructuring, the Principle 10 escalation, AIO operational pages.
- judgment calls beyond the Singapore bundle's rubric:
  - **5 stub project hubs included.** Rationale: even unpopulated, they live where they belong. Marketing decides to fill, merge, or retire.
  - **`ai-native-janus-positioning` as dual-location, not Marketing-canonical.** Reflects that it's Bonaventure's strategic positioning thesis (lives close to the framework author) but Marketing uses it as Infrastructure-layer content (needs to be in their vault for daily reference).
  - **Decision dedup picked the cleaner-titled / more-complete versions** where 5/12 had duplicates. Alternates left in AIO for the audit trail.
  - **The Marketing-stack technical writeup transfers** even though it's nominally Michael → Jehad. It's marketing-domain reasoning that informed Marketing decisions; it belongs in the Marketing vault for ongoing reference.
- next: Andrew (or Michael) imports both bundles into the Marketing vault. After verification, apply both bundles' post-import-AIO-updates docs on the AIO side. The two-bundle handoff event of 2026-05-22 is the precedent for future cross-vault project handoffs.
```

## Sanity check after both sides commit

- `grep -rl "agentic-lean-marketing-stack" .` on the AIO side should now find: federation-pointer stub, federation-handoff decision in `entities/departments/marketing/`, AIO strategic-context pages, index.md, log.md, both transfer bundles. Not the brief content.
- `grep -rl "agentic-lean-marketing-stack" .` on the Marketing side should find: the canonical brief, index.md, log.md, any pages that reference it.
- All `[[wikilinks]]` resolve to a real page on both sides (different pages for the moved content, but both legitimate).

## Future federation handoffs — what this precedent shows

The two-bundle 2026-05-22 federation event (Singapore monitoring + broader marketing corpus) establishes:

1. **Bundle structure** — a directory at the source-vault root with TRANSFER-README + migration-manifest + post-import-AIO-updates + a `files/` subtree pre-mapped to the destination-vault target paths.
2. **The four-class rubric** — canonical-to-destination / dual-location / supporting-context-copy / stay-source-canonical. Each class has a distinct frontmatter and reference pattern.
3. **Federation-pointer stubs, not deletion** — preserves inbound wikilinks from source-vault strategic-context pages.
4. **Pairing-decision in the mesh subfolder** — both vaults see the handoff decision via the shared `entities/departments/<peer>/` folder.
5. **Logged in both vaults' `log.md`** as `federation-handoff-package` (source) and `import` (destination).
6. **Bundle preserved as audit trail** at the source-vault root after import.

Apply the same pattern when:

- Engineering instance stands up — HGTFT moves canonical there; AIO retains pointer.
- IT/Ops instance stands up — IAM workstreams (Identity Is The Perimeter), sandbox-to-production handover SOP, ai-policy-gate-approval IT-side mechanics move there.
- HR instance stands up — recruitment pipeline, Assessify project, ims-enrolment work moves there.
- Office of CEO instance stands up — ai-native-janus-positioning may shift from dual-location to canonical-CEO with both Marketing and AIO holding federation pointers.
