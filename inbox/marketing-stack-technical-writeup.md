# Marketing stack: technical writeup

**For:** Jehad
**From:** Michael, AI Office
**Status:** Working document — captures the full reasoning behind the stack recommendation

---

## Why this document exists

I had a long Claude thread evaluating the marketing technology stack, which surfaced an architectural question we hadn't run into before: how do we build and operate a multi-tool stack with the team we actually have? The answer turned out to depend on three properties of the tools themselves — composability, agent operability, and reversibility — that aren't in our existing AI Tool Evaluation framework. This writeup captures the technical reasoning so you have the same context I do before the Andrew meeting.

I'm assuming you've read the briefing doc and have a working understanding of the recommendation. This document goes deeper on the technical details, the alternatives we rejected, and the reasoning chains behind each choice.

---

## The strategic shift that enables this approach

Two specific things have moved structurally in the last 18 months that change what a small team can run:

**Model Context Protocol (MCP).** Anthropic open-sourced this in late 2024 as a vendor-neutral protocol for AI agents to read and write into external systems. By mid-2026, native MCP servers ship from Salesforce (60+ tools), HubSpot, Attio, Vercel, Cloudflare, Sanity, Cosmic, Contentful, Adobe (Document Authoring MCP from Summit 2026), Notion, Linear, Stripe, Monday.com, and several hundred others. It's effectively become USB-C for AI tooling — Claude Code can operate any of these tools without per-vendor integration work.

**Mature agentic coding tools, particularly Claude Code.** Vercel reports that 30% of all deployments on their platform are now initiated by coding agents, with Claude Code accounting for 75% of those — a tenfold increase in six months. Your hour-long refactor of janusd.com from static HTML to TypeScript/React is the local data point.

The two together produce what Anthropic Claude called the "agent triad" — CLI + API + MCP. A tool that ships all three is operable by a single engineer with Claude Code at near-zero marginal ops cost. A tool that ships only a UI and a partial API still requires dedicated human ops time. The breakeven point at which a multi-tool stack becomes manageable for a lean team has shifted dramatically, but only for tools selected on this basis.

---

## The Stack Composition Framework (three lenses)

This is the new evaluation layer we should add to the existing AI Tool Evaluation framework, as a pre-filter before G1. For any tool we consider:

### 1. Composability

**The question:** What's the data-model contract between this tool and the two or three other tools that touch it? Does its data model map cleanly to adjacent tools, or does it require a custom sync layer?

**Strong signals:** Standard primitives (contact/company/deal as flat records), clean export formats, documented integration patterns with major adjacent categories, REST-first API design.

**Weak signals:** Proprietary data structures, custom objects required for basic use, integration only via paid marketplace connectors, UI-first information architecture.

### 2. Agent operability

**The question:** Can a lean team operate this tool primarily through agents like Claude Code, or does it require dedicated human ops time?

**Agent triad check:** Real CLI + robust API + native MCP server. Plus: is the data model expressible in code (schema-as-code), or only in the UI? Is there a documented Skills pattern that teaches Claude Code its conventions?

**Strong signals:** Official MCP server with broad tool coverage, mature CLI covering most operations (not just deployment), public API as the primary interface, TypeScript/JSON schema definitions, documented Skills pattern.

**Weak signals:** UI-first product where API is an afterthought, narrow CLI, community-only MCP server with limited tool coverage, schema only definable through the UI.

### 3. Reversibility

**The question:** If this tool needs to be replaced in 18 months, how hard is that migration?

This is the discipline that prevents the agentic-lean strategy from regressing over time. The strategy works because tools are replaceable; it stops working as soon as we accumulate state that only one vendor can read.

**Strong signals:** Standard data export formats (JSON, CSV, Parquet, SQL dumps), schema lives in our code repository, business logic implementable in standard languages (TypeScript, Python).

**Weak signals:** Business logic locked into proprietary languages (Salesforce Apex, HubSpot HubL, Adobe HTL), export requires special tooling or vendor services, critical workflows depend on platform-specific extensions.

