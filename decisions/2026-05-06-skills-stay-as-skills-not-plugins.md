---
type: decision
title: Skills remain as skills (not plugins)
slug: 2026-05-06-skills-stay-as-skills-not-plugins
created: 2026-05-06
updated: 2026-05-06
departments: [ai-office, engineering]
status: resolved
owner: michael-bruck
decided_by: michael-bruck
sources: [aio-2026-05-06]
related: [agent-skills, claude]
---

# Skills remain as skills, not plugins

**Decision date:** 2026-05-06
**Decided by:** Michael Bruck, Jehad Altoutou
**Source:** [[aio-2026-05-06]]

## What

Janus's AI Office tooling — `/standup`, `/ai-registry`, `/ai-tool-evaluation`, the upcoming ISO facilitation skill, the recruitment scoring skill — stays as Claude Skills. They are not packaged as Cowork plugins, even though that's a supported distribution path.

## Why

- Skills are used by Michael and Jehad only; the audience is two people, not an organisation. Plugin packaging is overhead that's only justified for broader distribution.
- Skill iteration is fast (file edits in a folder); plugin iteration adds a packaging + install cycle.
- Cross-skill orchestration (the `/standup` ↔ `/ai-registry` ↔ `/ai-tool-evaluation` chaining contract) is already proven within the skill substrate — no plugin-level affordance would meaningfully add to it.

## Reversal triggers

This decision should be revisited if any of these become true:
- More than 4 people regularly invoke any of these skills directly.
- Janus wants to ship one of these skills to a Cowork marketplace for external use.
- The skills themselves grow large enough that plugin-level encapsulation provides material clarity.

## Related

- [[agent-skills]] — concept page covering the Claude skill pattern.
- [[claude]] — vendor page covering the Anthropic product family that hosts skills.
