---
type: question
title: "Per-instance curator role — formalize before PM-team rollout deploys it"
slug: per-instance-curator-role
created: 2026-06-05
updated: 2026-06-05
departments: [ai-office]
status: active
owner: michael-bruck
related: [janus-prime-radiant-build, prime-radiant-instance-setup, nanoclaw-prime-radiant-wiring, nanoclaw, 2026-05-13-pm-team-prime-radiant-pilot-two, michael-bruck, jehad-altoutou, andrew-soane, lysander-liu, rosa-wu, spike-zhao, bonaventure-wong]
---

# Per-instance curator role — formalize before PM-team rollout deploys it

## TL;DR for standup

Each Prime Radiant instance gets **one designated curator** running Obsidian on their own machine. They own the vault's discipline: triage incoming drafts, run lints, make schema judgment calls, federate with other instances. Every *other* team member is a **contributor / user** who interacts with the instance through NanoClaude (Slack) — no local Obsidian, no local clone, no Docker, no rulebook to memorize. The PM-team rollout (Lysander as curator, Rosa + Spike as contributors) is the first place this pattern gets explicitly deployed; AIO + Marketing + Bonaventure's instances have been operating this way informally already. Asking Jehad to ratify, surface concerns, and confirm a few open points so we can land it as the rulebook default before PM goes live.

## Why now

The pattern emerged from the 2026-06-05 NanoClaude-write-access design conversation (see [[nanoclaw-prime-radiant-wiring]] and the in-session discussion that produced this question). Two threads converged:

1. **Vault-write access for NanoClaude is hard if every contributor is also a curator.** Race conditions with Obsidian-Git auto-commit, `index.lock` contention, no review gate on agent writes — all become tractable once exactly one human edits a given vault in Obsidian. The bot writes to staging (`inbox/`, PRs, OneCLI-approval-gated drafts); the curator reviews and lands canonical changes.
2. **Cloud migration becomes simpler.** Curator's Obsidian stays local — N=1 install per team, not N per contributor. NanoClaude moves to cloud (per the in-flight Hostinger+Caddy plan, or eventually multi-tenant). The "Obsidian-in-cloud" problem disappears because most team members don't need Obsidian at all.

The PM-team rollout is the first time we have a multi-person team where curator ≠ contributors, so it's the first real test of the pattern. AIO is curator=Michael / contributor=Jehad (close to the pattern); Marketing is curator=contributor=Andrew (single-person instance); Bonaventure's vault is curator=contributor=Bonaventure. PM will be 1 curator + 2 contributors.

## The four current instances

| Instance | Curator | Contributors | Pattern fit |
|---|---|---|---|
| **AIO** | [[michael-bruck]] | [[jehad-altoutou]] | Implicit; works because Jehad is highly rulebook-fluent. |
| **Marketing** | [[andrew-soane]] | (none yet) | Single-person; curator-contributor distinction collapsed. |
| **Bonaventure's** | [[bonaventure-wong]] | (none) | Single-person; CEO's personal vault. |
| **PM team** | proposed: [[lysander-liu]] | [[rosa-wu]], [[spike-zhao]] | **Pending — first explicit deployment of the pattern.** Open: confirm Lysander as lead vs Euclid (per 2026-05-13 decision Euclid was named — has the lead rotated?). |

## The proposal

### Curator role (one per instance)

**Operating model.** Runs Obsidian locally against their instance's git clone. Has push rights to the canonical remote (`Janusd-io/janus-prime-radiant-<instance>`). Has admin rights on their NanoClaude agent group (when the bot lands).

**Responsibilities.**

- **Daily:** triage any NanoClaude-surfaced drafts (chat replies, `inbox/` deposits, PRs). File the ones that warrant filing; edit the ones that need tightening; drop the ones that don't earn their keep. Update `log.md` and `index.md` in lockstep.
- **Weekly (or per 10-ingest threshold per CLAUDE.md §5.3):** run lint, resolve the judgment calls (which contradiction to flag, which orphan to archive, when to file a `questions/` page, when an attribution case needs softening).
- **As triggered:** review `questions/` (open) for items ready to promote to brief or decision; review `pulse/` for converging themes that warrant a brief.
- **As-needed:** propose schema (CLAUDE.md) edits via `questions/` pages when the rulebook needs to grow; coordinate with adjacent-instance curators when cross-vault federation is needed.

