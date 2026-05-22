# Migration manifest — file-by-file actions

Authoritative file-level list for the Singapore-monitoring federation handoff (2026-05-22). Each row says: what to do, where it goes in the Marketing vault, and any frontmatter / body edits applied vs. the AIO original.

## Files in this bundle (10 markdown + 1 PDF)

### Canonical-to-Marketing — Marketing owns, AIO has pointer

| File | Marketing target path | Action | Edits vs AIO original |
|---|---|---|---|
| `files/projects/singapore-news-monitoring.md` | `projects/singapore-news-monitoring.md` | New canonical | `owner:` flipped from `michael-bruck` to `andrew-soane`. Frontmatter `departments:` reordered `[marketing, ai-office]` (Marketing first, as instance owner). Body retains AIO-side cross-refs as plain-text mentions; wikilinks point to AIO-canonical content (resolves via federation). |
| `files/projects/singapore-monitoring-frame-audit-2026-05.md` | `projects/singapore-monitoring-frame-audit-2026-05.md` | New canonical | `owner:` → `andrew-soane`. Framer-of-Record language updated: Andrew operationally, Bonaventure for the strategic check-in (open question — Andrew confirms). Methodology unchanged. The pulse-entry deliverable target is the Marketing vault, not AIO. |

### Dual-location — both vaults carry, both update

| File | Marketing target path | Action | Edits vs AIO original |
|---|---|---|---|
| `files/processes/pre-ship-confidence-and-frame-check.md` | `processes/pre-ship-confidence-and-frame-check.md` | New copy in Marketing | `departments:` includes `marketing`. First-instance note updated — "First Marketing instance is the Singapore news monitoring agent." Other text unchanged. |
| `files/concepts/pilot-in-command.md` | `concepts/pilot-in-command.md` | New copy in Marketing | Unchanged (organisation-wide concept from AI Policy §5.9; applies identically in both vaults). |
| `files/entities/internal/joyce-woo.md` | `entities/internal/joyce-woo.md` | New copy in Marketing | Unchanged (Joyce is a Janus internal person; both vaults should carry her entity). |

### Supporting-context copy — Marketing gets its own, no further sync

| File | Marketing target path | Action |
|---|---|---|
| `files/entities/people/vivian-balakrishnan.md` | `entities/people/vivian-balakrishnan.md` | Copy |
| `files/decisions/2026-05-12-singapore-as-lead-market.md` | `decisions/2026-05-12-singapore-as-lead-market.md` | Copy |
| `files/sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.md` | `sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.md` | Copy (markdown twin) |
| `files/sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.pdf` | `sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.pdf` | Copy (original PDF) |
| `files/sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md` | `sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md` | Copy |
| `files/pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md` | `pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md` | Copy |

## Marketing vault `index.md` — suggested additions

Add to the relevant sections (paste verbatim, alphabetise within each section as the index discipline requires):

### Projects section

```
- [singapore-news-monitoring](projects/singapore-news-monitoring.md) — Bonaventure-driven scheduled market-intelligence agent: scrapes Singapore news sources, semantic-ranks against Janus themes, posts 1–2 nuggets/week to Slack. Owner Andrew; sponsor Bonaventure. [active]
- [singapore-monitoring-frame-audit-2026-05](projects/singapore-monitoring-frame-audit-2026-05.md) — 1-working-day frame audit experiment for the Singapore monitoring workflow. Tests whether the agent's operating frame still matches the framer's current strategic situation. [active]
```

### Processes section

```
- [pre-ship-confidence-and-frame-check](processes/pre-ship-confidence-and-frame-check.md) — reusable two-axis pre-ship gate for Layer-3 agentic workflows. Output-quality + frame-validity scored separately. First Marketing instance: Singapore news monitoring.
```

### Concepts section

```
- [pilot-in-command](concepts/pilot-in-command.md) — §5.9 accountability framing from the AI Policy. AI is a tool; the employee is the Pilot in Command. Applies organisation-wide.
```

### Decisions section

```
- [2026-05-12-singapore-as-lead-market](decisions/2026-05-12-singapore-as-lead-market.md) — Singapore confirmed as Janus's lead commercial market for AI Native products. [resolved]
```

### Pulse section

```
- [2026-05-12-vivian-balakrishnan-llm-wiki-government](pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md) — Singapore Foreign Minister running his own LLM wiki on a Raspberry Pi; keynoting AI Engineering Conference 16–17 May. Potential government-side advocate via Bonaventure's personal network. [high]
```

### Entities sections

