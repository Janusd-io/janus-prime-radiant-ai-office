---
type: question
title: "Sandbox evaluation of obsidian-headless — feasibility for in-container Prime Radiant"
slug: sandbox-eval-obsidian-headless
created: 2026-06-10
updated: 2026-06-10
departments: [ai-office]
status: active
owner: michael-bruck
related: [nanoclaw, nanoclaw-prime-radiant-wiring, prime-radiant-storage-substrate, per-instance-curator-role, 2026-04-22-per-user-data-control-hard-requirement-agent-platforms, jehad-altoutou]
---

# Sandbox evaluation of obsidian-headless — feasibility for in-container Prime Radiant

## TL;DR for standup

Michael wants to install `obsidian-headless` (Obsidian's official CLI tool, currently in open beta) inside the NanoClaude container as a step toward cloud-migrating the Prime Radiant. **Pre-flight doc study surfaces three concerns:** (1) it's open beta with operational details unspecified, (2) plugin support (specifically Obsidian-Git, our auto-commit mechanism) is *not addressed* in the published docs, and (3) it's architected around **Obsidian Sync** — a paid, Obsidian-managed sync service that conflicts with our [[prime-radiant-storage-substrate|GitHub-as-substrate]] decision. **Proposal:** a time-boxed sandbox evaluation (~1–2 days) to answer a small set of specific questions before any production commitment. Outcome routes to either (a) integrate `obsidian-headless` into the NanoClaw container build if findings are clean, or (b) fall back to a pure-git container with bot-driven bidirectional git ops. Asking Jehad in this morning's standup to take ownership of the sandbox, since Docker/Node tooling is in his wheelhouse.

## Context

### What `obsidian-headless` actually is (from the docs at obsidian.md/help/headless)

- Separate npm package (`npm install -g obsidian-headless`, Node.js 22+). **Not** Obsidian desktop running under xvfb.
- A CLI tool with a narrow surface. Documented commands: `ob login [--email --password --mfa]`, `ob logout`. Other commands and flags not documented in the beta material.
- **Open beta.** Many operational details unspecified.
- Authentication via Obsidian account. Implies tie to Obsidian's paid Sync service.
- Stated use cases overlap with ours: "grant agentic tool access to vaults without full computer access," "sync shared team vaults to servers," "run scheduled automations." Obsidian *intends* to support this — we just don't yet know how complete the implementation is.
- **Third-party plugin support (Obsidian-Git specifically) is unconfirmed.** Critical unknown.

### The genuine value-prop (if it works)

- **Auto-link-update on file rename** — Obsidian's killer feature for vault integrity.
- **Obsidian-Git plugin** — auto-commit-on-save inside the container, mirroring what Michael's local Obsidian does today.
- **Scheduled automations** — could host the daily news digest and other recurring tasks Obsidian-native rather than NanoClaw-native.

### The substrate-conflict risk

`obsidian-headless` is built around **Obsidian Sync** (encrypted, Obsidian-managed, paid). The [[prime-radiant-storage-substrate]] decision explicitly picked **GitHub** as the canonical substrate for the reasons that matter to federation and audit: every contributor pulls from the same `Janusd-io` remote, commits are the audit trail, GitHub-Teams handles permissions, no third-party vendor in the loop.

Using `obsidian-headless` for sync would mean either:
- **Splitting the substrate** (Obsidian Sync for the cloud container, GitHub for the curator's local Obsidian-Git — two sources of truth, conflict resolution nightmare), or
- **Migrating the substrate to Obsidian Sync** (loses GitHub-as-audit-trail; subjects the vault to Obsidian's centralized service; conflicts with the per-user-data-control posture of [[2026-04-22-per-user-data-control-hard-requirement-agent-platforms]]).

Neither is acceptable. **If we use `obsidian-headless` at all, it must be configured to skip its sync layer entirely** — operate only as a vault automator over a GitHub-cloned working tree. Whether that's a supported configuration in the open beta is the central question this sandbox needs to answer.

### What the curator-role decision implies

Per [[per-instance-curator-role]] (ratified this morning, assuming standup approval), **the curator runs Obsidian locally on their machine.** The container's role is bot-side: read vault, write proposals, commit, push. None of that *strictly* needs Obsidian. The case for `obsidian-headless` in the container is "we get auto-link-update + auto-commit + a known plugin layer for free." The case against is "open beta + sync-tied + adds Node+npm-package dependency for capability the bot could mechanise itself."

This is a real trade-off, not a slam-dunk. The sandbox decides which way it cuts.

## What we're trying to learn (Stage 1 success criteria)

Four primary questions to answer:

1. **Can `obsidian-headless` run WITHOUT Obsidian Sync?** Specifically, can it open a vault that exists as a regular git-cloned directory, do its work, and never call home to Obsidian's sync servers? If yes, in what mode/flag? If no, this whole avenue dies.
2. **Does it support community plugins — specifically Obsidian-Git?** If yes, what's the install mechanism, what's the config surface, does the plugin's auto-commit fire on file writes from outside Obsidian (e.g. from the bot, from cron)?
3. **Concurrency model: can it co-exist with another Obsidian instance editing the same vault?** Scenario: the headless container has the vault open; the curator's MacBook Obsidian has the same vault open via Obsidian-Git pulling the same GitHub remote. What happens when both write?
4. **Resource footprint.** RAM at idle, RAM under load, CPU at idle, container image size. Matters for the multi-tenant cloud-host calculus.

Secondary curiosity items (worth a look but not blockers):
- What automations come built in? Aggregate notes? Auto-tag?
- How does it handle malformed YAML frontmatter — silent skip, error, refuse to load?
- How does it handle a filename collision or invalid slug?
- Does `ob login` work with no Obsidian Sync subscription, or does it gate features behind a paid tier?

## Sandbox container spec

**Throwaway environment. Do NOT reuse Michael's NanoClaude install. Do NOT point at the Prime Radiant vault.**

- Base: Ubuntu 22.04 (or whatever matches Janus's container conventions).
- Node.js 22 (required by the package).
- `npm install -g obsidian-headless`.
- git CLI installed.
- A small synthetic test vault: 10–20 markdown files with frontmatter, a few `[[wikilinks]]`, a `.obsidian/` folder with the plugin community config so we can attempt to install Obsidian-Git. Could be a stripped-down copy of an existing Janus vault structure, NOT the live content.
- Optional sister environment: Michael's MacBook Obsidian pointing at the same GitHub-hosted test vault, to exercise the concurrency scenario.

## Test scenarios

1. **CLI surface mapping.** `ob --help`, then every documented subcommand's `--help`. Capture full output.
2. **No-login startup.** Try to open the test vault without ever running `ob login`. Document what works, what fails, what errors appear.
3. **Login + sync-off.** If `ob login` is required, log in. Look for any flag to disable Sync. Try `OBSIDIAN_SYNC_DISABLED=1` (a guess) and similar env-var conventions.
4. **Community plugin install.** Try to install Obsidian-Git inside the headless instance via whatever mechanism exists (.obsidian/plugins/ folder, a CLI command, an API call). Document what works.
5. **Auto-commit fire test.** With Obsidian-Git installed and configured, write a file to the vault via plain `echo "test" > new-file.md`. Wait. Does Obsidian-Git auto-commit fire? If yes, in how long? If no, why not — is the plugin not loading, not watching the filesystem, or watching but not committing?
6. **Rename + link-update test.** Rename a file that's wikilinked from elsewhere. Does Obsidian-headless update the links?
7. **YAML error test.** Write a file with deliberately malformed frontmatter. Does Obsidian-headless surface an error, silently skip, or load it broken?
8. **Concurrent-write test.** From the sister Obsidian on Michael's MacBook, edit a file. Pull on the container side. From the container, edit the same file via shell. Push from the container. Pull on Michael's side. Document what conflicts arise and how (cleanly resolved? merge marker? lost edit?).
9. **Resource measurement.** `docker stats` over 5 minutes at idle, then during the auto-commit fire test, then during concurrent writes. RAM peak, CPU peak.

## Decision tree (Stage 2 — after sandbox findings)

Two clean exits and a messy middle:

- **Clean win:** `obsidian-headless` runs without sync, hosts Obsidian-Git, auto-commits on bot writes, concurrency is sane, resource footprint is reasonable. → Plan its integration into the NanoClaw container Dockerfile. Becomes standard cloud-deploy shape.
- **Clean loss:** sync is mandatory, plugins don't load, or concurrency is broken. → Fall back to pure-git container (Option A from the design conversation). Bot writes to vault directly; bot or cron runs `git add . && git commit && git push` on a debounce. Curator's local Obsidian-Git handles the curator-side commits. Auto-link-update on rename becomes a lint problem rather than an editor problem.
- **Messy middle:** some things work, some don't. → Document specific failure modes in the sandbox-findings pulse; revisit when Obsidian moves the headless beta forward.

In all three branches: **the curator continues to run desktop Obsidian locally.** This sandbox does not change the curator-role pattern; it only decides whether the container also gets an Obsidian-layer.

## Stage 3 (after Stage 2 chooses a path)

Whichever option won Stage 2, package it for the existing Hostinger+Caddy migration path (Monday 2931866304):

- Bot reads vault, writes proposals, commits, pushes from the cloud VPS.
- Curator on their MacBook sees the changes via local Obsidian-Git pulling.
- Curator edits a file in Obsidian; cloud container picks it up on next pull.
- A real ingest cycle runs end-to-end in the cloud.

If that holds, you've got the playbook for the eventual multi-tenant cloud host, and the per-instance curator pattern composes cleanly: one curator-local-Obsidian + one cloud-bot-container, per Prime Radiant instance.

## Open sub-questions for Jehad

1. **Ownership.** Jehad as owner of the sandbox, or co-owned, or someone else? Sandbox is ~1–2 days; need to fit it into the AIO week somewhere.
2. **Timing.** Today/tomorrow vs. defer to next week? Tradeoff: doing it now keeps the cloud-migration momentum from the brief work; doing it next week lets the standup ratifications (per-instance curator, etc.) land first.
3. **Sandbox venue.** Throwaway Docker container on Michael's MacBook, a separate dev VM, or a fresh Hostinger box that we'd anyway need for Stage 3? Lean toward throwaway-on-MacBook for simplicity.
4. **Test vault content.** Synthetic mini-vault (cleanest, but doesn't exercise real CLAUDE.md-shape patterns), or a pruned copy of the Prime Radiant (more realistic, but more setup)? Lean toward synthetic for Stage 1.
5. **Reporting venue.** `pulse/2026-06-XX-obsidian-headless-sandbox-findings.md` for the writeup. Promote to a brief only if findings are substantial (e.g. surface meaningful trade-offs across cloud-migration plan).
6. **Hard exit.** If `obsidian-headless` requires an Obsidian login even in sync-off mode, do we proceed (one paid account just to test) or stop? Lean toward stop — that's enough of a signal that the tool isn't ready for non-Sync use.

## Risks / what NOT to do

- **Do NOT install `obsidian-headless` in the production NanoClaude container before the sandbox completes.**
- **Do NOT point `obsidian-headless` at the live Prime Radiant vault** (any of the four instances). Sandbox stays on synthetic data only.
- **Do NOT trigger Obsidian Sync on any real Janus vault.** If `ob login` succeeds, do not run `ob sync` on a vault that has any Janus content in it.
- **Do NOT add `obsidian-headless` to the NanoClaw container Dockerfile** until Stage 2 has chosen a path.
- **Do NOT pair the sandbox with a real GitHub PAT** that has push rights to `Janusd-io` repos. If git-push needs to be tested, use a throwaway test repo on a personal GitHub account.

## Decisions sought (this standup)

1. **Approve the sandbox eval** as scoped above (or amend scope).
2. **Confirm Jehad as owner** (or reassign).
3. **Time-box.** Suggested: 8–16 hours of focused work, target findings within the week.
4. **Confirm reporting shape.** `pulse/` entry for findings; escalate to brief only if substantial.
5. **Confirm hard-exit policy.** If sync is mandatory even with `ob login` against a free Obsidian account, stop and write up the negative finding.

Resolution recorded in frontmatter `status:` once Michael + Jehad align.
