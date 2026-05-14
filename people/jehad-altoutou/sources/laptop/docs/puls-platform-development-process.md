---
type: source
source_type: laptop
title: PULS-Platform-Development-Process
slug: puls-platform-development-process
created: 2026-05-08
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Desktop/PULS-Platform-Development-Process.docx
original_size: 24722
original_ext: .docx
category: docs
extracted_with: pandoc
extracted_at: "2026-05-14T09:51:42Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Jehad's PULS process doc for platform development — dept-shareable IMS work artefact, uses Assessify as worked example"
project: desktop-captures

---
<!-- jb:project-callout -->
> Part of [[desktop-captures|Desktop Captures]] — automatically linked by /janus-brain.


# PULS-Platform-Development-Process

> Part of [[desktop-captures|Desktop Captures]] — captured by /janus-brain.

_Extracted from `Desktop/PULS-Platform-Development-Process.docx` on 2026-05-14._

# [[platform-development-process|Platform & Tool Development Process]]

**How a new internal platform — a custom tool, not a third-party
purchase — goes from “we have a problem” to “live for the company” at
Janus Digital.**

> This is the long-form sibling of
> [07-MEETING-TO-TASK-WORKFLOW.md](./07-MEETING-TO-TASK-WORKFLOW.md) and
> [08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md).
> Where 07 is “small task → ship” and 08 is “evaluate someone else’s
> tool”, this document covers “build a whole platform from scratch when
> no good off-the-shelf option exists.” Worked example throughout:
> **[[assessify|Assessify]]** — the HR assessment platform we built when manual hiring
> assessments became a bottleneck.

| Field | Value |
|----|----|
| **Process Owner** | Jehad — AI Operations Engineer |
| **Covers IMS processes** | C1 AI System Design & Development · C2 Software Development & Release · S2 IT Infrastructure & Data Governance · A2 Intellectual Property Management |
| **Related ISO clauses** | 9001 §8.3 (design and development) · 9001 §8.5 (production and service provision) · 9001 §7.5 (documented information) · 27001 A.8 (asset management) · 27001 A.8.25-A.8.34 (secure development) · 42001 §6.1 (AI risk) · 42001 §8.2 (AI Impact Assessment for embedded AI components) |
| **Knowledge surface** | [[obsidian|Obsidian]] Vault (`/Users/jehad/Documents/Obsidian Vault/03 Projects/`) — every platform has a living project note · Graphify dumps for AI-agent consumption |
| **Source of truth for project state** | The Obsidian project note · the [[github|GitHub]] repo · the deployed instance |
| **Last updated** | 8 May 2026 |

------------------------------------------------------------------------

## 1. Why this process exists

Building a platform is not the same as building a feature. A feature
ships in days through the workflow in
[04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md). A platform takes
weeks-to-months and needs:

- A clear pain point that no third-party tool solves well enough (else
  the [Tool Evaluation Procedure](./08-TOOL-EVALUATION-PROCEDURE.md)
  applies instead)
- Strategic approval from leadership before sunk cost grows
- A deliberate stack choice that fits Janus’s standard tech stacks
- A [[knowledge-graph|knowledge graph]] that lets AI agents reason about the codebase as it
  grows
- An [[agentic-ai|agentic AI]] layer where useful (we’re an AI-first company — most
  internal platforms get one)
- A real handover to IT, not just a Docker container running on
  someone’s laptop

**The Assessify case (worked example):** HR was running hiring
assessments on manual spreadsheets. Inconsistent scoring, no analytics,
no audit trail, no automation, no fit with the rest of the AI-driven
recruitment pipeline. Off-the-shelf assessment platforms either lacked
the immersive UX we wanted or didn’t support the data flow we needed
(n8n webhooks, custom scoring, role-based RBAC, forms-as-code). So we
built it. Status today: sandbox-tested, n8n workflows wired, awaiting IT
handover for custom domain + HTTPS.

------------------------------------------------------------------------

