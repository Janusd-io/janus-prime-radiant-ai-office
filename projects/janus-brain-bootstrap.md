---
type: project
title: Janus Brain Bootstrap
slug: janus-brain-bootstrap
created: 2026-05-14
updated: 2026-06-09
status: active
owner: jehad-altoutou
captured_by: jehad-altoutou
departments: [ai-office, office-of-ceo]
sources: [2026-05-14-data-management-system-overhaul-meeting, 2026-05-12-aio-andrew-marketing, 2026-05-13-aio-it-meeting, 2026-05-18-michael-jehad-andrew-weekly-meeting]
related: [janus-prime-radiant-build, prime-radiant-instance-setup, prime-radiant-storage-substrate, llm-wiki, standup, jehad-altoutou, michael-bruck, andrew-soane]
---

# Janus Brain Bootstrap

Hub for the `/janus-brain` Claude Code skill — the installer + orchestration layer that turns any Janus employee's laptop + other local Obsidian vaults + Fireflies meetings into their slice of a single dept-shared [[llm-wiki|Prime Radiant]] vault on GitHub. Owned by [[jehad-altoutou]], part of [[michael-bruck]]'s [[janus-prime-radiant-build]] programme.

## Goal

Replace the Drive-era Prime Radiant substrate (decommissioned per [[2026-05-13-github-canonical-prime-radiant-substrate]]) with a Git-backed, one-vault-per-department model where each employee runs `/janus-brain` once and ends up with `~/janus/prime-radiant/` cloned from their dept's repo, per-person content scaffolded at `people/<slug>/`, and meetings rendered in the [[standup]] digest schema. Success = every Janus employee can self-enroll into the canonical 13-dir layout without manual intervention.

## Status — 2026-06-04

- **v0.1.0 production tag cut** (`f91894c`, 2026-06-03). Skill is fleet-pinned: auto-sync prelude resolves the latest `v*` tag on each fire (`git fetch --tags --prune --force`) so admin force-pushes propagate within 12h. Rollback = re-tag old SHA + force-push. `scripts/release.sh` cuts new releases.
- **Production-grade audit complete.** Two audit passes (`AUDIT-2026-06-03.md`, `AUDIT-2026-06-03-REAUDIT.md`) ran in the bootstrap repo. All 10 critical/important findings + 3 re-audit blockers (R1 tag force-fetch, R2 inbox_item queue loop, R5 dept GitHub Team) shipped. Cross-platform file locking (`_filelock.py` — POSIX flock + Windows msvcrt + stale-PID recovery), pre-push gitignore-private guard (`assert-gitignore-private.sh`), sync.lock for fire-overlap, log rotation (5MB → gzipped, keep 6).
- **All capability work merged.** PRs #5 (v2.0 autopilot), #6 (Phase 4.7 inbox sweep), #7 (7-day full coverage), #8 (auto-create dept repo), #9 (HTML + dedup + full-fidelity), #10 (incremental rescan), #11 (audit response). 30+ files added/modified since 2026-06-01.
- **Mass-deploy verdict: GO.** Andrew (macOS, existing) update commands ready; Lysander (Windows, fresh) enrollment 2026-06-04 — first Windows pilot.

## Status — 2026-06-01

- **v2.0 autopilot shipped** — quick mode (5 min) + background fill via twice-daily sync + model routing (haiku/sonnet/opus) for ~70% token reduction. Three modes: `quick` (first run, 30–50k tokens), `background-fill` (per sync fire, 100–150k tokens), `steady-state` (queue drained, 20–50k tokens). Pre-consent config at `~/.config/janus-brain/autopilot.yaml`. PR `feat/v2-autopilot` open against `main`.

## Status — 2026-05-25

- Templates at v1.3.0 on both production (`Janus-com`) and sandbox (`Janusd-io`).
- Two depts enrolled: [[jehad-altoutou]] in [[ai-office]] (sandbox); [[andrew-soane]] in [[marketing]] (production).
- macOS + Windows both production-ready. PowerShell `install.ps1` + Windows Task Scheduler `auto-sync.ps1` cover the Windows surface.
- One known quality gap: entity stubs (`projects/`, `vendors/`, `people/`) ship empty when auto-created — body sections stay placeholder until hand-filled. Phase 6.6 "stub-fill" subagent designed but not built yet.

