---
author: "liamjbennett"
title: "Mixed Operating Models - part 3"
date: "2022-08-22"
description: "DevOps, ITIL and the cultural changes"
tags: ["ITIL","DevOps","Agile","SixSigma","teams","culture", "wardleymapping", "outsourcing"]
series: ["mixed operating models"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/2022/operatingmodel-3-titlepage.jpeg"
---

![](/img/2022/operatingmodel-3-titlepage.jpeg)

In the first two parts of this series, I talked about the problem space of mixed operating models in an organisation, why it exists and how to prepare for it. In this post I want to talk about the most important and often most challenging element of operating mixed operating models within an organisation: the cultural change.

Any transition of working practices requires a corresponding and iterative process of empathetic change management, where with every modification and iteration, context is given for the changes, conversations are had with those who might be effected and (unlike many corporate change management initiatives) the process includes the input of those on the front-line of the changes. 

The first set of these conversations, I described in Part 1 - reviewing the applications and the landscape as a value-stream and as a wardley map. Ensure all the teams have the same shared understanding of the current state of your application ecosystem. With the foundation of this context beneath you it will allow you to have the next set of conversations - *what do we do about those applications on the right of the map?* 

Applications on the right side of the wardley map are either late-stage products or commodity services. This will be based on your teams view and understanding in the first set of conversations (as well as the lens, either micro or macro upon which you’re looking at the landscape) and you need to start answering the difficult questions: *is this core to my business? do we still want to be buying/managing this? how much is this costing us?* In these conversations it’s important to be very aware of the inertia and incentives at play. Moving between stages, whether deliberate or due to organic environmental pressures, has the result that the jobs of people developing and supporting those applications needs to change. The transition from product to commodity often means either moving to a PaaS service, a SaaS service or (more commonly in larger organisations) outsourcing to a third-party provider. The inertia will come flooding to the forefront when this conversation is had during the review of the wardley map. The most important part of this process is having those individual and very personal conversations about *what’s next for you?* 

So let’s look at those common options: Build-Upon and Outsource

## Build-upon

Either you, or your hosting provider are building a moat for themselves. The underlying application or service has become a commodity mostly because it’s been built-upon and therefore replaced by a higher-order service. 

This is most likely the path with the easiest set of conversations. This is a journey, your engineers will get opportunity to learn new skills in the high-order service while hopefully being glad to no longer have to concern themselves with the maintenance and support of the underlying components. 

Be wary of situations where you’ve built a rube goldberg machine with the application (it’s someone’s baby) or if you’ve got a bad case of “not invented here” in the organisation as this would make some of these conversations more challenged. In my experience these organisations are typically engineering-led organisations and often when these two scenarios emerge the personalities are always chasing “the next big/shiny thing”. This means that the strategic shape of this conversation can always be on the next shiny thing that can be built and worked on if they let go of the shackles of the current application.

With build-upon it’s unlikely that the operating model is going to change within the organisation itself: an Agile organisation will remain an Agile organisation because the new component or application they are now using will be in the custom-built phase while the existing component remains in commodity but not the teams responsibility. 

This is the typical scenario for PaaS or SaaS migrations.

## Outsource

The application or service is not core to the business, there are lots of other options in the market place and organisations who’s entire business model is just delivering that application or service at scale. If it’s not core to *your* business then outsourcing should be the direction of travel so your teams can focus only on those things that your business is unique in delivering. 

That’s the start of the conversation - start with why. *The purpose of this business is to do X, you joined this business to do Y not the delivery and maintenance of A,B,C.* By framing the conversation in this way it should make it clear to all that outsourcing would be the preferred option. It’s also important with conversations for any time of outsourcing that it’s included with “.. *here’s the next thing* *we need to focus on”* this allows people to be reassured about the future state and avoid the amygdala hijack of fearing for their jobs.

When framed in the context of a specific application and discussed in collaboration with those involved the outcome is likely to result outsourcing to a specialist provider for that application or service and having an ecosystem of small vendors (outsourcers and SaaS providers) stitched together.

> **NB**: With the agility that comes with having lots of small specialist providers, there needs be  a strong vendor management process and governance in place to help control this.

Outsourcing can often be a difficult conversation with teams because it’s typically not delivered and executed in the manner I have described here. Often when people hear the term outsourcing - they think about £MM contracts, long procurement cycles, poor service experiences and … redundancies. The challenge with this in large organisations is that it’s typically executed as a cost-saving exercise by a management team not for strategic reasons based on a well discussed collective knowledge of the application landscape and lifecycle. 

As mentioned previously, by focusing on the future in the conversation and moving folks on towards that future state in their day-to-day jobs you also set yourself up to avoid the ugliness of [TUPE]([https://www.hrreview.co.uk/hr-news/strategy-news/naomi-sansom-employment-law-outsourcing-tupe-not-tupe/56417](https://www.hrreview.co.uk/hr-news/strategy-news/naomi-sansom-employment-law-outsourcing-tupe-not-tupe/56417)) where employees can be transferred to the outsourced provider. This is common in some of these large GSI contracts.

Outsourcing like this does have its place however - these organisations (and at the time of writing I work for Claranet a large MSP in this space) a very adept at manage some of these legacy (typically EOL) applications. They can take a running service and it’s associated risk and package that up into a service and outcome for your business. This gives your team the time and freedom to work on the phase-2 process of killing off that application. 

The second most difficult challenge in moving to a model that includes outsourcing is not just preparing people in your teams for that change but also bring an ITIL operating model into your organisation if you don’t have it already. This was the main scenario that led me to write these post and I’ll discuss this a bit more below.

> **NB**: commodity is our business. I’ll note this, but it’s certainly not for everyone. What happens when you’re a logistics company, an insurance company, a bank, utilities etc - well then commodity services are your business. In this scenario your products and services are key to the economies of the countries in which you operate (you might even be considered critical national infrastructure) in which case a strong well governed ITIL process will already be familiar to you. The challenge in these organisations is moving in the opposite direction - being able to innovate and introducing Agile and Lean processes within a highly regulated environment. 

## Introducing change in small steps

There are a lot of [general change management]([https://open.lib.umn.edu/organizationalbehavior/chapter/14-3-organizational-change/](https://open.lib.umn.edu/organizationalbehavior/chapter/14-3-organizational-change/)) tips that I would quickly summarise here in the context of switching IT operating models:

- Single team and application at the time - Create small wins and time to adapt, learn and make mistakes.
- Communicate early and often - Show the first map, discuss it, change it and build trust.
- Explain the different models - Don’t assume that everyone understands everything about Agile, DevOps, SixSigma and Outsourcing. Don’t assume that everyone understands all the tools. Share the knowledge, share the context and work together.
- Hubris of outsourcing - don’t outsource too much, too early. Learn who your vendors are, how they operate, build relationships and change if it’s not working.
- Lead with purpose and value - [we all want meaningful work]([https://sloanreview.mit.edu/article/the-importance-of-meaningful-work/](https://sloanreview.mit.edu/article/the-importance-of-meaningful-work/)), so make sure changes to the application landscape and your operating models are done so from the perspective of what it means to the day-to-day lives of the people in those teams.

**Next time in this series** … DevOps and ITIL - working together with thoughtful consideration