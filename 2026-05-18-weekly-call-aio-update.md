# AI Office — Weekly Update for Bonaventure's Call

**Date:** 2026-05-18 (Monday)
**Owner:** Michael Bruck (AIO)
**Format:** Per Bonaventure's three-block structure — (1) last week completed, (2) this week's to-do list, (3) open discussion.

---

## 1. Last week's completed agenda (11–17 May)

This was a heavy week. The headline framing: Janus's AI Native commercial pitch crossed from internal-tooling into a publicly-anchored, three-pillar messaging spine with two Outputs artefacts in the field — and the underlying Prime Radiant substrate migrated off Drive onto GitHub in the same week.

**Singapore commercial layer — strategy operationalised in 3 days**

- **Janus Singapore white paper ("How agentic AI can answer the storms ahead")** landed 14 May; 20 pages, co-authored by Bonaventure and Joyce Woo (CEO, Singapore). First long-form externalisation of the three-pillar messaging spine. Anchored to PM Lawrence Wong's May Day Rally 2026 speech (also ingested into the wiki this week as upstream substrate).
- **Singapore campaign plan v1** delivered by Andrew on 15 May: 100 target accounts mapped (33 global/APAC PE-RE, 28 mid-market funds, 13 SG heavyweights, 14 specialised niche, 12 multi-family offices), 9-week timeline to the 8/9 July luncheon, ~S$23,995 / AED 69,210 budget, 5-venue shortlist (Vue / Saint Pierre / Artemis Grill / Sospiri / Shoukouwa).
- **Three-pillar messaging spine** ratified across CEO (Bonaventure: capital → companies → workers) and CMO (Andrew: society → business → individual) — same spine, different lead. Now the Outputs frame for all Marketing PR.
- **Joyce Woo** confirmed as CEO, Singapore; entity page filed; she is the named SG-face for direct outreach to the target list.
- **PM May Day Rally speech** ingested as the upstream Singapore policy vocabulary for the news-monitoring agent and any Janus public-facing response.

**Prime Radiant substrate — Drive → GitHub migration executed end-to-end**

