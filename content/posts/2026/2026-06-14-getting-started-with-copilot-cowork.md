---
author: "liamjbennett"
title: "Getting started with Copilot Cowork"
date: "2026-06-14"
description: "A practical first look at Microsoft Copilot Cowork, covering early productivity wins, limitations, and the kinds of workflows it’s good for."
tags: ["productivity", "ai", "copilot", "cowork"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
aliases:
  - /posts/2026-05-16-getting-started-with-copilot-cowork
---

I've been using Microsoft Copilot Cowork since it's first day of release into the [Frontier programme](https://www.microsoft.com/en-us/microsoft-365-copilot/frontier-program). It has had a significant impact on my productivity and for those few of us in the organisation going through our internal pilot of the tool. I've had so many conversations about it over the past two months that I felt the need to share my experience in the hope that you find it useful and get to share the experience with others.

I'm going to assume for the rest of this post that you have some experience with Microsoft Copilot, or at least experience with other similar tools like Anthropic Claude or ChatGPT. If you don't then there is some great content out there that will help you [get started with Copilot](https://www.youtube.com/watch?v=0_mqsU7yh5Q).

I started using Microsoft Copilot at work during the first part of 2024, and during the next 18-months it mostly replaced my use of enterprise search and google search. I'm not here to wade into [the AI debate](https://www.britannica.com/procon/artificial-intelligence-AI-debate), I found early on that it aided in my productivity and I started using it for initial content drafting, although I wasn't too happy with the output because I could never get it to look like something I might write for myself. Honestly, after a lot of use I wasn't really a huge fan of the GPT models (either personally or professionally). With the release of the newer Anthropic models in the summer of 2024 and after plenty of conversations with people about these models I moved most of my usage over to an internal chat interface that used the Sonnet model (LibreChat using Azure Foundry). It wasn't quite as smooth as using Copilot and didn't have integration with enterprise search yet, but the output was just better, or at least I felt so for my use cases.

## Introduction to Cowork

A strategically significant thing happened in May 2026 - Microsoft [announced Microsoft Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/). Cowork was the product name for the agentic system built and released by Anthropic in January and part of their Claude product. Given that Microsoft was a heavy investor in OpenAI it seemed more likely we'd have to wait for OpenAI to copy the feature set (as they did in April with [Workspace Agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)) and then wait for Microsoft to amend that feature set into the Copilot ecosystem. However perceptions were turning and Claude was becoming the tool du jour for a lot of scenarios. Microsoft made the smart move to do a deal with Anthropic and bring their Cowork solution into the Copilot ecosystem, releasing it into the Frontier programme on 30th May. So here we are, Anthropic models and agents, running inside your Microsoft tenancy.

At the time of writing Copilot Cowork is only available as part of the Frontier programme which means you're going to need to ask your friendly local administrator to give you access if you want to use it.

Cowork isn't just about having new Anthropic models inside Copilot Chat, it's a agentic system where you can leave the agent to go and perform actions on your behalf. The most common scenarios most people get started with is organising your calendar, setting up meetings with agendas and pre-read documents, and general content creation. What makes it different is that you can create content (documents, presentations, spreadsheets, pdf), organise meetings, send emails, perform deep research and chain all these things together into workflows that perform actions with very little prompting. For knowledge workers this huge. 

It has also brought into the Copilot ecosystem the idea of [Skills](https://learn.microsoft.com/en-us/agent-framework/agents/skills). As the etymology suggests it's about building small prompts, that perform one specific action (or skill) very well. The structure of this is formatted into specific SKILL.md files and there are lots of examples out there for things like summarise this document in a specific format, prepare for 1:1s or schedule a specific type of event. Get your head around that and then the real power comes from being able to compose multiple skills together to achieve a single task. 

The most extreme example of this I've been able to come up with has been: organising a management meeting. Think about it - arranging the meeting at suitable time without holidays or conflicts, building out content for multiple topics e.g. project updates, financial information, risks and issues and sharing that content before the meeting. All of that could be done with a set of skills, one to organise the meeting, one for each content type and pulling it together. Sometimes that could take a day to create content and arrange can now be done independently by an agent in less than 30 minutes.


## What's different to Anthropic Cowork

Despite being based on the customer product by Anthropic ([Claude Cowork](https://www.anthropic.com/product/claude-cowork)), there are some key differences.

* Claude Cowork is a consumer product and therefore has hundreds of MCP connectors for virtually any service your using. This is only of note if you're a company that uses some of these services such the Google Suite, Slack or JIRA. I suspect that Copilot Cowork will expand it's reach of out-the-box MCP servers but it'll likely be take a little while longer. 

* Claude Cowork is also able to work locally on your machine via the Claude Desktop application, which some will find useful, although if most of your work files are in OneDrive (as they should be) then you won't notice this as much when using Copilot Cowork. Microsoft has now released [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/) as there alternative to this, but it's a separate Frontier service and slightly separated at the moment. [Check it out](https://www.youtube.com/watch?v=PoSWJl3xWrI) though if OpenClaw has you excited.

* Copilot Cowork obviously shines in the place where you would expect it to - the workplace. With it's access to everything you have access to inside your tenancy via [Work IQ](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/), it means it knows about your meetings, emails, teams conversations, files you've created, your team structure etc. This is the huge upside for day-to-day knowledge work and building your own processes. Having using both versions of Cowork it certainty feels like a "work version" vs a "personal version".

* Copilot Cowork also has the upper hand when it comes to the mobile app. The Cowork agent has been rolled out into the Copilot mobile app which is very useful for keeping tabs on longer-running tasks or kicking off tasks when the moment strikes you. You can do the same with Claude Cowork via it's [dispatch functionality](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork) but that requires the desktop application running on your machine somewhere else - not the ideal experience.

* One last notable difference is that the format and structure of skills is slightly different. This becomes relevant when your looking at all those skills shared in the wider community that you might want to make use of. Fortunately Microsoft has thought of this and provides [tools to support the conversion](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development#convert-an-existing-claude-plugin).


## The current limitations

At the time of writing Copilot Cowork is still in Frontier, which means it's going to have a few rough edges, limitations and possibly even a few bugs here and there. Sometimes when adopting a new product in it's early release phase those edges can become frustrating if you're finding them for the first time and didn't know they were there. 

### Number 1: Creating that first skill
After you've got past the demo prompts like organising your calendar, the first thing your going to want to do with Cowork is create a skill. Here is where you're likely to run into your first issue. Copilot Cowork needs to create it's own skills, at least in the first instance. Cowork stores skills in a folder on OneDrive at ```<One Drive>/Documents/Cowork/skills``` but if you try and create a skill by manually creating the folder and SKILL.md file here then Cowork will fail to be able to see it. What you need to do first in have Cowork use it's skill-management skill to create the skeleton for you first and only then will Cowork know the skill exists and at that point you can choose to manually amend the SKILL.md file as you see fit and it will sync correctly.

### Number 2: The OneDrive sync issue
I'm pretty lazy so most of my skills have been created and amended by Cowork itself, but this is where you can run into issue number two: the OneDrive sync problem. When the skill-management skill creates skills for you there are two things that happen: it writes the skill for you into the current session (so that you can interact with it and test it) and it also writes the skill to your OneDrive so that you can immediately start using it in other sessions. However sometimes this second part fails. 

Each Copilot session sits within it's own container, with the ```.claude/skills/``` directory as a FUSE mount to the skills folder on your OneDrive. When the skill is first created it is just written to the local file system cache on the container. Copilot is often nice enough to tell you that it will take 35 seconds before it can be used in another session however it's often a considerably lot less than this. This 35 seconds is two parts: the ```rclone flush``` which forces the local changes back to the remote mounted file system and the upto 30 seconds for the backend blob storage to re-sync with your OneDrive. It's this second part where you can see failures as it's a asynchronous job that will occassionally fail. Copilot cannot force a restart of this background task, which means when it fails your basically stuck. I have come across this many times over the past few weeks while creating skills, enough to be annoying but not enough for me to stop using it. The workaround is pretty basic - just have Copilot export the skill to a zip file and unzip it back into your local OneDrive skills folder. The next session will refresh skills from OneDrive as normal.

### Number 3: The 50 skills limitation
There is currently a limitation on the [total number of skills to 50](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-faq#can-i-create-my-own-custom-skills). I've not personally hit this limitation just yet, but I am starting to see a path towards where that might be possible. I think the unfortunate answer to this is that you might start to see more monolithic skills be created that can perform multiple jobs which I don't see as the original the intent for skills. It's not clear if this limitation is due to a technical reason behind the scenes or an artificial limitation set to limit skills usage and encourage more advanced development. While skills are easy to create and use there is a point with which the more complex it becomes the more time likely it is that Copilot Studio is a better solution and building your own agents.

### Number 4: Copilot Cowork vs Copilot Chat
At the moment Cowork and the normal Copilot chat interface exist somewhat isolated from eachother. While both live within the same tenant and therefore have access to the same data, Cowork can only use skills and does not have access to all the other Copilot agents. In addition there is no way to trigger a Cowork session from an event in Power Automate in the same way you can with Copilot. 

For Cowork usage this requires some slightly odd behaviour in order to get work done. Cowork is somewhat limited in what is can do outside of the chat session itself, with emails, Teams messages and Planner tasks being the scope of it's capabilities. In order to have Cowork get real work done, it means using one of these three aspects as triggers for Power Automate workflows. While I love Cowork, I've spent as much time in Power Automate as I have in the Cowork interface itself while using it. Getting it to create documents is great. Having to email documents to myself to trigger another workflow outside of the chat session feels really clunky.

What this also means is that when I have a problem I want to solve with Copilot it has to start with the question "which tool is the right one for the job?". Do I use Cowork skills? Do I just need a prompt to orchestrate some existing Copilot agents or do I need to built my own agent? This is not an exact science and I've found myself starting down one path, hitting a road block and move to the other.

## What I use it for

So by now you're probably wanting to know what things I am using Cowork for (and how I found all the edge cases). So here are some examples.

### Branded documents
This is almost certainly the first skill that every Cowork user will try and create. Given that the word, excel and powerpoint skills for the actual content creation are already built in, this is about building a skill that focuses on your company branding, your colours, your text style, your iconography. You do already have a brand guide right?!

**Lesson learnt**: Your typical corporate brand guide probably won't cut it on it's own. Claude needs to know about accessibility rules like don't put red text on a black background and some common design rules like don't put things with round corners next to things with square corners. Also, it's worth noting that Claude has a very particular visual style built into the default skills, I'm sure you have seen some of it's generated content already. Expect to spend some time really tuning your skills so that they feel less like Claude and more like the corporate branding you want it to be - heck! maybe even get your existing designers to focus on this.

### Organising meetings
Organising meetings is such a common task that Cowork has the prompt already built in to help with this task, which is a great first start but I found it didn't go far enough. There are a lot of small decisions I make when managing my calendar manually: what types of meetings to move, when to shrink a meeting and when not to, what meetings to cancel, what meetings to mark as follow, how to handle clashes. All of these rules are decisions I make based on how I categories events, who it is and what my priorities are; suffice to say these are unique to me. Creating a skill that is unique to your calendar management workflow is one of the biggest gifts you can give yourself - this is one of the things that has contributed significantly my increase in productivity.

**Lesson learnt**: be explicit about what events it can cancel automatically and which will require your approval before hand. The same goes for emails. In fact you may need to be explicit in the future if Microsoft start enforcing some of that behaviour due to the recent [exfiltration issue](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files).

### Arranging focus time
Time blocking has been a productivity technique for knowledge workers for many years. Microsoft has supported [creating focus time blockers in your calendar for you since 2019](https://www.microsoft.com/en-us/microsoft-365/blog/2019/05/06/build-2019-people-centered-experiences-microsoft-365-productivity-cloud/), way before the Copilot was launched. I've used this technique for a long time and it is very useful, but it also used to take a quite a bit of effort to actually manage - oh the irony! Actions from meetings going onto my todo list, making sure that I had focus time for each of those actions, and moving those meetings around, it was a lot of work sometimes. 

With Cowork and a little Power Automate, I've now been able to automate the entire process. Tasks get added to Planner based on meeting transcriptions and I get a daily overview of any tasks that don't currently have focus time assigned. Cowork will also create focus time blocks for me, link those blocks to the planner task and then with the meeting organising skill I mentioned above also make sure it fits in with the rest of my calendar. This was by far this biggest productivity gain for me.

**Lesson learnt**: Cowork and Copilot chat are two separate worlds in the same interface. You can't use Copilot agents in Cowork and Cowork at the moment has a limited set of integrations. It can send emails, create events and create basic planner tasks - those are your only integration points. Files created within Cowork also only live with the session, so in order to get them out you need to email them to yourself. I have been using emails and calendar events as the the trigger points for some of the Power Automate flows that really makes this skill sing. The real lesson for me here has been that any sufficiently complex skill will eventually require you to spend time in Power Automate, just like any sufficiently complex Copilot work will eventually require you to get into Copilot Studio.

### 1:1 management
I am a manager with currently 13 direct reports, which means on average I've got 4.5 hours of 1:1s every week, plus ad-hoc 1:1s with many other people across the business which sometimes being that total up to closer to a day per week. That's fine, it's part of my job, but that also means a lot of meeting transcripts and a lot of actions. I now have a skill that reads the transcript, provides a summary, creates actions on a planner board shared between me and the other person and exports the summary, actions and transcript to a word document to be used as a permanent record of the meeting.

Hold on, doesn't that sound like [Copilot Facilitator](https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings)? Well yes, but that didn't really work for me and there were a few lessons along to way in putting this one together.

**Lesson learnt**: You can't automate Microsoft Loop. It doesn't have an API and the only way to get data out of it is as a manual print to pdf export. When Copilot Facilitator is added to a meeting it automatically transcribes, summarises and creates actions - so far so good. However it creates those actions in a Loop page per meeting and critically it doesn't even assign those actions. When a tasks is assigned in Loop, it's great because they appear as tasks in planner, but it still requires manually going to every loop page to review and assign tasks. It somewhat negates the productivity gains Facilitator thinks it's giving you.

**Lesson learnt**: Most folks, especially in 1:1 are ok with transcript but don't really like recordings. Having transcript enabled is the minimum requirement to make this automation work effectively. While I was developing this, it mean having to manually enable transcript at the start of each meeting (which I didn't always remember to do), however at the time of writing Microsoft has now released a meeting setting for "Transcript only" (even if it did have a bit of a [buggy role out](https://learn.microsoft.com/en-au/answers/questions/5890165/unable-to-select-transcribe-only-in-teams-meetings)) which can be set on each scheduled event.

**Lesson learnt**: One thing I didn't like about using Facilitator was that it didn't assign the tasks that it created despite knowing who the person was because it would always include a persons name in the task description. This was something that I wanted to solve when creating this skill, and did so with Power Automate, however translating from AI to actions didn't improve much and there still remains the manual activity for me to sanity check the actions in creates on the planner. This might be one of those things that after having spent time reviewing actions for a few months I might have a better idea on how to improve the automation based on rules - at the moment it's just a little too complex for that.

### Timesheets

Given that I work in a organisation that delivers professional services, timesheets on a core part of our day-to-day life, be that filling them in or approving them. This is one skill that I developed, which was very quick to put together, but also requires a very specific set of supporting workflow that might not be for everyone. 

Before I get into explaining the skill let me explain how I manage my time. I have for many years now used [time blocking](https://ctl.stanford.edu/weekly-planning-time-blocking-method) and [event colour coding](https://blog.splibrarian.com/2021/01/25/pro-work-tip-for-2021-build-a-color-coded-work-calendar/) to great effect. Looking at my calendar at the start of a week is often a rainbow of colours. This is not something that is a difficult to set-up and maintain as it sounds - set once for recurring events, a few email rules here and there and most of it is done. The background context of having this workflow is important because this event-to-category mapping is meta data that my timesheet skill will use later.

Putting together a timesheet is generally pretty straightforward, what I need to know is how much time I spent on certain projects or internal activities. Sounds like the time blocking I'm already doing, right? Well all I needed this new skill to do was map my time categories to projects, go through all the events in my calendar to calculate the total time spent, and produce a little summarised comment for each time record. Nice and easy (mostly!).

**Lesson learnt**: Rules on conflict. This took a bit of tuning to align to my own working habits. Examples such as how to handle "tentative" or "following" meetings, how to handle meetings where you join only for a few minutes and then do something else and how to handle sensitive meetings where you don't want details to appears in the commentry summary. Also, how to handle gaps in the calendar (that one took some head scratching!). All of these have nothing to do with the technology of developing the skills but speak quite a lot to the fact that most of the effort that goes into skill writing is writing down all of those rules about how you work, how you want things to happen and how you handle edge cases - lots more thinking time than actual keyboard time.

## Where Cowork fits into the wider Copilot ecosystem

The Copilot ecosystem is now large and quite complex: [Copilot Chat](https://copilot.microsoft.com/), [Microsoft 365 Copilot Chat](https://m365.cloud.microsoft/chat/), [Microsoft 365 Copilot in Office](https://support.microsoft.com/en-gb/topic/get-started-editing-with-copilot-in-office-6d043333-6eeb-49d8-a80c-681d29ab7c04), [Copilot Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/) and [GitHub Copilot](https://github.com/features/copilot) and [Microsoft Scout](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)

The best way to understand these and how you can use them is through four different modes:

1. **Chat Mode** - your day-to-day chat interface, question-and-response, likely replacing search for most people (primarily OpenAI-backed).
2. **Code Mode** - your development environment, writing and editing code on your behalf (using GitHub Copilot)
3. **Cowork Mode** - your on-demand, multi-step assistant. Delegate and move on (Anthropic Claude-based)
4. **Scout Mode** - your automated, background assistant (OpenClaw-based)

It is important to understand these modes for many reasons, first because each will have a different role in your day-to-day depending upon the requirements of your job, but it's likely that each will be used at different times. Also, because each is backed by different models, the economics of each will be quite different and at scale this will be a consideration. Finally, how each of these is developed, with skills, agents, and prompts will be slightly different.

As usage of AI matures it is important to understand each of these operating modes as well as when it's best to use a skill, when it's best to use an agent, when you should use traditional automation and when you should write software. Each of these are tools have specific trade-offs in terms of speed, security, stability and economics and each will have it's place in our futures.

## What's up next

I am far with finishing my experimentation with Copilot and Cowork and both tools also have a long way to go. There are a few areas however where I intend to spend a bit more time

* **Windows 365 / Project Opal** - taking the AI output and using that to automate systems through the browser using a Windows Cloud PC. For things like my timesheet skill this will be where it will actually complete the timesheet on my behalf or complete expenses for me. A huge time saver.
* **More agents** - I am particularly interested in the QA agent pattern. Using Cowork for document generation, with me in the loop for editing and then an agent that runs a standardised QA process before releasing it. I guess this is similar to a more traditional continuous delivery process. The limitation in Cowork now is that it doesn't really support many agents, especially even those that the main Copilot interface does - I expect this to change soon.
* **More MCPs** - Cowork is currently limited by it's out-the-box integration with a lot of tools, unlike it's big brother, however I do expect more of these to be validated and released as this moves out of Frontier.

Finally, I would expect things to change a bit as Copilot evolves into the [new unified interface](https://robquickenden.blog/2026/06/what-is-microsoft-scout/), so despite all the challenges I have mentioned here the overall direction is very clear - lots more skills, lots more integrations, lot more automations, lots more money but plenty of time saved. 
