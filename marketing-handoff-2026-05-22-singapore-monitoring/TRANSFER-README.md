# Transfer package — Singapore news monitoring → Marketing Prime Radiant

**From:** Janus Prime Radiant · AI Office
**To:** Janus Prime Radiant · Marketing ([[andrew-soane|Andrew Soane]])
**Date:** 2026-05-22
**Reason:** The Singapore news monitoring agent is operationally a marketing-intelligence workflow. It was incubated in the AIO Prime Radiant because the AIO was the first live instance; now that Andrew's Marketing instance is set up, the workflow should live where it belongs — closer to Andrew's daily operating surface, where the framer (you, increasingly) and the implementing agent share a vault.

This package is the federation handoff. It captures the AIO-side material that should move canonically to Marketing, the supporting context that should be copied over, and the items that stay AIO-canonical with cross-vault references. After the transfer, the AIO vault keeps federation pointers; the Marketing vault becomes the canonical home.

## What's in this package

- **`TRANSFER-README.md`** — this file. Read first.
- **`migration-manifest.md`** — file-by-file action list with target paths.
- **`files/`** — all the content that's transferring, laid out in the Marketing instance's target directory structure. Copy the `files/` subtree into the Marketing vault root; the paths are already where they need to land.
- **`post-import-AIO-updates.md`** — the AIO-side rewrites (federation pointers replacing canonical content) to apply *after* the Marketing vault has imported successfully.

## How to import (operationally)

1. **In the Marketing vault**, copy the contents of `files/` into the vault root. Paths are pre-mapped — each file lands where its slug and folder expect.

```bash
# from inside the Marketing vault root
cp -r /path/to/marketing-handoff-2026-05-22-singapore-monitoring/files/. .
```

2. **Add Marketing-specific frontmatter ownership.** The files in `files/` are already pre-rewritten with `owner: andrew-soane` (where appropriate), Marketing-context preambles, and adjusted `departments:`. No further edits required, but skim the manifest to verify each file's intent.

3. **Update the Marketing vault's `index.md`.** Each imported file should be registered. The manifest has the suggested index lines.

4. **Log the transfer** in the Marketing vault's `log.md` as an `import` entry. Suggested log block in the manifest.

5. **Update the Marketing CLAUDE.md** *only if needed.* This handoff doesn't change the schema. If Marketing's CLAUDE.md doesn't yet have `countries:` frontmatter in its vocabulary, add it (`sg`, `gb`, `us`).

6. **On the AIO side**, run `post-import-AIO-updates.md` — replace the moved files with federation-pointer stubs, update relevant cross-refs.

7. **Federation check.** Both vaults should now resolve `[[singapore-news-monitoring]]` correctly — Marketing to the canonical project hub, AIO to a one-line pointer page.

## What moves vs what stays — at a glance

| Class | Examples | Action |
|---|---|---|
| **Canonical to Marketing** | `projects/singapore-news-monitoring.md`, `projects/singapore-monitoring-frame-audit-2026-05.md` | AIO has a pointer; Marketing owns the content |
| **Dual-location (live in both)** | `processes/pre-ship-confidence-and-frame-check.md`, `concepts/pilot-in-command.md`, `entities/internal/joyce-woo.md` | Both vaults carry the content; updates flow via the [[peer-to-peer-mesh-federation-pattern\|mesh]] subfolder |
| **Supporting context copy** | `sources/articles/2026-05-14-janus-singapore-white-paper-storms-ahead.{pdf,md}`, `sources/articles/2026-05-01-pm-lawrence-wong-may-day-rally-2026.md`, `entities/people/vivian-balakrishnan.md`, `decisions/2026-05-12-singapore-as-lead-market.md`, `pulse/2026-05-12-vivian-balakrishnan-llm-wiki-government.md` | Marketing gets its own copy; AIO retains independently |
| **Stay AIO-canonical** (Marketing references via cross-vault link) | `briefs/coordination-leverage-model.md`, `concepts/coordination-three-layer-model.md`, `briefs/ai-native-janus-positioning.md`, `questions/2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room.md` | No copy. Marketing pages reference the AIO-canonical pages by slug — the federation resolver handles cross-vault wikilinks via the mesh `entities/departments/` shared subfolder |

