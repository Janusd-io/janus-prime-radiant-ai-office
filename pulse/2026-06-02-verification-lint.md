---
type: pulse
title: "2026-06-02 verification lint — post-v0.14 schema-bump pass"
slug: 2026-06-02-verification-lint
created: 2026-06-02
updated: 2026-06-02
departments: [ai-office]
confidence: high
related: [2026-06-02-lint, claude-md-v0.14-schema-bump-proposal, project-lint-workstream-backlog]
---

# 2026-06-02 verification lint — post-v0.14 schema-bump pass

Fresh lint immediately following the CLAUDE.md v0.13 → v0.14 bump. Verification mode: confirm the new schema lints cleanly against current vault state, surface anything still mismatched, set the carry-forward for the *next* (post-v0.14-aware) lint.

**Scope of scan:** ~600 wiki pages; structural checks against new §2 schema; ingest-since-last-lint counter; spot-check of newly-codified rules.

## Headline

**v0.14 schema lints cleanly.** Of the 8 items in the bump, all 8 are now reflected accurately in vault state. The wiki state and the schema match for the first time since ~2026-05-25. Three small residuals remain (all already in carry-forward queue); no surprises.

## §A — Schema vs reality verification (v0.14)

| §2 schema item | Current vault state | Status |
|---|---|---|
| `vendors/` top-level canonical | 124 files | ✓ |
| `people/` top-level canonical | 39 files | ✓ |
| `clients/` top-level canonical | exists (empty as expected) | ✓ |
| `departments/` top-level canonical | exists | ✓ |
| `presentations/` documented | 10+ files | ✓ |
| Legacy `entities/vendors/` deprecated | 8 files (down from 37); all curator-flagged for migration | ⚠️ partial — 8 unmigrated files; not blocking |
| Legacy `entities/people/` deprecated | 6 files (diana-hu, tom-blomfield, garry-tan, karpathy, vivian-balakrishnan, yusuf-apple-dubai) | ⚠️ partial — 6 unmigrated; not blocking |
| §4 frontmatter — attribution field | Schema documented; backfill on-touch | ✓ schema present; backfill begins now |
| §5.1 — inbox dedupe + .processed/ pattern | Codified; this session's 2026-06-02 batch ingest followed the pattern | ✓ |
| §5.3 step 8 — frontmatter-status escalation check | Documented; methodology defect resolved | ✓ documentation only — lint script needs update if/when a script exists |
| §5.3 — Carry-forward convention | Documented as load-bearing | ✓ |
| §6 — Memory-system reference convention | Documented; `feedback-*` / `project-*` / `user-*` prefixes accepted-as-broken-by-design | ✓ |
| §5.5 — Curate workflow | Documented as 5th workflow | ✓ — already exercised in this session's curation log entry |

**Three "partial" findings — all already known and queued:**

1. **8 vendor pages remain in `entities/vendors/`** (attio, caddy, cloudflare, cookiebot, cosmic, factset, onecli-agent-vault, vercel — the marketing-stack + AIR-tracked vendors). Per v0.14, these are *accepted-but-deprecated*; the 2026-05-Q2 migration was the *bulk* move and these are stragglers. No urgency — but a future curation pass should reconcile them with their `vendors/` counterparts (some have both — vendors/attio.md AND entities/vendors/attio.md exist; the divergence needs reconciling).

2. **6 people pages remain in `entities/people/`** (the YC partners + Karpathy + Vivian Balakrishnan + Yusuf). Same status — accepted-but-deprecated; bulk migration done; stragglers from before the migration date. Worth a single curation pass to move them.

3. **2 `.tmp` leftover files** from the 2026-06-02 dedupe pass (vendors/claude.md.tmp + vendors/google-cloud.md.tmp). The Cowork sandbox's `mv` had cross-mount permission issues; the .tmp files persist. Trivial `rm vendors/*.tmp` from Michael's vault-directory Claude Code.

## §B — Spot-check verifications

**B.1 — Wikilink retro-updates working.** 14 occurrences of `[[diana-hu]]` / `[[tom-blomfield]]` / `[[garry-tan]]` (with various display aliases) across pulse/, concepts/, briefs/, vendors/. The pages exist; the links resolve. Closes the deferred-to-lint item from the resolved YC-partner escalation.

