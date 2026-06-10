---
type: question
title: Aging-escalation triage (2026-06-02) — methodology defect, not real aging
slug: aging-escalation-triage-2026-06-02
created: 2026-06-02
updated: 2026-06-09
departments: [ai-office]
status: resolved
owner: michael-bruck
related: [2026-06-02-lint, 2026-05-25-lint, project-lint-workstream-backlog]
---

# Aging-escalation triage (2026-06-02)

The 2026-06-02 lint flagged 7 ingest escalations as ">14 days old, aging." On spot-check, **all 7 are already marked `status: resolved` in their frontmatter**. The aging warning is a **methodology defect in the lint check, not a real backlog** — the lint detects "active escalations" by *file presence in `questions/`* rather than by reading the `status:` field.

## The 7 false-positive escalations

| Escalation | Frontmatter status | Resolution recorded | Action needed |
|---|---|---|---|
| `ingest-2026-05-06-2300-new-project-hubs-from-monday.md` | `resolved` | Title carries "(resolved)" suffix | None — already resolved |
| `ingest-2026-05-06-2301-cowork-approval-governance-process.md` | `resolved` | Title carries "(resolved)" suffix | None — already resolved |
| `ingest-2026-05-11-standup-skill-dual-write-to-aio-inbox.md` | `resolved` | Standup skill v3.14+ shipped per 2026-05-21 lint | None — already resolved |
| `ingest-2026-05-12-1545-openai.md` | `resolved` | `vendors/openai.md` exists; substantively updated 2026-06-02 with Brockman/Codex section | None — already resolved |
| `ingest-2026-05-12-1530-mnemon.md` | `resolved` | "Defer as designed" — no second source surfaced; coverage via [[2026-05-12-mnemon-llm-supervised-memory]] | None — already resolved |
| `ingest-2026-05-14-lysander-liu-and-spike-zhao.md` | `resolved` | Both `people/lysander-liu.md` and `people/spike-zhao.md` exist | None — already resolved |
| `ingest-2026-05-15-joyce-woo.md` | `resolved` | `people/joyce-woo.md` exists | None — already resolved |

**No real action items.** All 7 are correctly resolved; only the lint detection methodology needs fixing.

## The methodology defect

The lint script currently runs something like:
```
ls questions/ingest-*.md | filter mtime > 14 days
```

It should run:
```
ls questions/ingest-*.md | filter frontmatter[status] == active | filter mtime > 14 days
```

**Two-line fix in whatever script runs §B.4 of the lint pulse.** Worth doing before the next lint to avoid the same false-positive cluster surfacing again.

## Process question for Michael

Two options for handling resolved questions/ pages going forward:

**(A) Keep resolved pages in questions/** (current state), fix the lint check to read frontmatter. Pro: preserves the question-shape audit trail in one folder; con: questions/ folder grows without bound; lint check needs to be smarter.

**(B) Move resolved pages to a `questions/resolved/` subfolder** (or similar). Pro: questions/ at the top level becomes a clean "open questions" surface; con: structural change; resolution-action becomes a multi-step process (update frontmatter + move file).

**Recommendation: (A)** — fix the lint check rather than change the folder structure. The status-in-frontmatter pattern is the wiki convention for every other type (project, decision, lesson); applying it consistently to questions/ matches that convention. The lint check is a script-level fix, not a schema-level change.

## Carry-forward for the next lint

- Add to the 2026-06-02-lint carry-forward queue: **lint methodology fix — escalation-aging check must read frontmatter `status` field, not just file presence**. Promote priority.
- After the methodology fix lands, the *real* aging-escalation count is **2 items** (the questions Michael surfaced 2026-06-02 in the resolution of the YC-partner question — none currently aging, both within 14d window).

## Summary for standup

**Disposition:** All 7 escalations in the lint report are false positives — already resolved. No action needed beyond a one-line lint-script fix to read `status:` from frontmatter. The "urgent" priority in the 2026-06-02 lint can be downgraded.

The substantive question for Michael's standup: do we adopt option (A) (fix the check) or option (B) (move resolved pages out of questions/)? Recommended (A).

---

## Resolution (2026-06-09)

**Resolved — both parts settled.**

1. **The 7 false positives:** confirmed already-resolved; no action was ever needed (the lint had mis-detected them).
2. **The methodology defect (the real ask):** **fixed in CLAUDE.md v0.14**, item (5) — *"Lint methodology fix in §5.3 step 8 — escalation-aging check reads frontmatter `status:` field, not file presence."* This is exactly the two-line fix this triage requested.
3. **Process question (Option A vs B):** **Option A adopted** (fix the check, keep resolved pages in `questions/` with status-in-frontmatter as the canonical signal) — now codified in CLAUDE.md §5.3 step 8 and the §5.3-check-8 lint rule (*"Status-in-frontmatter is canonical; file presence alone is not the trigger"*).

**How / who:** approved by **Michael Bruck** in the **2026-06-02 standup** as part of the v0.14 schema bundle (see [[claude-md-v0.14-schema-bump-proposal]], status: resolved — *"All 8 items approved as proposed"*); executed in the v0.13 → v0.14 curation pass. Solution lives in `CLAUDE.md` §5.3 step 8.
