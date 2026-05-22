# Post-import AIO-side updates

Apply these edits on the **AIO** Prime Radiant after the Marketing vault has successfully imported the handoff bundle. Sequence: (1) verify the Marketing vault renders the imported pages correctly; (2) apply these AIO-side rewrites; (3) commit both vaults.

## 1. Replace AIO-canonical content with federation pointers

These two pages move *canonical to Marketing*. The AIO vault retains thin pointer pages — slug-stable, with one line of body content pointing at the Marketing-canonical page. This preserves inbound wikilinks from the AIO's strategic-context pages (Coordination Leverage Model brief, three-layer model concept, etc.) without dual-canonical drift.

### `projects/singapore-news-monitoring.md`

Replace the body content with:

```markdown
---
type: project
title: Singapore News Monitoring Agent (federated to Marketing)
slug: singapore-news-monitoring
created: 2026-05-07
updated: 2026-05-22
departments: [marketing, ai-office]
countries: [sg]
status: federated
owner: andrew-soane
canonical_location: marketing-prime-radiant
related: [marketing-prime-radiant, peer-to-peer-mesh-federation-pattern, coordination-leverage-model, coordination-three-layer-model, singapore-monitoring-frame-audit-2026-05, bonaventure-wong, andrew-soane]
---

# Singapore News Monitoring Agent (federated to Marketing)

**Canonical location: [[marketing-prime-radiant|Janus Prime Radiant · Marketing]] vault.** This project was incubated in the AIO Prime Radiant from 2026-05-07 to 2026-05-22 and migrated to the Marketing instance on 2026-05-22 — see the [[2026-05-22-singapore-monitoring-federation-handoff|federation-handoff decision]].

Operationally a marketing-intelligence workflow. The AI Office continues to reference this work as the first concrete Layer-3 test case for the [[coordination-leverage-model|Coordination Leverage Model]] and the proving ground for the [[pre-ship-confidence-and-frame-check|pre-ship confidence + frame-validity gate]], but the project itself lives in Marketing.

For current state, owners, methodology, and updates, see the Marketing vault's `projects/singapore-news-monitoring.md`. Mesh-pairing folder for cross-AIO×Marketing notes: `entities/departments/marketing/` (this vault) ↔ `entities/departments/ai-office/` (Marketing vault).
```

### `projects/singapore-monitoring-frame-audit-2026-05.md`

Replace with:

```markdown
---
type: project
title: Singapore news-monitoring frame audit — May 2026 (federated to Marketing)
slug: singapore-monitoring-frame-audit-2026-05
created: 2026-05-22
updated: 2026-05-22
departments: [marketing, ai-office, office-of-ceo]
countries: [sg]
status: federated
owner: andrew-soane
canonical_location: marketing-prime-radiant
related: [singapore-news-monitoring, marketing-prime-radiant, pre-ship-confidence-and-frame-check, 2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]
---

# Singapore news-monitoring frame audit — federated to Marketing

**Canonical location: [[marketing-prime-radiant|Janus Prime Radiant · Marketing]] vault.** The audit experiment was designed in the AIO Prime Radiant on 2026-05-22 and migrated to the Marketing vault the same day as part of the [[2026-05-22-singapore-monitoring-federation-handoff|federation handoff]].

The AIO retains a strong interest in the audit's *outcome*: the resulting `pulse/` entry is the empirical evidence base for the [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room|Principle 10 ratification escalation]]. When Andrew completes the audit, cross-vault link the result back from this stub.
```

## 2. Cross-link from the Marketing pairing subfolder

Add a new pairing-notes entry in `entities/departments/marketing/`:

**Filename:** `entities/departments/marketing/2026-05-22-singapore-monitoring-federation-handoff.md`

```markdown
---
type: decision
title: Singapore-monitoring federation handoff — AIO → Marketing
slug: 2026-05-22-singapore-monitoring-federation-handoff
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, marketing]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: []
related: [marketing-prime-radiant, peer-to-peer-mesh-federation-pattern, singapore-news-monitoring, singapore-monitoring-frame-audit-2026-05, pre-ship-confidence-and-frame-check, 2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]
---

# Singapore-monitoring federation handoff — AIO → Marketing

Decision: the [[singapore-news-monitoring]] project and the [[singapore-monitoring-frame-audit-2026-05]] experiment move canonically to the Marketing Prime Radiant. The AIO retains federation-pointer stubs. The handoff is the first practical exercise of the [[peer-to-peer-mesh-federation-pattern]] beyond shared-meeting content — the first project handoff between vaults.

## Why

Operationally a marketing-intelligence workflow. The framer (increasingly Andrew, with Bonaventure as strategic check-in) and the executing agent should share a vault to keep the [[pre-ship-confidence-and-frame-check|pre-ship gate]]'s feedback loop tight. The AIO continues to reference the work as the first concrete Layer-3 test case for the [[coordination-leverage-model]], but the project itself belongs in Marketing.

## What moved canonically

- `projects/singapore-news-monitoring.md`
- `projects/singapore-monitoring-frame-audit-2026-05.md`

## What was copied (dual-location)

- `processes/pre-ship-confidence-and-frame-check.md`
- `concepts/pilot-in-command.md`
- `entities/internal/joyce-woo.md`

## What was copied (supporting context, no further sync)

- `entities/people/vivian-balakrishnan.md`
- `decisions/2026-05-12-singapore-as-lead-market.md`
- `sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.{pdf,md}`
- `sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md`
- `pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md`

## What stayed AIO-canonical

- `briefs/coordination-leverage-model.md`
- `concepts/coordination-three-layer-model.md`
- `concepts/coordination-tax.md`
- `concepts/organisational-digital-twin.md`
- `briefs/ai-native-janus-positioning.md`
- `briefs/ai-native-enterprise-restructuring.md`
- `questions/2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room.md`

## Federation hygiene

The transfer bundle at `marketing-handoff-2026-05-22-singapore-monitoring/` is retained on the AIO side as the audit trail for the move. The Marketing-side import log entry (in `log.md`) mirrors this decision page.

This is the **first non-meeting-content** federation exchange between AIO and Marketing. Worth noting in the mesh-pattern documentation as a precedent for future cross-vault project handoffs (e.g., when the IT/Ops instance takes over IAM workstreams, when HR takes over recruitment-pipeline operations).
```

