---
type: brief
title: Andrew's onboarding plan — Marketing Prime Radiant, Stage 1
slug: 2026-05-11-andrew-onboarding-plan
created: 2026-05-11
updated: 2026-05-12
departments: [ai-office, marketing]
status: active
confidence: high
sources: [2026-05-08-andrew-marketing-prime-radiant, 2026-05-12-andrew-onboarding-review]
related: [peer-to-peer-mesh-federation-pattern, marketing, ai-office, andrew-soane, michael-bruck, marketing-prime-radiant, ai-native-janus-positioning, 2026-05-12-marketing-pr-outputs-reordered, 2026-05-12-website-architecture-one-site-vs-country-sites, 2026-05-12-anti-ai-washing-as-content-discipline]
---

# Andrew's onboarding plan — Marketing Prime Radiant, Stage 1

> Draft pre-read for Andrew before our kickoff walkthrough. Sendable as-is (email, Slack, Google Doc); also lives here as institutional record of how we ran the first cross-department curator handover. Generalises into a future `processes/department-instance-onboarding.md` runbook when the next department (HR, ISO, Finance) goes through it.

---

**To:** Andrew Soane
**From:** Michael Bruck
**Re:** Onboarding to the Marketing Prime Radiant — pre-read for our walkthrough

---

Andrew,

Picking up where we left off on May 8 — I've spent the past few days standing up the Marketing version of what we demoed for you, what you called "the brain." It's live; the underlying Drive folder is already shared with you. Before we sit down to walk through it, here's the plan.

## What we're building

A working brain for the Marketing function — same pattern I showed you, tuned to you and to Janus Marketing specifically. It's a shared Drive folder; you interact with it through Claude (Cowork); you can browse and edit it directly in Obsidian; it captures inputs from your meetings, your Slack threads, articles you flag, relevant Notion docs. It then *synthesizes* across those inputs to produce things we actually want — POVs, briefs, campaign plans, positioning, white-paper drafts, country-launch playbooks. Over time it becomes the institutional memory of Marketing — and the bridge into Bonaventure's eventual digital-twin layer.

The technical name for it is "Janus Prime Radiant · Marketing." But the brain framing you used is the right one to keep in mind day-to-day.

## Why we're doing this in stages

There's a lot you might eventually want this brain to do — connect to FactSet for market data (Bonaventure flagged this, and he's right), run automated news-clipping against our themes, slot into the CRM once we pick one, drive campaign-automation, feed event registrations and lead scoring. We *will* build toward all of that. But the wrong move would be to wait until everything is plumbed before you start using it.

Starting small does three useful things at once:

1. **You get value immediately**, against today's real blockers — the SG and GB launches happening this week and next, the ICP and Persona work that's been in your head, the positioning conversations.
2. **We learn what you actually want it to do** before we over-engineer. Three weeks of you using a simple version teaches us more about what to build than three weeks of me speculating about your workflow.
3. **The brain learns about Janus Marketing as you feed it.** By the time the CRM is plumbed in, the brain already knows your ICP, your Personas, your themes, your country plans. The CRM data slots into context that's already understood, not into a blank.

Critically: **we don't need the CRM to get rolling.** The CRM is the highest-velocity signal channel once it lands, but everything in the first few weeks is CRM-independent.

## The four stages

**Stage 1 — this week and next.** You and I get you operational. You start authoring the Marketing-specific reference docs the brain needs to do anything useful. I get you the tools (Cowork, Obsidian, the Web Clipper). We backfill what already exists — your Fireflies meetings since you joined, Notion docs from you and Bonaventure worth ingesting.

**Stage 2 — weeks 3–4.** Real synthesis starts showing up. The brain produces its first POV draft from accumulating signals. We refine based on what's working and what isn't, and start collecting your wishlist for what comes next.

**Stage 3 — weeks 5–8.** CRM lands; richer signals come online (inbound, leads, opportunity history). We discuss what views you want pinned. We start scoping the custom dashboard / app — but only because by then you'll *know* what you want it to do, not be guessing.

**Stage 4 — beyond.** Automated news-clipping against your topic taxonomy, the FactSet integration Bonaventure flagged, deeper agentic workflows, campaign-automation tie-ins, the email-marketing and CMS connections. These build out over months, prioritised by what you've actually found yourself wishing for during Stages 1–3.

## What I need from you in Stage 1

Five reference documents to draft, in priority order. I've already created skeletons for all five — section headings, prompts, open questions to react to. You fill them in; you're not starting from a blank page.

