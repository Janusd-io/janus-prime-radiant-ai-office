---
type: lesson
slug: 2026-06-05-janus-brain-enrollment-hardening-memory
title: "Janus Brain enrollment hardening memory"
created: 2026-06-05
updated: 2026-06-05
captured_by: codex
audience: org
sensitivity: dept
tags: [janus-brain, enrollment, windows, macos, headless-sync, multi-agent, obsidian, lessons]
related: [janus-brain-bootstrap, office-of-ceo, prime-radiant, 2026-06-04-windows-enrollment-postmortem]
---

# Janus Brain enrollment hardening memory

This note captures the decisions, implementation work, CEO validation findings,
known risks, and next steps from the June 2026 hardening pass on
`Janusd-io/janus-brain-bootstrap`.

## Executive summary

The enrollment system is ready for controlled new enrollments. Use the GUI for
the initial `/janus-brain` foreground run, then use Claude CLI headless
auto-sync for background ingestion. Do not use the legacy GUI auto-sync path
unless explicitly forced as a temporary fallback.

The Office of CEO Windows update confirmed the current design works: install
verification passed, GitHub/Claude CLI auth worked, Fireflies/Google Drive/Slack
were visible to Claude CLI, the extraction toolchain was present, the vault was
clean, headless auto-sync was scheduled, and a verifying `/janus-brain sync`
exited `0`.

The same CEO update also found real upstream bugs. The critical ones have now
been fixed in `main`, especially queue self-poisoning, stale enrichment manifest
replay, person detection for headless sync, installer backup placement, and
Windows Tesseract detection.

## Operating decision

Use:

```text
/janus-brain
```

Do not tell employees to run `/janus-brain autopilot`. Autopilot is already the
default through `~/.config/janus-brain/autopilot.yaml`; the documented skill
trigger is `/janus-brain`.

Run split:

- Initial enrollment: Claude Desktop / Claude Code GUI, `/janus-brain`.
- Ongoing background ingestion: Claude CLI headless sync installed by
  `install.sh --install-auto-sync` or `install.ps1 -InstallAutoSync`.
- Legacy GUI auto-sync: fallback only, because it can steal focus and can skip
  while the employee is active.

## Why this direction

The original CEO enrollment took about 2.5 hours on Windows and required too
many approvals and manual interventions. The system needed to become:

- Cross-platform for Mac and Windows.
- Less prompt-heavy during enrollment.
- Capable of installing/checking missing dependencies.
- Resumable after laptop sleep, leave, or missed scheduled fires.
- Able to catch up after long offline gaps.
- Able to observe failures and leave durable history.
- Able to evolve the Obsidian brain over time instead of only ingesting data.
- Safer around private/confidential data.
- Easier to audit from logs and vault state.

The adopted design is a layered runtime:

```text
orchestrator -> specialist agents -> JSON manifests -> deterministic appliers -> lint/health gate -> commit/push
```

Agent memory lives in the vault, not chat history.

## Implemented commits

- `57816a8` — Harden pandas setup for Windows enrollment.
- `bd074e9` — Fix Windows enrollment postmortem issues.
- `88687be` — Harden general enrollment bootstrap and sync.
- `c62c019` — Add living brain evolution loop.
- `fe8543b` — Add macOS headless auto-sync parity.
- `3f278fb` — Implement multi-agent orchestration layer.
- `ac3b9c5` — Add specialist agent ledger records.
- `cc0d714` — Tighten headless sync parity.
- `68b6322` — Upstream CEO Windows sync fixes.

## What changed

### Installer and prerequisites

- macOS installer checks Homebrew and installs/verifies `python@3.12`, `gh`,
  `pandoc`, Poppler/PDF tools where available, Tesseract, and
  `pandas/openpyxl`.
- Windows installer uses PowerShell/winget for Git, GitHub CLI, Python 3.12,
  Pandoc, Tesseract, and verifies `pandas/openpyxl`.
- Windows `python3` shim support was hardened so Bash-based skill scripts can
  run under Git Bash.
