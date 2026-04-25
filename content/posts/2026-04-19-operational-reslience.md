---
author: "liamjbennett"
title: "The hot topic that isn't AI: Operational Resilience"
date: "2026-04-19"
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

The topic of operational resilience has been around for decades, with extensive research following not just the technical aspects of IT failures and cyber-security incidents but also the contributing human factors and organisational behaviours. With all these years of research and review you might think it surprising that it's such a hot topic again. Like many things in IT, there is a cycle of major incident, learning, new technology trend, and major incident again. From the early days like Y2K and ILOVEYOU, through Heartbleed and WannaCry to the more public Azure and AWS global outages, the pattern is consistent. Ensuring that we have systems in place to prevent mistakes and malicious intent continues to be a priority but the repetition of the large-scale events, not to name the millons of smaller ones, makes clear that prevention is not sufficient. 

Operational resilience has emerged again as a hot topic within the UK, not only because of the recent public cloud outages but also because of high-profile retail cyber attacks and increased focus on supply chain issues due to changes in the global political climate. 

What are we going to do differently this time? Also, is there anything we can do to predict where the next event might come from?

## What resilience actually looks like

Every organisation I have spoken to, large and small, treats operational resilience more like operational robustness, focusing on the prevention of failure. Backups, annual disaster recovery testing and compliance check lists and are cornerstone of this practice. Confidence is built based on designs, audits, and spot-check testing of critical assets. 

The challenges I see when speaking to new customers are extensive:
* Backup restores tested infrequently and at varing levels of granularity.
* DR tests only performed annually and only for a sub-set of assets.
* Assumptions of the avaliability and capacity of cloud platforms and SaaS vendors.
* Assumptions on the ability to quickly restore platfroms built with infrastructure-as-code.
* Limited visibility of supply chains and the impact of their outages.
* Limited testing of cybersecurity processes (through table-top exercises or red-team events)
* Limited incident response or critical event training.

I do not pass judgement on any organisation that faces one or more of these challenges. Solving these issues is a matter of trade-offs of time, cost and risk. However, even in highly regularity organisations such as financial services where impacts could have critical national side-effects, I still see some of these challenges which tells me that even laws and regulations are not sufficient to prevent you from outages.

But it is not all doom and gloom, I am working with some organisations that are taking this more seriously and focusing less on robustness and more on resiliance. This is where you assume failure in every aspect of your system, your orgnaisation and your supply chain. With this mindset, you are acknowledging not just the cycle of external events that may impact you, but also that the systems we build are complex and the humans in our organisations that run them are even more complex than that. By assuming failure, you can test separately for each failure scenario across all of your assets, applications as well as system-based and human-based operators. You still prioritise by risk and budgets, but you're doing so looking at the whole picture not just a small subset.

## How to stress test resilience

Failures can be broken down into three categories:
1. Platform issues - infrastructure, cloud, core systems (like DNS!)
2. Dependencies and supply chain issues - suppliers (SaaS), dependencies (other systems), ecosystems (other tools in use like Slack)
3. Operational and Human issues: people, processes, co-ordination.

Most incidents are a combination of all of these and knowing where to start can be difficult.

Testing platform is the comfort zone, it's where we look at backups and disaster recovery plans. Testing these is driven often by compliance obligations (e.g. DORA, FCA PS21/3 and ISO 27001) and often only triggered for critical applications. For those organisations not contrained by the legal or regularity obligations to do so, many don't perform this testing. Only 36% of organisations are testing their DR plans, however we're starting to see that shift. If we look at the movement of penertration testing over the past decade we've seen the gradual shift from annual testing to a continous approach, led by more frequent CVE released and supported by industry regluations such as CBEST. Given the current focus on operational resliance, one can make a reasonable assumption that the increase in operational outage events will follow a similiar trajectory and require organisations to test their backup and DR plans more often than annually. 

Practically, this will mean that the full-site, fingers-crossed, failover will become a thing of the past. We currently recommending starting at the very bottom of the stack, testing individual components such as virtual machines, pods, databases or network devices in order to build real confidence before moving on to applications, processes and sites. In additional to typical backup restores and high-avaliability failovers this also means testing those parts of your cloud infrastructure that typically don't get tested such as scaling groups, network rules and third-party connections. This is unhelpfully call chaos engineering, for which there are tools such as AWS Fault Injection Simular and Azure Chaos Studio which help write even more extensive testing. This is not new as I started talking to people and writing about [Chaos Engineering]() in 2022, but few people were using it then and few people seem to be using it now. Mostly this appears to be about the fear of recovery, especially when it comes to data.



## The importance of understanding your supply chain

## Ok, I get it - now what?!