## The frame-audit hand-off

The transfer comes with active work in progress: the [[singapore-monitoring-frame-audit-2026-05|frame audit experiment]] I designed yesterday. With this handoff Andrew is the natural runner of the audit, not me — *he* is becoming the Framer of Record (or co-framer with Bonaventure).

The frame-audit project hub in `files/projects/singapore-monitoring-frame-audit-2026-05.md` is **rewritten for Marketing** — owner is Andrew, framer language is consistent with Andrew's voice, the methodology is unchanged. If Andrew prefers a different cadence or methodology adjustment, he updates the project hub directly. The audit's pulse-entry deliverable goes to the Marketing vault's `pulse/` folder.

## Open questions for Andrew

1. **Who's the Framer of Record for the Singapore monitoring workflow long-term — Andrew or Bonaventure?** My instinct: Andrew operationally, Bonaventure strategically (i.e., monthly frame audits run by Andrew with a quarterly Bonaventure check-in). Decide and capture in `framed_by:` frontmatter on the project hub.
2. **Where does the agent's Slack channel post into?** The AIO has been the default audience. In Marketing's vault, the natural destination is a Marketing-specific channel (`#mkt-singapore-signals` or similar). If you switch, log the change in the project hub's "Update" section.
3. **What's Andrew's preferred cadence for the pre-ship gate?** [[pre-ship-confidence-and-frame-check]] proposes the gate runs *before each scheduled publish*. If Andrew finds it noisy, weekly or fortnightly is also acceptable — but daily is the recommended starting point.

## What I'm NOT transferring (deliberately)

- **The full Coordination Leverage Model brief.** It lives in the AIO Prime Radiant; Marketing cross-references it. The framework is broader than Singapore monitoring; transferring it would clutter the Marketing vault.
- **The Principle 10 ratification escalation.** The framework decision belongs with Michael (AIO instance). Marketing benefits from the *operationalisation* (`pre-ship-confidence-and-frame-check.md`) without owning the framework debate.
- **AIO standup pipeline meeting source files** that mention the Singapore monitoring agent in passing. Marketing builds its own audit trail going forward; AIO retains its historical Fireflies sources.
- **`projects/marketing-prime-radiant.md`** itself. That's the Marketing vault's own build hub; the AIO copy is the mesh-pairing version.

## After this transfer, what changes about how we work

- **Andrew owns Singapore monitoring operationally.** New decisions about the agent (theme prompts, source list, Phase 2 gating, etc.) get filed in the Marketing vault.
- **The frame audit produces evidence in the Marketing vault**, not the AIO vault.
- **Cross-departmental discussions about Singapore monitoring** (Bonaventure × Andrew × Michael) land in the mesh subfolder (`entities/departments/marketing/` from the AIO side; `entities/departments/ai-office/` from the Marketing side).
- **The AIO retains references** — Singapore monitoring is the first concrete Layer-3 test case for the Coordination Leverage Model, and the AIO's strategic-context pages keep pointing at it.

## Related (in the AIO vault — won't be in the Marketing vault unless you copy them later)

- [[coordination-leverage-model]] — Michael's theoretical framework (AIO-canonical).
- [[coordination-three-layer-model]] — Individual / Department / Organisation; Singapore monitoring is the Layer-3 prototype.
- [[organisational-digital-twin]] — the HGTFT-pattern applied to the company.
- [[ai-native-janus-positioning]] — three-pillar positioning brief; the white paper hangs off this.
- [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]] — Principle 10 escalation (awaiting evidence from the audit).
- [[peer-to-peer-mesh-federation-pattern]] — the federation architecture this transfer follows.

Read these in the AIO Prime Radiant when you need them.
