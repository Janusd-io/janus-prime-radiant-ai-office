---
title: "Google I/O: Agents, Agents, Agents"
source: "https://every.to/context-window/google-i-o-agents-agents-agents"
author:
  - "[[Jack Cheng]]"
published: 2026-05-20
created: 2026-05-22
description: "Plus: Why Anthropic just acquired a startup that makes developer tools for a reported $300 million, and a mini-Vibe Check on Figma's agent"
tags:
  - "clippings"
---
Google I/O dominated the week, and the message from Mountain View was unsubtle: Agents are now the product, with Gemini 3.5 Flash powering a redesigned search and a new fleet of always-on assistants. One layer down, Anthropic paid a reported $300 million for Stainless—so we’re re-upping our *[AI & I](https://every.to/podcast)* episode with CEO **Alex Rattray**, who laid out the design principles for making software legible to agents months before the deal happened. Plus: We did a mini- [Vibe Check](https://every.to/vibe-check) of Figma’s new in-canvas agent to see whether it solves the blank-page problem.— *[Kate Lee](https://every.to/@kate_1767)*

*Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.*

---

### Spotlight

#### Alex Rattray, Stainless CEO and MCP whisperer

Flashy frontier [model releases](https://every.to/vibe-check/gpt-5-5) suck up most of the oxygen in the AI ecosystem. But without reliable ways for AI agents to access these models, their capabilities are limited. This plumbing may be easy to overlook, but it’s an indispensable component of an agent-native internet.

You don’t have to take our word for it. On Monday, Anthropic announced it has [acquired Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless), a software platform for high-quality APIs, to extend Claude’s ability to connect to data and tools. (While terms weren’t disclosed, The Information put the purchase price at north of [$300 million](https://www.theinformation.com/articles/anthropic-talks-buy-developer-tools-startup-used-openai-google?rc=ekymys).) Former Stainless customers include OpenAI and Google, meaning Anthropic has acquired a developer tooling company used by its top rivals.

In October, Stainless CEO and founder **[Alex Rattray](https://www.linkedin.com/in/alexrattray/)** joined **[Dan Shipper](https://every.to/@danshipper)** on *[AI & I](https://every.to/podcast)* to talk about why teaching models to use software is so tricky, and what [design principles](https://every.to/podcast/he-s-building-the-plumbing-for-ai-to-use-the-internet) make model context protocol (MCP) servers more intuitive for LLMs. (TL;DR: Keep the number of tools an agent can access small, give the tools precise names, and aim to generate tightly defined outputs.) In the episode, Alex goes deep on Stainless’s approach to making it easier for AI agents to use the internet—hard-won insights that, as it turns out, can lead to a big-sticker acquisition from a top model company. \[Disclosure: Dan is a small investor in Stainless.\]

Read Anthropic’s [announcement](https://www.anthropic.com/news/anthropic-acquires-stainless) about its decision to buy Stainless and then watch Rattray’s *AI & I* episode [on X](https://x.com/danshipper/status/2057122805657821240) or [YouTube](https://youtu.be/diXNk8ibJVk), or listen on [Spotify](https://open.spotify.com/episode/2xKWTcJkEzJLPxChgXmHvg?si=XXbLCfDURE6AJmJh60b86g) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/inside-stainless-the-developer-tools-startup/id1719789201?i=1000768755708) (or read the episode [transcript](https://every.to/podcast/inside-stainless-the-developer-tools-startup-anthropic-just-bought-for-300-million)).— *[Laura Entis](https://every.to/@laura_27bbaf_1)*

[
![](https://www.youtube.com/watch?v=diXNk8ibJVk)
](https://youtu.be/diXNk8ibJVk)

---

[![Uploaded image](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/advertisements/1176/optimized_7bbc38da-3a88-490b-9f37-90084412f9d4.png)](https://b.link/every-n2)

#### Get your databases moving faster

Most databases require manual setup. Don’t limit your experiments to fit your infrastructure budget. Try Ghost. It’s Postgres designed for agents that need to move fast. Spin up as many databases as you need for parallel experiments, fork each test run, and delete what doesn’t work. Your agent handles authentication, schema introspection, queries, the entire lifecycle, via native MCP integration. Also works natively with Claude Code and co. Free tier: unlimited databases, 1TB storage.

[Get started](https://b.link/every-n2?source=post_button)

## Signal

#### Google goes all-in on agents

We’re hurtling toward an AI landscape divided into [two categories](https://every.to/context-window/the-dawn-of-codex-native-apps) of agents: those you collaborate with, and those you delegate to. Google’s new releases from its flagship I/O developer conference, happening this week in San Francisco, break neatly along that line.

The headline announcement is Gemini 3.5 Flash, Google’s just-announced frontier model it says operates four times faster and at half the cost of comparable LLMs. It’s the engine powering most of the agentic features below.

##### In the ‘collaborate with’ bucket

**AI Mode and the new search box:** Google is giving search its biggest interface change in 25 years. In addition to expanding the search box to accommodate longer, more conversational questions and terms from users, AI Mode, which Google introduced at [last year’s I/O conference](https://every.to/context-window/google-s-ai-vision-make-tech-human-again), is becoming the default search mode. With the 2026 updates, you can now build custom mini-apps, such as a personalized fitness tracker, or interactive visualizations directly within search itself.

**Antigravity 2.0**: Google’s agentic development platform is becoming a desktop app for managing teams of agents, with a new command line interface tool and an SDK for custom workflows. You orchestrate, and the agents code, design, or do whatever else you want them to accomplish.

##### In the ‘delegate to’ bucket

**Gemini Spark**: Google is pitching Spark as a 24/7 personal agent that lives in the cloud, works when your devices are off, and can operate across Gmail, Docs, Workspace, Chrome, and eventually, third-party tools through MCP.“You can just throw tasks over your shoulder,” **Josh Woodward**, vice president of Google Labs, Gemini, and AI Studio said in the keynote. “Spark will catch them and then run with them.”

**Daily Brief**: An out-of-the-box agent in the updated Gemini app that works overnight, scanning your inbox, calendar, and tasks so it can hand you a prioritized digest when you wake up in the morning.

**Universal Cart:** Google’s new shopping cart works across merchants as part of the Universal Commerce Protocol, which it co-developed with Amazon, Meta, Microsoft, and others. Whenever you add something in your cart, it automatically monitors the internet for information on the product, including price drops, price history, and whether something is back in stock. It also analyzes the full contents of your cart to proactively flag potential issues, like if you’re building a PC and the processor and motherboard you’ve selected are incompatible.

---

## Inside Google I/O

#### Anyone can cook

Gemini 3.5 Flash, announced in Tuesday’s opening keynote, seems like a meaningful step toward a fast and cheap model that can reliably handle the personal, everyday tasks that most people are looking for help with.

When is a model good *enough*? That was the question I asked myself heading back to my hotel after the first day of Google I/O. I often send agents on multi-hour coding missions, and need to pull together data from multiple accounts and channels to coordinate my workday. In these cases, each new model release seems to work better than the last. So I eagerly hop from one to another.

On the other hand, for simple, personal tasks like household briefings, tracking my journaling and meditation habits, and light web development, I am loyal to [Sonnet 4.6](https://every.to/vibe-check/vibe-check-anthropic-just-made-opus-cheaper-without-calling-it-that) —although sometimes I have to tell it to ask Opus or [GPT-5.5](https://every.to/vibe-check/gpt-5-5) for help.

But once a model like Sonnet grew smart enough to handle anything personal I might throw at it, I wondered, what else might I want from it?

I’d want it to be blazingly fast, so that I wasn’t waiting for responses when I was working with it in real-time. I’d also want it to cost next to nothing.

Gemini 3.5 Flash may offer exactly that.

[![Gemini 3.5 Flash is in a quadrant of its own. (Photo courtesy of Jack Cheng.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_9e2801e9-d98c-4cc6-89a9-3c206c37d4e3.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_9e2801e9-d98c-4cc6-89a9-3c206c37d4e3.png)

Gemini 3.5 Flash is in a quadrant of its own. (Photo courtesy of Jack Cheng.)

If the benchmarks are to be believed, then Gemini 3.5 Flash delivers [Opus 4.7](https://every.to/vibe-check/opus-4-7) -level intelligence at four times the speed. Accurate, near-instantaneous responses let Google believably send users from search results pages into its “AI Mode” without them realizing that they’ve entered a new state. A chat interface, after all, is not that far off from a search box. But for that chat interface to still feel like Google search, it has to be just as snappy as traditional search.

It remains to be seen how users will take to the deeper AI mode integration once the update rolls out globally, as it’s beginning to do this week. But Google says 2.5 billion people already use the “AI Overviews” at the top of results pages, and these summaries will now let you ask questions in response. Every search becomes the start of a conversation with an AI agent that can generate text and images, spin up research agents, code up interactive widgets and mini-apps, and more.

This could lead many more people to experience their first “aha moment” with AI. Google’s core competencies around speed and scale really come through in the Gemini 3.5 Flash release.

The context it already has on users though their Gmail, Google Calendar, and Google Docs accounts removes one of the main headaches in setting up AI agents. Google is perhaps one of two companies in the world—along with Apple (which will *also* be using Gemini to power its own coming AI integration)—with moats of this size. Pretty soon, billions of people could be newly using agentic AI to cook up tools and workflows that make their lives easier or more enjoyable in some small way.

Oddly enough, Google’s announcements at I/O so far don’t affect those of us riding the edge of the AI wave. Reception to the day’s announcements in Every’s Slack was tepid. But I don’t think Google’s keynotes were speaking to people tinkering with [OpenClaw](https://every.to/guides/claw-school) or using and building [Codex-native apps](https://every.to/context-window/the-dawn-of-codex-native-apps) to do their email and learn piano.

To me, the significance of Gemini 3.5 Flash and Google’s AI search announcement, amid a sea of other announcements, was underscored by one of the last slides of one of the last developer sessions of the first day. It read:

“We are the first generation of builders creating tools for a world where anyone can build anything.”— *[Jack Cheng](https://every.to/@jackcheng)*

---

## Log on

We host [camps and workshops](https://every.to/events) on topics like [compound engineering](http://youtube.com/watch?v=7YUBxMTF1Tc&time_continue=3&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fevery.to%2F) and [writing with AI](https://www.youtube.com/watch?v=oEvjbPwGwnc) to share what we’ve learned from training teams at companies like the *[New York Times](https://every.to/on-every/the-next-chapter-of-every-consulting)* [and leading hedge funds](https://every.to/on-every/the-next-chapter-of-every-consulting), and by using and experimenting with AI every day ourselves.

##### Upcoming event

- [Executive AI Sessions](https://every.to/events/executive-AI-sessions): On June 2, head of consulting [Natalia Quintero](https://every.to/@natalia_2944) hosts a live webinar introducing [Every Consulting](https://every.to/consulting) ’s new offering for leadership teams navigating AI adoption—built on the playbook we’ve been running with executive clients for months. [Learn more and register](https://every.to/events/executive-AI-sessions).

##### In New York City

- [Every 🤝 IRL](https://luma.com/2o67t7ob): Join us at the Every brownstone in Brooklyn on June 3 during New York Tech Week for a subscriber-only meetup celebrating the Every community over drinks and conversation. [Learn more and RSVP](https://luma.com/2o67t7ob).

---

## Mini-Vibe Check: Figma agent

### Figma makes the blank canvas less blank

In March 2026, **Figma** [opened its canvas](https://www.figma.com/blog/the-figma-canvas-is-now-open-to-agents/) to outside AI agents. The update let coding tools like [Claude Code](https://every.to/vibe-check/vibe-check-claude-cowork-is-claude-code-for-the-rest-of-us), [Cursor](https://every.to/vibe-check/cursor), and [Codex](https://every.to/vibe-check/vibe-check-codex-openai-s-new-coding-agent) connect to Figma through MCP (model context protocol, the open standard that lets AI agents talk to external software) and write designs directly into a Figma file.

Today, Figma releases [its own agent](https://www.figma.com/blog/the-figma-agent-is-here/) that lives inside Figma. It edits your canvas directly—switching component states (the variants of a design element, like when a button looks one way when hovered and another when clicked), restyling layouts, and generating new screens. It’s built on a mix of Google’s [Gemini Flash](https://every.to/vibe-check/vibe-check-gemini-2-5-pro-and-gemini-2-5-flash), Anthropic’s [Claude Sonnet](https://every.to/vibe-check/vibe-check-claude-sonnet-4-5), and Figma’s own fine-tuned models. Figma users no longer have to leave their canvas, or hand the work off to an engineer, to get an AI-generated first draft.

Every got access a day before the announcement. Head of marketing **Douglas Brundage**, senior designer **[Daniel Rodrigues](https://every.to/@daniel_5fbd21_1)**, and creative designer **Benjamin Ose** spent a day testing it. Here’s what they found.

### What works

When the prompt is specific, the agent produces solid early explorations, preserves copy well, and gives designers something to work with instead of a blank canvas.

As Daniel put it, “There’s really no excuse to start from scratch anymore.”

[![The agent can explore visual directions quickly, though fidelity and rendering still need designer review. (Image courtesy of Douglas Brundage.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_6b997d11-7467-446b-b47e-e4f203ba324d.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_6b997d11-7467-446b-b47e-e4f203ba324d.png)

The agent can explore visual directions quickly, though fidelity and rendering still need designer review. (Image courtesy of Douglas Brundage.)

It’s also good for quickly sketching out product ideas. Benjamin used it to mock up a SaaS dashboard for mining X mentions for testimonials and came away with viable early explorations. Here was his initial prompt:

> Design a SaaS dashboard that listens for your X handle mentions, uses AI to extract testimonials (positive shouts, reviews, endorsements), and stores them in a searchable vault. One-click export to websites as embeds, widgets, or APIs—think Grammarly’s clean proofing flow meets Stripe’s embeddable elements. Freemium entry: Basic capture free, premium for AI curation and analytics.

[![Benjamin used the agent to come up with a testimonial-mining SaaS dashboard, producing a structured early exploration ready for cleanup and iteration. (Image courtesy of Benjamin Ose.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_71af90ec-f87e-4333-961c-b33e9aa3c1af.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4269/optimized_71af90ec-f87e-4333-961c-b33e9aa3c1af.png)

Benjamin used the agent to come up with a testimonial-mining SaaS dashboard, producing a structured early exploration ready for cleanup and iteration. (Image courtesy of Benjamin Ose.)

### What needs work

The agent is less useful for detailed work. Tabs rendered improperly, buttons doubled up, components drifted out of alignment, and some outputs came back weirdly low-res. It can lay down the structure, but the designer still has to go in and fix the details. There’s no ability to attach an image or a link as a visual reference for the agent. Right now the agent relies on a prompt-writing skill or an existing Figma frame.

Benjamin also said the agent would be much more useful if it worked from an existing design system, instead of inventing from scratch—pulling in the components, colors, spacing, and styles a team already uses in Figma. Ideally, it could also draw on the reference tools designers use, like [Mobbin](https://mobbin.com/).

### Our verdict

Figma’s agent isn’t a fully trustworthy design copilot yet, but it solves the blank-page problem for early design work. Its job is to get designers from zero to first pass, so their energy can shift to judgment and polish.

It delivers on that promise for exploration, layout starts, and iteration. It still needs better fidelity, stronger detail handling, and richer reference inputs before it can feel dependable in production.— *[Katie Parrott](https://every.to/@katie.parrott12)*

---

***[Jack Cheng](https://every.to/@jackcheng)*** *is a senior editor at Every. He is a creative generalist and the author of two novels for young readers. You can follow him on [X](https://x.com/jackcheng) or read his occasional [Sunday](https://jackcheng.com/sunday) newsletter.*

*To read more essays like this, subscribe to [Every](https://every.to/subscribe), and follow us on X at [@every](http://twitter.com/every) and on [LinkedIn](https://www.linkedin.com/company/everyinc/).*

*We [build AI tools](https://every.to/studio) for readers like you. Write brilliantly with* ***[Spiral](https://writewithspiral.com/)****. Organize files automatically with* ***[Sparkle](https://makeitsparkle.co/?utm_source=everyfooter)****. Deliver yourself from email with* ***[Cora](https://cora.computer/)****. Dictate effortlessly with* ***[Monologue](https://monologue.to/)****. Collaborate with agents on documents with* ***[Proof](https://www.proofeditor.ai/)****.*

*For sponsorship opportunities, reach out to sponsorships@every.to.*