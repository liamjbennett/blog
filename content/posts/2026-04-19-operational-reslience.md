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

The topic of operational resilience has been around for decades, with extensive research following not just the technical aspects of IT failures and cyber-security incidents but also the contributing human factors and organisational behaviours. With all these years of research and review you might think it surprising that it's such a hot topic again. Like many things in IT, there is a cycle of major incident, learning, new technology trend, and major incident again. From the early days like Y2K and ILOVEYOU, through Heartbleed and WannaCry to the more public Azure and AWS global outages, the pattern is consistent. Ensuring that we have systems in place to prevent mistakes and malicious intent continues to be a priority but the repetition of the large-scale events, not to name the millions of smaller ones, makes clear that prevention is not sufficient. 

Operational resilience has emerged again as a hot topic within the UK, not only because of the recent public cloud outages but also because of high-profile retail cyber attacks and increased focus on supply chain issues due to changes in the global political climate. 

What are we going to do differently this time? Also, is there anything we can do to predict where the next event might come from?

## What resilience actually looks like

Every organisation I have spoken to, large and small, treats operational resilience more like operational robustness, focusing on the prevention of failure. Backups, annual disaster recovery testing and compliance check lists and are cornerstone of this practice. Confidence is built based on designs, audits, and spot-check testing of critical assets. 

The challenges I see when speaking to new customers are extensive:
* Backup restores tested infrequently and at varying levels of granularity.
* DR tests only performed annually and only for a sub-set of assets.
* Assumptions of the availability and capacity of cloud platforms and SaaS vendors.
* Assumptions on the ability to quickly restore platforms built with infrastructure-as-code.
* Limited visibility of supply chains and the impact of their outages.
* Limited testing of cybersecurity processes (through table-top exercises or red-team events)
* Limited incident response or critical event training.

I do not pass judgement on any organisation that faces one or more of these challenges. Solving these issues is a matter of trade-offs of time, cost and risk. However, even in highly regularity organisations such as financial services where impacts could have critical national side-effects, I still see some of these challenges which tells me that even laws and regulations are not sufficient to prevent you from outages.

But it is not all doom and gloom, I am working with some organisations that are taking this more seriously and focusing less on robustness and more on resilience. This is where you assume failure in every aspect of your system, your organisation and your supply chain. With this mindset, you are acknowledging not just the cycle of external events that may impact you, but also that the systems we build are complex and the humans in our organisations that run them are even more complex than that. By assuming failure, you can test separately for each failure scenario across all of your assets and applications as well as system-based and human-based operators. You still prioritise by risk and budgets, but you're doing so looking at the whole picture not just a small subset.

## How to stress test resilience

Failures can be broken down into three categories:
1. Platform issues - infrastructure, cloud, core systems (like DNS!)
2. Dependencies and supply chain issues - suppliers (SaaS), dependencies (other systems), ecosystems (other tools in use like Slack)
3. Operational and Human issues: people, processes, co-ordination.

Most incidents are a combination of all of these and knowing where to start can be difficult.

Testing the platform category is the comfort zone, it's where we look at backups and disaster recovery plans. Testing these is driven often by compliance obligations (e.g. DORA, FCA PS21/3 and ISO 27001) and often only triggered for critical applications. For those organisations not constrained by the legal or regularity obligations to do so, many don't perform this testing. Only [36% of organisations are testing their DR plans](), however we're starting to see that shift. If we look at the movement of penetration testing over the past decade we've seen the gradual shift from annual testing to a continuous approach, led by more frequent CVE released and supported by industry regulations such as [CBEST](). Given the current focus on operational resilience, one can make a reasonable assumption that the increase in operational outage events will follow a similar trajectory and require organisations to test their backup and DR plans more often than annually. 