```
- [joyce-woo](entities/internal/joyce-woo.md) — Janus CEO, Singapore. Co-author of the Janus Singapore white paper. Recommended-outlet source for the Singapore monitoring agent.
- [vivian-balakrishnan](entities/people/vivian-balakrishnan.md) — Singapore Foreign Minister; LLM-wiki advocate; Bonaventure's personal contact.
```

## Marketing vault `log.md` — suggested import entry

```
## [2026-05-22 HH:MM] import | Singapore-monitoring federation handoff from AIO | 10 markdown + 1 PDF
- driver: cross-vault federation transfer per [[peer-to-peer-mesh-federation-pattern]]. The Singapore news monitoring agent is operationally a marketing-intelligence workflow and now belongs in the Marketing instance, with [[andrew-soane]] as the owner-of-record.
- imported (canonical-to-Marketing):
  - projects/singapore-news-monitoring.md — Bonaventure-driven scheduled market-intelligence agent. owner:andrew-soane.
  - projects/singapore-monitoring-frame-audit-2026-05.md — 1-day frame audit experiment. owner:andrew-soane.
- imported (dual-location):
  - processes/pre-ship-confidence-and-frame-check.md
  - concepts/pilot-in-command.md
  - entities/internal/joyce-woo.md
- imported (supporting context):
  - entities/people/vivian-balakrishnan.md
  - decisions/2026-05-12-singapore-as-lead-market.md
  - sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.{md,pdf}
  - sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md
  - pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md
- not imported (stay AIO-canonical, accessed via cross-vault federation):
  - briefs/coordination-leverage-model.md
  - concepts/coordination-three-layer-model.md
  - briefs/ai-native-janus-positioning.md
  - questions/2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room.md
- next actions: file `framed_by:` decision (Andrew or Bonaventure?); choose Slack destination channel; calibrate pre-ship gate cadence; schedule the frame audit (1 working day, target end of W22).
```

## Cross-vault wikilinks that need resolution

The transferred files contain wikilinks that reference AIO-canonical pages (the ones not transferring). The Marketing vault should resolve these via the mesh subfolder (`entities/departments/ai-office/`). Inventory of cross-vault references in the transferred content:

- `[[coordination-leverage-model]]` — AIO-canonical (briefs/coordination-leverage-model.md in AIO vault)
- `[[coordination-three-layer-model]]` — AIO-canonical
- `[[coordination-tax]]` — AIO-canonical
- `[[organisational-digital-twin]]` — AIO-canonical
- `[[builders-sellers-measurers]]` — AIO-canonical
- `[[ai-native-janus-positioning]]` — AIO-canonical
- `[[ai-native-enterprise-restructuring]]` — AIO-canonical
- `[[ai-tool-evaluation-framework]]` — AIO-canonical (until ISO instance ratifies its own)
- `[[ai-policy]]` — AIO-canonical (the policy is company-wide; AIO is the maintainer)
- `[[shadow-ai-prohibition]]`, `[[tool-tiers]]`, `[[sandbox-environment]]` — AIO-canonical
- `[[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]]` — AIO-canonical
- `[[ai-registry]]` — AIO-canonical
- `[[standup]]` — AIO-canonical
- `[[fireflies]]` — AIO-canonical (Core Infrastructure, organisation-wide)
- `[[anthropic]]`, `[[claude]]`, `[[notion]]`, `[[monday]]`, `[[linear]]`, `[[hostinger]]`, `[[slack]]` — AIO-canonical
- `[[bonaventure-wong]]`, `[[jehad-altoutou]]`, `[[michael-bruck]]`, `[[euclid-wong]]` — AIO-canonical entities/internal pages

**Resolution mechanism:** the mesh `entities/departments/ai-office/` shared subfolder in the Marketing vault is where cross-vault federation lives. Obsidian's wikilink resolver will pick up the link if the slug matches a file *anywhere* in the vault, including via Drive-shortcut to the AIO vault folders.

**Pragmatic fallback for early Marketing vault state:** if wikilinks dangle, that's acceptable for the first 2–4 weeks — they're informational (the federation pattern documents `[[wikilinks]]` may not resolve until the mesh sync is fully wired). Marketing imports more content from AIO as needed.

## What you should NOT do during import

- **Do not modify the file contents** beyond what's already pre-rewritten in this bundle. The transferred files have been edited for Marketing context; further edits should happen *after* import as normal Marketing-vault iteration.
- **Do not delete the AIO copies** of the moved-canonical files. The AIO-side post-import step (in `post-import-AIO-updates.md`) replaces them with federation pointers, *not* deletes.
- **Do not import `coordination-leverage-model.md` or related framework pages.** Marketing references them via federation; importing the framework would clutter the Marketing vault and create dual-canonical drift.
- **Do not back-fill old AIO meeting source files** mentioning Singapore monitoring. Marketing's audit trail starts from the import date forward.
