---
type: source
source_type: laptop
title: seven-section-template
slug: seven-section-template
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/references/seven-section-template.md
original_size: 6713
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.90
sensitivity_reason: "ISO/IMS reference doc — process document template; work content"
project: janus-puls-onboarding

---

# seven-section-template

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/references/seven-section-template.md` on 2026-05-14._

# The 7 Sections — What Goes Inside Each Process Document

> Every IMS process document at Janus has exactly these 7 sections. Source: slide 9 of Simon's IMS Development Programme deck. The names and order are non-negotiable.

| # | Section name | What goes in it | Where it comes from |
|---|---|---|---|
| 1 | **Controls** | Which laws, policies, and ISO clauses apply (UAE / Singapore / UK + the specific ISO clause numbers) | Defined in IMS Manual #1 (Policy Management), #4 (Change Management), #10 (AI Systems Impact Assessment) — applied at process level |
| 2 | **Inputs** | Trigger events, preceding process outputs, client requests, data feeds, scheduled intervals, system alerts | Captured per procedure during the interview |
| 3 | **Activities & control points** | Step-by-step sequence, decision points, responsibilities, escalation rules, approval gates, RACI per step | This *is* the procedure document (Level 3 in document hierarchy) |
| 4 | **Monitoring & measurement** | KPIs per process, target values, measurement frequency, dashboards, automated alerts | Visible in PULS live once the dashboard is built |
| 5 | **Resources** | Process Owner (accountable), team roles assigned, systems, tools, budget, training requirements | Captured per process — same content drives the Resource Requirements slide for the overall PULS programme |
| 6 | **Outputs & records** | Deliverables to next process or client, documented evidence, mandatory records retained in Notion, audit-ready records | ~55 records defined across the IMS (Level 5 in document hierarchy) |
| 7 | **Process Owner** | One named C-level (or designated lead) accountable for performance and compliance of this process | Assigned by leadership — must be a name, not a role |

## How to think about each section

### 1. Controls

> *"What rules does this process have to obey?"*

- ISO clauses (e.g., "ISO 9001 §8.1 Operational Planning")
- Internal policies (e.g., "Data Classification Policy v2.3")
- Jurisdictional regulations (e.g., "UAE PDPL," "UK GDPR," "Singapore PDPA")
- Contractual obligations to clients or partners

If you can't name a single Control, the process isn't really governed — it's just custom.

### 2. Inputs

> *"What triggers this process? What does it consume?"*

- **Trigger events** — a request arrives, an incident is reported, a scheduled job fires
- **Predecessor outputs** — another process produces something that becomes our input
- **Data feeds** — automated systems push data into us
- **Resource inputs** — budget allocation, team capacity, infrastructure access

Each input should map back to a Source from the Sources of Inputs section (1 of the 7).

### 3. Activities & control points

> *"What actually happens? Step by step. Who does what. Where are the checks."*

This is the longest section. It's a numbered table:

| # | Step | Description | Owner | Control point on exit |

The **control points** between steps are critical — they're the moments where work can stop and wait for review before proceeding.

For a parent process document, Activities are *the major activities* of the department (3-10 things). Each gets its own sub-process document.

For a sub-process document, Activities are *the step-by-step procedure* of one activity (4-10 steps).

### 4. Monitoring & measurement (KPIs)

> *"How do we know it's working?"*

A table:

| KPI | Target | Source | Frequency |

Common KPI types:
- **Time-based:** Lead time, cycle time, response time, time-to-handover
- **Quality-based:** Defect rate, rework rate, customer satisfaction, audit findings
- **Volume-based:** Throughput, completion rate
- **Cost-based:** Per-execution cost, monthly run rate

If your department doesn't track formal KPIs today, that's fine — list **proposed KPIs** for Simon to help formalise.

### 5. Resources

> *"What's needed to run this?"*

Five sub-categories:

- **People** — Process Owner, team roles, headcount
- **Infrastructure** — Physical buildings, servers, networks
- **Tools & systems** — Software, AI services, platforms. **For AI tools specifically:** every AI tool in use at Janus already lives in [[linear|Linear]] AIR (the AI Systems Register required by ISO 42001) because the AI department evaluates and registers each tool before any department starts using it. Other departments just list the tools they use; the AI department cross-checks AIR coverage.
- **Knowledge** — Internal expertise, external standards, documentation
- **Budget** — Annual envelope, cost categories

### 6. Outputs & records

> *"What does this process produce?"*

Two sub-categories:

- **Deliverables** — What we hand to the next process, client, or audit (services, products, decisions, documents)
- **Records** — Evidence retained for audit (deployment logs, approval records, test results, security scans)

Each record has a retention location and retention period.

### 7. Process Owner

> *"Who is accountable?"*

One name. Not "the team." Not "TBD." Not "shared." 

The Process Owner is the person who:
- Speaks for the process at audit
- Approves changes to the process
- Reviews KPI performance
- Decides corrective actions

For C-level processes, the Process Owner should be a department head or above.

## How the 7 sections relate to [[iso-9001-figure-1|ISO 9001 Figure 1]]

```
Figure 1 element              7-section number
────────────────────────────  ─────────────────
Sources of Inputs             implicit in §2 Inputs
Inputs                        §2 Inputs
Activities (the box)          §3 Activities & control points
Outputs                       §6 Outputs & records
Receivers of Outputs          implicit in §6 Outputs & records
Controls (top box)            §1 Controls
Resources (bottom box)        §5 Resources
Monitoring (dashed line)      §4 Monitoring & measurement
Owner (process box header)    §7 Process Owner
```

Some templates (including ours) split Sources/Receivers into their own sections for clarity, which gives you 9 sections in the document but still maps to the same 7 ISO-required elements.

## What auditors will check

- ✅ All 7 sections are present and populated
- ✅ Controls cite specific ISO clauses and jurisdiction-specific regulations
- ✅ Process Owner is a name, not a role
- ✅ Activities have control points
- ✅ KPIs have target values (or documented as "to be defined")
- ✅ Records have retention periods
- ✅ Resources list AI tools (the AI department independently verifies each one against Linear AIR coverage)

A missing or hand-waved section is an audit finding.

## Source

Slide 9 of Simon's IMS Development Programme deck.