Practically, this will mean that the full-site, fingers-crossed, failover will become a thing of the past. We're currently recommending starting at the very bottom of the stack, testing individual components such as virtual machines, pods, databases or network devices in order to build real confidence before moving on to applications, then processes and then finally sites. In addition to typical backup restores and high-availability failovers this also means testing those parts of your cloud infrastructure that typically don't get tested such as scaling groups, network rules and third-party connections. This is unhelpfully called [Chaos Engineering](), for which there are tools such as [AWS Fault Injection Simulator]() and [Azure Chaos Studio]() which help write even more extensive testing. This is not new as I started talking to people and [writing about Chaos Engineering]() in 2022, but few people were using it then and few people seem to be using it now. Mostly this appears to be about the fear of recovery, especially when it comes to data. Calling it chaos engineering, while certainly memorable doesn't help when trying to justify investment in infrastracture testing to your boss - who wants to introduce chaos into production?! Despite the naming choice, the methodology is sound, ensuring that those cloud elements like the network and scaling methods are tested - first in non-production and then when confidence builds also in production.

For dependencies and supply chains - the key here is old school network-level testing. Chaos Engineering to add in network rules that block IP addresses, ports and endpoints used by your external suppliers. What happens? Does your application gracefully fail or hard fail? Ok, don't start with that, start with the table-top approach. Not all dependencies are equal and therefore failing over to something else while ideal might not always be practical. If your CDN provider goes down, perhaps there are options to failover to something else, but if a payment provider is having issues perhaps this is less practical. The point here is to work through all these scenarios, build tests, write runbooks, execute those tests and ensure that your infrastructure and appplications fail gracefully and that your communication on failures (both internal and external) is of high quality. This is also true of more internal matters such as ecosystem failures. I don't know of any organisations actually testing for Slack or Teams outages but it's always an important part of business continuity planning to have a known altenative and that everyone knows what it is.

Finally, you have the most complicated resilience part to solve - the people part. This is an area in which there is extensive research and for which I will not pretend to be an expert (I will leave that to the likes of [John Allspaw](https://www.linkedin.com/in/jallspaw/)), but what I can say is that the basics go along way here. Scenario planning, table-top exercises involved all stakeholders, co-writing runbooks, scenario stacking and real-world testing go a long way to ensure not just that there are well understood and tested process in place but also that there is confidence in the teams and the pschological safety in place to have failures and review them with fear of reprisals. 

## The importance of understanding your supply chain

I don't think I really heard many people outside of the logistics industry use the phrase supply chains until after the covid pandemic. Now I hear it all the time as organisations look to better understand not only the vendors they rely upon but also where possible those second-tier vendors. This is really important because of second-order outages. A recent example I was part of was during the October 2025 outages for AWS and Azure. We had one unfortunate customer who, was deployed fully onto AWS, so had unplesant start to the month, but after recovery was soon hit again byt the Azure outage - this time not because of anything with own direct resilience efforts but because of a vendor who supplied content to them had their own outage. Given the number of sites down during this month, it made national news and provided visibility to the complexities of many organisations running on these hyperscaler platforms. For a few organisations I worked with this was the first time they were realising the platform their vendors were running on. This is not the best way to find out but now they know and can do something about it. The recommendation is engage early with your vendors and ask these types of questions. Where possible also get SLAs in place. Most vendors will provide some form of SLAs but they will make you do the leg work of measuring against them and asking for service credits, they certainly won't give you money if you don't ask. Get good at this and have a process for requesting credits from all your vendors. It's not really part of resilience but just some good basic advice.

## Ok, I get it - now what?!

If there is one thing to take away from all of this, it is that resilience is not the same as robustness. Robustness tries to prevent failure; resilience assumes failure will happen and prepares the organisation to absorb it, recover quickly and learn. That means testing across all three areas: platform, dependencies and supply chain, and people and process. It also means moving from annual reassurance exercises to regular, practical testing that reflects how complex systems and real organisations actually behave.

The good news is that you do not need a massive programme to begin. Start small, start weekly.

1. Pick one service.
2. Pick one realistic failure mode.
3. Run one test this week.
4. Capture one lesson and one improvement.

Then do it again next week. The point is not to perform heroics, it is to build organisational muscle memory.

If you are reading this and wondering where to begin, here is the challenge: within the next 14 days, run one cross-team resilience scenario and publish one decision you changed because of it. That single step will tell you more about your real resilience than another year of assumptions.
