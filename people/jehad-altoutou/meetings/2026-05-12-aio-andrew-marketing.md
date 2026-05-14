---
type: source
source_type: meeting
title: "AIO, Andrew Marketing"
slug: 2026-05-12-aio-andrew-marketing
created: 2026-05-12
captured_by: jehad-altoutou
attendees: [michael-bruck, jehad-altoutou, andrew-soane]
duration_min: 96
fireflies_id: 01KRDXJX4SSA15S37XCCG7AWGA
audience: "departments:ai-office,marketing"
departments: [ai-office, marketing]
dept_scope: [ai-office, marketing]
sensitivity: dept
task_tracker: monday
parsed_at: "2026-05-14T09:51:32Z"
parser_version: 2
summary: "Michael walked Andrew through the Janus Prime Radiant / 'AI brain' system using an HTML deck Claude generated from prior context, and laid out a staged onboarding plan: get Andrew operational on Claude Cowork + Obsidian + Web Clipper pointing at a Marketing vault, then ingest existing Fireflies tran"
topics: [prime-radiant, marketing-onboarding, singapore-launch, crm-selection, website-architecture, messaging-pillars, claude-cowork, icp-personas]
decisions: [2026-05-12-start-marketing-prime-radiant-before-crm, 2026-05-12-reorder-marketing-outputs-plans-first, 2026-05-12-drop-factset-as-named-source, 2026-05-12-three-messaging-pillars-society-business-individual, 2026-05-12-treat-onboarding-deck-as-plan-of-record]
action_items_count: 10
confidence_overall: high
---

# AIO, Andrew Marketing

**Date:** 2026-05-12
**Attendees:** [[michael-bruck]], [[jehad-altoutou]], [[andrew-soane]]
**Duration:** 96 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KRDXJX4SSA15S37XCCG7AWGA)

---

## Summary

Michael walked Andrew through the Janus Prime Radiant / 'AI brain' system using an HTML deck Claude generated from prior context, and laid out a staged onboarding plan: get Andrew operational on Claude Cowork + Obsidian + Web Clipper pointing at a Marketing vault, then ingest existing Fireflies transcripts as a foundation, then layer CRM and automation. The two agreed to start narrow rather than wait on CRM selection, treating the deck as a living plan-of-record (eventually to be presented to Bonaventure). Andrew raised that he needs a single landing page live in days to support the Singapore launch campaign for an 8-9 July lunch, with form-capture into Google Sheets as an interim CRM. They debated multi-country site architecture (Andrew wants one CMS-backed gems.com with /singapore etc.; flagged a coming disagreement with Bonaventure who favours standalone country sites). Three messaging pillars for Janus were named: sustainability/SG agenda (society), AI as growth engine (business/capital), and augment/upskill people (individual). Fact Set was deprioritised as a named input source in favour of generic 'news/information gathering' including LinkedIn and Twitter. Andrew flagged he has draft ICP and personas he can complete within a week; reordering the Outputs list (plans/campaigns first, then briefs/positioning, then thought leadership) was agreed to push back internally on the 'marketing = white papers' framing.

## Decisions

- [[2026-05-12-start-marketing-prime-radiant-before-crm]] — Start Marketing Prime Radiant onboarding without waiting for CRM
- [[2026-05-12-reorder-marketing-outputs-plans-first]] — Reorder marketing Outputs list to put plans/campaigns first, white papers last
- [[2026-05-12-drop-factset-as-named-source]] — Drop FactSet as a named input source on the deck
- [[2026-05-12-three-messaging-pillars-society-business-individual]] — Adopt three messaging pillars: society, business, individual
- [[2026-05-12-treat-onboarding-deck-as-plan-of-record]] — Treat the HTML onboarding deck as the marketing plan-of-record

## Action items

- [ ] @andrew-soane Send Michael the light-hearted 'AI-powered' image so it can be used as the first LinkedIn post. (due: 2026-05-12; raised by @michael-bruck) — Monday
- [ ] @michael-bruck Use the AI-washing image as Janus's first LinkedIn post today. (due: 2026-05-12) — Monday
- [ ] @michael-bruck Feed this meeting's transcript to Claude and have it amend the onboarding deck based on Andrew's edits (reorder Outputs, drop FactSet, etc.). — Monday
- [ ] @andrew-soane Finish working drafts of the ICP and target personas documents so they can be loaded into the Marketing Prime Radiant. (due: 2026-05-19) — Monday
- [ ] @andrew-soane Schedule a hands-on session this week to install Claude Cowork, Obsidian, and Web Clipper on Michael's machine and point them at the Marketing vault. (due: 2026-05-15) — Monday
- [ ] @andrew-soane After tooling is set up, trigger a one-off backfill of Michael's Fireflies transcripts into the Marketing vault via the Fireflies MCP connector. — Monday
- [ ] @michael-bruck Verify and fix Claude connectors (Fireflies, HubSpot, etc.) after the warning that Claude can't reach them. (raised by @andrew-soane) — Monday
- [ ] @andrew-soane Stand up a single Singapore landing page (gems.com/singapore + gems.sg redirect) with a Google Form registration capturing leads into a Google Sheet, in time to start the campaign for the 8-9 July Singapore lunch. (due: 2026-07-08) — Monday
- [ ] @andrew-soane Build a shortlist of CMS options (Firebase, Wix, HubSpot, etc.) for the eventual gems.com rebuild so a vendor can be chosen alongside the CRM. — Monday
- [ ] @michael-bruck Reply to the HubSpot rep (Tony) to keep the CRM conversation alive while the internal evaluation runs. (raised by @andrew-soane) — Monday

