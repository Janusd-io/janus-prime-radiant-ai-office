# AIO 11 May

**Meeting Date:** 11th May, 2026 - 11:38 AM
**Attendees:** Michael Bruck, Jehad Altoutou (full session); Brett (brief mid-meeting appearance, ~01:08).

> **Note on attribution (added 2026-05-11):** Fireflies' automatic speaker diarisation misattributed a number of comments in this transcript — specifically, statements made by Michael Bruck were tagged as Jehad Altoutou and vice versa. To prevent downstream synthesis from inheriting these errors, all speaker markers in this transcript have been collapsed to `**Speaker**` (unattributed). The conversational structure is preserved by line breaks; specific attribution should not be inferred from this transcript. Where downstream wiki pages reference statements from this meeting, they should frame them as "the meeting concluded that…" or "in the standup it was discussed that…" rather than naming a specific speaker.

---

**Speaker** *[00:01]*: Yes, actually. And I have an email. 
**Speaker** *[00:06]*: Let's get the recording up, and I've got a bunch of stuff to go through, and I'm sure you do too. 
**Speaker** *[00:11]*: Yeah, same. 
**Speaker** *[00:13]*: Yeah. 
**Speaker** *[00:15]*: Okay. Fireflies is on. 
**Speaker** *[00:17]*: Good. Okay. 
**Speaker** *[00:18]*: Just so what you got. So I'm going to enroll Simon, for the, Obsidian. Graphify Obsidian. I'm going to create his digital brain today. 
**Speaker** *[00:33]*: For Simon? 
**Speaker** *[00:34]*: For Simon. 
**Speaker** *[00:35]*: Oh, okay. 
**Speaker** *[00:36]*: Today, hopefully. He was asking me in the morning that when like, if it's possible that we can do it today. 
**Speaker** *[00:43]*: What's he going to use it for, though? 
**Speaker** *[00:45]*: I have no idea, but I was like, "It's fine. Let me." Let's check a little bit. I mean, I just want to make sure that he's knows what he's doing. He's not that technical. He doesn't know? That's why he was Because you do need cowork. You need a local folder. It can interface with. 
**Speaker** *[01:53]*: Let me try it out. 
**Speaker** *[01:54]*: Yeah. I'll try it just. He doesn't have cowork? 
**Speaker** *[01:56]*: He—I don't think he has Claude to begin with. 
**Speaker** *[02:00]*: No, he does. He has Claude. Yeah. Okay. Yeah. 
**Speaker** *[02:02]*: I'll just try it on Java. 
**Speaker** *[02:03]*: He's got him Claude because he's doing all these PowerPoints in Claude. That's why he's been burning through tokens with a frightening rate. Given that most of his presentations are output only, he should be creating all that material using HTML. 
**Speaker** *[02:16]*: Mm-. 
**Speaker** *[02:16]*: It's way cheaper. But people don't know these kinds of things. I think when the training person comes, you have to start thinking about, you know, best practices, like— Yeah. People just out of habit have a tendency to always use the existing tools, Word and PowerPoint, but Claude and—I mean, it's a very clever anthropic that they support these tools. And of course, they're very happy because it uses up a lot of tokens. So for them, it's very good. But they're not the most efficient surfaces to write to. 
**Speaker** *[02:42]*: So what—what I was thinking, which I'm deploying—I don't know if I'm going to do it. Mm- But still, I'm thinking about it. 
**Speaker** *[02:49]*: Mm-. 
**Speaker** *[02:49]*: So the cron is going to be a shell command. Mm- Which is going to be running on the back end, on the backside, like. 
**Speaker** *[02:55]*: Cron for what? 
**Speaker** *[02:56]*: For Obsidian. 
**Speaker** *[02:57]*: Okay. 
**Speaker** *[02:57]*: Every day. 
**Speaker** *[02:58]*: Oh. 
**Speaker** *[02:59]*: On—at night, it will just fetch everything. And send it to Obsidian. So the idea is we're going to have either a repo on GitHub, either we send all of this information, all of these vaults in there. Mm- U each person is going to have the same profile as mine, like his name, what he does, all of this information, and everything, the skills, the projects, the documents. Literally, everything is going to be inside. 
**Speaker** *[03:25]*: So you—you—you're looking at this as building everybody's personal? 
**Speaker** *[03:28]*: Vault and then. 
**Speaker** *[03:29]*: Vault first, not the group one that—that we're doing for us. So this is the personal one? 
**Speaker** *[03:34]*: This is the personal one. 
**Speaker** *[03:35]*: Oh, okay. 
**Speaker** *[03:35]*: For them. 
**Speaker** *[03:35]*: Okay. 
**Speaker** *[03:36]*: For now. 
**Speaker** *[03:36]*: Okay. 
**Speaker** *[03:37]*: So what I'm seeing here, like. 
**Speaker** *[03:38]*: Yeah. 
**Speaker** *[03:38]*: On the horizon, each one has his own vault. Each vault is sent on—on GitHub. At the end, we will just either I'll develop something that it will fetch all of these vaults, create one main, company-wide. 
**Speaker** *[03:55]*: Mm- Mm-. 
**Speaker** *[03:56]*: And we use it on that for the CEOs and everything. If, let's say, the CEO is, like, comfortable with it or whatever it is, we can then enroll it. 
**Speaker** *[04:07]*: Yeah. Because I'm—I'm—I'm thinking about having three, like, layers of—of—of—of knowledge. One is your personal. Mm-. Like, you've done for yourself. Mm-. The next one is department level. Mm-. Like, the one on experimenting with us last week, and I'm going to try it with Andrew. 
**Speaker** *[04:21]*: Mm-. 
**Speaker** *[04:22]*: And then, you know, we move on. Maybe the next one is we use Euclid's IT group and so on and so forth. And then ultimately, as we have all these different systems at the department level, we roll them up into a company-wide one, you know. 
**Speaker** *[04:36]*: Mm-. 
**Speaker** *[04:36]*: Or maybe I do Joyce, but we have to think about—so I'm going to use—but on the individual one, I think it's quite different. proposition. 
**Speaker** *[04:46]*: Mm-. 
**Speaker** *[04:46]*: So clearly, you've done a very cool one for yourself. I'd like to try one for myself too. And. 
**Speaker** *[04:50]*: Mm-. 
**Speaker** *[04:51]*: How to maintain those as two separate vaults is—is kind of. 
**Speaker** *[04:55]*: Yeah. 
**Speaker** *[04:55]*: Interesting. And—and then the other part of it on the—on the shared one is I've already created a shared, folder on our shared drive in the Google Shared Drive, which you have access to. 
**Speaker** *[05:09]*: Mm-. 
**Speaker** *[05:10]*: So one of the things I want to do when we finish this call is I want to try to see if you can tweak our skill for the standup in addition to writing to Notion. Let's keep that alive still, but also write a markdown to the inbox. 
**Speaker** *[05:24]*: Okay. 
**Speaker** *[05:25]*: On the shared one, because that becomes—because right now. 
**Speaker** *[05:29]*: Mm-. 
**Speaker** *[05:29]*: I've—I've been pulling this stuff for the group, our group, wiki, out of Notion. 
**Speaker** *[05:35]*: Mm-. 
**Speaker** *[05:36]*: But there were a bunch I found were missing. And that month, April was actually—it's—I'm going to see if I can find those transcripts. You have some. I have some. The reason is that was when you were getting started. So there's a lot of good knowledge in there. 
**Speaker** *[05:47]*: Mm-. 
**Speaker** *[05:48]*: In our conversations in your first month here. Which are why we do things the way we do. And were developing a lot of the methodology, which now we've taken more into production. 
**Speaker** *[05:56]*: Mm-. 
**Speaker** *[05:57]*: During—so I think that first month, especially, has a lot of decisions that we made and stuff. I—I—I don't want to lose that. 
**Speaker** *[06:03]*: Yeah. Yeah, yeah. 
**Speaker** *[06:04]*: Right? And it's for whatever glitch we had a glitch, and it just—it deleted all these summaries out of Notion. So the best way is to recreate it is just to go back to the transcripts and tell it. It's a one-time thing. Capture all the knowledge. Mm-. When we bring somebody new on board, that stuff will be very—and then because I—I don't think our knowledge base at the group level, at our department level, is complete without that first month. 
**Speaker** *[06:27]*: Mm-. 
**Speaker** *[06:28]*: So that's one thing I want to do. But I think it would be within that framework, let's try also within the standup skill, what—whatever it writes to Notion, write a markdown version of that. 
**Speaker** *[06:41]*: Yeah. 
**Speaker** *[06:41]*: To the inbox, which. 
**Speaker** *[06:42]*: Yeah. 
**Speaker** *[06:42]*: You usually. 
**Speaker** *[06:43]*: But we need to keep it as a—I'm thinking what kind of section we need to create it for that specific thing. Because in—in Obsidian, because the markdown is going to be saved in Obsidian. 
**Speaker** *[06:55]*: But if you go to—if you go to, Drive, right, open—open your Drive. You should see— Okay. How come Drive's not doing shared folder? Oh, it's going to be not—oh, yeah, you got to go to Janice IO. How come IO's not there? 
**Speaker** *[07:25]*: Oh, wow. So many errors. 
**Speaker** *[07:28]*: I was thinking. Just go to the regular one. But you're not in Janice IO. You're under wrong account. 
**Speaker** *[07:40]*: Dot com? 
**Speaker** *[07:40]*: No, dot IO. 
**Speaker** *[07:42]*: This is dot IO. 
**Speaker** *[07:43]*: Oh, this is it. Okay. 
**Speaker** *[07:44]*: Oh, let me see. Dot com. 
**Speaker** *[07:45]*: Go to shared drives. 
**Speaker** *[07:46]*: This one? 
**Speaker** *[07:46]*: No, shared. 
**Speaker** *[07:49]*: Oh, isn't it this one? 
**Speaker** *[07:49]*: Oh, yeah. Oh, it's that one. Yeah. Yeah, there you go. So that's the vault for the Claude MD. So that's a vault that both the Claude cowork is pointing to. And Obsidian. So if you open that vault in your Obsidian, you'll see exactly the same we can share I want to see if that works. 
**Speaker** *[08:10]*: And if we updated. 
**Speaker** *[08:12]*: The web clipper was a pain in the ass to get it to point to the right directory, but it finally got it to work. Obsidian. 
**Speaker** *[08:18]*: And if we update— So I think if you push the N our standup into. We need to push it to the cloud. 
**Speaker** *[08:27]*: Push it into inbox. Inbox, it's empty, except what's been processed. So inbox is—so what I do, a web clip, or if I do everything, it goes first to inbox. 
**Speaker** *[08:38]*: Mm-. 
**Speaker** *[08:39]*: And then the reason inbox is good is because you could put a PDF in there and—and Claude itself will parse it and turn it into the right markdown and put it according to Claude MD into the right directory structure. 
**Speaker** *[08:50]*: Mm-. 
**Speaker** *[08:50]*: So it'll process that. It'll determine where it should fit. And then it'll populate the appropriate and—and—and make all the connections through that. 
**Speaker** *[09:01]*: Mm-. 
**Speaker** *[09:01]*: And Obsidian will still see it because it goes into the right directory. It goes from inbox to—so the flow is most of the time it's just a web clip that I use Obsidian web clipper. It puts it in there in markdown. 
**Speaker** *[09:15]*: Mm-. 
**Speaker** *[09:15]*: But you can also—I asked Claude. I said, "What if it's PDFs?" It's fine. I can just parse it and analyze it. So Claude will—you could put a PowerPoint in there. Anything Claude will always—whenever you run that skill. 
**Speaker** *[09:28]*: Mm-. 
**Speaker** *[09:29]*: Which is called ingest. So I said, you know, there's more data because it's batch mode. It's not doing it constantly. I will ultimately put it on a cron, which you can do inside of Claude. You can actually do a schedule, right? If you go to. 
**Speaker** *[09:42]*: Yeah. I tried it. I tried that one, but it wasn't the greatest I felt. 
**Speaker** *[09:46]*: Yeah. Ultimately, I want to move this to a standalone thing so. 
**Speaker** *[09:49]*: Because see, when on scheduled, you'll have to—like, let's say new task, you have to give it a name, description, and, like, work in project. You can't. 
**Speaker** *[09:57]*: Work in project is okay. Because you give it the—you need to create a project. So it has—so in my case, I don't have my computer with me, but in my case, I've created a project, which is the LLM. 
**Speaker** *[10:08]*: But the problem—not everyone has cowork. 
**Speaker** *[10:10]*: Oh. That's the thing. That's—so, so longer term, like with Android, I'm going to try this. I'm going to see—get this thing up and running without needing cowork. 
**Speaker** *[10:21]*: I don't want to have working on. 
**Speaker** *[10:23]*: Oh, you are. Okay. So we need to build a piece of software. Web frontend. 
**Speaker** *[10:27]*: Mm-. 
**Speaker** *[10:29]*: API into Claude, with all the capabilities that we have in cowork. But I've—but—but ported over so it's API-based. 
**Speaker** *[10:37]*: Mm- That's the—that's the. 
**Speaker** *[10:39]*: And then everybody—anybody can have that. So they don't need cowork. 
**Speaker** *[10:42]*: That's the idea I want to try out with Simon. 
**Speaker** *[10:44]*: Okay. B Because as a skill, I just hope it works. I was just going to say, in terms of time and resources, maybe we do Andrew first. Because I think he has a greater need. 
**Speaker** *[10:54]*: Mm-. 
**Speaker** *[10:55]*: Simon, I think, is doing it because he's just kind of curious. I don't think he has a—enough understanding to know what it's for. And I'm worried he's just going to be wasting his time on it. 
**Speaker** *[11:03]*: Mm-. 
**Speaker** *[11:04]*: I—I—I'm not seeing the value add. But Andrew, he definitely needs it. Like you heard, he says, "Can we have it by Thursday?" Mm-. He—he needs that. And he needs a CRM. 
**Speaker** *[11:13]*: Mm-. 
**Speaker** *[11:14]*: Because then—so I would say, let's use Andrew as our test case. And put Simon in the back burner for now. 
**Speaker** *[11:20]*: Mm-. 
**Speaker** *[11:21]*: Until he's got a clear—clearer, use case. For how he's going to use it. 
**Speaker** *[11:27]*: Okay. 
**Speaker** *[11:27]*: Okay. And for the personal wiki, let's—you and I play around with it some more before we roll this thing out too many people. 
**Speaker** *[11:35]*: Mm-. 
**Speaker** *[11:35]*: Because I'm just worried they're going—they're not going to know how to use it. And then it's going to take your time to train them and explain to them. And so I—I—I don't think we should put them on this yet. 
**Speaker** *[11:48]*: Well, I don't think we need any training for it, except, like, the—the surface. Because at the end, I'm thinking about just—it's an enrollment. We just download the skill. Mm- And it already has a cron job. Oh, it's going to run a shell command. It's going to be in the background of the—of the PC, you know, the management system. 
**Speaker** *[12:07]*: Mm-. 
**Speaker** *[12:08]*: And it's going to run it daily. They don't have to. I'm thinking about. 
**Speaker** *[12:11]*: But where is it going to source all the information from? Their own transcripts? 
**Speaker** *[12:15]*: From— that's what I wanted to ask you. Shall we add Notion and Fireflies? 
**Speaker** *[12:21]*: Fireflies, yes. Notion, not yet. Because Notion isn't—is not yet approved. 
**Speaker** *[12:25]*: Because if we're going to. 
**Speaker** *[12:26]*: Broader company is. 
**Speaker** *[12:28]*: If we're going to give them. 
**Speaker** *[12:29]*: Because we only have a Notion account. Our IO account. And I'm not adding anybody after Bonaventure said nobody gets—we don't have a Notion and JaniceD.com. In fact, I just had to pay our Notion bill. 
**Speaker** *[12:39]*: Oh, okay. 
**Speaker** *[12:39]*: So it's not the free version. 
**Speaker** *[12:41]*: Mm-. 
**Speaker** *[12:41]*: So we don't—you know, Euclid does not support Notion for company-wide yet. I think Andre has a copy, but he's using it. I don't know. I think it's his personal. 
**Speaker** *[12:50]*: Oh, the free version. 
**Speaker** *[12:51]*: So it's—so it's really not a sanctioned tool yet. 
**Speaker** *[12:53]*: Mm-. 
**Speaker** *[12:54]*: So I just want to be careful about tool sprawl and—and how we keep it—keep it sort of siloed for ourselves. So—so. So keep. Maybe hold off with—with Simon for now. 
**Speaker** *[13:06]*: Okay. I'll tell him then to—in case he wanted to enroll it, I'll tell him to check with you first. 
**Speaker** *[13:12]*: Yeah. 
**Speaker** *[13:12]*: Because today he came to me. He was like, "Can we use it?" and stuff like that. 
**Speaker** *[13:16]*: Yeah. Like, because he saw it in use. But I—but—but—but I want to make sure that he knows what he's signing up for. 
**Speaker** *[13:22]*: Mm-. 
**Speaker** *[13:23]*: And I want to understand that better with him. I mean, how is this going to help his. 
**Speaker** *[13:27]*: His department or his work. 
**Speaker** *[13:29]*: Exactly. How is it going to help him? I think people need to have a stronger use case of, "Oh, I just want to play with it and learn how to use it." Mm-. You know? 
**Speaker** *[13:37]*: I also enrolled the, ISO. It's Janice Pulse onboarding. Mm-. People will have—like, it's a skill, you can say. 
**Speaker** *[13:50]*: Mm-. 
**Speaker** *[13:50]*: Just into Claude. Get cron, all of this. It's going to download all of these references, the skill with the prompts, references, templates, and all of these. 
**Speaker** *[13:59]*: Mm-. 
**Speaker** *[14:00]*: It'll have around 22 reference. 
**Speaker** *[14:03]*: So this is what people will use to create those ISOs. 
**Speaker** *[14:07]*: The ISO. 
**Speaker** *[14:07]*: Sure. 
**Speaker** *[14:08]*: Yes. 
**Speaker** *[14:08]*: It flows and all of that, so. 
**Speaker** *[14:09]*: Well, everything. Literally everything. 
**Speaker** *[14:11]*: Okay. Okay. 
**Speaker** *[14:12]*: Once they install it, where is it going to be? 
**Speaker** *[14:16]*: Mm-. 
**Speaker** *[14:17]*: Mm-. Why it doesn't have? 
**Speaker** *[14:22]*: But I'm thinking installing. 
**Speaker** *[14:29]*: So once they install it, Claude will ask them, "What's your department and your name?" Mm-. Once they enroll that, it's going to ask them. 
**Speaker** *[14:36]*: But what do they need for this cowork? Or is it going to be? 
**Speaker** *[14:39]*: Hopefully, it's— What do they need for running? Hopefully, a normal chat will do. Because it's just a skill. 
**Speaker** *[14:50]*: Okay. 
**Speaker** *[14:50]*: And all of them are markdowns, files. So it doesn't really take any resources or anything. 
**Speaker** *[14:55]*: Mm- Mm- Okay. If—if—if it can be done. But—but again, I guess we need this. 
**Speaker** *[15:07]*: And it'll have the AI, what we've built already for the ISO. 
**Speaker** *[15:11]*: Mm-. 
**Speaker** *[15:11]*: As a—as a template. 
**Speaker** *[15:12]*: Mm-. 
**Speaker** *[15:13]*: So everything we spoke about, they seemed happy with it. So we're going to enroll this much. 
**Speaker** *[15:19]*: Okay. 
**Speaker** *[15:20]*: In case there's any. 
**Speaker** *[15:21]*: Who do you want to try next on this? Who's the Euclid team? 
**Speaker** *[15:24]*: The—the thing. I want to—which one you—you prefer? Shall we send it to Euclid? 
**Speaker** *[15:29]*: Yeah. Yeah. Make—let—let. 
**Speaker** *[15:31]*: Euclid team as an IT or the project management? Because I feel Euclid have two. 
**Speaker** *[15:35]*: Yeah. Yeah. Exactly. Ask him. 
**Speaker** *[15:37]*: Okay. 
**Speaker** *[15:38]*: Let's ask him. Let's ask him. I think they—I think they would be—may—maybe it's—it's operations. 
**Speaker** *[15:45]*: Okay. 
**Speaker** *[15:45]*: Yeah. 
**Speaker** *[15:46]*: Okay. 
**Speaker** *[15:46]*: The reason it's operate—the operations team is quite technically savvy. Mm-. Mm-. Or IT as well. And he's got a new person coming on board this week, I think, a new joiner in the IT team. So I think Euclid—yeah. Let's—let's use Euclid. They're also—I'm hesitant to use—you've got HR's already got their questionnaire and—and Mariam isn't—she's a good test case of some of a non-technical person. 
**Speaker** *[16:13]*: Mm- Mm-. 
**Speaker** *[16:14]*: You know? 
**Speaker** *[16:14]*: Yeah. 
**Speaker** *[16:15]*: The other area—the other reason Euclid would be interesting is because he's got, you know, Wisam and Sunshine under him as well, which are, you know, they—they do a lot of process stuff, like onboarding. It needs to be documented. So it's—so it's—but—but so Euclid would be one point of contact for us. But he can then decide how he wants to allocate the team. 
**Speaker** *[16:34]*: Exactly. 
**Speaker** *[16:35]*: You know, operation support, IT, or. 
**Speaker** *[16:39]*: But won't that confuse him? Because he's managing multiple departments. Because this skill, it tells the department—like, the first question's going to be from Claude, "Which department?" Yeah. But let—so let's sit down. Use him. Mm-. 
**Speaker** *[16:53]*: As—as a test case. And then let him decide how he wants to do it. And, you know, he has sub—three sub-departments. All the operational stuff. 
**Speaker** *[17:03]*: Getting him Michael. Why? Why—why? Email you five tasks. 
**Speaker** *[17:15]*: Mm-. 
**Speaker** *[17:16]*: So these—the six questions, your work, inputs, outputs, control, and checkpoints. Tools and system you use, your KPIs, what you need to work better. 
**Speaker** *[17:24]*: Mm-. 
**Speaker** *[17:24]*: The questions and ideas. So it's—it's literally on everything. 
**Speaker** *[17:33]*: Mm-. Oh, so you've put everything in there. 
**Speaker** *[17:37]*: No, this is as a—like a recommendation, showing up. 
**Speaker** *[17:40]*: Oh. 
**Speaker** *[17:40]*: With a recommendation. Like, documents of record. 
**Speaker** *[17:43]*: Yeah. Drizzle, Neon, Vercel. Oh my God. That's a big stack. 
**Speaker** *[17:47]*: Mm-. 
**Speaker** *[17:51]*: 98—198 a month? Mm- Interesting. Ask Michael. 
**Speaker** *[18:07]*: Yeah. Because you—it's—it's using my template as a—as an example. 
**Speaker** *[18:11]*: Mm-. 
**Speaker** *[18:12]*: Because— because there are a couple of things I wanted to ask you regarding which ones are the. 
**Speaker** *[18:17]*: Mm-. 
**Speaker** *[18:17]*: The process owners. Like, who's the process owner of this? Who's the process owner of that? But I al—I already know. So I just put them there. 
**Speaker** *[18:25]*: Yeah. Okay. 
**Speaker** *[18:26]*: But still good to—to keep this as an example because—like, others maybe have, like, a—like, employee and there's, like, a head of department. 
**Speaker** *[18:35]*: I—I—I—I—I really like how you're using GitHub as kind of this—the. 
**Speaker** *[18:40]*: Yeah. It needs to be a center point for all. 
**Speaker** *[18:42]*: I think GitHub is—is the best repo that we have right now. The hesitation is that we're going to have to explain to people how GitHub works. 
**Speaker** *[18:50]*: How to use it. 
**Speaker** *[18:50]*: GitHub accounts. Because that's not something that non—software engineers are. 
**Speaker** *[18:54]*: This is the thing. I'm thinking about not letting them know how to do it, but just keep the skill. 
**Speaker** *[18:59]*: Mm-. 
**Speaker** *[18:59]*: Create them an account. Link it with our— company. 
**Speaker** *[19:03]*: Okay. 
**Speaker** *[19:04]*: Create the repo there. 
**Speaker** *[19:05]*: So it pulls from it. But they don't need to actually— They don't need to actually be in there. The skill itself will just upload there. Mm-. 
**Speaker** *[19:12]*: On its own, without their— Mm-. —the need of, like, them to—to do it. 
**Speaker** *[19:18]*: Mm-. Is Pulse the right thing to call it? 
**Speaker** *[19:22]*: That's why I got—I got—I—I took it from Simon's, documents. 
**Speaker** *[19:27]*: Yeah. 
**Speaker** *[19:27]*: He needs to adjust it so I can adjust it. 
**Speaker** *[19:29]*: I think we need to have a conversation with Andrew about internal branding. We've got all these sub-names happening. Like, Nomi, which Bonaventure is not keen on. 
**Speaker** *[19:38]*: Yeah. I told him if he comes. 
**Speaker** *[19:39]*: We've got Wiki. 
**Speaker** *[19:39]*: I told him I need to look in the company. 
**Speaker** *[19:41]*: Yeah. So what—exactly. So we've got that. We've got what I'm calling a pr—a prime radiant. Which Bonaventure gets is very geeky. He's Welsh by nature. He knows that's—he's—he's—he's an SM of, he got it, like, right away. 
**Speaker** *[19:53]*: Yeah. 
**Speaker** *[19:54]*: By the way, that meeting we had with Bonaventure, for whatever reason, the transcript got you and me talking missed him altogether. 
**Speaker** *[20:03]*: Oh. 
**Speaker** *[20:03]*: Yeah. So I—we should go back to that and—and look—listen to it. I think the audio—he speaks very quietly. 
**Speaker** *[20:12]*: Mm-. 
**Speaker** *[20:12]*: So I don't think it caught his voice. So we may need to download the MPEG-3 and run it through Whisper. 
**Speaker** *[20:17]*: Which one? The one with the— The one where we talked to him after we talked to Andrew. 
**Speaker** *[20:22]*: Last week. After we had the ISO meeting, we had another one with Bonaventure. 
**Speaker** *[20:27]*: Oh, yeah. Yeah. Yeah. Yeah. Yeah. 
**Speaker** *[20:29]*: On Friday. 
**Speaker** *[20:30]*: Yeah. Yeah. 
**Speaker** *[20:30]*: But. 
**Speaker** *[20:31]*: I don't remember because. 
**Speaker** *[20:31]*: When I went to my—because I wanted to use that as input. 
**Speaker** *[20:35]*: Mm-. 
**Speaker** *[20:35]*: And add it to the department knowledge base because he had some good insights. It was just me talking. Oh. And answering his questions. And it didn't pick him up at all. 
**Speaker** *[20:44]*: Oh. 
**Speaker** *[20:45]*: So I think if we go back to Fireflies, you have that Fireflies. Or maybe you share. I think you shared it with me. I need—I think we need to go back and download. Yeah. That—that's the one, right? Friday. 
**Speaker** *[20:57]*: Oh, this one? Yeah. You see it. Is that you or click on that and let's hear it? I'll do as an available system recording. Oh, it's recording. 
**Speaker** *[21:21]*: Oh, because you're recording that. Anyway, let's go back to that later and see. 
**Speaker** *[21:24]*: Mm-. 
**Speaker** *[21:25]*: Yeah. Yeah. It's recording something. 
**Speaker** *[21:29]*: So shall I enroll, Andrew today? Marketing? 
**Speaker** *[21:36]*: Yeah. Let's—let's sit down and talk to him and get him going. But—but the question is, do we want Andrew on the individual? I don't think he's as interested in the individual knowledge base. See, we have to think—I'm thinking about, Does everybody get their own individual knowledge? Or do we want to keep it at the, you know, like, if they have the individual one, what aspects of it roll up into the department? 
**Speaker** *[22:07]*: Oh. So this is my idea. 
**Speaker** *[22:08]*: How do—how do we interconnect them? I mean, we could clearly create interconnections. Mm- By having—so if you go By having—so if you go back to—where—where—where's the knowledge base? Where's—where's your drive? Oh, here. So—so if you go back to prime. Radiant, it's cr—I've had it create something here. If you go to entities. Obsidian. Here, entities. It's created departments. It forgot to do ISO. I'm going to add that. So, for example, if you look here, The markdown. So you see the Bonaventure. I don't know why Simon's in here, but people—Office of the CEO. So we need to create a separate ISO because it—it's comp—it. But I think this is quite interesting. Finance. Let's see. Did it get this one right? Yeah. Ann. All right. 
**Speaker** *[23:13]*: Cross-instance. So these folders—these—these—these finance will become the description. But then I want to have subfolders for each department. So AI finance has a folder. And every time we have a meeting or—or AI operations, every time we meet with Euclid, that AI department with, operations becomes a shared folder. So our meetings with Euclid, we both have access. You, our group, and their group. And I think that's how we connect the nervous system between departments. It's an end-to-end relationship. And then once we have that's how we coordinate so that there's a—there's a folder there that—that links. So we'll do one with Andrew. To start with, because how do we connect these various databases? We could—we could either do it at the very top. But I think we could also do peer-to-peer. It's like a mesh network, if you think of it, right? 
**Speaker** *[24:12]*: You mean like? 
**Speaker** *[24:13]*: Say—say— Personal to AI? No. Not personal. So if you look at this is our vault. Right? For our Wiki. 
**Speaker** *[24:23]*: Mm-. 
**Speaker** *[24:24]*: Or prime radiant. These only we can view these. Now, you and I, because we're both part of the same group, have access to all of them. And I've created the concept of entities. So I'm—I'm thinking to create a whole series of subdirectories, which are—so, for example, when we meet with, Euclid, say, right? 
**Speaker** *[24:47]*: Mm-. 
**Speaker** *[24:48]*: We record it. 
**Speaker** *[24:49]*: Yeah. 
**Speaker** *[24:50]*: The pr—when—and that goes into inbox. And then it gets processed by Claude. Because we're meeting with Euclid, there should also be a right to—so we should create a AI office— operations or IT AI office IT. You know the IT meetings that we hold on a weekly basis? 
**Speaker** *[25:07]*: Mm-. 
**Speaker** *[25:08]*: So that directory has all the insights of the discussions we've had with them. And they also have—so their prime radiant has everything here. But it also has the con—so the conversations that we have between groups are shared in a very special directory. That's why we need this shared folder. Yeah. And that's how we stay in sync with each other. Because discussions that—so—or even if you and I are having a discussion and we mention them, the skill, Claude.md, should know, "Oh, this—this is a something that you want to—" that's how we do cross-department knowledge capture. Because that's very—we—we don't want to have silos, right? 
**Speaker** *[25:52]*: Yeah. Yeah. Yeah. 
**Speaker** *[25:53]*: So the way we avoid silos, and it be—we become an end-to-end. Because we will have AI office finance, AI office, ISO, AI office, going across all these departments. And they will have the same, except— It's from their prime radiant. Essentially building a peer-to-peer end times end, right? 
**Speaker** *[26:15]*: Yeah. I got that one. Yeah. 
**Speaker** *[26:16]*: Yeah. You got it, right? 
**Speaker** *[26:17]*: Yeah. Yeah. Yeah. 
**Speaker** *[26:17]*: I want to see that. Because I think that would be a good way to maintain coordination and, of course, we'll try it out with Andrew first. And then we'll try it out with—so I'm trying to figure out on the individual persons what does that tool—you know, what—what have you learned from using it for yourself? That would be applicable to other people to do their job better. 
**Speaker** *[26:43]*: Well, it's like, you can say it's—the way I'm thinking about it, I had three ideas. But I found one was the—the best, like, fit. 
**Speaker** *[26:53]*: Yeah. 
**Speaker** *[26:53]*: Either we upload everything, dump it into the repo, and we fetch from there. But everyone can access everything. Which I don't want. So I skipped this one. I was like, "It's fine. This decision is—is out of the—the scope. I don't need anyone to see everything, like, in general." Except the CEO, yes. But that's— Yeah. —down the horizon. 
**Speaker** *[27:14]*: Right. Right. Right. Right. 
**Speaker** *[27:15]*: So the second one was either we take specific thing from each person and we upload it to the repo, like, "Yes, they can see." Which repo? The individual repo or the department repo? The depart—I mean, like, it's going to be the main company. So the main company is the final decision, right? It's going to be— Okay. But we haven't built the CEO's office one yet. Yeah. But the thing is, it's going to be a personal, each one have its own vault. It shares into departments. These departments share to the main. 
**Speaker** *[27:51]*: So does that mean then when we do the departments, Claude.md, you know, the rules for this, when would it go in? So—so there's two questions I'm—I'm not clear about. Number one is, in addition to the transcripts and where there's overlap, so what—what—what? Because you—you did this before. I did the department one. But what did you use as a primary input source to build your vault on Obsidian for yourself? And how did you organize the information? Is it just—did you just dump everything into one directory? 
**Speaker** *[28:21]*: No. No. No. No. Because I don't want it to overlap and— Exactly. —a lot of people. So you created some structure for your personal. We—we need to properly structure it. Because at the end, it's going to enroll to the main company. And we need to know what information it's going to reach. 
**Speaker** *[28:35]*: And then the Claude at the department level has to know when to reach into your personal one and pull it out. And so I—I—I—it's that interaction that I'm thinking we need to clarify. Because—because you—you've clearly collected your own knowledge base, which is fantastic. For your own purposes. But you also—we also have to think about how that links. Because we don't want to put everything up there, just—just so—so what—what's that tree? So we got two things. We got a—we got a hierarchy. We got a tree structure to begin with, right? Individuals. Feeding into the department level. The department level still have a level of coordination. This—this—this mesh network, I think, is an important one. And then those, in turn, feed up. But, you know, so for example, when you and I just talked—it doesn't need to be shared. With Euclid, say, with that department. Unless we say, "Oh, we should talk to Euclid about blah, blah." And then the Claude.md should say, "Oh, this is relevant to them.". 
**Speaker** *[29:32]*: So we link it. 
**Speaker** *[29:32]*: And let's stick it in the shared folder so that they then will see that, you know, it's—it's that mentioning of each other's will also force everybody very polite. We can't diss anybody. But the—the—the point is it becomes a mechanism that allows us to do inter—you know, sharing knowledge between the company in such a way—you know, maybe it's something we won't even be needing Slack anymore. Except for intentional. But—but—but—but again, maybe Slack should be a data source for this stuff. Maybe we need—when we run the batch mode, we need to go through everything that Slack has created and pull that into our— into the prime radiant or wiki, whatever we end up calling it. So there's—I think we've got to think some more. And kind of to come up with a— But the main idea is that each vault, personal vault, will hold everything. 
**Speaker** *[30:28]*: All you—will go through your email inbox? Will it go through all your personal Slack emails? 
**Speaker** *[30:32]*: My emails. I put it as— Oh, there we go. —I put the structure as you have access to my laptop. I want you to fetch Notion. Fetch Linear. Fetch Fireflies. Fetch everything. Structure it properly. Have an idea about me. What I do in this company. What I—what is my values. What is my goals and everything. And create me, like, a file. Of me. Because at the end, it's going to read it. So it—it has to know who I am, right? 
**Speaker** *[31:02]*: Mm- Mm-. 
**Speaker** *[31:03]*: Structure everything. Understand my skills. How many skills I have through Claude, through antigravity, my repos, on GitHub, and everything. Yeah. 
**Speaker** *[31:12]*: But you see, just to jump in there, you use a different set of tools. You're using antigravity. You're using GitHub. Somebody like Anne, would have a very different set of inputs for what she does. 
**Speaker** *[31:22]*: Yeah. Yeah. 
**Speaker** *[31:23]*: And I think it's important to have that because it's—say she wants to bring on somebody else. Everything that Bonaventure has been explaining to her, "Here's how you do expenses. Here's how you do the payroll. Here's how you do pre-billing, paying bills." That's knowledge for her. Hasn't been captured. 
**Speaker** *[31:39]*: I mean, at the end. 
**Speaker** *[31:40]*: But we want to capture it. She should—we should have a—that individual. Yeah. Yeah. I mean, it's—it is. And the individual, if you think about it this way, because I told him, "See the tools I use." And Claude already have connections to the tools, right? Yeah. Yeah. 
**Speaker** *[31:55]*: If there is anything I can either add it or it will ask me, like, "Do you use any—anything except these?" And then I will just prompt him, "Yes, I use antigravity. I use this. I use that." And then it will just fetch it or just link it to the—to the website. But as, like, you've seen the—the—the vault becomes— Yeah. Yours is pretty impressive. The vault becomes, structured about this. 
**Speaker** *[32:20]*: Okay. So what do you have in yours? 
**Speaker** *[32:22]*: Okay. It has. 
**Speaker** *[32:22]*: You. 
**Speaker** *[32:23]*: User. Who—who am I? Mm-. I mean, I don't know why you put an AI ops engineer. But I'll change that. 
**Speaker** *[32:29]*: Mm-. 
**Speaker** *[32:29]*: The interest I have, SaaS development, creative immersive—immersive. 
**Speaker** *[32:33]*: And how did it get those? Just from reading all this stuff? 
**Speaker** *[32:36]*: Yeah. Reading my projects. Reading my guidebook, repo, and reading what I've done in—in the first week or something. preferences. Claude has learned. I told him, "Understand what you learned from me and also implement it there." You must not look like AI generated. Always use design MD. And it have references. It always have reference to something. Wants to maximize Obsidian plus Graphify as persistent preen. Wh at's Graphify? Graphify is, it's same as Wiki LLM. It takes everything, converts it into markdowns, and put it—push it into Obsidian. This is how it works. Export graphs and everything. And skills. Prefers. Oh, the skills, it's all the skills I have. Oh, wow. And I then SaaS scaffold. And each one of them also have references to something else. 
**Speaker** *[33:33]*: Yeah. It's all personal stuff. 
**Speaker** *[33:34]*: All skills in the home. Skill list. 
**Speaker** *[33:37]*: And then you got projects. 
**Speaker** *[33:39]*: And then the projects I've worked on for so far. SSFIs have a lot of it's huge. 
**Speaker** *[33:46]*: Oh, my God. That's huge. But that's good. 
**Speaker** *[33:48]*: Because everything I—I put it there. Have the brain to understand the project. Because I don't want Claude code to keep burning tokens. So that's why I—I put it on Obsidian. Because it's easier for him to—to understand the structure. 
**Speaker** *[34:05]*: Claude can handle it easily. Yeah. Yeah. It's not just Obsidian. It's also storing these files as YAML as front matter. So it's progressive disclosure. Progressive—no, not disclosure. Progressive something. You know—you know what I mean? Progressive discovery. 
**Speaker** *[34:17]*: Exactly. 
**Speaker** *[34:17]*: Is—is—is it? You know, I was reading this just—I put it. I haven't—finished reading it. But I found something that it—it's very interesting blog post. Very long blog post by the—by this guy. Who basically is saying, you know, that AI industry community kind of searched for all these different ways of storing knowledge. They went to vector databases and RAG and— And there's something new also is coming as JAC or something. Yeah. There's a lot of stuff out there. But he says at the end of the day, the thing that works the best is texts. Markdown. 
**Speaker** *[34:50]*: Absolutely. 
**Speaker** *[34:51]*: And—and the same technique, you know, software engineers have been using for 40 years. Save it as text files. 
**Speaker** *[34:58]*: Save it as text files. 
**Speaker** *[34:59]*: You know, so after all this looking at all these advanced technologies and way to do it, we're coming back to text files. 
**Speaker** *[35:05]*: We're coming back. 
**Speaker** *[35:05]*: Except Tariq. Did you see his—his next post? 
**Speaker** *[35:10]*: Yeah. 
**Speaker** *[35:10]*: Yeah. He's doing HTML. He's like, "So the internal engineering group at." I was thinking about that last night. 
**Speaker** *[35:16]*: Anthropic are beginning to use HTML more. Not so much as a storage, but as a way of presenting information. So for example, if you want to look something up, the HTML, you could actually create an interactive interface. So that's another post that I put on X that I—I've been in meetings all this time. And I only now, so I haven't even had time to edit to our knowledge. But these are two really interesting insights that—that—that—that—that I got. On Mivery. On—on my tagging. But I—you know, I haven't linked. I can't do—I can't load—I can't do clippings on Obsidian from home. Until I link my Obsidian account back together with, my—so if you do an account, it's five bucks a month to sync your mobile and your multiple Obsidian accounts. 
**Speaker** *[36:07]*: Oh. 
**Speaker** *[36:08]*: So that could be an interesting one to look at. But for example, the ones I found here, which I think are very interesting, is this—this is the one I was telling you about on X. I'm going to share it. Why does—no. Yes. Agent memory engineering. This is really good. Bottom line, TL;DR, it's text. And he compared Hermes Codex and Claude Code. They're different memory architectures. Why this is interesting is because you can't take them from one to another. You can't take your Claude memory system and move it to Codex. It won't work. 
**Speaker** *[36:38]*: Oh. 
**Speaker** *[36:39]*: Yeah. So he explains why. But why the clever architectures lost. Every memory startup pitched the same idea. Vector database. Inference. Retrieval happens at the—the—the. It works just well enough for a demo and then it breaks. So basically saying, "Look at what's winning in production. No vector database. No embedding store. No semantic search. No background memory." Agent has a read. It's basically markdown. Just like a human would. It's very interesting article. 
**Speaker** *[37:06]*: Very cute. 
**Speaker** *[37:07]*: Yeah. Yeah. And then the other one I found here. This is also a good one. The unreasonable effectiveness. So this guy, Tariq, he's great. I don't know if you've seen his—he works. 
**Speaker** *[37:27]*: Yeah. He came up once or twice. 
**Speaker** *[37:29]*: Yeah. He works in the Claude Code team. Oh. He's part of Claude Code. He's one of the key contributors. He's an ex-Media Lab, MIT Media Lab. 
**Speaker** *[37:36]*: Wow. 
**Speaker** *[37:37]*: Yeah. This—this—this guy knows his shit. And he's very interesting. He's very interested. So he's another one of the OGs that I follow. Because his—because he's doing—so he says, "Why HTML?" So anyway, so these are going to go into our Wiki. And they're going to be pushed up. 
**Speaker** *[37:54]*: Yeah. 
**Speaker** *[37:54]*: And supporting our whole thesis about memory. Because I think we've cracked—I didn't say we've cracked the code. But text is— Text is—is very important. With Obsidian, and with this, and—and with progressive discovery, we don't need very fancy databases. 
**Speaker** *[38:13]*: No, no. 
**Speaker** *[38:14]*: Just—just—just use text and organize it in a shared directory structure with the right permission levels. And I think we don't need anything. And we can control access control at the file level. 
**Speaker** *[38:24]*: I wanted to try the—when you have multiple—like, when you can share vaults. From Obsidian itself. The one which requires like payment and stuff. 
**Speaker** *[38:35]*: Well, there's two ways to share. You can create a sync by—through a paid account. Obsidian will allow you to share vaults. Through a synchronization. So if you go to the Obsidian web page, you'll see all the things we could buy. It doesn't have sync. It's not connected. But you can connect. Question is which ones? All right. 
**Speaker** *[38:59]*: Subscriptions. 
**Speaker** *[39:00]*: Right. Right. Right. So if you go to pricing, so there's a $5 sync notes across devices. Intent encryption. Version history. Collaborate on shared vaults. And here it goes up a level. Still not that expensive. If you go for monthly billing. Catalyst. Early access. We don't need support development. I like the shared vaults. 
**Speaker** *[39:36]*: I mean, if we create the repo on—on GitHub, we're actually just creating like a sync. 
**Speaker** *[39:44]*: We are. But find. Grain sync control. Which files you want to sync with which devices. Select a sync. Let's take a look at this. I don't mind paying for it. If it gives us better security and better—you can control what you want to sync. I like the snapshots. Sync activity. The logging. And if we go to the next tier above it, yeah, I think Obsidian and Claude co-work and building—so Obsidian is a memory system. Claude LLM is the brains. And we're creating. A shared memory system. And then accessing. So—so I'm beginning—it's beginning to become clear, I think, in our minds what the potential architecture that we have to be looking at here. 
**Speaker** *[40:53]*: Yeah. 
**Speaker** *[40:53]*: Yeah. But from the personal to the department level, here we should not send everything. No. No. We need—we need to decide what gets pulled up. And—and—and what gets—and—and what's—so what you've built for yourself is very valuable. But you have to think of—we have to think about how does that map to other people. You know, what would, say. 
**Speaker** *[41:17]*: I'm thinking about. 
**Speaker** *[41:19]*: Andres or—or—or think about Wisam. As an admin. You see, the other reason I like a—a private— Repo. A private vault is if somebody leaves—two—two—two things. One, if somebody leaves, the knowledge doesn't leave with them. Yeah. Which is very important. 
**Speaker** *[41:41]*: Absolutely. 
**Speaker** *[41:41]*: In a—in a company. You want to maintain that information. And two, if we're bringing on somebody on board, how much—you know, that—that—that's a very easy way. I—you know, like when you started, you know, we had to take a month for me to have to—you know, we had our meetings and I explained it to you. But that information should be in our system. Should have been in our system. In which case, I don't spend as much time. I simply say, "Here. Chat with it." The AI will train a new person. And, you know, but how we—how we can—it's not clear in my brain yet how we want to use the individual one. Because— Well, the individual is going to fetch all of the information on the—on the person's personal accounts. 
**Speaker** *[42:26]*: Yeah. But that is a—but does that include emails, Slack messages, and stuff? How far do we want to go? There's privacy concerns as well. 
**Speaker** *[42:33]*: How far? It's already there. Let me just show you. 
**Speaker** *[42:36]*: Yeah. Go back to yours. To your Obsidian. Where was it? 
**Speaker** *[42:40]*: No. It's the skill which I—which one was this? Code option. 
**Speaker** *[42:43]*: Oh, yeah. Your personal Claude.md. 
**Speaker** *[42:46]*: That's the IMS. This is the skill which I created for the—yeah. It should be on GitHub now. Why it's not on—on GitHub? 
**Speaker** *[43:04]*: Yeah. We got a nice shout-out from Bonaventure. I think he's quite impressed with what we've built here. And where it's going. It's actually happening quicker than I thought. 
**Speaker** *[43:16]*: Which one? 
**Speaker** *[43:18]*: Our—our building a—a global company-wide knowledge base. 
**Speaker** *[43:21]*: Oh. Oh, yeah. 
**Speaker** *[43:22]*: So it's happening sooner. And I think he was very excited about. 
**Speaker** *[43:25]*: So the skill, it's going to fetch two layers. 
**Speaker** *[43:28]*: This is your personal one. 
**Speaker** *[43:29]*: No. This is which is going to be enrolled into everyone. The brain. 
**Speaker** *[43:34]*: Oh, okay. 
**Speaker** *[43:34]*: So it's—it has. 
**Speaker** *[43:35]*: Oh. So here's how you're going to adapt and build one for each person specific to their— Yeah. This is how their personal—what information is going to be taken from. For every text bearing file, it passes a privacy filter. Per document. What's a privacy filter? 
**Speaker** *[43:51]*: It's a per document. The sub-agent extracts the title, summary, keychain, and entities, and all of these. Decisions, action items, wiki links, and per-person roll-up. It's going to have this structure. 
**Speaker** *[44:04]*: There we go. Okay. Skills, project knowledge, people, decisions, daily. Your personal knowledge graph. 
**Speaker** *[44:15]*: So. 
**Speaker** *[44:15]*: Instead of—oh, what federates company brand? Interesting. 
**Speaker** *[44:18]*: Yeah. Because it's going to be enrolled on a company-wide. That's the main goal. 
**Speaker** *[44:22]*: Oh. Anything tagged private. Interesting. Who tags it? 
**Speaker** *[44:27]*: Oh. Either by default, it's going to be like upon the Fireflies conversation. How private that is going to be. 
**Speaker** *[44:35]*: Oh. That's interesting. Put the front matter. You could put privacy as well. Oh. This is good. So there can be—there can mark stuff private. 
**Speaker** *[44:45]*: Yeah. And stripped before sync. Absolute source path. And any privacy. 
**Speaker** *[44:51]*: Tag. 
**Speaker** *[44:52]*: So the company sees who works on what, who they collaborate with, what decisions they make, what tools they use, knowledge they hold. Minus anything they mark private. What never gets captured at all. 
**Speaker** *[45:04]*: But how will the average user, if they don't know about Markdown files, know to do that? 
**Speaker** *[45:09]*: I didn't get it. 
**Speaker** *[45:10]*: So how would—I don't want to pick on anyone particular. Implying that they're not. 
**Speaker** *[45:15]*: No. No. How would. 
**Speaker** *[45:15]*: How would one of the non-technical people know that they—they have that option to mark a particular piece of information as private? 
**Speaker** *[45:24]*: That's from the training. 
**Speaker** *[45:25]*: From the UI going to be? 
**Speaker** *[45:26]*: That's from the training. 
**Speaker** *[45:27]*: So we have to train them on how this—this folder is built? 
**Speaker** *[45:30]*: No. No. Not really. What we tell them that, "Okay. This is the skill. You—it's going to be daily synced." For your vault. You have the option to keep any documents as private. This is how to do it. This is the training. This is like telling them what they have options, what they don't have, how it's going to work. 
**Speaker** *[45:49]*: Okay. So for example, if you're having a meeting, and during the meeting itself, like we are now, you say, "Hey. I want this meeting to be private. It should not be—will that be enough?" That's for—we're talking about department-wide or company-wide. 
**Speaker** *[46:07]*: But for personal, it's going to be fed. If you got my point. Because we need all of this information in case we want to take—like let's say the finance is talking to Bonaventure. But they made a decision last week. It was private. It's a private conversation. But they want to come up like again with it. Right? They want to be like, "No. We spoke about this last week. This is the recording. So this is going to be in the personal one." But let's say from the CEO level, if the CEO—he'll have like access to private. But let's say from marketing department, he's saying, "What did the—" So private—okay. So private is different from personal. Yeah. 
**Speaker** *[46:45]*: You don't think about it being—because we shouldn't be doing personal work. 
**Speaker** *[46:49]*: Absolutely. Everything we do here effectively belongs to the company. That's our employment contracts like that. So that's it. Also, when you say private, it means not to be shared across the entire company. 
**Speaker** *[47:01]*: Not to be shared across departments, but to share with the CEO. Okay. 
**Speaker** *[47:06]*: Okay. So that's the definition of private. So I was thinking personal. But of course, personal should not be in it. It should not be a thing. If we need to do a personal call, you go, "You can call from your phone in the booth or go outside or do." Exactly. You know? But. A personal is going to be only for personal purposes. It's going to have. Yeah. But. 
**Speaker** *[47:22]*: Public and private. Private is linked with the CEO. 
**Speaker** *[47:24]*: So private has to do with—with—okay. I get it. It's private as in it won't get shared broadly. It's. Exactly. It's got restrictions. 
**Speaker** *[47:32]*: Exactly. Only with the CEO level. Once Bonaventure—but we need to know how to like— Right. So Bonaventure and Teresa are discussing an employee's performance or a salary negotiation or something. That's. That's private. 
**Speaker** *[47:48]*: That—that would be. 
**Speaker** *[47:49]*: That's only for. 
**Speaker** *[47:51]*: For them. 
**Speaker** *[47:51]*: Bonaventure to. 
**Speaker** *[47:52]*: So we could maybe say that only the people directly involved in the conversation are privy to that information. Nobody else—it will never go beyond that. 
**Speaker** *[48:01]*: In case if it's private. 
**Speaker** *[48:02]*: Yes. Yes. Yes. 
**Speaker** *[48:03]*: Other. I If it's private. Yes. Otherwise, if it's public, yes. The other departments can because they need. 
**Speaker** *[48:08]*: Yes. Because that's how you break down the silos. So Bonaventure, you and I are having a brainstorm about something. We don't—you know, we want that to be in the master—to get in our department and especially—and especially if in our discussion, we're also saying, "Oh. You know, this would be a solution that would be really good for Simon to use in the ISO department." It—parts of it should go into the. 
**Speaker** *[48:28]*: The. 
**Speaker** *[48:29]*: Shared document. 
**Speaker** *[48:29]*: Documentation. Yeah. 
**Speaker** *[48:30]*: ISO AIO as well. So he is aware of it. And when it runs the batch mode, even better, it'll say, "Oh. By the way, Simon, you were mentioned in this discussion. You should know about this." I will give him a hyperlink like this. Yeah. Because that's how we replace Slack. I have this vision that at some point, we don't need Slack. For—for this kind of stuff. You don't need to chase. Like a hyperlink with this? Mm-. 
**Speaker** *[48:55]*: It's going to tell him like "Hey, Simon. By the way, you had like a connection with the—with the AI team that you spoke about this and this last week." So this is the connection to it. It will just link it to us. 
**Speaker** *[49:05]*: Yeah. 
**Speaker** *[49:06]*: Because we already have it in our vault, and we have created like a. 
**Speaker** *[49:08]*: And it could—and it becomes part of his knowledge. And that's how we do the cross-fertilization between—it's—we're like bees running around pollinating flowers. 
**Speaker** *[49:16]*: Exactly. Yeah. 
**Speaker** *[49:17]*: You know? That's kind of my vision. You know, the bee goes around here, and then there. And, you know, we're—we're cross-pollinating knowledge across the company. It's not just that we're capturing it. It's not just that we're deriving insights like how decisions are made and—and—and other things like that. And broader level insights. But there's—I think this cross-pollinization is really something that I believe is very important. And it's missing in companies. It's done manually. It's done by chance. Like Pixar when Steve Jobs left Apple, I don't know if you know the story. He created—he started Pixar. And he started Pixar. He bought this visual effects division of LucasArts. The Star Wars George Lucas. Right? So he bought their—their—what they were doing CGI, computer graphics. And he created Pixar. He designed the office in a very particular way. He designed the office that their people from different departments would meet in the middle to have these random conversations. So in the old days, research labs like Bell Labs, which was a famous research lab—in fact, Euclid used to work there. And all these other things. Some of the most interesting innovations and inventions came about by people from two completely different departments. Nothing to do with each other. Just bumping into each other. You know, having a coffee and having some discussion. And they're like, "Oh. It's this cross kind of specialization pollinization that has sometimes emerged in some of the greatest discoveries and insight because people do tend to work in silos." So Steve Jobs recognizes, for example, he once—he never graduated from university. But he took a course in typography. And if you— Ever read his bio, he explained why. Because typography is a very precise thing. And the influence it had on him on type setting and carried over to the design of the Apples. This fastidiousness to detail comes about from what he picked up between that. You know? So I'm a big believer in that. And I've worked at SRIs. And the Stanford Research Institute at some point. And they also had a similar idea that, you know, they had lots of different labs and lots of things. But—but it was very often the cross-pollinization between the things. So—so I've experienced this. We have the perfect tool to do this with that did not exist before. 
**Speaker** *[51:45]*: Exactly. Yeah. 
**Speaker** *[51:46]*: Right? 
**Speaker** *[51:46]*: True. 
**Speaker** *[51:47]*: So how do we capture this kind of financial. Because that's where some of the best ideas are going to come be born out of. 
**Speaker** *[51:56]*: Yeah. 
**Speaker** *[51:57]*: You know, make it easy for ideas to flow between and—and—and that's why I think the other thing that this does is it'll take conversations. And it'll turn into decisions. But, you know, another output is ideas. Which we kind of have in the wiki. If you go back to that. Right? So—so generation of ideas that came out of this thing is—it's not just the decisions. But, you know, any—oh, what about—we wanted to use it as kind of an idea generator as well. Which especially happens across— You also have to be like Andrew. Take a selfie. Truly stand up meeting. We're—we're not—I was using Bell Labs as an example. 
**Speaker** *[52:37]*: Oh. My—my God. 
**Speaker** *[52:39]*: I know. He didn't know you were at Bell Labs. So one of the things we're talking about, we're—we're—we're brainstorming some ideas about stuff, is you remember the things that happened in the labs and why Steve Jobs also built the Pixar office? Because some of the best discoveries were—were multidisciplinary. Two people from two separate disciplines meeting and having a coffee over, you know, the water cooler discussion. And they're like, "Oh. Oh. I want to create the same thing." The part of this global brain, this wiki, is to create linkages between different departments that effectively will generate ideas. But—but now we have the tool to break down that barrier that is more not. Discipline. It's more methodical than before. It was like chance. 
**Speaker** *[53:24]*: Yes. 
**Speaker** *[53:24]*: Right? It was random. You happen to have met somebody. 
**Speaker** *[53:27]*: Yeah. And then when you talk, oh, it's a boom. But—but then it doesn't happen most of the time. But now it's already there. 
**Speaker** *[53:33]*: But—but so one of the functions, one of the features I want to—I want us to build into the system, which is what we're talking about, is this cross-departmental thing. So one thing we're going to test with you—we were just talking about you—is as we build our—our AI. 
**Speaker** *[53:48]*: As personally. 
**Speaker** *[53:49]*: No, no. But—so—so—so we're looking at building this thing in several stages. There's going to be in. 
**Speaker** *[53:55]*: What do you sign? 
**Speaker** *[53:59]*: He's already started the work assignment. But I—I—I was. 
**Speaker** *[54:02]*: You prefer me. Thank you. 
**Speaker** *[54:04]*: Thank you, Brett. 
**Speaker** *[54:05]*: Also—also I don't want—I—I—it's not clear to me that Simon knows exactly what he wants to do. So there's a personal knowledge. One of the things that Jehad was showing me that he's built is his own personal knowledge base, which is actually what I've actually talked about the brain. It's—show Euclid. 
**Speaker** *[54:21]*: Yeah. 
**Speaker** *[54:21]*: You got a few minutes? 
**Speaker** *[54:23]*: Yeah. 
**Speaker** *[54:23]*: Yeah. 
**Speaker** *[54:24]*: For you. 
**Speaker** *[54:24]*: So this is—this is. 
**Speaker** *[54:25]*: Yeah. I was so impressed with that the other day when he showed us. I said, "Ameba. This is ameba." But every dot here. Every dot. It's a single cell. But together it's one. 
**Speaker** *[54:36]*: Like if you go inside exactly, you'll see like literally names and everything connected into each other. 
**Speaker** *[54:42]*: This is. 
**Speaker** *[54:42]*: This is everything that Jehad has learned and contributed and created. This is. The last 28 years. In the—no, just in the last month. 
**Speaker** *[54:50]*: Just last month. 
**Speaker** *[54:51]*: April '12. 
**Speaker** *[54:51]*: If I want to put everything in here, it's going to explode. 
**Speaker** *[54:54]*: It's—so—so it's really interesting. So—so we're thinking about doing an individual one. And then a department one. And when we do the department one, we want to create a linkage. An end-to-end linkage. So for example, when we meet with you andre on IT, we're going to create—because the way this entire thing that they—the—the—the database schema is very simple. It's a—it's directories. And text files. Were just talking about there's a lot—you know, Anthropic and all these—we had these RAG and different database and vector database and what everybody is coming to the conclusion. You know what the simplest format is? Text files. Markdown files. 
**Speaker** *[55:35]*: Oh. 
**Speaker** *[55:36]*: And you organize them in the directory. Because the LLM can read and write more text very easily. 
**Speaker** *[55:40]*: Oh, fast. 
**Speaker** *[55:41]*: Cheaply. 
**Speaker** *[55:41]*: Oh, wow. 
**Speaker** *[55:42]*: Fast, easily. Unit. 
**Speaker** *[55:43]*: Oh, because it—yeah. Just like flat file. You know, you don't have to extract. 
**Speaker** *[55:48]*: But here's the innovation that's come out recently. It's—it's something called Front Matter and YAML. And YAML—show them an example. 
**Speaker** *[55:57]*: Some—some say. 
**Speaker** *[55:58]*: So the—the Markdown files. Some say I can spread on a piece of toast. I know YAML. Mark. Yeah. Yeah. Yeah. So. These are Markdowns anyway. Yeah. 
**Speaker** *[56:06]*: These are Markdowns. 
**Speaker** *[56:07]*: But the Markdowns has a property section at the top. This property section is separate. So if you look, can you see the source file or you can't look at source. You can just see the rendering. So this—this is already rendered. 
**Speaker** *[56:19]*: Oh. 
**Speaker** *[56:20]*: But if you look at the raw Markdown, there's a section at the top that puts—you probably can't see it—that—that puts that property is at the top. So when the LLM is looking for which file to load, it only needs to look at the top three, four lines. You know, the top lines. And it says, "Oh, this is important. I'll pull that in." So it makes it very—very efficient. 
**Speaker** *[56:44]*: Help the indexing. So to speak. 
**Speaker** *[56:46]*: Yeah. You just do, you know, remember units? Grep. Search. You just grep. 
**Speaker** *[56:49]*: It's just something we've done, I think. 
**Speaker** *[56:52]*: Yeah. 
**Speaker** *[56:53]*: Or just an MD file. 
**Speaker** *[56:54]*: Yeah, yeah. Anyway, so but you see everything is Markdown. And HTML. So it's all based on text. I want us to get away from all the fancy heavy formats. 
**Speaker** *[57:03]*: Yeah, no. 
**Speaker** *[57:03]*: We don't need those. 
**Speaker** *[57:04]*: Those overheads. 
**Speaker** *[57:05]*: And that's why we're spending so much tokens. 
**Speaker** *[57:07]*: Yeah. 
**Speaker** *[57:08]*: Like why are we creating a PowerPoint every time when it's read-only? All you write it and then do it HTML. And you can always print an HTML into PDF if you need. 
**Speaker** *[57:18]*: Yeah. People either spend this time, you know, so pretty. So pretty. Send them what's the message? 
**Speaker** *[57:24]*: Yeah. 
**Speaker** *[57:25]*: Like all chat is so confused. Like amazed, you know. 
**Speaker** *[57:27]*: Yeah. And—and—and generating images. 
**Speaker** *[57:31]*: All chat is very simple. That's it. 
**Speaker** *[57:33]*: Right. People don't know that they need to upload HTML. You can do an old chart in HTML because HTML you can do an interactive one if you want even. But if you want it, once you've got the HTML, you can always—if you need to—and I'm beginning to become less of a fan because when you create a PDF, it's not changeable. It's version. 
**Speaker** *[57:50]*: You should see the onboarding version of the old chart. 
**Speaker** *[57:53]*: We're going to change that. 
**Speaker** *[57:54]*: You will not—you—I—I told—I told that person frankly. I said, "I work here. I'm confused. Let alone a new person coming in." There—there were not trained properly in this kind of our fault that we didn't have the resources and ability to train them. But we—we've learned a lot. Why PD? 
**Speaker** *[58:11]*: We should not be—first of all, we—we should probably stop using notebook LM. Because notebook LM creates images. They're not writes. They're not easy. They're impossible to edit. 
**Speaker** *[58:21]*: But—but the worst is. 
**Speaker** *[58:22]*: It's easier to tell. 
**Speaker** *[58:23]*: Like you say, it's not write. But the individual doesn't know how to correct that. And you keep going down to that path. It's getting. 
**Speaker** *[58:30]*: And you're trying over and over. 
**Speaker** *[58:31]*: Yes. 
**Speaker** *[58:32]*: So the right methodology, I would say, you can still do it in Gemini. Create the org chart in HTML. Any web browser can read it. 
**Speaker** *[58:41]*: Yeah. 
**Speaker** *[58:42]*: Simple. It's quick and you can correct it very easily. It's easy to edit. 
**Speaker** *[58:46]*: I mean, at the end of the day, it's just a conversation, right? You say, "Well, I do the appointment, two, three." That's it. 
**Speaker** *[58:50]*: Mm-. 
**Speaker** *[58:50]*: I don't need—I don't need an hour. It's just I can do it in minutes. Meeting. 
**Speaker** *[58:55]*: Oh, by the way, why are we using notebook LM? 
**Speaker** *[58:58]*: Notebook LM? 
**Speaker** *[59:00]*: When? 
**Speaker** *[59:00]*: Why? 
**Speaker** *[59:01]*: Oh, why? For creating. 
**Speaker** *[59:02]*: Oh. I mean, for creating. Oh, go back to the genesis. But the genesis of genesis. The genesis of genesis. Spot adventure. 
**Speaker** *[59:10]*: Yeah. 
**Speaker** *[59:10]*: No, I mean, if we—we just use it for creating the images. No. No, no, no. 
**Speaker** *[59:14]*: No, it was for genesis started. 
**Speaker** *[59:16]*: So when there were only like three of us, Spot adventure used it heavily to do PowerPoints, presentations, to use. 
**Speaker** *[59:23]*: Easy. He didn't like us when we had meetings. Just do PowerPoint. He goes, "Why don't you use that?" He was pushing it. Because it was a very interesting tool. He did the podcast. He did the videos and everything. Yeah. He was right. 
**Speaker** *[59:34]*: I think. At the time, it was the right tool. But now that we have people like you. But also. 
**Speaker** *[59:38]*: On board and we've got really good. 
**Speaker** *[59:40]*: Because we had those computer backgrounds when we did that. It was—he was right to actually, it's for illustration and everything. It's better than PowerPoint. Because we—we three of us understood the computer. But then when you—when the admin, for instance. 
**Speaker** *[59:57]*: Yeah. There's a difference. Plus in—in—in—in nonce people don't have the right training and skills. So we—we—one of the things we're also thinking about is, you know, what is our data architecture here? And it's good for you to be in that picture because when it gets rolled out at scale to the entire company, we have to think about these things. So what—what we've done here is our wiki that we are now building—I've put it in a Google Share drive. So Mikey or Yuki, not Wiki. 
**Speaker** *[01:00:26]*: Wiki. 
**Speaker** *[01:00:26]*: Yuki put Euclids. Yuki. Oh, Mikey. 
**Speaker** *[01:00:30]*: So—so this I'm calling a prime radian. This is actually sitting in Share drives. 
**Speaker** *[01:00:35]*: Yeah. 
**Speaker** *[01:00:36]*: Okay. 
**Speaker** *[01:00:36]*: So if you go in here. 
**Speaker** *[01:00:37]*: Huh. 
**Speaker** *[01:00:38]*: So these are the files. This is the vault. 
**Speaker** *[01:00:41]*: Mm-. 
**Speaker** *[01:00:41]*: That has everything in here. And we've got, for example, if you. Look at entities. 
**Speaker** *[01:00:48]*: By the way, do you like that? 
**Speaker** *[01:00:50]*: You're in here, by the way. 
**Speaker** *[01:00:51]*: Oh, thank you. 
**Speaker** *[01:00:52]*: Oh, no. Not in this one. 
**Speaker** *[01:00:53]*: Oh. Do you—do you like this room better than the conference room that you have to sit down in? 
**Speaker** *[01:00:58]*: It's cold there also. 
**Speaker** *[01:00:59]*: Yeah. And—and plus standing up, you know, you—you like your brain works better. So you're—you're in here. Oh, thank you. 
**Speaker** *[01:01:07]*: See, this is front matter. You see the three dashes? 
**Speaker** *[01:01:09]*: Mm-. 
**Speaker** *[01:01:10]*: These are the tags. It's type, person, your title, slug. 
**Speaker** *[01:01:15]*: I'm a slug. 
**Speaker** *[01:01:16]*: Well, the slug is what it needs. 
**Speaker** *[01:01:17]*: Could you change that? 
**Speaker** *[01:01:18]*: Kebab case. 
**Speaker** *[01:01:19]*: What's that? 
**Speaker** *[01:01:19]*: But you see, it's got the created date, updated date, departments, IT ops. And then what's related, right? Andre is in here. See, these are all the things that are—this is how it builds a connection to do that. And then it says this only knows from all the conversations we've had. And it already knows that you're head of IT. Ooh. You work exclusively. 
**Speaker** *[01:01:38]*: With Lion. 
**Speaker** *[01:01:39]*: Yeah. The sandbox to production handoffs. Because our wiki is trained—it's not trained. It draws in the information from our transcripts. Linear. 
**Speaker** *[01:01:52]*: Okay. 
**Speaker** *[01:01:53]*: Monday.com and Notion. So everything that's discussed in these things and areas of involvement, IT approved tools list, CRM, so. And working pattern, co-attendee on the AI IT meeting. huh. Was the most recent surface day. So this—this—this is, yeah. This is automatic way of. 
**Speaker** *[01:02:12]*: It's all automatic. Yeah. These things—these things are—are running Automatically. 
**Speaker** *[01:02:19]*: Okay. 
**Speaker** *[01:02:20]*: I'm very starting to build a department level ones. And it's—this is sitting on the Share drive. 
**Speaker** *[01:02:27]*: Huh. 
**Speaker** *[01:02:27]*: But we're also—we were discussing before we came in here that you—that Obsidian, which is the database, we can actually—the paid version of it—will sync. So we can create sync. So we're—we're still. 
**Speaker** *[01:02:37]*: I like that Obsidian. I mean, you know. 
**Speaker** *[01:02:40]*: It's cool, right? 
**Speaker** *[01:02:41]*: What Simon sent me. 
**Speaker** *[01:02:44]*: What was that? 
**Speaker** *[01:02:47]*: Simon. 
**Speaker** *[01:02:48]*: See, he should. 
**Speaker** *[01:02:51]*: It's too early for Simon. It's going to take. 
**Speaker** *[01:02:54]*: He should spend time working. 
**Speaker** *[01:02:56]*: Not right. Yeah. I agree. Don't give him Obsidian yet. He's going to waste time on it. 
**Speaker** *[01:03:00]*: Yeah. 
**Speaker** *[01:03:01]*: And then Bonaventure's going to yell at us. 
**Speaker** *[01:03:02]*: Yeah. 
**Speaker** *[01:03:03]*: Yeah. 
**Speaker** *[01:03:04]*: Everyone just down to cross-check with you. 
**Speaker** *[01:03:06]*: Yeah. Yeah. 
**Speaker** *[01:03:06]*: They say we. 
**Speaker** *[01:03:08]*: And Obsidian is still on the same. 
**Speaker** *[01:03:09]*: We somehow hung something two weeks ago. It's still. 
**Speaker** *[01:03:11]*: Yeah. Obsidian is still on the—it's getting. 
**Speaker** *[01:03:14]*: No. Plus, he doesn't. 
**Speaker** *[01:03:15]*: Anyway, so—so also the other thing we want to be able to do is—is—is create a cross-department. So when we have our meetings together, it will go into a folder in the shared folder that both of us will have access to. So it becomes part of your department knowledge base too. 
**Speaker** *[01:03:30]*: Yeah. 
**Speaker** *[01:03:30]*: And that's how we create linkages. The mesh network of. 
**Speaker** *[01:03:34]*: Oh, because they also check the process, the workflow. If any breakages or stuff. 
**Speaker** *[01:03:39]*: You could tell that. 
**Speaker** *[01:03:40]*: So today has a breakage. I didn't want to bring it up. 
**Speaker** *[01:03:43]*: Why? 
**Speaker** *[01:03:44]*: Did you receive that? Supposedly we have a new guy joining today. No. I don't think so. I haven't checked my email. 
**Speaker** *[01:03:51]*: So this is the brains behind it. 
**Speaker** *[01:03:53]*: On your calendar, you—you had that. So it was. 
**Speaker** *[01:03:56]*: So—so the way the system works is you've got several components to it. You've got Obsidian. Which manages this vault. But it only stores and displays it. And then it's the memory. Think of Obsidian as a memory. And Claude, we're using Cowork as the brains. But how does Claude know that the structure of all these directories? How does it know to put what where? It's in this file called Claude.md. Oh. So this is the instructions of everything. 
**Speaker** *[01:04:25]*: Oh, you keep. 
**Speaker** *[01:04:26]*: It shows. 
**Speaker** *[01:04:26]*: To Claude. 
**Speaker** *[01:04:27]*: This is created by Claude. 
**Speaker** *[01:04:28]*: Oh. 
**Speaker** *[01:04:28]*: Through a conversation. 
**Speaker** *[01:04:30]*: Huh. 
**Speaker** *[01:04:30]*: So these are the rules for why we—so for example, if breakages is something that's important, it would go into this file. This is the instructions to Cowork as to where things belong. 
**Speaker** *[01:04:40]*: Oh. 
**Speaker** *[01:04:41]*: And how to think about this and everything is in here. This is—this is like the master program. This is the DNA that tells Claude how to manage that memory. So we've got Obsidian, Claude, file structure. Are the three key components of what we've got here. 
**Speaker** *[01:04:58]*: Mm-. 
**Speaker** *[01:04:58]*: And taken together, we're going to build the entire company. 
**Speaker** *[01:05:02]*: Oh, right. 
**Speaker** *[01:05:02]*: Base or knowledge base. So we want— Thursday? —to work with you. 
**Speaker** *[01:05:07]*: Yeah. Thursday. 
**Speaker** *[01:05:08]*: Oh, Tuesday. 
**Speaker** *[01:05:09]*: To—to—you—you—well, the question is, which—which—which team? Your IT team, your operations team, or your project management team? Would you? 
**Speaker** *[01:05:16]*: I think project management would have a role. 
**Speaker** *[01:05:18]*: I think so too. 
**Speaker** *[01:05:19]*: Yeah. I mean, it's the biggest department. 
**Speaker** *[01:05:22]*: Yeah. It's already there. 
**Speaker** *[01:05:23]*: The one. 
**Speaker** *[01:05:24]*: And it's already there. 
**Speaker** *[01:05:24]*: We have convert most of the stuff. Yeah. I think so too. Because you want to capture the knowledge and the insights. Yeah. The knowledge. Okay. 
**Speaker** *[01:05:32]*: Yeah. More of a bank of the buck. 
**Speaker** *[01:05:35]*: Yeah. And—and the other thing I like about that team, they're technical. I know. Yeah. 
**Speaker** *[01:05:40]*: Yeah. 
**Speaker** *[01:05:40]*: Next would be the IT. 
**Speaker** *[01:05:41]*: IT. 
**Speaker** *[01:05:41]*: It's easiest to talk to. 
**Speaker** *[01:05:44]*: In Chinese. 
**Speaker** *[01:05:44]*: Easiest to talk to. 
**Speaker** *[01:05:45]*: In Chinese? 
**Speaker** *[01:05:46]*: Well, both Chinese and English. Their English is not good. But then because it's domain like Los Angeles, right? He was able to share a lot of information with us and get excited with simple English. Because it's domain expertise, right? Simple. 
**Speaker** *[01:06:00]*: So—so let's start building that linkage and bring—and spin up a— We. We—how about our Wednesday meeting? Bring him—bring Los Angeles. 
**Speaker** *[01:06:10]*: But can we separate it from IT? I think they're two different functions. 
**Speaker** *[01:06:13]*: Oh. Yeah. Oh, yeah. Let's. 
**Speaker** *[01:06:15]*: Let's keep the IT with Andre and your new guy if necessary. Because that is. My new guy—I My new guy—I think my new guy is very sharp. Good. The IT is important because that's where we're going to discuss how we move things into production. And once the ISO stuff is standardized, oh, the other thing Jahad has built is a mechanism for creating all the ISO stuff. 
**Speaker** *[01:06:35]*: Oh, yeah. It's already there. 
**Speaker** *[01:06:35]*: Which we can show you and. Yeah. Yeah. It's built. It's done. 
**Speaker** *[01:06:38]*: We're 20 reference. 
**Speaker** *[01:06:39]*: I see. Well, that day we'll have that meeting. I was very impressed. I mean, a lot more than what I have had thus far. 
**Speaker** *[01:06:46]*: You cracked the code with Simon. 
**Speaker** *[01:06:47]*: I cracked the code. 
**Speaker** *[01:06:47]*: Somehow you two have chemistry. I. 
**Speaker** *[01:06:51]*: It's a fun guy, though. 
**Speaker** *[01:06:52]*: He—yeah. He struggles a bit with the language, I think. 
**Speaker** *[01:06:54]*: Yeah. Just the language. 
**Speaker** *[01:06:55]*: Is that language? 
**Speaker** *[01:06:56]*: I think so. Yeah. No, he's really smart. He's really smart. 
**Speaker** *[01:07:00]*: No, he is really smart. I like the Indian way of saying things. 
**Speaker** *[01:07:04]*: He's not Indian, by the way. I know, but he—he was india. 
**Speaker** *[01:07:08]*: That's true. That's true. He picked up some of the. 
**Speaker** *[01:07:10]*: Influence. 
**Speaker** *[01:07:10]*: I picked a lot of things from there. 
**Speaker** *[01:07:12]*: No, he's really smart. 
**Speaker** *[01:07:14]*: Yes. N No, he's really smart. But no, he's really smart. Yeah. He picked up a few habits. 
**Speaker** *[01:07:20]*: But the English part, which like took me forever to crack it, but yeah. You just need the—I just told him. I just need documents. Just send me documents. 
**Speaker** *[01:07:29]*: Great. The AI wrote it. 
**Speaker** *[01:07:32]*: I'll understand it. Just send me. 
**Speaker** *[01:07:33]*: I was going to say do the same thing. Because do you remember he did the form and he—he never had to do the form? I said, "Just give me the form. Let me use AI to fill out the form for me." So—so—so—so I think we're there on that one. And—and—. Also, he's the only one in the company that can— Understand. Even Andre could not. 
**Speaker** *[01:07:54]*: And he's Russian. It's not a language thing. 
**Speaker** *[01:07:56]*: That they—that they—three of us, right? I said, "Andre and Simon, I don't mind. Just speak your language as long as I can get the information." Andre later said, "My God." Well, good. Good—good—good job, Jahad. 
**Speaker** *[01:08:12]*: It's multitalent. Andre—I'm glad. I'm glad. 
**Speaker** *[01:08:15]*: Yeah. 
**Speaker** *[01:08:15]*: Huh? Yeah. One—one of these days, you'll wear the suit back. 
**Speaker** *[01:08:21]*: Sharp. 
**Speaker** *[01:08:22]*: Sharp. 
**Speaker** *[01:08:22]*: Yeah. 
**Speaker** *[01:08:23]*: And then you walked in. 
**Speaker** *[01:08:24]*: Yeah. We're a software company. We're hoodies. 
**Speaker** *[01:08:25]*: The first day I came. 
**Speaker** *[01:08:26]*: Yeah. Yeah. When you came for the interview. 
**Speaker** *[01:08:28]*: The interview. You walked in and people wouldn't recognize me. Oh, especially if he's shaving came in. Sometimes I hear for interview. 
**Speaker** *[01:08:40]*: That's good. That's good stuff. Okay. So. 
**Speaker** *[01:08:42]*: Oh, by the way. 
**Speaker** *[01:08:43]*: So—so—so in addition then, we'll do the meetings with you. 
**Speaker** *[01:08:46]*: I'm separate. Sunshine and Wisdom. So Sunshine is doing everything for us. Mm- But Wisdom was going to support the department head and the C-level. O Oh, okay. 
**Speaker** *[01:09:01]*: Okay. So I think what else do we need to cover? I think we covered everything. Oh, one thing I wanted to ask you, since you're here. So I went to the Apple Store. I was looking to see maybe get myself all the Neo computers and Mac Minis are sold out for months. 
**Speaker** *[01:09:17]*: Ooh. 
**Speaker** *[01:09:17]*: Gone. Wow. 
**Speaker** *[01:09:18]*: Oh, you're on the waiting list? 
**Speaker** *[01:09:21]*: No. Not yet. I'm for the Mini, I'm going to wait for them finally. 
**Speaker** *[01:09:24]*: It's very expensive, isn't it? 
**Speaker** *[01:09:25]*: The—the Neo is very cheap. 
**Speaker** *[01:09:27]*: Who said what? 
**Speaker** *[01:09:27]*: M6 isn't out yet? 
**Speaker** *[01:09:29]*: How much is it? 
**Speaker** *[01:09:30]*: No. Neo for 2,500 dirhams. You can get yourself a Mac. But it uses the A—it uses the same chip that the iPhones use. It's not a— It's not as powerful as a—as ours. But for a lot of stuff, it's. 
**Speaker** *[01:09:41]*: It's good enough for my— It's good enough. 
**Speaker** *[01:09:43]*: Yeah. So—so anyway, the point is. 
**Speaker** *[01:09:45]*: It's good. 
**Speaker** *[01:09:45]*: The guy that—the guy Yusuf was the guy that was the—he says, "I'm not here to sell. Just to explain. I determined I learned two things. Number one is the prices here are much higher than Hong Kong and other countries. And they don't do a VX." Why is that? Like substantial. Like we're talking on a 2,600 dirham, 300 dirham difference to the price of buying them in Hong Kong. Something to think about where we buy them. Yeah. Hong Kong, other places. Yeah. Well, it comes with a pros and cons as well. Yeah. 
**Speaker** *[01:10:16]*: As it says. No pro. No warranty. 
**Speaker** *[01:10:18]*: Is it the same? 
**Speaker** *[01:10:18]*: Yeah. Worldwide warranty. 
**Speaker** *[01:10:21]*: Well, an international version you will also find there? Like a US. 
**Speaker** *[01:10:24]*: Yes. Absolutely. 
**Speaker** *[01:10:25]*: Version—US version, absolute number one. 
**Speaker** *[01:10:27]*: Where? 
**Speaker** *[01:10:27]*: The second thing, which—which I wanted to bounce off you. 
**Speaker** *[01:10:30]*: In Hong Kong, you will find like a US version or something. 
**Speaker** *[01:10:33]*: Oh, no, no. No. 
**Speaker** *[01:10:34]*: Oh. We—we use Hammer. Oh. 
**Speaker** *[01:10:37]*: Of course. 
**Speaker** *[01:10:37]*: We use British. 
**Speaker** *[01:10:39]*: Used to be, I guess. 
**Speaker** *[01:10:40]*: Yeah. They—no, Hong Kong, they sell international and. Oh, that's. And the keyboard actually. 
**Speaker** *[01:10:43]*: We don't use Chinese one, for example. 
**Speaker** *[01:10:45]*: Seriously? 
**Speaker** *[01:10:45]*: You don't need it? 
**Speaker** *[01:10:46]*: We don't use Chinese. 
**Speaker** *[01:10:47]*: It's not a productive—production in China? 
**Speaker** *[01:10:49]*: No. Because the way you enter text, the Chinese characters is—you don't need. 
**Speaker** *[01:10:54]*: Oh, sorry for that. 
**Speaker** *[01:10:54]*: Yeah. You use a Roman—anyway, the other thing is I found out this—the—the guy Yusuf, he's studying computer science at the—the American University here. He's in his third year. 
**Speaker** *[01:11:05]*: Oh, yeah. 
**Speaker** *[01:11:06]*: I was thinking, should we think about an internship? If we can get an interns in? 
**Speaker** *[01:11:11]*: For what time? 
**Speaker** *[01:11:11]*: He's—he—he under—he's vibe coding. I mean, he kind of gets it. I was just wondering. I got his WhatsApp. 
**Speaker** *[01:11:17]*: Oh, that's good. 
**Speaker** *[01:11:18]*: So you can do that in your group. You can consider. 
**Speaker** *[01:11:20]*: We can do interns? 
**Speaker** *[01:11:21]*: I think so. 
**Speaker** *[01:11:22]*: I'll talk to Theresa. 
**Speaker** *[01:11:23]*: I mean. 
**Speaker** *[01:11:23]*: She comes. 
**Speaker** *[01:11:24]*: That's a good way to, you know, a lot of. 
**Speaker** *[01:11:26]*: He seemed very bright. And he's doing a lot of the stuff. And, you know, interns don't cost much money. And maybe we could. 
**Speaker** *[01:11:32]*: Well, that and also fresh revenue. 
**Speaker** *[01:11:36]*: Because we still need for the AI native on the production side, we still need someone that techs be able to talk to that. Whereas maybe we find out something. 
**Speaker** *[01:11:46]*: I mean, if he's working already in Apple, so we have this consumer. Yeah. 
**Speaker** *[01:11:50]*: Well, he's got good people skills because he works at Apple, right? So he's very great people skills. Really nice guy. And he's in his third of—third of fourth—third out of four years. 
**Speaker** *[01:11:59]*: Oh. 
**Speaker** *[01:11:59]*: Doing studying computer science. So he's only third year, but he's already vibe coding. I was talking about stuff. He understood everything. 
**Speaker** *[01:12:06]*: Yeah. 
**Speaker** *[01:12:07]*: That I was saying. He gets it. So he's—he's deep into the AI and the talent. Maybe something to think. Anyway, I'll send him—I'll talk to Theresa if. 
**Speaker** *[01:12:16]*: I think we'll. 
**Speaker** *[01:12:16]*: Interns is a possibility. 
**Speaker** *[01:12:17]*: In my opinion, we need more of that to influence the small group of people. And then eventually bring that. 
**Speaker** *[01:12:23]*: And I'm thinking one of the things he could help us is to bring up, as we spread all this wealth of all these AI tools, so different departments, he could help because he's got the Apple personal skills. He could help us interface. That could be an interesting job. Yeah. You know, once you've built the system, have him help the recipient, particularly the less technical ones, get up to speed on it. 
**Speaker** *[01:12:45]*: Yeah. Sounds assembly line. 
**Speaker** *[01:12:47]*: Yeah. It's good if you can catch up really quick because it's going to be hard for me to explain. 
**Speaker** *[01:12:52]*: Well, exactly. He could be the explainer. I think that would be a perfect thing for somebody like that to do if we could get him in the summer. 
**Speaker** *[01:12:57]*: Well, and also, yeah, explain or train everything. 
**Speaker** *[01:13:00]*: Yeah. 
**Speaker** *[01:13:01]*: I dive too deep into technical. That's why I'm—I'm not a great in training. 
**Speaker** *[01:13:05]*: Yeah. So—so maybe somebody that. 
**Speaker** *[01:13:06]*: Because we don't. 
**Speaker** *[01:13:06]*: That's what I. 
**Speaker** *[01:13:07]*: We don't have patient for stupid people. 
**Speaker** *[01:13:10]*: That's—that's another thing. 
**Speaker** *[01:13:11]*: But he could be the—so simple. Why do you understand? 
**Speaker** *[01:13:14]*: Yeah. So that could be an impedance match between us and—and the less technical people because he's—he—he did that very well at Apple. 
**Speaker** *[01:13:21]*: Right. Right. 
**Speaker** *[01:13:22]*: Because that's what Apple teaches you, how you deal with non-technical people. Yeah. Yeah. Good people skills. 
**Speaker** *[01:13:26]*: Yeah. Yeah. 
**Speaker** *[01:13:27]*: You know, and—and you know. 
**Speaker** *[01:13:28]*: Yeah. Well, plus, like I said, we—we—we—we need seriously, we need—we need a group of people that work in the AI native for the—for the products. Yeah. For the products. Yeah. 
**Speaker** *[01:13:42]*: Yeah. So maybe you don't even know. 
**Speaker** *[01:13:44]*: Yeah. That's—I mean, so anyway. 
**Speaker** *[01:13:46]*: Good. 
**Speaker** *[01:13:47]*: I need an Apple version. 
**Speaker** *[01:13:49]*: Vision Pro? 
**Speaker** *[01:13:50]*: Vision Pro. 
**Speaker** *[01:13:52]*: So then you could just. 
**Speaker** *[01:13:52]*: Just like, yeah. 
**Speaker** *[01:13:54]*: Anything else that we missed? Anything else we need to cover? 
**Speaker** *[01:13:56]*: Yeah. We're outside. We're standing outside saying, "Wait, wait." Oh my God. This was a very long standup. And then start talking to yourself. 
**Speaker** *[01:14:05]*: Become a musician. 
**Speaker** *[01:14:06]*: Yeah. 
**Speaker** *[01:14:08]*: Long—long standup. One hour. 
**Speaker** *[01:14:11]*: 14 minutes. 
**Speaker** *[01:14:12]*: I think we're done for today, right? 
**Speaker** *[01:14:14]*: Yeah. 
**Speaker** *[01:14:15]*: We covered most of it. 
**Speaker** *[01:14:16]*: And—and also tomorrow. That is so rude. 
**Speaker** *[01:14:18]*: So cool. 
**Speaker** *[01:14:20]*: Thank you, gentlemen. 
**Speaker** *[01:14:21]*: Thank you. Thank you. Thank you. And, so I'm going to work some more on, Andrews architecting Andrews. 
**Speaker** *[01:14:29]*: Yeah. I'll check then the—let me just finish these, two skills. The ISO and the, 
**Speaker** *[01:14:35]*: Yeah. Yeah. Finish the ISO. 
**Speaker** *[01:14:36]*: CDO. And then I will move into moving part of my Obsidian into the—the main vault. Let's see how it goes. 
**Speaker** *[01:14:45]*: Yeah. Exactly. Because I've created a share folder, so you have access to that. 
**Speaker** *[01:14:48]*: Yeah. Yeah. I'll work on that and to make sure, like, how—let me be the—the—the, like, the test in there. 
**Speaker** *[01:14:56]*: Mm-. 
**Speaker** *[01:14:57]*: How can I send my—like, Obsidian there without, like, sending everything? Because we don't need to send everything. So I need to. No. 
**Speaker** *[01:15:06]*: No. And—and the thing is. 
**Speaker** *[01:15:08]*: What does—does your cloud—it's because cloud MD is inside that. So what I'll ask my cloud cowork to do, I'll tell it that you want to have access to it through your cloud. It can prep a small file that will— Give—give your cowork. So create a project. Right? And the project doesn't have knowledge files, but it—it organizes everything else. Point yourself to the shared folder. So create a new project. Call it. 
**Speaker** *[01:15:41]*: No. I'll use co—the cloud—the code. 
**Speaker** *[01:15:44]*: Code. 
**Speaker** *[01:15:44]*: For that. 
**Speaker** *[01:15:45]*: Oh, you want to do it through code, not cowork? 
**Speaker** *[01:15:46]*: Yeah. Because the cowork doesn't have everything I'm—like, I didn't connect it to everything. 
**Speaker** *[01:15:51]*: Should I switch the code as well from cowork? I'm using cowork to build that wiki thing, but maybe I should use clo—code. 
**Speaker** *[01:15:58]*: I mean, honestly, you shouldn't use code for that. 
**Speaker** *[01:16:00]*: I should, right? 
**Speaker** *[01:16:01]*: Yeah. 
**Speaker** *[01:16:01]*: I'll move it. 
**Speaker** *[01:16:01]*: Because it understands, like, the MD files and all of these structures properly. And it understands the function. 
**Speaker** *[01:16:06]*: So does cowork, but I'm thinking if I want to build something using an HTML and host it, yeah. Yeah. You're right. I'm—I'm—I'm—I'm—I'm—yeah. I'm going to do it as a project. And then you can use also CLI. Yeah. The Yeah. The cloud? I—I can launch clo—cloud code. Actually, I could use cowork on the UI and cloud code and the CLI. 
**Speaker** *[01:16:30]*: Yeah. 
**Speaker** *[01:16:31]*: So they can both work together. 
**Speaker** *[01:16:32]*: True. 
**Speaker** *[01:16:33]*: Right? Yeah. 
**Speaker** *[01:16:38]*: Because for me, cloud code already. 
**Speaker** *[01:16:40]*: Through the CLI or VS Code as well. I mean, V—I could point VS Code at that directory as well. Yeah. And— And—and launch so I don't need—yeah. That's another way to do it. But I do want to build something for Andrew that by. Passes cloud cowork or and just build its own UI. He's not—okay. 
**Speaker** *[01:17:04]*: I think we covered enough today. We got—now we have to get—and were talking about a venture, and. 
