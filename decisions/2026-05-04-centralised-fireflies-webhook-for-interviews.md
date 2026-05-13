---
type: decision
title: Centralised Fireflies webhook for interview transcripts
slug: 2026-05-04-centralised-fireflies-webhook-for-interviews
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, hr]
status: resolved
owner: jehad-altoutou
decided_by: jehad-altoutou
sources: [aio-2026-05-04, aio-2026-05-05]
---

# Centralised Fireflies webhook for interview transcripts

**Decision date:** 2026-05-04 (chosen); 2026-05-05 (architecture confirmed)
**Decided by:** Michael Bruck, Jehad Altoutou
**Sources:** [[aio-2026-05-04]], [[aio-2026-05-05]]

## What

Interview transcripts will be captured by a centralised Fireflies setup using a webhook architecture: a dedicated invitee email auto-records interviews and triggers a post-assessment skill on completion.

## Why

Per-interviewer Fireflies setups would have introduced consent variance, naming inconsistency, and missing transcripts on interviews with non-Fireflies-equipped staff. A central invitee normalises capture.

## Implications

- All recruitment interviews are scheduled with the dedicated Fireflies invitee email on the calendar invite.
- A post-assessment skill is triggered by the webhook to score the interview transcript against the candidate's CV and JD.
- Front-end agentic UIs become the line manager surface; they never directly access Fireflies.
- The same webhook pattern likely generalises to other meeting categories (vendor demos, customer interviews) once recruitment proves it out.

## Related

- [[2026-05-05-recruitment-scoring-as-claude-skill]] — the post-assessment skill that the webhook triggers.
- [[2026-05-04-recruitment-execution-on-hr-dashboard-board]] — the board this work is tracked on.