## 🎯 This week

- @team Get Andrew/Michael operational on the Marketing Prime Radiant tooling stack (Cowork + Obsidian + Web Clipper) this week, while Bonaventure is on holiday from Wednesday. (raised by @andrew-soane)
- @andrew-soane Start the Singapore launch campaign workstream: paid ads, organic social, PR (Business Times), and white-paper promotion to drive registrations for the July lunch.
- @michael-bruck Begin drafting investor / asset-management decks and messaging / tone-of-voice doc that Bonaventure has asked for.

## 🏔️ Long horizon

- Build a peer-to-peer mesh of department Prime Radiants across Janus via shared sub-folders, so every department brain links into every other. (owner: @michael-bruck; horizon: quarter)
- Move off PowerPoint, PDFs, and NotebookLM in favour of HTML-as-deliverable across the AI Office, because HTML is cheap to generate, readable by Claude, and far better looking. (owner: @michael-bruck)
- Eventually abstract the Prime Radiant behind a custom dashboard so non-technical users never have to open the Obsidian vault or talk to Claude directly. (owner: @michael-bruck)
- Re-platform gems.com onto a proper CMS-backed, multilingual, multi-country site (gems.com/singapore, /uk, etc.) rather than building standalone country sites. (owner: @andrew-soane; horizon: quarter)
- Adopt a three-pillar Janus messaging spine (society / business / individual) that ultimately drives content, navigation, and tone across all marketing surfaces. (owner: @michael-bruck; horizon: year)
- Roll the Marketing Prime Radiant pattern out to other departments after Marketing proves it, then package the stack so it's installable beyond the early hand-held users. (owner: @andrew-soane; horizon: year)

## Findings

- LLMs systematically over-estimate the duration of operational setup tasks; Claude framed Marketing onboarding as 'weeks' when it should be days. (stated by @michael-bruck)
- Claude defaults to PowerPoint generation (via Python skills) when asked for a presentation, which burns disproportionate tokens; HTML is dramatically more efficient and better-looking. (stated by @michael-bruck)
- LinkedIn is in practice the single highest-signal intelligence source for Janus marketing, ahead of any paid news terminal; Twitter is the secondary channel. (stated by @andrew-soane)
- AI fatigue and AI-washing backlash are already starting in market; 'AI-powered' as a marketing claim is rapidly losing credibility. (stated by @michael-bruck; confidence: medium)
- Bonaventure favours standalone dedicated country websites; Andrew assesses this as a 'fool's economy' and expects a 'mighty battle' over multi-country site architecture. (stated by @andrew-soane)
- The Singapore lunch event is on 8-9 July 2026 — roughly 45-60 days out from this meeting — so lead-capture campaign must launch immediately. (stated by @andrew-soane)
- Bloomberg Terminal-grade financial data is ~$20k/month/seat and out of scope for Janus; FactSet is the 'poor person's Bloomberg' and was Bonaventure's suggested news source for asset-manager content. (stated by @michael-bruck)
- Capturing leads via Google Form into Google Sheets is sufficient interim CRM until HubSpot (or alternative) is selected; an agent can enrich the captured records later. (stated by @michael-bruck)

## Open questions

- Which CRM platform will Janus adopt (HubSpot vs alternatives), and on what timeline relative to the Singapore campaign? (raised by @andrew-soane)
- Which CMS will gems.com sit on once it's rebuilt to support multi-country, multilingual, CRM-integrated pages? (raised by @andrew-soane)
- How will the Prime Radiant onboarding work for Windows users on the team, given the install flow is currently Mac-only and well-rehearsed only on macOS? (raised by @andrew-soane)
- How do separate Cowork projects share memory back into the Prime Radiant vault — i.e. what's the canonical pattern when content work is done outside the vault-anchored project? (raised by @michael-bruck)
- Is the UK push still active enough to warrant marketing investment, or is it parked behind Singapore for now? (raised by @andrew-soane)
- What's the exact wording for the third messaging pillar (individual / augment+upskill people)? (raised by @michael-bruck)

