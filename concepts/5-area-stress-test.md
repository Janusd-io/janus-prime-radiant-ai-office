---
type: concept
title: 5-area stress test
slug: 5-area-stress-test
created: 2026-05-14
updated: 2026-05-14
departments: [ai-office]
captured_by: jehad-altoutou
audience: [department]
sources: [06-first-voice-final, 09-platform-development-process]
related: [platform-development-process, meeting-to-task-workflow, assessify]
---

Jehad Altoutou's working quality-bar for any built artefact before it leaves sandbox — *'can I break it?'* across five areas. As of 2026-05-07 (per `06-first-voice-final`) it is his informal KPI structure; per `09-platform-development-process` Stage 7 it is the standard handover gate for any platform produced by the AI Office and applies equally to the per-feature flow in [[meeting-to-task-workflow]].

The five areas:

| Area | What's tested |
|---|---|
| Functionality | Every feature works under expected load · happy paths · edge cases |
| UI / UX | Usable · accessible · intuitive · responsive · consistent |
| Security | Auth · authz · CSRF · rate limiting · audit logging · session integrity · file validation · secrets handling |
| APIs | Response times · error rates · payload validation · webhook signing · idempotency |
| Stability | Sustained-use behaviour · memory leaks · log volume · backup integrity |

If none of the five areas can be broken by Jehad's own testing, the artefact is ready for handover. The framework is currently informal — Jehad's standing open ask to [[simon-tarskih]] (per Q4 of `06-first-voice-final`) is to formalise pass/fail thresholds, measurement frequency, and target values so the test phase produces signals the PULS dashboard can monitor automatically.