## 2. The flow at a glance (ISO 9001:2015 Figure 1)

    flowchart LR
        SRC["<b>SOURCES OF INPUTS</b><br/>Pain point from a department<br/>Strategic priority (Michael)<br/>Gap left by tool evaluation (08)<br/>Regulatory or audit driver"]

        IN["<b>INPUTS</b><br/>Use case · stakeholders<br/>Existing tools surveyed<br/>Tech stack constraints<br/>Budget · timeline · success criteria"]

        subgraph ACT ["<b>ACTIVITIES</b> — 7 stages from pain point to live platform"]
            direction LR
            S1["1. Identify<br/>need"] --> S2["2. Scope &<br/>approval"]
            S2 --> S3["3. Stack<br/>selection"]
            S3 --> S4["4. Sandbox<br/>build (phased)"]
            S4 --> S5["5. Graphify +<br/>Obsidian sync"]
            S5 --> S6["6. AI / agentic<br/>layer"]
            S6 --> S7["7. Stress test +<br/>internal demo"]
            S7 --> S8["8. Document<br/>SOP + README + plan"]
            S8 --> S9["9. IT handover +<br/>company-wide deploy"]
        end

        OUT["<b>OUTPUTS</b><br/>Live platform · GitHub repo<br/>Obsidian project note (living)<br/>Graphify dump (AI consumption)<br/>SOP · README · implementation plan<br/>n8n workflows · MCP skills"]

        RCV["<b>RECEIVERS OF OUTPUTS</b><br/>Requesting department (end-users)<br/>IT department (operates it)<br/>All employees (eventual access)<br/>Internal Audit (full trail)<br/>AI agents (via Graphify + MCP)"]

        CTRL["<b>CONTROLS</b><br/>Build vs buy decision (08 first)<br/>Strategic approval gate (Michael)<br/>Stack alignment with existing stacks<br/>Phased build with control points<br/>[[5-area-stress-test|5-area stress test]] before handover<br/>Requester sign-off · IT acceptance<br/>Graphify before code review"]

        RES["<b>RESOURCES</b><br/>Stacks: SaaS Default · AI App · Creative Dev<br/>AI tools: Claude AI · [[openai|OpenAI]] · Codex · Antigravity<br/>Infra: [[hostinger|Hostinger]] VPS · Vercel · Neon · Docker<br/>Knowledge: Obsidian Vault · Graphify · /brain"]

        KPI["<b>MONITORING & MEASUREMENT</b><br/>Time pain-point → live (target ≤ 3 months) · Phase completion vs plan<br/>Stress-test pass rate · Defect rate post-IT · Adoption rate by requester<br/>AI components passing 42001 Gate 1 · Obsidian note freshness"]

        CTRL --> ACT
        SRC --> IN --> ACT --> OUT --> RCV
        RES --> ACT
        ACT -.-> KPI

        classDef ctrl fill:#FFF8D6,stroke:#996600,stroke-width:2px,color:#000
        classDef act fill:#E6F0FF,stroke:#1A4480,stroke-width:2px,color:#000
        classDef res fill:#FFE8E8,stroke:#990000,stroke-width:2px,color:#000
        classDef kpi fill:#E8F5E9,stroke:#1B5E20,stroke-width:2px,color:#000
        classDef neutral fill:#F5F5F5,stroke:#666,stroke-width:1px,color:#000

        class CTRL ctrl
        class ACT,S1,S2,S3,S4,S5,S6,S7,S8,S9 act
        class RES res
        class KPI kpi
        class SRC,IN,OUT,RCV neutral

------------------------------------------------------------------------

## 3. Stage-by-stage procedure

### Stage 1 — Identify need

| What happens | Output |
|----|----|
| A pain point is captured — usually surfaced in standup (Path A — see [07](./07-MEETING-TO-TASK-WORKFLOW.md)), via Slack, or directly from a department head | One-paragraph problem statement |
| Determine: is this a feature, an external tool, or a whole platform? | Decision: continue here only if “platform” |
| **Build vs buy gate** — first run the [Tool Evaluation Procedure](./08-TOOL-EVALUATION-PROCEDURE.md). Only proceed if no third-party tool clears Gates 1-4 for the use case | Documented “no fit” outcome on [[linear|Linear]] AIR if applicable |

