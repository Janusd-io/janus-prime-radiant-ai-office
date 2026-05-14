---
type: decision
title: Personal vaults shelved pending federation-architecture redesign on the GitHub substrate
slug: 2026-05-14-personal-vaults-shelved-pending-federation-redesign
created: 2026-05-14
updated: 2026-05-14
status: resolved
owner: michael-bruck
decided_by: michael-bruck
departments: [ai-office]
sources: []
related: [michael-bruck, jehad-altoutou, janus-prime-radiant-build, peer-to-peer-mesh-federation-pattern, ai-native-janus-positioning, project-management-digital-delivery-workflow, 2026-05-14-windows-as-first-non-mac-deployment]
---

## Decision

Personal vaults are **shelved for now** as a Prime Radiant rollout component. The focus reverts to **team brains only** (department-level Prime Radiant instances). Personal vaults remain a stated future-state goal — revisited once the federation architecture on the GitHub substrate is settled and the rules for what flows from a personal vault into a department vault are well-defined.

Effective immediately: the Project Management Prime Radiant rollout proceeds team-only. Future department rollouts (IT, Operations, ISO, HR, Finance, Office of CEO, Engineering, Training) also proceed team-only by default. The company-wide intro deck and other materials that show personal vaults alongside team vaults are now overstated relative to the rollout reality — to be updated at next refresh.

## Decided by

[[michael-bruck|Michael]] and [[jehad-altoutou|Jehad]], 14 May 2026 morning conversation.

## Why this decision now

Four threads converged this week to make personal vaults the wrong piece to push through right now:

1. **Implementation complexity is higher than it looked.** A personal vault is technically straightforward; the rules for *what gets promoted from a personal vault into the department vault* are not. Privacy, ownership, schema coherence, decision-history continuity, who-can-see-what — every one of these needed an answer before the first personal vault could be safely federated upward. We do not have those answers yet.
2. **Federation architecture is in active redesign on the GitHub substrate.** Per [[janus-prime-radiant-build|the program-level hub]] and the 2026-05-13 IT meeting, the move from Google Shared Drive to GitHub as the canonical store changes how federation works between vaults. The original mesh-federation pattern ([[peer-to-peer-mesh-federation-pattern]]) was designed against the Drive model; it needs to be re-thought for Git semantics (clones, branches, sync direction, conflict resolution). Adding personal vaults *during* that redesign multiplies the surface area being worked on.
3. **Technical blocker: two-vault GitHub sync is not yet working.** Concretely: we could not get two vaults (a personal one and a department one) to sync against GitHub from the same machine — the Obsidian Git plugin + repo-clone topology that works for a single vault breaks down when a user has two vaults sharing GitHub state. This is a solvable problem but a *separate* engineering effort from the rollout we want to ship this week. The personal-vaults concept depends on this working cleanly, so we wait until the sync mechanics are sorted.
4. **Team brains are the load-bearing piece for the [[ai-native-janus-positioning|AI Native pitch]].** Bonaventure's framing of Prime Radiant as a commercial-asset proof point depends on department-level institutional memory, not on individual personal vaults. Sequencing team brains first delivers the strategic outcome faster, and personal vaults can land later without breaking the architecture.

## What changes operationally

- **Project Management rollout** (this week) — team brain only. Personal vaults explicitly *not* part of the standup. Communicated in the [[project-management-digital-delivery-workflow|workflow]] and in the standup-proposal deck.
- **Marketing rollout** (Andrew, in flight) — already team-brain-focused via the AIO × Marketing mesh subfolder; no material change.
- **Future department rollouts** (IT, Operations, ISO, HR, Finance, Office of CEO, Engineering, Training) — all team-brain-only by default.
- **Internal communications** — the company-wide intro deck (`janus-prime-radiant-intro-deck.html`) currently shows the three-layer personal → department → company structure prominently. At next material communication, the personal-vault layer is presented as a future-state goal rather than a current rollout component. Existing version stays in the workspace as historical; rewrite for next town hall.
- **`/janus-pulse` skill** ([[michael-bruck|Michael]]'s personal-vault-onboarding skill) — work continues since the long-term goal hasn't changed, but it is no longer on the immediate rollout critical path. Validation-test of the skill can wait for the federation-architecture redesign to land.

## Options considered

1. **Push through personal vaults now** — rejected on implementation-complexity + federation-redesign-distraction grounds.
2. **Shelve entirely, no future commitment** — rejected; we still believe the long-term value of personal vaults is real, especially for the [[ai-native-janus-positioning|three-pillar messaging]] pillar 3 (augment individuals). Just not now.
3. **Shelve until federation-architecture redesign is done, then revisit** (chosen) — preserves the long-term goal while removing it from the immediate critical path.

## What we need to revisit when personal vaults come back on the table

- **Two-vault GitHub sync mechanic** — root cause of the current technical blocker. Needs to work cleanly before personal-vault rollout is feasible. Likely candidates: separate clone roots, per-vault Obsidian-Git config isolation, separate GitHub Desktop / CLI flows, or a wrapper skill that mediates the multi-vault state.
- **Federation rules** between personal vault and department vault: what flows up automatically, what requires explicit promotion, what stays personal forever.
- **Privacy taxonomy** beyond the existing public/private/personal split (see [[2026-05-11-privacy-vs-personal-vault-content-taxonomy]]).
- **GitHub repo topology** — is each personal vault its own repo? A branch within the department repo? A separate org? — needs to be designed against the redesigned federation pattern.
- **Onboarding skill scope** — `/janus-pulse` was designed to do both personal-vault setup and federation hook-up; will probably split into two skills when this comes back.

## Related

- [[janus-prime-radiant-build]] — program-level hub; status updated to reflect personal-vault deferral.
- [[peer-to-peer-mesh-federation-pattern]] — concept page in line for redesign on the GitHub substrate.
- [[2026-05-14-windows-as-first-non-mac-deployment]] — sibling decision from today on platform-test framing for the Project Management rollout.
