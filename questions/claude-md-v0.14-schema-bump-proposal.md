---
type: question
title: "CLAUDE.md v0.14 schema-bump proposal — bundle of 8 accumulated changes"
slug: claude-md-v0.14-schema-bump-proposal
created: 2026-06-02
updated: 2026-06-02
departments: [ai-office]
status: resolved
owner: michael-bruck
related: [2026-06-02-lint, 2026-05-25-lint, 2026-05-23-lint, 2026-05-20-lint, project-lint-workstream-backlog, recursive-self-improving-loop]
---

# CLAUDE.md v0.14 schema-bump proposal

The 2026-06-02 lint surfaced that CLAUDE.md v0.13 is now substantially out of sync with the actual vault structure, and that 8 schema-evolution items have accumulated across the last 4 lint cycles waiting for a v0.14 sign-off session.

This page is **the proposal artefact for that session.** Each item is presented as: trigger, status quo, proposed diff, decision required from Michael. Skim and approve/reject each in turn during the standup; the executable diffs are short enough to apply in 30 minutes after approval.

## Background — why bundle them

Each lint pulse since 2026-05-20 has surfaced 1-3 schema-evolution items that require Michael's sign-off. The wiki's discipline is that CLAUDE.md edits are high-stakes (per §5.1) and must not be made unilaterally. The accumulating bundle is now load-bearing — the 2026-06-02 lint flagged it as **the highest-priority finding** because every subsequent lint surfaces the same "schema vs reality" mismatches until v0.14 ships.

## The 8 items

### Item 1 — `vendors/` and `people/` rename (top-level, not under entities/)

**Trigger:** 2026-05-25 lint §C.1; 2026-06-02 lint §A.1.

**Status quo:** v0.13 §2 says vendor pages live at `entities/vendors/<slug>.md` and people pages at `entities/people/<slug>.md`. **Reality:** vendors/ (top-level) now has 124 files; entities/vendors/ has 8. people/ (top-level) has 43 sub-entries; entities/people/ has 6 (the YC-partner pages + Karpathy + Vivian Balakrishnan + Yusuf). The migration has *de facto* happened; only the schema is stale.

**Proposed diff:**

In v0.13 §2, replace the `entities/` block:

```
entities/
  vendors/         → AI tools, SaaS vendors, services we evaluate or use
  clients/         → client context (when applicable)
  people/          → external network: analysts, founders, partners
  internal/        → Janus teammates, expertise map, role/scope
  departments/     → Janus departments as entities ...
```

with:

```
vendors/           → AI tools, SaaS vendors, services we evaluate or use
                     (top-level; migrated from entities/vendors/ in 2026-05-Q2;
                     `migrated_from:` frontmatter on each file records original location)
people/            → external + internal people: analysts, founders, partners,
                     Janus teammates. (top-level; merged 2026-05-Q2 from
                     entities/people/ + entities/internal/. A `kind:` frontmatter field
                     distinguishes external | internal | departments.)
clients/           → client context (when applicable). (top-level; migrated from
                     entities/clients/ in same wave.)
departments/       → Janus departments as entities ...
                     (top-level; migrated from entities/departments/.)
```

Then add a note in §3 (filing rules):

> *Legacy `entities/` paths are accepted-but-deprecated.* The `migrated_from:` frontmatter field on each page records the original location for audit. New pages should use the top-level location only.

**Decision required:** Approve? Reject and migrate back? Or a third option (e.g., keep both with `entities/` as canonical for new entities and `vendors/` etc. for "anything else")?

**Recommendation:** Approve as proposed. The migration has happened operationally; the schema needs to match.

---

### Item 2 — Attribution-schema (from v0.12 + 2026-05-25 carry-forward)

**Trigger:** Originally proposed 2026-05-25 (lint §"Attribution sweep follow-up"). Held since then for sign-off.

**Status quo:** v0.12 added Fireflies attribution discipline as a *prose rule* in §5.1, but no frontmatter field captures attribution confidence. When a `decided_by:` field names a person, lint has no way to flag "this attribution is transcript-only" — the rule lives only in the curator's head.

**Proposed diff:**

Add to §4 frontmatter schema, under `decided_by:`:

```yaml
attribution: confirmed | corroborated | transcript-only | inferred
attribution_sources: [<source-slug>, <meeting-slug>, ...]   # optional, lists where confidence comes from
```

`attribution:` becomes required when `decided_by:` names a *person*. Values:
- **confirmed** — Michael or another curator explicitly stated who said something.
- **corroborated** — a non-Fireflies source (Slack thread, Notion log, calendar entry, email) supports the attribution.
- **transcript-only** — Fireflies transcript is the sole source; treat with skepticism.
- **inferred** — substantive consistency only (e.g., a CEO veto only the CEO could issue).

Add to §5.3 lint checks: pages where `decided_by:` names a person but `attribution:` is `transcript-only` or `inferred` should surface as candidates for review.

Backfill default per Michael's earlier directive (recorded in 2026-05-25 log): **leave `attribution:` absent on pre-existing pages; enforce only on new pages; sweep when an existing page is touched.**