**Assessify example:** Pain point — manual hiring assessments.
Build-vs-buy review — checked off-the-shelf platforms (none integrated
with n8n, none gave the immersive UX we wanted, none supported the data
model). Decision: build.

### Stage 2 — Scope & strategic approval

| What happens | Output |
|----|----|
| Draft a one-pager: problem · proposed solution · scope · success criteria · rough effort estimate · stack | One-page brief |
| Create the Obsidian project note from `_TEMPLATE.md` (path: `/Users/jehad/Documents/Obsidian Vault/03 Projects/<Name>.md`) | Living project note (status: planned) |
| Create the Linear AIP issue for tracking | Linear AIP-N issue |
| Present to Michael for strategic approval | Approval (or pivot / kill) recorded as comment on AIP issue |

**Control point:** No code is written before approval. Sunk cost stays
at one document.

**Assessify example:** Brief stated the goal as “Replace boring hiring
assessments with a premium, data-rich, automation-ready product. Serves
candidates (immersive UX) and internal teams (scoring, analytics,
webhooks, n8n).” Approved by Michael in mid-April 2026.

### Stage 3 — Stack selection

| What happens | Output |
|----|----|
| Pick from Janus’s defined tech stacks in Obsidian: `05 Tech Stacks/` (SaaS Default · AI App · Creative Dev) | Stack profile selected |
| Justify any deviation in the project note | Decision recorded |
| Confirm AI tooling — Claude API · OpenAI · AI Gateway · Codex · Antigravity | AI components listed |
| Run any new vendor through the [Tool Evaluation Procedure](./08-TOOL-EVALUATION-PROCEDURE.md) before committing | AIR entries created if needed |

**Assessify example:** Selected SaaS Default Stack (Next.js 16 + Prisma
v7 + SQLite + Tailwind v4 + shadcn/ui + Resend + Docker). Linked from
`Assessify.md` to `[[05 Tech Stacks/SaaS Default Stack]]`.

### Stage 4 — Sandbox build (phased)

| What happens | Output |
|----|----|
| Build in a phased plan: Phase 1A → 1B → 2A → 2B → … Each phase is a coherent vertical slice that’s testable end-to-end | Working code per phase |
| Build runs in an **isolated sandbox** — local Docker, ngrok exposure for stakeholder testing, never directly in production | Sandbox URL · ngrok tunnel |
| Each phase ends with a Progress Log entry on the Obsidian project note | Living changelog |
| Code lives in a private GitHub repo (under `Jehada-Janusd` org or personal) | GitHub repo |
| **Standing rule:** never wipe Docker volume (`docker compose down -v`) unless schema changed (per personal `[[01 User/Jehad]]` rule) | Data preserved across rebuilds |

**Assessify example (verbatim from project note):** - 2026-04-10 — Phase
1-2D complete (CRUD, preview, recommendation thresholds, score
calculator, duplicate, job-role management) - 2026-04-13 — Question Bank
section grouping + filtered import picker - 2026-04-14 — Admin user
invite system, RBAC, role badge, full README rewrite + SOP, production
hardening (HMAC tokens, rate limiting, audit logging, session expiry,
PDF export, backup script), analytics dashboard revamp, custom form
template builder - 2026-04-16 — n8n Bank Details + Personal Data
workflows + error handler workflow - 2026-04-17 — Docker + ngrok
verified live

### Stage 5 — Graphify + Obsidian sync

| What happens | Output |
|----|----|
| Run `/graphify <project_path> --update --obsidian --obsidian-dir <vault>/03 Projects/<Name>/` after each significant code change | Knowledge graph dump in vault |
| Graph notes capture: communities · god nodes · edges · cohesion scores · refactor candidates | AI-consumable architecture map |
| Project note’s “Architecture Quick-Map” section links to the graph communities | Navigation hub |
| AI agents read the graph **before** grepping source — ~2400× token reduction (benchmarked) | Faster, cheaper AI assistance |

**Assessify example (verbatim from project note):** Graph dump of 451 →
480 → 481 → 611 notes across iterations. Communities include API Routes,
Assessment Editor, Scoring Engine, Analytics, Auth, Email, Webhook
Dispatcher, File Validation, Easter Eggs.

