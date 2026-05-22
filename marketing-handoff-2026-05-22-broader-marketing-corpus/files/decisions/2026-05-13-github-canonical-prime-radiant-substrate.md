---
type: decision
title: GitHub is the canonical file store for Prime Radiant; Google Shared Drive structure project deprecated
slug: 2026-05-13-github-canonical-prime-radiant-substrate
created: 2026-05-13
updated: 2026-05-14
departments: [ai-office, it-ops]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
captured_by: jehad-altoutou
sources: [2026-05-13-aio-pm-meeting]
related: [janus-prime-radiant-build, janus-prime-radiant, monday-rollout, marketing-prime-radiant]
audience: [department]
---

# GitHub is the canonical file store for Prime Radiant

## Decision

As of 2026-05-13, GitHub (specifically the `Janusd-io/janus-prime-radiant-<dept>` repo family) is the canonical substrate for every Prime Radiant instance across departments. The previously planned Google Shared Drive structure project is **deprecated** (Monday item `2898141770` moved to Status: Deprecated with rationale + Description Update).

## Options considered

- Google Shared Drive — original plan; finer-grained ACLs but no version control, no merge semantics, no skill-friendly substrate.
- GitHub repos per dept — what was chosen; transparent version control via Obsidian Git, push-based federation, programmatic onboarding.
- Hybrid (Drive for binaries, Git for markdown) — rejected as added complexity without solving the auth-and-history pain points.

## Why

Git gives Prime Radiant the substrate it was always implicitly assuming: deterministic merges, full history, branch-and-PR escalations, and a clean push surface from each person's local Obsidian vault. `/janus-brain` provisions GitHub accounts silently so users never touch GitHub directly — the discoverability cost is borne by the skill, not the employee. Per `2026-05-13-aio-pm-meeting`, decided live with the PM team in the room (Euclid, Rosa) so the rollout to PM as pilot #2 inherits the GitHub substrate from day one.

## When

2026-05-13 · AIO Project-Management meeting · decided by Michael Bruck with Jehad facilitating the architecture demo.

## Implications

- The Drive structure project is no longer the Prime Radiant blocker; deprecate it on Monday board `5095012818` (done at meeting).
- PM team rollout uses the GitHub substrate from day one, not a temporary Drive-based scaffold.
- IT/Operations needs a follow-up session to wire GitHub-account provisioning into the onboarding flow.
- The CLAUDE.md v0.10 language pinning Drive as substrate is now outdated; the v0.11 rewrite (deferred from v0.10) inherits this as a load-bearing change.
