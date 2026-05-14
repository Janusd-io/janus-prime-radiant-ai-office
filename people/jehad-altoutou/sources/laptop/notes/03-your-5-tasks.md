---
type: source
source_type: laptop
title: 03-YOUR-5-TASKS
slug: 03-your-5-tasks
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/03-YOUR-5-TASKS.md
original_size: 7057
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.85
sensitivity_reason: "Onboarding task list for Jehad's PULS engagement; dept-relevant orientation material, no sensitive content."
project: janus-puls-onboarding

---
<!-- jb:project-callout -->
> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — automatically linked by /janus-brain.


# 03-YOUR-5-TASKS

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/03-YOUR-5-TASKS.md` on 2026-05-14._

# 03 — Your 5 Tasks

> The complete task breakdown. Read after the ISO lead has replied to the email in [02-DO-THIS-TODAY.md](./02-DO-THIS-TODAY.md).

---

## Task 1 — Fill your [[puls-first-voice|PULS First Voice]] form (15 minutes)

The ISO lead will send everyone a 6-question form. Don't wait — answer it now and send it back.

### The 6 questions

1. **Your work — inputs & outputs.** What kicks off your work? What do you produce? Who do you send it to?
2. **Controls and check points.** Where are the quality checks in your work?
3. **Tools & systems you use.** Every tool — feeds the AI Systems Register (a 42001 requirement).
4. **Your KPIs.** How do you know if you're doing well?
5. **What you need to work better.** What's blocking you — access, info, training, clarity?
6. **Your questions & ideas.** Anything you want to say.

### Already done — your real answers

Final answers (in your voice, based on how you actually work) are in **[06-FIRST-VOICE-FINAL.md](./06-FIRST-VOICE-FINAL.md)**. Just review and send when the ISO lead asks for the form.

For the long-form Figure-1 diagram version (same answers, in ISO 9001:2015 Figure 1 schematic format with full tables), see [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md).

---

## Task 2 — Lead the AI/IT tooling discussion (Step 4 on slide 17)

The ISO lead needs to decide **what software will Janus actually use to run the IMS and build PULS?** This is your meeting because you're the AI/IT person.

### Showing up with a recommendation

Don't show up empty-handed. Show up with a specific stack and a defensible reason for each choice.

The recommended stack (already drafted in [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md), section "PULS Tooling Proposal"):

| Layer | Tool | Why |
|---|---|---|
| Document of record | **Notion** | Already chosen by the ISO lead in slide 6 |
| Automation | **n8n** on [[hostinger|Hostinger]] VPS | Already running in production at `n8n.janusd.io` |
| PULS dashboard | **Next.js + Drizzle + Neon Postgres + Vercel** | Same stack as the AirWallex platform — proven |
| CAPA / audit findings | **[[linear|Linear]]** | Already used by the AI Projects team |
| Predictive layer | **Claude API** via AI Gateway | Existing skills + 42001 governance fits |
| Identity | **Clerk** | Vercel Marketplace, free under 10k MAU |
| Comms | **Slack** (Chat SDK) | Already integrated for AirWallex |

**Net new spend: ~$90-190/mo for v1.** Versus ~$2-5k/mo for a dedicated GRC platform.

### Indicative timeline

- Weeks 1-2 — Notion workspace + 20 process templates + AI Systems Register
- Weeks 3-4 — PULS dashboard MVP (3 pilot processes: M3 KPIs, C7 Incidents, M4 Internal Audit)
- Weeks 5-6 — First Voice ingestion → process documents drafted
- Weeks 7-8 — Remaining 17 processes onboarded + internal audit dry-run on Dubai-only scope
- Month 3+ — Multi-entity (SG, UK) deployment using the AirWallex template approach

---

## Task 3 — Find out if you're a Process Owner (5 min — ask Michael)

The ISO lead needs ONE C-level Process Owner per process. Three of them naturally fall on you because of your role:

- **C1 — AI System Design & Development**
- **C2 — Software Development & Release**
- **S2 — IT Infrastructure & Data Governance**

### What to ask Michael

> Quick one — ISO lead is going to assign Process Owners for the 20 IMS docs. C1, C2 and S2 line up with my work. Want me to take all three, split with you, or is one of them better elsewhere? Want to know before I write anything.

This unblocks Task 4. Don't start drafting process docs until you know which ones are yours.

---

## Task 4 — Write your process documents

For each process you own, write ONE Notion page using the **7-section template** from [01-START-HERE.md](./01-START-HERE.md).

### Time budget

- 2-4 hours per process if you actually know the work (you do for C1, C2, S2)
- The ISO lead will probably provide a Notion template — wait for it before drafting, otherwise you'll redo work

### Each document must have

1. **Controls** — relevant ISO clauses (9001 §X.X, 27001 Annex A.X.X, 42001 §X.X) + UAE/SG/UK regulations
2. **Inputs** — triggers, predecessor processes, data feeds
3. **Activities & control points** — step-by-step with RACI
4. **Monitoring & measurement** — KPIs with target values
5. **Resources** — Process Owner + team + systems + budget
6. **Outputs & records** — deliverables + evidence retained
7. **Process Owner** — your name, accountable

### Worked example

[04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md) has a complete example for "AI System Design, Development & Operations" (covers C1 + C2 + S2). Use it as the template skeleton.

---

## Task 5 — Build the actual PULS dashboard

The deck talks about PULS as if it exists. **It doesn't.** Someone has to build it. Given your role, that's likely you.

### Don't start until

- ✅ Task 2 is done — tooling decision is locked
- ✅ Task 3 is done — Process Owner assignments are clear
- ✅ Task 4 is in flight — at least 3 process docs exist to wire to
- ✅ The ISO lead has confirmed scope (full 20 processes vs. 3-process pilot first)

### Rough scope (v1 pilot — 3 processes)

```
Next.js 15 App Router (Vercel)
  ├── Auth: Clerk SSO (Vercel Marketplace)
  ├── DB: Neon Postgres (Drizzle ORM)
  ├── Reads from:
  │     ├── Notion API → process docs (cached)
  │     ├── Linear API → CAPA / audit findings
  │     ├── GitHub API → deploys, change failure rate
  │     └── n8n webhooks → operational signals
  ├── Routes:
  │     ├── /                → Org-wide health (traffic-light per process)
  │     ├── /process/[id]    → Drill-down per process
  │     ├── /entity/[id]     → Filter by Dubai / SG / UK / future
  │     └── /audit-pack      → One-click audit evidence export
  └── Scheduled:
        └── n8n cron → daily KPI roll-up + regulatory feed scan
```

### Scope creep watch

The ISO lead will be tempted to add features ("can it also do X?"). Stay disciplined: **3-process pilot first, then expand**. The deck's 6-month orientation timeline assumes a pilot-first approach.

---

## Order of operations summary

```
TODAY              → Send the 3-sentence email (file 02)
                       │
                       ▼
LATER THIS WEEK    → Task 1 (First Voice form)
                       │
                       ▼
LATER THIS WEEK    → Task 2 (tooling meeting — be ready with the proposal)
                       │
                       ▼
NEXT WEEK          → Task 3 (Michael confirms Process Ownership)
                       │
                       ▼
WEEKS 2-4          → Task 4 (write your process documents)
                       │
                       ▼
MONTH 2+           → Task 5 (build PULS dashboard — pilot first)
```

---

**Next:** [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md) — the formal Figure-1 diagram response (use after the kickoff meeting is scheduled).
