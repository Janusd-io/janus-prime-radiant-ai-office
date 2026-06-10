---
type: concept
title: Three ISO Standards
slug: three-iso-standards
created: 2026-05-08
updated: 2026-06-09
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
migrated_from: personal-obsidian-vault (07 ISO IMS PULS)
tags: [iso, standards, 9001, 27001, 42001]
---
# Three ISO Standards (and the supporting cast)

## The three core standards

| Standard | What it certifies | Maturity |
|---|---|---|
| **ISO 9001:2015** | Quality management — well-documented processes, well-run | Mature, widely adopted |
| **ISO/IEC 27001:2022** | Information security — data protection, cybersecurity, incident handling | Mature, widely adopted |
| **ISO/IEC 42001:2023** | AI governance — responsible management of AI systems, impact assessments, human oversight | **Brand new** — very few companies have it |

These three are **integrated** — one IMS satisfies all three, one audit covers all three, one certificate.

---

## ISO 9001:2015 — Quality

### What it requires (in plain English)

- Document every process: who does what, when, why
- Set objectives and measure performance against them
- Manage risks to product/service quality
- Run internal audits before external auditors arrive
- Hold formal management reviews
- Continuously improve based on findings

### Key clauses I keep referencing

| Clause | About |
|---|---|
| §7.5 | Documented information |
| §8.1 | Operational planning and control |
| §8.3 | Design and development of products and services |
| §8.4 | Control of externally provided processes/products/services |
| §8.5 | Production and service provision |
| §8.5.6 | Control of changes |
| §9.1 | Monitoring, measurement, analysis, evaluation |
| §9.1.3 | Analysis and evaluation |

### Figure 1 (slide 8 of Simon's deck)

The schematic ALL process documents must follow:

```
SOURCES OF INPUTS  →  INPUTS  →  ACTIVITIES  →  OUTPUTS  →  RECEIVERS
                                      ↑
                         Controls + Check points
                              Resources
```

Every one of the [[ims-process-documents]] follows this shape.

---

## ISO/IEC 27001:2022 — Information Security

### What it requires

- A risk-based approach to protecting information
- Documented information security policies (Annex A controls)
- Asset management (the AI Systems Register lives here)
- Supplier relationship management
- Incident management
- Continuous improvement of the security posture

### Key Annex A controls

| Control | About |
|---|---|
| A.5.7 | Threat intelligence |
| A.5.21 | Information security in supplier relationships |
| A.5.22 | Monitoring and review of supplier services |
| A.8 | Asset management |
| A.8.25–A.8.34 | Secure development |

---

## ISO/IEC 42001:2023 — AI Management

### What it requires (this is the new one)

- Document every AI system the organisation uses (the **AI Systems Register**)
- Run an **AI System Impact Assessment** for every AI system before deployment
- Establish governance: who approves new AI systems, who can decommission them, what policies apply
- Risk management specific to AI (bias, drift, hallucination, training data)
- Lifecycle management — from development through retirement
- Human oversight provisions

### Key clauses

| Clause | About |
|---|---|
| §6.1 | AI risk management |
| §8.2 | AI System Impact Assessment |
| Annex A | Lifecycle controls |

### How we satisfy 42001 today (already implemented)

| Requirement | Implementation |
|---|---|
| AI Systems Register | **Linear AIR** team — sole source of truth, written via [[standup|/standup]] dispatching `/ai-registry` |
| AI Impact Assessment | **`/ai-tool-evaluation`** skill runs Gates 1-4 — evaluation comments stored on each AIR-N issue |
| Auto-chained Gate 1 on new tools | `/standup` v3.10+ auto-chains evaluation when a new tool is registered — **no AI tool enters use without an Impact Assessment** |
| Lifecycle | AIR status transitions: Eval → Approved → Sandbox → Active → Suspended → Retired |
| Human oversight | Approval gates at Stage 4 (decision) and Stage 9 (re-evaluation) — see [[janus-puls-onboarding|repo file 08]] |

This is one of our strongest evidence claims for the audit.

---

## The supporting cast (from Simon's deck slide 18)

Standards beyond the core three.

### Applicable to Janus — certifiable

| Standard | Purpose |
|---|---|
| **ISO/IEC 27701:2025** | Privacy extension to 27001 — adds GDPR-style PII controls |
| **ISO/IEC 20000-1:2018** | IT service management — ITIL-style operations |
| **ISO 22301:2019** | Business continuity / disaster recovery |

### Applicable to Janus — non-certifiable / supporting

| Standard | Purpose |
|---|---|
| **ISO/IEC 27017:2015** | Code of practice for cloud information security |
| **ISO/IEC 27018:2025** | PII protection in public clouds |

### Client environment — certifiable (these are for the buildings Janus monitors, not Janus itself)

| Standard | Purpose |
|---|---|
| **ISO 50001:2018** | Energy management |
| **ISO 41001:2018** | Facility management |

---

## How an audit actually works

1. We pick a **Certification Body** — an external company (BSI, TÜV, DNV, LRQA, SGS, etc.) accredited to issue ISO certificates
2. They visit each site (Dubai, Singapore, UK) — physically or remotely
3. They ask: "show me how you do X" — where X is a process from our IMS
4. We open PULS (when built) → show the live process status → drill into Notion for the documented procedure → show records as evidence
5. They flag findings (major / minor / observations)
6. We respond to findings within agreed timeline
7. Once cleared, certificate issued — typically valid 3 years with annual surveillance audits

The whole point of PULS is making step 4 trivial.

---

## Related

- [[ims-process-documents]] — what each process must be documented as
- [[ims-open-questions-for-simon]] — selection of certification body is one of the open items
- [[janus-puls-onboarding|GitHub repo]] — all clause-mapping tables

← Back to [[iso-ims-puls]]

## Clause mapping (2026-06-09)
Every clause of ISO 9001 / 27001 / 42001 is cross-referenced against the 41 [[ims-process-register|IMS processes]] with per-clause evidence requirements in the [[ims-clause-comparison-matrix|ISO Clause Comparison Matrix]] (includes ISO 9001:2026 DIS + Amendment 1:2024). See [[ims-digital-twin]].
