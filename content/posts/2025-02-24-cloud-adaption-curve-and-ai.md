---
author: "liamjbennett"
title: "What the Cloud Adoption curve can teach us about AI"
date: "2025-02-24"
description: "We've all been on the ebbs and flows of cloud fascination, resistance, adoption, pragmatism so its lets look at what this can tell us about the latest AI trend"
tags: ["goals","purpose", "why", "personal growth"]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
---

![Cloud vs AI adoption](/img/2025/cloud-and-ai-adoption.png)

It's 2025 and AI is here, and just about the only thing people in tech can talk about, but let's flash back to 2010 when Public Cloud was the latest trend and the only thing tech could talk about. Can we follow this historical trend to predict the future of AI? How does the general public perceive AI? I'm pretty sure your non-tech neighbours can tell you what ChatGPT is, but do they know what AWS is? So, what's different this time?

### The journey to the cloud
<*Cue tv-style flashback harp music*>
<p/>
It's 2010, AWS EC2 has already been a thing for 3 years, Google has AppEngine, Rackspace has OpenStack, Microsoft was just launching Azure. Engineers were experimenting with deploying new workloads, but mainstream businesses still had concerns over security, privacy, resilience, unpredictable costs and vendor lock-in.

Lots of businesses, vendors and these hyper-scale cloud companies spent most of the decade arguing over these topics, but the big three (AWS, Microsoft and Google) also spent much of the decade getting more compliance certificates, better migration tooling and better management tooling. Plus a whole industry of FinOps tooling and practices emerged to deal with costs.

By 2015, while debates continued in some circles, many medium and large businesses adopted a "public cloud first" strategy - moving everything in their datacentres into the public cloud as fast as they could, mostly without modification to the technology or operating practices.

Skip ahead five years, and there wasn't a company that didn't have some form of public cloud deployment, some with a multi-cloud configuration and many many new companies who had never been deployed anywhere else. Public cloud adoption became mainstream, and the laggards’ voices faded into the background.

Now, in 2025 the world economy is not as strong as it was, money is no longer as readily available or inexpensive as before, and companies are starting to return to the most persuasive and consistent of the original argument - cost. Lots of discussions are happening in offices around the worlds about how the money on cloud is spent, halting any further migrations that had not been complete and even moving forward with repatriation back into datacentres. Despite this, you can't actually travel back in time, and while there are certainly some ways to save costs there are unique challenges of this migration back. Expectations have changed, and fewer engineers now have the required skills or the desire to build and maintain servers, networking and entire datacentres.

### The current state of AI

So here we are for our next tsunami of hype, ambition and billionaire-making technology. AI has moved from the niche world of data science and academia into mainstream use, with both technical and non-technical users adopting it.

2024 was the year of the big splash and 2025 is likely to be the year where it really hits the mainstream. So guess what the arguments look like? 
* Security and privacy - Can I trust it with my data and how do we know it's making ethical decisions? 
* Resilience - Can it scale and do we have enough datacentres to support it? 
* Unpredictable costs - What is a token? How can I estimate my token usage?
* Vendor lock-in - Do I need to make my application multi-modal?

Sound familiar?

### What can we predict for the future

No one can predict the future, even the futurologists whose profession is based upon it, but we can follow the patterns.

So let's take a look at those AI arguments again.

Security and privacy - Can I trust it with my data? Remember when banks initially refused to store data on S3 due to security concerns? Then AWS got those CE+, PCI DSS and FedRamp certificates and suddenly everything was ok. It's likely that the recent European AI Act and ISO 42001 standard will be further built upon and more industry- and region-specific regulation will emerge as it did for cloud, making this less and less of a concern over the next couple of years. Concerns about how your data is used? Well the AI Act was the starting point for this but I believe that having two big players Meta and Deepseek, both having open models with open weights, will further put pressure on others to do the same. As for Ethics, well I think perhaps that's a new problem for this generation and something I'll discuss more soon.

Reliability - Can AI scale? Do we have enough datacentres to support it? Well this is a fun one, because the cloud providers have been on a bit of a roller-coaster of a journey themselves and I'm still not convinced this is a totally solved problem. They are still building more and more datacentres for both scale, regional requirements and also for resiliency. Now we have AI, where demands to build more datacentres are increasing, where demands for power stations and water facilities are increasing, and rare earth metals for chips are all topics of conversation. If AI continues to progress at its current pace, it will likely follow the same trajectory - datacentres in every corner of every country, larger cloud datacentres and possibly even dedicated AI facilities. The question is real question here is - can governments keep pace?

