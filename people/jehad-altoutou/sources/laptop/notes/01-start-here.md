---
type: source
source_type: laptop
title: 01-START-HERE
slug: 01-start-here
created: 2026-05-07
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/01-START-HERE.md
original_size: 5955
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "Plain-English explanation of Janus PULS/IMS programme — non-confidential dept reference material."
project: janus-puls-onboarding

---

# 01-START-HERE

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/01-START-HERE.md` on 2026-05-14._

# 01 — Start Here

> What the ISO lead's deck is actually asking for, in plain English.

---

## What's actually going on

**Janus Digital wants to get three ISO certifications at the same time, on one certificate, covering Dubai + Singapore + UK + future entities.**

The three certifications:

- **ISO 9001** — proves the company has a quality management system (good processes, well-run)
- **ISO 27001** — proves the company protects information securely (cybersecurity, data protection)
- **ISO 42001** — proves the company governs its AI systems responsibly (newest one, very few companies have it)

To get certified, an external auditor (a "Certification Body") will come in, ask "show me how you do X," and demand evidence. If you can show clean documents + live evidence that processes are followed, you pass.

## The ISO lead's plan

1. Write down **20 standard process documents** (one per area of the business — see below) in **Notion**.
2. Build a live dashboard called **PULS** that shows the real-time status of every one of those 20 processes.
3. When the auditor shows up, Janus opens PULS and says "look, every process is green, here's the evidence" — instead of scrambling for weeks like every other company.
4. Do this once for Dubai, then "deploy" the same system to every new branch (10 this year, 20/yr from 2027).

**That's it.** The whole deck — PULS, "Live · Visible · Trusted," Predictive Unified Live System, the heartbeat metaphor — is just a branded way of saying *"we're going to write down our processes properly and monitor them with software."*

---

## The 20 documents that must exist

Each of these gets ONE document in Notion. The deck calls them the "20 IMS documents."

### CORE — how Janus delivers value (10)

| # | Process | What it's about |
|---|---|---|
| C1 | AI System Design & Development | How AI features get designed and built |
| C2 | Software Development & Release | How code ships to production |
| C3 | Partner Enablement & Certification | How partners are onboarded and qualified |
| C4 | Customer Onboarding & Activation | How new customers go live |
| C5 | Service Delivery & Operations | How the live service is run day-to-day |
| C6 | Commercial Performance & Revenue | Sales pipeline and revenue management |
| C7 | Incident Management | How things-going-wrong are handled |
| C8 | Management of Outsourced Services | Managing third parties doing work for us |
| C9 | Procurement of External Providers | How we buy tools, services, subcontractors |
| C10 | Partner & Client Training | How we train people who use our stuff |

### SUPPORT — what keeps the business running (3)

| # | Process | What it's about |
|---|---|---|
| S1 | Control of Documented Information | How documents are stored, versioned, retired |
| S2 | IT Infrastructure & Data Governance | Servers, networks, data classification |
| S3 | Legal Compliance & Contract Management | Contracts, regulatory compliance |

### MANAGEMENT — leadership and oversight (5)

| # | Process | What it's about |
|---|---|---|
| M1 | Strategic Leadership & IMS Planning | Setting direction |
| M2 | Integrated Risk Management | Identifying and handling risks |
| M3 | Performance Monitoring & KPI | Measuring how things are going |
| M4 | Internal Audit | Auditing ourselves before the auditor does |
| M5 | Management Review & Corrective Action | Leadership reviews + fixing problems |

### ADDITIONAL (2)

| # | Process | What it's about |
|---|---|---|
| A1 | Marketing & Brand Management | How the brand is run |
| A2 | Intellectual Property Management | Managing IP, patents, trademarks |

**On top of these 20**, there's also an **IMS Manual** with 11 policy-level documents (Policy Management, Roles and Authorities, Objectives, Change Management, Competence, Awareness, Communications, Requirements for Products, Nonconforming Outputs, AI Impact Assessment, AI Data Management). Those are higher-level policies — not your problem unless you're explicitly asked.

---

## What goes INSIDE each of those 20 documents

For every one of the 20 documents, there are **7 things** that must be filled in. This is what slide 9 of the deck shows. These 7 sections are the ISO requirement.

| # | Section | Plain English |
|---|---|---|
| 1 | **Controls** | Which laws/policies/ISO clauses apply (UAE, SG, UK rules + the relevant ISO clause numbers) |
| 2 | **Inputs** | What kicks the process off — events, requests, data feeds, schedules |
| 3 | **Activities & control points** | The actual step-by-step of what happens. Who does what. Where the checks/approvals are. RACI per step. |
| 4 | **Monitoring & measurement** | The KPIs. Target values. How often we measure. What thresholds trigger alerts. |
| 5 | **Resources** | Who owns the process · team roles · systems used · budget · training needed |
| 6 | **Outputs & records** | What the process produces · what evidence gets retained as proof |
| 7 | **Process Owner** | One named C-level person who is accountable for that process |

**That's the structure.** Every one of the 20 documents looks the same. Same 7 sections. The auditor flips through them and ticks off the boxes.

---

## The schematic shape (slide 8)

The ISO lead and CEO want every reply to follow this shape — it's ISO 9001:2015 Figure 1:

```
SOURCES OF INPUTS  →  INPUTS  →  ACTIVITIES  →  OUTPUTS  →  RECEIVERS OF OUTPUTS
                                      ↑
                         Controls + Check points
                         monitoring & measurement
```

Every process answers: *what triggers it, what does it consume, what does it do step-by-step, what does it produce, who receives the output.* Plus: where are the quality checks, and what KPIs prove it's working.

A worked example for your AI Ops role is in [04-FORMAL-RESPONSE.md](./04-FORMAL-RESPONSE.md).

---

**Next:** [02-DO-THIS-TODAY.md](./02-DO-THIS-TODAY.md) — the one email to send today.