- AIO instance migrated 13 May to a private GitHub repo (`Janusd-io/janus-prime-radiant-ai-office`), cloned to `~/janus/prime-radiant/ai-office/` on the curator's machine. Obsidian Git plugin handles auto-pull/commit/push; Cowork now sees real files on real disk (no streaming-mount placeholder layer).
- Substrate decision brief filed (`briefs/prime-radiant-storage-substrate.md`) with diagnosis of the Drive failure mode that blocked Andrew's onboarding, alternatives considered, migration sequence.
- Curator-side setup runbook with a working bash script extracted (`processes/prime-radiant-instance-setup.md`) — reduces a future instance scaffold from ~2h unscripted to ≤10 min scripted.
- **Two GitHub orgs locked in**: `Janusd-io` for AIO + template repo; `Janusd-com` for every other department instance (Project Management, IT, Marketing, ISO, HR, Finance, Office-of-CEO, Engineering, Training).
- CLAUDE.md schema bumped twice (v0.10 multi-graph framing for the wiki's frontmatter; v0.11 Git-substrate documentation + git-awareness in workflows).

**Project Management Prime Radiant — first non-Mac/non-AIO instance scoped**

- Lysander Liu (Head of PM) walked Michael through the full 28-phase digital-delivery workflow on 14 May (~60 min). Captured as a canonical process page — the PM instance gets initialised against it.
- Structural insights filed as two lessons: (i) **AI's bounded role in PM** (~30–60%, first-draft only, human verification gates remain non-negotiable); (ii) **document-management gap** (current substrate is an Excel master + Google Docs network + Monday — Prime Radiant coexists, not displaces).
- Four entity pages created: Lysander Liu, Rosa Wu (co-head of PM with Euclid), Spike Zhao (digital modeling engineer), Dhyey Mehta (recent IT joiner, stub).
- **Standup-proposal deck** for the kickoff went through three rounds of refinement on 14 May; ready to share with Euclid / Rosa Wu / Lysander / Spike.
- **Personal vaults shelved** pending federation-architecture redesign on Git substrate (two vaults can't sync against GitHub cleanly from the same machine yet). Team brains only for now.
- **Windows-first deployment** framing locked: PM rollout doubles as Janus's first non-Mac Prime Radiant; tooling-install session re-budgeted ~60 → ~60–90 min.

**AIO Marketing & operations**

- AIO × Marketing mesh-federation pairing stood up 11 May as the first practical test of the peer-to-peer mesh-federation concept.
- Standup skill v3.15 in production (13 May) — Step 5G writes directly to the vault inbox via Drive MCP connector.
- **Notion deprecation target confirmed: end of May 2026.** Dual-write to vault inbox is the transition path; subsequent decisions plan around Notion being offline as a Janus surface from June.
- **NotebookLM retired** for org chart / presentation outputs in favour of HTML — CEO-endorsed convention now.
- Brand guideline derived from Andrew's PPTX (v0.1, 15 May) → upgraded to v1.0 the same day on the official brand book (orange `#FCB745`, navy `#013A7D`, light blue `#028CDC`, Montserrat). SG strategy alignment deck retrofitted.
- **AI Registry pipeline**: 11 tools moved through AIR this week (Microsoft Clarity, Resend, Mailchimp, LinkedIn Marketing Solutions, Canva, FactSet, Solace, Whisper Flow, Google Stitch, Hercules added to Backlog; Hostinger advanced in Sandbox). Heavy Marketing-tooling tilt — directly downstream of Andrew's campaign-plan needs.

**Stakeholder signal**

- Bonaventure's positive shout-out on Prime Radiant at the 11 May standup ("happening quicker than I thought") — validates pacing and pre-empts political resistance as the rollout reaches non-AIO instances.

---

## 2. This week's agenda / to-do list (18–24 May)

**Project Management Prime Radiant — kick off the first cross-department instance**

- Share the standup-proposal deck with Euclid, Rosa Wu, Lysander, Spike; schedule the kickoff session.
- Stand up `janus-prime-radiant-project-management` on `Janusd-com` via the new runbook; first scripted execution of the scaffold script.
- Tooling-install session with the PM team (Windows-first; expect ~60–90 min).
- Decision needed: who curates the PM instance day-one (Lysander has the workflow authority; Rosa Wu has the strategic altitude; Euclid wears the broader hat).

**Marketing Prime Radiant — Singapore campaign in build**

- Andrew's 1-week deliverables (committed 12 May → due ~19–20 May): ICP cross-tally with Bonaventure's separate ICP, Target Personas, Topic Taxonomy.
- Target-list review by Bonaventure + Joyce due end-of-day Wed 20 May (missing companies, wrong inclusions, existing-relationship flags).
- Singapore landing page build in days, pending website-architecture resolution (see open discussion).
- Possible migration of Andrew's vault from `Janusd-io` to `Janusd-com` (TBC depending on where it currently sits).
- Web Clipper config for marketing-themed channel; bulk Fireflies ingest of Andrew's prior meetings as the seed corpus.
- Venue selection for the 8/9 July luncheon (date availability + private-room + cost ceiling).

**AIO infrastructure & ops**

- Jehad's first Git substrate round-trip — validates the runbook before we extract `processes/prime-radiant-member-setup.md` as the per-contributor reference.
- Drive webhooks API investigation (Monday 2912592197) — right-sized replacement for cron-based ingest after Kafka rejected as overkill (<100 events/day).
- Schema linter scoping — schema drift surfaced as a real risk against Euclid's 5,000-document personal-vault validation; needed as a first-class requirement (Monday 2912631119).
- ISO 27001 evidence-chain cross-linking spec under the `entities/departments/iso/` federation pattern (Monday 2912592188).
- Continue triaging the 11 backlog AIR tools added this week — most are Marketing/campaign-tooling and gate the Singapore launch (Mailchimp, Canva, LinkedIn Marketing Solutions, Microsoft Clarity, Resend).
- Notion deprecation runway — every active surface needs its dual-write or migration confirmed before end-May.

**Strategic content**

- Brief on the three-pillar messaging spine now has a public surface (the white paper) — consider whether a brief / pulse entry tracking external reactions is warranted.
- Bonaventure's audio-recovery item from the prior Friday meeting (Fireflies quiet-voice failure mode) — still open.

---

## 3. Open discussion items

Items where I want Bonaventure's input or a coordinated decision:

**Singapore launch — website architecture (urgent)**

Three URLs are simultaneously in flight: `janusd.com` (canonical), `janusdg.com` (vanity, appears in the v1 campaign plan), `janusd.sg` (formal SG-entity domain, appears in the white paper as `engage@janusd.sg`). The landing page build is blocked on this. Andrew anticipates this is a "mighty battle." Recommendation: `janusd.com` canonical + `janusd.sg` SG vanity, retire `janusdg.com`. Need a call this week.

**CRM scope and timing**

Bonaventure's "glorified contact list" framing from 12 May reshaped this. Target: ~2–3 weeks to a recommendation Bonaventure agrees with, ~3 weeks for implementation. Google Sheets is the interim; lands by mid-June for the SG launch. Need explicit confirmation that the marketing-CRM (campaign management) vs sales-CRM (pipeline) distinction is acceptable as a scoping move.

**Internal branding consolidation**

Multiple sub-names are circulating: Prime Radiant, Nomi, brain, wiki, Pulse, PULS. The system name stays Prime Radiant; the user-facing surface for non-technical audiences is open. Andrew should be in this conversation. Worth a 20-minute decision on the call.

**External-agency scope (Andrew)**

Bonaventure flagged on 12 May that some of Andrew's external-agency scope (logo, website, design work) might be brought in-house through Janus's own AI-Native capabilities. Open question — Andrew has commitments out; need to know which ones to honour vs reshape.

**Strategic signals worth a beat**

- **Vivian Balakrishnan** (SG Foreign Minister) keynoted the AI Engineering Conference 16–17 May and runs his own LLM wiki on a Raspberry Pi. Bonaventure knows him personally. Potential government-side advocate for the Prime Radiant pattern.
- **Yann LeCun's Advanced Machine Intelligence has a Singapore office** (one of four globally, Asia base for physical AI) — surfaced in the PM speech ingest. Direct adjacency to Janus's physics-first positioning.
- **Mnemon** (LLM-supervised persistent memory for AI agents) — closest external system in the market to the Prime Radiant discipline applied at agent runtime. Single-source so far; tracking.

**Federation architecture — when do personal vaults come back?**

Shelved this week pending the Git-substrate redesign. Affects `/janus-pulse` onboarding skill scope and the long-term "every employee has a vault" pitch in the company-wide intro deck (which is currently overstated relative to rollout reality). Timing question.

**Pacing check**

Bonaventure said on 11 May that Prime Radiant is "happening quicker than I thought." Want a calibration: is the current cadence right, too aggressive, or should AIO accelerate further given the SG commercial timeline?

---

*Sources: [AIO wiki log](file:///Users/michaelbruck/janus/prime-radiant/ai-office/log.md) (entries since 2026-05-11) · [Janus Prime Radiant build hub](file:///Users/michaelbruck/janus/prime-radiant/ai-office/projects/janus-prime-radiant-build.md) · [Marketing Prime Radiant hub](file:///Users/michaelbruck/janus/prime-radiant/ai-office/projects/marketing-prime-radiant.md) · [Linear AI Registry team](https://linear.app/janusd/team/AIR)*
