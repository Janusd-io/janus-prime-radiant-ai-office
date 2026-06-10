---
type: source
source_type: meeting
title: AIO Standup 10 Jun 2026
slug: 2026-06-10-aio-standup
created: 2026-06-10
captured_by: jehad-altoutou
fireflies_id: 01KTR07R7XRJA9CAGX44XMJA5G
fireflies_url: https://app.fireflies.ai/view/01KTR07R7XRJA9CAGX44XMJA5G
attendees: [Michael Bruck, Jehad Altoutou, Andrew Soane]
duration_min: 43
audience: department
departments: [ai-office]
standup_skill_version: v3.24
parser_version: 3
related: [2969245116, 2956556122, 2917860817, 2926633922, 2956596446, 2956583393, 2939705098, 2928678309, 2906196174, 2983087073, 2983125505, 2983049194, 2983085570, 2983058290, 2983058318, 2983082619, 2983060623, AIR-161, AIR-160, AIR-83, AIR-86, AIR-10]
---

## Clean Meeting Summary

The team diagnosed the ISO/IMS documentation effort as stuck in a chicken-and-egg loop — the company has almost no documented processes, and Simon keeps anchoring every request back to the full IMS structure — and decided to de-emphasise the effort rather than keep spinning. The afternoon AIO/IT meeting was prepped: production handover criteria, the Microsoft Entra SSO constraint (which forces Monday Enterprise tier against AIO's Standard-tier needs), website hosting migration (Cloudflare DNS first, then CloudFront + Vercel), and moving Nomi/Accessify onto IT-managed VPS hosting. Andrew reported a Cowork failure — an 18-page deck PDF duplicated to 324 pages on export to Drive — which Michael took as proof that raw Cowork is too unguarded for most staff and a controlled front-end is needed. The AI Platform Engineer JD is finalised and going to Bonaventure via Mary-Ann. AI cost management was discussed at length: duplicate OpenAI company workspaces, Codex credit limits, console access for Jehad, and a per-user monthly AI budget (~$250/mo floated, Uber's $1,500 cap cited). Ann's budget approval workflow remains undefined; the session with her is deferred until she completes the budget itself.

## 🎯 Next steps — by next standup

- **Process Simon's ISO files into Prime Radiant and surface blockers to Claude** — Owner: Jehad | Due: 11 Jun | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983087073)
- **Set up Jehad access to OpenAI console + billing overview** — Owner: Michael | Due: today (after standup) | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983058318)
- **Re-enable Obsidian Git sync on Jehad's vault / resolve curator sync conflict** — Owner: Jehad | Due: today | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2906196174) (tracked as Update on the sync-investigation item)

## 📅 Next steps — this week