**Scoring:** 3/3 = preferred default. 2/3 = viable with documented trade-off. 1/3 = generally reject. 0/3 = reject.

---

## CMS analysis: why Cosmic over the alternatives

We evaluated six headless CMSs against the framework:

### Cosmic (3/3) — recommended

- **CLI:** Full-stack. Handles content management AND deployment to Vercel with one command. Manages repos, branches, PRs, domains, DNS.
- **API:** REST-first by design with TypeScript SDK. MongoDB-style query operators (industry-standard, no proprietary language).
- **MCP:** Official server (`npx @cosmicjs/mcp`) with 17–18 tools across Object Types, Objects, Media, and Search categories. Hosted on Cosmic's infrastructure.
- **Agent Skills:** Documented and published. Installs via `npx claude-skill add cosmic-headless-cms`. Teaches Claude Code SDK patterns, content modeling, media management, and query patterns persistently — same primitive as our standup/ai-registry/ai-tool-evaluation skills.
- **Multi-region:** 400+ locales supported via `locale=` query parameter; also supports 5 buckets on the Business plan ($499/mo) so we can have global + per-region buckets.
- **Reversibility:** Content is plain JSON, exportable via API. No proprietary query language to lock us in.

### Sanity (2.5/3) — strong runner-up

- Excellent CLI with Claude Code auto-config (`sanity` CLI detects Claude Code and configures MCP).
- Hosted MCP at `mcp.sanity.io` with Content Agent, Agent Actions API, Compute, Blueprints.
- Highest G2 rating in the category (4.7/5 from 900+ reviews).
- Content Lake architecture stores everything as structured JSON.
- **Loses 0.5 points on reversibility because of GROQ.** GROQ (Graph-Relational Object Queries) is Sanity's homegrown query language. It's genuinely well-designed — more concise than GraphQL for nested content, more expressive than REST for filtering — but it's proprietary. If we accumulate 50–100 GROQ queries across the Next.js codebase over a year, migrating to Cosmic or Contentful means rewriting all of them. The content itself stays portable (JSON), but the query logic is Sanity-specific.

Example GROQ query:
```groq
*[_type == "article" && publishedAt > "2026-01-01"] {
  title,
  slug,
  "author": author->name,
  "categories": categories[]->title
} | order(publishedAt desc)
```

Same intent in Cosmic's MongoDB-operator syntax:
```js
{
  type: "article",
  publishedAt: { "$gt": "2026-01-01" }
}
```

Cosmic's syntax is industry-standard (MongoDB operators are used everywhere); GROQ is Sanity-only. Hence the half-point ding.

### Contentful (2/3) — enterprise default we're not picking

Mature CLI, hosted MCP server at `mcp.contentful.com` (beta), deep i18n. Used by IKEA, Spotify. **Doesn't fit because:**
- $300–$2,000+/mo with hard limits on content types (48 max on Basic, 150 max on Premium) and locales (3 on Basic).
- One documented case of an org unable to add a second report type at 149/150 content types.
- Adding locales multiplies costs aggressively — bad fit for our multi-ccTLD plan.

### Payload (2.5/3) — interesting if we ever go self-hosted

TypeScript-native, schema-as-code (content types are TypeScript files in your repo), can install inside Next.js directly with no separate CMS server. Cut dependencies from 88 to 27 in v3. Best reversibility story in the category because the schema IS the codebase. MCP is community-maintained rather than official. Worth keeping on the radar for when we want full data ownership.

### Adobe AEM (1.5/3) — wrong tier

Got the new Document Authoring MCP server at Summit 2026, but content fragments + HTL templating accumulate vendor-specific state. Enterprise DXP pricing (six-figure annual contracts). Not for our stage.

### HubSpot CMS Hub (1.5/3) — same structural issue as AEM

HubL templating is HubSpot-proprietary; HubDB is HubSpot-only. MCP coverage is read-heavy with limited write tools. Decent CLI. Strong composability *only when bundled with HubSpot CRM and Marketing Hub*, weak outside the HubSpot ecosystem.

---

## CRM analysis: why Attio

