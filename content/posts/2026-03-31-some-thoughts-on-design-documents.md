---
author: "liamjbennett"
title: "Some thoughts on design documents"
date: "2026-03-31"
description: ""
tags: [""]
ShowToc: false
ShowBreadCrumbs: false
thumbnail: "/img/main/profile.jpg"
audio_url: ""
audio_length: ""
audio_bytes: ""
---

![Design document post banner](/img/2026/Design_document_post_banner.png)

In engineering and product organisations, design documents are a vital but oft-hated set of assets to be produced and maintained. In the world of the MSP, I come cross design documents of all shapes and sizes - both created by us and also those created by customers and other organisations. There is one thing they all have in common, they are all long and as difficult to read as they are to write. In the age of AI and high-levels of automation surely there are things that we can do to improve these assets and make them better and more valuable for everyone.

## A little bit of history of design documents

The history of design documents very closely follows the history of computing itself, with it's roots in the formal design artifacts produced in the physical engineering disciplines. It wasn't until Winston Royce's paper [Managing The Development of Large Software Systems, 1970](https://web.archive.org/web/20250826033037/https://www.praxisframework.org/files/royce1970.pdf), often cited as advocating for waterfall software development, that the "Program Design" phase was established. By the 1990s design documents really became part of the fabric of day-to-day development, with [MIL-STD-498](https://en.wikipedia.org/wiki/MIL-STD-498)/[ISO-12207](https://en.wikipedia.org/wiki/ISO/IEC_12207), [CMMI](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration) and [ITIL](https://en.wikipedia.org/wiki/ITIL) ensuring they were enshrined in standards. This coincided with the rise of large-scale software outsourcing, particularly to India. Firms like Infosys, Wipro, and TCS operated in a model where clients in the US or Europe would provide requirements, the outsourcing partner would produce a high-level design ("HLD") for client approval, then a low-level design ("LLD") for internal use, and then code. This model deeply embedded HLD/LLD culture into the IT services industry, both the large global service integrators and the smaller MSPs, where it remains a prominent practice to this day. The 2000s had the [Agile Manifesto](https://agilemanifesto.org/) which explicitly valued *"working software over comprehensive documentation"* which represented a direct challenge to heavyweight design document culture. The large heavy-weight design documents transitioned to more collaborative solutions like Architecture Decision Records ([Documenting Architecture Decisions, Michael Nygard, 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)), wiki pages and diagram-as-code tools like Mermaid. 

Like Agile itself, it didn't totally eradicate what had come before it, with outsourced IT firms and regulated industries (e.g. finance, healthcare, public-sector) still requiring these assets. Hopefully they were now perhaps a little leaner, more visual and updated more frequently in a collaborative manner (or so you'd think!)

## Diagrams and Decisions