**Decision required:** Approve? Modify the enum values? Backfill differently?

**Recommendation:** Approve as proposed. Backfill-on-touch is the right pragmatic approach.

---

### Item 3 — `presentations/` top-level folder formalisation

**Trigger:** 2026-05-25 vault reorg created this folder; was held for v0.14 along with the other §2 amendments.

**Status quo:** `presentations/` exists at the top level with 10+ HTML / md deliverables. v0.13 §2 doesn't document it.

**Proposed diff:**

Add to §2 (alongside `briefs/` and `assets/`):

```
presentations/     → outbound deliverables: HTML decks, marketing collateral,
                     external one-pagers. Distinguished from briefs/ (internal
                     synthesis) and assets/ (binary artefacts referenced inline).
                     Naming: free-form within domain conventions; date-prefix
                     for time-bound deliverables. Treated as ephemeral relative
                     to the underlying context — per [[html-as-deliverable]].
```

**Decision required:** Approve as proposed? Any naming-convention refinement?

**Recommendation:** Approve. Matches existing reality.

---

### Item 4 — `inbox/.processed/` discipline codification

**Trigger:** 2026-05-25 lint §C.3; 2026-06-02 lint §A.3 (convergence on a mixed pattern).

**Status quo:** Multiple recent ingests have used different patterns. v0.13 §5.1 step 7 says *"Move the original from inbox/ to inbox/.processed/<YYYY-MM>/ for audit. Never delete."* But in practice, recent batch ingests have moved *unique items directly to sources/* and only used `.processed/` for duplicates.

**Proposed diff:**

In §5.1 step 7, replace:

> Move the original from inbox/ to inbox/.processed/<YYYY-MM>/ for audit. Never delete.

with:

> **Unique items**: move directly from `inbox/` to the canonical location in `sources/<subfolder>/` with a kebab-case rename. The mv operation is the audit trail (git records it).
> **Duplicates** (a source whose URL / body matches an existing `sources/<subfolder>/<slug>.md`): move to `inbox/.processed/<YYYY-MM>/` with the original filename. The duplicate file is preserved for audit but is not added to the canonical `sources/` tree.
> **Never delete from inbox/.** Move only.

Add dedupe-check as a new step 2.5 in §5.1:

> 2.5. **Dedupe check.** Before filing, grep `sources/<subfolder>/` for matching URL / title / date. If a match is found, treat as a duplicate per step 7. Log the duplicate in the ingest log entry.

**Decision required:** Approve? Adjust the granularity of the dedupe check?

**Recommendation:** Approve as proposed. Matches the convergent pattern from the last 3 ingests.

---

### Item 5 — Lint methodology fix — read frontmatter `status:` for active escalations

**Trigger:** 2026-06-02 [[aging-escalation-triage-2026-06-02|aging-escalation triage]] surfaced this as a methodology defect — the lint's escalation-aging check uses file presence rather than reading frontmatter. **All 7 "aging" escalations from the 2026-06-02 lint are actually resolved.**

**Status quo:** §5.3 step 8 says *"Unresolved escalations — `questions/ingest-*.md` pages older than 14 days waiting on Michael."* Doesn't specify *how* to detect "unresolved."

**Proposed diff:**

In §5.3 step 8, replace:

> Unresolved escalations — `questions/ingest-*.md` pages older than 14 days waiting on Michael.

with:

> Unresolved escalations — `questions/*.md` pages with **frontmatter `status: active` AND** `updated:` older than 14 days. Status-in-frontmatter is canonical; file presence alone is not. Note that the title or filename may carry "(resolved)" or similar suffix as a curator convention — the canonical signal is the frontmatter field.

**Decision required:** Approve? Or move to option (B) from [[aging-escalation-triage-2026-06-02]] (move resolved pages out of `questions/`)?

**Recommendation:** Approve as proposed (option A). Folder structure stays clean; lint script gets one extra check.

---

### Item 6 — "Always end with Carry-forward" convention in §5.3

**Trigger:** Repeated 2026-05-20 / 2026-05-23 / 2026-05-25 / 2026-06-02 lint carry-forward items.

**Status quo:** The convention exists *de facto* (every lint pulse since 2026-05-20 ends with a "Carry-forward queue for the next lint" section), but isn't documented in §5.3.

**Proposed diff:**

Add to §5.3 after the lint pass list, before the example log format:

> **Every lint pulse ends with a `## Carry-forward queue for the next lint` section.** This is the operational backlog for the *next* lint workstream. The next lint executes carry-forward items first, then layers a fresh structural scan on top. Per Michael's 2026-05-20 directive, this convention is the load-bearing mechanism that lets each lint compound on the previous one rather than re-discovering known issues.

**Decision required:** Approve? Move to a different section?

**Recommendation:** Approve. Codifies the established convention.

---

### Item 7 — Memory-system-reference convention

**Trigger:** 2026-05-23 / 2026-05-25 / 2026-06-02 lint carry-forwards.

**Status quo:** Some wiki pages reference memory-system files (e.g., `[[project-lint-workstream-backlog]]` references a file under `memory/`, not in the vault). These wikilinks lint as broken because the target lives outside the vault. The convention has been "accept as broken-by-design"; not yet codified.

**Proposed diff:**

Add to §6 (tone and style):

> **Memory-system references.** Some wikilinks reference files in the memory system (`<vault>/../memory/` or equivalent) rather than wiki pages — e.g., `[[project-lint-workstream-backlog]]`, `[[feedback-attribution-from-fireflies]]`. These are accepted-as-broken-by-design: the targets exist but in a different filesystem location that's deliberately outside the wiki audit tree. Lint should detect the `feedback-` / `project-` / `user-` slug prefixes and skip them in broken-ref detection.

**Decision required:** Approve? Adjust the prefix-detection scheme?

**Recommendation:** Approve. Codifies the existing accept-as-broken-by-design pattern.

---

### Item 8 — Curation as a 4th workflow in §5

**Trigger:** 2026-05-25 vault reorg + this session's vendors/ migration cleanup were "curation" work that doesn't cleanly fit Ingest / Query / Lint / Index Update.

**Status quo:** v0.13 §5 names four workflows: Ingest, Query, Lint, Index Update. Curator-driven structural reorganisation (moving files between folders, deduping, schema-level cleanup) falls between the cracks. The 2026-05-25 log entry called this work *"curation"* and proposed it as a 5th workflow; deferred.

**Proposed diff:**

Add to §5 as a new sub-section §5.5:

```
### 5.5 Curate

Trigger: curator-driven, not file-driven. Examples: folder restructuring, vendor-page deduplication, schema-aligned cleanup that touches multiple pages.

1. Begin with `git pull` per the standing rule.
2. Define the scope explicitly in a log entry header: `curation | <scope description>`.
3. Execute the cleanup. Touch only files in scope; do not opportunistically edit adjacent files.
4. Update affected pages' `updated:` frontmatter to today.
5. If the cleanup reveals a schema gap that should be permanent, propose a CLAUDE.md edit (high-stakes; escalate to questions/).
6. Append a `## [YYYY-MM-DD HH:MM] curation | <scope>` log entry with: scope, files-touched, decisions-made, follow-ups.
7. End with `git add . && git commit && git push`.
```

**Decision required:** Approve? Combine with another workflow?

**Recommendation:** Approve. The 2026-05-25 vault reorg + this session's dedupe pass both exercised this shape; codification will improve consistency.

---

## Proposed sign-off process

1. **Skim items 1-8 above.** Each takes < 1 min to read.
2. For each: approve / reject / modify (one-line note).
3. After sign-off, I (or another agent / Michael's Claude Code) executes the diffs against `CLAUDE.md` and bumps to v0.14.
4. The v0.14 commit message: *"CLAUDE.md v0.14: vendors/ + people/ canonical at top level; attribution schema; presentations/ formalised; .processed/ pattern codified; lint methodology fix; carry-forward convention; memory-ref convention; curation as 5th workflow."*
5. Update `MEMORY.md` index entry for `project-lint-workstream-backlog` to point at the post-v0.14 carry-forward queue.
6. Run a quick lint pass to verify the new schema lints cleanly against current state.

## Estimated execution time after sign-off

- CLAUDE.md edits: ~30 minutes (8 surgical diffs).
- Memory file update: ~5 minutes.
- Verification lint pass: ~10 minutes.

**Total: ~45 minutes of post-sign-off work.**

## Resolution (2026-06-02)

**All 8 items approved as proposed in the 2026-06-02 standup.** CLAUDE.md bumped from v0.13 → v0.14 in a single curation pass. Executed diffs:

- §1 prose updated: 3 stale `entities/...` references cleaned (cross-instance federation; per-domain entity vocabulary; cross-instance linkage layer).
- §2: top-level `vendors/`, `people/`, `clients/`, `departments/` documented as canonical; `presentations/` added; legacy `entities/` paths flagged as accepted-but-deprecated.
- §3: per-folder naming table updated to top-level paths; `entities/internal/` row merged into `people/`.
- §4: frontmatter schema gains `attribution:`, `attribution_sources:`, `migrated_from:` fields; field rules expanded; `departments:` ↔ `departments/` linkage updated.
- §5.1: dedupe-check added as new step 2 (steps renumbered); step 8 (was step 7) split unique-vs-duplicate `mv` discipline.
- §5.3: lint check 5 references the memory-system-reference exception; check 8 fixed to read frontmatter `status:`; new check 9 surfaces attribution-discipline-violators; "Always end with Carry-forward" convention documented as load-bearing.
- §5.5: new "Curate" workflow added between §5.4 and §6.
- §6: new "Memory-system references" bullet documents the `feedback-*` / `project-* `/ `user-*` slug-prefix convention.
- Top-of-file version note records the 8 items.

Carry-forward for the next lint: verify the new schema against current vault state (the 2026-06-02 verification lint).

