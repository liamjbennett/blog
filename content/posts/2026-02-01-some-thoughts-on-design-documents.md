---
author: "liamjbennett"
title: "Some thoughts on design documents"
date: "2026-02-01"
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

In engineering and product organisations, design documents are a vital but oft-hated set of assets to be produced and maintained. In the world of the MSP, I come cross design documents of all shapes and sizes - both created by us and also those created by customer and other organisations. There is one thing they all have in common, they are all long and as difficult to read as they are to write. In the age of AI and high-levels of automation surely there are things that we can do to improve these assets and make them better and more valuable for everyone.

* A little bit of history on HLD and LLD documents
The history of design documents very closely follows the history of computing itself, with it's roots in the formal design artifacts produced in the physical engineering disciplines. It wasn't until Winston Royce's paper [Managing The Development of Large Software Systems, 1970]() often cited as advocating for waterfall software development that the "Program Design" phase was established. It wasn't really however, until the 1990s when design documents really became part of the fabric of day-to-day development, with [MIL-STD-498]()/[ISO-12207](), [CMMI]() and [ITIL]() ensuring they were enshrined in standards. This coincided with the rise of large-scale software outsourcing, particularly to India. Firms like Infosys, Wipro, and TCS operated in a model where clients in the US or Europe would provide requirements, the outsourcing partner would produce HLD for client approval, then LLD for internal use, and then code. This model deeply embedded HLD/LLD culture into the IT services industry, both the large global service integrators and smaller MSPs where it remains a prominent practice to this day. The 2000s, had the [Agile Manifesto]() which explicitly valued "working software over comprehensive documentation," which represented a direct challenge to heavyweight design document culture. The large heavy-weight design documents transitioned to more collaborative solutions like architecture decision records (ADRs), wiki pages and diagrams-as-code tools like Mermaid. 

Like Agile itself, it didn't totally eradicate what have come before it, with outsourced IT firms and regulated industries (e.g. finance, healthcare, public-sector) still requiring these assets, however there were now perhaps a little leaner, more visual and updated more frequently in a collaborative manner (or so you'd think!)

* Diagrams and Decisions
Diagrams have always been part of design documents since the very beginning with every decade coming with new ideas and new options: we had [Data Flow Diagrams]() of the 1970s-1980s, the dreaded [UML]() of the 1990s, [ArchiMate]() in the 2000s, the [C4-model]() and [Mermaid]() diagrams of the 2010s. I've seen almost all of these still in active use. Then you've got the cloud infrastructure architecture diagrams, which evolve as often as the Microsoft or AWS's marketing department roadmap. 

I actually love diagrams, well visuals of any kind actually. That combination of picture and explanatory words is what makes complex information easy to digest. Like all writing it also serves an important purpose of breaking up text to ensure that the reader remains focused. 

The most important text in any design document is the decisions that are made, the context and information about why that decision was made and how it links to the overall architecture that is being presented. In more traditional design documents, like those I read from global service integrators (and those I write myself from time-to-time) this information is often presented more visually using some format of the call-out box. While in principle I like this approach is suffers with two main problems: there is rarely a link to between the decision and the specific resources impacted by the decision, those decisions often don't make it out of the design document into ITSM systems linked to risks and problems that come later. Like all design documents and the corresponding content - it all becomes a stale and out-of-date pretty quickly.

* Architecture Decision Records (ADRs)


* How to know the connection and when it needs updating
* The link to change?
* How can we do this better
