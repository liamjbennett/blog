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


## What's differnt to Anthropic Cowork

* Anthopic: operates locally on your machine, has hundreds of MCP connectors, only dispatch app
* Copilot: access to data inside the tenant (Work IQ), more focus on enterprise connectors, mobile app
* Format of skills slightly different - but [can be converted](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development#convert-an-existing-claude-plugin)


## The current limitations and what's missing

* creating skills
* syncing to onedrive
* power automate
* 50 skills - sub-skills
* full autonomy
* memory

## What I use it for

* Branded documents
* Organising meetings
* Arranging focus time
* 1:1 management
* Timesheets

## Where Cowork fits into the wider Copilot ecosystem

* Copilot Chat, Copilot in Office, Cowork, GitHub Copilot

## What's up next

* Project Opal / Windows 365 MCP
* More agents
* More MCPs