- **Discuss ISO/IMS de-emphasis with Teresa** — Owner: Michael | Due: 12 Jun | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983125505)
- **Prepare Nomi/Accessify VPS hosting handover to IT (freeze edits, clone, IT pays)** — Owner: Both | Due: 12 Jun | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983049194)
- **Reconcile duplicate OpenAI company workspaces (same email, separate balances)** — Owner: Both | Due: 12 Jun | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983082619)
- **Align with IT this afternoon**: handover criteria + Entra SSO ([Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2969245116)), SaaS approval requirements ([Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2956556122)), Monday tier conflict ([Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2956596446)), website hosting coordination ([Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2926633922)) — Owner: Both | Due: 10 Jun PM
- **Diagnose Cowork PDF duplication incident (Andrew's deck export)** — Owner: Jehad | [Monday](https://janusd-company.monday.com/boards/5095012818/pulses/2983058290) — mark Done when root-caused and fixed

## 🏔️ Next steps — longer horizon

- **Propose per-user monthly AI spend budget (fungible cap, ~$250/mo baseline)** — Owner: Michael | Due: 16 Jun | [Monday](https://janusd-company.monday.com/boards/5095012849/pulses/2983060623)
- **Website migration execution** (Cloudflare DNS → CloudFront + Vercel) — joint AIO/IT, sequenced after this afternoon's alignment | [Monday](https://janusd-company.monday.com/boards/5095012818/pulses/2917860817)
- **Headless Obsidian / containerised desktop test** — Michael experimenting; discussion tomorrow (no Monday item yet — exploratory)

## Decisions made

- De-emphasise the ISO/IMS documentation effort; AIO stops spending time on it. The blocker is identified (no documented company processes exist); the fix is department self-documentation, owned by ISO/CEO, not AIO. Michael to reset expectations with Teresa.
- Website hosting target stack: Cloudflare (DNS, first) → AWS CloudFront + Vercel (hosting/delivery), chosen explicitly for agent-manageability ("you can completely manage the website with Claude Code"). Joint AIO/IT project.
- Nomi/Accessify move to IT-owned VPS hosting: frozen for direct edits, cloned to IT systems, paid by IT, out of the AIO sandbox.
- Direction (not yet a project): raw Cowork is unsuitable as a direct interface for most staff; build a controlled environment / custom front-end isolating users from it. Managed/cloud-hosted approach favoured.
- Ann/budget requirements session deferred until Ann completes the budget itself.

## Findings / context

- ISO loop diagnosis: Simon is brilliant but lost — used to documenting pre-existing processes into an IMS, while Janus has nearly none documented (AIO is the exception; HR policy is the only official policy). Jehad's proposed mechanism: one-page explainer (what is a process/policy) → departments fill a processes/policies spreadsheet → only then the formal documentation file. Town hall flagged as the venue for the company-wide ask.
- Obsidian two-curator sync conflict: Jehad had sync off during a large local reorg (personal → prime migration); Michael's pushes conflicted (index conflict; Claude Code emitted terminal commands instead of pushing). ~15 min unresolved during standup. Reinforces the cloud-managed direction. Follow-up: full technical review/diagnostics of vault sync + Claude integration.
- Entra constraint: IT has standardised on Microsoft Entra (over Okta et al.) for company-wide SSO/IAM. Everything in production must support Entra at entry — forces Enterprise tiers (Monday is the live example). Registered as AIR-161.
- Budget workflow gaps (Ann): request → in-budget check → approval (approver unclear) → payment method (reimbursement vs direct pay vs approved vendor — unthought-through). General lesson: the team doesn't think in processes; AIO/software people do.
- AI cost notes: Codex hit credit limits despite subscription; two OpenAI company workspaces under one email, each with balances; model choice is the main cost lever (4o-mini/nano cheap; Pro tiers expensive); per-user caps with fungibility floated.
- ATS: filtering capability already implemented on the Assessify HR platform — no external ATS needed when the careers section goes live (Andrew's advice: don't rush an ATS).

## Monday items touched

✅ 17 items, ⚠️ 0 backfilled, ➡️ 0 move-rationales, ❌ 0 coverage failures

Updated (source bump where applicable + meeting Update): 2969245116 (IT handover criteria), 2956556122 (SaaS approval Wednesday meeting), 2917860817 (hosting investigation), 2926633922 (Cloudflare+Vercel coordination), 2956596446 (Monday rollout scope), 2956583393 (SaaS approval + budgeting process), 2939705098 (AIO hire JD), 2928678309 (agent harness approach), 2906196174 (Obsidian sync investigation).

Created (all with Description Updates): sub-items 2983087073 (process Simon's files), 2983125505 (Teresa discussion), 2983049194 (Nomi VPS handover); parent 2983085570 (AI usage cost management) + sub-items 2983058318, 2983082619, 2983060623; parent 2983058290 (Cowork PDF incident — Marketing group, per Jehad's routing).

## External / Other-Department Follow-ups

- **Careers section on the website** — Owner: Marketing (Andrew) | Monday: excluded by AI Office Ownership Gate
- **Department process/policy self-documentation rollout + town hall announcement** — Owner: ISO (Simon) / CEO (Bonaventure) | Monday: excluded by AI Office Ownership Gate
- **JD approval** — Owner: Bonaventure (via Mary-Ann) | Monday: excluded by AI Office Ownership Gate (AIO's JD-drafting item 2939705098 updated instead)
- **Budget definition itself** — Owner: Ann (Finance) | Monday: excluded by AI Office Ownership Gate (AIO supports via 2956583393)

## Linear AIP reconciliation

No transcript-authorised AIP changes — skipped (no AIP issues referenced; conflict safety honoured).

## AI Registry / Tool Evaluation outcomes

- **AIR-161 Microsoft Entra (Entra ID)** — created (Backlog, High). IT-adopted company-wide SSO standard; no Gate 1 needed (adopted standard, not under competitive evaluation). Open: tier licensed (P1/P2/Suite), rollout sequence. Curator note: subagent suggests a `vendors/microsoft-entra.md` wiki page — high-stakes (new entity), needs a questions/ escalation before creation.
- **AIR-160 AWS CloudFront** — created (Backlog, Medium) + **Gate 1 PASS** (all five criteria; SSO via AWS IAM Identity Center federation, Slack via AWS Chatbot, IaC/API agent-operability, contractual no-training, published API). Stage 2 must settle the single content-delivery owner (CloudFront vs Cloudflare proxy vs Vercel edge) and AWS/IAM ownership. Recommendation: move to Evaluating.
- **AIR-83 Monday.com** — enriched: Enterprise-vs-Standard tier conflict (Entra SSO is Enterprise-only; AIO needs Standard features for Prime Radiant integration); sandbox-vs-company-account question. Status unchanged (Sandbox).
- **AIR-86 OpenAI Platform** — enriched: duplicate workspaces, Codex credit-limit collision (cross-ref AIR-84), billing access extension, per-user budget consideration. Status unchanged (Sandbox).
- **AIR-10 Claude** — enriched: Cowork adoption-failure evidence (Andrew's PDF incident) + controlled-environment direction. Status unchanged (Production). Open: should the controlled front-end be formalised as an AIP project?
