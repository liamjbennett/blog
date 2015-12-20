+++
title = "[Quick Update] - 23-Mar-2015"
date = "2015-03-23T08:50:00Z"

+++

Ok, so you’ve seen the date of this post. I’m not exactly as regular with these posts as I would like but it seems that I do in fact still have things to write about.

#### Foreman
One of the big things that I have been working on recently has been in puppetizing the foreman infrastructure used at OpenTable. Thankfully this is quite a mature community and there has already been a lot of work done however one limitation that I found was that I wanted to actually use puppet to configure foreman after I had installed it.

For anyone that has actually spent some time with foreman you will know that entity model is a little complex and it can take a long time to configure with settings specific to your organization. Having a somewhat ageing foreman installation meant that we were suffering from the problems of any aging, snow-flaked system, namely it was flakey and no one wanted to make changes to it. This is when I decided that this was a good opportunity to extend the already existing puppet module to support this entity model with custom types/providers.

This was my first foray into writing types and providers so it took a little longer than might be expected and took several iterations to get the code working and more importantly, performant. Writing types and providers is still one of those areas that I don’t think is a well documented process and is not for the unexperienced. For the majority of my time I had [this]() wonder blog open, in addition to [the book]() and the [puppet documentation]() on the subject. Only with the arsenal of resources available was I able to tackle the challenge. Thankfully a couple of weeks of hacking later and I managed to have types for all the major foreman components: operatingsystems, configuration templates, provisioning profiles etc.

Take a look at my work and see what you think ...

#### puppet-community

Puppet community is a github organization that has been developing for some time now. The idea behind the project/community is provide a shared space for puppet modules to live and be developed. It’s key benefits are really just starting to develop but are quite useful - shared build scripts, shared testing infrastructure and shared development and PR management. The hope is that with the experience that is found in the community the quality of the modules in the community as a whole will increase.

Being a separate non-corporate, non-individual entity means that when a primary author moves organizations and/or does not have the time to work on a module any more they have people who will continue to support it. This is huge, as anyone who has any more than about 5 modules on the forge will tell you - managing PRs and releasing updates can become a big job pretty fast. I know there are 8 modules authored by me personally and over 10 authored by myself and my OpenTable colleagues - this was becoming a full time job.

As you might be able to assume by this point, I am a huge fan of the project and I have been moving both my own personal modules as well as a number of OpenTable modules into the community. I won’t discuss this aspect any further, because there will be a much larger post of the subject - but be assured, it’s very exciting and a good move for all the users of all the modules I have written.

#### puppet notes

Finally anther small thing I have been working on is externalizing the notes I have been keeping about puppet over the last couple of years.  These notes over everything from weird edge-cases you might run into, certain style guides and by far the largest part of the notes is on different code patterns I have been and my comments on them. As you might expect there is lots of content in there on several different approaches to the same problem - I have been doing my best to document these, including when I think they can be used and trying to pick a favourite.  I’d love for you to take a look and let me know your thoughts.

\* \* \*

Hopefully by now you are not too bored and have found some interesting things. In which case you should absolutely reach out to be at [@liamjbennett](https://twitter.com/liamjbennett) and let me know your thoughts.

Until next time …..