1. **Country plan — Singapore.** Time-critical; the launch window is open now. Top accounts, channel strategy, local nuances (MAS, ESG, business culture), 90-day calendar.
2. **Country plan — UK.** Same shape, GB-specific. Window opens this week.
3. **Ideal Customer Profile.** The companies we want to win — characteristics, vertical fits, disqualifiers. You'd started this on May 8.
4. **Target Personas.** The roles inside ICP companies — CFO, COO, Head of Strategy, Head of Asset Management, possibly Head of Sustainability. What they care about, how they buy, what messaging resonates.
5. **Topic taxonomy.** The themes we track externally — AI in real estate / built environment / real assets, asset management, banking, PE/credit, sustainability, marketing-industry trends. Sub-topics under each, why each matters to us.

These don't need to be polished. They need to be **yours**. I'd rather see five rough drafts this week than two beautifully-finished ones in three weeks — the brain works better with imperfect drafts it can react to than with blanks. We'll iterate together.

## What I'll do in Stage 1

- Get you set up on **Cowork** with the Marketing vault mounted — your primary interface to the brain. We'll spend 30–60 minutes walking through it together.
- Install **Obsidian** and the **Web Clipper** on your machine.
- **Backfill your Fireflies** transcripts from when you joined (mid-April onwards) — anything marketing-relevant gets ingested.
- **One-time ingest** of relevant Notion docs from you and Bonaventure (mission, multi-year strategy, anything worth capturing).
- Make sure what you produce **flows toward Bonaventure** and toward the other departments' brains as those come online — you don't need to do anything special; it happens through the shared-folder structure.
- Keep the underlying schema tight as we go. Your job is to feed and direct the brain, not to wrangle file structures.

## The tools you'll use

- **Claude Cowork** — your primary interface. Think of it as you talking to the brain. You'll ask it to ingest things, query things, synthesize things, draft things. Setup is just connecting your existing Claude account to the Marketing vault.
- **Obsidian** — your browsing and authoring surface. It's where you'll see the knowledge graph build up over time, navigate between related pages, and write directly into the brain when you want to do that yourself rather than going through Claude. You mentioned on May 8 that you'd heard of Obsidian (Jehad's setup) — this is your version of that.
- **Web Clipper** (Obsidian extension) — when you see an article worth keeping (analyst piece, competitor move, regulatory shift, thought-leadership angle), one click puts it in the brain's inbox. From there the system processes it: extracts the key points, tags it against your themes, links it to anything it relates to. This is your most repeatable signal source right now, and it activates immediately.
- **Custom dashboard / app** — *later.* Once you've used Cowork for a few weeks and know what views you want to come back to, we'll scope a tailored UI. Building it before then would be guessing at your workflow.

## Our kickoff walkthrough (45–60 minutes)

When we sit down, I'll show you:

1. **The Marketing vault structure** — what's there and why it's organised that way. Kept light; you don't need to internalise the schema, just enough to find things.
2. **How Cowork works against the vault** — a few example interactions (ingest an article, ask a question, get a synthesis).
3. **Web Clipper in action** — clip one article, watch what happens to it.
4. **The five skeleton reference docs** — where they live, what they need, how to write into them.
5. **The shared subfolder between the AIO and Marketing brains** — how our two functions stay connected, so when I do something on the tool-evaluation side that affects you, you see it, and vice versa.

We'll go from "Andrew's never opened the vault" to "Andrew can clip an article, ask the brain a question, and edit a reference doc" in that session.

## Things worth thinking about beforehand

Not homework; just sitting with these ahead of the walkthrough will make it land faster.

- For **Singapore**: what would Marketing's first 90 days there look like if everything went right?
- For **UK**: same question. Is the answer different in any non-obvious way?
- **Personas**: which one carries the most weight for the verticals we're targeting? Which one do you want to write first?
- **Themes**: any I'm missing from the May 8 list? Any I have that you'd cut?
- **Most useful single thing**: what's the single most useful thing the brain could do for you in three weeks?

That last one is the one I'm most interested in. Your answer shapes Stage 2.

---

Let me know what time works to walk through it. A few windows that work for you this week and I'll book it.

— Michael

---

## Notes on this artifact (for the wiki, not Andrew)