### Stage 6 — AI / [[agentic-layer|agentic layer]]

If the platform benefits from agentic AI (most internal platforms do),
this stage adds it.

| What happens | Output |
|----|----|
| Identify the agentic surface: which workflows can an AI agent drive? | Agent boundary defined |
| Build n8n workflows for orchestration where event-driven automation fits | n8n workflow set |
| Build a [[claude-code|Claude Code]] skill OR an MCP connector for direct platform control by Claude / Cursor / agents | Skill file · MCP server |
| Register the AI components in Linear AIR (auto-handled if mentioned in standup; otherwise manual via `/ai-registry`) | AIR-N entries |
| Auto-chained Gate 1 evaluation runs (per [Tool Evaluation Procedure](./08-TOOL-EVALUATION-PROCEDURE.md)) | Gate 1 comments on AIR |

**Assessify example:** - n8n workflows hosted at
`https://n8n.srv1086109.hstgr.cloud` — webhook `POST` from Assessify
form submissions, switch on `formType`, branches for Bank Details and
Personal Data, [[google-drive|Google Drive]] upload, HTML → Google Doc conversion, Slack
notification, error handler workflow logging to Google Sheets + Slack -
MCP-driven peer skill: `[[assessify-hr]]` (path:
`/Users/jehad/Documents/Obsidian Vault/AI Office Brain/Skills/assessify-hr.md`)
— drives the full Assessify domain model (assessments, sections,
questions, job roles, departments, competencies, candidate invites,
sessions, candidates, lookup) directly from Claude - Naming convention:
British English in all assessment text · job role names match [[deel|Deel]] ·
competency names stable across roles

### Stage 7 — Stress test + internal demo

Apply the standard 5-area stress test from
[04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md):

| Area | What’s tested |
|----|----|
| **Functionality** | Every feature works under expected load · happy paths · edge cases |
| **UI / UX** | Usable · accessible · intuitive · responsive · consistent design |
| **Security** | Auth · authz · CSRF · rate limiting · audit logging · session integrity · file validation · secrets handling |
| **APIs** | Response times · error rates · payload validation · webhook signing · idempotency |
| **Stability** | Sustained-use behaviour · memory leaks · log volume · backup integrity |

Then run an **internal demo** with the requester (the HR team for
Assessify, etc.). Requester signs off that the platform meets their
original need.

**Assessify example:** 2026-04-16 — database cleaned for demo;
transactional data purged, structure preserved (1 admin, 4 depts, 6
roles, 4 templates, 3 form templates). Production hardening completed
prior. Currently in demo / testing phase.

### Stage 8 — Documentation (handover package)

Three artifacts must exist before IT handover:

| Document | Purpose | Lives in |
|----|----|----|
| **README** | Setup · run · key URLs · architecture overview · changelog | Repo root |
| **SOP** | Day-to-day operations · admin tasks · backup · restore · escalation paths | Repo `/docs/` or Notion |
| **Implementation plan** | Step-by-step deployment plan for IT · DNS · TLS · SSO · backups · monitoring · cost allocation | Notion or repo `/docs/deploy/` |

The Obsidian project note must also be updated with current state,
deployment URLs, and the final Open/Next list.

**Assessify example (verbatim):** Full README rewrite + SOP document
added on 2026-04-14. SOP v1.1 with 3 new sections. README updated with
security/PDF/team sections. Pending: implementation plan formalisation
for the IT custom-domain handover.

### Stage 9 — IT handover + company-wide deployment

| What happens | Output |
|----|----|
| AI Ops produces the handover package (Stage 8 outputs bundled) | Handover bundle |
| IT department reviews and accepts | Acceptance recorded on Linear AIP |
| IT provisions production: custom domain · TLS · SSO · backups · monitoring · cost allocation · access policies | Live deployment |
| Linear AIP issue moves to “Done” | Audit trail closed |
| Obsidian project note updated with production URLs and handover date | Living docs current |
| Requester (and originating channel if Slack-driven) receives final notification | Loop closed |
| Move to **continuous improvement** — bug fixes, feature requests, deprecations all flow through standup → tasks → builds | Next phase |