- Tesseract detection on Windows now probes the default UB-Mannheim paths after
  winget and PATH refresh, avoiding false missing-tool warnings.
- Installer backups now live under `~/.claude/skill-backups/` instead of
  `~/.claude/skills/janus-brain.bak`, preventing Claude from loading a backup
  copy as a duplicate skill.

### Enrollment command and mode

- `/janus-brain` is the canonical initial enrollment command.
- Autopilot is default via `autopilot.yaml`.
- `/janus-brain sync` is the ongoing sync command used by scheduled headless
  fires.
- `/janus-brain status` remains the health check.

### Mac and Windows background sync

- macOS and Windows now prefer Claude CLI headless sync for scheduled runs.
- Scheduled sync does not drive Claude Desktop, does not steal focus, and does
  not idle-skip when the employee is using the laptop.
- GUI AppleScript/SendKeys auto-sync remains opt-in fallback only.
- Headless wrappers check `claude mcp list` and log connector/auth failures
  instead of failing silently.
- Headless wrappers auto-detect `JB_PERSON` from the single
  `people/<slug>/` subtree when the environment variable is unset.
- macOS launchd template was tightened and validates after rendering.
- Windows scheduled task uses headless `headless-sync.ps1` by default when
  Claude CLI exists.

### Queue and catch-up

- The first run builds a queue instead of trying to ingest everything
  foreground.
- Background fires process bounded slices.
- Every fire does an incremental rescan before claiming work.
- Per-scope timestamps live in `.state/last-sync.json`.
- If an employee laptop is off for weeks, the next fire computes catch-up or
  recovery mode and scans from the last successful timestamps.
- Stale `in_progress` queue records are reclaimed after interrupted runs.
- Queue records include pending, in-progress, done, skipped, and failed state.

### Queue self-poisoning fix

The CEO update found the queue builder could scan the Prime Radiant vault and
the `janus-brain-bootstrap` repo into the enrollment queue when walking the
home directory. That produced a slice that was mostly junk and could re-ingest
the brain into itself.

Fixed in `68b6322`:

- `build-enrollment-queue.py` prunes the Prime Radiant vault root.
- It prunes the bootstrap clone path.
- It honors configured `scope.laptop_exclude_dirs`.
- It does not globally exclude OneDrive/Google Drive roots, because general
  enrollment should include those unless a specific employee config excludes
  them.

### Multi-agent layer

Agent contracts were added under `skills/janus-brain/agents/`:

- enrollment orchestrator
- source discovery
- extraction
- sensitivity classifier
- meeting intelligence
- graph linker
- evolution
- remediation recommendation
- health QA

The orchestrator decides which specialists to run. It should not blindly spawn
all agents every time.

### Agent ledger

Durable multi-agent run memory was added:

- `.state/agent-ledger.jsonl`
- `.state/agent-ledger-summary.json`

Scripts now append records for:

- queue/source discovery
- inbox sweep
- meeting digest apply
- enrichment/classification apply
- graph backlinks
- wikilink stub creation
- stub enrichment
- evolution candidate scans
- remediation candidate scans
- orchestrator claim/complete events

Each record captures found, processed, skipped, failed, remaining, reason, and
status. This is the foundation for answering: "What did the brain miss while
the laptop was offline?"

### Evolution loop

The living-brain evolution scanner now produces:

- `.state/evolution-candidates.json`
- `pulse/YYYY-MM-DD-evolution-candidates.md`

It looks for open questions, orphans, weak sources, empty stubs, and decision
edge gaps. The goal is to prevent knowledge from staying orphaned,
unenriched, and unorganized.

### Remediation loop

The remediation scanner now reads queue failures and run issues, then writes:

- `.state/remediation-candidates.json`
- `pulse/YYYY-MM-DD-remediation-candidates.md`

The scanner classifies likely safe automatic actions versus manual escalation.
Automatic remediation is intentionally bounded; it should not silently do
dangerous operations.

### Enrichment manifest replay fix

