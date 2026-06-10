---
type: source
title: IMS Process Register — 41 processes, 4 categories, owners
slug: reg-ims-process-register
created: 2026-06-09
updated: 2026-06-09
source_type: document
source_origin: Google Drive — ISO/IMS department (Simon Tarskih)
document_id: REG-IMS-ProcessRegister
document_version: v0.5
document_status: DRAFT
captured_by: jehad-altoutou
departments: [ai-office, ims-compliance]
related: [ims-digital-twin, iso-ims-puls, three-iso-standards, ims-enrolment, simon-tarskih]
ingested_in_full: true
---

> Full-fidelity ingest of the ISO/IMS source document `REG-IMS-ProcessRegister v0.5` (DRAFT), received from Simon (IMS & Compliance) via Google Drive, 2026-06-09. Content preserved verbatim (pandoc/xlsx → markdown); not summarized.

# REG-IMS-ProcessRegister-v0.5-2026-05-18.xlsx


## Sheet: Process Register (48 rows)

| Janus Digital — IMS Process Register (DRAFT v0.5) |  |  |  |  |  |  |
| Standards: ISO 9001 / 27001 / 42001  \|  Status: DRAFT v0.5  \|  Date: 2026-05-18  \|  Changes from v0.4: Additional category dissolved. A1 Marketing & Brand Management → C15 (Core, value-chain top-of-funnel for C3). A2 Intellectual Property Management → S8 (Support, intangible-asset management alongside S2/S3). Total: 41 processes (13 Governance / 15 Core / 8 Support / 5 Management). |  |  |  |  |  |  |
| Code | Process name | Brief description (plain language) | Standard / clause | Proposed owner (Role [Status]; interim if any) | Your role | Comments |
| GOVERNANCE PROCESSES (13) |  |  |  |  |  |  |
| G1 | Policy Management | Creating, approving, communicating and updating company policies. How policies are written, reviewed and made known to staff. | ISO 9001 cl. 5.2; ISO 27001 cl. 5.2, A.5.1; ISO 42001 cl. 5.2, A.2 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| G2 | Management of Organisational Roles and Authorities | Defining who is responsible for what in the company. Assigning IMS roles, decision rights and accountability. | ISO 9001 cl. 5.3; ISO 27001 cl. 5.3, A.5.2-A.5.4; ISO 42001 cl. 5.3, A.3 | Chief Talent Officer [Hiring Aug 2026]; interim: HR Manager (Mariam) |  |  |
| G3 | Objectives Management | Setting measurable IMS objectives (quality, security, AI). Target-setting, monitoring progress, updating. | ISO 9001 cl. 6.2; ISO 27001 cl. 6.2; ISO 42001 cl. 6.2 | Global CEO (Bonaventure Wong) [Onboard] |  |  |
| G4 | Change Management | Managing changes to processes, systems, products or organisation in a controlled way — assessing risks before approving. | ISO 9001 cl. 6.3, 8.5.6; ISO 27001 cl. 6.3, A.8.32; ISO 42001 cl. 6.3 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| G5 | Competence Management | Ensuring staff have the right skills: defining required competencies, planning training, recruitment input, assessing competence and effectiveness. For multi-jurisdiction operations (Singapore, UK, UAE, future EU), competence requirements explicitly include cross-cultural collaboration capability, language proficiency where needed, and awareness of local professional norms. Includes wellbeing factors that materially affect work capability. | ISO 9001 cl. 7.2; ISO 27001 cl. 7.2, A.6.1-A.6.6; ISO 42001 cl. 7.2 | HR Manager (Mariam) [Onboard] |  |  |
| G6 | Awareness Management | Making staff aware of IMS policies, their role in IMS, and consequences of non-compliance. Includes awareness of cultural and psychological factors of the work environment — inclusion, respectful workplace, mental health resources, and channels for reporting concerns. | ISO 9001 cl. 7.3; ISO 27001 cl. 7.3, A.6.3, A.7.7; ISO 42001 cl. 7.3 | HR Manager (Mariam) [Onboard] |  |  |
| G7 | Communications Management | How we communicate IMS-related information internally and externally — what, when, who, to whom. | ISO 9001 cl. 7.4; ISO 27001 cl. 7.4; ISO 42001 cl. 7.4, A.8.5 | CMO (Andrew Soane) [Onboard] |  |  |
| G8 | Management of Requirements for Products and Services | Capturing customer, regulatory and internal requirements for products/services; ensuring they are met. | ISO 9001 cl. 8.2; ISO 27001 cl. 6.1, 8.1; ISO 42001 cl. 6.1, 8.1 | Head of AI Native (Michael) [Onboard] |  |  |
| G9 | Nonconformity Management | Handling nonconformities across the IMS — product/service outputs, process deviations, audit findings, customer complaints, incidents — including identification, containment, root-cause analysis, corrective actions, effectiveness verification, and learning. | ISO 9001 cl. 8.7, 10.2; ISO 27001 cl. 10.2; ISO 42001 cl. 10.2 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| G10 | AI Systems Impact Assessment | Assessing impact of AI systems on individuals, groups and society (bias, fairness, harm). Applies to both external AI product and internal IMS digital twin. | ISO 42001 cl. 6.1.4, 8.4, Annex A.5; ref. ISO/IEC 42005 | Head of AI Native (Michael) [Onboard] |  |  |
| G11 | AI System Components, Assets and Data Management | Managing AI system components (models, weights), assets (training/inference infrastructure, deployed instances), and data (sourcing, quality, lineage, retention, privacy) throughout the lifecycle. Covers versioning of models and datasets, provenance, access control specific to AI artefacts. | ISO 42001 cl. 7.4, Annex A.4.3, A.7; ISO 27001 A.5.12-A.5.14; ISO 9001 cl. 7.1.5 | Head of AI Native (Michael) [Onboard] |  |  |
| G12 | AI Tools Approval for Use | Gate process for selecting, evaluating, approving (or rejecting) external AI tools and services for internal use (e.g., LLM APIs, AI coding assistants, AI productivity tools). Distinct from G10 (impact assessment of AI systems already in use). Outputs: approved-tools list, conditions of use, prohibited-tools list. | Cross-standard (27001 A.5.23 cloud services, 42001 A.10 third-party) | Head of AI Native (Michael) [Onboard] |  |  |
| G13 | AI Skills Development | Creation, validation, versioning and retirement of AI skills (instructions/capabilities used by AI systems, e.g., Anthropic-style skills). Sub-process applicable to both external (C1) and internal (C12) AI products. Covers skill specification, testing, change management, deprecation. | Cross-standard (42001 A.6 AI lifecycle, 9001 8.3 D&D) | Head of AI Native (Michael) [Onboard] |  |  |
| CORE PROCESSES (15) |  |  |  |  |  |  |
| C1 | External AI Product — Design & Development | Lifecycle of the external AI SaaS product for clients — requirements, architecture, model selection, training, validation, release. CAIO drives strategically; Head of AI Native executes operationally. (Renamed from generic 'AI System Design' in v0.2.) | ISO 9001 cl. 8.3; ISO 27001 A.5.8, A.8.27; ISO 42001 cl. 6.2.4, Annex A.6 | Chief AI Officer [Hiring]; operational: Head of AI Native (Michael) |  |  |
| C2 | Software Development & Release | Developing, testing, releasing software updates — version control, code review, secure coding, release management. | ISO 9001 cl. 8.3, 8.5, 8.6; ISO 27001 A.8.25-A.8.34 (DevSecOps); ISO 42001 Annex A.6 | CTO [Vacant] |  |  |
| C3 | Partner Enablement & Certification | Onboarding non-supplier partners only (resellers, integrators, channel partners). Capability certification, ongoing partner audits. Distinct from C8 (outsourced services) and C9 (procurement of suppliers). | ISO 9001 cl. 8.2, 8.5.1; ISO 42001 cl. 4.3, Annex A.10.2 | Head of Training & Certification [Vacant]; interim: PJ Office Co-heads (Euclid + Rosa) |  |  |
| C4 | Customer Onboarding & Activation | Setting up new customers — contract signing, account provisioning, initial training, go-live. | ISO 9001 cl. 8.2.1, 8.2.3, 8.5.1; ISO 27001 A.5.15-A.5.18; ISO 42001 Annex A.8.2, A.10.4 | CCO [Vacant]; interim: PJ Office Co-heads (Euclid + Rosa) |  |  |
| C5 | Service Delivery & Operations | Day-to-day delivery of SaaS services to clients — monitoring, support, performance, SLAs of the external cloud product. | ISO 9001 cl. 8.5; ISO 27001 cl. 8; ISO 42001 cl. 8, Annex A.6.2.6, A.9 | Chief Platform Officer [Vacant] |  |  |
| C6 | Commercial Performance & Revenue | Sales, pricing, contracts, revenue tracking. (Customer satisfaction and success metrics handled by C14.) | ISO 9001 cl. 8.2.1, 9.1.2 | CCO [Vacant] |  |  |
| C7 | Incident Management | Reactive handling of incidents (service outages, security breaches, AI failures) — detection, response, communication, post-mortem. | ISO 9001 cl. 10.2; ISO 27001 A.5.24-A.5.28, A.6.8; ISO 42001 cl. 10.2, A.8.3-A.8.4 | CTO [Vacant]; interim: Head of AI Native (Michael) |  |  |
| C8 | Management of Outsourced Services | Managing services we outsource (cloud hosting, dev partners, facilities, IT services) — SLAs, performance review, risk. | ISO 9001 cl. 8.4; ISO 27001 A.5.19-A.5.23; ISO 42001 cl. 4.3, A.10.3 | Head of Global Facilities [Vacant] |  |  |
| C9 | Procurement of External Providers | Selecting, evaluating and contracting external providers (suppliers, vendors, consultants). | ISO 9001 cl. 8.4; ISO 27001 A.5.19-A.5.23 | CFO [Hiring]; interim: Financial Controller (Ann Greed) |  |  |
| C10 | Partner & Client Training | Training delivered to partners and clients on Janus products and services. | ISO 9001 cl. 7.2, 8.5.1; ISO 42001 cl. 7.3, A.8.2 | Head of Training & Certification [Vacant] |  |  |
| C11 | Threat & Vulnerability Management | Proactive identification, assessment and remediation of security threats and technical vulnerabilities. Distinct from C7 Incident Management (reactive). CTO acts as CISO function. | ISO 27001 A.5.7 (threat intelligence), A.8.8 (vulnerability mgmt); ISO 42001 cl. 6.1 (risk) | CTO [Vacant] — acting as CISO function |  |  |
| C12 | Internal AI Product (IMS Digital Twin) — Design & Development | Lifecycle of the INTERNAL AI product that manages the IMS itself ('IMS digital twin') — requirements, architecture, development, testing, deployment, monitoring, change management. Same lifecycle rigour as the external product (C1). | ISO 9001 cl. 8.3; ISO 27001 A.5.8, A.8.25-A.8.28; ISO 42001 cl. 6.2.4, Annex A.6 (full life cycle for internal AI) | Head of AI Native (Michael) [Onboard] |  |  |
| C13 | Subsidiary Management & Regional Operations | Spinning up and managing subsidiary AI offices in new jurisdictions — replicable playbook for legal entity, infrastructure, staffing, IMS rollout. Target: deploy a new AI office in minutes given basic preconditions (legal entity, infrastructure, people). Currently: Singapore, UK. (NEW in v0.3.) | ISO 9001 cl. 4.1, 4.3, 5.1; ISO 27001 cl. 4.3 (scope), 5.1; ISO 42001 cl. 4.1, 4.3 | Global CEO (Bonaventure Wong) [Onboard] |  |  |
| C14 | Customer Satisfaction & Success Management | Measuring customer perception (CSAT/NPS), gathering and analysing feedback, handling complaints (interface with C7 incident management and G9 nonconformity management), managing customer success metrics, conducting account reviews, win/loss analyses. Carved out from C6 in v0.4 to keep commercial and satisfaction concerns separate. | ISO 9001:2015 5.1.2, 8.2.1, 9.1.2; 42001 A.8 | CMO (Andrew Soane) [Onboard] |  | New in v0.4 — split from C6 |
| C15 | Marketing & Brand Management | Marketing, brand, partner attraction and pipeline. Strategic priority — drive 10-20 new partners per year as growth target. Top-of-funnel for C3 Partner Enablement. Moved from A1 in v0.5 — Additional category dissolved. | ISO 9001 cl. 8.2.1 (customer communication), 7.4 (communication) | CMO (Andrew Soane) [Onboard] |  | Moved from A1 in v0.5 |
| SUPPORT PROCESSES (8) |  |  |  |  |  |  |
| S1 | Control of Documented Information | Managing IMS documents — versioning, approval, distribution, retention, archival. | ISO 9001 cl. 7.5; ISO 27001 cl. 7.5, A.5.33, A.5.37; ISO 42001 cl. 7.5 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| S2 | IT Assets & Access Management | Managing information assets and access — inventory, classification, labelling, acceptable use, identity, authentication, access rights, asset return on termination. | ISO 9001 cl. 7.1.3 (infrastructure); ISO 27001 A.5.9-A.5.18, A.5.37, A.6.7 (~13 controls) | Head of IT Administration [Vacant] |  |  |
| S3 | Legal Compliance & Contract Management | Tracking legal/regulatory obligations, managing contracts (customer, supplier, partner). | ISO 9001 cl. 4.1, 4.2; ISO 27001 A.5.31-A.5.33; ISO 42001 cl. 4.2 | CLO [Hiring July 2026] |  |  |
| S4 | Physical & Environmental Security | Physical perimeter, entry controls, securing offices/devices, environmental threats, clear desk/screen, secure disposal. For Janus mostly applies to offices and end-user devices (cloud-first model). | ISO 27001 Annex A.7.1-A.7.14 (14 controls) | Head of Global Facilities [Vacant] |  |  |
| S5 | Network, Endpoint & Cloud Security Operations (SecOps) | Operational security controls — endpoint protection, network security, access restriction, encryption, logging, monitoring, malware protection, web filtering, capacity, configuration. Cloud-first SecOps for SaaS infrastructure. | ISO 27001 Annex A.8.1-A.8.24 (~24 controls); ISO 42001 cl. 7.4 (data resources) | Head of Infrastructure [Vacant] |  |  |
| S6 | Business Continuity & ICT Resilience | Business continuity planning, disaster recovery, ICT readiness, redundancy, backups, RTO/RPO definition and testing. Required for SaaS availability commitments. | ISO 27001 A.5.29, A.5.30, A.8.13, A.8.14; reference ISO 22301; ISO 9001 cl. 6.1 (risks) | CTO [Vacant]; interim: Head of Infrastructure [Vacant] |  |  |
| S7 | Privacy & Data Subject Rights | Privacy and PII protection — data subject rights, DPIA, breach notification, lawful basis, retention, cross-border transfers. CLO holds DPO function. | ISO 27001 A.5.34, A.8.11 (masking); reference GDPR, ISO 27701; ISO 9001 cl. 4.2 | CLO [Hiring July 2026] — acting as DPO function |  |  |
| S8 | Intellectual Property Management | Managing Janus IP (patents, trademarks, copyright, trade secrets, third-party licenses). Moved from A2 in v0.5 — Additional category dissolved. | ISO 9001 cl. 7.1.6; ISO 27001 A.5.32; ISO 42001 cl. 7.4 | CLO [Hiring July 2026] |  | Moved from A2 in v0.5 |
| MANAGEMENT PROCESSES (5) |  |  |  |  |  |  |
| M1 | Strategic Leadership & IMS Planning | Top-level IMS direction — context, scope, planning, leadership commitment, resource provision at strategic level. Includes process lifecycle management (definition, description, approval, actualisation, retirement of IMS processes). | ISO 9001 cl. 4-6; ISO 27001 cl. 4-6; ISO 42001 cl. 4-6 | Global CEO (Bonaventure Wong) [Onboard] |  |  |
| M2 | Integrated Risk Management | Identifying, assessing and treating risks across quality, security and AI in one integrated register. | ISO 9001 cl. 6.1; ISO 27001 cl. 6.1.2-6.1.3, 8.2-8.3; ISO 42001 cl. 6.1, 8.2-8.3; ref. ISO 31000, 23894, 42005 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| M3 | Performance Monitoring & KPI | Defining KPIs, collecting performance data, reporting on IMS effectiveness. | ISO 9001 cl. 9.1; ISO 27001 cl. 9.1; ISO 42001 cl. 9.1 | Global CEO (Bonaventure Wong) [Onboard] |  |  |
| M4 | Internal Audit | Planning and conducting internal audits of IMS processes against ISO requirements. | ISO 9001 cl. 9.2; ISO 27001 cl. 9.2, A.5.35, A.5.36, A.8.34; ISO 42001 cl. 9.2 | Head of IMS & Compliance (Simon) [Onboard] |  |  |
| M5 | Management Review & Corrective Action | Top-management reviews of IMS performance — opportunities, corrective actions, improvements. | ISO 9001 cl. 9.3, 10; ISO 27001 cl. 9.3, 10; ISO 42001 cl. 9.3, 10 | Global CEO (Bonaventure Wong) [Onboard] |  |  |