**Assessify example — current state:** waiting on IT for hosting
decision on the custom domain. Resend domain verification still uses the
free tier (sends only to `jehada@janusd.io`) until custom domain is
verified. Backup script `scripts/backup.sh` exists but cron not yet set
up on production host. **This stage is in flight as of 8 May 2026.**

------------------------------------------------------------------------

## 4. Worked example — Assessify, end to end

| Stage | What happened | Date | Linked artifact |
|----|----|----|----|
| 1\. Identify need | Manual hiring assessments — slow, inconsistent, no analytics, no automation | Pre-2026-04 | Internal HR conversations |
| 2\. Scope & approval | One-pager + brief; approved by Michael | 2026-04-13 | `[[03 Projects/Assessify]]` project note created |
| 3\. Stack selection | SaaS Default Stack (Next.js 16 · Prisma · SQLite · Tailwind v4 · shadcn/ui · Docker · n8n · Resend) | 2026-04-13 | Stack noted in Obsidian |
| 4\. Sandbox build | Phase 1-2D CRUD/scoring/analytics → RBAC + production hardening → form templates + PDF export | 2026-04-10 → 2026-04-17 | GitHub repo `HR-Assessment-Platform` |
| 5\. Graphify + Obsidian | Graph dumps at 451 → 480 → 481 → 611 notes; communities mapped | 2026-04-13 → 2026-04-17 | `03 Projects/Assessify/_COMMUNITY_*.md` |
| 6\. AI / agentic layer | n8n workflows (Bank Details · Personal Data · Error Handler); MCP-driven `[[assessify-hr]]` skill | 2026-04-16 → 2026-05-04 | `AI Office Brain/Skills/assessify-hr.md` |
| 7\. Stress test + demo | Production hardening complete (HMAC tokens · rate limiting · audit logging · session integrity · backup script). DB cleaned for demo. | 2026-04-14 → 2026-04-16 | Progress log on project note |
| 8\. Documentation | README v2 · SOP v1.1 · API docs page (`/admin/api-docs`) | 2026-04-14 | Repo + Obsidian |
| 9\. IT handover | **In flight** — awaiting IT decision on custom domain + HTTPS hosting | Pending | Open/Next on project note |

The point of the worked example: every stage of this process produced an
Obsidian artifact. The vault is the audit trail.

------------------------------------------------------------------------

## 5. Controls & check points

| Control | Where it fires | Why |
|----|----|----|
| **Build-vs-buy gate** | Stage 1 | Forces the [Tool Evaluation Procedure](./08-TOOL-EVALUATION-PROCEDURE.md) to run first — prevents reinventing wheels |
| **Strategic approval gate** | Stage 2 | No code before Michael’s approval — caps sunk cost at one document |
| **Stack alignment** | Stage 3 | Consistency across Janus platforms — auditor sees one architecture, not ten |
| **Phased build with control points** | Stage 4 | Each phase is shippable; failures don’t sink the whole project |
| **Sandbox isolation** | Stage 4 | No production data touches the build until handover |
| **Standing rule: no** `down -v` | Stage 4 | Prevents accidental data wipes — codified per personal rule, lives in Obsidian |
| **Graphify before review** | Stage 5 | AI-agent reasoning gets the architecture map before code-level grep — token cost discipline |
| **42001 Gate 1 on AI components** | Stage 6 | Auto-chained via standup workflow when components are registered in AIR |
| **5-area stress test** | Stage 7 | Functionality · UI/UX · security · APIs · stability — same bar as every other build |
| **Requester sign-off** | Stage 7 end | Tool can’t proceed to IT without the original requester confirming use case |
| **Documentation triad** | Stage 8 | README + SOP + implementation plan — IT cannot accept handover without all three |
| **IT acceptance gate** | Stage 9 | Tool cannot go company-wide without IT acceptance recorded |
| **Obsidian-as-living-docs invariant** | Throughout | Every stage updates the project note · note staleness is a process failure |

------------------------------------------------------------------------

## 6. Resources