## Repos

- **Skill installer**: `Janusd-io/janus-brain-bootstrap` — the `/janus-brain` skill code.
- **Production dept template**: `Janus-com/janus-prime-radiant-template` (v1.3.0) — cloned for every new dept enrollment.
- **Sandbox dept template**: `Janusd-io/janus-prime-radiant-template` (v1.3.0) — sandbox parity.
- **Dept clones**: `Janus-com/janus-prime-radiant-<dept>` (production) or `Janusd-io/...` (sandbox).

## Key decisions

This page is a hub — atomic decision records live in `decisions/`. Major calls so far:

- [[2026-05-13-github-canonical-prime-radiant-substrate]] — Drive → Git substrate migration.
- Single-vault rewrite (2026-05-14, `REWRITE-SPEC.md` in the bootstrap repo) — kill the personal-repo + federation model; one local vault per employee.
- Meeting digest schema parity with [[standup]] (2026-05-14) — `/janus-brain` Phase 3.5 mirrors the standup skill's Meeting Intelligence Digest output.
- Sensitivity classifier hard rule (2026-05-14) — canonical OSS public docs (README/SECURITY/CONTRIBUTING/LICENSE/etc.) always `dept`, regardless of repo ownership.
- Transcript siblings dropped (2026-05-15) — `parser_version: 3`; `## Transcript` points at Fireflies URL.
- Notion ingest replaced by local Obsidian-vault ingest (2026-05-20) via `scripts/fetch-obsidian.py`.
- Canonical 13-dir layout amendment (2026-05-22) — walked back from over-pruned v1.0.0 template; restored `lessons/pulse/questions/briefs/entities/inbox/sources/` as canonical alongside the original six.
- Production org is `Janus-com` (2026-05-22) — `Janusd-io` reserved as AI Office sandbox.
- Vault-root `sources/` standardized (2026-05-22) with `articles/meetings/misc/linear/monday/notion/` subfolders; `meetings/` is an auto-emitted wikilink hub embedding canonical per-person meetings.
- **CLAUDE.md v1.4 promotion** (2026-06-01) — promote AIO's mature v0.13 dept rulebook (~510 lines: four-graph framing, three-layer architecture, per-source ingest rules, attribution discipline, brief shape, lint cadence) to the canonical dept template. Genericized via `{{DEPT_DISPLAY}}` / `{{DEPT_SLUG}}` / `{{CURATOR_NAME}}` / `{{CURATOR_SLUG}}` placeholders that `bootstrap-dept-vault.sh` substitutes at enrollment time. Both template repos bumped to v1.4.0 via squash-merged PRs; Andrew's Marketing CLAUDE.md replaced in-place (was the lean v1.3 default, no Marketing customizations to preserve). AIO's own CLAUDE.md is NOT auto-aligned — it's the lead vault and is strictly richer than the generic template.
- **v2.0 autopilot** (2026-06-02) — three-mode architecture: `quick` (5-min enrollment), `background-fill` (twice-daily sync drains 200 items/fire × 14 fires ≈ 7-day full drain), `steady-state` (incremental only). Model routing: haiku for parser/classifier/captions, sonnet for enrichment/stub-fill/translation, opus for orchestration — ~70% token reduction vs all-sonnet. Pre-consent config at `~/.config/janus-brain/autopilot.yaml` (autopilot true by default; user gave full consent). PR #5.
- **Phase 4.7 inbox sweep** (2026-06-02) — Web Clipper drops to `inbox/` auto-promoted to `sources/articles/<slug>.md` with proper frontmatter; swept originals archived to `inbox/.swept/`. Idempotent. PR #6.
- **7-day full coverage** (2026-06-02) — 5 chunks × 40 files = 200 items/fire, `$HOME` scope, 12 file categories (pdf/docx/md/pptx/txt/rtf/odt/key/pages/numbers/xlsx/csv), `.html` added 2026-06-03, 365-day Fireflies horizon, 10k file cap. PR #7.
- **Auto-create dept repo** (2026-06-03) — Phase 2 detects missing `Janus-com/janus-prime-radiant-<dept>` and creates from template + adds curator as collaborator. Sandbox uses `Janusd-io`. Round-2 fix added dept GitHub Team creation so subsequent employees of the same dept inherit access. PRs #8 + #11 (R5).
- **HTML + content-dedup + full-fidelity ingest** (2026-06-03) — `.html` first-class category (preferred over `.pptx` as AI-readable slide alternative); Layer 2a content-sha256 dedup at queue-build time prevents byte-identical re-ingest; explicit "documents ingested in full, never summarized" rule in enrichment subagent prompt + applier guard rejecting manifests with `summary:` key on `sources/articles/`. Meetings keep their structured digest (digest is for meetings only). PR #9.
- **Incremental rescan on every fire** (2026-06-03) — `.state/last-sync.json` tracks per-scope timestamps (laptop / Fireflies / Obsidian / inbox). Each auto-sync pre-call `build-enrollment-queue.py --incremental` so a laptop sleeping for N days catches up on first wake. No data loss from missed fires. PR #10.
- **Production hardening — audit response** (2026-06-03) — `_filelock.py` (cross-platform file locking), `.state/sync.lock` (fire-overlap defense), pre-push `assert-gitignore-private.sh` (block leaked `people/*/private/` content), `auto-sync-prelude.sh` tag-pinning + force-fetch (`git fetch --tags --prune --force`), `scripts/release.sh`, log rotation, second-employee dept-team grant. PR #11.
- **v0.1.0 release** (2026-06-03) — first fleet-pinned baseline tag. Every employee's auto-sync prelude now resolves to `v0.1.0`; rollback procedure documented (`git tag v0.1.0 -f <sha> && git push --tags --force`).
- **Twice-daily auto-sync** (2026-06-01) — replaces the single-fire daily schedule. macOS launchd plist now carries an `<array>` of `<dict>` `StartCalendarInterval` entries; Windows Task Scheduler gets two `-Daily` triggers. Default fires at **12:00 + 17:00 in the employee's LOCAL time** (lunchtime + end-of-day catch-up) — both surfaces interpret against the local clock so Dubai / Singapore / London teammates all get the same shape without timezone config. Override via `install.sh --install-auto-sync --times "HH:MM,HH:MM"` (macOS) or `install.ps1 -InstallAutoSync -Times @('HH:MM','HH:MM')` (Windows). Migration for existing users: `--uninstall-auto-sync && --install-auto-sync`.