## Sheet: How to use (11 rows)

| How to use this Process Register (DRAFT v0.5) |  |
| Purpose | Define the full list of IMS processes for Janus Digital and assign owners. Inputs: ISO 9001, ISO 27001, ISO 42001. |
| Status | DRAFT v0.5 — internal review. 41 processes total. Additional category dissolved (A1→C15, A2→S8). |
| Process codes | G = Governance (13). C = Core (15). S = Support (8). M = Management (5). Total 41. |
| Owner format | Role title [Status]. Status = Onboard / Hiring / Vacant. If the role is not yet filled, the role acts as future owner. 'Interim:' identifies who covers the function today. |
| Changes from v0.4 | Dissolved Additional category. (1) A1 Marketing & Brand Management → C15 (Core) — rationale: Marketing is value-chain top-of-funnel feeding C3 Partner Enablement. (2) A2 Intellectual Property Management → S8 (Support) — rationale: IP is intangible-asset management, sits alongside S2 IT Assets and S3 Legal Compliance. No owners, descriptions or clause refs changed. Total process count unchanged (41). |
| Columns | Code \| Process name \| Brief description \| Standard/clause refs \| Proposed owner (role + status) \| Your role (dropdown) \| Comments. |
| For colleagues (when distributed) | 1) Read brief description. 2) Pick Owner / Participant / Not involved. 3) Use Comments to dispute, clarify, or add missing processes. |
| Conflict resolution | Two Owner claims → escalate to Simon. No Owner claim → escalate to Bonaventure. |
| Next steps | v1.0 register → RACI matrix → pilot process card (ISO 9001 Fig.1) on 1-2 processes → mass roll-out. |
| File naming | REG-IMS-ProcessRegister-v[VERSION]-[YYYY-MM-DD].xlsx. |
