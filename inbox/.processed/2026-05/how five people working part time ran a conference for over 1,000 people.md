---
title: "how five people working part time ran a conference for over 1,000 people"
source: "https://x.com/agrimsingh/status/2057919355808288946?s=12"
author:
  - "[[@agrimsingh]]"
published: 2026-05-23
created: 2026-05-23
description: "we ran @aiDotEngineer Singapore with five people, all of us working on it part time alongside our day gigs. here's how we did it.(of course ..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HI8k-3UXsAAnWcH?format=jpg&name=large)

we ran [@aiDotEngineer](https://x.com/@aiDotEngineer) Singapore with five people, all of us working on it part time alongside our day gigs. here's how we did it.

(of course we did get volunteers in the final week for the in-person push, and they were critical - you need humans on the ground when 1,000+ people are physically moving through a venue. but the 3 months of planning, tooling, speaker ops, sponsor ops, workshop allocation, email systems, and backend work before that were the five-person crew.)

a conference with over 1,000 people is not a notion page with a venue attached. it is speakers, sponsors, tickets, check-ins, dietary restrictions, headshots, talk titles, booth assets, reimbursements, attendee emails, maps, badge printing, room capacity, waitlists, last-minute changes, and a constant stream of questions from every channel people can possibly use to reach you.

this naturally introduces chaos at an information level, long before the challenges turn physical. but the main reason we managed to make it work is that we did not try to staff the chaos manually.

we turned as much of the conference as possible into software with a lot of custom tools, and a willingness to build the missing piece whenever a workflow started repeating.

## the boring secret: event ops is a data problem

while conferences are about programming, curation, community, sponsorship and vibes, a lot of the pain is just data consistency once the event gets large enough.

is this the latest speaker bio?

did this sponsor upload their booth assets?

which email should this person use to log in?

is this attendee booked for the workshop or only waitlisted?

did the ticket buyer use a different email from the person attending?

which room is full?

who still needs to receive the workshop update?

where is this talk happening right now?

you can answer those questions with spreadsheets and group chats for a while until one day the spreadsheet is stale, the thread is buried, and someone at the registration desk needs an answer in 20 seconds. this necessitated that the conference have a backend.

[@convex](https://x.com/@convex) became that backend for all our the custom apps. [@nextjs](https://x.com/@nextjs) gave us quick web surfaces. [@resend](https://x.com/@resend) handled email. [@DevinAI](https://x.com/@DevinAI) helped build the conference website. [@openai](https://x.com/@openai) Codex and [@cursor\_ai](https://x.com/@cursor_ai) Cloud helped us build the internal apps, especially on the move. [@ManusAI](https://x.com/@ManusAI) helped with repetitive outreach over linkedin and twitter dms. codex plugins helped with making sense of emails, mass sponsor outreach, and status checks. [@NotionHQ](https://x.com/@NotionHQ) was there for tracking when a lightweight human-readable layer made sense.

## the website was only the front door

our first point of contact was the conference website. this was where people saw speakers, sponsors, the schedule, and the basic story of the event.

but the website was only the visible part.

behind it we had:

- a speaker and sponsor portal at [aie.65labs.org](https://aie.65labs.org/)
- a public conference API at [aie.65labs.org/api/v1](https://aie.65labs.org/api/v1)
- a workshop operations app at [aie-workshops.65labs.org](https://aie-workshops.65labs.org/)
- a live attendee site at [live.65labs.org](https://live.65labs.org/) complete with live maps and conference programming
- a lead scanner app for QR codes and sponsor scans at [leads.65labs.org](https://leads.65labs.org/)
- admin tools for tickets, emails, capacity, exports, and sync jobs

the alternative was not "use one clean off-the-shelf platform." the alternative was five people becoming the glue between ten different platforms, spreadsheets, inboxes, and venue realities.

## the portal replaced hundreds of loose threads

the speaker portal started with a very normal problem: speakers send information in annoying ways.

one person sends a headshot in email. another updates their talk title in WhatsApp. someone else has a bio in a google doc. another speaker has reimbursement details in a thread with a different subject line. none of this is malicious, it is just how humans operate.

at a small scale, you can live with it. but at conference scale with nearly 100 speakers, it eats you alive.

![Image](https://pbs.twimg.com/media/HI8xBxVXMAAZQIz?format=jpg&name=large)

we collected speaker details through our own portal: talk titles, descriptions, bios, headshots, social links, travel notes, reimbursement info, dietary restrictions (for our speaker dinner). the sponsor side worked the same way. sponsors could submit booth assets, workshop details, logos, descriptions, and the other bits the team would otherwise chase across inboxes.

the important design choice was that drafts had to save even when incomplete.

while a normal form wants to be finished, event ops rarely works like that. a sponsor might have the booth logo today and the workshop copy tomorrow. a speaker might have a bio but no final talk title (we were getting these as late as the day of the talk!). if the tool refuses to save partial work, people go back to email. and we don't want this on email. so we treated completeness as a score, not a gate - save the partial truth. show what is missing.

## we made the conference machine-readable

we also exposed the conference through an API.

at [aie.65labs.org/api/v1](https://aie.65labs.org/api/v1), we had endpoints for the event, schedule, sessions, speakers, calendar feeds, and OpenAPI docs. talks could be filtered by format, topic, or search query. speaker metadata and talk details could be pulled from the portal data without exposing private fields.

this was partly for us and partly for agents.

if the schedule only exists as a webpage, every downstream tool has to scrape it. if it exists as an API, you can build on it - you can generate an itinerary or ask for all the coding-agent talks. you can search for MCP or power a live map. you can hand the endpoint to codex and have it curl its way through the conference.

this was a conscious design decision i.e. we were not only using AI tools around the event but also structuring the event so AI tools could actually understand it. a conference website is for humans and the conference API is for everything else.

## workshops needed their own operating system

workshops were where the custom software paid for itself most clearly.

the attendee-facing side lived at [aie-workshops.65labs.org](https://aie-workshops.65labs.org/). an attendee could open their ticket and see exactly which workshops they were booked into, the time, and the room. staff could also use that ticket view to quickly check whether someone was actually on the list.

![Image](https://pbs.twimg.com/media/HI8ovCuW8AA1ylS?format=jpg&name=large)

underneath, we had to connect workshop state to ticket data, support allocations and waitlists, expose attendee tickets, and give admins enough visibility to make decisions on the day itself. we reverse engineered the ticket platform flow to build the layer we needed on top of it since it did not expose webhooks or an api.

the admin side had the boring buttons that actually make an event run:

- ticket sync
- attendee management
- email campaigns
- capacity dashboard
- CSV exports
- waitlist visibility

![Image](https://pbs.twimg.com/media/HI8o_Y9WcAA93Hl?format=jpg&name=large)

the email campaign view let us draft, snapshot recipients, preview the audience, send tests, and send through Resend. the preview showed the difference between claimed attendees and ticket buyers. that mattered because the person who bought the ticket was not always the person attending.

this is the kind of detail that sounds small until you email 1,000 people because if your recipient list is wrong, the whole campaign is wrong.

workshop updates could use the latest ticket and allocation data. sponsor emails could be tied to portal access. admins could preview the audience before sending. this made it really easy for us to run our email ops to "send this to the people who match the current state."

![Image](https://pbs.twimg.com/media/HI8pLi3XoAAfnW7?format=jpg&name=large)

the capacity dashboard showed what we actually needed to know: scheduled sessions, room capacity, speaker gaps, booked counts, waitlists, and exports per workshop. if a room was at 300/300 with a waitlist, we could see it. if a workshop host needed an attendance export, we could get it. if staff needed to know whether there was pressure in a room, they did not need to ask three people.

a workshop signup form is easy - the hard part is everything after signups: people change plans, rooms have limits, ticket data changes, emails need to go out, staff need to verify attendees at the door, and workshop hosts need clean lists. convex being realtime made it a breeze to track this data as attendees were updating their preferences.

## the live site made the venue easier to navigate

we built [live.65labs.org](https://live.65labs.org/) for the event itself.

the goal was not complicated: people needed to know what was happening, where it was happening, and where to go next. maps, session locations, favourited talks, the stuff you need when you are physically moving through a venue.

![Image](https://pbs.twimg.com/media/HI8yMN9WEAAwlGh?format=jpg&name=large)

![Image](https://pbs.twimg.com/media/HI8yCOJXEAAc2ek?format=jpg&name=large)

this worked because the schedule was already structured. the live site did not have to be another disconnected artifact. it could sit on top of the same conference data. the live site answers the question someone has while walking between rooms: where am i supposed to go now?

## lead scanning connected sponsors back to ticket data

we also built our own lead scanner app.

sponsors needed to scan attendee qr codes. attendees needed badges. we needed the scans to connect back to ticket data and printable badge data enriched with data like job title, place of work. the ticket platform we used did not expose this information to be readily available so we used codex/cursor to dynamically generate qr code links, saved in convex, that could be rendered as qr codes. the badge printers could then print the appropriate qr code and sponsors could scan them.

our alternative, if we didn't build this, would be to use an external lead scanning service which would sit in a separate silo from the actual tickets and badge printing, which would only lead to more manual work. additionally, it also puts the burden on the team to deliver scanned leads post-event. with our custom app, this could be done on the sponsors' side itself.

## manus was an outreach intern that sent linkedin/twitter dms

not all of the work was internal systems. Some of it was distribution.

For outreach, we used [@ManusAI](https://x.com/@ManusAI) like a browser-based ops teammate which could operate linkedin and twitter/x, follow a target list, move slowly, and write down what happened.

![Image](https://pbs.twimg.com/media/HI8s8glW0AAMWm6?format=jpg&name=large)

one run handled twitter/x outreach for a company target list. manus searched for company accounts and affiliated people, followed relevant accounts, attempted DMs where available, paced the actions, and wrote back a report. it also recorded the dead ends: no active handle, DMs restricted, no good contact.

another run was linkedin research - using manus' wide research, we found likely contacts across sponsor and partner targets, with names, roles, and linkedin urls. additionally, it biased toward people who might actually care about a conference partnership: developer relations, growth, product marketing, partnerships, founders, gtm leads.

a later run moved from research to execution, sending personalized connection requests across ai and robotics companies. it adjusted based on company size instead of forcing the same quota everywhere.

the lesson was not "automate spam" but constrained delegation. humans set the target list, positioning, and tone. manus did the repetitive browser work and came back with an audit trail.

## codex plugins helped with the inbox layer

codex was not just for code.

the team used codex plugins for conference ops too: making sense of the chaos spread across various emails, thread summaries, status checks, sending sponsor updates and follow-up tracking. we connected work into notion where it made sense, so the state did not live only in someone's inbox.

![Image](https://pbs.twimg.com/media/HI8tu_5XkAA6tci?format=jpg&name=large)

this is the unsexy part of running an event. no one wants to manually triage requests across gmail, slack, notion like, "did this sponsor send the asset?", "did we reply to that thread?"

## what actually made this work

1. if data matters, put it in a backend.
2. if a workflow repeats, build a small app.
3. if staff need to inspect something, make an admin view.
4. if attendees need to act, give them a direct surface.
5. if agents need to help, expose an API.
6. if email depends on state, send from state.
7. if data is incomplete, save it anyway.

a tool that only accepts perfect submissions pushes everyone back to whatsapp. a tool that saves partial state gives the team something to work with.

none of this replaced judgment, obviously. ai tools do not know what the conference should feel like and did not decide which sponsors mattered, which speakers were right, or when a workflow was getting too brittle. a browser agent will happily execute a bad outreach plan. a coding agent can build the wrong thing very quickly.

we spent less time manually reconciling rows and more time designing the reconciliation flow. less time copying email lists and more time deciding who should receive what. less time digging through sponsor threads and more time deciding what to do next.

## what i would do again

for next year's edition i would preemptively ask:

- where does the truth live?
- what work is repeating?
- what should attendees be able to check themselves?
- what does the team need to see at a glance?
- what should be available through an API?
- where should humans stay in the loop?

five people working part time can run most of the machinery for a 1,000-person conference, but only if they are not manually carrying every piece of state in their heads. the software will not replace the team but let a very small team act like a much larger one.