| Resource | Detail |
|----|----|
| **Process Owner** | Jehad — AI Operations Engineer (accountable) |
| **Knowledge surface** | Obsidian Vault `/Users/jehad/Documents/Obsidian Vault/` — `03 Projects/` for project notes · `02 Skills/` for skill files · `05 Tech Stacks/` for stack profiles · `99 Graphify/` for graph dumps |
| **Graphify** | Binary at `~/.local/bin/graphify` · skill at `~/.claude/skills/graphify/SKILL.md` · `/brain` skill at `~/.claude/commands/brain.md` for project lifecycle management |
| **Standard tech stacks** | SaaS Default Stack (Next.js · Prisma · SQLite/Postgres · Tailwind · shadcn · Docker · n8n · Resend) · AI App Stack · Creative Dev Stack |
| **AI tooling** | Claude AI · OpenAI · Claude Code · Codex · Antigravity · AI Gateway |
| **Infrastructure** | Hostinger VPS (production · `n8n.janusd.io`) · Vercel (Next.js apps) · Neon Postgres · Docker · Cloudflare / [[godaddy|GoDaddy]] DNS |
| **Tracking** | Linear AIP team (project tasks) · Linear AIR team (AI tool / component registry) · Monday Automations board (`5095012818`) |
| **Per-project auto-memory** | `~/.claude/projects/-Users-jehad-<project>/memory/` — survives across all conversations, separate from main vault |

------------------------------------------------------------------------

## 7. Outputs and records

| Output | Where it lives | Retention |
|----|----|----|
| Obsidian project note | `03 Projects/<Project>.md` | Permanent · living |
| GitHub repo | `github.com/Jehada-Janusd/<Project>` | Permanent |
| Graphify dump | `03 Projects/<Project>/_COMMUNITY_*.md` and node notes | Permanent · refreshed per `--update` |
| Linear AIP issue | Linear AIP team | Permanent |
| Linear AIR entries (AI components) | Linear AIR team | Permanent |
| n8n workflow definitions | Self-hosted n8n at `n8n.janusd.io` (or per-project subdomain) | Backup script daily |
| MCP skills / Claude Code skills | `~/.claude/skills/` and `~/.claude/commands/` (or vault `02 Skills/`) | Permanent |
| README · SOP · implementation plan | Repo `/docs/` or Notion · linked from project note | Permanent |
| Production deployment | Per-project URL · IT-managed | Per IT retention policy |
| Auto-memory | `~/.claude/projects/-Users-jehad-<project>/memory/` | Permanent across conversations |

------------------------------------------------------------------------

## 8. KPIs (proposed for PULS dashboard)

| KPI | Target | Source |
|----|----|----|
| Time from problem statement → Stage 9 (live) | ≤ 3 months for medium platform | Linear AIP timestamps |
| Phase completion vs plan (per platform) | ≥ 90% phases shipped on time | Project note Progress Log |
| 5-area stress test pass rate at handover | 100% | Stage 7 records |
| Defect rate in first 30 days post-IT-handover | trended, target downward | Linear post-deploy issues |
| Adoption rate by requesting department | ≥ 80% within 30 days of go-live | Platform analytics |
| AI component coverage in AIR | 100% of embedded AI registered + Gate 1 evaluated | Linear AIR audit |
| Obsidian note freshness | last update ≤ 14 days for active projects | Vault file timestamps |
| Graphify dump freshness | refreshed within 1 week of major code change | Graph dump timestamps |
| Build-vs-buy decisions documented | 100% (every platform brief shows the buy-side review) | Linear AIP comments |

------------------------------------------------------------------------

## 9. ISO clause mapping

| Clause | How this process satisfies it |
|----|----|
| **ISO 9001 §8.3** Design and development of products and services | Stages 2-7 document inputs · controls · reviews · verification · validation · changes · outputs |
| **ISO 9001 §8.5.1** Control of production and service provision | Stage 9 plus continuous improvement loop |
| **ISO 9001 §7.5** Documented information | README · SOP · implementation plan · Obsidian project note · Graphify dump — all retained |
| **ISO 9001 §9.1.3** Analysis and evaluation | KPIs measured per platform; trends fed back into process improvements |
| **ISO 27001 A.5.7** Threat intelligence | Security tested at Stage 7 (5-area stress test); production hardening built into Phase plan |
| **ISO 27001 A.8** Asset management | Linear AIR registers all AI assets · Obsidian registers all platforms |
| **ISO 27001 A.8.25-A.8.34** Secure development | Phased build · sandbox isolation · stress test · documented standards (no-`down -v` rule etc) |
| **ISO 42001 §6.1** AI risk management | Stage 6 invokes Tool Evaluation Procedure (Gate 1-4) for every embedded AI component |
| **ISO 42001 §8.2** AI System Impact Assessment | Auto-chained Gate 1 evaluation when AI components are registered in AIR |