The CEO update found stale enrichment manifests could be replayed by later
fires. This caused already-published docs to be moved incorrectly.

Fixed in `68b6322`:

- `apply-enrichment-digests.py` archives successfully applied `chunk_*.json`
  files under `<ingest-dir>/.processed/<timestamp>/`.
- Later fires will not re-glob and replay those manifests.

### Privacy and sensitivity

Current behavior:

- Sensitivity classifier routes `self`, `confidential`, and low-confidence
  items to `people/<slug>/private/`.
- `private/` is gitignored.
- Review queue is gitignored.

CEO incident:

- Obsidian Git auto-push raced the classifier and pushed pre-classification
  confidential intermediate states to git history.
- HEAD was cleaned, but historical commits remain visible to repo readers.
- Owner decision for CEO repo: leave the historical leak as-is.

Design lesson:

- Future architecture should classify before content lands on a committable
  path, or pause Obsidian Git auto-push during a sync fire.

## CEO current status

As of the CEO update report:

- Existing Office of CEO vault was reused, not wiped.
- Install verification passed.
- GitHub auth was good.
- Claude CLI auth was good.
- Fireflies, Google Drive, and Slack were visible to Claude CLI.
- Asana, Calendar, Gmail, Notion, monday, Linear, Figma, Canva needed auth but
  were not required by Janus Brain.
- `pdftotext`, `pandoc`, `pandas/openpyxl`, and Tesseract OCR were available.
- Vault was clean and in sync.
- Headless auto-sync was scheduled at 12:00 and 17:00 local.
- Verifying `/janus-brain sync` exited `0`.
- Queue after cleanup: 955 pending, 0 in progress, 204 done, 0 failed, 1,228
  skipped.
- Expected drain: about 5 fires / 2.5 days.
- Lint had 14 errors and 9 warnings, 0 blockers; reported as pre-existing.

Interpretation: the CEO enrollment is operational, but his machine should pull
`68b6322` so the local CEO-only queue-builder patch becomes upstreamed and
survives future reinstalls.

## New employee enrollment runbook

macOS:

```bash
gh repo clone Janusd-io/janus-brain-bootstrap ~/Documents/janus-brain-bootstrap
cd ~/Documents/janus-brain-bootstrap
git pull
./install.sh
./install.sh --check
./install.sh --install-auto-sync
```

Then in Claude Desktop / Claude Code GUI:

```text
/janus-brain
```

Windows PowerShell:

```powershell
gh repo clone Janusd-io/janus-brain-bootstrap "$env:USERPROFILE\Documents\janus-brain-bootstrap"
cd "$env:USERPROFILE\Documents\janus-brain-bootstrap"
git pull
.\install.ps1
.\install.ps1 -Check
.\install.ps1 -InstallAutoSync
```

Then in Claude Desktop / Claude Code GUI:

```text
/janus-brain
```

Watch during the first few enrollments:

- `gh auth status`
- `claude mcp list`
- Fireflies visibility
- `.state/run-issues.jsonl`
- `.state/agent-ledger-summary.json`
- `.state/last-status.json`
- headless sync logs
- no private files staged for commit

## CEO update runbook

For an already-enrolled CEO machine, do not rerun full enrollment from zero.
Update and verify:

macOS:

```bash
cd ~/Documents/janus-brain-bootstrap
git pull
./install.sh
./install.sh --check
./install.sh --install-auto-sync
./install.sh --auto-sync-status
claude mcp list
```

Windows:

```powershell
cd "$env:USERPROFILE\Documents\janus-brain-bootstrap"
git pull
.\install.ps1
.\install.ps1 -Check
.\install.ps1 -InstallAutoSync
.\install.ps1 -AutoSyncStatus
claude mcp list
```

Then run:

```text
/janus-brain status
/janus-brain sync
```

Only rerun full `/janus-brain` if the vault is missing or unrecoverable.

## Known open risks

### Fireflies headless ingestion