**Skillset.** Rulebook-fluent + domain-fluent (Marketing curator understands marketing; PM curator understands delivery; etc.) + willing to do the work. Not a title; a role assignment.

**Bandwidth expectation.** Best estimate from the AIO instance (Michael's actual time): a few hours/week steady-state, more during heavy ingest periods or rulebook evolution. Worth costing as a protected fraction of the curator's week.

### Contributor / user role (everyone else)

**Interface.** NanoClaude Slack DM (read, query, draft-via-chat). For richer drops: a Slack message into a shared "vault inbox" channel that gets ingested into `inbox/` by the bot.

**Optional surfaces (longer-term):** a per-user dashboard (see below) showing the contributor's relevant vault state.

**Not required.** Local Obsidian. Local git clone. Docker / NanoClaw install. Rulebook memorization.

**Affordances.**
- Ask questions; bot reads vault, replies.
- Drop content (links, transcripts, observations) into vault inbox; curator triages.
- Surface decisions they made; curator decides whether it becomes a `decisions/` page.

### NanoClaude's role

Sharpened by the curator pattern: it is the **contributors' read interface** primarily, the **curator's draft-staging assistant** secondarily. Not "fully autonomous curator" and not aiming to be in the short-to-medium term.

## The PM-team deployment (first explicit test)

Proposed shape:

- **Curator:** [[lysander-liu]] (confirm vs. 2026-05-13 decision naming Euclid Wong — has the lead shifted, or is Lysander a different role here?).
- **Contributors:** [[rosa-wu]], [[spike-zhao]] — Slack + NanoClaude only.
- **Vault:** new `janus-prime-radiant-pm` repo under `Janusd-io`, cloned to Lysander's machine per the [[prime-radiant-instance-setup]] runbook.
- **NanoClaude instance:** TBD timing — could be local on Lysander's machine first (matching the Michael-2026-05-21 pattern), or wait until the cloud-bot host comes online (Plan A from the NanoClaude wiring conversation). Cleanest option: stand up the vault first, give Lysander a few weeks to curate against it solo, then add NanoClaude once content density justifies it.
- **Onboarding sequence:** [[prime-radiant-instance-setup]] runbook + a curator-specific addendum (rulebook walk-through, lint dry-run, schema judgment-call examples). To be written.

## Dashboard idea (related but separate)

Michael flagged this in the same conversation: build a per-user dashboard to simplify the contributor/user UX — a place where each contributor sees what's relevant to them (recent briefs touching their work, open questions assigned to them, news digest, etc.).

Two notes:
- **The PM team already has dashboard work on Rosa's plate** per `[[2026-05-13-pm-team-prime-radiant-pilot-two]]` ("Dynamic dashboards and visualisation prompts (Rosa) scoped as longer-horizon, not a rollout blocker"). This dashboard direction isn't a new ask — it's surfacing existing Rosa-work and asking what the pan-instance version looks like.
- **It deserves its own `questions/` page** — design surface is too big to develop here without diluting the curator-role focus. Proposed slug: `per-user-jpr-dashboard-design`. Captures: scope (per-user vs per-team), surface (web vs Slack-rendered vs HTML-deck-generated), live-vs-batched, NanoClaude-driven vs separately-engineered, relationship to Rosa's existing visualization work.

Filed as a deferred follow-up; not in scope for this question.

## Rulebook implications (if ratified)

Scope of edits if the pattern lands:

1. **CLAUDE.md §1 amendment.** Currently reads: "Michael Bruck is the primary curator. Other AI Office members … contribute directly or indirectly." Extend to: each Prime Radiant instance has a designated curator (primary, plus optional deputy); contributors interact through NanoClaude. Vocabulary lock: "curator" rather than "owner" / "maintainer" / "admin" for this role.
2. **New concept page** `concepts/per-instance-curator-role.md` (or `processes/` if more runbook-shaped). Full role definition, responsibilities, weekly cadence, handoff protocol. Becomes the canonical reference for new instances spinning up.
3. **[[prime-radiant-instance-setup]] addendum.** "Identify and onboard the instance curator" as step 1 of any new-instance bootstrap. Curator's first-day tasks: read CLAUDE.md, read the rulebook test cases (this page), run a dry-lint to surface their judgment-call style.
4. **[[janus-prime-radiant-build]] update.** Program-level page reflects the curator-role as a load-bearing architectural choice, not just a Michael-specific accident.

No other rulebook surfaces affected.

## Open sub-questions for Jehad (and standup discussion)

1. **PM lead — Lysander or Euclid?** The 2026-05-13 decision says Euclid is pilot lead. Michael's framing today says Lysander as curator. Has the team rotated, or are these two different roles (Euclid = strategic owner; Lysander = day-to-day curator)? Need this nailed before the PM-instance setup runs.
2. **Deputy curator model.** Should every instance have a designated backup curator for PTO / illness / busy-week coverage, or do we accept that some instances are too small for that (Marketing, Bonaventure's) and just queue work in `inbox/` until the primary returns? Tentative answer: deputies where headcount allows (AIO: Jehad; PM: Rosa or Spike). Single-person instances accept the queue.
3. **Power-user-Obsidian policy.** Restrictive "only the curator runs Obsidian" is probably too strong — some contributors will want to navigate the graph view or use Obsidian as a query tool. Soft norm: "discouraged because (a) maintenance load shouldn't be distributed, (b) you risk creating divergent local edits that don't fit the discipline; but not blocked." Curator empowered to push back on inconsistent edits. Confirm this is the posture.
4. **Curator handoff protocol.** When a curator leaves Janus or rotates out, what's the handoff? Tentative: 2-week pair-curate with the incoming curator; rulebook (CLAUDE.md) is the manual; per-instance bootstrap docs are the runbook. Possibly add a `processes/curator-handoff.md` page when the first handoff actually happens — too speculative to design abstractly.
5. **NanoClaude timing for PM instance.** Stand up vault first then add bot, or both at once? Recommendation: vault first; bot once content density justifies it (~50 pages? a month of curation?). The reasoning is that NanoClaude is most valuable as a query layer over existing content, and a near-empty vault produces low-signal answers.
6. **Curator-as-formal-job-allocation vs role-assignment.** For PM, Lysander has a day job. The curator role costs a few hours/week. Does this need to be reflected in Lysander's quarterly objectives / Monday surface, or is it implicit in the pilot agreement? AIO's answer for Michael is "implicit because curator and AIO-lead are the same person"; PM is the first place this needs an explicit answer.
7. **Cross-instance federation in practice.** When Marketing's curator writes a brief about a vendor decision that's also AIO-relevant, who initiates the cross-vault reference? Tentative: the *receiving* instance's curator pulls. The originating curator publishes; downstream curators decide whether to absorb. Confirm.

## Real-world precedent (just to legitimize)

This shape isn't novel — it's the pattern Wikipedia's WikiProject maintainers, Stripe's docs-owners, and large engineering teams' designated docs-leads all converge on. "Everyone curates" works at small team scale and breaks at any larger scale. "One curator + everyone contributes" is the durable shape. Janus is just adopting it earlier than most institutions because the Prime Radiant pattern surfaced the need.

## Decisions sought (for this standup or the next)

1. **Ratify the curator-role pattern as the rulebook default.** If yes, schedule the CLAUDE.md §1 amendment and the new `concepts/per-instance-curator-role.md` page as a separate curation task.
2. **Confirm PM curator = Lysander (or correct to Euclid / different mapping).**
3. **Confirm deputy policy, power-user-Obsidian policy, and federation-direction defaults** (or note these as further-discussion items).
4. **Greenlight the per-user dashboard as its own `questions/` page** — to be filed separately, not bundled here.
5. **Decide PM-instance NanoClaude timing** — vault-first then bot, or both at once.

Resolution recorded in frontmatter `status:` field once Michael + Jehad align.
