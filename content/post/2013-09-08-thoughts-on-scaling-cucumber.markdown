+++
title = "thoughts on scaling cucumber"
date = "2013-09-08T18:01:00Z"

+++

I have been spending a lot of time lately working with Ruby and in particular a reasonably large suite of cucumber tests. Cucumber has been adapted by several teams within Mimecast to varying degrees of success and maturity, mostly dependent on each individual teams' experience with Ruby.

My recent work has identified two problems scaling the test suite: cross-team testing and multi-platform. I want to discuss some of these problems and how we are going about solving them.

I guess the fist of these needs a little bit of background. Mimecast has grown significantly since I first joined them 3 years ago and while I joined them as a start-up I guess you would now consider them a medium-sized enterprise. In the beginning all developers worked on the entire codebase at different times but now the codebase and feature-set is so large that functional teams have formed around various products and/or various aspects of the Mimecast platform. What this means for testing is that many of the engineers are now focussing on testing features within their own little world view: database, front-end, corporate website etc. We call this the horizontal.

About six months ago we realised that there was an obvious problem with this approach: that the actual day-to-day workflows of the customer were being missed because of the team-siloed view of things (I will talk more about this in a future post) -- we call this the vertical. What we wanted to do was to cover these workflows while making the most use of the work that each team had already done.

Let's take a simple example: sending an email. There are a number of ways that the [Mimecast](https://www.mimecast.com/) platform can receive an email: from a windows client, from a mobile client, from a web client or even from the telnet command-line itself. As the most critical aspect of the business we want to make sure that all of these scenarios work as expected. This is are number one smoke test.