Claude CLI showed Fireflies connected on the CEO machine, but the verifying fire
deferred Fireflies. The next scheduled fires need to prove meeting parsing works
headlessly with a small cap such as 10 meetings per fire.

### Obsidian Git race

The biggest privacy design gap is the race between Obsidian Git auto-push and
classification. Future design should either:

- classify into a staging/private area before any committable path exists; or
- pause/lock Obsidian Git auto-push while a sync fire is running; or
- use a separate staging branch/worktree and merge only classified output.

### Release hygiene

`main` carries important unreleased fixes beyond tag `v0.1.5`. Cut a
`v0.1.6` tag after the current hardening commits so enrollees can pin to a
known version.

### Full stress test

Build a real stress harness:

```bash
./scripts/stress-enrollment.sh --platform mac
```

```powershell
.\scripts\stress-enrollment.ps1 -Platform windows
```

The harness should simulate:

- missing tools
- missing auth
- offline gap / stale timestamps
- laptop vault self-poisoning
- bootstrap repo self-poisoning
- stale manifests
- private/confidential routing
- Obsidian Git race conditions
- Fireflies unavailable
- queue crash/recovery
- duplicate content by hash

Expected assertions:

- no vault/bootstrap files are queued
- stale manifests do not replay
- private files are not staged
- failed items produce remediation candidates
- agent ledger captures each specialist scope
- queue drains across fires
- status snapshot is written

### UTF-8 consistency

The CEO report mentioned cp1252-related Windows read issues. Many scripts
already use explicit UTF-8, but a full audit should replace remaining implicit
reads/writes with `encoding="utf-8"` or `errors="replace"` where appropriate.

### Config knobs to upstream

Consider first-class config support for:

- `scope.include_recurring_meetings`
- `scope.confidential_never_delete`

Default recommendation:

- recurring meetings: false unless owner wants full coverage
- confidential never delete: true; relocate to private rather than delete

## Current readiness judgment

Ready for controlled new enrollments.

Do not enroll the entire company in one batch yet. Enroll 2-3 more employees
with close monitoring, then widen rollout once:

- Fireflies headless parsing is proven.
- No queue self-poisoning appears.
- No stale-manifest replay appears.
- No private files are pushed.
- Headless sync runs at least two scheduled fires without manual intervention.

## Source of truth files

Repository:

- `README.md`
- `ENROLLMENT.md`
- `HANDOVER.md`
- `skills/janus-brain/SKILL.md`
- `skills/janus-brain/scripts/build-enrollment-queue.py`
- `skills/janus-brain/scripts/process-queue-slice.py`
- `skills/janus-brain/scripts/apply-enrichment-digests.py`
- `skills/janus-brain/scripts/headless-sync.sh`
- `skills/janus-brain/scripts/headless-sync.ps1`
- `install.sh`
- `install.ps1`

Vault state:

- `.state/enrollment-queue.jsonl`
- `.state/last-sync.json`
- `.state/agent-ledger.jsonl`
- `.state/agent-ledger-summary.json`
- `.state/run-issues.jsonl`
- `.state/last-status.json`
- `pulse/*-evolution-candidates.md`
- `pulse/*-remediation-candidates.md`

## Human prompt for future CEO update

```text
Update the existing Janus Brain enrollment to the latest version.

1. Find the local janus-brain-bootstrap repo in Documents.
2. Pull latest changes from GitHub.
3. Re-run the installer for this OS.
4. Verify install.
5. Install or refresh headless auto-sync.
6. Check Claude CLI auth/MCP visibility.
7. Run /janus-brain status.
8. Run /janus-brain sync once if status is healthy.
9. Show the final health summary and any issues from:
   - .state/run-issues.jsonl
   - .state/agent-ledger-summary.json
   - headless-sync logs

Important:
- Do not wipe the existing vault.
- Do not rerun full enrollment unless the vault is missing.
- Use the existing vault at ~/janus/prime-radiant or %USERPROFILE%\janus\prime-radiant.
- If auth/login is required, prompt clearly.
- If anything fails, show the exact command and error.
```