**B.2 — Vendor-page dedupe stuck.** vendors/claude.md (129 lines, 1 "Merged from" block) and vendors/google-cloud.md (116 lines, 1 "Merged from" block) — both halves of the migration merge are now consolidated. No remaining duplicate sections. The 2026-06-02 lint's §B.2 finding is closed.

**B.3 — Block source secondary URL recorded.** `source_secondary:` field on `sources/articles/2026-03-31-block-from-hierarchy-to-intelligence.md` carries the Dorsey X URL with audit note. The "Dorsey tweet thread" follow-up from the YC pulse is fully closed.

**B.4 — Aging-escalation false-positive cleanup.** All 7 escalations the 2026-06-02 lint flagged as "aging urgent" are confirmed `status: resolved` in frontmatter. New §5.3 check 8 reads frontmatter; next lint will not flag them. Methodology defect from 2026-06-02 lint §B.4 is closed at the rule level.

**B.5 — New inbox items detected.** 2 new files have arrived in `inbox/` since the v0.14 bump: *"Google Search as you know it is over.md"* and *"Google's AI Shift Is Causing a Collective Freak-Out.md"*. **Not in scope for verification lint** — these are normal ingest workload. Flagging for the next session.

**B.6 — Out-of-band ingest detected.** Log shows `## [2026-06-03 12:42] ingest | 2026-06-02-founders-blueprint-agentic-ai-on-aws | meeting / event` — appears to be a standup-skill or Jehad-driven ingest landing after this session's lint timestamp. Date stamp `2026-06-03` is one day ahead of the session's current calendar date; possibly a clock-skew artefact from a separate workstation. **Not a defect — just unusual ordering.** Worth verifying with Jehad in next sync.

## §C — Ingest counter status

Counter since 2026-06-02 lint: **1** (the Jehad founders-blueprint ingest at 12:42). Plus 2 new inbox items pending. Well below §5.3 trigger threshold (10).

## §D — Curation log entry (this session)

This verification lint follows immediately on a curation pass — both the 2026-06-02 lint carry-forward execution (items 2, 3, 7) and the v0.14 schema bump are logged under `## [2026-06-02 14:25] curation`. The new §5.5 Curate workflow was effectively dogfooded by writing it.

## Carry-forward queue for the next lint

Substantially shorter than the 2026-06-02 lint's queue — most items have closed:

1. **Process the 2 new inbox items** (Google Search piece + Google AI shift piece). Normal ingest — both look like Google-competitive-landscape signals that pair with the existing [[2026-05-19-google-io-2026-agents-as-product]] cluster.
2. **8 stragglers in `entities/vendors/`** — reconcile / migrate or document divergent content. Curation work; low priority since v0.14 explicitly accepts the legacy paths.
3. **6 stragglers in `entities/people/`** — same pattern. Especially worth migrating the YC-partner pages so the wikilink resolution is unambiguous.
4. **2 `.tmp` files** in `vendors/`. Trivial `rm` from Michael's vault-directory Claude Code.
5. **Lint-script update for §5.3 step 8** — if there's a script that runs the escalation-aging check, update it to read frontmatter `status:` per v0.14. The rule is in CLAUDE.md but the script may need a code-level change.
6. **Dimon duplicate resolution** — still curator-decision-blocked from 2026-05-25 lint.
7. **Marketing-handoff slug resolution** — still curator-decision-blocked from 2026-05-25 lint.
8. **Fireflies-blocked meeting source** — still external blocker.
9. **Out-of-band timestamp in 2026-06-03 ingest entry** — verify clock-skew with Jehad; if real future-date entries are expected, codify in §5.

**Carry-forward intent:** the next lint should be a *normal mechanical lint*, not a schema-bump-driven one. Items 1, 4 are trivial / micro-task. Items 2, 3 are curation passes that can roll up into one session. Items 5-8 are decision-blocked.

## Notes for the curator

The v0.14 bump is the largest single CLAUDE.md change since v0.10's multi-graph framing. **It closes 4 cycles of compounding "schema vs reality" debt.** From here, lints should run faster — most of the structural gaps are now closed, and the remaining work is content-level (real findings, not methodology defects).

Counter reset: 0 ingests / 0 batch-ingests since this lint.