## Architecture

The skill operates as 8 phases (Pre-flight → Identity → Bootstrap → Cloud pulls → Laptop walk → Extraction → Enrichment → Apply → Commit-push → Lint+report). Detailed phase contracts in the bootstrap repo's `skills/janus-brain/SKILL.md`. Per-employee content lives at `people/<slug>/` with `sources/`, `meetings/`, `private/` (gitignored), `.config.yaml`, `CLAUDE.md`, `self.md`, `.review-queue.md`. Dept-shared content at the 13 canonical top-level dirs.

Continuous sync runs via Obsidian Git plugin (5-min auto-pull + auto-commit-push). Optional daily catch-up via `auto-sync.sh` (macOS launchd) or `auto-sync.ps1` (Windows Task Scheduler) firing `/janus-brain sync`.

## Open questions

- ~~Empty entity stubs / Phase 6.6 stub-fill subagent~~ — **resolved 2026-06-01** (shipped, production-hardening on real backlog still pending real-world run).
- ~~AIO legacy `entities/internal/external/vendors/` migration~~ — **resolved 2026-06-01** (60 files migrated on Jehad's vault, pushed).
- Phase 6.6 real-world run on Jehad's ~1,500-stub backlog — designed + smoke-tested but not yet fired against the full backlog. Trigger via `/janus-brain sync --backfill-all`.
- Schema-version CI between templates and dept clones — still manual. Worth a GitHub Action when 5+ depts enrolled.
- Cross-dept federation (CEO-tier read-only across N dept repos) — separate skill, deferred per [[2026-05-13-github-canonical-prime-radiant-substrate]] guidance.
- Layer 2b semantic / cross-language dedup — documented in SKILL.md but subagent fields not yet wired. Layer 2a (byte-identical) covers ~80% of dedup needs.

## Cross-references

- [[janus-prime-radiant-build]] — parent programme.
- [[standup]] — sibling skill whose meeting-digest output shape this skill mirrors.
- [[prime-radiant-instance-setup]] — companion runbook for setting up a new instance.
- [[prime-radiant-storage-substrate]] — the brief that decided Git over Drive.
- [[llm-wiki]] — the underlying knowledge-system concept this implements.
- `REWRITE-SPEC.md` + `HANDOVER.md` + `REPORT-2026-05-14-first-run-jehad.md` (in the bootstrap repo) — full forensic + design history.

---

## Full decisions & progress log

_Migrated from Jehad's personal Obsidian vault, 2026-06-09. Detail not previously in this page._

## Key Decisions

- *(2026-05-13)* Migrate substrate from Google Drive → Git on GitHub. Reason: Drive's stream-on-demand sync caused Cowork mount failures; Cross-Workspace identity (`.com` vs `.io`) was broken; Git solved both structurally. Per Michael Bruck's brief.
- *(2026-05-13)* One repo per Prime Radiant instance (dept + personal), federation via curator-mediated `inbox/`. *Superseded same-day by single-vault model below.*
- *(2026-05-14)* **Single-vault rewrite**: kill the separate personal-repo + federation model. Each employee = one local vault = one clone of their dept's GitHub repo. Per-person content lives in `people/<slug>/`. Multiple teammates push to the same dept repo via standard git. Privacy boundary = GitHub Team membership; sensitive items go to gitignored `private/`. See `REWRITE-SPEC.md` in the repo.
- *(2026-05-14)* Meeting notes use the [[standup|/standup]] skill's output schema (Summary / Decisions / Action items / 🎯 This week / 🏔️ Long horizon / Findings / Open questions / Blockers / Tool mentions / Related). Raw transcripts go to a sibling `<slug>.transcript.md` file, never inline.
- *(2026-05-14)* Task-tracker is asked per-employee at enrollment (`monday` / `linear` / `asana` / `notion` / `none` / `other`); action-item formatting adapts. AI Office uses Linear AIP; Marketing likely Notion or Monday. Multi-tracker support shipped in 2.16 fix.
- *(2026-05-14)* Sensitivity classifier (Phase 5 enrichment subagent) with hard rule: canonical OSS public docs (README/SECURITY/CONTRIBUTING/LICENSE/CODE_OF_CONDUCT/CHANGELOG/ARCHITECTURE/INSTALL/USAGE) are ALWAYS `dept`, never `self` or `confidential`. Repo ownership ≠ sensitivity.
- *(2026-05-14)* No org-tier repo for now; deferred to a future read-only "CEO brain" federation skill. Cross-dept items get cross-tagged in originating repo until then.
- *(2026-05-15)* **Transcript siblings killed**: bump `parser_version` 2→3, applier no longer writes `<slug>.transcript.md` next to meeting notes — the `## Transcript` section now points at the Fireflies URL. Shipped one-shot `migrate-v2-to-v3-meetings.py` to retrofit existing vaults (Jehad's: 12 transcripts deleted, 12 meetings re-rendered).
- *(2026-05-15)* **Auto-diagnostic reports**: every enrollment now emits `.last-run-report.md` (brief) + `.last-run-diagnostic-report.md` (forensic, same shape as REPORT-2026-05-14-first-run-jehad.md). Phase 8 gates the `git push` when any `blocker`-severity issue lands in `.state/run-issues.jsonl`.
- *(2026-05-15)* **Multilingual + embedded image pipeline**: extract-content.py uses pandoc `--extract-media` + pdfimages → `_media/<stem>/`; language detection adds `needs_translation: true` for non-English bodies; Phase 5 enrichment subagent translates to English with `## Original (<lang>)` appendix preserving the source; vision-captioned images injected inline as `_Caption: …_`.
- *(2026-05-15)* **Fireflies horizon configurable per enrollee**: Phase 1 asks 30/90/180/365/all (default 180); `limit` raised 30→200 with pagination up to a 500-meeting safety ceiling. Long-tenured staff can pull years of history.
- *(2026-05-15)* **`/standup` skill patched to v3.17**: retargets the daily standup write from legacy `personal/sources/meetings/` to single-vault `people/<slug>/meetings/`. Stops creating ghost paths in the dept repo.
- *(2026-05-22)* **Canonical 13-dir layout amendment**: my initial v1.0.0 template over-pruned (removed lessons/pulse/questions/briefs/entities/inbox/sources). Walked back to the full 13 canonical top-level dirs: `decisions/projects/vendors/concepts/processes/people/lessons/pulse/questions/briefs/entities/inbox/sources/`. `entities/` keeps only `clients/` and `departments/` sub-dirs; `entities/internal/external/vendors/` deprecated (warn-only) in favor of top-level `people/<slug>.md` + `vendors/<slug>.md`. Bumped both templates to v1.2 / v1.2.0.
- *(2026-05-22)* **Production org is `Janus-com`**; `Janusd-io` reserved as AI Office sandbox. Skill default `--org` flipped; `--sandbox` / `JB_SANDBOX=1` opt-in for dev work. Existing `Janusd-io` repos stay where they are.
- *(2026-05-22)* **Vault-root `sources/` standardized** to 6 subfolders: `articles/`, `meetings/`, `misc/`, `linear/`, `monday/`, `notion/`. The `meetings/` subdir is auto-emitted by the applier as a wikilink hub — each stub embeds the canonical per-person meeting via `![[…]]` for dept-wide browsability. Bumped both templates to v1.3.0.
- *(2026-05-22)* **Windows production-ready**: `install.ps1` + `auto-sync.ps1` + `install.cmd` ship; PowerShell-native install + Windows Task Scheduler auto-sync; bash scripts execute under Git Bash; Python scripts are platform-aware via `Path.home()` + `sys.platform` branches. ENROLLMENT.md has a top-of-doc Windows section.
- *(2026-06-02)* **v2.0 autopilot architecture** (PR #5): three-mode skill — `quick` (~5-min enrollment, 30–50k tokens), `background-fill` (twice-daily sync drains ~200 items/fire × 14 fires ≈ 7-day backlog drain), `steady-state` (incremental only). Pre-consent config at `~/.config/janus-brain/autopilot.yaml` (autopilot true by default — full consent given). Model routing: haiku (parser/classifier/captions), sonnet (enrichment/stub-fill/translation), opus (orchestration) → ~70% token reduction. Work queue at `.state/enrollment-queue.jsonl`. Layer A pre-sync hook auto-pulls bootstrap repo before each fire.
- *(2026-06-02)* **Phase 4.7 inbox sweep** (PR #6): Web Clipper drops to `inbox/` auto-promoted to `sources/articles/<slug>.md` with proper frontmatter; swept originals archived to `inbox/.swept/`. Calls inbox-sweep subagent (haiku) per item — ~5-10k tokens per fire at 20 items.
- *(2026-06-02)* **7-day full coverage** (PR #7): defaults raised to 5 chunks × 40 files = 200 items/fire; scope broadened from `~/Documents` → `$HOME` (with `laptop_exclude_dirs` for Library/Trash/cache/media); 12 file categories (pdf/docx/md/pptx/txt/rtf/odt/key/pages/numbers/xlsx/csv); 365-day Fireflies horizon; 10k file cap. `target_drain_days: 7` in config.
- *(2026-06-03)* **Auto-create dept repo** (PRs #8 + #11): Phase 2 detects missing `Janus-com/janus-prime-radiant-<dept>` and creates from template + adds curator as collaborator + creates `Janus-com/<dept>` GitHub Team so subsequent dept employees inherit access. Falls back to per-user collaborator on org-admin 403.
- *(2026-06-03)* **HTML + content-dedup + full-fidelity ingest** (PR #9): `.html` first-class category (preferred over `.pptx` as AI-readable slide alternative); Layer 2a content-sha256 dedup at queue-build time (`.state/content-fingerprints.json`) prevents byte-identical re-ingest; **explicit "documents ingested in full, never summarized" rule** — enrichment subagent prompt forbids summary; applier guard rejects manifests with `summary:` key on `sources/articles/` and `people/<slug>/sources/laptop/`. Meetings keep the structured digest (digest is for meetings only).
- *(2026-06-03)* **Incremental rescan on every fire** (PR #10): `.state/last-sync.json` tracks per-scope timestamps (laptop / Fireflies / Obsidian / inbox). Each auto-sync pre-calls `build-enrollment-queue.py --incremental` so a laptop sleeping for N days catches up on first wake. No data loss from missed fires.
- *(2026-06-03)* **Two-pass production audit + hardening** (PR #11): `AUDIT-2026-06-03.md` (10 findings) + `AUDIT-2026-06-03-REAUDIT.md` (3 follow-on blockers R1/R2/R5). All fixed. New `_filelock.py` (cross-platform file locking — POSIX flock + Windows msvcrt + stale-PID recovery), `.state/sync.lock` (fire-overlap defense), pre-push `assert-gitignore-private.sh` (block leaked `people/*/private/` content), `auto-sync-prelude.sh` tag-pinning with `git fetch --tags --prune --force` (rollback propagates fleet-wide), `scripts/release.sh`, log rotation (5MB → gzipped, keep 6), `inbox_item` queue-loop closed, dept GitHub Team creation.
- *(2026-06-03)* **v0.1.0 released** — first production-pinned tag. `./scripts/release.sh v0.1.0 "Production baseline — audit-hardened"`. Every employee's next auto-sync fire (within 12h) pins to this baseline.
- *(2026-06-04)* Lysander (PM lead, Windows) enrollment day — first fresh-employee Windows pilot. Andrew (Marketing, macOS) update commands ready to migrate from pre-v0.1.0 state.

## Blockers / Open Questions

- [x] ~~Empty entity stubs~~ — **resolved 2026-06-01**: Phase 6.6 stub-fill subagent shipped (commit `c5d6634`). `apply-stub-enrichment.py` + `prompts/stub-fill-subagent.md` ship; orchestrator detects new stubs via `.state/new-stubs-this-run.jsonl`; up to 20 fill subagents per batch. Cost-bounded to current-run stubs by default; `--backfill-all` opt-in for retroactive fill.
- [x] ~~AIO legacy `entities/internal/external/vendors/`~~ — **resolved 2026-06-01**: `migrate-legacy-entities.py` shipped (commit `c5d6634`); ran live on Jehad's AIO vault — 60 files migrated (15 internal + 1 external + 41 vendors merged), 0 stale wikilinks (vault was already slug-form). Pending: final `git push` from `~/janus/prime-radiant/` to publish to the dept repo.
- [ ] Phase 6.6 needs a real-world run — built + unit-tested, but hasn't fired on Jehad's or Andrew's actual ~1,500 stub backlog yet. Trigger via `/janus-brain sync` (or `--backfill-all` for full sweep with token-cost decision).
- [ ] Schema-version CI between templates and dept clones — still manual; worth a GitHub Action.
- [ ] Cross-dept CEO-tier federation skill — deferred (out of current scope).
- [ ] Layer 2b semantic / cross-language dedup — documented in SKILL.md but subagent fields not yet wired. Layer 2a (byte-identical) covers ~80%.
- [ ] PowerShell `.ps1` runtime parse-check on a real Windows machine — Lysander's enrollment 2026-06-04 is the first live test. Will catch any syntax surprise.
- [ ] 4 peripheral JSONL appenders still use plain append (sub-PIPE_BUF atomic on POSIX — safe in practice but not under explicit lock).

## Progress Log

- *(2026-05-12)* Initial Google-Drive-based skill shipped. Real-data run by Jehad surfaced sync failures.
- *(2026-05-13)* Substrate migration to Git on GitHub. Personal-template repo created. First end-to-end enrollment ran for Jehad (507 files in personal vault, 121 items federated to AIO inbox).
- *(2026-05-14)* **First-pass rewrite**: single-vault architecture replacing personal+dept split. 5 commits on `rewrite/single-vault-2026-05-14`. Merged to main, installed.
- *(2026-05-14)* **First end-to-end rerun on Jehad's vault** produced a 1,793-file local commit (not pushed). Surfaced 18 issues — see `REPORT-2026-05-14-first-run-jehad.md` in the repo.
- *(2026-05-14)* **Second-pass fixes**: 12+ commits on `rewrite/post-first-run-fixes-2026-05-14` addressing all P0/P1/P2/P3 items + every §3 gap from the report.
- *(2026-05-15)* Fix branch merged to main; install.sh re-run; bootstrap repo pushed to GitHub. v2→v3 meeting migration ran cleanly on Jehad's vault. Obsidian Git push/pull stale-lock errors diagnosed + resolved. `/standup` skill patched to v3.17 (legacy paths eliminated).
- *(2026-05-20)* **Notion ingestion replaced by Obsidian-vault ingestion**: skill now reads from any *other* local Obsidian vault the user has registered (via `scripts/fetch-obsidian.py`). Notion ingest deprecated.
- *(2026-05-22)* Andrew enrolled on his laptop (Marketing). Output landed in `Janus-com/janus-prime-radiant-marketing` (correct org, since Janus-com is production). Surfaced template drift (v0.9.0 inherited stuff still in his repo) → ran walk-back to restore canonical 13 dirs and bumped both templates to v1.3.0. Andrew's repo brought in line + new sources schema added.
- *(2026-05-22)* Windows readiness audited. `install.ps1` shipped. Marketing repo standardized. Auto-emitted `sources/meetings/` wikilink hub wired into applier.
- *(2026-05-25)* Status: 23+ commits on main, both template repos at v1.3.0, Windows + macOS production-ready, Andrew running on the latest skill. Empty-stub enrichment is the one remaining quality issue blocking "full" production polish.
- *(2026-06-01)* **CLAUDE.md v1.4 promotion shipped.** AIO's mature v0.13 rulebook (~510 lines, four-graph framing, three-layer architecture, per-source ingest rules, attribution discipline, brief shape, lint cadence) genericized via `{{DEPT_DISPLAY}}` / `{{DEPT_SLUG}}` / `{{CURATOR_NAME}}` / `{{CURATOR_SLUG}}` placeholders, shipped as `templates/dept-claude-md.template.md` in the bootstrap repo, and pushed to both `Janus-com` and `Janusd-io` template repos (TEMPLATE-VERSION → 1.4.0, squash-merged PRs #3 and #4). `bootstrap-dept-vault.sh` extended to substitute the placeholders at enrollment time. Andrew's `Janus-com/janus-prime-radiant-marketing` CLAUDE.md replaced in place (3,977 B → 43,424 B). Jehad's AIO vault NOT touched — it's the source we promoted from.
- *(2026-06-01)* **Auto-sync now twice-daily at 12:00 + 17:00 LOCAL time.** macOS launchd plist gained an `<array>` of `<dict>` `StartCalendarInterval` entries; Windows Task Scheduler gets two `-Daily` triggers; both surfaces interpret times against the LOCAL clock so Dubai / Singapore / London / etc. all get sync at their own lunchtime + EOD with zero timezone config. `install.sh --install-auto-sync` now defaults to twice-daily; legacy `--time HH:MM` still accepted (back-compat); new `--times "HH:MM,HH:MM"` for custom schedules. `install.ps1 -InstallAutoSync` defaults to `@('12:00','17:00')`; `-Times` accepts an array; legacy `-Time` still accepted. Existing users migrate via `--uninstall-auto-sync && --install-auto-sync`.

