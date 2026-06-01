---
type: project
title: Janus Brain Bootstrap
slug: janus-brain-bootstrap
created: 2026-05-14
updated: 2026-06-01
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
- **Twice-daily auto-sync** (2026-06-01) — replaces the single-fire daily schedule. macOS launchd plist now carries an `<array>` of `<dict>` `StartCalendarInterval` entries; Windows Task Scheduler gets two `-Daily` triggers. Default fires at **12:00 + 17:00 in the employee's LOCAL time** (lunchtime + end-of-day catch-up) — both surfaces interpret against the local clock so Dubai / Singapore / London teammates all get the same shape without timezone config. Override via `install.sh --install-auto-sync --times "HH:MM,HH:MM"` (macOS) or `install.ps1 -InstallAutoSync -Times @('HH:MM','HH:MM')` (Windows). Migration for existing users: `--uninstall-auto-sync && --install-auto-sync`.

## Architecture

The skill operates as 8 phases (Pre-flight → Identity → Bootstrap → Cloud pulls → Laptop walk → Extraction → Enrichment → Apply → Commit-push → Lint+report). Detailed phase contracts in the bootstrap repo's `skills/janus-brain/SKILL.md`. Per-employee content lives at `people/<slug>/` with `sources/`, `meetings/`, `private/` (gitignored), `.config.yaml`, `CLAUDE.md`, `self.md`, `.review-queue.md`. Dept-shared content at the 13 canonical top-level dirs.

Continuous sync runs via Obsidian Git plugin (5-min auto-pull + auto-commit-push). Optional daily catch-up via `auto-sync.sh` (macOS launchd) or `auto-sync.ps1` (Windows Task Scheduler) firing `/janus-brain sync`.

## Open questions

- Empty entity stubs need a Phase 6.6 stub-fill subagent that reads backlinking sources and synthesizes a real body for each newly-created stub. Logged but not yet built. Cost: one subagent per new stub; scoped to current-run stubs only.
- 75 files in legacy `entities/internal/external/vendors/` paths in the AIO vault — migration script designed but not shipped. Lint warns rather than fails.
- Schema-version CI between templates and dept clones — currently manual.
- Cross-dept federation (CEO-tier read-only across N dept repos) — separate skill, deferred per [[2026-05-13-github-canonical-prime-radiant-substrate]] guidance.

## Cross-references

- [[janus-prime-radiant-build]] — parent programme.
- [[standup]] — sibling skill whose meeting-digest output shape this skill mirrors.
- [[prime-radiant-instance-setup]] — companion runbook for setting up a new instance.
- [[prime-radiant-storage-substrate]] — the brief that decided Git over Drive.
- [[llm-wiki]] — the underlying knowledge-system concept this implements.
- `REWRITE-SPEC.md` + `HANDOVER.md` + `REPORT-2026-05-14-first-run-jehad.md` (in the bootstrap repo) — full forensic + design history.
