---
author: "liamjbennett"
title: "The hot topic that isn't AI: Operational Resilience"
date: "2026-04-19"
description: "Operational resilience means assuming failure, testing platform, dependency and people risks regularly, and building the muscle memory to recover and learn."
tags: ["operational resilience", "testing", "chaos engineering", "disaster recovery", "supply chain"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
draft: true
---

The topic of operational resilience has been around for decades, with extensive research following not just the technical aspects of IT failures and cyber-security incidents but also the contributing human factors and organisational behaviours. With all these years of research and review you might think it surprising that it's such a hot topic again. Like many things in IT, there is a cycle of major incident, learning, new technology trend, and major incident again. From the early days like [Y2K](#ref-y2k) and [ILOVEYOU](#ref-iloveyou), through [Heartbleed](#ref-heartbleed) and [WannaCry](#ref-wannacry) to the more public [AWS](#ref-aws-oct2025) and [Azure](#ref-azure-oct2025) global outages, the pattern is consistent. Ensuring that we have systems in place to prevent mistakes and malicious intent continues to be a priority but the repetition of the large-scale events, not to name the millions of smaller ones, makes clear that prevention is not sufficient. 

Operational resilience has emerged again as a hot topic within the UK, not only because of the recent public cloud outages but also because of [high-profile retail cyber attacks](#ref-retail-attacks) and increased focus on supply chain issues due to changes in the global political climate. 

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

Testing the platform category is the comfort zone, it's where we look at backups and disaster recovery plans. Testing these is driven often by compliance obligations such as [DORA](#ref-dora), [FCA PS21/3](#ref-fca-ps213) and [ISO 27001](#ref-iso-27001) and often only triggered for critical applications. For those organisations not constrained by the legal or regularity obligations to do so, many don't perform this testing. Few organisations are testing their DR plans regularly and consistently ([TWC IT Solutions, 2024](#ref-twc); [Telstra International, 2026](#ref-telstra); [Woollacott, 2025](#ref-woollacott); [Keepit, 2026](#ref-keepit); [SecurityBrief UK, 2025](#ref-securitybrief)). The data on this topic is inconsistent and worthy of a further meta-analysis, however from what data there is avaliable we can see a trend towards further testing. If we look at the movement of penetration testing over the past decade we've seen the gradual shift from annual testing to a continuous approach, led by more frequent CVE releases ([YesWeHack, 2025](#ref-yeswehack)) and supported by industry regulations such as CBEST ([Bank of England, 2024](#ref-cbest)). Given the current focus on operational resilience, one can make a reasonable assumption that the increase in operational outage events will follow a similar trajectory and require organisations to test their backup and DR plans more often than annually. 

Practically, this will mean that the full-site, fingers-crossed, failover will become a thing of the past. We're currently recommending starting at the very bottom of the stack, testing individual components such as virtual machines, pods, databases or network devices in order to build real confidence before moving on to applications, then processes and then finally sites. In addition to typical backup restores and high-availability failovers this also means testing those parts of your cloud infrastructure that typically don't get tested such as scaling groups, network rules and third-party connections. This is unhelpfully called Chaos Engineering ([Chaos Engineering Community, 2019](#ref-chaos-eng)), for which there are tools such as [AWS Fault Injection Simulator](#ref-aws-fis) and [Azure Chaos Studio](#ref-azure-chaos) which help write even more extensive testing. This is not new as I started talking to people and [writing about Chaos Engineering](/posts/2022-11-16-chaos-engineering/) in 2022, but few people were using it then and few people seem to be using it now. Mostly this appears to be about the fear of recovery, especially when it comes to data. Calling it chaos engineering, while certainly memorable doesn't help when trying to justify investment in infrastracture testing to your boss - who wants to introduce chaos into production?! Despite the naming choice, the methodology is sound, ensuring that those cloud elements like the network and scaling methods are tested - first in non-production and then when confidence builds also in production.

For dependencies and supply chains - the key here is old school network-level testing. Chaos Engineering to add in network rules that block IP addresses, ports and endpoints used by your external suppliers. What happens? Does your application gracefully fail or hard fail? Ok, don't start with that, start with the table-top approach. Not all dependencies are equal and therefore failing over to something else while ideal might not always be practical. If your CDN provider goes down, perhaps there are options to failover to something else, but if a payment provider is having issues perhaps this is less practical. The point here is to work through all these scenarios, build tests, write runbooks, execute those tests and ensure that your infrastructure and appplications fail gracefully and that your communication on failures (both internal and external) is of high quality. This is also true of more internal matters such as ecosystem failures. I don't know of any organisations actually testing for Slack or Teams outages but it's always an important part of business continuity planning to have a known altenative and that everyone knows what it is.

Finally, you have the most complicated resilience part to solve - the people part. This is an area in which there is extensive research ([Weick, 1987](#ref-weick); [Hollnagel, Woods and Leveson, 2006](#ref-hollnagel); [Dekker, 2011](#ref-dekker), [Woods and Allspaw, 2020](#ref-woods-allspaw)) and for which I will not pretend to be an expert, but what I can say is that the basics go along way here. Scenario planning, table-top exercises involved all stakeholders, co-writing runbooks, scenario stacking and real-world testing go a long way to ensure not just that there are well understood and tested process in place but also that there is confidence in the teams and the pschological safety ([Edmondson, 1999](#ref-edmondson)) in place to have failures and review them with fear of reprisals. 

## The importance of understanding your supply chain

I hadn't heard many people outside of the logistics industry use the phrase supply chains until after the covid pandemic. Now I hear it all the time as organisations look to better understand not only the vendors they rely upon but also where possible those second-tier vendors. This is really important because of second-tier outages. A recent example I was part of was during the October 2025 outages for [AWS](#ref-aws-oct2025) and [Azure](#ref-azure-oct2025). We had one unfortunate customer who, was deployed fully onto AWS, so had unplesant start to the month, but after recovery was soon hit again byt the Azure outage - this time not because of anything with own direct resilience efforts but because of a vendor who supplied content to them had their own outage. Given the number of sites down during this month, it made national news and provided visibility to the complexities of many organisations running on these hyperscaler platforms. For a few organisations I worked with this was the first time they were realising the platform their vendors were running on. This is not the best way to find out but now they know and can do something about it. The recommendation is engage early with your vendors and ask these types of questions. Where possible also get SLAs in place. Most vendors will provide some form of SLAs but they will make you do the leg work of measuring against them and asking for service credits, they certainly won't give you money if you don't ask. Get good at this and have a process for requesting credits from all your vendors. It's not really part of resilience but just some good basic advice.

## Ok, I get it - now what?!

If there is one thing to take away from all of this, it is that resilience is not the same as robustness. Robustness tries to prevent failure; resilience assumes failure will happen and prepares the organisation to absorb it, recover quickly and learn. That means testing across all three areas: platform, dependencies and supply chain, and people and process. It also means moving from annual reassurance exercises to regular, practical testing that reflects how complex systems and real organisations actually behave.

The good news is that you do not need a massive programme to begin. Start small, start weekly.

1. Pick one service.
2. Pick one realistic failure mode.
3. Run one test this week.
4. Capture one lesson and one improvement.

Then do it again next week. The point is not to perform heroics, it is to build organisational muscle memory.

If you are reading this and wondering where to begin, here is the challenge: within the next 14 days, run one cross-team resilience scenario and publish one decision you changed because of it. That single step will tell you more about your real resilience than another year of assumptions.

## References
* <a id="ref-dora">European Insurance and Occupational Pensions Authority (EIOPA) (no date) Digital Operational Resilience Act (DORA). Available at: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en (Accessed: 9 May 2026)</a>
* <a id="ref-fca-ps213">Blythe, F., Phythian-Adams, J., Savoie, M.C., Dodding, E., Manhambara, P. and Rodriguez, J. (2025) 'UK Operational Resilience Rules: Are You Ready for 31 March 2025?', Data Matters Privacy Blog, 7 January. Available at: https://datamatters.sidley.com/2025/01/07/uk-operational-resilience-rules-are-you-ready-for-31-march-2025/ (Accessed: 9 May 2026)</a>
* <a id="ref-iso-27001">ISMS.online (no date) ISO 27001:2022 Annex A Control 8.13 Explained. Available at: https://www.isms.online/iso-27001/annex-a-2022/8-13-information-backup-2022/ (Accessed: 9 May 2026)</a>
* <a id="ref-y2k">Thomas, M. (2017) What really happened in Y2K? Gresham College, 4 April. Available at: https://www.gresham.ac.uk/sites/default/files/2017-04-04-MartynThomas_Y2K-T.pdf (Accessed: 9 May 2026).</a>
* <a id="ref-iloveyou">Byman, C. (2025) '25 years ago: The ILOVEYOU worm', BCS. Available at: https://www.bcs.org/articles-opinion-and-research/25-years-ago-the-iloveyou-worm/ (Accessed: 9 May 2026).</a>
* <a id="ref-heartbleed">Johns Hopkins University (2014) 'Heartbleed bug: How did it happen, and how do we know it won't happen again?', The Hub, 10 April. Available at: https://hub.jhu.edu/2014/04/10/heartbleed-matthew-green/ (Accessed: 9 May 2026).</a>
* <a id="ref-wannacry">CyberPeace Institute (2021) WannaCry is not history. Available at: https://cyberpeaceinstitute.org/news/wannacry-is-not-history/ (Accessed: 9 May 2026).</a>
* <a id="ref-aws-oct2025">Robinson, D. (2025) 'AWS outage exposes Achilles heel: central control plane', The Register, 20 October. Available at: https://www.theregister.com/off-prem/2025/10/20/aws-outage-exposes-achilles-heel-central-control-plane/1236001 (Accessed: 9 May 2026).</a>
* <a id="ref-azure-oct2025">Claburn, T. (2025) 'Microsoft Azure challenges AWS for downtime crown', The Register, 29 October. Available at: https://www.theregister.com/off-prem/2025/10/29/microsoft-azure-challenges-aws-for-downtime-crown/1253365 (Accessed: 9 May 2026).</a>
* <a id="ref-retail-attacks">Magee, T. (2025) 'Which UK retailers have been hit by cyber attacks in 2025?', Raconteur, 23 September. Available at: https://www.raconteur.net/technology/which-uk-retailers-have-been-hit-by-cyber-attacks-in-2025 (Accessed: 9 May 2026).</a>
* <a id="ref-twc">TWC IT Solutions (2024) 60+ disaster recovery statistics you shouldn't ignore in 2024. Available at: https://twc-it-solutions.com/blog/disaster-recovery-tips/disaster-recovery-statistics/ (Accessed: 4 May 2026).</a>
* <a id="ref-telstra">Telstra International (2026) 'Organisations in the US, UK and Germany unprepared for large-scale digital disruption, new study finds', PR Newswire, 14 April. Available at: https://www.prnewswire.co.uk/news-releases/organisations-in-the-us-uk-and-germany-unprepared-for-large-scale-digital-disruption-new-study-finds-302741040.html (Accessed: 4 May 2026).</a>
* <a id="ref-woollacott">Woollacott, E. (2025) 'Too many organizations assume they're more resilient than they actually are – UK firms are facing huge financial losses from IT outages and downtime', ITPro, 7 August. Available at: https://www.itpro.com/infrastructure/too-many-organizations-assume-theyre-more-resilient-than-they-actually-are-uk-firms-are-facing-huge-financial-losses-from-it-outages-and-downtime (Accessed: 4 May 2026).</a>
* <a id="ref-keepit">Keepit (2026) 'New survey highlights gap between perceived AI readiness and tested disaster recovery capability', Disaster Recovery Journal, 21 April. Available at: https://drj.com/industry_news/new-survey-highlights-gap-between-perceived-ai-readiness-and-tested-disaster-recovery-capability/ (Accessed: 4 May 2026).</a>
* <a id="ref-securitybrief">SecurityBrief UK (2025) 'UK leads world in critical cyber attacks but risks recovery gap', SecurityBrief UK, 20 August. Available at: https://securitybrief.co.uk/story/uk-leads-world-in-critical-cyber-attacks-but-risks-recovery-gap (Accessed: 4 May 2026).</a>
* <a id="ref-yeswehack">YesWeHack (2025) 'CVE surge: Why the record rise in new vulnerabilities?', YesWeHack, 28 January. Available at: https://www.yeswehack.com/news/cve-surge-record-jump-vulnerabilities (Accessed: 9 May 2026).</a>
* <a id="ref-cbest">Bank of England (2024) CBEST threat intelligence-led assessments: Implementation guide. Available at: https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide (Accessed: 9 May 2026).</a>
* <a id="ref-chaos-eng">Chaos Engineering Community (2019) Principles of chaos engineering. Available at: https://principlesofchaos.org/ (Accessed: 9 May 2026).</a>
* <a id="ref-aws-fis">Amazon Web Services (no date) Resilience testing tools – AWS Fault Injection Service. Available at: https://aws.amazon.com/fis/ (Accessed: 9 May 2026).</a>
* <a id="ref-azure-chaos">Microsoft Azure (no date) Azure Chaos Studio – Chaos engineering experimentation. Available at: https://azure.microsoft.com/en-us/products/chaos-studio (Accessed: 9 May 2026).</a>
* <a id="ref-weick">Weick, K.E. (1987) 'Organizational culture as a source of high reliability', California Management Review, 29(2), pp. 112–127.</a>
* <a id="ref-hollnagel">Hollnagel, E., Woods, D.D. and Leveson, N. (eds.) (2006) Resilience Engineering: Concepts and Precepts. Aldershot: Ashgate.</a>
* <a id="ref-dekker">Dekker, S. (2011) Drift into Failure: From Hunting Broken Components to Understanding Complex Systems. Farnham: Ashgate.</a>
* <a id="ref-woods-allspaw">Woods, D.D. and Allspaw, J. (2020) 'Revealing the critical role of human performance in software', ACM Queue, 17(6), 21 January. Available at: https://spawn-queue.acm.org/doi/full/10.1145/3380774.3380776 (Accessed: 9 May 2026).</a>
* <a id="ref-edmondson">Edmondson, A. (1999) 'Psychological safety and learning behavior in work teams', Administrative Science Quarterly, 44(2), pp. 350–383.</a>