Diagrams have always been part of design documents since the very beginning with every decade coming with new ideas and new options: we had [Data Flow Diagrams]() of the 1970s-1980s, the dreaded [UML](https://en.wikipedia.org/wiki/Unified_Modeling_Language) of the 1990s, [ArchiMate](https://en.wikipedia.org/wiki/ArchiMate) in the 2000s and the [C4-model](https://en.wikipedia.org/wiki/C4_model) and [Mermaid](https://mermaid.js.org/) diagrams of the 2010s. I've seen almost all of these still in active use. Then you've got the cloud infrastructure architecture diagrams, which evolve as often as the Microsoft's or AWS's marketing department roadmaps. 

I actually love diagrams, well visuals of any kind actually. That combination of picture and explanatory words is what makes complex information easy to digest. Like all writing it also serves an important purpose of breaking up text to ensure that the reader remains focused (see: [Cognitive Theory of Multimedia Learning](https://web.archive.org/web/20251103114846/https://media.repository.chds.hsph.harvard.edu/static/filer_public/ca/62/ca625803-3d73-4855-b3e1-765870ce3772/2023_jwaxman_monograph_cogtheory_multimed.pdf)). 

The most important text in any design document is the decisions that are made, the context and information about why that decision was made and how it links to the overall architecture that is being presented. In more traditional design documents, like those I read from global service integrators, this information is often presented more visually using some format of the call-out box. While in principle I like this approach, is suffers with two main problems: there is rarely a link to between the decision and the specific resources impacted by the decision; and those decisions often don't make it out of the design document into ITSM systems and linked to risks and problems that come later. Like all design documents and the corresponding content - it all becomes stale and out-of-date pretty quickly.

### Architecture Decision Records (ADRs)

One method for extracting those decisions and context from the design documents was to have specific small records for each decision, known as [Architecture Design Records](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html) ("ADRs"). This not only allows you to capture the decision made, but the background information, who reviewed and supported the decision, what alternatives were reviewed and a lot of additional context. By using ADRs, the traditional call-out boxes become merely a cross-reference to this more context rich document. There is no prescribed format for these decision records and organisations will choose for themselves a standard format for them, but there use builds upon the agile principles of *"individuals and interactions"* by supporting the documentation of conversations and allows this context to be fed later into ITSM systems where decision records can be linked to other ticket types.

![ADR Example in plain markdown](/img/2026/ADR_example_1.png)

### Keeping those diagrams up-to-date

There was a time when it was a significant part of some people's jobs to keep these design documents up to date. One of the trickiest (and some would say most annoying) parts of this activity was keeping the diagrams up-to-date, not only because of the evolving design changes but also because of the ever-evolving adaptations to the environment as a result of in-life changes.

Thankfully, in my experience, the Visio diagrams of the 90s have almost entirely been replaced with the much more ubiquitous [draw.io](https://www.drawio.com/) format. What makes this a step forward is that there are now many tools that support this format for both import and export, allowing a rich cottage industry of automation tools for generating and maintaining diagrams. Tools such as the [draw.io MCP server](https://github.com/lgazo/drawio-mcp-server) allow for the [AI generation of those initial diagrams](https://thomasthornton.cloud/draw-io-mcp-for-diagram-generation-why-its-worth-using/) and tools like [Terravision](https://github.com/patrickchugh/terravision) allow them to be kept in sync with infrastructure as code.

### Connecting decisions to diagrams

Now here's the bit that people often miss - how do you know which resources in your diagram(s) are impacted by which decision records and visa versa? Honestly, for most of the design documents I've read this is information is either not included as all or is very verbose text in the decision description. The key to really solving this problem is having both your ADRs and your diagrams as code. Using the [Markdown ADR](https://adr.github.io/madr/) system you can link your design decisions to relevant diagrams using the front matter to include that meta data. With draw.io digrams, each shape in a diagram can contain custom properties, these properties can be amended to include references to ADRs. Having both of these aspects in code also allows the validation and meta data synchronisation to also happen in code - linting both asset types like any other code and ensuring that no ADR orphaned and not linked to relevant visual resources and no digram exists without descriptions of the decisions made.

![ADR Example with front matter](/img/2026/ADR_example_2.png)
![Drawio Example](/img/2026/Drawio_example_1.png)

## Handling Change

One final gap I see that causes design documents to become stale is the in-life change process. Now, as a prefix - this bit requires a pretty mature ITSM system and processes.

**Real example**: A customer raises a ticket to add a new rule to a subnet to allow connectivity to an environment we are not responsible for. 
* Question 1 - do we require the low-level design to be updated before the change is implemented (which slows down the process for the customer) or do we update the document afterwards (which results in a stale document until the next review cycle)? 
* Question 2 - we have lots of design decisions split across multiple HLD and LLD documents, how do I know which documents will need to be updated when I raise a change?

This was a real conversation I had last year with a customer. When managing a traditional documentation approach, you have to choose one of these two options but there are more modern methods of handling this. They key is looking at the Configuration Items ("CIs").

*(n.b. my examples here are based mostly on my experience of ServiceNow, although similar ideas do exist in alternative ITSM platforms)*

The key thing to stop this gap is to ensure that the configuration items in your ITSM system are automatically updated based on the live system. This is important in this scenario because if you're following along and using Terravision for your diagrams then as you're making changes to your environment with Terraform (you are using infrastructure-as-code right?!) then the diagrams in your design documents are updated and your CI items are kept in sync from the real environment so both sides of the equation are up-to-date with the real environment.

## Back to the documents - pulling it all together

With design decisions extracted and diagrams dealt with, what you're now left with in that traditional document format is typically a combination of templated/boilerplate content and some customer/environment pre-amble. While the document format itself can certainly be automated, there are certainly better alternatives such as confluence or even static site generators that allow for more dynamic and fluid updating of design content. The key here is to keep templated documentation in a re-useable location and really focus on re-constructing these written assets into composable parts. This allows them to updated more quickly, with most of the content remaining live and in sync with the day-to-day operation.

## Where AI can help

This wouldn't be a 2026 technical blog post without there being some reference to AI would it?! Well given that we've been talking about documents as code, templated content and keeping this live and up-to-date, then this certainly seems like something where both generative and agentic AI can support these workflows. Examples where we're exploring AI to support:

* Validating ADR quality - having agents both support the creation and review of ADRs based upon agreed standards and quality gates.
* Generating the documents themselves - most of our documents are moving to markdown formats so we're experimenting with pulling together templates, generating environment specific context and integrating generated diagrams using agents.

## Summary

Design documents have evolved significantly from the heavyweight waterfall artifacts of the 1970s to today's more agile approaches, but they remain challenging to create and maintain. The key to modernising them lies in treating documentation as code: extracting decisions into Architecture Decision Records, maintaining diagrams with automated tools like draw.io and Terravision, and linking these components together through metadata and custom properties. By decomposing traditional monolithic documents into composable, interconnected parts and integrating them with ITSM systems and infrastructure-as-code workflows, we can ensure design documents remain living artifacts that stay synchronised with real environments rather than becoming stale reference material. AI can further accelerate this transformation by validating ADR quality and generating environment-specific documentation from templates, making the entire process more efficient and sustainable.