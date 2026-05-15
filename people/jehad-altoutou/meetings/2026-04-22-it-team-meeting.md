---
type: source
source_type: meeting
title: IT team meeting
slug: 2026-04-22-it-team-meeting
created: 2026-04-22
captured_by: jehad-altoutou
attendees: [jehad-altoutou, speaker-2-unidentified, michael-bruck, speaker-4-unidentified]
duration_min: 100
fireflies_id: 01KPTE203THBDKJPZZF7HBMW9R
audience: department
departments: [ai-office, it-ops]
dept_scope: [ai-office, it-ops]
sensitivity: dept
task_tracker: monday
parsed_at: 2026-05-15T09:25:59Z
parser_version: 3
summary: The IT team reviewed in-flight infrastructure and tool evaluation work
topics: [hr-leave-platform, hostinger-vps, domain-transfer, openai-codex-eval, ai-rollout-strategy, rbac-zero-trust, disaster-recovery, n8n-self-host]
decisions: [2026-04-22-self-host-n8n-on-hostinger-over-gcp, 2026-04-22-reject-victor-ai-tool, 2026-04-22-evaluate-openai-codex-as-claude-fallback, 2026-04-22-defer-disaster-recovery-until-devops-hire, 2026-04-22-add-hr-platform-as-third-docker-container]
action_items_count: 7
confidence_overall: medium
---

# IT team meeting

