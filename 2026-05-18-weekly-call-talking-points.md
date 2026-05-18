# Weekly call — talking points

**For:** Michael · **Call date:** 2026-05-18 · Bonaventure's three-block format.
**Scope:** AIO work only (Michael + Jehad). Andrew's Singapore commercial layer reported separately.

---

## (1) Last week — what landed

**Track A — substrate migration.** AIO instance moved off Drive onto GitHub end-to-end (`Janusd-io/janus-prime-radiant-ai-office`). Substrate brief + setup runbook (with bash script) shipped. Two orgs locked: `Janusd-io` for AIO+template, `Janusd-com` for every other department. Cowork sees real files on real disk — fixes the failure mode that blocked new-contributor onboarding.

**Track B — Project Management Prime Radiant fully scoped.** Lysander walkthrough → 28-phase workflow captured as process page. Two structural lessons filed (AI bounded role; document-mgmt gap). Four entity pages (Lysander, Rosa Wu, Spike, Dhyey). Kickoff deck through 3 rounds — ready to share. **Personal vaults shelved** pending federation redesign on Git. **Windows-first deployment** for the first time.

**Track C — AIO infrastructure.** Standup skill **v3.15 in production** (writes direct to Prime Radiant inbox — v3.16 needs to port off the Drive MCP connector now we're on Git). CLAUDE.md **v0.10 + v0.11** (multi-graph framing + Git substrate documentation). Mesh-federation **first practical test** stood up (AIO × Marketing pairing). **NotebookLM retired** in favour of HTML. **Notion deprecation end-May confirmed.** **11 tools moved through AIR** (Jehad assignment). Schema linter + ISO 27001 evidence-chain now first-class requirements.

**Stakeholder signal:** BW's 11 May Prime Radiant shout-out ("happening quicker than I thought").

---

## (2) This week — to-do

**Michael:**

- Ship PM kickoff deck → Euclid/Rosa Wu/Lysander/Spike; schedule session.
- Scaffold `janus-prime-radiant-project-management` on `Janusd-com` (first scripted run of the new setup script).
- PM tooling install (Windows-first; ~60–90 min). Document friction.
- Drive-webhooks API investigation (replaces Kafka, which was overkill).
- Schema linter scoping + ISO 27001 evidence-chain cross-linking spec.
- Notion deprecation runway — every active surface needs dual-write or migration confirmed before end-May.
- BW audio-recovery item from 11 May.

**Jehad:**

- **First Git round-trip on the new clone** → validates the runbook → unblocks per-member runbook extraction.
- **Standup skill v3.16** — port Step 5G write path off Drive MCP onto Git substrate.
- Continue AIR pipeline (11 backlogged tools).
- Hostinger Sandbox advance.
- ISO programme `/ims-enrolment` — continue post-CEO-checkin; process-owner mapping with Simon.

*Sequencing: v3.16 → member-runbook extraction → first PM scaffold are dependent in that order. Stretch: all three by 24 May. Realistic: by 29 May.*

---

## (3) Open discussion — decisions I want from BW

1. **Internal branding for the wiki.** Prime Radiant / Nomi / brain / wiki / Pulse / PULS all in use. System name stays *Janus Prime Radiant*; user-facing name open. Andrew should be in the conversation. 20-min decision.
2. **Personal vaults — when do they come back?** Shelved last week pending federation redesign on Git. Affects `/janus-pulse` scope and the company-wide intro deck (currently overstated). Timing call.
3. **Schema governance.** Linter + ISO 27001 evidence-chain are real engineering, not maintenance. Want priority confirmation relative to v3.16 + Drive-webhooks work.
4. **Pacing check.** BW said "quicker than I thought." Three instances live by end-May if PM lands cleanly. Should AIO compress the HR / Finance / ISO / Office-of-CEO queue further?
5. **Notion-after-May story.** End-May deprecation confirmed. Want a signal on how forcefully to land the cutover with department heads — coordination item, not AIO-only.

**Signals worth flagging (not decisions):**

- **Mnemon** — LLM-supervised persistent memory for AI agents. Closest external system to Prime Radiant discipline at runtime. Tracking.
- **Multi-graph memory convergence** — Mnemon's four-graph store + MAGMA experimental validation = same four-axis vocabulary we adopted in CLAUDE.md v0.10.
- **"Claude OS"** — Hostinger-hosted vault files via purpose-built APIs/MCPs. Approved for exploration last week.

---

## If BW asks me

- *"What's the single biggest risk this week?"* → The v3.16 → member-runbook → PM scaffold sequence is dependent in that order. If Jehad's Git round-trip surfaces friction we didn't anticipate, the PM kickoff slips. Mitigation is upfront — get the round-trip done early in the week.
- *"What did the substrate migration actually buy us?"* → Cowork sees real files on real disk (no Drive streaming-mount placeholder layer that broke onboarding); GitHub auth decoupled from Workspace identity; substrate aligns with our content discipline; federation via sibling clones matches the mesh pattern.
- *"How many Prime Radiant instances will be live by end of month?"* → AIO live; Marketing in build; PM kicking off this week → 3 by 31 May if PM kickoff happens this week. ISO / HR / Finance / IT-proper / Office-of-CEO / Engineering / Training still queued.
- *"What's the Notion-after-May story?"* → Standup skill v3.15 already writes to the vault inbox. Operations Notebook content gets dual-written / migrated by end-May. Anything else still in Notion as SoR after 31 May needs to move — and that's an org-coordination ask, not AIO-only.
- *"Why are personal vaults shelved?"* → Two vaults can't sync against GitHub cleanly from the same machine yet — the Obsidian Git plugin + repo-clone topology works for one vault, breaks down at two. Solvable, but separate engineering work from this week's rollout. Doesn't affect team-vault rollouts.
