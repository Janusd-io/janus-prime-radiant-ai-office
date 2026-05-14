---
type: transcript
source: meeting
meeting_slug: 2026-05-14-data-management-system-overhaul-meeting
captured_by: jehad-altoutou
created: 2026-05-14
fireflies_id: 01KRJHC7PHQWWJH66T3DBB13K4
fireflies_url: https://app.fireflies.ai/view/01KRJHC7PHQWWJH66T3DBB13K4
---

Speaker 1: Okay, we're configured.
Speaker 2: I think it's going to be quick from my end.
Speaker 3: Mm-
Speaker 2: Because I was just working on the,  enrollment.
Speaker 2: For the,  Obsidian.
Speaker 3: Mm-
Speaker 2: Yes, yes, yesterday.
Speaker 3: Yeah.
Speaker 2: So hopefully today it's going to be done.
Speaker 2: Let's see.
Speaker 3: Cool, cool, cool.
Speaker 3: So do you need that to get Android to speak?
Speaker 2: Mm-
Speaker 3: Yeah.
Speaker 2: You, you need that for the marketing one?
Speaker 3: Yeah.
Speaker 2: Okay. 'Cause this directory on the local, well, the directory is set up in Google Shared, so we don't want it there anymore. So we have to do everything. So we just.
Speaker 3: Yeah, I've already fixed it to go to GitHub.
Speaker 2: Yeah, so we should so you'll just start over with it?
Speaker 3: Yeah.
Speaker 2: Yeah, I think it's easier.
Speaker 3: Oh.
Speaker 2: He's got Obsidian installed. Oh, downloaded. So Obsidian works.
Speaker 3: Mm-
Speaker 2: He's got Cowork set up. I did I did try to connect it, but it didn't do very well, so.
Speaker 3: Mm-
Speaker 2: Probably delete that project and start over. So we got to do one, one, once the GitHub is up and running.
Speaker 3: Mm-
Speaker 2: Do you really need the do we really need the GitHub app, desktop app, or?
Speaker 3: No, no, no.
Speaker 2: No? The Claude can do the.
Speaker 3: Mm-
Speaker 2: But it needs to run in CLI?
Speaker 3: Well, today I noticed something on the.
Speaker 2: Apaches?
Speaker 3: When I opened Obsidian today.
Speaker 2: Mm-
Speaker 3: For some reason, I got notifications get pull, get push. Everything.
Speaker 2: Mm- Is updated. So I was like, you know.
Speaker 2: Yeah. That's the that's the thing running in the background.
Speaker 3: Mm-
Speaker 2: Probably.
Speaker 3: So I don't think we need CLI.
Speaker 2: No, I think. Just  Just push.
Speaker 2: Just like it does it directly. Yeah.
Speaker 3: Push everything in there once you open it, everything's going to be refreshed.
Speaker 2: Yeah, it's a it's a good plugin. It, it, it.
Speaker 3: It's really good. Yeah.
Speaker 2: It's got all sorts of settings and everything on it. So yeah, I think I think it's fine.
Speaker 3: Mm-
Speaker 2: Um, so yeah. Okay, so let's start with a blank sheet.
Speaker 3: Okay. Let  Let's get Android open and running as quickly as practical today. I mean, if we have to wait in, obviously, if you need to wait another day, that's.
Speaker 3: Mm-
Speaker 2: That's fine. But.
Speaker 3: I know I have created, like, a sync skill.
Speaker 2: Oh, okay.
Speaker 3: Well, first we need to run Janice,  Brain. So it can fetch everything on the. Mm-
Speaker 3: On the laptop and push it.
Speaker 3: And then in case.
Speaker 2: And what does it want to start?
Speaker 3: Why do we want to start?
Speaker 2: So okay, this is sync skill for what? For the.
Speaker 3: Skill the sync is later on after we push everything. Maybe, like, once a week if you want to sync anything. It's going to run automatically.
Speaker 2: Mm-
Speaker 3: But in case you want to push something, like, pretty soon before the cron, so we can. Mm- Syn  Sync it there.
Speaker 2: Well, what you're calling a sync, the I call it in-ingest.
Speaker 3: Oh.
Speaker 3: Oh, yeah.
Speaker 2: That's why I was confused, sync. It's, it's really more to me, it's an ingest.
Speaker 3: Mm-
Speaker 2: When you want when you put when your inbox is full.
Speaker 3: Mm-
Speaker 2: It's the, the process of ingesting is that's when it goes and pulls in.
Speaker 3: Oh.
Speaker 2: Mm- It's actually pulling the, the information in.
Speaker 3: Mm-
Speaker 2: And organizing it accordingly.
Speaker 3: Mm-
Speaker 2: So the term that I picked up.
Speaker 3: From the inbox?
Speaker 2: From the inbox.
Speaker 3: Mm-
Speaker 2: But the question is, do you also want to pull from the system's record? Does it also go check linear? It doesn't have a it didn't go full analysis of everything in linear with all the enrichment. It just picked a few tools.
Speaker 3: Mm-
Speaker 2: So I'm wondering if, if we need to force it to get more s.
Speaker 3: Well, from, from.
Speaker 2: Smarter.
Speaker 3: From this one, it, like, the sync here, it doesn't go from the inbox. It comes from the laptop itself.
Speaker 2: Mm-
Speaker 3: So whatever you're connected, your,  Claude is connected to.
Speaker 2: Oh, oh, okay.
Speaker 3: It will fetch all of them.
Speaker 3: From there. Linear, Notion, whatever it's in the connector.
Speaker 2: Okay, so it pulls it and does it also do the inbox too?
Speaker 3: Yeah.
Speaker 2: Yeah.
Speaker 2: Okay. So that's I, I called it the ingest.
Speaker 3: Oh.
Speaker 2: The, the reason is, is because it's pulling it in.
Speaker 3: Mm-
Speaker 2: To from the external sources in.
Speaker 3: Mm-
Speaker 2: And,  not syncing per the sync is what it does with.
Speaker 3: Mm-
Speaker 2: Anyway, it's a semantic detail. If you want to key it Claude sync, that's fine.
Speaker 3: Mm-
Speaker 2: Yeah. But  But I was thinking about how we're going to pull all of them to create, like, a, a whole company structure.
Speaker 2: That, that, that, that'll come later. But before we move there, the other thing I've noticed because I just did a lint last night, but it had a bunch of stuff that it queued up that need, you know, nice to do, organizing.
Speaker 3: Mm-
Speaker 2: There's quite a lot of housekeeping involved in maintaining the wiki, maintaining.
Speaker 3: Mm-
Speaker 2: The, the, the, the entire structure.
Speaker 3: Well, is it was there anything.
Speaker 2: Is there anything you need to run housekeeping tasks? So lint is one. And then.
Speaker 3: Was there anything from my end? Because it does have lint integrated as well.
Speaker 2: Mm-
Speaker 3: For me.
Speaker 2: Yeah, but if you go to Claude.
Speaker 2: If you go to the Cowork project where it is.
Speaker 3: Mm-
Speaker 2: It gave me a whole list of things that so you're now connected to,  to the repo, right?
Speaker 2: You-you're Obsidian is the same as mine.
Speaker 3: Yeah.
Speaker 2: Yeah, so we're synced. Okay.
Speaker 2: So there's a bunch of stuff. So I just did a lint last night while I was away. And then there's another area that it, it gave me a list of things that were nice to do but not urgent to go through. Mm-
Speaker 2: Kind of just it, it just kind of reorganizing things.
Speaker 3: Mm-
Speaker 2: Like, I call it tidying up.
Speaker 3: Mm-
Speaker 2: Making sure  because what it does, is certain tasks that are it doesn't view as urgent. It defers them.
Speaker 3: Mm-
Speaker 2: So you can queue them up and do them later.
Speaker 3: Mm-
Speaker 2: So you got to keep track.
Speaker 3: Yeah. Of  Of these things and then s periodically ask it, "So is there anything in the queue that needs to be taken care of?"  Mm-
Speaker 2: Hmm.
Speaker 2: And as and part of it is, as it's processing, new information, and it starts detecting new patterns and new connections and all of that, it wants to reorganize things around those themes.
Speaker 3: Mm- Mm-
Speaker 2: Right? So it, it, it's really interesting because it's actually spotting patterns. And when a pattern gets big enough, because usually there are enough data points for it, it actually will create, like, a folder.
Speaker 3: Mm-
Speaker 2: And it'll organize it that way. And it wants to make sure, you know, the index has to be updated. So there's a lot of maintenance that, that gets done and as it grows, it gets more complicated.
Speaker 2: So I'm just thinking, you know, how do we automate that? Because some of that requires the person in charge you know, there's a queue. I think in one of the earlier chats with Claude, it, it was it was talking about, you know, having a curator.
Speaker 3: Mm- Mm-
Speaker 2: You know, and, and I'm thinking, how are we going to do that? Because that's something we as kind of the do, do we want to have, like, a dashboard? Because we can connect to every one of these because we've got the GitHub, right?
Speaker 3: Yeah.
Speaker 2: Yeah.
Speaker 2: So we can actually connect to any one of these various systems. So maybe that's the stuff that want to venture needs. Mm-
Speaker 2: Because if he has read access because we can set it at GitHub, he can we can build him a system that will read every single one of these wikis.
Speaker 3: Mm-
Speaker 2: Brains and then organize it and pull it all up to him. The, the advantage of doing it on GitHub is now we can do this.
Speaker 3: Yeah.
Speaker 2: We can build a wiki of wikis as every group goes in there. So I think our next kind of architectural discussion is, is, is whether, you know, how we do that.
Speaker 3: Mm-
Speaker 2: How maintenance gets done. You know, there's curation of the system.
Speaker 3: Mm-
Speaker 2: Mm- Parent feeding. Mm-
Speaker 2: It's not just about ingesting it, but sometimes it'll come up with an idea. But it but it but it need it wants verification.
Speaker 3: Mm-
Speaker 2: It, it, it, it's waiting for so that's why there's a file in there called questions. If you if you find if you go dig for it, it's not an entity. It's going to be I think it's a high at the high level. Yeah, there you go.
Speaker 2: So these ques you see, these are ingest. That's why I'm using the term ingest. So you see, what it does in ingest,  it comes up with questions. And then it collects all these things and we need to yeah. So this is actually quite important here. You see, two new entity pages. The one that is proposing an action. Like.
Speaker 2: You see, I, I didn't act on this. But it's waiting for me to tell it.
Speaker 2: So we need to answer these.
Speaker 3: Mm-
Speaker 2: Should, should we start tracking them? I, I would say yes.
Speaker 2: You know, fact-setting, should we add that as a vendor?
Speaker 3: Mm-
Speaker 2: Because there's a lot of analysis.
Speaker 2: Or it's saying, "Create it now. Do this the recommendation." So it's and it doesn't surface this unless you ask it.
Speaker 2: Right?
Speaker 3: Mm- Yeah.
Speaker 2: So I've been neglecting these questions, but I need to go back to them because this is stuff so it doesn't autonomously take actions on all these things. It's waiting for suggestion. Now, we could simply say, "These are low " I don't know if you have questions. Yeah, you've got questions too in your first one.
Speaker 2: And again, it's calling ingest. That's the term it uses. So with the skill, I maybe you should rename it. So it's consistent with what it uses. Mm-
Speaker 2: You see?
Speaker 2: Ingest is the atomic action that it does, but see here, questions, what should you do?
Speaker 2: So I haven't really been paying much attention to these, but these are actually quite important. Like, you see, you've got one from yesterday. You've got two from yesterday. In your personal one.
Speaker 2: So the first phase we're going to do this is just going to be to plug everything in and build the data the database.
Speaker 3: Mm-
Speaker 2: I think the next phase we then have to go into is then go through a process with the different departments saying, "Okay, so, so what do you want as the outputs?" Because we, we, we can't expect them to go through this. So do we want to create like a dashboard page? Mm-
Speaker 2: Do we write prototype X, put one together last week, just to kind of see what it looks like? You know, how do we want to present this to people? And when we present it through some kind of dynamic dashboard page, maybe they're in that page, there is a section there that says, you know, "Here's things that are need attention from you."  Mm-
Speaker 2: And surface it that way. There's got to be some kind of if not UI,  because  driving it through just a Claude chat interface is okay, but I don't but again, it goes back to the blank prompt problem.
Speaker 3: Mm-
Speaker 3: Yeah.
Speaker 2: Yeah.
Speaker 2: So I, I don't know yet. I think it's something I see it's doing the same right now.
Speaker 3: Mm-
Speaker 4: So let me ask.
Speaker 3: Oh, there's something or.
Speaker 3: I have to do this manually.
Speaker 4: See, that, that the other thing that's, that's I find very useful is sometimes just to create something. So what I'm going to do because we have another meeting with,  Rosalind and Lysandra later this afternoon, I was going to incite the group that has access to,  the knowledge base, ask it to put a presentation together that I'm going to point it towards your,   That you have something there. I want I want to have a presentation that describes what the process is going to be with them, going you know, how are we going to get them up and running? Step one, step two, step three, what we need from you, what, what we're going to provide. Kind of just lay out the, the a nice lead. Present, you know, a presentation. That we're going to show people, "This is what we plan to do with you." And each one will be a bit unique as to what it's good about this.
Speaker 3: Mm-
Speaker 2: And tailored to what they want. And then we take the conversations, so yeah.
Speaker 4: All right. So let's see if it doesn't that's weird. Why it's giving me the.
Speaker 4: Should run it on its own.
Speaker 2: You can run a command. Then why are you telling me to do it myself?
Speaker 3: Sometimes Claude wants validation.
Speaker 3: Access denied.
Speaker 2: Oh, question denied. Oh, obeyed.
Speaker 3: Who is Ubuntu?
Speaker 2: It's why is it this thing doesn't run Ubuntu Linux.
Speaker 2: It's weird.
Speaker 2: Yeah.
Speaker 2: Step one, let's get everybody up and running the, the, the thing populated. Ingesting as much as it can and what all the various sources that they can give it. Um, but we need I need to go through some of these questions or we go through.
Speaker 3: Mm-
Speaker 2: Maybe that's what we do during the standup.
Speaker 3: Yeah.
Speaker 2: Get some questions.
Speaker 2: All right?
Speaker 2: So the escalation, the new entity page, they say, "Yeah, we should have a entity page for Vivian Balakrishnan Singapore and for fact set." What's the ingest from oh, there's two from yesterday. Three.
Speaker 3: Mm-
Speaker 2: Three questions.
Speaker 2: Lint-driven escalation, create entities, vendors, OpenAI, yeah, we should do an OpenAI. Why is it even asking? Why is this overdue?
Speaker 2: Yeah, definitely should create an OpenAI.
Speaker 2: Yes.
Speaker 2: And just Niman.
Speaker 2: Yes.
Speaker 2: Vendor.
Speaker 2: Create a new vendor.
Speaker 2: Oh gosh, it's really far. It's really falling behind.
Speaker 2: So yesterday we had three things that it's asking for: arguments for, argument against.
Speaker 2: But this is a yeah, a vendor page. It should also get updated in,  the AI registry.
Speaker 3: Mm-
Speaker 2: Ah, you see what it's saying doing? Create it's only got one source, so it's waiting. You see maybe to get more sources, to verify that it's a trend and not just a one-off data point.
Speaker 3: Mm-
Speaker 2: And the second source mentions a new.
Speaker 3: Confidence.
Speaker 2: There's somebody at Janus actually evaluates to use it. Yeah, we're not really using it. But I'd want to keep it in the backlog together with the,  Pinecone.
Speaker 3: Mm-
Speaker 2: For, for future. I don't think it's something we need to use now, although we should do a bit of an analysis.
Speaker 2: And then it's got the vendor for the whole peer set. You see these are some other things. Claude met a manpower's maneuver.
Speaker 3: Mm-
Speaker 2: Q2 agent. Yeah.
Speaker 3: Just one sec.
Speaker 2: What's the recommendation?
Speaker 2: What's it recommending? I don't know.
Speaker 2: To do?
Speaker 2: Defer.
Speaker 2: Match the Q2 OpenAI deferral precedent.
Speaker 2: Ooh.
Speaker 2: Hmm.
Speaker 2: So it's learning from the past.
Speaker 3: Mm-
Speaker 2: Interesting.
Speaker 2: So it takes decisions that we've done in the past as precedent.
Speaker 2: Interesting.
Speaker 2: It's really interesting to see how it's thinking.
Speaker 3: Oh, yeah.
Speaker 2: Right?
Speaker 3: Concepts.
Speaker 2: Yeah.
Speaker 3: We have so many concepts. But where is the,  meetings? Where can I find the meetings?
Speaker 2: It's in there somewhere.
Speaker 3: Hmm. Process.
Speaker 2: Let's use meetings.
Speaker 2: Sources.
Speaker 2: It's in there. There it is.
Speaker 2: In the middle.
Speaker 2: Meetings.
Speaker 3: Okay.
Speaker 3: Yeah, this is the one we had yesterday with the.
Speaker 2: Yeah.
Speaker 3: Contraprisement team.
Speaker 2: Oh, did you run the, the, the transcript through it?
Speaker 3: Mm-
Speaker 2: Is that how I got it? Oh, you already did that.
Speaker 3: Yeah, now transcripts are going into Obsidian now.
Speaker 2: Automatically?
Speaker 2: Oh, they are?
Speaker 3: Instead of Notion. I don't want to use Notion. I'm going to remove it.
Speaker 2: Yeah.
Speaker 3: Because I keep hitting APIs issues.
Speaker 2: We don't need Notion now.
Speaker 2: The only thing we, we, we may want to do is,  you know, for us it's okay to navigate through directory, but you notice it took you a while to even find.
Speaker 3: Mm-
Speaker 2: Over time, it'll get better at it, but I think we need some kind of navigation.
Speaker 3: An Obsidian?
Speaker 2: Yeah.
Speaker 3: Yeah. Because I didn't know where I should look into.
Speaker 2: Yeah.
Speaker 2: But that's the you don't have you shouldn't have to know.
Speaker 3: Yeah, you don't need to.
Speaker 2: You surfaced some way.
Speaker 3: Yeah.
Speaker 2: Not for not just for us, but for.
Speaker 3: Oh, also creates the keeps the idea of Monday.
Speaker 3: That's nice.
Speaker 2: Oh, wow.
Speaker 3: Okay. Okay.
Speaker 2: Oh.
Speaker 2: It really is turning into a brain.
Speaker 3: Mm-
Speaker 2: Like, like our third employee.
Speaker 3: Mm-
Speaker 2: It's the third me-member in the team.
Speaker 2: Yeah.
Speaker 3: That's cool.
Speaker 2: That's where I wanted to get to. I want I want it to become like the like, like a like a member of the team.
Speaker 3: Yeah.
Speaker 2: It's thinking for us. It's making recommendations. It's keeping it's organizing everything. It's kind of like a chief of staff.
Speaker 3: Mm-
Speaker 3: But I don't think it goes into.
Speaker 3: What did we find it?
Speaker 2: Articles?
Speaker 3: What is this?
Speaker 2: Sources.
Speaker 2: Yeah, sources.
Speaker 2: Articles.
Speaker 3: Oh.
Speaker 2: So I'm the one that's putting articles.
Speaker 2: But if you go to LingQ, it doesn't have everything.
Speaker 3: AIO, IT meeting. So it didn't update it didn't sync.
Speaker 2: But I'm glad that meeting is in there because now when I'm going to ask it let's do it now. Go to go to Claude.
Speaker 2: Let's try this.
Speaker 2: Go to go to the,  cohorts.
Speaker 2: Interpreter. Uh, make  Uh, make but the project make sure it's pointed to the wiki.
Speaker 3: Because of this one.
Speaker 2: Is this the one?
Speaker 3: No, that's correct.
Speaker 2: No, that's a different one. Oh, you don't have it. So choose a different folder.
Speaker 3: I don't know where's my vault is.
Speaker 2: It's on your desktop somewhere. It's probably.
Speaker 3: No, I didn't use the.
Speaker 2: Where's the where is it synchronizing to when it pulls it off? Oh, it's in Janus. Go to go to Janus.
Speaker 2: No, there. Primary again. That's it. AI office.
Speaker 2: It's AI office.
Speaker 2: That-that's where it lives.
Speaker 2: So open the oh, oh, so it always allow.
Speaker 3: Oh.
Speaker 2: So tell it let's tell it to create a presentation.
Speaker 2: For the next meeting when the project management throws it on the center.
Speaker 3: For.
Speaker 2: Following up from yesterday's meeting and the presentation should lay out how we plan to onboard them.
Speaker 3: Following up from the.
Speaker 2: Primary again.
Speaker 2: Their own primary again.
Speaker 2: Um,  primary and,  ma remind us to, to, to, to,  mention have it render in an HTML render in an HTML.
Speaker 2: Generated, yeah.
Speaker 2: Okay.
Speaker 2: That's what it does.
Speaker 3: But I don't think it can because it's not yet synced to the office.
Speaker 3: I don't see it in the office. I see it in my personal only.
Speaker 2: Oh, this is in your personal one?
Speaker 3: Hmm.
Speaker 2: Oh, you want some time for that?
Speaker 3: Yeah.
Speaker 2: Okay.
Speaker 2: Oh, this is your personal one. Oh, oh, it's not in the office one.
Speaker 3: No.
Speaker 2: Oh, shit.
Speaker 3: Which PM team?
Speaker 2: Project management team.
Speaker 2: Oh,  no, no, no, no, no, no.
Speaker 2: Okay, it doesn't have enough time.
Speaker 3: Oh, one second.
Speaker 2: Oh, see, this is only in your.
Speaker 3: Oh, I got it. No, not at all.
Speaker 2: No, it's not in my internal.
Speaker 3: Then what is syncing? I'm not understanding. It keeps showing me it's syncing. It's everything is updated, so.
Speaker 2: Yeah.
Speaker 2: Well, it's, it's doing the personal one, but it didn't it hasn't,  ingested the transcript from yesterday's meeting into the office one. Only into your personal one.
Speaker 3: Yeah, that's the thing because it was showing me here.
Speaker 3: Uh, it failed. Pushing it to can't access stored credentials.
Speaker 2: Oh.
Speaker 2: Hmm.
Speaker 3: Let me try some.
Speaker 2: Primary personal.
Speaker 3: Real quick.
Speaker 2: Yeah, the AIO PM meeting. So if it's AIO PM meeting, it should go in the AIO, not into the personal.
Speaker 2: Like those three, if it's if it's Jahad, with you, but if it's these are AIO, Andrew, AIO, IT, AIO, PM, those should go in the AIO folder. It's they're misfiled, I think.
Speaker 3: The AIO?
Speaker 2: Yeah, the last three meetings.
Speaker 3: Hmm.
Speaker 2: Because they're the AI office.
Speaker 3: Hmm.
Speaker 2: Not you person-personally. Those should actually go into  The other wiki. The other brain.
Speaker 2: And they're not in the other one.
Speaker 2: It could just be w-which Claude instance you were running it in. If, if you're running it and Claude cowork is directory is your personal wiki.
Speaker 3: Mm-
Speaker 2: It's going to interact with that. If you're running it when so what I do is I set up a project.
Speaker 3: Hmm.
Speaker 2: A project for personal wiki, a project for,  AIO wiki, and then I make sure that each project it's default directory is the per is the right one.
Speaker 2: Because if you go back to that file directory.
Speaker 2: You'll see. Bear with me so  Bear with me so I've already I don't know.
Speaker 2: Maybe we need to rerun yeah.
Speaker 2: Is the Andrew meeting in the AIO AI office?
Speaker 2: No, not the not the latest. Not the one for oh, yes. Is that the one? Andrew onboard?
Speaker 2: It's the same date.
Speaker 2: Oh, it's with the whole transcript in there.
Speaker 2: Interesting.
Speaker 3: Oh, why?
Speaker 2: I don't know.
Speaker 2: And what about on the your personal where it says AIO Andrew? What do you put there?
Speaker 2: Oh, you see here, here it created the summary.
Speaker 2: That's weird.
Speaker 3: Why it's two different things? No, those are different things. Just.
Speaker 2: Sources meetings. There's also sources meetings.
Speaker 2: It, it handled it differently. One different summary.
Speaker 3: Different time.
Speaker 3: Why this one says 3:00 PM, this one is 12:00 PM?
Speaker 2: I don't know.
Speaker 3: That's past.
Speaker 2: Past,  so it parsed this one. It didn't parse the other one. It just dumped the directory.
Speaker 2: Hmm.
Speaker 2: It just copied. What about the other meetings?
Speaker 2: Yeah, it's just doing so oh.
Speaker 2: But here it does it, it did it differently.
Speaker 3: This is following Notion.
Speaker 2: Yeah, it pulled the Notion one.
Speaker 3: No, I mean, look, Notion structure.
Speaker 2: Yeah.
Speaker 2: It's okay.
Speaker 2: Hmm.
Speaker 2: This thing's still a little bit buggy at working.
Speaker 3: Hmm. We need to see why that happened.
Speaker 2: Oh, so these are Monday of oh.
Speaker 3: Well, these are the one which I which got created from the enrollment.
Speaker 2: Oh.
Speaker 3: And this is the one I created through the stand-up skill.
Speaker 2: Right.
Speaker 3: So that's the difference. Maybe I need to give the same structure to the to be implemented in the enrollment.
Speaker 2: Hmm.
Speaker 2: I think so. Yeah.
Speaker 2: Because. I think  This one the enrollment just dumped everything there.
Speaker 3: Hmm.
Speaker 2: It just pulled it out of,  Fireflies.
Speaker 3: Yeah, and just dumped it there.
Speaker 2: Yeah.
Speaker 2: I see. Yeah.
Speaker 3: Yeah.
Speaker 2: I need to fix that.
Speaker 2: Ah.
Speaker 2: Store GitHub personal access token in the vault session can read something like?
Speaker 2: Oh.
Speaker 2: Sandbox is limited. Can't reach your Mac.
Speaker 2: Keychain.
Speaker 2: Oh.
Speaker 2: That's only locally.
Speaker 2: Yeah, I need a long-term fix.
Speaker 3: Yeah, that's something that errors keeps happening. We'll find a lot of errors now.
Speaker 2: Yeah, well, it's this thing's growing and getting more complicated, so this is what I what I meant. It, it, it, it's, it, it's, it needs a na-nanny.
Speaker 3: Yeah, now it's a game.
Speaker 2: Ah.
Speaker 3: Now it's there.
Speaker 2: Now it clean means. Sorry. Okay. Oh, good. Oh, good.
Speaker 2: Good. This is what we need.
Speaker 3: Hmm.
Speaker 2: Oh, and it even did Monday.
Speaker 2: GitHub repo. Oh, it oh, it caught all this stuff. Yeah, so now it's doing what it did in Notion, but okay.
Speaker 3: That's from the stand-up skill.
Speaker 2: Oh.
Speaker 3: The stand-up skill did the did way better understanding of structure.
Speaker 2: Hmm. Oh, so you ran.
Speaker 3: The enrollment just dumped all the information there.
Speaker 2: Yeah.
Speaker 3: And how does it look?
Speaker 2: So the stand-up skill needs to be included.
Speaker 2: In Claude.md.
Speaker 2: So this is.
Speaker 3: No, not fully, but I mean, just the structure of how to parse.
Speaker 2: Yeah.
Speaker 3: The,  Fireflies meetings.
Speaker 2: Right.
Speaker 3: How to create.
Speaker 2: But the thing is, when it puts the meetings in there, is it going to then go through and do the processing to do check all the linkages and everything?
Speaker 2: The same way the Claude.md does, or do we need to l-lint and kind of re-fix all the connections?
Speaker 3: No, no. It's gonna be connect everything.
Speaker 2: It will. Okay.
Speaker 3: Yeah. Yeah.
Speaker 2: All right.
Speaker 2: Because that's.
Speaker 2: Anything it forgets lint will catch it.
Speaker 3: Because that's what I've done, like.
Speaker 2: Ooh, that looks so cool.
Speaker 3: Uh, when I run the enrollment, it connected everything all together, but I don't know what it was. Is it  Is it orphans?
Speaker 3: I have no idea what are these.
Speaker 3: PR backup something.
Speaker 3: I have no idea what is it.
Speaker 2: These are orphaned.
Speaker 2: It's nothing.
Speaker 3: No, I mean, orphaned for what? Like, even.
Speaker 2: Yeah.
Speaker 3: What is what is I don't remember we had these, these conversations.
Speaker 2: Orphaned. Yeah, it's it picks up some noise.
Speaker 2: I don't know.
Speaker 3: I don't know. I still need to try to understand why there are orphans in here.
Speaker 2: You just run a to give it a, a request, look at all orphaned things, and decide what we do with them.
Speaker 2: There's a whole bunch there.
Speaker 2: Look, backup snapshots.
Speaker 3: Yeah, the that's the thing. Look, it's saying backup shots, but I haven't I have no idea what it's what is backup.
Speaker 2: We have a few in the AI office too, but not as many as in your personal one.
Speaker 3: Hmm.
Speaker 2: Hmm.
Speaker 2: Hmm.
Speaker 2: I don't know. Index is cool.
Speaker 3: Hmm. No, right.
Speaker 2: So that's a that's a full index of everything.
Speaker 3: It's connected to everything.
Speaker 3: That's cool.
Speaker 2: How many connections is Index have?
Speaker 2: Does it need a number?
Speaker 2: Yeah.
Speaker 2: A lot there.
Speaker 3: That's a lot.
Speaker 3: The list is so long.
Speaker 2: It's only gonna get bigger.
Speaker 3: Hmm.
Speaker 2: Yeah. That's yours. And,  AI office one.
Speaker 3: Oh, that's the AI office. That's the thing. It's like, it keeps popping up, but it's not fetching anything.
Speaker 3: So I'm a little confused on where is it.
Speaker 2: Is it.
Speaker 3: Connected and where it's fetching from.
Speaker 2: Well, look where look at the,  GitHub. You can go to preferences.
Speaker 2: And look at no, it's community plugins.
Speaker 2: Click, click on it. Yeah.
Speaker 2: It'll be pulling from the AI office one.
Speaker 2: I don't know. It doesn't say here which one it's from.
Speaker 2: Right?
Speaker 3: Hmm. No.
Speaker 2: So how does it know which GitHub?
Speaker 3: Preferences. Pulling from where?
Speaker 2: Decision settings.
Speaker 3: It's pulling from where. That's the thing.
Speaker 3: Where is this? Okay. It's donated.
Speaker 2: No, that's just goes to the.
Speaker 2: Where's the linkage?
Speaker 3: Wait.
Speaker 2: It's in some settings somewhere, but I can't remember where it is.
Speaker 3: Uh, deployment folder.
Speaker 2: Ah, it's a folder.
Speaker 3: Is it from there?
Speaker 2: Yeah. Click that.
Speaker 3: Oh, it's just.
Speaker 2: Oh, no. That's a plugin.
Speaker 3: Hmm. That's just the plugin one.
Speaker 2: I don't understand where it is.
Speaker 2: Where, where how's, how's it know?
Speaker 2: Well, it, it, it, it's dependent on the folder. So if you go each one has its own plugin. I think if you go to your personal one, that's your.
Speaker 3: This one? This one?
Speaker 2: Yeah.
Speaker 2: Click the look, look, let's see what this.
Speaker 2: You have the GitHub there too.
Speaker 2: Oh, this doesn't have it.
Speaker 2: So you see each of so you need to put the plugin on your personal one. That's why.
Speaker 2: You need to install the Git separately.
Speaker 2: It's, it's not it's still no good. Just it, it it was there just until they go back. So it's right up top.
Speaker 2: It's.
Speaker 3: Okay.
Speaker 2: Yeah. That's the one. The by Vincent 03.
Speaker 2: Yeah.
Speaker 3: Install.
Speaker 2: There you go. Options.
Speaker 2: Yeah. You need to change it to match that.
Speaker 3: Which one?
Speaker 2: So your personal one has not been syncing.
Speaker 2: Which I guess is okay because you're the only one using your personal one.
Speaker 3: Hmm.
Speaker 2: Maybe you don't need this to have a sync, but it's just on your laptop.
Speaker 2: On the local drive.
Speaker 3: Yeah.
Speaker 2: But with other people's.
Speaker 3: Hmm.
Speaker 2: That's why you're not getting the messages on this one.
Speaker 3: Hmm.
Speaker 2: Although now you've turned it on. I think you've enabled it. But it's set to zero, so it's not gonna do anything because if you go back to the settings, you know, thi-this one is set to five minutes.
Speaker 2: You see where it says auto-commit and sync zero? So it's not gonna be doing anything until you put a number in there.
Speaker 2: And do the other changes.
Speaker 2: Yeah.
Speaker 3: But even in here, it was zero, right?
Speaker 2: No.
Speaker 2: I set it to you see it's five, five, five minutes.
Speaker 3: Oh my God.
Speaker 3: Five, five.
Speaker 3: One thing else.
Speaker 2: And also the vault and everything. You s you see those settings of vault, data, host name. So it knows who did the push.
Speaker 3: Hmm.
Speaker 2: It's basically your computer name.
Speaker 3: Do you need a do I need to change anything here?
Speaker 2: Hmm. If you don't, it'll just it won't it'll just give a date, but you'd only use your own personal one. So I guess it doesn't really matter.
Speaker 3: Hmm.
Speaker 2: The other one is useful because you can always it, it, it knows it allows us to determine whether you did it or it's not from your computer buying.
Speaker 3: Hmm.
Speaker 2: Or anyone else's.
Speaker 3: Hmm.
Speaker 2: But we gotta figure out this multi-user thing for Android. It's less important, but for the PM group.
Speaker 3: Oh yeah.
Speaker 2: And,  and for IT, is, is that happens? We need to.
Speaker 2: Oh, failed.
Speaker 2: Another Git processor seems to be oh,  so you can't be running two?
Speaker 2: Oh, that's interesting. You can't run two separate ones?
Speaker 2: All right. Turn it off.
Speaker 2: Maybe each system can only run one?
Speaker 3: All righty.
Speaker 2: I guess we must be doing this fine, but.
Speaker 3: Hmm.
Speaker 2: Yeah.
Speaker 2: I think we need to be careful with the personal one. It's adding a adding complexity.
Speaker 2: My brain is struggling.
Speaker 2: To get my brain wrapped around this.
Speaker 3: Hmm.
Speaker 2: So the sources that you've got there, I guess looking at it, if it says Jihad Vault, is that from your personal one?
Speaker 2: Is that what this is?
Speaker 3: Uh, I think this is what I have uploaded, maybe.
Speaker 2: Hmm.
Speaker 3: Yeah. What does that mean?
Speaker 3: From Jihad?
Speaker 2: Hmm. It's personal yeah. It's personal vault articulation. So this is coming from your personal vault.
Speaker 3: Hmm.
Speaker 2: So this is the cross-link?
Speaker 2: 'Cause we still haven't figured out how we're gonna link these things that old federated approach. We're not working. We don't need maybe a different.
Speaker 3: Hmm.
Speaker 3: But not having access is not gonna be useful for them.
Speaker 2: Yeah.
Speaker 3: Federation's gonna be wasted.
Speaker 2: Yeah. Exactly.
Speaker 3: It won't be even implemented.
Speaker 2: Hmm.
Speaker 2: So should we go ahead getting Android set up or?
Speaker 3: Yeah. I'm gonna switch the,  meeting one.
Speaker 2: This? Yeah.
Speaker 2: Yeah. This will be easy 'cause just one. Yeah.
Speaker 2: System just for him for now.
Speaker 3: Hmm.
Speaker 2: But this personal group one, it's still a little bit in.
Speaker 2: Janky.
Speaker 2: And it's not working quite like.
Speaker 2: I don't quite there yet.
Speaker 3: Hmm.
Speaker 2: It's, it's the overlap between the two, but it's also a, a confused as to how this Git sync knows 'cause you're, you've got a personal one. I mean, you can go back to the GitHub itself and see what the date stamp's on there and when.
Speaker 3: I mean, oh, do we need to do that?
Speaker 2: For the personal one, I don't know. I don't know.
Speaker 3: No. I mean, like, even for the company one, they can't go to GitHub and check it out and.
Speaker 2: Well, how else are we gonna keep them synced between your copy and my copy?
Speaker 2: If we go to yeah. Go to I/O.
Speaker 2: Right?
Speaker 2: So if we go to repos.
Speaker 2: That's the AI office one, right?
Speaker 3: Yeah.
Speaker 2: You yeah. So your, your personal one's not up there.
Speaker 2: Is it?
Speaker 3: Hmm.
Speaker 2: 'Cause your personal one, if you go, go up to the.
Speaker 2: Yeah. This is a mirror of the AI office, right?
Speaker 2: AI office.
Speaker 2: Well, what does that do with the top one? 20 commits? Oh, that's just saying that you did com you were doing commits?
Speaker 2: So let's see.
Speaker 3: Yeah.
Speaker 2: Yeah. Is it added?
Speaker 3: Yeah.
Speaker 3: The commits I've, I've done.
Speaker 2: Yeah.
Speaker 2: Oh, and these are mine. Okay. So, so it is getting the backup suite too, but your MB.
Speaker 3: Hmm.
Speaker 2: Mine. So it's, it so to log in so, so it is working, but we're both able to update it.
Speaker 3: Hmm.
Speaker 2: So that's good.
Speaker 2: Federate. Oh, interesting.
Speaker 2: It's not a backup. What does federate mean?
Speaker 3: What?
Speaker 2: Go, go, go scroll up. There. You see? Premiere.
Speaker 3: This one?
Speaker 2: The next one down. What does fe 121 notes federate? What is that?
Speaker 3: It's one of the it's when I pushed everything, when I created the enrollment.
Speaker 2: Oh.
Speaker 3: That was the enrollment.
Speaker 2: Oh, I see. Okay. Gotcha.
Speaker 2: Enable. Go to initial. Initial import. Okay.
Speaker 2: And then the backups.
Speaker 3: Hmm.
Speaker 2: It's every time I did a push, the sync my desktop with this.
Speaker 3: Hmm.
Speaker 2: Yeah. Yeah.
Speaker 2: It's not showing the pull request, just the push.
Speaker 3: Does it show pull requests?
Speaker 2: I don't know.
Speaker 3: Hmm. I don't think it does.
Speaker 3: Just the commits.
Speaker 2: Just the commits. Okay.
Speaker 3: Because these are the changes which happened to the.
Speaker 2: Right. Right. Right. Right. So this doesn't change. It changes happen and then they get pushed.
Speaker 3: Hmm.
Speaker 2: To this, and then you just I think it committed. So that's how you and I are both synchronizing it.
Speaker 2: And according to Claude, since we don't do it that often, there's very little risk of us both overriding each other's.
Speaker 3: Hmm.
Speaker 2: Commits.
Speaker 2: And if there is, it will tell you that you're both editing the same line at the same time.
Speaker 3: Hmm.
Speaker 2: So I think it's okay.
Speaker 2: Well, what's the other one? If you go up to all the other list.
Speaker 2: Of go back to Janice, the has primary ADNs. What else do we have in the what other repos do we have here now? Go back one more. Okay. So this is the one we looked at. Per oh, your personal one is here.
Speaker 3: Hmm.
Speaker 2: But it's empty.
Speaker 2: Oh, no. It's not.
Speaker 3: That's a template. That's the enrollment.
Speaker 2: It's just a template. I don't think it's, it's enrollment. I don't think it's actually got any I don't think you're syncing with it 'cause otherwise, it would say HTML. See?
Speaker 3: Hmm.
Speaker 2: I, I think the folders are empty.
Speaker 2: They just have a README in there.
Speaker 2: Click in.
Speaker 2: Oh, no.
Speaker 2: They're full. They're populated.
Speaker 2: Hmm.
Speaker 2: But that was 16 hours ago. Okay.
Speaker 2: Anything more recent?
Speaker 3: Yeah. This one.
Speaker 2: Sources 30 minutes ago.
Speaker 3: I'm not sure updated just now.
Speaker 2: Okay.
Speaker 2: Hmm.
Speaker 2: So it is receiving?
Speaker 2: And the rest are all bootstrap and templates.
Speaker 3: Hmm.
Speaker 2: And AI skills library. Just the other one. So that's where you got stand-up and everything on AI skills?
Speaker 3: Yeah.
Speaker 2: Okay.
Speaker 2: Hmm.
Speaker 2: Yeah. It says updated 22 minutes ago on the personal one.
Speaker 2: So it seems to be working.
Speaker 3: Yeah. But I have to run it manually.
Speaker 2: Oh. Okay.
Speaker 3: I run it personal and AI.
Speaker 2: Ah, that's because you did the pu okay. So the automatic GitHub sync.
Speaker 3: Yeah. Because I can't access our the GitHub.
Speaker 3: It doesn't even have a plugin for it, so. The pushes have to be done manually. That's the problem.
Speaker 2: That's the problem. That's the problem.
Speaker 2: So you can only do.
Speaker 3: Our ap-upon the cron job. The cron job's gonna do it, but it's, like, once a day. It's gonna be around, like, 3:00 PM or something.
Speaker 2: Yeah. Once a day is okay.
Speaker 2: So for the personal one, you'll use a cron job.
Speaker 3: For personal?
Speaker 2: The yeah. The,  the personal sync has been done through a cron job on your personal vault.
Speaker 3: No. Personal and the company are done by cron job.
Speaker 2: Oh, okay.
Speaker 2: But so, but I thought the per company one is using the plugin.
Speaker 3: Yeah. Now I got to use the plugin, so.
Speaker 2: Oh, okay. Okay. So plugin now is working every five minutes.
Speaker 3: Hmm.
Speaker 2: Okay.
Speaker 3: But for the other people, I feel it's g it's just easier if we just make it one fail well, it start crashing.
Speaker 2: Oh, shit.
Speaker 3: Pull everything is up to date. Push is not working.
Speaker 2: Okay.
Speaker 2: Maybe.
Speaker 3: Hmm. Mm-
Speaker 2: Maybe just remove it.
Speaker 3: Hmm.
Speaker 2: You know.
Speaker 2: And, and there goes the other one. Let's see if that works.
Speaker 3: So the other for the company, I'm thinking it's not do personal and company. Let's just push it everything in the in the.
Speaker 2: Cool.
Speaker 2: So that's how the personal and the company one for the yeah.
Speaker 3: 'Cause they're, they're, like, the department knows what the other person is working on.
Speaker 2: I think so. I, I, I, I, I, I agree.
Speaker 3: There's nothing personal.
Speaker 2: I don't think the personal one adds more. I know one venture was saying we should add one, but I'm thinking about it some more.
Speaker 3: Hmm.
Speaker 2: What would you have in your personal one that's not in the group one?
Speaker 3: Nothing.
Speaker 2: Nothing. Right?
Speaker 3: Just add more complexity to what we're working on and, and.
Speaker 2: And confusion.
Speaker 3: Yeah.
Speaker 2: Confusion.
Speaker 3: Yeah. Ye  Yeah. I'm confused. I got this.
Speaker 3: You are confused. We're I'd say we're pretty technical.
Speaker 3: Like, it's, it's just adding more confusion to us. Imagine to the other people. So we don't need to enroll them. And plus, we now have this get issue with the Obsidian, so we're.
Speaker 3: Yeah.
Speaker 2: We can't.
Speaker 3: So let's focus for now on just the department-level ones. Later, we can yeah.
Speaker 2: I agree.
Speaker 3: And then we can clarify when he's back from holiday with one venture and think about the personal one.
Speaker 2: Yes, we can do it, but, but is it really personal? It's your employee one. It's not, like, a personal one as in private. If you wanna run a personal one, you can do it in your own home computer.
Speaker 3: Hmm. Exactly.
Speaker 2: On other things.
Speaker 3: Yeah.
Speaker 2: That are not work-related.
Speaker 3: Hmm.
Speaker 2: But if they were work-related stuff, it doesn't—  Maybe the idea maybe let's just give it time. But for the time being, to keep it simple, let's just do the group ones: marketing, AI office, project management, IT.
Speaker 3: Hmm.
Speaker 2: And leave it at that and just make sure that multiple users are able to synchronize and run it. Use GitHub. We'll figure out the federation. How if there is any level of cross-pollinization.
Speaker 2: Yeah. 'Cause  'Cause I'm thinking it's not it's not just federation. It's not just sharing the knowledge between ourselves. Because if you think about it, if we're both going to be in the same meeting, with IT, their system is gonna be recording the same meeting as we have. So they will come to do similar conclusions, you know, do, do we need that level of synchronization or do we each reach some other conclusion of what? But the thing that is also interesting conceptually for me to look at is cross-pollinization between different departments, which happens in the real life. It happens through chance encounters. You know, sit there, you're talking to somebody in finance or with coffee, and in the cafeteria, and they're saying, "Oh, I got this problem. I'm trying to figure out," and, you know, the engineer sits on this and says, "Oh, well, I can fix that for you." And then that becomes an idea. Which then suddenly becomes a solution to something. And, you know, in the old days, when the, the companies used to have research labs like Bell Labs and all these famous labs, IBM, Watson labs, that cross-pollinization between say a physicist and a chemist very often, that's how things like the transistor got invented, right? This stories about that. You know, Steve Jobs at Pixar, intentionally designed Pixar so that the central area required everybody from different departments of the engineering, the people that were doing the software, you know, the, the, the computer graphics, the storyboard, the artists, they all had a they all would bump into each other randomly.
Speaker 3: Hmm.
Speaker 2: And ideas were shared between different disciplines.
Speaker 3: Yeah.
Speaker 2: And one, one, one nice side effect as we collect all this stuff is we can kind of recreate that cross-pollinization process.
Speaker 3: Hmm.
Speaker 2: But right now, I think let's not get too ahead of, you know, let's not get over our skis a bit too far. Let's focus on just getting the department-level one working reliably and consistently. Then we can start adding these bells and whistles later.
Speaker 3: Yeah.
Speaker 2: But I think we're trying to push on too much onto it, and, and getting ourselves confused.
Speaker 3: That's right.
Speaker 2: It's getting everyone confused, I feel.
Speaker 3: Hmm?
Speaker 2: It's getting everyone's confused.
Speaker 3: Yeah.
Speaker 2: Like, let's work on that. So personal becomes a department.
Speaker 3: Yeah.
Speaker 2: So there's no separate personal and a department. A personal becomes a department.
Speaker 3: Well, multiple people become a department, but AI office is the two of us.
Speaker 2: No, I mean, like, Obsidian and Vault. I'm talking.
Speaker 3: Oh, oh, yeah, yeah.
Speaker 2: Obsidian and Vault, personal becomes a department.
Speaker 3: Oh.
Speaker 2: Yeah.
Speaker 3: It's so fatal. You're still getting errors now.
Speaker 2: I don't know.
Speaker 3: Another Git process. Shit. Maybe just.
Speaker 3: Close it and reopen.
Speaker 2: Yeah. Subs  Subscribe.
Speaker 2: Yeah, anything.
Speaker 3: Maybe just needs to reset.
Speaker 3: Hmm.
Speaker 2: Okay. I'll work on this then.
Speaker 3: Okay. Yeah. Let's go back.
Speaker 2: I'm not gonna make two separate Obsidian. I'll just make it one and push that to GitHub.
Speaker 3: Yeah.
Speaker 2: It'll create the user. So we can still have access to what who's done who and what and what happened to, to this.
Speaker 3: Right. For marketing, it'll be Andrew, and yeah.
Speaker 2: Hmm. And since meetings and all of that, one person is recording, so recording is gonna be, like, pushed in there. Well, whatever everyone is working on, that becomes the knowledge of the department. That's why a personal becomes a department.
Speaker 3: Yes. Exactly.
Speaker 2: Instead of separate things. Instead of pushing from personal to department and department to.
Speaker 3: That makes it too complicated.
Speaker 2: Yeah.
Speaker 3: I agree.
Speaker 2: I agree.
Speaker 3: Okay.
Speaker 2: So let's, let's go with that.
Speaker 3: All right.
Speaker 2: Construct for now.
Speaker 3: Yeah. Just a department level.
Speaker 2: Yeah.
Speaker 3: And then after Andrew, once we get all that him working and let's focus on the content and making sure that it's all organized and.
Speaker 2: Mm-
Speaker 3: Accessible and.
Speaker 2: Yeah.
Speaker 3: And lack of, you know, you know, you know. And then, and then we can you know, at least start the pre the project management, but let's wait. Let's not fully deploy that until we get Andrew up and running.
Speaker 2: Hmm.
Speaker 2: And at least we can fix this issue because once, like, it can re it can write to the local. Yeah. Vault. I  Vault. I mean, the standalone can write to the local Vault and the local Vault already have a Git, which is pull and push. So we don't even need to use this anymore. Manually, so.
Speaker 3: No, you got it.
Speaker 2: It'll automatically be there.
Speaker 3: Yeah. It'll automatically do the pull and push. Exactly.
Speaker 2: Yeah. Yeah.
Speaker 2: My thinking too.
Speaker 3: Okay. Let's go with that. For  For today.
Speaker 3: Yeah.
Speaker 2: Yeah. We may I need to finish the standalone the enrollment because this one okay.
Speaker 2: Let's take a little bit of time.
Speaker 2: I need to think about a copy because I don't like to enroll something, which is—  Well, the first thing is enrollment, which is setting up the basic structure. Second step is plug it into all the data sources. So there's gotta be a enrolling the user first, but also enrolling all the data sources. So how do you begin populating this thing and doing the first pass?
Speaker 2: And when it creates the, the GitHub repository, is it gonna create it on its personal on their personal?
Speaker 3: No, the group one. The company one.
Speaker 2: How are we gonna link it, though?
Speaker 3: Same way. You add users. That's what I did with us. So I created it on the personal one. If you go back to the GitHub, that's why your name shows up there.
Speaker 2: I need to send the send them an invitation and accept it.
Speaker 3: First of all, they need so okay. Yeah. They need a GitHub account.
Speaker 2: And I need to send them to join their organization.
Speaker 3: And then and I would say that for Andrew and those guys, put there's also a parent organization dot com.
Speaker 3: So if you look at the way it's set up because I set up too. I set up in dot IO and a dot com.
Speaker 2: Hmm.
Speaker 3: And once you have an account, you can add to the you can have contributors. I mean, this is how open source works, right? You can add anybody you want.
Speaker 2: Yeah.
Speaker 3: And then, you know, my dog had an account. I could put her in there too, right?
Speaker 2: Hmm.
Speaker 3: So, so all you're doing is you're adding so it's a private repo. It sits in Janice I Janice com.
Speaker 2: Hmm.
Speaker 3: For the rest of the company.
Speaker 2: Mm-
Speaker 3: Right? Now that we're gonna do that because we wanna be careful about not putting people who are not in our work in IO. And then once they have their personal account, you invite them in as in your case, I so you could what, what we could also do is create a group.
Speaker 2: Hmm.
Speaker 3: So if you go to GitHub repo.io for AIO, you'll see through so there's a group. So you can create a group of users. You can invite the group to have access to it. So I gave the group only limited access.
Speaker 2: Hmm.
Speaker 3: And then for you and me, I, I set us up as admins.
Speaker 2: Hmm.
Speaker 3: So again, w-we should have admin because we, we need to manage these GitHubs. So to.
Speaker 2: Admins and all that.
Speaker 3: But then the group so for example, I wouldn't give Andrew or Rosa and Lysander for their respective so they all need to get their own accounts. And then you add them to the shared repo with whatever privileges you need. And that's what CloudWalker threw yesterday, so.
Speaker 2: Hmm.
Speaker 3: It's like set up a group of all the members in that. So first, get them their own accounts. Hmm. On GitHub, right?
Speaker 3: Which should be on their Janice deep dot com email address. But you've got that. Then once they've done that, create the shared.
Speaker 3: Repo on the and populate it, right?
Speaker 3: Um, quick thinking. And, and you got there's a little bit of tweaking. You got to branch because there's main and default. So I, I, I have to do again, Cloud walked me through it. I think it's in that appendix. If not, we can try to recreate what I did yesterday.
Speaker 2: Mm-
Speaker 3: But there were little fiddly things I had to do. Like, it said the branch I had to create it with a particular name. And then I had to add the users. In a group. And then I realized, "Oh, but I don't want everybody in the group to be able to have admin." So just write access because I know there's a layers of permissions.
Speaker 2: Yeah.
Speaker 3: So then for full admin, I put both of us. So that's why you're seeing marketing,  AI office group, which is still the two of us, but we're also admins in the individually.
Speaker 2: Mm-
Speaker 3: So then you have to create so you basically managing the membership of who has what access to that particular repo, which is living in the Janice deep dot com.
Speaker 2: Hmm.
Speaker 3: Uh, organization.
Speaker 2: So it's like one repo is gonna have subfolders? Each folder for, like, departments or?
Speaker 3: No, no, no. Each department gets get its own top-level repo.
Speaker 2: Repo. Oh, okay.
Speaker 3: Wh-which mirrors the directory structure.
Speaker 2: Okay.
Speaker 3: Right?
Speaker 2: Yeah.
Speaker 3: So marketing will get a repo. Similar to what we have. Product management will get a repo.
Speaker 2: Hmm.
Speaker 3: And then within that, each one gets different set of. Hmm. Access. But beca  Access. But because we're setting it up, you and I so you and I should have admin because we'll, you know, we, we need to configure it.
Speaker 2: Yeah.
Speaker 3: And then we have then we add those users, which gives them the permission to push and to commit and pull.
Speaker 2: Hmm.
Speaker 2: Yeah.
Speaker 3: That's all they need. And once they've got the commit and pull, you then, like we then link it to the Obsidian install install the Git plugin, community plugin. And then it's all gonna sync up.
Speaker 2: Yeah.
Speaker 3: So the question is, where do we start? Do we so what I did, you know, we, we did the first push, which is the initial population of it, I did it from because I already had a directory on my.
Speaker 2: Hmm.
Speaker 3: Um, I actually used the one so what I did is I took the Google shared one. I copied every oh, and you also gotta do a Git ignore. You gotta edit the Git ignore. And then because there's some files, you don't want to be pushed there because they're the hidden files. Hmm.
Speaker 3: You know, the.
Speaker 2: Credentials as well.
Speaker 3: Cred yeah. So there's some you want to make sure that they don't push get pushed to Git ignore. So I think it's already there. I'll check it.
Speaker 2: I'll check it.
Speaker 2: Ours is. Our Git ignore.
Speaker 3: Our Git enrollment because the enrollment does follow the same structure.
Speaker 2: Yeah. But if you go back to what I did, it did it created this massive bash script.
Speaker 3: That should be doing everything that I just described. I asked Cloud to do that, but I didn't check it.
Speaker 2: Hmm.
Speaker 3: And they wanted to get a look at it. But we wanna automate this. So what I'm guessing is we do is create a bash script that does everything in the local drive to create the empty folders and then it'll do the because you can go using the GH command line.
Speaker 2: Hmm.
Speaker 3: GitHub. And it will it does whatever it needs to do.
Speaker 2: Hmm.
Speaker 3: But I wanted to automate it because there was so many stupid little steps.
Speaker 2: Oh, yeah.
Speaker 3: That I had to do, like the creating the users and the set of the set of so I asked it. I said, "Look, you've got the history of what you asked me to do." And I did everything. Now stick it all into a big script. So it's automated as much as possible. So we just run the script.
Speaker 3: Kinda like you NPM something, right?
Speaker 2: Hmm.
Speaker 3: So but I, I didn't debug it yet.
Speaker 2: Oh.
Speaker 3: It, it did the dump. I think it's in that folder. If you're not, I'll I, I, I think I sent it to you and.
Speaker 2: Yeah. I sent it. I'll check it today.
Speaker 3: Yeah. In Slack.
Speaker 2: I'll check it.
Speaker 3: Check it today. And play with it. Improve on it. I'm sure it's got many things that I missed. But you're better at this than I am, so.
Speaker 3: I'll give you the first, first passage. You clean it up and sort of catch anything I might have missed.
Speaker 3: All right. Well, not the Cloud might have missed, but it was generating it.
Speaker 2: Hmm.
Speaker 3: But it's but it's a useful thing. I'm sure that you do the same thing. You have to I but after a very long conversation where you're setting and configuring stuff, save the damn thing.
Speaker 2: Yeah.
Speaker 3: Because otherwise, going back and seeing, "Oh, what did he tell me to do? Just, just create something." It's, it's a good habit to get into. So Rosa was asking about yesterday.
Speaker 3: How do we take long conversations with lots of it.
Speaker 3: Iterations and interaction stuff and then just encapsulate this is the final.
Speaker 2: Oh.
Speaker 3: This is the recipe.
Speaker 2: Yeah.
Speaker 3: Yeah.
Speaker 2: I mean, it's either like enrichment or handoover.
Speaker 3: Yeah. So  So for me, I, I do this when I'm using Cloud code. If it's here.
Speaker 3: Yeah. Yeah, yeah, yeah.
Speaker 2: About times, you see.
Speaker 3: Yeah. There it is.
Speaker 2: Oh, yeah. This one.
Speaker 3: Yeah.
Speaker 3: What's in the handoover exactly?
Speaker 2: So you tell them to do a h-handoover, especially when I'm about to hit my limit.
Speaker 3: Hmm. Oh, the handoover to a new thread. Yeah.
Speaker 2: Yeah. They'll take that as a handoover from the previous employee and.
Speaker 3: Yeah. I, I do the same thing as well. I don't call it handoover, but same concepts. I, I, I call it save state.
Speaker 2: Yeah.
Speaker 3: And load. It's, it's kind of like it goes.
Speaker 3: Back to my computer architecture days, you know, like, like, like you save the state of the machine and then you can bring it up in another. Hmm. Install Ob  Install Obsidian Git plugin in personal plus area office fold one time, two minute each.
Speaker 2: Oh, okay.
Speaker 3: Okay. Oh, that was a lot of work.
Speaker 2: Hmm.
Speaker 2: I need to work on it then.
Speaker 2: Push this drive I/O.
Speaker 3: Oh, content. What is this?
Speaker 3: Okay. Uh, this was a long and painful one.
Speaker 3: It had to be done.
Speaker 2: Hmm.
Speaker 3: Uh.