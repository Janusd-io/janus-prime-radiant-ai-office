---
type: question
title: "log.md concurrency: author tag in entry headers (schema) + union merge driver (infrastructure)"
slug: log-md-author-attribution-and-union-merge
created: 2026-06-12
updated: 2026-06-12
departments: [ai-office]
status: active
owner: michael-bruck
captured_by: jehad-altoutou
related: [per-instance-curator-role, prime-radiant-storage-substrate]
---

# log.md concurrency: author attribution + union merge

## Context

On 2026-06-12 Jehad hit a hard merge conflict in `log.md`: both Jehad and Michael appended different entries (09:40 and 09:44) at the end of the file from separate machines. The interrupted merge also stranded git lock files (`index.lock`, `HEAD.lock`, `MERGE_HEAD`) that blocked all subsequent pulls until manually cleared. This is the race condition [[per-instance-curator-role]] anticipates ("only the primary or deputy runs Obsidian at any given time"), but in practice both curator and deputy are writing concurrently.

## Proposed actions

**1. (Done — infrastructure, not schema) `.gitattributes` union merge for log.md.** Added `log.md merge=union`. Git now auto-combines both sides' appended entries instead of conflicting. Safe because log.md is append-only — entries never rewrite existing lines. This is the mechanical fix; it required no CLAUDE.md change but is recorded here for visibility/veto.

**2. (Proposed — CLAUDE.md §5.1 logging-format edit) Author tag in the entry header.** Extend the header format with the author's entity slug:

```
## [YYYY-MM-DD HH:MM] <operation> | <scope> | <author-slug>
```

e.g. `## [2026-06-12 09:40] curation | ims-enrolment sign-off sheet | jehad-altoutou`. Mirrors `captured_by:` at the log layer; makes concurrent-author history legible and union-merged entries attributable. Backfill on-touch, not retroactive.

## Considered and rejected

**Merging all same-day entries into one per-day block (per author).** Rejected: a shared "today" block both authors edit concentrates writes onto the same lines and *increases* conflict frequency. Discrete appended entries are the merge-friendliest shape; union merge handles the append-append case.

## Open question for Michael

Union-merged entries can land in non-chronological order within the file when both sides push close together (each side's block is kept whole, order depends on merge direction). Acceptable, given timestamps in headers make true order recoverable? If not, the alternative is per-author log files (`log-jehad.md`, `log-michael.md`), a heavier schema change.
