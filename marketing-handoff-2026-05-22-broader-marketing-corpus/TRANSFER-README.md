# Transfer package — broader marketing corpus → Marketing Prime Radiant

**From:** Janus Prime Radiant · AI Office
**To:** Janus Prime Radiant · Marketing ([[andrew-soane|Andrew Soane]])
**Date:** 2026-05-22
**Bundle #2** of 2026-05-22 federation work — sibling to `marketing-handoff-2026-05-22-singapore-monitoring/` (the Singapore-monitoring workflow handoff). Read that one first if you haven't.

## Scope — what this bundle covers

While the Singapore-monitoring bundle moved one operational workflow, **this bundle moves the broader marketing-domain knowledge body** the AIO has accumulated from 2026-05-04 onward. Specifically:

- The full **marketing stack story** (Cosmic / Attio / Vercel / Cloudflare / Resend / Cookiebot decisions) + the supporting framework (Stack Composition Framework).
- The **website + CMS + CRM** project hubs (janus-website, janus-website-cms, janus-crm-selection, crm-evaluation-and-selection).
- The **brand surface** — the official brand guideline process page, logo SVGs, and the `janus-html-deck` skill bundle snapshots.
- The **marketing-domain decision record** — 27 decision entries spanning brand commission, CRM shortlisting, the five-capability framework, three messaging pillars, marketing-PR outputs ordering, white-paper gating pattern, single-domain ccTLD architecture, anti-AI-washing content discipline, and more.
- The **AIO×Marketing meeting source files** — 5 substantial meetings that produced the marketing-domain decisions.
- **Marketing-domain Infrastructure concepts** — buyer-personas, messaging-pillars, ai-washing, builders-sellers-measurers, stack-composition-framework (dual-location with AIO).
- **Marketing-stack vendor entities** — Resend, Mailchimp, Monday (with "not-a-CRM" framing), Canva, Marketo, Microsoft Clarity, LinkedIn Marketing Solutions.
- **Two key internal entities** — Andrew Soane, Bonaventure Wong (dual-location across both vaults).
- **The two recent marketing-thesis briefs** — `agentic-lean-marketing-stack` (Marketing-canonical) + `ai-native-janus-positioning` (dual-location).

## What's NOT in this bundle (deliberate exclusions)

- **The Singapore monitoring workflow** — see the sibling `marketing-handoff-2026-05-22-singapore-monitoring/` bundle. Imported separately.
- **The Coordination Leverage Model framework and its concepts** (coordination-leverage-model brief, coordination-tax, coordination-three-layer-model, organisational-digital-twin). Stays AIO-canonical; Marketing references via federation.
- **The AI Policy + AI Tool Evaluation Framework** (ai-policy concept, ai-tool-evaluation-framework process, ai-registry process, sandbox-environment, pilot-in-command, shadow-ai-prohibition, tool-tiers). Stays AIO-canonical (the policy is org-wide; AIO maintains).
- **Coordination-related concepts** that touch marketing but are AIO-canonical (the architecture-level material).
- **AI-native-enterprise-restructuring brief** — touches marketing through the Drucker frame but is broader synthesis; stays AIO-canonical, Marketing references via federation.
- **HGTFT** — Engineering-domain, separately federated when the Engineering instance stands up.
- **Standup pipeline + AIO operational pages** — AIO-internal.
- **Open vendor escalation** — `questions/ingest-2026-05-20-1145-create-marketing-stack-vendor-pages.md` stays AIO-canonical; once Michael ratifies, the new vendor pages (Cosmic, Attio, Vercel, Cloudflare, Cookiebot) get filed in AIO as canonical (per AI Registry SoR) with dual-location to Marketing.

## How this bundle relates to the Singapore-monitoring bundle

