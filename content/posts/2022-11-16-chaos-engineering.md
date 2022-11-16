---
author: "liamjbennett"
title: "Chaos Engineering - fact or fiction"
date: "2022-11-16"
description: "The realities of chaos engineering and steps to get there"
tags: ["chaos engineering","testing","disaster recovery"]
ShowToc: false
ShowBreadCrumbs: false
---

## Intro (what even is it?!)
I have been a developer and a DevOps engineer (or whatever the latest title is now) for most of my career and I like my systems to be reliable and well architected. I like being confident that when the unexpected happens, and it always does, that the systems that I am responsible for can handle it and not wake me up at 2am. 

When I talk to developers, I'm often talking about testing and the testing pyramid - we all know it's value and the positive investment that it is. The more testing of our systems we have the earlier we see bugs, the more reliable the application. It's a fairly simple statement but its still worth reiterating because of how easy is it to neglect in fast-moving customer/feature driven teams.

When I talk to operations folk, I'm often talking about business continuity and disaster recovery - we all know its value but more often that not disaster recovery is a tick-box exercise for compliance. DR environments, bought and paid for to fulfill compliance requirements, are often not tested and are therefore are a risk in themselves. If not producing meaningful value one could argue they are a compliance-tax. In order to gain some of that real value they need to be tested comprehensively and often. So why aren't they? In most organisations I've worked with, the reason these systems are never tested or failed-over to is because of risk (ironic huh!). The perceived risk of causing downtime if the DR system and process doesn't work is felt to be worse than the risk of an real incident that may or may not happen in the future. So it sits there at great expense, providing false confidence.

But you came to this post to read about Chaos Engineering not boring old DR. Chaos Engineering sounds scary because it's got Chaos in the title - but that's what makes it cool, right?!

Chaos Engineering was born out of [Netflix circa 2011](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) and launched into the public consciousness with the release of their first tool Chaos Money which disables computers on a network to see how the other components of their applications react. During the following couple of years they released a series of similar tools, collectively known as the Simian Army to trigger other types of failures. The premise was simple - write an experiment, run the tool, see what happens and quickly remediate the problems - sounds like testing, huh?! 

What sets Chaos Engineering apart from regular testing however is when and where those experiments are run. By simulating failures in lower/non-production environments it is possible to build confidence and find problems earlier on in the process and by promoting those experiments into staging and production environments you're validating the reliability of those systems. Chaos Engineering really leans into its namesake when you have sufficient confidence to run those experiments at random intervals thereby introducing controlled entropy into your complex distributed system and ensuring that most known large failures are handled regularly and consistently. This also acts as evidence for compliance auditors that your reliability and disaster recovery plans are real and executed rather than a nice idea on paper.

## Fact vs Fiction (challenges and reality)

Ok, well that's great - but what happens if you're not a FAANG company or a tiny start-up? Does this even make sense? 

The question I was asking myself was - is anyone actually really doing this? If so, at what scale? That was the question I posed to the room at [DevOpsDays London 2022](https://devopsdays.org/events/2022-london/welcome/). What I heard back from the group there was what I was suspecting - that everyone seems to understand the ideas and principals but that the risk and the cost of investment doesn't appear to be worth it.

This all feels like the conversations I was having about testing and automated testing in the mid-2000s, there were people doing it but there was still a lot of conversation about how to manage it and what its real value was. At the time there were plenty of arguments (and still are) about too much unit testing, flaky end-to-end tests and investing too much in testing vs shipping features. Today the arguments against Chaos Engineering are about investing in large-scale failure testing, how much time should be spent on this vs shipping features.

With software, there are bugs, and everyone now seems to understand that developing tests finds bugs sooner in the lifecycle. It is therefore a cheaper investment than the cost of finding those bugs in production. The same is true of Chaos experiments. Those experiments, however complicated the solution, are cheaper and more cost effective than having to fix that failure (rebuilding infrastructure in another region, anyone?).

But in my conversations with engineers and with customers the real issue has nothing to do this understanding or the cost that the investment might need. The real reason that this hasn't taken off is because Cloud providers are very good at their jobs! That's right, because Amazon, Microsoft and Google have invested billions of dollars into ensuring their infrastructure is reliable (probably using some of these same Chaos techniques) most ordinary DevOps teams don't see the sort of reliability issues that they may have seen 10-15 years ago. When an AWS region has near 100% reliability (for those outside us-east-1) then the argument for investing time and money to write experiments that test that failure scenario seem to not add up. This is a totally valid and realistic reason for not investing in Chaos Engineering.

But wait, isn't this blog meant to be espousing the virtues of Chaos Engineering? Well, yes, it is. 

The mistake people make in the conversations about Chaos Engineering is by assuming that these experiments have to be testing the big failures - region outages, DNS failures, Authentication chaos. That comes back to the history of the types of tools Netflix initially released - they were big tools for big problems because Netflix were building a big platform for massive scale - but 99% of us aren't working at Netflix. My experience working almost exclusively with all 3 major cloud platforms is that the big failures are very rare, more common are much much smaller failures. Individual services fail (see the public status dashboard history of any provider) and often those failures only impact a small subset of customers - so called brownouts. These are the types of scenarios to plan for, and to test with, Chaos Engineering. What happens to your application if Lambda executions are slower? What happens if a single AppService goes down? Does your application recover gracefully when that CloudSQL database starts dropping connections?

## How to start and see some benefits

So the trick is, start small. Prepare for those brownout scenarios and start with one test, then another, then another. No big, upfront investment, no massive disaster recovery test. Just small, incremental coded experiments, running regularly forcing your application and infrastructure teams to think about failures and reliance - not because it might fail, but because it will fail and you're just being prepared. Already seen a service failure? Make that an experiment so you're prepared for next time.

You might not even have to invest in much of this yourself, there are now tools and providers that understand these scenarios and can support you in testing each of the component failures and how you can improve your architecture, your release pipelines and your processes to better meet this requirement.

Give it a go and let me know what you think..