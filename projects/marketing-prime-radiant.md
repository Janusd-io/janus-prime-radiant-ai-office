---
type: project
title: Janus Prime Radiant · Marketing
slug: marketing-prime-radiant
created: 2026-05-08
updated: 2026-05-12
departments: [marketing, ai-office]
status: active
owner: michael-bruck
sources: [2026-05-08-andrew-marketing-prime-radiant, 2026-05-11-aio-standup-with-jehad, 2026-05-12-bonaventure-ai-native-call, 2026-05-12-andrew-onboarding-review]
related: [andrew-soane, marketing, janus-prime-radiant-build, llm-wiki, 2026-05-07-llm-wiki-extends-to-marketing-domain, 2026-05-08-marketing-prime-radiant-greenlit-with-andrew, 2026-05-08-marketing-prime-radiant-as-separate-vault, crm-evaluation-and-selection, singapore-news-monitoring, peer-to-peer-mesh-federation-pattern, 2026-05-11-andrew-onboarding-plan, ai-native-janus-positioning, 2026-05-12-singapore-as-lead-market, 2026-05-12-html-as-presentation-format-adopted, 2026-05-12-marketing-pr-outputs-reordered, 2026-05-12-website-architecture-one-site-vs-country-sites, 2026-05-12-anti-ai-washing-as-content-discipline]
---

# Janus Prime Radiant · Marketing

