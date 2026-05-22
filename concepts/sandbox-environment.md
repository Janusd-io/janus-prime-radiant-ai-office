---
type: concept
title: Sandbox Environment
slug: sandbox-environment
created: 2026-05-22
updated: 2026-05-22
departments: [ai-office, it-ops, iso, engineering]
status: active
sources: [section-5-ai-charter-policy-v2.1]
related: [ai-policy, ai-tool-evaluation-framework, ai-tool-evaluation, sandbox-to-production-handover, hostinger, ai-policy-gate-approval]
---

# Sandbox Environment

Janus Digital's dedicated, governed venue for safe evaluation of third-party AI tools and development of internal AI solutions, without risk to production data, client data, or live operational systems. Codified in §5.5 of the [[ai-policy|AI Policy v2.1]].

> "The sandbox is the mandatory environment for all Stage 3 tool evaluations (see §5.4.4) and for all internal AI solution development prior to production deployment (see §5.6). It is not an informal test area; it is a governed environment with formal data restrictions and defined entry and exit conditions."

## Properties (per §5.5)

- **Mirrors production infrastructure with full fidelity.** The sandbox is not a degraded test environment — its purpose is to surface integration / performance / security issues that would also surface in production.
- **Mandatory for:**
  - All Stage 3 evaluations of third-party tools (per [[ai-tool-evaluation-framework]] §5.4.4).
  - All internal AI solution development *prior to* production deployment (per §5.6 pipeline).
- **Time-boxed for evaluations.** Stage 3 evaluations run for **three to five working days** against a structured test brief defined by the AI Office. Domain experts execute the brief and complete a structured evaluation form.
- **Formal entry + exit conditions.** Promotion to production is a *deliberate, documented act* via the relevant gate process (Gate 3 for third-party tools, formal acceptance testing for internal solutions). Not an informal transition.

## Data restrictions (the non-negotiable rule)

**Only non-sensitive or synthetic data** may be processed within the sandbox at any time. The following are **strictly prohibited**, no exceptions:

- Production data of any kind
- Client data or client-related information
- Personally Identifiable Information (PII)
- Confidential company information or intellectual property

§5.5.2 names this as a hard rule and §5.10's compliance notice escalates: violation of sandbox data boundaries is treated as a breach of Data Governance (§5.7) and is subject to the disciplinary provisions — *"up to and including termination of employment."*

The reason is structural: the sandbox exists to run *experimental, unvetted* AI capability against data. Any data class that would not be acceptable to leak in a worst-case sandbox failure is therefore prohibited from the sandbox.

## How it sits in the pipelines

### Third-party tool evaluation (§5.4)

```
Stage 1 (Intake & Triage, Gate 1 binary)
  → Stage 2 (Technical Qualification, Gate 2 mandatory + scored)
    → Stage 3 (Sandbox + Domain Expert Evaluation, Gate 3)        ← lives here
      → Stage 4 (Approval, IT Handover, Registry Listing, Gate 4)
```

Stage 3 is the only stage that requires sandbox provisioning. Domain experts execute the test brief against the candidate tool *only* in the sandbox; the tool does not touch production systems or production data during evaluation.

### Internal AI solution development (§5.6)

```
Intake → Discovery → Triage → PRD/SoW Sign-Off → Product Spec → Sandbox Build  ← lives here
  → Acceptance → Production & Monitor
```

The "Sandbox Build" stage is the development phase. **No build without a signed PRD** is the upstream hard gate; sandbox-only-development is the downstream hard rule. Both are non-negotiable per §5.6.2.

## Why the rigour

The sandbox isn't a security best-practice — it's the structural mechanism that makes Stage-3 evaluations *credible*. If Domain Experts were testing candidate tools against production data, the evaluation would be entangled with production-data risks, the tool would have already accumulated state that complicates rejection, and the binary "approve / reject at Gate 3" decision would be coloured by switching costs. By forcing all Stage-3 work into a non-sensitive-data environment, the evaluation produces a clean signal on tool fit independent of integration cost.

The same logic applies to internal development. AIO solutions built in the sandbox can be rejected at Acceptance with no production exposure; if built in production, rejection is more expensive than approval, biasing the AIO toward shipping mediocre solutions.

## Current implementation (as of 2026-05-22)

- **Substrate.** The sandbox runs on [[hostinger]] (per the 2026-04 GCP-vs-Hostinger decision; flat-fee cost model + APAC residency + Docker-native). Sandbox-environment-specific resources distinct from any production deployments.
- **Provisioning workflow.** Stage 3 evaluations get sandbox accounts + scoped credentials at the start of the 3–5 day window; access is revoked at the end of the window or at Gate 3 decision.
- **Promotion path.** Documented separately under [[sandbox-to-production-handover]] (the SOP gap-fill that the 2026-05-06 AI-IT meeting flagged).
- **AI-policy-gate-approval.** The reusable governance process [[ai-policy-gate-approval]] codifies the Sub-Gate B (IT Handover) work that moves a tool out of sandbox into production.

## Watch for

- **Synthetic-data generation as a sub-capability.** §5.5.2's "non-sensitive *or synthetic*" wording assumes synthetic-data availability. As more sensitive use cases need sandbox evaluation, the AIO may need to standardise synthetic-data generation tooling.
- **Sandbox-to-production handover SOP.** [[sandbox-to-production-handover]] is currently a stub flagged as a procedure gap. Fill needed.
- **Cross-jurisdiction sandbox.** Multi-country expansion creates a question: does the sandbox need regional instances (Singapore, UK, etc.) to satisfy data-residency requirements during Stage 3 evaluation of region-scoped tools? Currently centralised; reassess as expansion progresses.
- **Sandbox observability.** Audit-trail requirements for sandbox activity (which Domain Expert tested which capability, on which data, with which outcome) may need explicit instrumentation for ISO/IEC 42001 surveillance.
