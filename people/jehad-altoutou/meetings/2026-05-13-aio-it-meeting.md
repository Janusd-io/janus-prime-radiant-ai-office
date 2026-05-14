---
type: source
source_type: meeting
title: "AIO, IT Meeting"
slug: 2026-05-13-aio-it-meeting
created: 2026-05-13
captured_by: jehad-altoutou
attendees: [michael-bruck, jehad-altoutou, michael-bruck, jehad-altoutou]
duration_min: 48
fireflies_id: 01KRGGC9NR73YCVW11HC68XDHM
audience: department
departments: [ai-office, it-ops]
dept_scope: [ai-office, it-ops]
sensitivity: dept
task_tracker: monday
parsed_at: "2026-05-14T09:51:32Z"
parser_version: 2
summary: "Michael Bruck walked the IT-Ops attendees through the Janus Prime Radiant concept — a federated Obsidian-based personal/department/company knowledge brain inspired by Andrej Karpathy's LLM Wiki gist — showing Jehad's vault as the worked example"
topics: [janus-prime-radiant, obsidian-vault, google-drive-blocker, github-substrate-migration, andrew-onboarding, iso-automation, claude-cowork-licensing, federation]
decisions: [2026-05-13-migrate-prime-radiant-substrate-from-google-drive-to-github, 2026-05-13-onboard-andrew-soane-as-first-cross-dept-prime-radiant-pilot, 2026-05-13-defer-github-paid-tier-pending-bonaventure-approval, 2026-05-13-presentations-default-to-html-not-pptx]
action_items_count: 5
confidence_overall: medium
---

# AIO, IT Meeting

**Date:** 2026-05-13
**Attendees:** [[michael-bruck]], [[jehad-altoutou]], [[michael-bruck]], [[jehad-altoutou]]
**Duration:** 48 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KRGGC9NR73YCVW11HC68XDHM)

---

## Summary

Michael Bruck walked the IT-Ops attendees through the Janus Prime Radiant concept — a federated Obsidian-based personal/department/company knowledge brain inspired by Andrej Karpathy's LLM Wiki gist — showing Jehad's vault as the worked example. The meeting surfaced a hard blocker discovered that morning: Obsidian vaults cannot run on Google Shared Drive because Drive streams file content on demand, so Claude Code/Cowork sees directory listings as empty until each file is clicked. The team decided to migrate the substrate from Google Shared Drive to GitHub (using the Obsidian Git plugin with ~5-minute auto-sync), citing version control, audit trail, and per-account access control as additional wins. GitHub free tier is the starting point; a paid upgrade (~$4/user/month) is needed for branch protection but is parked pending Bonaventure's approval. Andrew Soane is the next person to onboard (he is a team of one preparing for a Singapore roundtable event next month); IT-Ops and project management are queued as subsequent co-creators after Andrew's flow stabilises. Open questions remain on how non-Claude-licensed users will contribute (possible MCP server exposing the vault to Gemini, or a cheaper Claude tier), and on cross-department shared directory creation being automated by the /janus-brain skill.

## Decisions

- [[2026-05-13-migrate-prime-radiant-substrate-from-google-drive-to-github]] — Migrate Prime Radiant substrate from Google Shared Drive to GitHub
- [[2026-05-13-onboard-andrew-soane-as-first-cross-dept-prime-radiant-pilot]] — Onboard Andrew Soane next as the first cross-dept Prime Radiant pilot
- [[2026-05-13-defer-github-paid-tier-pending-bonaventure-approval]] — Stay on GitHub free tier until Bonaventure approves the paid upgrade
- [[2026-05-13-presentations-default-to-html-not-pptx]] — Default to HTML output for presentations instead of PowerPoint

## Action items

- [ ] @jehad-altoutou Migrate Jehad's personal Prime Radiant vault from Google Shared Drive to GitHub. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Write the bootstrap script that automates the GitHub-based Prime Radiant setup for a new user. (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Extend the /janus-brain skill to create the shared GitHub directory and structure automatically when it's missing. — Monday
- [ ] @andrew-soane Stand up Andrew's Prime Radiant on the new GitHub substrate so it is usable for his Singapore roundtable event preparation. (raised by @michael-bruck) — Monday
- [ ] @andrey-timokhov Re-send or follow up on the Janusd-io GitHub organization invite to the user who has not yet accepted ('Les-Lesender'-style mishear in transcript). (raised by @michael-bruck) — Monday