## 3. Update AIO-side `index.md`

Three lines to update under Projects:

- **Replace** the existing `singapore-news-monitoring` line with:

```
- [singapore-news-monitoring](projects/singapore-news-monitoring.md) — federated to Marketing 2026-05-22; canonical in the Marketing Prime Radiant vault. AIO retains a pointer + the strategic-framework cross-references. [federated]
```

- **Add** for the frame audit:

```
- [singapore-monitoring-frame-audit-2026-05](projects/singapore-monitoring-frame-audit-2026-05.md) — federated to Marketing 2026-05-22; the audit experiment for the Singapore monitoring workflow now runs in Marketing. [federated]
```

(Or remove both from the curated Projects section if you prefer; both are now `status: federated`.)

## 4. Update the AIO `log.md`

Append:

```markdown
## [2026-05-22 HH:MM] federation-handoff | Singapore news monitoring → Marketing Prime Radiant | first cross-vault project transfer
- driver: Michael — "the Singapore monitoring is a marketing activity, it really should belong in Andrew's Prime Radiant." First operational exercise of the federation pattern beyond shared-meeting content; first cross-vault project handoff.
- moved canonical to Marketing:
  - projects/singapore-news-monitoring.md (replaced in AIO with federation-pointer stub)
  - projects/singapore-monitoring-frame-audit-2026-05.md (replaced in AIO with federation-pointer stub)
- copied to Marketing (dual-location):
  - processes/pre-ship-confidence-and-frame-check.md
  - concepts/pilot-in-command.md
  - entities/internal/joyce-woo.md
- copied to Marketing (supporting context, no further sync):
  - entities/people/vivian-balakrishnan.md
  - decisions/2026-05-12-singapore-as-lead-market.md
  - sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.{pdf,md}
  - sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md
  - pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md
- updated (AIO side):
  - projects/singapore-news-monitoring.md → federation-pointer stub
  - projects/singapore-monitoring-frame-audit-2026-05.md → federation-pointer stub
  - index.md → status flips to "federated"; brief note added
  - entities/departments/marketing/2026-05-22-singapore-monitoring-federation-handoff.md → new pairing-decision page (also visible in Marketing's `entities/departments/ai-office/` per the mesh pattern)
- stayed AIO-canonical (referenced from Marketing via mesh):
  - briefs/coordination-leverage-model.md
  - concepts/coordination-three-layer-model.md / coordination-tax.md / organisational-digital-twin.md
  - briefs/ai-native-janus-positioning.md / ai-native-enterprise-restructuring.md
  - questions/2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room.md
- transfer bundle preserved at: marketing-handoff-2026-05-22-singapore-monitoring/ — audit trail for the move.
- judgment calls:
  - Federation-pointer stubs (not deletion) — preserves inbound wikilinks from AIO strategic-context pages.
  - The pre-ship gate is dual-location, not federated — it's a reusable governance process that both vaults will independently call. Updates flow via the mesh subfolder when material changes.
  - Pilot in Command stays dual-location for the same reason (organisation-wide concept from AI Policy §5.9).
  - The Principle 10 escalation stays AIO-canonical — it's a framework decision that belongs with the framework's author (Michael, AIO instance). Marketing benefits from the operationalisation (`pre-ship-confidence-and-frame-check.md`) without owning the framework debate.
- next: Andrew runs the frame audit at his cadence; outcome routes the Principle 10 ratification decision; if Principle 10 ratifies, the AIO framework brief gets v0.4 bumped + the wiki schema gets `framed_by:` added.
```

## 5. Optional — soften references in AIO strategic-context pages

The Coordination Leverage Model brief (`briefs/coordination-leverage-model.md`) references `[[singapore-news-monitoring]]` and `[[singapore-monitoring-frame-audit-2026-05]]` as "the first concrete Layer-3 test case." With federation, both still resolve via the stub pages — no rewrite required. **Suggested**: add a one-line note in the brief's "Watch for" section:

```
- **Singapore monitoring federation (2026-05-22).** First cross-vault project handoff. Singapore monitoring is now Marketing-canonical; the audit-result evidence base for Principle 10 ratification lives in the Marketing vault going forward.
```

Apply at next iteration of the brief; not blocking on this handoff.

## 6. Sanity-check after both sides commit

- `grep -rl "singapore-news-monitoring" .` on the AIO side should now find only: federation-pointer stub, federation-handoff decision in `entities/departments/marketing/`, the AIO strategic-context pages (briefs, concepts), the index.md, the log.md, and the transfer bundle. *Not* the actual project content.
- `grep -rl "singapore-news-monitoring" .` on the Marketing side should find: the canonical project hub, the frame-audit hub, the index.md, the log.md, and any future audit pulse entries.
- Both sides resolve `[[singapore-news-monitoring]]` to a real page (different pages, but both legitimate).

## 7. When Engineering Prime Radiant stands up — repeat for HGTFT

The `projects/hgtft.md` page in the AIO is already framed as a placeholder for the eventual Engineering instance. When that instance stands up, repeat this federation-handoff workflow for HGTFT. This Marketing handoff is the precedent.