All four contenders (Attio, HubSpot, Salesforce, Monday) ship official MCP servers in 2026, so the floor is high across the board. The framework still produces a clear winner.

### Attio (3/3) — recommended

- **Agent-native by design:** "An MCP server cannot be designed like a public API, because context windows and token costs force different primitives" — Attio's positioning statement. They designed the data model and MCP surface together rather than retrofitting.
- **Data model:** Relationship-graph with standard objects (Person, Company, Deal). MongoDB-style queries.
- **Pricing:** Free tier with real features. Plus at $29–36/user/month. Pro at $69–86/user/month. Published on the website, no "contact sales" gating.
- **Trade-offs:** Smaller integration ecosystem than HubSpot/Salesforce. Reporting is shallower than the giants.

### Salesforce (2/3) — viable with the Apex constraint

Deepest MCP integration: 60+ tools, dynamic toolset loading, SOQL queries, Apex test execution. Mature CLI. **Loses on reversibility because of Apex.** Any meaningful customization accumulates non-portable Java-derived code. If we adopt Salesforce with the explicit constraint of writing zero Apex, it scores higher; once we cross that line, we're locked in for years.

### HubSpot (2/3) — bundling play, not a CRM play

136 MCP tools, but the official server is read-heavy — write operations require community servers with low adoption. Strong only if we're going all-in on the HubSpot ecosystem (CRM + Marketing Hub + CMS Hub). Standalone, it's weaker than Attio at our stage.

### Monday.com (already in our stack but not as primary CRM)

Has an official MCP server (390+ GitHub stars). Data model is board-centric rather than relationship-centric — works fine for the AI Registry and project tracking we already use it for, but it's not a CRM in the way Attio or Salesforce are. Keep Monday for what it's already doing; don't promote it to system-of-record for customer relationships.

---

## Mail campaign analysis: Resend wins for our stage

### Resend (already in place)

Developer-first transactional email. Already integrated for the Singapore campaign. Strong API and CLI. Resend now also has Broadcasts for marketing campaigns — meaning we may not need to add Mailchimp at all. Free tier is generous; we should be on the paid tier for production support regardless.

### Mailchimp (probably unnecessary)

If we already have Resend doing transactional reliably, the only reason to add Mailchimp is for the campaign UI that marketing teams are used to. Worth revisiting after Singapore launches to see if Andrew prefers the dedicated marketing tool or is happy operating through Resend Broadcasts.

### HubSpot Marketing Hub (declined)

Would only make sense if we were bundling with HubSpot CRM. Since we're going with Attio, this falls away.

### Klaviyo (declined)

E-commerce-focused. Overkill for B2B corporate marketing.

---

## Hosting & edge: Vercel + Cloudflare

This is where your pushback lives, so I want to address it properly.

### Your concern on Vercel

You've experienced reliability issues on Vercel's free tier and data-extraction friction on migration ("a month or two to fetch your data"). Both are real.

**On reliability:** Free-tier Vercel and paid (Pro/Enterprise) Vercel are operationally different products. Free tier shares resources aggressively; Pro at $20/user/month gives you dedicated edge functions, higher build minutes, better SLAs, and priority support. For janusd.com production traffic we'd be on Pro from day one. The 30%-of-deployments-from-agents statistic is Pro/Enterprise traffic — they're not getting that volume on free-tier hobby projects.

**On data lock-in:** Vercel hosts code, not data. Our code is in GitHub; that's our source of truth, not Vercel's. The "month or two to migrate" friction usually applies to teams using Vercel KV, Vercel Postgres, or Vercel Blob storage as primary data stores — i.e., letting Vercel be both runtime and database. We're explicitly *not* doing that. Our database story is: Cosmic stores content (their data, but exportable as JSON), Attio stores CRM data (exportable as CSV/JSON), and any operational data lives in GitHub or in our own storage. If we ever need to migrate off Vercel, it's "push the Next.js app to Cloudflare Pages or AWS Amplify, repoint DNS." Days, not months.

