---
type: decision
title: Project Management rollout is also Janus's first Windows deployment of Prime Radiant
slug: 2026-05-14-windows-as-first-non-mac-deployment
created: 2026-05-14
updated: 2026-05-14
status: resolved
owner: michael-bruck
decided_by: michael-bruck
departments: [ai-office, it-ops]
sources: []
related: [michael-bruck, jehad-altoutou, euclid-wong, project-management-digital-delivery-workflow, janus-prime-radiant-build, 2026-05-14-personal-vaults-shelved-pending-federation-redesign]
---

## Decision

The Project Management Prime Radiant rollout is also explicitly framed as **Janus's first Windows deployment** of the Prime Radiant pattern. Until now the rollout has only run on Mac (AI Office: [[michael-bruck|Michael]] + [[jehad-altoutou|Jehad]]; Marketing: [[andrew-soane|Andrew]]). The Project Management team — [[euclid-wong|Euclid]], Lysander Liu, Rosa Wu, Spike Zhao — is all on Windows. Tooling install for this rollout is therefore a dual-purpose exercise: it stands up the Project Management instance *and* it is the controlled environment for figuring out the Windows install path.

## Decided by

[[michael-bruck|Michael]], 14 May 2026. Surfaced as a planning consideration while updating the Project Management standup proposal.

## Why this matters

- **Platform coverage is required for company-wide rollout.** All future Janus department rollouts (IT, Operations, ISO, HR, Finance, Office of CEO, Engineering, Training) include teams predominantly on Windows. Treating the Project Management rollout as the first Windows reference deployment de-risks every subsequent rollout.
- **Mac-only assumptions need to be surfaced and addressed.** Current tooling install runbooks (Cowork project setup, Obsidian, Web Clipper, Fireflies connector) were written for Mac. Windows install paths, shortcuts, file-path conventions, and any platform-specific friction need to be documented as the install happens.
- **Frame as a test, not a gamble.** Communicating to the Project Management team that they are the first Windows deployment is more honest than pretending the install is routine. Lysander, Rosa, and Spike will hit friction; framing it as a controlled test makes the friction useful (it becomes documented input for the rollout playbook) rather than a confidence problem.

## What changes operationally

- **Standup-proposal deck** ([`2026-05-14-project-management-prime-radiant-standup-proposal.html`](2026-05-14-project-management-prime-radiant-standup-proposal.html)) updated to surface the Windows-test framing on slide 3 (step 3) and slide 5 (week 1 timeline).
- **Tooling install session expected duration** revised from ~60 min to ~60–90 min to absorb Windows-specific debugging.
- **Lessons captured during the install** — any Windows-specific gotcha gets documented as a `lessons/` page for downstream rollouts.
- **Followup Windows-install runbook** as a `processes/` page once the Project Management install is complete — fold the lessons into a clean reference doc that the next team (IT, Operations, etc.) inherits.

## Options considered

1. **Wait for Windows tooling to be perfected before rolling out to Project Management** — rejected; this would delay the rollout indefinitely. We do not know what we do not know about Windows installs until we try one.
2. **Roll out to Project Management on Windows quietly, treat issues as bugs** — rejected; under-communicates the actual platform exposure and makes any friction feel like a failure rather than expected discovery.
3. **Frame the Project Management rollout as the first Windows deployment** (chosen) — honest about the platform exposure, captures lessons systematically, sets correct expectations.

## What we'd like to learn

- Does Cowork's local-folder access work as smoothly on Windows as on Mac? (Earlier in the rollout we hit a path-based-mounting unreliability issue on Mac with Andrew's vault.)
- Does Obsidian Git sync behave the same way on Windows? Any quirks in vault discovery or auto-pull/commit/push?
- Does the Web Clipper Chrome extension install the same way on Windows? Any sandbox/permission issues?
- Does the Fireflies connector authenticate cleanly on Windows? Any browser-specific oddities?
- What does the `/janus-pulse` onboarding skill look like on Windows when it returns to the critical path post-federation-redesign?

## Related

- [[2026-05-14-personal-vaults-shelved-pending-federation-redesign]] — sibling decision from today on rollout scope.
- [[project-management-digital-delivery-workflow]] — the workflow the Project Management rollout initialises against.
- [[janus-prime-radiant-build]] — program-level hub; status to be updated.
- [[euclid-wong]] — sponsor; runs all three teams the Windows rollout pattern will eventually serve.
