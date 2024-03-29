---
author: "liamjbennett"
title: "6 things I learnt migrating to the cloud"
date: "2022-01-14"
description: "After many different migration and transformation projects; these are the things they don't tell you."
tags: ["teams","culture","tools","vendor","cloud","migrations","transformation","TCO"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: "https://dd1bd01h7j6z1.cloudfront.net/2022-01-14%20-%206%20things%20I%20learnt%20migrating%20to%20the%20cloud.m4a"
audio_length: "00:10:50"
audio_bytes: 22499496
---

I’ve had the opportunity over the past 5 years to be involved in many many different cloud migrations of all shapes, sizes and industries. From large-scale lift and shifts, native refactoring and even one or two cloud-to-cloud migrations. There are couple of things I have learnt along the way that appear to remain true irrespective or size, scope or type of organisation.

## 1. The cloud provider you choose isn’t the best technical fit but the best cultural fit

There used to be a trend when organistations were moving to the cloud to ask the question: *which cloud provider do we go with*? I still occasionally see this in RFPs for big multi-nationals. This lead to a lot of long conversations, commercial modelling, TCO comparisons and contract negotiations. After all of this work (for which we were handsomely paid) you were still left with a fairly long list of trade-offs that you were buying into and the decision was made based on an executive point-of-view associated with levels of comfort with the various risks on the table. Saying the decision was made based on trade-offs and risk is probably being a little kind. The truth in more often the whole exercise is one of confirmation bias to a decision that has already been made. 

So what really drives that decision in the first place? What I’ve observed is that the decision is based not on commercials or on technical best-fit, but on the alignment of the cultural values between the cloud provider and the organisation. There are already some well known tropes about this: you’re a windows-shop so you’ll choose Azure, most of your estate is custom applications on linux - you’ll choose AWS or you’re building a data project so you’ll choose Google. Well these are tropes for a reason but let me add something that’s always missing from these things - nuance.

The culture of organisations that typically select Microsoft Azure aren’t just those organisations with a heavy investment in Windows and the .net framework. Microsoft are a big partner-centered organisation with a large eco-system of partners and many of their engagements with customers will involve alignment of multiple parties. What I’ve discovered is that organisations with a large number of vendors and partners (application vendors, service providers etc) are culturally aligned with working in this same mode. Microsoft also appears to be the preferred platform for “back-office” or traditional IT environments.

Digital native organisations have been the mainstay of AWS since inception - strong in Retail, strong in ISV and SaaS providers. Now they are strong in every vertical and at the time of writing hold the dominant position in the market, not just because of the first-mover advantage but because they shaped their identity around transformation. Those organisations that I have seen self-selecting AWS are those who’s move to the cloud was “do it right, not do it fast”. Infrastructure was rebuilt not moved, applications were re-factored not shifted and in some cases existing vendors were unseated by that modernisation. That’s not to say that those more difficult (often legacy) components don’t migrate well, if fact AWS has done a lot in writing services to support these environments, but it’s just not aligned well with their culture or the culture of the organisations selecting them.

Google is still the corner-case - they are the “think different” brand. They are also the cloud provider that most folks associate with data services, and rightly so - it’s their strongest area. Organisations that select GCP are more often than not cloud-native, green field and data-driven. What I’ve seen is that data is not just the strongest of Google’s services but it’s very much engrained in their culture and how they see the world. Organisations where the infrastructure and even the applications matter less than the data and insights they provide, are the organisations that are most aligned with Google.

So what about the multi-cloud story? If each provider has a very different culture how does this work in mutli-cloud organisations? The multi-cloud organisations I have worked with are more often than not in that position based on the different sub-cultures within the organisation rather than any other technical reasons. Either different business units or different regions with an organisation have each selected a different provider (because it’s different people who make the decisions) and actually, that’s ok. 

Cloud in general is about being an enabler to the business and being an enabler means providing tools and services that people can use quickly, effectively and actively want to continue to keep using. As this really about the choice of people - the most effective cloud will be the one that the most number of people in the organisation get along with and that means the one that most aligns with their own needs and values.

## 2. The TCO doesn’t matter

Every cloud migration or modernisation activity I have seen (some more successful than others) has started in the same way: build a “why cloud” business case. At the better end of the scale this is an investment case to justify budget but at the worst end it’s a business case to track an ROI for cloud vs keeping it in the datacenter (and yes people still really think this is a valid argument). Somewhere in the middle there is the tick-box exercise business case where the decision(s) have already been made and it’s a paper filling activity for governance reasons. 

In either of the scenarios there is one thing that always comes up: the TCO (Total Cost of Ownership) which is the detail of the financial case. This can range anywhere from the cost of the projects cloud billing to a complete business case including people, cost of risk and even multi-cloud comparisons. There are many many tools in the market now to support this, all of which have their own focus areas and their own trade-offs - but it’s clearly a market solving a big problem. I personally spent 2 years building and maintaining a model for exactly this (ask me over drinks one day).

The unspoken reality however is that the TCO really doesn’t matter. In most cases any model produced is never referred back to once the first thing gets deployed in the cloud environment and in the rare case that it is - there is a quick realisation that there are so many known-unknowns when modelling cloud spend (e.g. bandwidth and real-world compute usage) that the model quickly shows the impact of it’s long long list of assumptions. 

My advice is to forget the TCO and even forget the ROI. If you’re not in the cloud already (and there are many that aren’t) or your not investing regularly in transforming your applications then the clock is ticking before you’re forced to by the market. It’s not a choice of if you’ll be investing, it’s just a case of when. It’s also not a case of how much it’s going to cost (which assumes it’s a one-off project) but it’s a case of how much you can afford to spend this year and next year and what you want to do with that budget.

## 3. The Vendors aren’t going anywhere

Whether it’s network, backup, patching, disaster recovery or corporate applications - there is always a vendor and rightly so. Most enterprise organisations will favour build vs buy when it comes to tools and applications and this means that many large estates have hundreds of vendor applications and infrastructure. There is a prevailing and addictive ideology that moving to the cloud will allow an all-in approach to cloud native services reducing the vendor landscape to only the chosen cloud provider. This idea is very much supported by the hundreds of cloud native services now available and the YoY growth in new services makes negotiating long vendor contracts a much riskier bet than it used to be.

Generally speaking, I support this ideological view - the decision should always be native first unless proven otherwise. That is where is get’s interesting however. The cloud providers take the wide and shallow approach to many of the services they develop, having set themselves into an an annual cycle of releasing newer services and setting an expectation that wherever there is a problem, however niche, there will be a tool or service to solve it. As a result they are all racing to be first to market and like any good product organisation they are releasing the basic feature set first to be followed with more advanced feature months and years later. Most vendors in contrast have a small product set, specialise in a one or two areas and go really deep into those. It means that there are many cases where the vendors can provide functionality where the cloud provider services cannot or at a price level that the cloud provider is unwilling to match. 

So what do we do about this? Well the choice is to embrace the vendors - but do so deliberately, tactically (not strategically) and with as short a time frame as it’s reasonable to negotiate. You want to use those vendor technologies to meet your needs now (cost or features) but give yourself the option to continually review those choices and expect to replace them with cloud native technologies in a couple of years time.

To use the language of wardleymapping - vendors live in the product/rental space, cloud providers dominate in the commodity space. Know where your applications and infrastructure are on their lifecycle and make the right choice accordingly.

## 4. You need a toolbox

Cloud migration and modernisation is a complex business. There are lots of standardised things: VM migrations, upgrades, IaC pipelines; but there are also a larger number of areas that maybe unique to your business, your industry, the types of applications you have or where they are in their lifecycle. Having been in many organisations and completed migration of different sizes and types the one thing that has allowed me and my team to be successful is ensuring we have a rich toolbox to use. What do I mean by that? I mean that for each of those 7R areas we have a potential solution no matter where the application is in it’s lifecycle. Want to move your first party python app to containers? Tick. Want to migrate your SQL 2005 instance to SQL 2019 on a linux docker container? Tick.  This requires a rich portfolio of options, some cloud provider tools, some vendor tools and some custom built tooling. 

The deeper you go, the more often you’re reviewing your estate asking the question: *what’s the next move?* then the more you will built up a collection of options that you can use for this transformation and the next. The more options you have, the more agile you can be as a business.

## 5. All the things that might happen will happen

I suppose this is an obvious an inevitable statement for any project or product development of any significant size or duration but I am reminded of this all the time. I’ve seen lots of examples of this that have come close to de-railing many projects I’ve worked on: services being down just at the minute you want to use them or when you least have time to waste, people not being available when you need them (for so-so many reasons, some work, some personal), and my personal favorite - undocumented service edge-cases (ask any cloud engineer about those - there is probably a whole conference track in there somewhere).

The point here is every risk, every assumption you make should have a plan (and that’s standard PM practice) but you should also test those plans, especially when these are regular risks and assumptions across multiple projects. No one needs to be in a position of twiddling their thumbs and going “well we did document this risk - so we’re just going to wait it out”. If you do this and test these assumptions your less likely to find yourself in a war-room scenario - the less of those the better.

## 6. It takes a village

The last lesson that I want to leave you with is that just like any cultural change isn’t just about changing the tools, any cloud migration or transformation isn’t just about the toolbox you have to deliver it; it is fundamentally about the people. This is the people you have on your team, the people your working with from the customer or the third-parties. Any reasonably-sized migration cannot be completed by a lone-wolf who knows everything. It takes diversity - of skills, of knowledge and of experience in order to be successful. So be reminded to invest here first, worry about the tools and the approaches second and you’ll find yourself moving forward a better outcome.