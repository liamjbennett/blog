---
author: "liamjbennett"
title: "Getting started with Copilot Cowork"
date: "2026-05-16"
description: ""
tags: [""]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
draft: true
---

I've been using Microsoft Copilot Cowork since it's first day of release into the [Frontier programme](). It has had a significant impact on my productivity and for those few of us in the organisation going through out internal pilot of the tool. I've had so many conversations about it over the past six weeks that I felt the need to share my experience in the hope that you find it useful and get to share the experience with others.

I'm going to assume for the rest of this post that you have some experience with Microsoft Copilot, or at least experience with other similiar tools like Athopic Claude or ChatGPT. If you don't then there is some [great content out there]() that will help you [get started with Copilot]().

I started using Microsoft Copilot at work during the first part of 2024 and during the next 18-months it mostly replaced my use of enterprise search and google search. I'm not here to wade into [the AI debate](), I found early on that it aided in my productivity and I started using it for initial content drafting, although I wasn't too happy with the content because I could never get it to look like something I might write for myself. Honestly, after a lot of use I wasn't really a huge fan of the GPT models (either personally or professionally). With the release of the newer Anthopic models in the summer of 2024 and after plenty of conversations with people about these models I moved most of my usage over to an internal chat interface that used Sonnet (LibreChat using Azure Foundry). It wasn't quite a smooth as using Copilot and didn't have integration with enterprise search yet, but the output was just better, or at least I felt so for my usecases.

## Introduction to Cowork

A strategically significant thing happened in May 2026 - Microsoft announced Microsoft Cowork. Cowork was the product name for the agentic system built and released by Anthopic in January and part of their Claude product. Given that Microsoft was a heavy investor in OpenAI it seemed more likely we'd have to wait for OpenAI to copy the feature set (as they did in April with Workspace Agents) and then wait for Microsoft to amend that feature set into the Copilot ecosystem. However perceptions were turning and Claude was becoming the tool du jour for a lot of scenarios. Microsft made the smart move to do a deal with Anthopic and bring their Cowork solution into the Copilot ecosystem, releasing it into the Frontier programme on 30th May. So here we are, Anthopic models and agents, running inside your Microsoft tenancy.

At the time of writing Copilot Cowork is only availbile as part of the Frontier programme which means you going to need to ask you friendly local administrator to give you access if you want to use it.

Cowork isn't just about having new anthopic models inside Copilot Chat, it's a agentic system where you can leave the agent to go and perform actions on your behalf. The most common scenarios most people get started with is organising your calendar (i.g. moving meetings around), setting up meetings with agendas and pre-read documents, and general content creation. What makes it different is that you can create content (documents, presentations, spreadsheets, pdf), organise meetings, send emails, perform deep research and chain all these things together into workflows that perform actions with very little prompting. For knowledge workers this huge. 

It has also brought into the Copilot ecosystem the idea of Skills. As the etomology suggests it's about building small prompts, formatted into specific SKILL.md files, that do one specific action (or skill) very well. There are lots of examples but think about things like summarise this document in a specific format, prepare for 1:1s or schedule a specific type of event. Get your head around that and then the real power comes from being able to compose multiple skills together to achive a single task. 

The most extreme example of this I've been able to come up with has been: organising a management meeting. Think about it - arranging the meeting at suitable time without holidays or conflicts, building out content for multiple topics e.g. project updates, financial information, risks and issues and sharing that content before the meeting. All of that could be done with a set of skills, one to organise the meeting, one for each content type and pulling it together. Sometimes that could take a day to create content and arrange can now be done idependently by an agent in less than 30 minutes.


## What's different to Anthropic Cowork

Despite being based on the customer product Anthoripic Cowork, there are some key differences.

* Anthopic Cowork's focus is as a consumer product and therefore has hundreds of MCP connectors for virtually any service your using. This is only of note if your a company that uses some of these services such the Google Suite, Slack or JIRA. I suspect that Copilot Cowork will expand it's reach of out-the-box MCP servers but it'll likely be take a little while longer. 

* Anthopic Cowork is also able to work locally on your machine via the Claude Desktop application, which some will find useful, although if most of your work files are in OneDrive (as they should be) then you won't notice this as much when using Copilot Cowork. Given that OpenAI Codex now supports this same behaviour I think it is only a matter of time for Microsoft to iron out any security concerns around local machine access and bring this to the Copilot application as well.

* Copilot Cowork obviously shines in the place where you would expect it to - the workplace. With it's access to everything you have access to inside your tenancy via Work IQ, it means it knows about your meetings, emails, teams conversations, files you've created, your team structure etc. This is the huge upside for day-to-day knowledge work and building your own processes. Having using both versions of Cowork it certainy feels like a "work version" vs a "personal version".

