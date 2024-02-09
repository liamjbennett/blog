---
author: "liamjbennett"
title: "Mixed Operating Models - part 1"
date: "2022-03-28"
description: "Understanding how ITIL and DevOps co-exist in an organisations landscape."
tags: ["ITIL","DevOps","Agile","SixSigma","teams","culture", "wardleymapping"]
series: ["mixed operating models"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: "https://dd1bd01h7j6z1.cloudfront.net/2022-03-28%20-%20mixed%20operating%20models%20-%20part%201%20-%20Final.m4a"
audio_length: "00:09:54"
audio_bytes: "19027927"
---

This month I wanted to start discussing a topic that has been going around and around in circles of conversation and thoughts for several years now - mixed operating models in IT organisations. There is a lot of ground to cover so stick with me over the next couple of posts and I’ll show you how and why this comes about and what we can do about it.

![WardleyMap](/img/2022/wardleymap-1.jpeg)

## The Problem

One of the most challenging aspects of operating IT systems in large enterprise organisations is that there is a complex web of applications, data and infrastructure of varying ages and levels of support. At one end of the spectrum there are homegrown applications supported by agile development teams releasing every two weeks (or more often - wooo!) and then at the other end there are big clunky corporate applications that support all the revenue and all the processes that get the job done day-to-day. One problem I’ve seen in organisations is process and culture that treats both of these applications (and everything in between) the same way. 

ITIL is the operating model du jour in these large organisations, and for good reason - it’s a well proven cross-industry standard which is periodically updated and written by folks who have spent decades in the ITSM world. The problem with ITIL was never the standard but the multitude of ways that it was interpreted and implemented by organisations wanting to provide a strong governance model. The DevOps movement developed as a result of these poor implementations and with a desire to have less process, more speed and a stronger focus on people, relationships and getting things done. It worked! Folks were removing process, removing box-ticking exercises, introducing code and pipelines to handle what had previously be done by people. Excellent. Sign me up. And many organisations did.

Well enough of the history lesson. Both of these models continue to exist and not because of the the laggards waiting for their pensions to kick-in but because of the reality that both of the models have a lot of value when they are used in the correct context. Then here is the problem - context. Many organisations that I see having been on this journey, they have either started adopting agile but it’s only one team in the corner, or they have kept the classic (v2,v3 standard) ITIL and force everyone through it or around it. There are even organisations working on SaFe (the scaled agile framework) which aims to have the benefits of both but in reality just absorbs whatever other frameworks and ideas are popular and wraps in all in classic enterprise governance.

## Mapping the landscape

So what’s the real answer to this problem? How do you move an organisation to a model that supports both the speed and flexibility of agile methods with the structure and controls of ITIL. Well the fact is, you don’t! The solution is, to quote Simon Wardley, to “***use appropriate methods***”. What works for your brand new shiny application that you’re deploying every day isn’t going to be what works or is even appropriate for a big corporate application where incidents could cost millions. Some applications weren’t even developed with the foundations for more Agile and Devops working practices. In what might become a trend in my blogs - **it’s all about context**.

Ok, so far so good. We need to use both, great. Well how the hell do we actually do that?

The first step is to understand exactly what each application needs. Are there any immovable requirements e.g. contractual or compliance that limits your choice and how you handle it? I suspect that you’ll think this list is bigger than it really is. If there aren’t too many of those, then next is to understand where is the application in its lifecycle within your environment. How you manage a brand new application vs an application you’re about to sunset in six months is going to be very different.

The second step is to map those applications - wardley map them based on their lifecycle and their inter-dependencies.

![WardleyMap](/img/2022/wardleymap-2.jpeg)

This will allow you to start having the conversations about what to do and where to focus your efforts. How many applications do you have that are commodity? How many of those in-house applications are your product or *truly* innovative vs could be replaced by a SaaS? Understanding your landscape of applications will allow you to work out what operating model would be most appropriate - Agile/Lean at the start of the lifecycle and ITIL/SixSigma at the end.

But a map isn’t just about showing current state - it’s about movement over time. Movement means understanding you market and understanding your internal politics. The market will move with or without you - today’s shiny toy will be the next decade’s commodity. The conversation is, are you going to be the company that’s ahead of it or the company that’s forced along with it?

Next up, you need to take that map and overlay the movement you see in the market and critically look at the inertia to that movement within your own organisation. There are lots of reasons for that inertia, not all of it laggards, but all of it structural and about business incentives. Try to get some of that down on paper. The better you know it and acknowledge it, the more you can do about it.

## The Transition

We also haven’t solved the culture problem of running multiple models - what do we do about that? Well here is where it all ties together. That movement of applications over time though both internal and external pressure will push an application from product to commodity and therefore from Agile/DevOps to SixSigma/ITIL. Time it too early and you’re slowing innovation and product evolution but time it too late and your “move fast and break things” could come at a heavy cost. It’s easy to visualise that Team A supporting Application B needs to be agile and Team B supporting Application C need to use SixSixma and ITIL but what happens when Application B becomes a core business-critical component or becomes a commodity in the market? How do you transition? When do you transition and how do you take Team A on that journey?

Let’s start with the timing. The timing requires up-to-date market data - what do other products in the market looks like? Do they have all the features you need and what does the pricing model look like? For any product you’ve developed to support your business you should be looking at other ISV products in the market for comparison. This is an iterative version of the build vs buy debate. When it’s not your core business and cost of building it yourself outweighs the cost of buying it (it usually does!) then it’s time to buy and therefore start making that transition into vendor management. You need to look at your options and the lifecycle of the application. Is this an application that was written at a time when there weren’t appropriate SaaS products and it’s time to just kill it off or is this an application that you want to maintain (either because of inertia, perceived value or because of how engrained it is)? Well, your approach to that transition will be quite different in each case.

Next up, the team that built that application, what’s their path forward? It could be one of one of two paths: something new or something higher-level. What approach you take will depend as much on the lifecycle of the application as it will on the type of people that you have in the team. Do you have a team of creative, innovators who are always looking at the next shiny tool, language or technology? Or do you have a team of folks who have engrained the application into the organsation, scaled it and introduced processes around it. I won't discuss this in too much detail here because Simon Wardley does an excellent description of these character types in [pioneers, settlers and town planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html). What types of people you need at each stage will be very different.

If you’re replacing the application with a SaaS product, think for a moment about what you’re buying - there is complexity, configuration and organisational knowledge. Someone needs to make sure all those products and SaaS applications are configured and stitched together. This is where the platform team comes in. It’s a common trend right now to have a platform team - a team focused on engineering enablement, productivity and pulling all those applications together into a bespoke solution. The platform teams sits exactly on the intersection (or the fault-line) of the agile and ITIL movement. They are building something totally bespoke for the organsation in an agile manner using products and services managed by often by ITIL processes.

If you’re choosing to decommission that application then the path is onto the next new shiny and novel development - here you need to creative, innovative, entrepreneur types.

There is also a third option - outsourcing. If you’re in an organisation with lots of innovators and not enough town planners or you find yourself with an application that should be a service or a commodity then outsourcing that may be the best option. Most outsourcing arrangements will provide the scale, process and compliance required and allow the organisation to focus on its core competency. Outsourcing sometimes comes with a bit of a bad reputation but in reality context is important and it’s a tool to be used at the correct point in the lifecycle. Moving to a cloud managed service is a form of operational outsourcing. Just ensure you demand excellence from your provider.

## The Implementation

So, now you understand your application landscape, the structure, the types of people supporting it and the support model you want to choose, right? Phew! You must be exhausted.

The next step is taking all that knowledge you’ve gained and turning into something operational, something you can track and something that allows you to indicate that operating model to the rest of the organisation. 

Well, keep your eyes peeled for next the next post in this series where I will show you exactly how to do that ....