---
type: meeting
title: AIO × IT Weekly — Sandbox to Production Process
slug: 2026-06-10-aio-it-weekly-meeting
date: 2026-06-10
created: 2026-06-11
participants: [michael-bruck, euclid-wong, jehad-altoutou, andrey-timokhov, dhyey-mehta]
departments: [ai-office, it-ops]
attribution: confirmed
attribution_sources: []
---

# AIO × IT Weekly — 10 June 2026, 3:02 PM

**Participants:** Michael Bruck (AIO), Euclid Wong (IT lead), Jehad Altoutou (AIO engineer), Andrey Timokhov (IT/DevOps), Dhyey Mehta (IT).

**Attribution note:** All speaker labels in raw transcript are individual names (Michael Bruck, Euclid Wong, Jehad Altoutou, Andrey Timokhov, Dhyey Mehta). No conference room system account appears — attribution is clean and confirmed.

## Agenda context

Meeting convened to walk IT through the AIO tool pipeline (Linear AIR) and establish a formal sandbox-to-production handover process. First time the two teams have aligned on process in this format; prior approach was informal ("hey Andre, set up the APIs").

## AI Registry walkthrough

Michael walked Euclid, Andrey, and Dhyey through the Linear AIR pipeline:
- **Approved / Production**: current approved tool list (Zendesk, NotebookLM, Gemini, Google Cloud, Fireflies, Claude Console, etc.). Some entries stale — Asana being deprecated; Entra/SSO requirement noted as a gate criterion.
- **Backlog**: tools under initial enrichment (AI agent scrapes web, enriches with policy alignment, flags next actions). Cloudflare and Resend shown as examples.
- **Evaluation / Sandbox**: gate 1/gate 2 criteria explained — Google Workspace integration, Slack integration, data portability, documented API. Non-native Slack is acceptable if webhook/MCP path exists.
- Claude + AI system updates entries automatically from standup transcripts. IT team impressed; clarification that skill launch is manual not fully automatic.

## Prime Radiant / knowledge base discussion

Michael explained the Prime Radiant architecture to the IT team:
- All text, markdown files, git-backed on GitHub, synced via Obsidian Git plugin.
- Currently on Bonaventure's and Andrew's laptops. Andrew instance "a bit rough" (first deployment); Bonaventure's (Windows) working well.
- Key problem: **too brittle and fiddly for company-wide rollout.** Must move to cloud/VPS before scaling. Hostinger current infra; containerised cloud is the target.
- Euclid suggested a shared server; Michael confirmed: "That's exactly the direction we want to go."
- Obsidian has a headless mode but has its own issues — under evaluation.
- PM (Lysander/Rosa/Spike) is the priority rollout per Bonaventure, not Andrew first (plan changed after Emma meeting).
- IT team (Euclid, Andrey, Dhyey): **not prioritized for Prime Radiant right now.** Office/admin staff (Ann, Wisa) also not appropriate given technical skill requirements. Will revisit when containerised version is ready.
- Hiring an AI Platform Engineer to productize the system for company-wide robustness.

## Sandbox-to-production process (key outcome)

Agreed handover process for AIO-built tools going to IT production:

1. Tool or project built + tested in AIO sandbox (Hostinger dev environment).
2. IT team gets **named individual accounts** (per Jehad: named not generic, for accountability tracking). Andrey Timokhov and Dhyey Mehta added to Janusd-io GitHub org during this meeting.
3. IT stress-tests with their named accounts.
4. AIO provides: **GitHub repo** (read access) + **README** (installation + configuration dependencies) + **SOP** (usage manual) + **stress test log** + **version number**.
5. IT deploys to **separate production infrastructure** (Hostinger account distinct from AIO dev; IT owns it). Budget/server provisioning is IT's responsibility.
6. **Business user acceptance**: target user (e.g. Miriam for HR) must submit a Zendesk ticket confirming testing complete before IT considers it accepted.
7. **Feature requests**: business users file in Zendesk to IT → IT notifies AIO. Change requests require retesting + version bump before re-deployment.

First deliverable: **Assessify** (HR leave request tool, currently "done" in AIO but not yet deployed to IT production). Blocking item: Miriam has not yet filed a Zendesk acceptance request (Euclid raised this; Michael agreed to follow up).

## Next topics flagged

- Website + infrastructure: Cloudflare, Vercel, multi-region (Singapore IP), CMS selection — separate technical session to be scheduled between AIO + IT.
- CRM: Twenty CRM and Attio top contenders; Andrew's Martech stack the priority next.
- Quantum computing: Bonaventure forwarded something — acknowledged, not actioned.
