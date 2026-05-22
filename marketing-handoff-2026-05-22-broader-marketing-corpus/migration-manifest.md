# Migration manifest — file-by-file actions

Authoritative list of file actions for the broader-marketing-corpus federation handoff (2026-05-22, bundle #2). Companion to the Singapore-monitoring handoff bundle.

## Files in this bundle — 69 total (66 markdown + 2 SVG + 1 PDF)

### Canonical-to-Marketing — Marketing owns; AIO retains federation-pointer stubs

#### Briefs (1)

| File | Marketing target path | Notes |
|---|---|---|
| `files/briefs/agentic-lean-marketing-stack.md` | `briefs/agentic-lean-marketing-stack.md` | The strategic-aha brief locking the marketing stack (Cosmic / Attio / Vercel / Cloudflare / Resend / Cookiebot). Frontmatter unchanged — `departments: [ai-office, marketing, it-ops]` already lists Marketing. Owner stays michael-bruck for now; Andrew may flip to owner if he wants Marketing to maintain the brief going forward. |

#### Projects (11)

| File | Marketing target path | Notes |
|---|---|---|
| `files/projects/janus-website.md` | `projects/janus-website.md` | The marketing-site rebuild hub. Substantial content. |
| `files/projects/janus-website-cms.md` | `projects/janus-website-cms.md` | Cosmic decision + alternatives evaluated. |
| `files/projects/janus-crm-selection.md` | `projects/janus-crm-selection.md` | Attio decision + alternatives evaluated. |
| `files/projects/crm-evaluation-and-selection.md` | `projects/crm-evaluation-and-selection.md` | The broader CRM evaluation history (HubSpot-leaning → Attio flip). Cross-link with `janus-crm-selection.md`. |
| `files/projects/singapore-launch.md` | `projects/singapore-launch.md` | The Singapore campaign + lunch postponement. Operational marketing project. |
| `files/projects/janus-thought-leadership.md` | `projects/janus-thought-leadership.md` | Stub. Marketing may consolidate or expand. |
| `files/projects/janus-careers-page.md` | `projects/janus-careers-page.md` | Stub. Marketing × HR boundary; Marketing owns brand surface. |
| `files/projects/janus-marketing-capabilities.md` | `projects/janus-marketing-capabilities.md` | Stub. The five-capability framework hub. |
| `files/projects/janus-brand-guidelines-refresh.md` | `projects/janus-brand-guidelines-refresh.md` | Stub. The agency-led brand refresh in flight. |
| `files/projects/janus-prime-radiant-marketing.md` | `projects/janus-prime-radiant-marketing.md` | Stub — alternative slug for marketing-prime-radiant. Marketing may retire or merge. |
| `files/projects/apply-standup-methodology-to-andrew-work-stream.md` | `projects/apply-standup-methodology-to-andrew-work-stream.md` | Workstream porting AIO standup discipline to Andrew. Owner is Michael; flip to Andrew on import. |

#### Decisions (19, deduplicated)

Picked the cleaner-titled / more-complete version where duplicates exist. Alternates left in AIO for the audit trail. All canonical to Marketing going forward; AIO-side becomes federation pointers.

| File | Notes |
|---|---|
| `files/decisions/2026-05-05-commission-london-agency-brand-guidelines.md` | Brand-refresh authorisation |
| `files/decisions/2026-05-05-crm-shortlist-for-evaluation.md` | Initial CRM shortlist |
| `files/decisions/2026-05-05-five-marketing-capabilities-framework.md` | The five-capability framework decision |
| `files/decisions/2026-05-05-five-marketing-capabilities-scoped.md` | Scoping of the same |
| `files/decisions/2026-05-05-janus-needs-a-crm.md` | The decision to evaluate CRMs |
| `files/decisions/2026-05-05-stand-up-ai-marketing-workspace.md` | The marketing-workspace authorisation |
| `files/decisions/2026-05-05-stand-up-shared-marketing-surfaces.md` | Shared surfaces authorisation |
| `files/decisions/2026-05-05-website-build-in-house-not-agency.md` | Website-build approach |
| `files/decisions/2026-05-07-llm-wiki-extends-to-marketing-domain.md` | The decision that authorised the Marketing instance |
| `files/decisions/2026-05-08-marketing-prime-radiant-as-separate-vault.md` | Vault topology |
| `files/decisions/2026-05-08-marketing-prime-radiant-greenlit-with-andrew.md` | Greenlight decision with Andrew |
| `files/decisions/2026-05-12-three-messaging-pillars-society-business-individual.md` | Society / Business / Individual pillars (chose this version over the 2026-05-12-three-messaging-pillars variant) |
| `files/decisions/2026-05-12-marketing-pr-outputs-reordered.md` | Plans + campaigns first, briefs + positioning second, POVs + white papers third |
| `files/decisions/2026-05-12-anti-ai-washing-as-content-discipline.md` | The anti-AI-washing content rule |
| `files/decisions/2026-05-12-generalise-factset-to-news-sources.md` | FactSet → generic news-sources framing (chose this version over the drop-factset variant) |
| `files/decisions/2026-05-12-interim-lead-capture-via-google-form-sheet.md` | Interim lead-capture mechanism for SG launch |
| `files/decisions/2026-05-12-single-domain-gems-com-with-country-paths.md` | Single-domain ccTLD architecture (also in the Singapore bundle for completeness) |
| `files/decisions/2026-05-12-start-marketing-prime-radiant-without-waiting-for-crm.md` | Start the Marketing instance immediately (chose this version over the start-before-crm variant) |
| `files/decisions/2026-05-12-treat-onboarding-deck-as-plan-of-record.md` | Onboarding deck as the marketing-plan-of-record |
| `files/decisions/2026-05-13-andrew-soane-first-cross-dept-prime-radiant-rollout.md` | Andrew as the first cross-dept rollout target |
| `files/decisions/2026-05-13-onboard-andrew-soane-as-first-cross-dept-prime-radiant-pilot.md` | The onboarding pilot itself |
| `files/decisions/2026-05-18-gated-white-paper-pattern.md` | White paper behind email capture |
| `files/decisions/2026-05-18-janus-website-hostinger-deploy.md` | Hostinger deploy decision (superseded later by Vercel + Cloudflare in the agentic-lean stack brief) |
| `files/decisions/2026-05-18-website-react-typescript-full-rebuild.md` | Full React/TypeScript rebuild |

#### Sources (3 articles + 5 meetings)

| File | Notes |
|---|---|
| `files/sources/articles/marketing-stack-technical-writeup.md` | Michael's technical writeup → Jehad on the marketing stack |
| `files/sources/articles/2025-janus-brand-guidelines-v1.0.md` | Brand guideline markdown twin |
| `files/sources/articles/2025-janus-brand-guidelines-v1.0.pdf` | Brand guideline PDF |
| `files/sources/meetings/2026-05-08-andrew-marketing-prime-radiant.md` | Marketing PR greenlight session |
| `files/sources/meetings/2026-05-12-aio-andrew-marketing.md` | The 12 May Andrew × Michael × Bonaventure call |
| `files/sources/meetings/2026-05-12-andrew-onboarding-review.md` | The 3pm Andrew session |
| `files/sources/meetings/2026-05-12-prime-radiant-marketing-setup-debug.md` | Marketing-instance setup debug session |
| `files/sources/meetings/2026-05-19-aio-mktg-meeting.md` | Marketing-stack lock-in session |

### Dual-location — both vaults carry; updates flow via the mesh subfolder

#### Briefs (1)

| File | Notes |
|---|---|
| `files/briefs/ai-native-janus-positioning.md` | Bonaventure's three-pillar positioning thesis. Marketing uses it as Infrastructure-layer content. Dual-location: AIO-canonical (positioning thesis lives with the framework author), Marketing carries a copy for daily reference. |

#### Concepts (5)

| File | Notes |
|---|---|
| `files/concepts/stack-composition-framework.md` | Three-lens framework for tool selection. Marketing uses it for stack decisions; AIO uses it as a framework primitive. Dual. |
| `files/concepts/builders-sellers-measurers.md` | Drucker frame. Used by Marketing for hiring + positioning; AIO uses it framework-wide. Dual. |
| `files/concepts/buyer-personas.md` | Marketing Infrastructure concept (stub — Marketing should populate). Dual but Marketing operationally owns. |
| `files/concepts/messaging-pillars.md` | Marketing Infrastructure concept (stub — Marketing should populate). |
| `files/concepts/ai-washing.md` | Anti-AI-washing content discipline concept. |

#### Processes (1)

| File | Notes |
|---|---|
| `files/processes/janus-html-deck-brand-guideline.md` | v1.1 brand guideline. Dual-location; both vaults reference it for deck production. |

#### Decisions — org-wide that Marketing should carry (5)

| File | Notes |
|---|---|
| `files/decisions/2026-05-12-html-as-presentation-format-adopted.md` | HTML over PowerPoint, organisation-wide |
| `files/decisions/2026-05-13-prefer-html-over-powerpoint-for-claude-generated-decks.md` | Same direction, follow-on |
| `files/decisions/2026-05-11-notion-restricted-to-aio-no-broad-rollout.md` | Affects Marketing (no Notion for non-AIO use) |
| `files/decisions/2026-05-08-per-department-prime-radiant-instances.md` | Each department gets its own instance — foundational federation decision |
| `files/decisions/2026-05-13-github-canonical-prime-radiant-substrate.md` | GitHub as the canonical substrate — applies to the Marketing instance |

#### Entities — internal (2)

| File | Notes |
|---|---|
| `files/entities/internal/andrew-soane.md` | Andrew (CMO). Dual-location — both vaults carry his entity page. |
| `files/entities/internal/bonaventure-wong.md` | Bonaventure (CEO). Dual-location. |

#### Entities — vendors (7 — the marketing-stack-relevant ones)

| File | Notes |
|---|---|
| `files/entities/vendors/resend.md` | Confirmed for transactional email; 3/3 on Stack Composition Framework. AIR-118. Dual. |
| `files/entities/vendors/mailchimp.md` | Held open (Rejected → Backlog). AIR-111. Dual. |
| `files/entities/vendors/monday.md` | Includes explicit "not the Janus CRM" framing. Dual (AIO uses for AI Registry tracking; Marketing uses for execution). |
| `files/entities/vendors/canva.md` | Marketing-candidate (AIO-99, Backlog). |
| `files/entities/vendors/marketo.md` | Monitored signal source. |
| `files/entities/vendors/microsoft-clarity.md` | Marketing analytics candidate (AIO-102). |
| `files/entities/vendors/linkedin-marketing-solutions.md` | B2B advertising suite (AIO-98). |

#### Assets (5)

| File | Notes |
|---|---|
| `files/assets/branding/janus-logo-white.svg` | Official logo, white-variant. |
| `files/assets/branding/janus-logo-black.svg` | Official logo, black-variant. |
| `files/assets/janus-html-deck/SKILL.md` | Skill bundle spec (v1.1 wiki snapshot; v1.0 of skill itself per the file's own provenance section). |
| `files/assets/janus-html-deck/template.html` | Working template. |
| `files/assets/janus-html-deck/example-deck.html` | Reference deck demonstrating all 10 slide patterns. |

## Marketing vault `index.md` — section-by-section suggested additions

### Briefs section

```
- [agentic-lean-marketing-stack](briefs/agentic-lean-marketing-stack.md) — why MCP-native tooling collapses SaaS sprawl risk for Janus; the strategic-aha brief locking the marketing stack on Cosmic / Attio / Vercel / Cloudflare / Resend / Cookiebot. [active, high]
- [ai-native-janus-positioning](briefs/ai-native-janus-positioning.md) — Bonaventure's three-pillar messaging spine (Society / Business / Individual). Marketing Infrastructure. Dual-located with AIO. [active, high]
```

### Concepts section

```
- [ai-washing](concepts/ai-washing.md) — anti-AI-washing content discipline concept. [stub, populate]
- [builders-sellers-measurers](concepts/builders-sellers-measurers.md) — Drucker's role trichotomy applied to AI restructuring. Use for hiring strategy + positioning content. [high]
- [buyer-personas](concepts/buyer-personas.md) — Marketing Infrastructure (Personas vocabulary). [stub, populate]
- [messaging-pillars](concepts/messaging-pillars.md) — Marketing Infrastructure (the three-pillar spine vocabulary). [stub, populate]
- [stack-composition-framework](concepts/stack-composition-framework.md) — three-lens evaluation layer for tool selection. [high]
```

### Processes section

```
- [janus-html-deck-brand-guideline](processes/janus-html-deck-brand-guideline.md) — v1.1 brand guideline (palette + Montserrat + logo + structural elements + 10 slide patterns + workflow). Skill bundle at `assets/janus-html-deck/`.
```

### Projects section — substantive entries

```
- [janus-website](projects/janus-website.md) — the Janus Digital marketing website (janusd.com / janusd.sg). Phase 1 in flight. [active]
- [janus-website-cms](projects/janus-website-cms.md) — Cosmic as the locked-in headless CMS. Onboarding in June. [active]
- [janus-crm-selection](projects/janus-crm-selection.md) — Attio as the locked-in CRM (flipped from HubSpot-leaning). [active]
- [crm-evaluation-and-selection](projects/crm-evaluation-and-selection.md) — broader CRM evaluation history. [active]
- [singapore-launch](projects/singapore-launch.md) — Singapore campaign + the September 2026 lunch (postponed from July). [active]
```

### Projects section — stubs to populate or retire

```
- [janus-brand-guidelines-refresh](projects/janus-brand-guidelines-refresh.md) — the agency-led brand refresh; stub. [active, stub]
- [janus-careers-page](projects/janus-careers-page.md) — careers brand surface (marketing × HR). [active, stub]
- [janus-marketing-capabilities](projects/janus-marketing-capabilities.md) — five-capability framework hub. [active, stub]
- [janus-thought-leadership](projects/janus-thought-leadership.md) — thought-leadership work. [active, stub]
- [apply-standup-methodology-to-andrew-work-stream](projects/apply-standup-methodology-to-andrew-work-stream.md) — port the AIO standup discipline to Andrew's workflow. [active]
```

### Decisions section

Add the 24 imported decision pages. Suggest alphabetising the existing entries and inserting in chronological order. The 2026-05-05 batch (8 decisions), 2026-05-07 (1), 2026-05-08 batch (3), 2026-05-11 (1), 2026-05-12 batch (7), 2026-05-13 batch (3), and 2026-05-18 batch (3).

### Vendors section

Add the 7 marketing-stack vendor pages. Note any vendors already in the Marketing vault — overwriting is acceptable since these are dual-location.

### Internal section

Add `andrew-soane` and `bonaventure-wong` if not already present.

## Marketing vault `log.md` — suggested import entry

```
## [2026-05-22 HH:MM] import | broader marketing corpus federation handoff from AIO | bundle #2 | 66 markdown + 1 PDF + 2 SVG
- driver: cross-vault federation transfer (companion to the Singapore-monitoring handoff). The full marketing-domain knowledge body the AIO has accumulated from 2026-05-04 onward moves to the Marketing instance where it operationally belongs.
- imported counts (see migration-manifest.md for the file-by-file list):
  - canonical-to-Marketing: 1 brief, 11 projects, 24 decisions, 8 sources (3 articles + 5 meetings + 1 PDF + brand-md-twin)
  - dual-location: 1 brief, 5 concepts, 1 process, 5 org-wide decisions, 2 internal entities, 7 vendor entities, 5 asset files
- not imported (stays AIO-canonical):
  - briefs/coordination-leverage-model.md, ai-native-enterprise-restructuring.md
  - concepts/coordination-three-layer-model, coordination-tax, organisational-digital-twin, ai-policy, pilot-in-command, shadow-ai-prohibition, tool-tiers, sandbox-environment
  - processes/ai-tool-evaluation-framework, ai-registry, ai-policy-gate-approval
  - questions/2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room
  - All AIO operational pages (standup, AI Registry skill references)
- next actions: triage the 5 stub project hubs (fill / merge / retire); confirm owner for apply-standup-methodology + marketing-capabilities; if Andrew wants to maintain agentic-lean-marketing-stack going forward, flip the owner.
```

## Cross-vault wikilinks expected to resolve via federation

The transferred files contain many wikilinks pointing at AIO-canonical content. Marketing vault resolves these via the mesh `entities/departments/ai-office/` shared subfolder. Most-frequent cross-vault references:

- `[[coordination-leverage-model]]`, `[[coordination-three-layer-model]]`, `[[coordination-tax]]`, `[[organisational-digital-twin]]`, `[[builders-sellers-measurers]]`
- `[[ai-native-enterprise-restructuring]]`
- `[[ai-policy]]`, `[[ai-tool-evaluation-framework]]`, `[[ai-registry]]`, `[[shadow-ai-prohibition]]`, `[[tool-tiers]]`, `[[sandbox-environment]]`, `[[pilot-in-command]]`
- `[[2026-05-22-coordination-leverage-model-principle-10-framer-stays-in-the-room]]`
- `[[peer-to-peer-mesh-federation-pattern]]`, `[[prime-radiant-three-layer-architecture]]`
- `[[standup]]`, `[[fireflies]]`, `[[ai-registry]]`
- `[[anthropic]]`, `[[claude]]`, `[[notion]]`, `[[linear]]`, `[[hostinger]]`, `[[github]]`
- `[[jehad-altoutou]]`, `[[michael-bruck]]`, `[[euclid-wong]]`, `[[joyce-woo]]`, `[[vivian-balakrishnan]]`

Same federation-mesh resolution pattern as the Singapore bundle. Dangling wikilinks are acceptable for the first 2–4 weeks while the mesh sync is wired up — they're informational.