###The badly written test problem
The first problem that we had in this case was each teams set of tests were written with only them in mind and a common pattern we discovered was the long 20+ line step definition. We also started to see really long features and long complex example tables. These code smells (and let's not forget that this is code) are common [[1]](#e2e078226ecd495cdc06b632fc822d74) [[2]](#93ef1249d48646ce3957aebacef6d80f) [[3]](#fb0cf1fb3edbc52aa90c995da186a536) [[4]](#3b7225a0b2e8835f3d0a56b9b722a395) and pointed us immediately to the need for refactoring and abstraction.

###The novice Ruby problem
Then we ran into another problem, something common to novice Ruby users: the non-OO Ruby script pattern. There was abstraction in the test code, they had defined common functions and split them up into related collections of Ruby files but that is as far as it had gone: no-classes, no-modules and plenty on inbuilt assumptions. Now here is the fun bit -- we knew this code was messy, but it worked and so our priority was first to abstract it into a format that was sharable across all our projects: gems.

What this also meant this that everyone got to see what was available, we found out that we had implemented 3 different ways to access the database, 2 different methods for logging and many other smaller common pieces of functionality. We were being open about the technical debt [[5]](#0adde2169acddcffd1cb1b9a3a5d6360) rather than hiding it away in some corner of the codebase. It also had the added benefit that more people were looking at this code and trying to use it in different ways, which meant that it always going to improve as a result. I think it is very important to be open about your technical debt -- it's nothing to be ashamed of and hidden away, it happens to all projects and can given occur without you doing anything. It's important to be honest and blameless about where it lives and try and integrate it's pay-back into your standard project planning process. There is a lot of good resources out there on technical debt and how to manage it so I won't discuss that much here. There aren't so many on the cultural aspect of managing technical debt so I might write more about that in the future.

Using gems was tricky, we has a lot of them -- about 10 or 15. Authoring them was the easy part, after one failed attempt to use them with bundler as-is we realised that the code was not stable enough and so we decided that the best approach was the vendor all our dependencies. The reason we do this is not as horrible as it first sounds (some people [[6]](#dff1f33327669c1dd56106c5c898f4ef) even agree with it). We don't fully vendor our gems in each project and we never check-in our vendor directory into source control. The only reason we vendor is for developer convenience. What it allows them to do is to debug the code problems, add logging and possible even work out a possible bug fix, all within the safety of their own environment knowing that whatever changes they make will be blown away when they next vendor.

###The Sharing problem
The next problem we discussed was sharing step definitions. I am sure that this topic has come up with any team that has used cucumber for any decent length of time and I have one answer to this: **Don't!** The path that many of our developers went down was to do exactly what we were doing with the rest of the code: to package it up into gems and share it around. This sounds good in practice, but in reality it causes more problems that it solves. This leaves you with 3 sorts of projects: one containing feature files, ones containing steps, and ones containing plain Ruby code. Aside from that fact that it means that a developer will be committing to 3 separate projects at any one time it also causes the projects containing the steps to start to build up with code again, something we were trying very hard to avoid. It also means that as a project grows over time it is more likely that the steps with conflict between shared projects or become so abstract as to be painful to debug. We considered switching away from Cucumber to something like Spinach [[7]](#9a84b3b91b1ddc4bbd5fdff9023a5218) to avoid this problem but in the end we realised at it wasn't the best option for us at the time. Actually the end solution was much more simple: keep the steps with the features but have a strict rule on the amount of code that should be contained within an individual step: at the moment this is 10 lines, I guess this is pretty arbitrary and perhaps not the best way to do it but it works for us and we are enforcing it within our code review process.

There is also a cultural problem here: individual teams were still writing libraries for their own needs first, forgetting or ignoring the needs of the downstream consumers in other teams. I think what makes this a difficult problem is that each team has it's own test developer, incentivised to enhance the tests of their teams own product(s) not the wider testing effort. They will write code for the functions that they need and if other teams can use it then that is an additional bonus but not a priority. Each team has it's own needs and it's own way of doing things. Team-A will write a function to send a email via the command-line and Team-B will write a function to send an email via the web-ui and both of these are incompatible at the API-level. There are two solutions to this problem: put in an architect and force the teams to standardize or alternatively create an abstraction layer above the differences. Actually the answer is both as it's the most flexible without causing too much cultural strain.

###The cross-platform problem
The final problem isn't really a problem at all - well not yet. It's the issue of dealing with cucumber in a cross-platform way. I can only briefly discuss this problem and without a good solution at this point as we have yet to resolve it ourselves. What we have is a very cross platform set of projects: we have Java projects (on Linux) and C# projects (on Windows) and Objective-C projects (on Mac and iOS). Each set of projects is running tests with it's own gherkin-based tool (Cucumber [[8]](#83abb1fd7981242620bd4073d1dcea9b) and SpecFlow [[9]](#8641e08483c2e057395dec05e1e98e43)) this is all well and good, we are arguably using the best tool for the job in each case while culturally still speaking the same language. Where we find difficulties is in sharing code: both because of language differences and platform differences. We are currently looking to move away from SpecFlow to cucumber which should solve one problem but the other problem is likely to involve some nasty ssh-based solution. I shall follow up with our outcomes on this.


Both myself and my current organisation are continuing to learn and mature in our experience with cucumber and with Ruby and how best to deal with these projects when we have it used so widely and by so many. Hopefully this will lead to further discussions and I hope to follow up this blog with further updates in the future.

####References
<ul style="list-style-type: none; padding:0; margin:0;">
  <li>
    <a name="e2e078226ecd495cdc06b632fc822d74">[1]: http://chrismdp.com/2011/09/layers-of-abstraction-writing-great-cucumber-code </a>
  </li>
  <li>
    <a name="93ef1249d48646ce3957aebacef6d80f">[2]: http://andrewvos.com/2011/06/15/writing-better-cucumber-features </a>
  </li>
  <li>
    <a name="fb0cf1fb3edbc52aa90c995da186a536">[3]: http://robots.thoughtbot.com/post/25650434584/writing-better-cucumber-scenarios-or-why-were </a>
  </li>
  <li>
    <a name="3b7225a0b2e8835f3d0a56b9b722a395">[4]: http://renderedtext.com/blog/2011/12/06/sucking-less-at-writing-cucumber </a>
  </li>
  <li>
    <a name="0adde2169acddcffd1cb1b9a3a5d6360">[5]: http://salvetore.wordpress.com/2012/08/08/open-technical-debt </a>
  </li>
    <li>
    <a name="dff1f33327669c1dd56106c5c898f4ef">[6]: http://ryan.mcgeary.org/2011/02/09/vendor-everything-still-applies </a>
  </li>
  <li>
    <a name="9a84b3b91b1ddc4bbd5fdff9023a5218">[7]: https://github.com/codegram/spinach </a>
  </li>
    <li>
    <a name="83abb1fd7981242620bd4073d1dcea9b">[8]: http://cukes.info </a>
  </li>
    </li>
  <li>
    <a name="8641e08483c2e057395dec05e1e98e43">[9]: http://www.specflow.org </a>
  </li>
</ul>
