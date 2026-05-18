# AI Office — Weekly Update for Bonaventure's Call

**Date:** 2026-05-18 (Monday)
**Reporting:** Michael Bruck · Jehad Altoutou
**Window:** 11 May → 17 May 2026
**Format:** Per Bonaventure's three-block structure — (1) last week completed, (2) this week's to-do list, (3) open discussion.

*Scope note: this update covers AI Office work only — what Michael and Jehad were driving. The Singapore commercial layer (white paper, campaign plan, three-pillar messaging) is Andrew's track and is reported separately.*

---

## 1. Last week's completed agenda (11–17 May)

Heavy week with three load-bearing things landing in parallel: Prime Radiant moved off Google Drive onto GitHub; the first cross-department instance got fully scoped and made ready to kick off; the standup pipeline tied off ahead of Notion's end-of-May deprecation.

**Track A — Drive → GitHub substrate migration executed end-to-end**

- AIO instance migrated 13 May to a private GitHub repo (`Janusd-io/janus-prime-radiant-ai-office`), cloned to `~/janus/prime-radiant/ai-office/` on the curator's machine. Obsidian Git plugin handles auto-pull/commit/push; Cowork now sees real files on real disk (no streaming-mount placeholder layer that was breaking new-contributor onboarding).
- Substrate decision brief filed (`briefs/prime-radiant-storage-substrate.md`) — diagnosis of the Drive failure mode, alternatives considered, migration sequence.
- Curator-side setup runbook with embedded bash script extracted (`processes/prime-radiant-instance-setup.md`) — reduces a future instance scaffold from ~2h unscripted to ≤10 min scripted.
- **Two GitHub orgs locked in**: `Janusd-io` for AIO + the template repo; `Janusd-com` for every other department instance (PM, IT, Marketing, ISO, HR, Finance, Office-of-CEO, Engineering, Training). Keeps AIO experimentation isolated from company-operational vaults while reusing the same template + tooling.

**Track B — Project Management Prime Radiant scoped and ready to launch**