------------------------------------------------------------------------

## 10. Knowledge graph integration — why Obsidian is the spine

Janus’s platform process **runs on Obsidian as the living source of
truth.** Every platform produces:

1.  **A project note** at
    `/Users/jehad/Documents/Obsidian Vault/03 Projects/<Name>.md` with
    status, stack, decisions, progress log, n8n workflows, deployment,
    related skills
2.  **A Graphify dump** at `03 Projects/<Name>/` with `_COMMUNITY_*.md`
    files, node notes, edges — consumable by AI agents at ~2400× token
    efficiency vs raw source
3.  **Skill files** at `02 Skills/` (or `AI Office Brain/Skills/`) when
    an MCP / Claude Code skill drives the platform
4.  **Cross-links** to related stacks, references, learning resources,
    the personal user note `01 User/Jehad.md`

The `/brain` skill (`~/.claude/commands/brain.md`) manages the
lifecycle: `init` (create project note from template), `update` (sync
state), `recall` (semantic retrieval), `connect` (link to related
notes), `status` (health check).

**Why this matters for ISO:** the auditor doesn’t just see “we have
docs.” They see a continuously-updated knowledge graph that proves the
docs are *living*, that decisions trace to commits, that AI agents
reasoning over the codebase use the same source-of-truth as humans.
That’s a strong §7.5 + §9.1.3 evidence pattern.

------------------------------------------------------------------------

## 11. Open items for Simon (ISO Lead)

- Confirm Stages 2-7 satisfy the **§8.3 design and development**
  evidence requirement, or specify what additional documentation (design
  plan, design review records, etc.) is needed.
- Confirm the **Obsidian-as-living-docs** approach is acceptable as §7.5
  documented information, or whether a Notion mirror per platform is
  required for auditor accessibility.
- Confirm the **build-vs-buy gate** (Tool Evaluation Procedure run
  first) is sufficient evidence of supplier-control diligence per 27001
  A.5.21, or whether a formal documented decision template is needed.
- Decide whether platforms with embedded AI need a **separate AI Impact
  Assessment document per platform**, or whether the AIR-N entries plus
  Gate 1-4 comments from the Tool Evaluation Procedure suffice.
- Decide whether the **handover documentation triad** (README · SOP ·
  implementation plan) needs a fourth document — the auditor’s preferred
  “deployment runbook” style — or whether the existing three are
  sufficient.

------------------------------------------------------------------------

## 12. Relationship to other process documents

    [09] Platform Development Process  ◀── this file (long-form: build a platform from scratch)
           │
           ├── invokes ──▶ [08] Tool Evaluation Procedure (build-vs-buy at Stage 1, AI component eval at Stage 6)
           ├── feeds ──▶  [07] Meeting → Task → Build (continuous improvement post-Stage 9)
           ├── inherits ──▶ [04] Formal Response — 5-area stress test (Stage 7)
           └── audit-ready via ──▶ [06] First Voice — Q3 lists this entire stack as the AI Ops resource set

This document is intended to become the **Activities section of the C2
(Software Development & Release) IMS document**. Stages 1-9 here equal
the step-by-step procedure required by ISO 9001 §8.3.

------------------------------------------------------------------------

← Back to [README](./README.md) · See also:
[07-MEETING-TO-TASK-WORKFLOW.md](./07-MEETING-TO-TASK-WORKFLOW.md) ·
[08-TOOL-EVALUATION-PROCEDURE.md](./08-TOOL-EVALUATION-PROCEDURE.md) ·
[04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md)
