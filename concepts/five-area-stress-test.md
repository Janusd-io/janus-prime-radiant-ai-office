---
type: concept
title: Five-area stress test — Jehad's quality bar before IT handover
slug: five-area-stress-test
created: 2026-05-14
updated: 2026-05-14
captured_by: jehad-altoutou
audience: department
departments: [ai-office]
sources: [parent-process, 04-formal-response, sub-process-platform-development, sub-process-tool-evaluation]
related: [meeting-to-task-workflow, platform-development-process, ai-tool-evaluation, sandbox-to-production-handover, jehad-altoutou]
---

# Five-area stress test — Jehad's quality bar before IT handover

Across every build the AI Operations Engineer ships — features (Meeting→Task→Build), platforms (Platform Development), and third-party tools (AI Tool Evaluation sandbox stage) — the same **five-area stress test** is the gate before IT handover. The bar is "can I break it?" — Jehad tries to find weaknesses himself before users do.

## The five areas

| Area | What gets tested |
| --- | --- |
| **Functionality** | Does every feature work under expected load? Happy paths + edge cases. |
| **UI / UX** | Usable, accessible, intuitive, responsive, consistent. |
| **Security** | Auth · authz · CSRF · rate limiting · audit logging · session integrity · file validation · secrets handling. Survives standard attack patterns and API abuse. |
| **APIs** | Response times · error rates · payload validation · webhook signing · idempotency. Edge cases under load. |
| **Stability** | Sustained-use behaviour · memory leaks · log volume · backup integrity. |

If all five areas pass, the build is ready for handover. If not, weaknesses are logged in Linear and patched in the Fix & Enrol stage.

## Why this matters for ISO

Until Simon helps formalise KPIs (pass/fail thresholds, measurement frequency, target values), this is the operating-time quality bar that produces audit evidence for **§7.5 Documented information** and feeds the proposed PULS KPIs:

- Test-area pass rate (5/5 required for handover)
- Critical security findings at handover
- Time from requirements gathered to IT handover
- Post-handover defect rate (issues found by IT or users)
- AI Systems Register coverage (% of deployed AI tools with [[ai-registry|Linear AIR]] entries)

## Open ask to Simon (ISO Lead)

Formal pass/fail thresholds + measurement frequency + target values so the test phase produces something the [[puls-dashboard|PULS dashboard]] can monitor automatically — currently the bar is Jehad's judgement "can I break it," which is operationally sufficient but not yet machine-readable.
