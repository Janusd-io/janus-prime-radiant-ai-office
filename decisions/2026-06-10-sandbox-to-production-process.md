---
type: decision
title: Sandbox-to-production handover process formalised (AIO → IT)
slug: 2026-06-10-sandbox-to-production-process
created: 2026-06-11
updated: 2026-06-11
departments: [ai-office, it-ops]
status: active
owner: michael-bruck
decided_by: 2026-06-10-aio-it-weekly-meeting
attribution: confirmed
attribution_sources: [2026-06-10-aio-it-weekly-meeting]
confidence: high
sources: [2026-06-10-aio-it-weekly-meeting]
related: [assessify, janus-prime-radiant-build, euclid-wong, andrey-timokhov, dhyey-mehta, jehad-altoutou]
---

# Sandbox-to-production handover process formalised (AIO → IT)

**Decision:** Formalise a structured handover process for AIO-built tools moving from AIO's sandbox infrastructure to IT's production infrastructure.

**Context:** Prior to June 10, 2026, handovers were informal — verbal instruction ("hey Andrey, set up the APIs"). This created risk of deployment inconsistency, no version control discipline, and no user acceptance gate. The June 10 AIO × IT weekly meeting produced an agreed process. Attribution confirmed: all speakers named directly in the Fireflies transcript (Michael Bruck, Euclid Wong, Jehad Altoutou, Andrey Timokhov, Dhyey Mehta).

## The agreed process

**Phase 1 — AIO builds and tests (sandbox)**
- Tool passes through the Linear AIR pipeline (Backlog → Evaluation → Sandbox stages).
- AIO builds and stress-tests in the AIO sandbox environment (Hostinger dev account).

**Phase 2 — IT access and pre-production testing**
- IT team members (Andrey Timokhov, Dhyey Mehta) receive **named individual accounts** — not generic test accounts. Named accounts are traceable and accountable. Andrey and Dhyey were added to the `Janusd-io` GitHub organisation during the meeting.
- IT receives read access to the GitHub repo and stress-tests with their named accounts.

**Phase 3 — Handover package**
AIO delivers a complete handover package:
1. **GitHub repo** (with read access for IT)
2. **README** — installation steps and configuration dependencies
3. **SOP** — usage manual for the production operator
4. **Stress test log** — AIO's own pre-handover test results
5. **Version number** — semantic versioning required from handover date forward

**Phase 4 — IT deployment**
- IT deploys to **separate production infrastructure** (Hostinger account owned by IT, distinct from AIO's dev account). Budget and server provisioning are IT's responsibility.
- IT owns the production environment post-deployment.

**Phase 5 — User acceptance gate**
- The business-side target user (e.g., Miriam for HR / Assessify) must file a **Zendesk ticket** confirming they have tested the production deployment before IT considers the tool accepted.
- No user acceptance ticket = not accepted.

**Phase 6 — Ongoing support**
- Business users submit feature requests or bug reports via Zendesk to IT.
- IT relays to AIO as needed.
- Major new features require re-testing in sandbox + version bump before re-deployment.

## Immediate next step

First deliverable is **Assessify** (HR leave request platform). Blocking item: Miriam has not yet submitted a Zendesk ticket confirming testing. Euclid flagged this; Michael agreed to follow up. AIO side is ready (GitHub repo, README, SOP, stress test log exist); production deployment is pending user acceptance request.

## Why this matters

This process closes the informal handover loop that existed since the AIO started building internal tools. It gives IT a predictable intake format, ensures AIO can't be blamed for production issues on undertested deployments, and creates a user-acceptance gate that prevents business-side non-adoption from being confused with technical failure.