Build hub for the Marketing-department Prime Radiant — a **full institutional knowledge base for the Marketing department**, not a "PR project." Scope clarified 2026-05-08 ([[2026-05-08-marketing-prime-radiant-as-separate-vault|see decision]]): this is the second live Prime Radiant instance (after [[ai-office]]'s), with its own Google Shared Drive vault and its own `CLAUDE.md` derived from the AIO one. Pilot kicked off in the 2026-05-08 working session with [[andrew-soane]] (CMO). The Marketing instance is being built in parallel with continued AIO honing — kicking off a new instance does not freeze the AIO instance, and the Marketing instance is the first concrete test of the federation pattern (`entities/departments/` cross-references between separate vaults).

## Origin

Authorised in the 2026-05-08 brainstorm with Andrew Soane ([[2026-05-08-andrew-marketing-prime-radiant|raw transcript]]; [[2026-05-08-marketing-prime-radiant-greenlit-with-andrew|decision record]]). Michael demoed the AIO Prime Radiant to Andrew, walked through synthesised insights / concepts / projects / decisions / lessons / pulse / briefs, and Andrew's response was: build one for Marketing.

The originating context goes back further — the Marketing instance was anticipated in the [[2026-05-07-llm-wiki-extends-to-marketing-domain|2026-05-07 decision]] when the AIO prototype was first validated. Andrew's brainstorm turned the *anticipated* into *in flight*.

## Scope

Stand up a Marketing-domain Prime Radiant that:
- Captures all the right Signals (Fireflies, Slack, CRM once selected, inbound web messages, emails, news scraping, competitor intel, industry analyst opinions across Janus's verticals — real estate, real assets, built environments, asset management, sustainability, private equity, credits).
- Documents the Infrastructure layer Marketing needs to make explicit (ICP, Target Personas, Bonaventure's mission, country plans, topic taxonomy).
- Generates Outputs that compress operational marketing work — strategic POVs, white papers, blog posts, marketing plans, campaigns + assets, positioning documents, reporting that feeds back to learning.

Inherits the three-layer architecture model from CLAUDE.md v0.8 (Signals / Infrastructure / Outputs).

## Architecture (per three-layer model)

**Signals layer (sensors):**
- Fireflies meeting transcripts (Andrew's calls with prospects, partners, advisers)
- Slack threads (bookmarked)
- CRM (once selected — see [[crm-evaluation-and-selection]]; agentic-capable CRM is the gating dependency)
- Inbound web messages from janus.com forms
- Emails (CRM-routed; raw email ingest deferred)
- Curated articles via Web Clipper (Andrew adds; eventually automated news scraping)
- Industry-vertical news feeds: AI in real estate / real assets / built environments; investments + banking + asset management; sustainability; private equity; credits
- Competitor intel and industry analyst opinion pieces

**Infrastructure layer (durable reference — required for Outputs):**
- **Ideal Customer Profile** — types of companies Janus targets (pending; Andrew action item)
- **Target buyer Personas** — CFO, COO, sustainability leads, PE / asset management decision-makers (pending)
- **Mission and multi-year strategy** — sourced from [[bonaventure-wong]] / [[office-of-ceo]]
- **Country plans** — SGP (W19 launch), GB (W20 launch), expansion targets
- **Topic taxonomy** — sustainability regulation, AI in real estate, asset management trends, finance verticals

**Outputs layer (what the instance produces):** *(Reordered 2026-05-12 per [[2026-05-12-marketing-pr-outputs-reordered]] — plans / campaigns first to anchor scope as a full marketing function, not a white-paper engine)*

1. **Marketing plans, campaigns and supporting assets** — annual / quarterly plans; campaign briefs and execution assets; promotion sequencing.
2. **Briefs and positioning** — campaign briefs (positioning *first*, then assets); narrative spine for content production.
3. **POVs, thought leadership, white papers and other long-form / short-form** — POV documents, white papers, blog posts, social content. One delivery format among several, not the destination.
4. **Reporting decks** (event attendance, content downloads, web analytics) feeding back into Signals as performance data.

## Build sequence

Per CLAUDE.md §1 Architecture build pattern (Signals → Infrastructure → Outputs):

1. **Signals first** (immediately doable): Fireflies + Slack + curated articles via Web Clipper. This gives the instance enough perception to start surfacing patterns even before the CRM is in place.
2. **Infrastructure next** (Andrew dependency): ICP, Personas, mission, country plans documented as durable reference pages. Andrew's first sketch of inputs/outputs (committed to in the brainstorm) feeds this.
3. **Outputs follow** (when Infrastructure is in place): briefs, POVs, campaign drafts. Outputs cannot be top-down designed before Infrastructure is captured — that's the architectural lesson from the AIO instance and the Marketing brainstorm both.

## Status (as of 2026-05-11)

- **Andrew confirmed as active test case** per AIO 11 May standup. The meeting discussed enrolling [[simon-tarskih|Simon]] in the personal-vault pattern and concluded: hold off on Simon until he has a clear use case ("It's too early for Simon. Andrew is our test case."). Andrew remains the pilot ramp for the Marketing instance.
- Greenlit in 2026-05-08 brainstorm: ✅ ([[2026-05-08-marketing-prime-radiant-greenlit-with-andrew]])
- Vault topology decided: ✅ — separate Google Shared Drive folder + own `CLAUDE.md` derived from AIO one ([[2026-05-08-marketing-prime-radiant-as-separate-vault]]). Sets the precedent for HR / Finance / IT-Ops / Office-of-CEO / Engineering / Training instances to follow.
- Schema available: CLAUDE.md v0.8 (formalised three-layer architecture, added `entities/departments/` federation type)
- Department entity page in AIO vault: [[marketing]] — created
- Drive folder: **not yet created** — Michael action. Suggested name: *Janus Prime Radiant — Marketing*, parallel to the AIO Shared Drive folder.
- Marketing CLAUDE.md: not yet authored. First draft will derive from AIO CLAUDE.md v0.8 with entity vocabulary adapted per CLAUDE.md §1 Domain generalisability (possible additions: `entities/outlets/`, more prominent `entities/clients/`, possibly `entities/campaigns/` and/or `entities/personas/` — final shape TBD).
- Inputs status: Fireflies and Slack accessible; CRM blocked on [[crm-evaluation-and-selection]] (gating dependency for Signals-layer richness, not blocker for design/architecture work); Web Clipper Marketing-themed channel pending setup.
- Infrastructure status: ICP / Personas / mission / country plans / topic taxonomy not yet documented. Andrew action item; this is the **highest-leverage pre-CRM work** because Outputs depend on it.
- Andrew's sketch of inputs/outputs: committed to in brainstorm; pending delivery (Andrew said "I'll draw this up... it won't be very pretty").
- Andrew's "next Tuesday" target: aspirational, not committed. Realistic v0 is a working frame Andrew can react to, with the vault standing-up + CLAUDE.md derivation + Infrastructure-layer scaffolding partly done; full Signals integration follows when CRM lands.

## Architecture work that proceeds pre-CRM

CRM-independent design work that should happen *now* (does not wait for the CRM evaluation to resolve):

1. **Vault stand-up** (Michael) — create the new Shared Drive folder; mirror the AIO scaffolding (`inbox/`, `sources/{meetings,articles,linear,monday,slack,notion}/`, `entities/{vendors,clients,people,internal,departments}/`, `concepts/`, `processes/`, `projects/`, `decisions/`, `lessons/`, `questions/`, `pulse/`, `briefs/`); seed `log.md` + `index.md`.
2. **Marketing CLAUDE.md derivation** (Michael) — adapt AIO CLAUDE.md v0.8 for the Marketing domain. Schema discipline carries over verbatim; entity vocabulary swap is the main design move. Decide whether to add domain-specific entity folders (outlets / campaigns / personas / themes) or treat those as Infrastructure-layer docs vs concepts vs projects.
3. **Infrastructure layer scaffolding** (Andrew + Michael) — create stub pages for ICP, target Personas, mission framing, country plans (SGP / GB / future), topic taxonomy (real estate / asset management / sustainability / PE / credits). Stubs first; Andrew fills in content as available.
4. **Federation linkages to AIO** — the AIO `entities/departments/marketing.md` page gets a note pointing at the canonical Marketing Prime Radiant vault once it exists. The Marketing vault's `entities/departments/ai-office.md` stub points back. This is the lightweight federation pattern; heavier mechanisms (skill-driven cross-vault signal flow) deferred.
5. **Seed entity pages** — Andrew's entity page from the Marketing vault's perspective; an internal-people subset relevant to Marketing (Bonaventure for mission/strategy reference, Michael as build partner); first vendor pages for Marketing-relevant tooling (CRM-candidates entity stubs even if undecided; potential email-marketing tools like [[marketo]] candidate; social-media-management tools when Andrew names them).
6. **Inaugural source ingest** — the 2026-05-08 Andrew brainstorm transcript filed in the Marketing vault as the originating source (analogous to how the Karpathy gist seeded the AIO vault). This grounds the Marketing instance's history in the founding conversation.

Everything above is CRM-independent and can ship before CRM selection lands. CRM-dependent work (full Signals layer richness, lead/opportunity ingest, email-thread capture) waits for the CRM decision.

## Action items from the 2026-05-08 brainstorm

From [[2026-05-08-andrew-marketing-prime-radiant|the transcript]], roughly in priority order:

1. **Andrew**: read Michael's HubSpot CRM evaluation document (sent earlier; not yet read).
2. **Andrew**: draw up signals / inputs / outputs sketch for the Marketing instance (verbal commitment).
3. **Andrew**: be more disciplined about labelling speakers in Fireflies (Michael walked him through the in-app speaker tagging).
4. **Michael**: feed transcript back to Claude (this ingest pass) and seed the Marketing instance design (in flight).
5. **Michael**: expand CRM benchmark beyond HubSpot to Monday, Salesforce, HubSpot, Attio (Bonaventure prefers ≥3 options; Zoho on watch).
6. **Both**: align on CRM requirements — Andrew's draft has gaps; Michael adds MCP / agentic-capability as a hard criterion.

## Open dependencies

- **CRM selection** — gating dependency for Signals layer richness *only* (lead flow, email threading, inbound web message ingest). Not a blocker for the pre-CRM architecture work above. See [[crm-evaluation-and-selection]].
- **Marketing infrastructure documents** — ICP, Personas, mission framing, country plans, topic taxonomy. Andrew dependency. Highest-leverage pre-CRM deliverable because Outputs (briefs, POVs, campaign drafts) can't emerge without it.
- **Marketing CLAUDE.md derivation** — Michael action. Will define the Marketing entity vocabulary (outlets / campaigns / personas as candidates).
- **Federation mechanism** — cross-instance signal sharing is light at v0.8 (`entities/departments/` stubs in each vault, manual cross-reference); skill-driven federation deferred until the multi-instance pattern is proven beyond Marketing.
- **Tier 3 brief on the "10 → 2-3 strategic operators" hypothesis** — explicitly on hold per Michael "pending the refinement of the design per the above."

## Cross-instance federation

Federates with:
- [[ai-office]] — AI tooling decisions matter for marketing-tech (CRM, marketing automation, content generation).
- [[office-of-ceo]] — mission, strategy, and country plans live there; Marketing's Infrastructure derives from them.
- [[hr]] — employer brand is an HR / Marketing crossover.

## Andrew onboarding plan

The cross-department curator handover for Andrew is captured in [[2026-05-11-andrew-onboarding-plan]] — a sendable pre-read for Andrew's kickoff walkthrough, structured as the canonical Stage 1 onboarding artefact that will generalise into a `processes/department-instance-onboarding.md` runbook when the next department (HR, ISO, Finance) goes through it.

## Update — 2026-05-12 AI Native CEO call

Bonaventure validated the overall direction and surfaced reframing input that affects Marketing PR scope:

- **Three-pillar messaging spine is the Marketing PR Outputs frame.** Per [[ai-native-janus-positioning]], capital → companies → workers becomes the spine that POVs, white papers, campaign briefs are designed to deliver. Andrew's Outputs are not "marketing content" in the generic sense — they're the public surface of the [[ai-native-janus-positioning|AI Native pitch]].
- **Singapore-first.** Per [[2026-05-12-singapore-as-lead-market]] the Marketing PR Outputs should be scoped Singapore-first in v0; expansion to UAE / UK as country-go-to-market intelligence matures.
- **HTML-as-output endorsed by CEO.** Bonaventure approved the HTML format for the onboarding deck Michael showed on the call. See [[2026-05-12-html-as-presentation-format-adopted]]. Campaign briefs, POVs, white papers, reporting decks — all default HTML.
- **Bonaventure's ICP frame is open.** Bonaventure questioned the "ideal customer profile" / "target Personas" framing on the call ("What ideal customer? What was the ideal person... let's see if he matches mine"). Implies he has his own ICP view that Andrew's first sketch should be compared against. Worth surfacing his ICP framing as a Marketing PR Infrastructure-layer input — direct conversation needed.
- **CRM downgrade.** Bonaventure dial-in on the CRM (see [[crm-evaluation-and-selection]] update) reinforces CRM-not-in-critical-path: scope-skepticism, output-spec-required, minimum-viable Singapore-first. Marketing PR can ship Signals + Infrastructure + initial Outputs without it.
- **3pm Andrew meeting (12 May)** — Michael's working session today walks Andrew through the briefing deck (built earlier as `andrew-onboarding-deck-...`). Output of that session feeds the next iteration of the Marketing PR design.
- **Bonaventure concerns re Andrew/CRM scope.** "I want to drill down everything line of the brief he has with an ad company to kind of do our logo and our website and all that kind of stuff. I will just say we could do that ourselves." Flag: Bonaventure thinks some of Andrew's external-agency scope could be brought in-house through Janus's own AI-Native capabilities. Worth a follow-up on what Andrew has committed to externally.

## Update — 2026-05-12 Andrew onboarding review (3pm session)

Source: [[2026-05-12-andrew-onboarding-review]] (~50-min session walking Andrew through the HTML onboarding deck built earlier).

### Scope refinements Andrew committed to

- **Outputs reordered** per [[2026-05-12-marketing-pr-outputs-reordered]] — plans / campaigns first, briefs / positioning second, POVs / white papers / assets third. Counters the white-paper-centric framing Andrew hears from Bonaventure.
- **Three pillars articulated** (Andrew's working framing of the [[ai-native-janus-positioning|three-pillar messaging spine]]):
  - **Society** — driving the sustainability and ESG agenda; impact on society.
  - **Business** — AI as a growth engine; impact on business capital.
  - **Individual** — augment / upskill / certify people; "Uber for engineers"; impact on workers.
  - Pillars will dictate content navigation on the website + the categorisation of all Outputs. Same spine as Bonaventure's morning framing (capital → companies → workers), reordered to lead with audience-of-impact rather than money.
- **FactSet de-emphasised; LinkedIn primary.** Andrew pushed back on FactSet-specific framing in the deck — "if you looked at this, you think FactSet, we're going to define everything around FactSet... that's not a poor strategy." Reframed as generic "news sources / information gathering." Andrew: *"the biggest single source of intelligence for us will be LinkedIn. And then stuff like Twitter."* (Note: this contradicts Bonaventure's morning FactSet suggestion — see [[ingest-2026-05-12-1730-vivian-balakrishnan-and-factset]] which now needs re-scoping.)
- **AI-washing as content angle.** Andrew committed to a first social post today on the "AI Powered Living" property-development example Michael spotted. The pattern — "name three things that make it AI" — is captured as a content-discipline lesson at [[2026-05-12-anti-ai-washing-as-content-discipline]]. Series potential.

### Singapore launch campaign (8th–9th July luncheon target, <60 days)

- **Personas:** asset managers — specifically **GPs and LPs** (general partners / limited partners). Confirmed on the call.
- **Campaign mix:** paid advertising + organic social + PR (Business Times tried; other PR being explored) + landing-page + lead-capture funnel.
- **White paper** as the campaign anchor — multiple promotions of the white paper.
- **Lead capture funnel:** form on the Singapore landing page → Google Sheets (interim, until CRM lands) → invite list for the July luncheon → nurture sequence.
- **Goal volume:** tens to low hundreds of qualified records by July — not thousands; signal-quality matters more than scale.

### Website architecture (open question)

- **Single landing page needed in *days*** for the Singapore launch — white-paper headlines + registration form + data-privacy notice.
- **CMS selection question is downstream** — Andrew wants a CMS; candidates floated were Wix, Firebase, or custom. Multilingual capability is a hard requirement.
- **Architecture choice** — one Janus site (`janusd.com/sg`) with country sub-paths vs standalone country sites (`janusd-sg.com`) — captured as the open question [[2026-05-12-website-architecture-one-site-vs-country-sites]]. Andrew anticipates a "mighty battle" with Bonaventure on this. Sequenced ahead of the landing-page work.

### CRM timing committed

- HubSpot decision target: **~2-3 weeks** to recommendation that Bonaventure agrees with.
- Implementation / SaaS terms: **~3 more weeks** for negotiation + setup (Michael thinks shorter given low seat count).
- **Total runway:** end-May / first-week-June for decision; mid-June for live implementation.
- CRM remains *not in critical path* — Marketing PR Signals + Infrastructure + initial Outputs proceed without it. Google Sheets is the interim system-of-record for Singapore-launch leads. See [[crm-evaluation-and-selection]].
- Marketing-CRM (campaign management) vs sales-CRM (pipeline) distinction confirmed — Marketing PR needs the marketing-campaign-management capabilities specifically.

### Andrew action items (1-week horizon)

1. **ICP draft completion** — working skeleton exists; needs cross-tally with Bonaventure's separately-developed ICP repository.
2. **Target Personas** — working version exists; same cross-tally work.
3. **Topic taxonomy / themes** — three-pillar spine maps to themes; specific topic taxonomy in draft.
4. **First social post on AI-washing** — today (12 May).
5. **Singapore landing page** — in the next few days, pending website-architecture resolution.

### Michael action items (this week)

1. **Tooling install session** with Andrew on his Mac — Cowork project + Obsidian + Web Clipper + Fireflies connector check. Andrew confirmed he's been getting Cowork connector warnings; needs reset. Thursday or Friday this week best (Bonaventure on holiday, less traffic).
2. **Bulk Fireflies ingest** of Andrew's prior meetings — single command via the Web Clipper → Inbox → ingest flow, will give the Marketing instance an immediate-seed of context.
3. **Web Clipper config** for marketing-themed content channel.
4. **Update the onboarding deck** based on this transcript (Michael said on the call he'd feed the transcript back to Claude for revision) — same artefact, same `aio-update-bonaventure-...` HTML pattern.

### Notes from the meeting

- **Notion is not the source of truth for Marketing PR.** Andrew started exploring Notion this week because "Claude told me to use it" for the Singapore launch page. Michael clarified: Claude defaults to Notion for some artefacts because of training data, not because Notion is the right tool. Will reassess what Andrew actually needs.
- **Bonaventure on holiday Wed onward.** Window of relative quiet for Andrew + Michael to do the tooling install + first-content sprint Thursday-Friday.
- **Mac vs Windows tooling** — both Andrew and Michael on Mac; rollout to Windows users (Euclid's team, others) will need separate tooling support pass. Flagged for IT-Ops instance prep.

## Related

[[marketing]] · [[andrew-soane]] · [[janus-prime-radiant-build]] · [[llm-wiki]] (methodology) · [[2026-05-07-llm-wiki-extends-to-marketing-domain]] · [[crm-evaluation-and-selection]] · [[singapore-news-monitoring]] · [[2026-05-11-andrew-onboarding-plan]]
