# Weekly call — talking points

**For:** Michael · **Call date:** 2026-05-18 · Bonaventure's three-block format.

---

## (1) Last week — what landed

**SG commercial layer went public.** White paper (BW + Joyce Woo co-authored) + campaign plan v1 (Andrew, 100 accounts mapped, 9-week plan to 8/9 July luncheon, ~S$24k budget) — strategy → operational artefacts in 3 days. Three-pillar messaging spine has a public surface. Joyce confirmed as **CEO, Singapore**.

**Drive → GitHub substrate migration executed.** AIO instance now on `Janusd-io/janus-prime-radiant-ai-office`, cloned locally. Brief + runbook (with bash script) shipped. Two orgs locked: `Janusd-io` for AIO+template, `Janusd-com` for every other department. CLAUDE.md v0.10 and v0.11 landed.

**PM Prime Radiant fully scoped.** Lysander walkthrough → 28-phase workflow captured as process page. Two structural lessons filed (AI bounded role, document-mgmt gap). Four entity pages (Lysander, Rosa Wu, Spike, Dhyey). Standup-proposal deck through 3 rounds — ready to share with Euclid / Rosa Wu / Lysander / Spike. **Windows-first deployment** for the first time.

**AIO ops:** mesh federation pairing AIO×Marketing stood up (first practical test). Standup skill v3.15 in production — writes direct to the Prime Radiant inbox (v3.16 needs to port off the Drive MCP connector now that we're on Git). **Notion deprecation end-May confirmed.** NotebookLM retired in favour of HTML decks. Brand guideline v1.0 from the official brand book. **11 tools moved through AIR**, mostly Marketing tooling for the SG campaign.

**Stakeholder signal:** BW's 11 May Prime Radiant shout-out ("happening quicker than I thought").

---

## (2) This week — to-do

- **Project Management PR kickoff** — deck out to Euclid/Rosa Wu/Lysander/Spike; scaffold the new vault on `Janusd-com`; Windows tooling install (~60–90 min).
- **Andrew's 1-week deliverables** (committed 12 May): ICP cross-tally with BW's, Personas, Topic Taxonomy — due ~19–20 May.
- **Target-list review** by BW + Joyce **by end-of-day Wed 20 May**.
- **SG landing page build** — blocked on website-architecture decision (open item below).
- **Jehad's first Git round-trip** → validate runbook → extract `prime-radiant-member-setup.md`.
- **AIR triage**: 11 tools added last week mostly Marketing-tooling (Mailchimp, Canva, LinkedIn Marketing, MS Clarity, Resend) — gating SG launch.
- **Drive webhooks API investigation** (replaces Kafka, which was overkill).
- **Schema linter scoping** + **ISO 27001 evidence-chain cross-linking** spec.
- **Notion deprecation runway** — every active surface needs dual-write or migration confirmed before end-May.

---

## (3) Open discussion — decisions I want from BW

1. **Website architecture (urgent, blocking landing page).** Three URLs in flight: `janusd.com` / `janusdg.com` / `janusd.sg`. My recommendation: `janusd.com` canonical + `janusd.sg` SG vanity, retire `janusdg.com`. Need this call this week. Andrew expects a "mighty battle."
2. **CRM scope.** Glorified-contact-list framing reshaped it. Target: ~2–3 weeks to recommendation, ~3 weeks impl, live by mid-June. Confirm marketing-CRM vs sales-CRM split is acceptable.
3. **Internal branding consolidation.** Prime Radiant / Nomi / brain / wiki / Pulse / PULS all in use. System name stays Prime Radiant; user-facing name open. Andrew should be in the conversation. 20-min decision.
4. **Andrew's external-agency scope.** BW flagged on 12 May that some of it could go in-house. Need to know which commitments to honour vs reshape.
5. **Personal vaults — when do they come back?** Shelved this week pending federation-redesign on Git. Affects `/janus-pulse` skill scope and the company-wide intro deck (currently overstated). Timing.
6. **Pacing check.** BW said "happening quicker than I thought." Calibration: is the current cadence right, or should AIO accelerate further given the SG July timeline?

**Signals worth flagging:**

- **Vivian Balakrishnan** keynoted AI Engineering Conf 16–17 May; runs his own LLM wiki on a Raspberry Pi. BW knows him personally. Potential gov-side advocate.
- **Yann LeCun's AMI has a Singapore office** (physical AI). Direct adjacency to Janus positioning.
- **Mnemon** — closest external system to Prime Radiant discipline at runtime. Single-source; tracking.

---

## If BW asks me

- *"What's the single biggest risk this week?"* → SG launch is gated on the website-architecture decision and the CRM-not-in-critical-path bet holding. If either breaks, the 8/9 July luncheon timeline slips.
- *"What did the substrate migration actually buy us?"* → Cowork sees real files on real disk (no Drive streaming-mount placeholder layer that broke Andrew's onboarding); GitHub auth decoupled from Workspace identity; substrate aligns with content discipline; federation via sibling clones matches the mesh pattern.
- *"How many Prime Radiant instances will be live by end of month?"* → AIO live; Marketing live; PM kicking off this week → 3 by 31 May if PM kickoff happens this week. ISO / HR / Finance / IT (proper, separate from PM) / Office-of-CEO / Engineering / Training still queued.
- *"What's the Notion-after-May story?"* → Standup skill v3.15 already writes to the vault inbox. Operations Notebook content gets dual-written / migrated by end-May. Any team still using Notion as a SoR after that needs to move.