That said, your point on reliability deserves a test before we commit. Worth running janusd.sg on Vercel Pro with monitoring (Sentry + Vercel's own metrics) for two weeks before the lunch event in July, to validate the SLA claims with real data. If it's actually flaky, fallback is Cloudflare Pages — same Next.js codebase, different edge runtime, also fully agent-operable through Wrangler CLI.

### Cloudflare

Wrangler CLI has been rebuilt for AI agents. The official Cloudflare API MCP server gives access to the entire 2,500+ endpoint API through 2 tools (`search()` and `execute()`). Cloudflare Code Mode is the most aggressive agent-operable hosting platform on the market right now.

For our use case Cloudflare handles:
- DNS for all ccTLDs (consolidate registrars under Cloudflare nameservers)
- WAF + DDoS protection
- Global CDN with regional caching
- Bot management
- Edge routing (the Singapore-IP, UK-IP geo-resolution question — more on this below)

This is IT/DevOps territory — DA already knows Cloudflare, which is a big win.

---

## Multi-region strategy: the technical detail

You raised this in the standup: "Why do we need multi-domain when I've already implemented IP-based geo-routing?" Good question. Here's the technical resolution.

### What you've built

Server-side IP geolocation in the Next.js app: when a request comes in from a Singapore IP, the app serves Singapore content under `janusd.com/sg` (or similar). When it comes from a UK IP, UK content.

### What Bonaventure wants

Local IP addresses per region. When someone in Singapore does a `dig janusd.sg`, they should see a Singapore-resolved IP. When a UK visitor hits janusd.co.uk, they should see a UK-resolved IP. This is partly about local SEO (search engines weight local IPs favorably), partly about brand presence (the site "feels" local), and partly about hreflang correctness.

### Why your current approach doesn't fully solve this

Geo-routing inside the app happens after DNS resolves. The DNS lookup will return wherever your Hostinger server lives, regardless of who's asking. A Singapore visitor sees the right *content* but resolves to a non-Singapore IP. Bonaventure's "local IP" requirement isn't met.

### How Cloudflare + Vercel solves it cleanly

Cloudflare's edge network has POPs (points of presence) in Singapore, UK, UAE, and every other major market we care about. When you point `janusd.sg` at Cloudflare nameservers, a `dig` from Singapore returns a Singapore-edge IP. A `dig` from London returns a UK-edge IP. The DNS resolution itself is geo-routed.

Then Cloudflare serves the cached content from that edge — meaning Singapore visitors get content from a Singapore-resolved IP without us managing per-region servers.

Vercel sits behind Cloudflare as the origin. One Next.js codebase, multi-domain deployment: same code serves janusd.sg, janusd.co.uk, janusd.com, with locale resolution happening either in middleware (your IP-based approach, which we keep) or via the incoming domain (which is cleaner because it doesn't depend on accurate IP geolocation databases — some users are on VPNs, some IPs are misclassified).

### Recommended pattern

1. **Single Next.js codebase** in one GitHub repo. Locale-aware middleware that resolves which content + which legal disclaimers + which CTAs based on incoming domain (preferred) or IP (fallback).
2. **One Vercel project per ccTLD** deployed from the same monorepo. Cleaner observability, per-region rollback, per-region deployment cadence. Vercel supports this natively.
3. **Cloudflare in front of all of them** providing DNS, edge cache, WAF, and the regional IP resolution Bonaventure wants.
4. **Cosmic with multi-bucket strategy.** Master bucket = global content (HQ leadership, brand-wide copy). Per-region buckets = local overrides (SG-specific case studies, UK-specific press). Cosmic's MCP and Agent SDKs explicitly support operating across multiple buckets in the same project.

### Bonaventure's demo test

When we show this to Bonaventure, the demo is: VPN to Singapore, `dig janusd.sg`, see a Singapore-resolved Cloudflare IP. That answers the "local presence" requirement without us running per-region servers.

---

## Singapore launch implementation (next 10 days)

For the actual launch we're not adding anything new. The stack is what's in place:

1. **Hosting:** Whatever's hosting the Next.js site you just built (current Hostinger setup if Vercel migration hasn't happened yet, or Vercel if migrated). Cloudflare DNS in front.
2. **Code:** Next.js codebase in GitHub. Single codebase, regional content via your existing IP-based geo-routing or domain-based middleware.
3. **Forms:** Landing page form submits to a Next.js API route that writes to a Google Sheet via the Sheets API. We agreed you'll use your own Google account (since IT permissions for the marketing service account haven't been provisioned yet) and share the sheet to Andrew. Hacky but unblocking.
4. **Email:** Resend for the auto-reply with the white paper attached.
5. **Privacy/cookie consent:** Third-party cookie management service (we'll use one of the cheap options Andrew mentioned — Cookiebot, Iubenda, or similar) inserted via script tag. Covers GDPR, PDPA, CCPA per region automatically.
6. **Pages needed:** `/singapore` landing, `/singapore/thank-you`, `/privacy`. The incoming Chief Legal Officer's privacy policy review needs to happen before paid traffic.

The four pages and one webhook should be a half-day of Claude Code work on top of what you've already built.

---

## What gets added in June (after Singapore launches)

Six-week window before the July 8/9 lunch:

- **Weeks 1–2:** Cosmic comes in. Migrate content from hand-coded Next.js pages into Cosmic. Set up the MCP server in your Claude Code config. Install the Cosmic Agent Skill. Master bucket for global content, SG bucket for Singapore overrides.
- **Weeks 2–3:** Decide on marketing email approach (Resend Broadcasts vs Mailchimp). Set up the campaign workflow for the 6-email nurture series Andrew described.
- **Weeks 3–4:** Attio CRM. Import the Google Sheet leads as seed data. Configure MCP for Claude Code so it can score, segment, and draft outreach against the CRM directly.
- **Through July:** Operational pattern is: Andrew describes campaigns in plain language → Claude Code drafts content → reviews happen in Cosmic → publishes via MCP → broadcast from Resend → leads land in Attio → Claude Code drafts personalized follow-ups.

### UK launch

After Singapore is proved out, UK becomes a clone exercise: new Cosmic bucket (or new locale if we go single-bucket), new Vercel project pointed at janusd.co.uk, Cloudflare DNS configured, new locale in the Next.js codebase. Days of work, not weeks. Same playbook for AE/UAE and every region after.

---

## Open questions and items needing your input

1. **Vercel reliability test.** Worth scheduling a 2-week monitoring window on Vercel Pro before committing fully. Sentry + Vercel metrics. If it fails, fallback is Cloudflare Pages with the same Next.js codebase.

2. **Google Sheet API permissions.** Long-term we need a marketing service account with Sheets API access; for now you're using your personal account as a workaround. Worth raising with IT (DA) so it's on the queue.

3. **Cookie management service choice.** Cookiebot, Iubenda, OneTrust, or hand-rolled. Andrew can probably pick this without us getting too involved; it's commodity tooling.

4. **The hreflang implementation.** When we go multi-region, every page needs `<link rel="alternate" hreflang="...">` tags pointing at the equivalent page on every other regional domain. This is critical for SEO and easy to get wrong. Worth dedicating a Claude Code session to once Cosmic is in place.

5. **Privacy policy review.** The CLO hasn't joined yet. We're using the working draft Andrew has for the soft Singapore launch. Need the CLO's review before paid traffic.

6. **Building/product terminology.** Your point about needing to sync with Rosa on the property management naming before the Singapore site goes wide. Worth a separate thread.

---

## Reference materials

- **The companion briefing doc** (`marketing-stack-strategy-briefing.md`) — the version for Andrew and Bonaventure, less technical, optimized for alignment.
- **The Stack Composition Framework** (`stack-composition-framework.md`) — the one-pager that captures the three lenses for inclusion in the AI Tool Evaluation framework. We should integrate this as a pre-G1 filter.
- **The original Claude thread** — has the full back-and-forth, including alternatives we evaluated and rejected. I'll share it if you want the raw context.

---

*Working document. Update as we make decisions. Last updated: May 2026.*