## 🎯 This week

- @michael-bruck Get Andrew Soane's Prime Radiant up and running, then encapsulate the from-scratch onboarding process before opening it to IT-Ops and project management.
- @team Try out Monday's enterprise/AI demo on Monday and assess whether the gap between it and the AIO's own tooling is small enough to be worth adopting. (raised by @michael-bruck)
- @jehad-altoutou Start a new Claude project for Jehad's own work because the existing 'LLM wiki' project is auto-writing to itself and cannot be deleted in place.

## 🏔️ Long horizon

- Federate the per-person and per-department Prime Radiant vaults into a company-wide digital knowledge twin where each instance can share insights through dedicated shared directories without exposing private content. (owner: @michael-bruck)
- Roll the Prime Radiant out department by department, with HR last because of personnel-file sensitivity, while building privacy controls that prevent personal material from migrating upward. (owner: @michael-bruck; horizon: quarter)
- For non-Claude-licensed contributors, expose the Prime Radiant vault as an MCP server so other LLM tools (e.g. Gemini) can read it without giving every user a Claude license. (owner: @michael-bruck; horizon: weeks)
- Build a dashboard layer on top of the Prime Radiant to surface insights for users who don't directly work in Claude. (owner: @michael-bruck)
- Use the Prime Radiant as the source knowledge that generates ISO/IMS documentation automatically (Jehad's ISO automation feeds from the wiki). (owner: @jehad-altoutou; horizon: quarter)

## Findings

- Google Shared Drive streams file content on demand, so Claude Code / Claude Cowork sees a directory listing but reads file bodies as empty until each file is clicked — this makes Google Shared Drive unworkable as the substrate for an Obsidian-based vault. (stated by @michael-bruck)
- GitHub gives the vault version control, an audit trail, and per-account access control, and protects against accidental deletion in a way Google Drive does not without a separately implemented backup. (stated by @michael-bruck)
- Jehad's personal Prime Radiant currently holds ~5,000 files and still captures only a small fraction of his total knowledge — the substrate scales but personal context is much larger than even an aggressive ingest covers. (stated by @michael-bruck)
- The Prime Radiant's efficiency win over a traditional RAG + vector-database setup is that the LLM scans frontmatter and wikilink edges before pulling file bodies — progressive disclosure that keeps the context window small and avoids re-running the embedding pipeline on every query. (stated by @michael-bruck)
- Generating PowerPoint via Claude is expensive because the model has to invoke a Python skill, whereas HTML output is cheap and fast; one AIO user (Simon, referenced) hit Claude usage limits primarily from generating PowerPoint after PowerPoint. (stated by @michael-bruck)
- RAG and vector databases are falling out of favour for agent workloads because every agent step would have to regenerate retrieval, which is expensive — the wiki/compile pattern is the cheaper alternative. (stated by @michael-bruck; confidence: medium)
- The whole prototype was built in roughly one week of AI-time effort starting from Karpathy's LLM Wiki gist as the inspiration. (stated by @michael-bruck)
- Karpathy's LLM Wiki gist is deliberately abstract: it describes the pattern (ingest, query, lint) but leaves directory structure, schema, and tooling to the implementer's domain and LLM choice. (stated by @michael-bruck)

## Open questions

- How will non-Claude-licensed contributors interact with the Prime Radiant — through a custom desktop/web app fronting the Claude API, through MCP exposure of the vault to Gemini, or through cheap ($20-tier) Claude licences? (raised by @michael-bruck)
- How does a user feed their day-to-day non-Claude work (e.g. Gemini drafts, local files) back into the Prime Radiant so the brain stays comprehensive? (raised by @andrey-timokhov)
- Is GitHub the correct long-term place to store the institutional knowledge from a strategy and security perspective, or is it a stepping stone? (raised by @michael-bruck)
- Does the Prime Radiant work on Windows laptops, or has it only been validated on macOS so far? (raised by @andrey-timokhov)
- Should the company keep a Google Shared Drive at all for non-Prime-Radiant material (presentations, templates, policies), and if so, how is the boundary maintained? (raised by @euclid-wong)

## Blockers

- GitHub branch protection (and other paid-tier controls) cannot be enabled until Bonaventure approves the ~$4/user/month GitHub paid plan. (blocks: [[janus-prime-radiant-build]]; owner: @bonaventure-wong)
- Andrew Soane's Prime Radiant onboarding hit a blocker yesterday: Obsidian on a Google Shared Drive substrate doesn't work because Drive's on-demand streaming hides file bodies from Claude. (blocks: [[andrew-soane]]; owner: @michael-bruck)
- Simon Tarskih is the bottleneck on ISO/IMS work; documentation submitted to him three weeks ago is still pending review, blocking Jehad's ISO automation from moving forward. (blocks: [[iso-ims-puls]]; owner: @simon-tarskih)
- A GitHub organization invite to a teammate ('Les-Lesender' as transcribed) has not been accepted, blocking that user from joining the Janusd-io org workflow.

## Tool mentions

- [[obsidian]] — Database / front-end for the Prime Radiant vault
- [[github]] — New substrate for the Prime Radiant vault, replacing Google Shared Drive
- [[obsidian-git]] — Obsidian plugin doing five-minute push/pull syncs to GitHub
- [[google-drive]] — Old substrate, deprecated for the Prime Radiant because of on-demand file streaming
- [[claude-cowork]] — Primary user interface for working inside the Prime Radiant vault
- [[claude-code]] — Alternative interface used by Jehad through VS Code and CLI mode
- [[claude-api]] — Possible backend for a custom harness so users without a Cowork licence can still contribute
- [[gemini]] — Discussed as a possible read-only consumer of the vault via MCP
- [[notebooklm]] — Compared unfavourably as a less-controlled alternative to the Prime Radiant
- [[monday-com]] — AIO project tracking; an enterprise/AI Monday demo is happening Monday and the team will assess the gap
- [[linear]] — System of record for the AI Tools Registry that feeds the AIO Prime Radiant
- [[fireflies]] — Source of meeting transcripts ingested into the Prime Radiant
- [[obsidian-web-clipper]] — Captures interesting articles into the Inbox for ingest

## Topics

- janus-prime-radiant
- obsidian-vault
- google-drive-blocker
- github-substrate-migration
- andrew-onboarding
- iso-automation
- claude-cowork-licensing
- federation

## Related

- Project: [[janus-prime-radiant-build]] — Primary subject of the meeting — the program owning the substrate migration and federation roadmap.
- Project: [[iso-ims-puls]] — Discussed at the end: Jehad's ISO automation will feed from the Prime Radiant once the substrate stabilises; Simon is the bottleneck.
- Concept: [[llm-wiki]] — Karpathy's gist is the explicit inspiration — Michael recounts how he handed it to Claude and got the prototype in a day.
- Person: [[andrej-karpathy]] — Originator of the LLM Wiki pattern that inspired the Prime Radiant.
- Person: [[andrew-soane]] — Next person to onboard onto the Prime Radiant; team-of-one pilot tied to a Singapore roundtable event.
- Person: [[bonaventure-wong]] — Holds the budget approval for the GitHub paid tier.
- Person: [[simon-tarskih]] — Cited as the ISO-work bottleneck; also flagged as hitting Claude usage limits from PowerPoint generation.
- Vendor: [[github]] — Chosen new substrate — version control, audit, account-based access.
- Vendor: [[google-drive]] — Deprecated substrate; streaming-on-demand behaviour breaks Obsidian / Claude vault access.
- Vendor: [[obsidian]] — Vault front-end / database layer for the Prime Radiant.
- Vendor: [[monday-com]] — Has an upcoming enterprise/AI demo the team will attend to evaluate the gap.
- Concept: [[retrieval-augmented-generation]] — Discussed as the alternative pattern the Prime Radiant deliberately moves away from for agent-era workloads.
- Concept: [[model-context-protocol]] — Floated as the integration surface for letting non-Claude tools (Gemini) read the vault.

---

## Transcript

See [[2026-05-13-aio-it-meeting.transcript|full transcript]]
