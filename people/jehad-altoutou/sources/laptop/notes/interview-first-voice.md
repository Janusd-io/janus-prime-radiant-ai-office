---
type: source
source_type: laptop
title: interview-first-voice
slug: interview-first-voice
created: 2026-05-11
captured_by: jehad-altoutou
audience: personal
original_path: /Users/jehad/Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-first-voice.md
original_size: 6168
original_ext: .md
category: notes
extracted_with: text-copy
extracted_at: "2026-05-14T09:51:46Z"
sensitivity: dept
sensitivity_confidence: 0.95
sensitivity_reason: "Per-person interview prompt template for IMS enrolment — public-internal process artefact."
project: janus-puls-onboarding

---

# interview-first-voice

> Part of [[janus-puls-onboarding|Janus PULS Onboarding]] — captured by /janus-brain.

_Extracted from `Documents/janus-puls-onboarding/skills/ims-enrolment/prompts/interview-first-voice.md` on 2026-05-14._

# Interview Prompt — Phase 4 — First Voice (Per Person)

> Use this prompt once per person in the department. Goal: produce one `first-voice-<person-slug>.md` per department member. Each interview is ~15-20 min.

## Two delivery modes

**Mode A — Live interview (recommended for small departments, ≤ 5 people):**
The skill runs the interview with each person directly, populating the template as you go.

**Mode B — Async distribution (recommended for larger departments, > 5 people):**
The skill generates a blank populated template per person (with name and role pre-filled from the parent process resources list) and the department head distributes via Slack/email. Returned forms are integrated into the bundle later.

Ask the department head which mode to use. Default to Mode A.

---

## Opening (Mode A — live)

> "We're going to capture your individual First Voice — your perspective on how you do your work. This becomes part of the [Department] IMS bundle that goes to Simon (ISO Lead). About 15-20 minutes. 6 sections matching what Simon's deck calls for (slide 15).
>
> The questions overlap a bit with what we did in the parent process, but **here you answer for yourself, not for the department**. If your answer is 'same as the parent process,' that's fine — just say so."

## Pre-population from parent + sub-process docs

Before starting the interview, pre-fill:

- `[PERSON NAME]`, `[ROLE]` — from parent process Section 8 Resources / People row
- `[DEPARTMENT]` — known
- `[MANAGER]` — Process Owner from parent process header
- `[DATE]` — today

This saves time and helps the person see the doc is already partially structured.

---

## Q1 — Your work · inputs & outputs

> "Where does the work that lands on your desk come from? Internal meetings, Slack channels, departmental handoffs, external clients, vendors, regulators."

**Probing:**

- "What's the most common way work arrives — meetings, Slack, email, ticketing?"
- "Who do you receive direct asks from?"
- "Does anything fire automatically — scheduled tasks, system alerts?"

**Inputs:**

> "Concretely — what flows in? Requirements, data, requests, briefs."

**Activities:**

> "Walk me through your typical workflow as 4-10 numbered steps. From the moment a request lands to when you hand off the result."

**Outputs:**

> "What do you produce?"

**Receivers:**

> "Who consumes what you produce — internal teammates, other departments, clients?"

Map all answers to template **Q1** section.

---

## Q2 — Controls and check points

> "Where in your workflow are the quality gates? What stops you from proceeding until something's verified?"

**Probing:**

- "Before you start work, does anything need to be confirmed?"
- "During the work, are there checks?"
- "Before handover, who reviews?"

Map to template **Q2** table.

---

## Q3 — Tools & systems you use

> "Be exhaustive — every tool you touch in your day-to-day. Software, AI services, platforms, internal systems."

**Probing — go category by category to prompt their memory:**

- **AI tools** — "Anything Claude, ChatGPT, Copilot, internal agents?"
- **Development / specialist tools** — "VS Code, Figma, n8n, [[linear|Linear]], etc.?"
- **Infrastructure** — "Servers, hosting, cloud accounts?"
- **Productivity** — "Notion, Slack, Monday, email, calendar?"

> **Important:** Remind them they do **NOT** need to add anything to Linear AIR themselves. Just list what they use; the AI department verifies AIR coverage independently.

Map to template **Q3** section.

---

## Q4 — Your KPIs

> "How do you know you're doing well? If you don't have formal metrics, describe your quality bar — what does 'good output' look like for your role?"

**Probing if they say 'no KPIs':**

- "What would tip you off that you're underperforming?"
- "What does a great week vs a bad week look like?"
- "If your manager asked 'how's it going?' — what data would you point to?"

Map to template **Q4** section. Free text is fine.

---

## Q5 — What you need to work better

> "What's blocking you today? What would speed you up if you had it?"

**Probing:**

- "Anything you've asked for but didn't get?"
- "Access, training, tools, support from other teams, clarity on responsibilities?"

Map to template **Q5** section.

---

## Q6 — Questions & ideas

> "Anything you want to ask or suggest about the IMS programme? Doesn't have to be process-related — could be tool ideas, concerns, opportunities."

Map to template **Q6** section.

---

## Closing

> "That's all 6 sections. I'll save your First Voice form as `first-voice-<your-slug>.md` in the Desktop folder. It'll be included in the handover bundle to Simon along with the parent and sub-process documents."

Save the populated `first-voice-<person-slug>.md`. Use the slug generation rule from SKILL.md.

---

## Mode B — Async distribution (alternative)

If the department has > 5 people OR people are in different timezones OR the department head prefers async:

1. For each person on the parent process Resources / People list, generate a blank `first-voice-<person-slug>.md` with `[PERSON NAME]`, `[ROLE]`, `[DATE]` pre-filled
2. Save all forms to the Desktop folder
3. Generate a Slack/email cover note for the department head to send, e.g.:

```
Hi team — as part of [Department] ISO enrolment, please fill in your First Voice form.

Find your form on shared drive at: <path>/first-voice-<your-name>.md
(Or ask me for a Word doc version.)

6 questions, ~15-20 min. Due: [date].

Thanks
[Department head]
```

4. As responses come back, the department head pastes the answers into each form
5. Once all forms are complete, proceed to Phase 5 (handover)

---

## If a person gets stuck

Show them `examples/ai-department/parent-process.md` (the AI Ops Engineer First Voice content is embedded in section 8 Resources of that file). The shape is the same — they can pattern-match.

Or refer them to the worked example in `examples/ai-department/` more broadly.

---

## After all First Voice forms are done

Update `state.json` with the list of completed `people_filled_first_voice`. Proceed to Phase 5 (Handover bundle).
