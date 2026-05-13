---
title: "Hyperproductivity: The Next Stage of AI?"
source: "https://secondthoughts.ai/p/hyperproductivity?r=q09jx&triedRedirect=true"
author:
  - "[[Steve Newman]]"
published: 2025-11-20
created: 2026-05-07
description: "A glimpse at an astonishing, exhilarating, exhausting new style of work"
tags:
  - "clippings"
---
![Image](https://substackcdn.com/image/fetch/$s_!y3iz!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf312086-ea35-4dc8-b0c3-d2a8fd057e06_1232x928.webp)

Recently, I’ve been hearing of a new phenomenon: teams reportedly using agentic AI tools to “enter takeoff” – achieving astounding feats of productivity that escalate each week, with no limit in sight.

These teams have four things in common:

1. They are aggressively using AI to accelerate their work.
2. They aren’t just using off-the-shelf tools like ChatGPT or Claude Code. They’re building bespoke productivity tools customized for their personal workflows – and, of course, they’re using AI to do it.
3. Their focus has shifted from *doing* their jobs to *optimizing* their jobs. Each week, instead of delivering a new unit of work, they deliver a new improvement in productivity.
4. **Their work builds on itself: they use their AI tools to improve their AI tools, and the work they’re optimizing includes the optimization process.**

The classic scenario for AI ascending to superintelligence involves “recursive self-improvement”, where an AI builds a smarter AI, which builds an even smarter AI, and so on. These stories of teams entering takeoff are not quite that, because there is still a human in the loop, but they have a similar flavor. If the singularity ever arrives, the early stages might look just like this.

## What Aggressive Use of AI Looks Like

![](https://substackcdn.com/image/fetch/$s_!bnIs!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0e23d28-096c-4c7f-bd0c-b7e3162aa2e5_1026x444.png)

One of many businesses Liu Xiaopai is running simultaneously

Afra Wang recently published the fascinating [Story of A Beijing Vibe Coder](https://afraw.substack.com/p/story-of-a-chinese-vibe-coder). This is her account of Liu Xiaopai, a Chinese programmer who is using AI tools to crank out product after product. Working mostly on his own, he currently has “one or two dozen revenue-generating products” and reports clearing over $1,000,000/year in profit. By contrast, a typical startup requires many people to build and maintain a single product.

Liu Xiaopai isn’t just using AI tools to write code. He’s automating, as the article says, “the entire product lifecycle”. For instance, once he has an idea for a new product, he uses Claude Code [^1] to brainstorm product names and find one for which the domain name is available:

> **Afra:** Was there a specific moment when you realized Claude had fundamentally transformed your working methods?
> 
> **Liu Xiaopai:** Too many to count. Building software products for overseas markets—programming actually represents only a small fraction.
> 
> Look at any normal internet company in China: engineers comprise just 20-30%. What about the remaining 70%? They are design, product management, testing, operations, user growth—these roles require substantial human resources, and nearly all follow standardized operating procedures (SOPs).
> 
> After using AI to solve the programming component, I faced a larger challenge: how to automate all the work with standardized processes? After entering July, I spent more time with Claude Code on non-programming tasks. Here’s a simple use case that was previously impossible: I need to launch a new product, which requires naming it and registering a website domain. Let’s say I build the product Manus, with the domain [Manus.ai](http://manus.ai/). Sounds simple—but this having a product name and domain means many steps, and each step was hard to automate before. You’d brainstorm names, then manually check domain availability one by one; it’s too time-consuming. **How about using AI to generate 10,000 viable domains and instantly determine which are available for registration? Thus, determine the product name?**
> 
> I would begin by writing product requirements documentation. Then I’d list all the competitors, noting how each differs from mine and what features I want to emphasize. I write an extensive description, and then have Claude synthesize this information to auto-generate 10,000 appropriate domains and query their registration status. Then I can go to sleep. Five or six hours later, the results arrive. I automate many SOPs like this.
> 
> \[emphasis added\]

Liu Xiaopai describes how he uses AI for many parts of his work – not just coding. But hyperproductive teams aren’t just using AI – they’re building their own AI-powered tools.

## Building Custom Productivity Tools

It is not surprising that the individuals who are finding the most aggressive ways to use AI are mostly software engineers. Programmers have a notorious fascination with automating, not just their customer’s work, but their own. As DEC engineer Dick Sites famously said, “I’d rather write programs to write programs than write programs”. Today, this translates into engineers using AI to build custom tools tuned to their personal workflow.

Entrepreneur Jesse Vincent recently published [a pair](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/) of [blog posts](https://blog.fsck.com/2025/10/09/superpowers/) describing his own approach to automation, also based on Claude Code. **He has been systematically incorporating his best practices into a custom tool, reducing the amount of effort he has to spend in prompting the AI.**

Jesse’s tool presents Claude [^2] with a series of prompts that instruct it to approach each task according to a careful plan:

1. Ask clarifying questions to refine the task definition.
2. Sketch a design, and present it in short installments, asking for feedback after each installment.
3. Generate a detailed plan for implementing this design.
4. Review the plan to verify that it matches the task definition and design.
5. Carry out the plan, a few steps at a time. After every few steps, double-check the progress so far against the design.

I’ve left out a lot of details, but the point is that this process breaks up each project into tasks that the AI agent can manage on its own, and inserts ample cross-checks where the agent is able to refine its own work. As yet another cross-check, the workflow instructs the agent to use a technique known as “test-driven development”. This means that before the agent writes any code, it first creates *test* code that will evaluate whether the actual code is working correctly. If the tests don’t pass, the agent will revise its work until they do.

All this is augmented by a carefully crafted, 1600-word [instruction file](https://raw.githubusercontent.com/obra/dotfiles/6e088092406cf1e3cc78d146a5247e934912f6f8/.claude/CLAUDE.md), densely packed with directives, tips, and tricks to nudge Claude into the habits Jesse has found make it most productive. Some examples:

> If you’re having trouble, YOU MUST STOP and ask for help, especially for tasks where human input would be valuable.
> 
> NEVER add comments explaining that something is “improved”, “better”, “new”, “enhanced’, or referencing what it used to be. \[Presumably he found Claude to clutter its code with these notes.\]
> 
> YOU MUST ALWAYS find the root cause of any issue you are debugging. YOU MUST NEVER fix a symptom or add a workaround instead of finding a root cause, even if it is faster or I seem like I’m in a hurry.
> 
> YOU MUST use the journal tool frequently to capture technical insights, failed approaches, and user preferences.

I haven’t really done Jesse’s work justice in this brief description. You can read more in the two blog posts linked above, and a [GitHub repository](https://github.com/obra/superpowers) in which he has published some of the work. The repository includes a rich suite of “skills” that tell Claude how to do things like brainstorming, systematically identifying the cause of a problem, and responding to feedback.

Getting the best results from AI requires expert prompting skills; Jesse is codifying his best prompts so that he doesn’t need to keep entering them by hand, and so that the system can operate for longer without his intervention. But that’s still not the full story: **true hyperproductivity also requires closing the loop of tool creation**.

## It’s Tools All the Way Up

![](https://substackcdn.com/image/fetch/$s_!9YzF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39cc9caf-900d-4947-916c-a26071041a43_1530x1272.png)

One of the things that Jesse uses his productivity tools for is to improve those very tools:

> One of the first skills I taught Superpowers was [How to create skills](https://raw.githubusercontent.com/obra/superpowers-skills/35c29f0fe22881149a991eca1276c148567a7c29/skills/meta/writing-skills/SKILL.md). That has meant that when I wanted to do something like add git worktree workflows \[a technique for managing multiple projects in parallel\] to Superpowers, it was a matter of describing how I wanted the workflows to go… and then Claude put the pieces together and added a couple notes to the existing skills that needed to clue future-Claude into using worktrees.

**It’s hard to overstate just how self-referential this is**. For instance, when Jesse uses his “Superpowers” tool to codify a skill, the tool uses its test-driven development module to verify that the new skill has been implemented correctly. It generates an example of a task that the new skill is meant to help with, verifies that it is unable to complete that task without the new skill, and then checks to see whether it *can* complete the task once the new skill has been installed. This is a very sophisticated approach, but it all falls out of the understanding of test-driven development that Jesse has already taught his agent:

> As Claude and I build new skills, one of the things I ask it to do is to “test” the skills on a set of subagents to ensure that the skills were comprehensible, complete, and that the subagents would comply with them. (Claude now thinks of this as TDD \[Test-Driven Development\] for skills and *uses* its RED/GREEN TDD skill as part of the skill creation skill.)

He’s not the only engineer pursuing this path. In [Amplifier: Notes from an experiment that’s starting to snowball](https://paradox921.medium.com/amplifier-notes-from-an-experiment-thats-starting-to-snowball-ef7df4ff8f97), Microsoft engineer Brian Krabach describes [Amplifier](https://github.com/microsoft/amplifier), a rich toolkit built to facilitate the practice of moving advanced skills out of the programmer’s head and into a tool. To quote from the project’s home page:

> Amplifier is a coordinated and accelerated development system that turns your expertise into reusable AI tools without requiring code. Describe the step-by-step thinking process for handling a task—a “metacognitive recipe”—and Amplifier builds a tool that executes it reliably. As you create more tools, they combine and build on each other, transforming individual solutions into a compounding automation system.

In his blog post, Brian (the lead engineer) explains how Amplifier is used to improve Amplifier:

> Out of the box, AI coding assistants are strong but context-blind. They don’t remember your patterns, don’t carry forward your prior decisions, and they need hand-holding on anything ambitious.… **\[Amplifier includes\] tooling that can self-improve the system** from observations where users have guided the assistant, reducing the need for the user to do so in the future.  
>   
> ...**We build tools that build tools.** A lot of Amplifier’s scenarios are literally tools that improve Amplifier - transcript processors, knowledge extractors, article illustrators, blog writers - each created from a “describe the thinking, then build it” flow. Over time, the environment gets smarter.  
>   
> \[emphasis added\]

Paul Payne is another engineer on Microsoft’s Amplifier team. He believes we are witnessing a profound change in the practice of software development. Last month, in a blog post titled [My Programming Career is a Historical Artifact](https://payne.io/posts/historical-artifact/), he wrote:

> **This won’t be** ***the*** **thing that replaces me as a programmer, but it convinces me that our timeline is months, not years.**
> 
> With Amplifier, you now have the ability to describe what you want and it will build it for you, from design, to backend, to frontend, including testing, according to your own programming philosophy. But this isn’t the main point. The main point is that **the more you use it, the better it gets. You create reusable tools over time. It captures useful techniques. It learns from your usage of it, suggesting ways to improve** ***itself*****. This is a type of exponential productivity. The things you build help you make things faster.**
> 
> …
> 
> All of the programming skills I described above, the skills I developed over a lifetime, can now be accomplished by tools like Amplifier with the right prompting. The final stretch is to wrap up all this expertise and hand it over to the AI and then anyone, with no programming experience, will be able to have AI build whatever software they need, as they need it.
> 
> \[emphasis added\]

I know of at least three examples of teams who are working in this style, building tools which build tools to improve their tool-building tools. Sam Schillace, manager of the Amplifier team (and my Google Docs co-founder) calls them [compounding teams](https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams) – and they all report astonishing productivity that continues to spiral upward. Is this “it”? Are we witnessing the dawn of the Singularity?

## These Techniques Will Have Limits – For Now

It’s clear that people like Liu Xiaopai, Jesse Vincent, Brian Krabach, Paul Payne, and Sam Schillace are experiencing something profound. And I know of other examples that aren’t yet public. Some people are proclaiming the end of the era in which human beings write code, or even review it. At the same time, I [recently reiterated](https://secondthoughts.ai/p/a-project-is-not-a-bundle-of-tasks) my belief that today’s cutting-edge AIs are still missing important cognitive capabilities, and that full automation of software engineering is years away. Do I need to throw that idea out the window?

My confidence is shaken, but not yet broken. I believe that what these developers are experiencing is real, but I don’t think they’ve “solved” programming (nor do I think any of them have claimed to have done so). Here are some reasons that I’m tempering my expectations.

**They’re all working on new, small projects** (so far as we know). Software developers mostly spend their time extending and maintaining large, mature projects. I don’t just mean behemoths like Microsoft Office; even “upstarts” like Slack, Notion, or Figma have long since grown into complex codebases. To say nothing of the great mass of legacy software that runs inside your Toyota automobile or behind the scenes at United Airlines. The oldest and largest project the Amplifier team has reported working on is Amplifier itself. If these techniques are being applied successfully in larger, messier environments, I haven’t heard about it yet.

**I don’t expect these techniques to reliably handle complex, novel challenges**. When asked to undertake a substantial project, current AI models can [go off the rails in all sorts of ways](https://secondthoughts.ai/p/gpt-5-the-case-of-the-missing-agent). They fall down a rabbit hole investigating an unimportant detail, persist in attempting an unworkable approach, or hallucinate an incorrect understanding of their situation that renders all of their future efforts counterproductive. The systems these hyperproductive engineers are building incorporate mechanisms to keep their agents on track, but those mechanisms will only go so far. For instance, instructing an agent to review its own work can lead it to correct obvious errors, but there’s no guarantee that it will spot subtle mistakes or failures of judgement. It might even find unnecessary things to complain about, creating more work for itself.

**We’re witnessing a selection effect**. These hyperproductive teams are, quite naturally, gravitating toward the kinds of tasks that best match the capabilities of their tools. We shouldn’t expect the current generation of those tools to provide the same level of productivity boost for other tasks, even if it’s not yet clear what sorts of tasks fall into each category. Nor should we expect just anyone to be able to follow in their footsteps; it takes a special sort of mind to use tools to instruct tools to improve their tools. (Yet another reason that [the future is already here, it’s just not evenly distributed](https://secondthoughts.ai/p/uneven-impact-of-ai).)

**Small teams having a big impact is not a new phenomenon**. Instagram was only 13 people on the occasion of its billion-dollar acquisition by Facebook. When we see these early examples of exceptional teams achieving exceptional things using AI, **the key ingredient might be the exceptional teams**.

**Everything is overestimated in the short run**. When an exciting new phenomenon appears on the scene, it usually takes longer than we think for it to have a broad impact. Though [this process may run faster in the AI era](https://edisonscientific.com/articles/announcing-edison-scientific):

> It is often said that people overestimate what they can do in 2 years and underestimate what they can do in 10. These days, with the extraordinary pace of AI research, my impression is that we may actually overestimate what we can do in 6 months, and underestimate what we can do in 2 years.

These are my reasons for expecting hyperproductivity to have limits, at least for a while. But even so, it may have a significant impact. We should strive to learn more about the scope of that impact.

## Hyperproductivity May Struggle to go Mainstream

One thing I’ve heard repeatedly to describe this style of work is “exhausting”. Much of the productivity boost comes from being able to pursue several sub-projects at once, each using a separate AI agent. The human role is to be a simultaneous manager, tutor, and genetic engineer for a squad of tireless, but sometimes clueless, agents. Each agent needs to be kept busy with tasks, and those tasks need to be coordinated so as to prevent one agent from interfering with another’s work. At the same time, the hyperproductive worker is constantly evaluating their every move (and every move taken by their agents) to see whether it could be done more efficiently.

Perhaps the most exhausting aspect of this work is that it’s constantly evolving. You can never settle into a routine, because those routines are exactly what gets automated. Each step up the productivity ladder means a new way of working and a new set of skills to acquire.

**This may be a difficult transition for most people**. Delegating all of your direct work to an AI is a major transition. Shifting your focus from doing the work to optimizing tools and workflows is another transition. Managing multiple agents is stressful – if exhilirating. All of this requires a new mindset and a different set of skills.

Software engineers at least start out with experience working with automation and, often, customizing their tools. The challenge may be even greater for people with other backgrounds. Hyperproductivity may not be limited to programmers, but that’s where the early examples have been found (even if they are sometimes using these techniques for tasks other than programming).

## What To Watch For

As I mentioned at the outset, the new breed of hyperproductive teams have three things in common. They’re building lots of bespoke tools. They’re letting AIs do all of the direct work, reserving their own efforts to specify what should be done and to improve the tools. And they are achieving a compounding effect, using their tools to improve their tool-improving tools. The net effect is what I’m calling “hyperproductivity”:

> **A hyperproductive individual does not do their job; they delegate that to AI. They spend their time optimizing the AI to do their job better.**
> 
> **A hyperproductive individual may also spend time** ***deciding what the AI should do,*** **but that represents a failure to fully delegate**.

There are plenty of open questions. How large is the productivity boost? (It will certainly vary by team and task.) What is the range of situations for which AI systems have the needed capabilities? How many people will gravitate toward this style of work? What skills are required, how many people have them, how many can learn them, and how long will that take?

If this is going to be more than a niche phenomenon, we should expect to see the following things:

1. A dramatic increase in the number of hyperproductive teams [^3].
2. In particular, a shift toward teams using “off the shelf” hyperproductivity frameworks (like Amplifier), rather than building their own recursive toolkits from scratch.
3. This approach being applied in a broad range of situations, some with large-scale impact; not just tiny teams working on greenfield projects and well-defined tasks.
4. Potentially, broad usage beyond software engineering.

It will be very interesting to see whether this approach takes root inside the frontier AI labs. (Of course that might be happening already. For what it’s worth, the handful of anecdotal reports I have suggest not.) Plausibly, this is how an “intelligence explosion” would first manifest.

We should especially watch to see whether Claude Code, OpenAI’s Codex, or Google’s Jules are evolving to support the kinds of skill-accumulation and self-improvement techniques the hyperproductive teams are using, and *in particular* for signs that the frontier AI labs are prioritizing these capabilities in their model training process. Conceivably this could be the next big avenue for AI progress, tagging in if reinforcement learning – RL – starts to lose steam.

If hyperproductivity tools become easier to use, but remain limited to small, new projects, we should expect an explosion of those small projects. We’ll see less energy expended on getting things done in legacy applications.

Suppose, however, that the limitations I’ve suggested don’t pan out, and hyperproductivity turns out to be widely applicable, including for large, mature software engineering projects, and for tasks outside of engineering. What then?

## What Would Widespread Hyperproductivity Yield?

If and when this new style of “compounding” work goes mainstream, I don’t think the immediate impact would be profound. It takes time to adapt workflows to take full advantage of a new technology. If Microsoft engineers can work ten times faster, Windows and Office wouldn’t be ten times better. Perhaps they could ship updates to Office ten times more often, but would that even be desirable?

We should look for a major impact when this approach rolls out within the labs that are developing cutting-edge AI. In the meantime, what we might most expect to see is a tsunami of fast-moving startups. The AI era was *already* having this effect, both because of the opportunity to build new AI-powered applications (like Cursor, a company which in three short years has achieved massive adoption and a $29 billion valuation), and because AI tools are goosing the productivity of nimble startup teams (see the story of Liu Xiaopai, above). Startups will find ways to bring the hyperproductive approach to an increasing number of domains, and the results will be dramatic. I’ll close with this quote from [The Amplifier Vision](https://github.com/microsoft/amplifier/blob/main/AMPLIFIER_VISION.md):

> **The bottleneck isn’t AI capability; it’s human imagination in how to use it.**

*Thanks to Afra Wang, Amar Sood, Herbie Bradley, James Cham, Jesse Vincent, and Rohit Krishnan for suggestions and feedback (and to Abi for the post image).*

## Appendix

A few ideas that didn’t fit into the main piece:

1\. Aggressive use of AI is, for the moment at least, expensive. Some hyperproductive teams are spending [thousands of dollars per day](https://paradox921.medium.com/amplifier-notes-from-an-experiment-thats-starting-to-snowball-ef7df4ff8f97#:~:text=and%20reading%20docs.-,Not%20cheap,-.%20We%E2%80%99re%20pushing%20the) to power their AI tools. In some cases they see this as worthwhile for its own sake. Sometimes they view it as an investment in understanding the future. But AI operating costs are notoriously plunging by 10x or more each year, and the range of applications for which this AI-intensive approach is cost-effective will widen rapidly.

2\. [Tasklet](https://tasklet.ai/) is a new service that builds AI agents on demand. “Just describe what you want in plain English, and Tasklet handles the rest.” Users can provide feedback to their agents, again in plain English, and the agent will update itself. There are parallels with the way the hyperproductive teams are working, though without the “compounding” aspect. [An interview with Tasklet founder Andrew Lee](https://www.cognitiverevolution.ai/always-bet-on-the-models-how-tasklet-puts-the-agency-in-agents-with-ceo-andrew-lee/) does provide hints that the team behind Tasklet is moving in the direction of hyperproductivity. For instance, they use Tasklet agents to test Tasklet.

3\. Jesse Vincent [describes a particularly impressive use case](https://blog.fsck.com/2025/10/09/superpowers/):

> I haven’t published all the skills Claude and I have built, because some of them are a little esoteric and some of the ones I’ve played with come from telling Claude “Here’s my copy of programming book. Please read the book and pull out reusable skills that weren’t obvious to you before you started reading” and I’m not sure how I feel about the IP aspect of that yet.
> 
> Stop and think about that last workflow a little bit. This is, I think, one of the foundational ideas in how all this works. You can hand a model a book or a document or a codebase and say “Read this. Think about it. Write down the new stuff you learned.” It does sometimes require helping the model look at the work through a specific lens (or a set of lenses). But it is insanely powerful. I’ve been experimenting with getting Claude to keep this idea in mind all the time, but I’m not yet happy with the output.

4\. The initial rush of bespoke software applications will be exhilarating, and will provide a productivity boost. But there will probably be diminishing returns. We won’t soon find ourselves writing 100 times more software and becoming 100 times more productive as a result.

[^1]: Claude Code is a tool introduced by Anthropic earlier this year. It allows the Claude AI model to carry out extended projects on the user’s computer, working step by step and – ideally – noticing and correcting its own mistakes. Designed for software engineering tasks, it has proven useful for other sorts of work as well.

[^2]: I’m using “Claude” to refer to both the language model behind the Claude chatbot, and the Claude Code agent which uses that model.

[^3]: Amplifier has 2500 stars and 184 forks on Github. I don’t know what this might imply about how many people are making serious use of it.