- Lysander Liu (Head of PM) walked Michael through the full 28-phase digital-delivery workflow on 14 May (~60 min). Captured as a canonical process page — the PM instance gets initialised against it.
- Two structural lessons filed: (i) **AI's bounded role in PM** (~30–60%, first-draft only, human verification gates remain non-negotiable); (ii) **document-management gap** (current substrate is Excel master + Google Docs network + Monday — Prime Radiant coexists, not displaces).
- Four entity pages created: Lysander Liu, Rosa Wu (co-head of PM with Euclid), Spike Zhao (digital modeling engineer), Dhyey Mehta (recent IT joiner, stub pending Euclid confirmation).
- **Standup-proposal deck** went through three rounds of refinement on 14 May; ready to share with Euclid / Rosa Wu / Lysander / Spike.
- **Personal vaults shelved** pending federation-architecture redesign on Git (two vaults can't sync against GitHub cleanly from the same machine yet). Team brains only for now.
- **Windows-first deployment** framing locked: PM rollout doubles as Janus's first non-Mac Prime Radiant; tooling-install session re-budgeted ~60 → ~60–90 min.

**Track C — AIO infrastructure: skill, schema, federation, registry**

- **Standup skill v3.15 in production** (13 May) — Step 5G writes standup logs directly to the Prime Radiant inbox, closing the dual-write loop ahead of the confirmed **end-of-May 2026 Notion deprecation**. (Substrate-migration follow-up: v3.15 was built against the Drive MCP connector; v3.16 needs to port the write path onto Git now that AIO has migrated.)
- **CLAUDE.md schema bumped twice.** v0.10 (13 May) formalises the wiki's frontmatter as a four-graph encoding (entity/semantic/temporal/causal edges) — matches the agent-memory community vocabulary that converged in mid-May 2026. Added `decided_by` + `captured_by` fields. v0.11 (14 May) documents the Git substrate and adds git-awareness framing across all workflows.
- **Mesh federation first practical test executed 11 May** — AIO × Marketing pairing stood up the same afternoon the concept page was authored, with shared `entities/departments/<other>/` subfolders in both vaults.
- **AI Registry — 11 tools moved through AIR**: Microsoft Clarity, Resend, Mailchimp, LinkedIn Marketing Solutions, Canva, FactSet, Solace, Whisper Flow, Google Stitch, Hercules added to Backlog; Hostinger advanced in Sandbox. AIP had zero activity in the window (status surface reconciled from Monday — no recon needed).
- **NotebookLM retired** for org chart / presentation outputs in favour of HTML — Bonaventure endorsed the convention on the 12 May AI Native call.
- **Schema linter + ISO 27001 evidence-chain cross-linking** surfaced as first-class requirements (Monday 2912631119, 2912592188) after Euclid's 5,000-document personal vault validated Prime Radiant at scale but exposed schema drift as a real risk.
- **Vault-event ingest direction set.** Kafka rejected as overkill (<100 events/day); Drive webhooks API to be investigated as the right-sized replacement. Adjacent "Claude OS" research stream (Hostinger-hosted vault files exposed via purpose-built APIs/MCPs) approved for exploration.

**Stakeholder signal**

Bonaventure's positive shout-out on Prime Radiant at the 11 May standup — *"happening quicker than I thought"* — validates pacing and pre-empts political resistance as the rollout reaches non-AIO instances.

---

## 2. This week's agenda / to-do list (18–24 May)

**Michael — primary load**

- Ship the **PM kickoff deck** to Euclid / Rosa Wu / Lysander / Spike; schedule the session.
- Scaffold `janus-prime-radiant-project-management` on `Janusd-com` using the new setup runbook — first scripted execution of the scaffold script.
- **PM tooling-install session** (Windows-first; ~60–90 min). Document the friction.
- **Drive-webhooks API investigation** — replaces Kafka path for vault-event ingest.
- **Schema linter scoping** + ISO 27001 evidence-chain cross-linking spec.
- **Notion deprecation runway** — every active surface needs dual-write or migration confirmed before end-May.
- **Bonaventure audio-recovery item** — open since 11 May (Fireflies quiet-voice channel gap).

**Jehad — primary load**

- **First Git-substrate round-trip** on the new clone. Validates the curator runbook end-to-end. Gates the per-member runbook extraction.
- **Standup skill v3.16** — port Step 5G off the Drive MCP connector onto the Git substrate so the standup pipeline keeps closing the loop after the AIO vault migration.
- **Extract `processes/prime-radiant-member-setup.md`** once the Git round-trip validates the substrate brief's Appendix A.
- **Continue AIR pipeline management** — the 11 newly-backlogged tools mostly tied to upcoming evaluation work.
- **Hostinger Sandbox** — advance through evaluation.
- **ISO programme `/ims-enrolment` skill** — continue post-12 May CEO check-in (approved-to-continue). Process-owner mapping with Simon.

*Sequencing note: the v3.16 port + per-member runbook extraction + first PM scaffold are sequential — each unblocks the next. Realistic landing target for all three is end of next week (29 May); aggressive target is end of this week (24 May) if the PM kickoff sequence lands cleanly.*

---

## 3. Open discussion items

Items where I'd like Bonaventure's input or a coordinated decision before the work proceeds.

**Internal branding for the wiki**

Multiple sub-names are in circulation: Prime Radiant, Nomi, brain, wiki, Pulse, PULS. The system name stays *Janus Prime Radiant*; what we call the user-facing surface for non-technical audiences is open. Andrew should be in this conversation. Bonaventure's 11 May read: *"Prime Radiant is very geeky."* Recommend a 20-minute decision on the call.

**Personal vaults — when do they come back?**

Shelved last week pending federation-architecture redesign on Git substrate (two vaults can't sync against GitHub cleanly from the same machine yet — solvable but separate engineering effort). Affects `/janus-pulse` onboarding skill scope and the company-wide intro deck (which is currently overstated relative to rollout reality). Need a timing call.

**Schema governance — linter + ISO 27001 evidence-chain**

Euclid's 5,000-document vault surfaced schema drift as a real scale risk. Schema linter + ISO 27001 evidence-chain cross-linking are now requested as first-class requirements. This is real engineering, not maintenance — would like priority confirmation relative to the v3.16 port and Drive-webhooks work.

**Pacing check**

Bonaventure said on 11 May that Prime Radiant is *"happening quicker than I thought."* Want a calibration: is the current cadence right, too aggressive, or should AIO accelerate further? Three instances live by end-May if PM kicks off cleanly (AIO, Marketing, PM); want a read on whether to compress the HR / Finance / ISO / Office-of-CEO queue.

**Notion-after-May story**

End-of-May 2026 deprecation is confirmed. Standup skill v3.15 dual-writes; Operations Notebook content migrating. Any team still using Notion as a SoR after 31 May needs to move — that's an organisational coordination item, not an AIO-only one. Want a signal on how forcefully to land the end-May cutover with department heads.

**External signals worth a beat (not decisions)**

- **Mnemon** — LLM-supervised persistent memory for AI agents. Closest external system in the market to the Prime Radiant discipline applied at agent runtime. Single-source; tracking.
- **Multi-graph memory convergence** — independently surfaced by Mnemon's four-graph store (12 May) and validated experimentally by MAGMA (13 May). Same four-axis vocabulary we adopted in CLAUDE.md v0.10. Cross-layer recognition.
- **"Claude OS" research direction** — Hostinger-hosted vault files exposed via purpose-built APIs/MCPs. Approved for exploration last week.

---

*Sources: AIO wiki `log.md` (entries since 2026-05-11), project hubs `janus-prime-radiant-build` and `iso-compliance-programme`, brief `prime-radiant-storage-substrate`, process pages `prime-radiant-instance-setup` and `standup` (v3.15), Linear AI Registry team.*