**Date:** 2026-04-22
**Attendees:** [[jehad-altoutou]], [[speaker-2-unidentified]], [[michael-bruck]], [[speaker-4-unidentified]]
**Duration:** 100 min
**Fireflies:** [original meeting](https://app.fireflies.ai/view/01KPTE203THBDKJPZZF7HBMW9R)

---

## Summary

The IT team reviewed in-flight infrastructure and tool evaluation work. Jehad demoed the HR leave-request platform he built (live balances, Slack approvals via Nomi AI, PDF export with signatures) and walked the team through the Hostinger VPS that now runs n8n plus Docker containers, replacing a planned GCP deployment that was ~7x more expensive over two years. The team discussed transferring the janus.io domain (or just DNS management) from GoDaddy to Hostinger so Jehad can create the HR subdomain. They began evaluating OpenAI Codex as a Claude fallback after hitting Cloud Code usage limits, and Michael outlined a three-layer AI rollout vision (individual productivity, department-level, company-wide digital twin) — flagging RBAC / zero-trust access control as the unsolved engineering problem behind cross-department AI rollout. Disaster recovery (offsite backup, multi-region) was deferred until a dedicated DevOps hire. The team also rejected Victor as an AI tool because it leaks data across Slack channel members.

## Decisions

- [[2026-04-22-self-host-n8n-on-hostinger-over-gcp]] — Self-host n8n on Hostinger VPS instead of GCP
- [[2026-04-22-reject-victor-ai-tool]] — Reject Victor as an AI tool
- [[2026-04-22-evaluate-openai-codex-as-claude-fallback]] — Evaluate OpenAI Codex as a Claude Code fallback
- [[2026-04-22-defer-disaster-recovery-until-devops-hire]] — Defer multi-region disaster recovery until a DevOps hire is in place
- [[2026-04-22-add-hr-platform-as-third-docker-container]] — Run the HR platform as its own Docker container

## Action items

- [ ] @michael-bruck Pay for and provision the OpenAI Codex / Platform seats so Jehad and the team can begin sandbox evaluation — Monday
- [ ] @jehad-altoutou Fix the Dubai working-calendar / public-holiday handling in the HR leave-request platform — Monday
- [ ] @jehad-altoutou Investigate whether janus.io DNS management can be delegated from GoDaddy to Hostinger without transferring domain ownership, and proceed with whichever option works (raised by @michael-bruck) — Monday
- [ ] @jehad-altoutou Stand up an HR subdomain (e.g. hr.janus.io) on Hostinger and migrate the HR platform off the temporary NG Rock URL — Monday
- [ ] @jehad-altoutou Move Obsidian to the sandbox environment tomorrow morning (due: 2026-04-23; raised by @michael-bruck) — Monday
- [ ] @michael-bruck Onboard the Chinese-speaking multi-agent contributor onto Monday.com inside the janus.io workspace so he stops running company work on personal accounts — Monday
- [ ] @michael-bruck Migrate the multi-agent contributor's GitHub work from his personal account to the Janus GitHub org — Monday

## 🎯 This week

- @jehad-altoutou Wrap up the HR leave-request platform demo iteration so Marianne can start using it on a real domain
- @team Start using OpenAI Codex in the sandbox in parallel with Claude Code and produce comparison feedback (raised by @michael-bruck)
- @jehad-altoutou Get the AWS signature pictures fully migrated off Signature Hound and complete the email-signature audit

## 🏔️ Long horizon

- Roll AI out across Janus in three layers: individual productivity, department-level shared knowledge, and ultimately a company-wide digital twin federating across departments (owner: @michael-bruck; horizon: year)
- Solve role-based access control / identity access management for cross-department AI rollout — the unsolved engineering problem behind sharing AI tools across finance, IT, HR, marketing without leaking data (owner: @michael-bruck; horizon: quarter)
- Likely need to support all three major model families (Anthropic, OpenAI, Google) rather than standardising on Claude — competitive landscape suggests no single winner (owner: @michael-bruck; horizon: quarter)
- Hire a DevOps / infrastructure person before promoting any AI tooling from sandbox to production-grade with proper disaster recovery (owner: @michael-bruck; horizon: quarter)
- Reconsider Anthropic Enterprise plan once seat counts justify it — would give SSO via Entra, RBAC, per-feature controls (e.g. turn off computer-use for risky users) and prompt visibility (owner: @michael-bruck; horizon: weeks)
- Possibly buy janus.ai as a defensive domain registration to prevent squatting (owner: @michael-bruck)

## Findings

- GCP-hosted n8n was projected to cost roughly $70/month basic and scale to $4-5K/year, vs. roughly $900/year on a Hostinger VPS — a ~7x cost gap (stated by @jehad-altoutou; confidence: medium)
- Several Janus employee email signatures have broken mailto links — e.g. Euclid's signature still routes clicks to Bonaventure's address (stated by @speaker-2-unidentified)
- Signature Hound was hosting employee signature images on an external (non-Janus) domain; Jehad has now downloaded them and moved them into the Janus AWS account (stated by @jehad-altoutou)
- Claude Code hit a hard usage cap recently, requiring Euclid to top up the console balance manually — a real production risk if more teams depend on it (stated by @speaker-2-unidentified)
- Hostinger ships with AI/agent-controllable APIs, so the team can manage the VPS programmatically rather than via console clicks (stated by @michael-bruck; confidence: medium)
- Google reportedly making catching up to Claude a top priority under Sergey Brin; Google engineers are using Claude Code to build Google's own AI (stated by @speaker-2-unidentified; confidence: low)
- Hostinger Malaysia (Johor) data centres are scheduled to come online late 2026; current Hostinger presence is Singapore + Europe (stated by @speaker-2-unidentified; confidence: low)
- Bahrain-based cloud regions (Google, AWS) recently suffered a major incident — Abu Dhabi Commercial Bank took three weeks to recover; UAE government platforms (RTA, police) still degraded (stated by @michael-bruck; confidence: medium)
- OpenAI Codex is noticeably faster than Claude Code on query response and has a broader third-party integration catalogue (MCP, Gmail, etc.) (stated by @speaker-2-unidentified; confidence: medium)
- Janus Anthropic API tier is currently tier 1; tiers unlock at $100, with tier 5 being the cap — early usage may feel rate-limited (stated by @michael-bruck)
- Domain transfer of janus.io from GoDaddy to Hostinger costs ~$50 and includes a 2-year renewal (expiry 2028), but transfer requires unlocking at the registrar plus an EPP/auth code (stated by @speaker-2-unidentified)
- The HR leave-request platform now has live per-employee balances (Jehad's shows 16 days → 12 after a 4-day test deduction) wired into the approval flow (stated by @jehad-altoutou)

## Open questions

- Should Janus transfer janus.io ownership to Hostinger, or only delegate DNS management while keeping GoDaddy ownership? (raised by @michael-bruck)
- What is the minimum seat count for Anthropic Enterprise, and is it cheaper per seat than Team given volume discounts? (raised by @speaker-2-unidentified)
- How will Janus implement role-based access control across departmental AI tools so e.g. IT cannot reach finance data through a shared knowledge base? (raised by @michael-bruck)
- Where should offsite / cross-provider disaster-recovery backups for the Hostinger VPS live — Singapore, UK, Europe? (raised by @michael-bruck)
- Should Janus defensively register janus.ai before someone else squats it? (raised by @michael-bruck)

## Blockers

- HR platform cannot move off the temporary NG Rock URL until Jehad has DNS control over janus.io to create the hr.janus.io subdomain (blocks: [[hr-leave-request-platform]]; owner: @jehad-altoutou)
- Multi-agent contributor cannot deploy his system into the Janus sandbox until Michael provisions him on janus.io infrastructure (Cloud, ChatGPT, server) (owner: @michael-bruck)
- AI Projects automation work is on hold pending Simon defining the workflows it should automate (blocks: [[ai-projects]]; owner: @simon-tarskih)

## Tool mentions

- [[hostinger]] — self-hosting VPS now running n8n + Docker, replacing GCP plan
- [[n8n]] — workflow automation, now self-hosted on Hostinger sandbox
- [[openai-codex]] — evaluating as a Claude Code fallback; reportedly faster and better integrations
- [[claude-code]] — current primary coding agent; hit usage cap, requiring console top-up
- [[anthropic-enterprise]] — considered for SSO, RBAC, feature-level toggles; needs minimum seat count
- [[viktor]] — rejected AI Slack tool — leaks data across channel participants
- [[linear]] — AI Tools Registry source of truth; production vs sandbox lists reviewed
- [[monday-com]] — execution surface; replacing Asana for AI Office work; multi-agent contributor to be onboarded here
- [[asana]] — being phased out for Janus AI Office in favour of Monday
- [[godaddy]] — current registrar for janus.io; team weighing transfer to Hostinger
- [[ngrok]] — temporary tunnel currently fronting the HR platform; blocking proper rollout
- [[signature-hound]] — external signature service that was hosting images on its domain; Janus migrating images to AWS
- [[aws]] — Janus account; signature assets being moved in; Singapore region has 3 AZs
- [[gcp]] — evaluated and rejected for n8n hosting on cost + DevOps burden grounds
- [[tencent-cloud]] — previously considered as third option in n8n hosting bake-off
- [[perplexity]] — listed among AI tools being tested
- [[obsidian]] — to be moved to sandbox tomorrow
- [[cursor-ide]] — in the monitored / under-test list in Linear
- [[gemini]] — named as one of three model families Janus will likely need to support
- [[trae]] — Chinese Claude-Code-like tool tried by Speaker 3; not adopted
- [[kimi-code]] — Chinese tool briefly tried; not adopted
- [[microsoft-copilot]] — tried for Excel; team consensus that it is poor
- [[notebooklm]] — used to generate training videos; quality flagged as imperfect
- [[slack]] — approval channel for HR leave requests routed via Nomi AI
- [[fireflies]] — feeds morning standup transcripts into the AI Registry update flow
- [[notion]] — shared knowledge surface alongside Linear for AI Registry
- [[github]] — Janus GitHub org should hold the multi-agent contributor's repos, not his personal account
- [[nomi-ai]] — internal Janus AI handling HR leave-request routing between employee, line manager, and HR

## Topics

- hr-leave-platform
- hostinger-vps
- domain-transfer
- openai-codex-eval
- ai-rollout-strategy
- rbac-zero-trust
- disaster-recovery
- n8n-self-host

## Related

- Project: [[hr-leave-request-platform]] — primary demo subject — Jehad walked through it end to end
- Project: [[hostinger-vps-sandbox]] — newly stood up; hosting n8n, Docker, future HR platform
- Project: [[ai-tools-registry]] — Michael walked through the Linear production / sandbox / monitored / rejected lists
- Project: [[company-wide-ai-digital-twin]] — Michael's three-layer rollout vision referenced repeatedly
- Vendor: [[hostinger]] — platform of record for the new sandbox VPS
- Vendor: [[openai]] — Codex evaluation just kicked off
- Vendor: [[anthropic]] — current primary AI vendor; Enterprise plan under reconsideration
- Vendor: [[godaddy]] — current janus.io registrar — domain transfer discussion
- Vendor: [[monday-com]] — destination for multi-agent contributor's task tracking
- Vendor: [[viktor]] — AI Slack tool rejected on RBAC grounds
- Person: [[bonaventure-wong]] — referenced as manager of the multi-agent contributor and earlier RBAC concern about Cowork access
- Person: [[euclid-wong]] — had to manually top up Claude Code console; signature mailto bug mentioned
- Person: [[simon-tarskih]] — AI Projects automation work paused waiting on Simon's workflow definitions
- Person: [[marianne]] — HR contact specifying leave-form requirements; not on roster — likely external HR stakeholder
- Person: [[rosie]] — named as upcoming maternity-leave case validating the HR platform
- Concept: [[role-based-access-control]] — named as the unsolved engineering problem for cross-department AI
- Concept: [[zero-trust-security]] — framed by Michael as the model for AI access
- Concept: [[digital-twin-of-the-company]] — Michael's framing for the company-wide AI layer
- Concept: [[disaster-recovery]] — deferred until DevOps hire; Bahrain-region failure cited as cautionary tale

---

## Transcript

Raw transcript stays in Fireflies — fetch via MCP when needed.
Fireflies: [original meeting](https://app.fireflies.ai/view/01KPTE203THBDKJPZZF7HBMW9R)