* Copilot Cowork also has the upperhand when it comes to the mobile app. The Cowork agent has been rolled out into the Copilot mobile app which is very useful for keeping tabs on longer-running tasks or kicking off tasks when the momemt strikes you. You can do the same with Anthorpic Cowork via it's dispatch functionality but that requires the desktop application running on your machine somewhere else - not the ideal experience.

* One last notable differnece is that the format and structure of skills is slightly different. This becomes relevant when your looking at all those skills shared in the wider community that you might want to make use of. Fortunatly Microsoft has thought of this and provides [tools to support the conversion](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development#convert-an-existing-claude-plugin).


## The current limitations

At the time of writing Copilot Cowork is still in Frontier, which means it's going to have a few rough edges, limitations and possibily even a few bugs here and there. Sometimes when adopting a new product in it's early release phase those edges can become frustrating if you're finding them for the first time and didn't know they were there. 

### Number 1: Creating that first skill
After you've got past the demo prompts like organising your calendar, the first thing your going to want to do with Cowork is create a skill. Here is where you're likely to run into your first issue. Copilot Cowork needs to create it's own skills, at least in the first instance. Cowork stores skills in a folder on OneDrive at ```<One Drive>/Documents/Cowork/skills``` but if you try and create a skill by manually creating the folder and SKILL.md file here then Cowork will fail to be able to see it. What you need to do first in have Cowork use it's skill management skill to create the skeleton for you first and only then will Cowork know the skill exists and at that point you can choose to manually amend the SKILL.md file as you see fit and it will sync correctly.

### Number 2: The OneDrive sync issue
I'm pretty lazy so most of my skills have been created and amended by Cowork itself, but this is where you can run into issue number two: the OneDrive sync problem. When the skill-management skill creates skills for you there are two things that happen: it writes the skill for you into the current session (so that you can interact with it and test it) and it also writes the skill to your OneDrive so that you can immediately start using it in other sessions. Hoever sometimes this second part fails. 

Each Copilot session sits within it's own container with the ```.claude/skills/``` directory as a FUSE mount to the skills folder on your OneDrive. When the skill is first created it is just written to the local file system cache on the container. Copilot is often nice enough to tell you that it will take 35 seconds before it can be used in another session however it's often a considerably lot less than this. This 35 seconds is two parts: the ```rclone flush``` which forces the local changes back to the remote mounted file system and the upto 30 seconds for the backend blob storage to re-sync with your OneDrive. It's this second part where you can see failures as it's a asynchronous job that will occassionally fail and Copilot cannot force a restart of, which means when it fails your basically stuck. I have come across this three times over the course of a week creating skills, enough to be annoying but not enough for me to stop using it. The workaround is pretty basic - just have Copilot export the skill to a zip file and unzip it back into your local OneDrive skills folder. The next session will refresh skills from OneDrive as normal.

### Number 3: The 50 skills limitation
There is currently a limitation on the total number of skills to 50. I've not personally hit this limitation just yet, but I am starting to see a path towards where that might be possible. I think the unfortunate answer to this is that you might start to see more monolithic skills be created that can perform multiple jobs which I don't see as the original the intent for skills. It's not clear if this limitation is due to a technical reason behind the scences or an artificial limitation set to limit skills usage and encourage more advanced development. While skills are easy to create and use there is a point with which the more complex it becomes the more time likely it is that Copilot Studio is a better solution and building your own agents.

### Number 4: Copilot Cowork vs Copilot Chat
At the moment Cowork and the normal Copilot chat interface exist somewhat isolated from eachother. While both live within side the same tenant and therefore have access to the same data, Cowork can only use skills and does not have access to all the other agents. In addition there is no way to trigger a Cowork session from an event in Power Automate in the same way you can with Copilot. 

For Cowork usage this requires some slightly odd behaviour in order to get work done. Cowork is somewhat limited in what is can do outside of the chat session itself, with emails, Teams messages and Planner tasks being the scope of it's capababilities. In order to have Cowork get real work done, it means using one of these three aspects as triggers for Power Automate workflows. While I love Cowork, I've spent as much time in Power Automate as I have in the Cowork interface itself while using it. Getting it to create documents is great. Having to email them documents to myself to trigger another workflow outside of the chat session feels really clunky.

What this also means is that when I have a problem I want to solve with Copilot it has to start with the question "which tool is the right one for the job?". Do I use Cowork skills? Do I just need a prompt to orchestrate some existing Copilot agents or do I need to built my own agent? This is not an exact science and I've found myself starting down one path, hitting a road block and move to the other.

## What I use it for

So by now you're probably wanting to know what things I am using Cowork for (and how I found all the edge cases). So here are some examples:

* Branded documents
* Organising meetings
* Arranging focus time
* 1:1 management
* Timesheets

## Where Cowork fits into the wider Copilot ecosystem

* Copilot Chat, Copilot in Office, Cowork, GitHub Copilot

## What's up next

* Project Opal
* More agents
* More MCPs