Unpredictable costs - Remember trying to explain to your boss or your finance team that this virtual machine is going to be charged by the second? Or explain that this lambda function is charged per-execution? Well in those early days of cloud, the tools for understand and predicting costs were limited and excel was still king. In AI land today, with APIs being priced per-token, it becomes very difficult to predict what the costs are going to be. Yes we have some tools like the OpenAI tokenizer, but when you're looking at multiple languages or considering user-input then this prediction of the number of tokens used in a real-world example is very tough. But the fact we have tools this early in the lifecycle does mean that some thought has been given to this problem even if it's not as mature as we might need just yet. Costs for AI might remain a bit un-predicable for a while, but five years from now? I doubt it.

Vendor lock-in - This is my favourite of the original concerns of cloud, because it was the one dispelled so easily. There was (and in some places still is) a concern that putting all your infrastructure and data into one vendor and developing your application against vendor-specific tools as a big problem. With cloud it was a recurring conversation for years and there were plenty of multi-cloud vendors that would try and sell you something to solve that problem. What was fun about this concern was that while it applied to cloud migrations, there was no such conversation about moving data to SaaS providers. In the intervening years two schools of thought have emerged, either go all-in on a provider to get the best commercial deal or pick the best provider for each workload. Well now we're seeing the vendor lock-in topic re-emerge around AI, it seems likely a similar solution will be found, that some organisations will go all-in on on vendor based on a very successful enterprise sales deal or that engineers will explorer using different AI models for different solutions and we'll end up with multi-model solutions. I certainly expect, with such a low-bar to entry and continuous evolution of these models over the next few years that vendor lock-in won't be as loud a topic as it was for cloud and the multi-model approach will win out.


### What's different this time

With every new significant change in technology, be that the internet revolution of the late-90s and early-00s, to the cloud migrations of the 2010s and now the new AI hype train, each generation comes with it's own set of unique challenges. 

The recent AI revolution has been compared with the internet revolution, where the challenges and discussions about them are both very public and very much focused about the changes, not just in the technology but also in the societal changes, both positive and negative, that they will bring about.

The demand for additional resources and to build additional datacentres, while not entirely a new issue has now become a huge political issue. The need for good relationships with the countries that have the rare-earth metals required for AI chips, the countries with the fabrication facilities to produce them and the countries that make the machines that make the chips has never been more important. AI and its sovereignty have become national security issues, with some branding it the new Cold War arms race, something we've not seen since the real Cold War and the space race of the 1960s. The demand for additional resources might be the only thing that slows down progress of AI if, governments and businesses physically can't deploy enough resources fast enough or the relationships between countries deteriorates. 

The ethics of AI has been a topic for many years and I remember studying this topic myself as part of my undergraduate degree but now it's probably one of the hottest topics within general AI discourse. There are concerns about models enhancing already existing bias, there are concerns about it being used to replace jobs, there are concerns about AI supply chain and there is the huge reality of it's impact to the climate. Each of these topics warrants in-depth analysis, and many researchers have explored them extensively. I would certainly recommend digging deeper in these areas. I guess the question that remains here for me, is will any of these concerns actually provide enough inertia to the pace of change? At the moment it seems unlikely.

Some are saying the speed, scale and impact of AI is unprecedented. I'm not sure I agree with this position just yet. While the internet era has similar hyper and global impact it's growth was more linear. I don't expect the same from AI. If resources and regulations slow progress, we may see this hype train plateau until those constraints are resolved. Rather than a rocket ship, I expect to see AI grow in waves over the next decade.

### So what can we learn?

When we're comparing the AI adoption lifecycle to the previous cloud adoption lifecycle, we can learn that we're going to see the same conversations and lifecycle as any large technology change and that despite a lot of discussion and it won't stop progress. Despite the unique physical and political challenges of AI, the gene is out of the bottle now and so we're going to have to run head first into trying to solve this problems - how exciting!

Even if this AI bubble bursts, as some predict - like the dotcom bubble before it - technology will endure. Companies will come and go, but we must learn from past tech cycles and embrace the future.