- **Type framing.** Filed as `brief` since the closer-fit type (`plan` or `communication`) doesn't exist in the locked vocab. Loosely interpreted — this isn't a strategic-aha brief per CLAUDE.md §6.
- **Future generalisation.** When HR / ISO / Finance instances spin up, their curators will need an equivalent onboarding pass. Generalise this into `processes/department-instance-curator-onboarding.md` after Andrew's onboarding completes and we know what worked / didn't.
- **Why filed in the mesh subfolder.** This is pairing-level content — AIO running an onboarding for the Marketing curator. Belongs here rather than in either single-side vault.
- **Iteration hooks.** Stage-2 review and Stage-3 app-scoping are deliberately deferred decision points. Their content will accumulate as Andrew's first weeks produce real usage data.

## Post-walkthrough revisions (2026-05-12)

Andrew and Michael walked through this plan together on 12 May 2026 (3pm session — see [[2026-05-12-andrew-onboarding-review]] for the full transcript). The body above is preserved as the *pre-read* artefact that was sent to Andrew. The revisions that came out of the session are captured here as an addendum, and are reflected in the live [[marketing-prime-radiant|Marketing PR project hub]] going forward.

### Output ordering reversed

The original "what we're building" prose listed POVs / briefs / campaign plans / positioning / white-paper drafts in that approximate order. Andrew explicitly requested the reverse — plans / campaigns first, briefs / positioning second, POVs / white papers / assets third — to keep the scope from being read as a white-paper-generation engine. See [[2026-05-12-marketing-pr-outputs-reordered]] for the decision and reasoning.

### FactSet de-emphasised

The "Stage 2 / Stage 4" mentions of FactSet integration (Bonaventure-flagged) are now scoped under a generic "news sources / information gathering" category. Andrew's pushback on the call: *"if you looked at this, you think FactSet — we're going to define everything around FactSet... that's not a poor strategy."* LinkedIn is now the primary intelligence channel; Twitter secondary; FactSet alongside other news sources.

### Three pillars added as the themes spine

The "Topic taxonomy" reference doc in Stage 1 should be structured around the [[ai-native-janus-positioning|three-pillar messaging spine]] as Andrew articulated it: **Society** (sustainability / ESG) → **Business** (capital / AI as growth engine) → **Individual** (workers / upskilling / Uber for engineers). Every theme rolls up to one pillar; pillars dictate website navigation when the site architecture lands.

### Personas narrowed to GPs and LPs for Singapore launch

For the 8th–9th July Singapore luncheon target, the primary Personas are **General Partners** and **Limited Partners** in the asset-management world — not the broader CFO / COO / Sustainability-lead list in the pre-read. Wider Persona work continues but the launch-campaign focus is GP/LP-first.

### Singapore launch campaign committed

- Single landing page on `janusd.com` (or `janusd-sg.com` — depends on the [[2026-05-12-website-architecture-one-site-vs-country-sites|website architecture question]]) — white-paper headlines + registration form + data-privacy. Needed in *days*.
- Lead capture → Google Sheets interim → invite list for the July luncheon → nurture sequence.
- Campaign mix: paid + organic social + PR (Business Times tried) + landing-page lead funnel.
- Target volume by July: tens to low hundreds of qualified leads; signal-quality over scale.

### CRM timing committed (HubSpot direction)

- HubSpot decision target: ~2–3 weeks (~end May / first week June).
- Implementation: ~3 more weeks for terms + setup.
- CRM remains *not in critical path* — Google Sheets is the interim system of record. See [[crm-evaluation-and-selection]] for full framing.

### AI-washing campaign hook adopted

Andrew committed to a first social post today (12 May) on the "name three things that make it AI" frame, originating from a real-world "AI Powered Living" property-development example Michael spotted on his way to the meeting. The pattern is captured as a generalisable content discipline at [[2026-05-12-anti-ai-washing-as-content-discipline]]. Series potential — a recurring Janus-tone content thread.

### Website architecture is an open question

One Janus site with country sub-paths (Andrew + Michael position) vs standalone country sites (anticipated Bonaventure position). See [[2026-05-12-website-architecture-one-site-vs-country-sites]]. Resolution needed before the Singapore landing-page work commits to a URL pattern.

### Tooling install scheduled

Cowork project setup + Obsidian + Web Clipper + Fireflies connector reset on Andrew's Mac, Thursday–Friday this week (Bonaventure on holiday from Wednesday — lower-traffic window). Andrew's existing Fireflies meetings will be backfilled as the first-content seed for the Marketing instance.

### Reference docs commitment

Andrew committed to delivering working drafts of ICP, Target Personas, and Topic Taxonomy in **~1 week**. Working skeletons exist; needs cross-tally with Bonaventure's separately-developed repository — Andrew has been working independently of Bonaventure's parallel work.