## Blockers

- Jehad is blocked across multiple APIs (Notion, Obsidian, AI Office login all timing out), preventing further work today. (blocks: [[jehad-altoutou]])
- Michael's Claude connectors are throwing 'cannot connect' warnings, which will block the Fireflies-MCP backfill until fixed. (blocks: [[michael-bruck]]; owner: @michael-bruck)
- A full CRM-backed marketing flow is blocked on choosing a CMS and the additional investment a CMS rebuild of gems.com requires. (blocks: [[singapore-launch-campaign]]; owner: @andrew-soane)

## Tool mentions

- [[claude-cowork]] — primary IDE/agent surface Andrew will install on Michael's machine for the Marketing Prime Radiant
- [[obsidian]] — local vault viewer that surfaces the Prime Radiant markdown graph and links
- [[obsidian-web-clipper]] — Chrome extension that captures articles as markdown into the vault inbox for later ingest
- [[fireflies]] — source of meeting transcripts, to be backfilled into the Marketing vault via MCP connector
- [[hubspot]] — leading CRM candidate; rep Tony has been chasing the deal
- [[notion]] — Andrew may need access for a near-term Singapore asset; flagged that Claude defaults to Notion and that may be unnecessary
- [[factset]] — Bonaventure's suggested aggregated news source for asset-manager content; explicitly de-prioritised on the deck
- [[linkedin]] — named as Janus's single highest-signal marketing intelligence source
- [[linkedin-sales-navigator]] — mentioned alongside LinkedIn as a manual-input data source for the brain
- [[wix]] — candidate CMS / website builder; noted as largest hosting platform and paid tier removes branding
- [[firebase]] — candidate CMS / hosting backend to evaluate alongside Wix and others
- [[google-forms]] — interim lead-capture mechanism feeding a Google Sheet until the CRM is live
- [[google-sheets]] — interim store for captured Singapore-campaign leads
- [[google-drive]] — shared substrate where the Marketing vault directory lives and syncs
- [[notebooklm]] — compared unfavourably to HTML decks; on the list of formats Janus AIO wants to move away from
- [[bloomberg-terminal]] — reference point for the financial-data tier Janus cannot afford; FactSet was offered as cheaper alternative
- [[powerpoint]] — on the list of formats AIO is actively moving away from
- [[raspberry-pi]] — anecdote about California foreign minister demoing open Claude on a Raspberry Pi at an AI engineering conference

## Topics

- prime-radiant
- marketing-onboarding
- singapore-launch
- crm-selection
- website-architecture
- messaging-pillars
- claude-cowork
- icp-personas

## Related

- Project: [[janus-prime-radiant-marketing]] — primary subject of the meeting — onboarding Andrew into a Marketing instance
- Project: [[janus-prime-radiant-build]] — this meeting is a real-world test of the cross-instance Prime Radiant programme
- Project: [[singapore-launch]] — 8-9 July Singapore lunch and supporting campaign are the immediate driver
- Person: [[bonaventure-wong]] — non-attendee; CEO whose preferences (FactSet, country-specific sites) were referenced multiple times
- Person: [[andrej-karpathy]] — referenced as the inspiration for the open-Claude-on-Raspberry-Pi demo
- Person: [[tony-hubspot]] — HubSpot rep chasing Janus on the CRM deal
- Vendor: [[hubspot]] — leading CRM candidate
- Vendor: [[claude-cowork]] — core tooling for Marketing onboarding
- Vendor: [[obsidian]] — vault viewer to install on Michael's machine
- Vendor: [[fireflies]] — transcript source to be backfilled into the vault
- Vendor: [[linkedin]] — named as Janus's highest-signal intelligence source
- Vendor: [[wix]] — candidate CMS for gems.com rebuild
- Vendor: [[firebase]] — candidate CMS / hosting backend
- Vendor: [[factset]] — discussed and explicitly de-prioritised as a named input source
- Concept: [[ai-washing]] — discussed at length as a market backlash Janus should lean into satirically
- Concept: [[messaging-pillars]] — three Janus pillars introduced: society, business, individual
- Concept: [[ideal-customer-profile]] — Andrew has a draft and will complete it within a week
- Concept: [[buyer-personas]] — Andrew has draft target personas to finalise
- Concept: [[html-as-deliverable]] — core stance: HTML over PowerPoint/PDF/NotebookLM for AIO outputs
- Concept: [[federation]] — shared subfolder pattern between AI Office and Marketing Prime Radiants
- Country: [[sg]] — primary geographic focus of the launch and themes
- Country: [[gb]] — ABM-only mode for UK via Fairfax conversation, otherwise tabled

---

## Transcript

See [[2026-05-12-aio-andrew-marketing.transcript|full transcript]]