These are **two sibling bundles** doing the same federation handoff at different scopes. Both target the Marketing vault. Both should be imported in the same window (within a day or two of each other), but the order doesn't strictly matter — the bundles don't overlap in content. A handful of files are referenced by both bundles (e.g., `decisions/2026-05-12-singapore-as-lead-market.md` is in both because it's relevant to both Singapore monitoring AND the broader Singapore launch). If you import both bundles, the second import's `cp -r` will be a no-op for already-imported files.

| Bundle | Scope | File count |
|---|---|---|
| `marketing-handoff-2026-05-22-singapore-monitoring` | Singapore news-monitoring workflow + frame audit + pre-ship gate + relevant SG sources | 13 md + 1 PDF |
| **`marketing-handoff-2026-05-22-broader-marketing-corpus`** *(this one)* | Marketing stack, website/CMS/CRM, brand, positioning, marketing-domain decisions + meetings | 66 md + 3 binaries (1 PDF + 2 SVG) |

## How to import (operationally)

Same as the Singapore bundle:

1. **In the Marketing vault**, copy `files/` contents into the vault root:

```bash
cp -r /path/to/marketing-handoff-2026-05-22-broader-marketing-corpus/files/. .
```

2. **Verify the imports** — see `migration-manifest.md` for the file-by-file action list including frontmatter edits already applied.

3. **Update the Marketing vault's `index.md`** — the manifest has suggested index lines for each section (Briefs, Concepts, Projects, Decisions, etc.).

4. **Log the import** in the Marketing vault's `log.md` as an `import` entry. Suggested log block in the manifest.

5. **Verify the brand assets** render correctly. The two SVG files at `assets/branding/` are referenced in the `processes/janus-html-deck-brand-guideline.md` process page. The skill-bundle snapshot at `assets/janus-html-deck/` is used by the deck-creation workflow.

6. **On the AIO side**, run `post-import-AIO-updates.md` — replaces the canonical-to-Marketing files with federation-pointer stubs.

## Open questions for Andrew

1. **Marketing capabilities project hubs** (`janus-thought-leadership.md`, `janus-marketing-capabilities.md`, `janus-brand-guidelines-refresh.md`, `janus-careers-page.md`) are **stubs** — they were filed during AIO ingest but never populated. Marketing should own filling them out; transfer brings them across so they live where they belong, not so they continue to live as orphans. Triage: fill, retire, or merge into a single Marketing-capabilities umbrella?
2. **`apply-standup-methodology-to-andrew-work-stream.md`** is in scope for both AIO and Marketing — it's the workstream that operationally ports the AIO standup discipline to Andrew. Suggest: Marketing owns the project, AIO advises. Confirm and assign owner.
3. **`janus-careers-page.md`** sits at the marketing × HR boundary (employer brand + hiring process). Suggest: Marketing owns the careers *brand surface*, HR owns the *operational hiring pipeline*. Confirm split.
4. **The `crm-evaluation-and-selection.md` history** (the broader CRM evaluation arc that ran HubSpot-leaning → Attio in May) is in the bundle as supporting context for `janus-crm-selection.md`. Both come over; the former is the evaluation history, the latter is the locked-in Attio choice. Andrew may consolidate later.

## What I'm flagging as borderline

Three calls I made that you may want to override:

- **`ai-native-janus-positioning.md` as dual-location, not Marketing-canonical.** It's Bonaventure's three-pillar positioning brief — used heavily by Marketing as Infrastructure-layer content, but written from the AIO/CEO axis. Dual-location keeps both vaults able to update; Marketing-canonical would centralise the canonical voice. Default to dual; flip to Marketing-canonical if Andrew wants ownership.
- **The `2026-05-05-*` marketing decisions** were the first decision batch from the weekly meeting that authorised Marketing-domain work but were filed in AIO because the AIO instance was the only one then. They're Marketing-canonical *retroactively*. Transferring as canonical-to-Marketing; AIO-side stays as federation-pointer stubs (per the post-import-AIO-updates doc).
- **The five "stub" project hubs** (`janus-thought-leadership` etc.) are being transferred even though they're stubs. Rationale: they live where they belong now, even if Marketing decides to consolidate later. Alternative would have been leaving them in AIO; that creates more orphan-pages-not-where-they-belong than just transferring them.

## After this transfer, what changes about how we work

- **Marketing owns the marketing-domain decision record from 2026-05-04 onward.** All future marketing-domain decisions land in the Marketing vault.
- **The marketing-stack vendor entities are dual-location.** When the AIO creates the new vendor pages (Cosmic / Attio / Vercel / Cloudflare / Cookiebot per the open escalation), the same dual-location pattern applies.
- **Andrew Soane and Bonaventure Wong entity pages live in both vaults.** Future updates flow via the mesh subfolder.
- **The brand guideline process page is dual-location.** When Andrew's agency-led brand refresh lands, both vaults need the v2.0 update; agreement on cadence pending.
- **AIO retains references** to all moved-canonical content via federation-pointer stubs; inbound wikilinks from AIO strategic-context pages keep resolving.

## Related (in the AIO vault — won't be in the Marketing vault unless you copy them later)

- [[coordination-leverage-model]] — Michael's theoretical framework (AIO-canonical).
- [[coordination-three-layer-model]], [[coordination-tax]], [[organisational-digital-twin]] — framework concepts.
- [[ai-native-enterprise-restructuring]] — the JPMorgan / Cloudflare / KPMG / Anthropic-profitability synthesis brief.
- [[ai-policy]], [[ai-tool-evaluation-framework]], [[ai-registry]], [[shadow-ai-prohibition]], [[tool-tiers]], [[sandbox-environment]], [[pilot-in-command]] — AI Policy + governance machinery.
- [[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]] — Principle 10 escalation, evidence base for the framer-stays-in-the-room rule.
- [[peer-to-peer-mesh-federation-pattern]] — the federation architecture this bundle follows.
- [[hgtft]] — Janus customer product, Engineering-canonical when that instance lands.
