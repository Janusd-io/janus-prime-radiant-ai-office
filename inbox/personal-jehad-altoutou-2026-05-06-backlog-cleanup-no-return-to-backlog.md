---
type: decision
title: Backlog cleanup principle — post-evaluation tools never return to Backlog
slug: 2026-05-06-backlog-cleanup-no-return-to-backlog
created: 2026-05-06
updated: 2026-05-13
departments: [ai-office]
status: resolved
owner: michael-bruck
sources: [pr-backup-2026-05-11-decision-2026-05-06-backlog-cleanup-no-return-to-backlog]
related: [linear, ai-tool-evaluation-framework]
audience: [department]
captured_by: jehad-altoutou
---

# Backlog cleanup — post-evaluation tools never return to Backlog

**Decision date:** 2026-05-06. **Decided by:** Michael Bruck, Jehad Altoutou.

## What

In Linear AIR, tools that have moved out of Backlog into any subsequent stage (Evaluating, Sandbox, Production, Monitor, Rejected, Deprecated) **never return to Backlog**. Re-evaluation moves a tool back to Evaluating or directly into a later stage as appropriate, but Backlog is reserved exclusively for tools awaiting their first triage.

## Why

- Backlog is the "not yet looked at" state. Sending evaluated tools there hides them in the same list as un-triaged candidates, which destroys the signal of the Backlog list.
- Each post-evaluation status (Sandbox / Rejected / Deprecated) carries decision context that returning to Backlog would silently discard.

## Implications

- The standup skill and `/ai-registry` enforce this rule.
- Any tool found to be back in Backlog after having a prior gate decision is a registry-hygiene issue worth flagging during lint.

## Related

- [[ai-tool-evaluation-framework]] — the framework producing these stage transitions.
- [[linear]] — the substrate on which Linear AIR runs.
