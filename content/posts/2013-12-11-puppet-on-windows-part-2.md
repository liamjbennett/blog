---
author: "liamjbennett"
title: "Puppet on Windows - Part 2"
date: "2013-12-11"
description: ""
tags: ["puppet"]
ShowToc: false
ShowBreadCrumbs: false
expiryDate: "2015-12-01"
---

In <a href="/blog/2013/10/06/puppet-on-windows-part-1">part 1</a> of this series of posts I discussed some of the challenges when writing modules for puppet on windows: documentation, packging, ISOs and reboots. In part 2 I will discuss how I learnt about this, about the modules that I have written, the learning outcomes and about contributing to the forge.

There are many ways that you can contribute and extend puppet: classes, defintions, facts, types and providers. Of the modules that I have written I wanted to specifically look at the following:

* <a href="http://forge.puppetlabs.com/liamjbennett/win_facts">win_facts</a>
* <a href="http://forge.puppetlabs.com/liamjbennett/dotnet">dotnet</a>
* <a href="http://forge.puppetlabs.com/liamjbennett/msoffice">msoffice</a>
* <a href="http://forge.puppetlabs.com/liamjbennett/windows_firewall">windows_firewall</a>

###Writing facter facts (win_facts)
Writing facter facts is actually a good place to start with puppet. What is puppet not telling you about the system? Puppetlabs have actually provided a very useful tool that tells you lots of great information about the system but in some areas, either in general (platform-speific) cases or in your specific edge cases it might not give you that information you were hoping for.

When I started working with Windows the only facts that classied specifically for windows were:

    :kernel => windows
    :operatingsystem => windows

While this is useful if your mananging windows machines in an existing linux environment and want to seperately classify them, if you've got multiple versions of windows then your going to need a little bit more. This is why I started to write win_facts which provided the following additional facts:

    :operatingsystemversion  => "Windows Server 2008 R2"
    :windows_productkey      => "XXX-XXX-XXX-XXX-XXX"
    :windows_sid                  => "S-1-S"
    :windows_systemtype      => "x64"

These facts use two techniques that I want to draw attention to: The **registry read** and the **command wrapping**:

    ...
    require 'win32/registry'

     Win32::Registry::HKEY_LOCAL_MACHINE.open('Software\Microsoft\Windows NT\CurrentVersion') do |reg|
        reg.each do |name,type,data|
          if name.eql?("ProductName")
            operatingsystemversion = data
          end
        end
     end
     ...

(see: https://raw.github.com/liamjbennett/puppet-win_facts/master/lib/facter/operatingsystemversion.rb)

As dicsussed in Part 1. The windows registry should be any windows developers friend and contains a weath of information. This is just one example - there are centainly plenty more than this. Puppet recently introduced the concept of External facts [[1]](#53f76edfd65c1180adcd08fb6eb7bd45) - drop a file in the C:\ProgramData\PuppetLabs\facter\facts.d\ directory and facter will read it. This is good for many reasons but windows already has a great list of files containing facts - the windows registry - so let's read from it and find some more.

The alternative is the command wrapper:

    ...
    systemtype = Facter::Util::Resolution.exec('wmic ComputerSystem get SystemType | FindStr /i x')
    systemtype.gsub!(/-based PC/,'')
    systemtype.gsub!(/\s/,'')
    systemtype.downcase!
    ....

(see: https://raw.github.com/liamjbennett/puppet-win_facts/master/lib/facter/windows_systemtype.rb)

The registry is, for most people, a very complex nest of hidden information. Sometimes it doesn't contain all the information you need and sometimes it's difficult to find or process. In these cases it's always going to be an option to exec out and wrap an existing windows command. Windows has a wealth of small utilities [[2]](#347ddd0bb5273c14a5cce0688cef7939) avaliable that can be used to pull out information, wmic is just one example of these.

Make sure that if your are going to exec that it's as simple as possible. No long multi-line commands, no pages of powershell. If your logic is suffiently complex then facter is probably not appropriate to execute it inline. Instead write a utility (C#, Powershell, or even ruby) and build, test and deploy that seperately. You can then execute that as a fact or execute it out-of-band and have it write a external fact. Either way, getting the complex logic out of the main facter code and making it simpiler for everyone wishing to use it or maintain it.

And that points me to another important thing - do test your facts! Many people, myself included are guilty of not doing this but it's pretty simple to do using standard rspec [[3]](#9d7fcbe9e40e5fac0ea095bfdfdae797).

Most windows libraries, utilities and applications vary widely from one version of windows to another (and sometimes from one edition or service pack to another) so I make plenty of use of these facts in my modules to take this into account and you should to.

###Writing classes for comman dependencies (dotnet)
There is category of classes that will be used everywhere, they are not common code (that could be built into the PuppetX namespace) but they are common between manifests. Such classes include java, dotnet, powershell, ruby, gcc. I call these common dependencies.

Many people will implement common dependencies in different ways but the community really needs to converge on a standard for most of them - this hasn't happened yet. The first thing I would suggest is to **always write as a definition first** and only if it is totally impossible to install mutliple versions on the same machine (either legitimately or though some form of hack) should you make it a class. This is what I did with the dotnet module.

The .NET framework has some unique characteristics - firstly its installed differently on servers than it is on clients and secondly major versions (2,3,4) can be installed side-by-side while minor versions overwrite (4 and 4.5). I still made it a defintion because it can be installed side-by-side.

For modules like java and powershell there are even custom providers [4] that use those commands and will require seperate modules to make sure they are installed.

What I learnt about writing this module was actually a very simple lesson - **don't assume how your users will want to provide the packages**. I assumed the exe files used would be stored on a network share (this was my personal use-case) but what if your users want to download over http, use chocolatey or some other custom package manager. I want not have wanted to (or had time to) implement all the possibilities but this is really about good design and about amking your module as extensible as possible. I am still refactoring now to take this into account - it's easier if you design it in from the beginging.

These modules are probably the best modules - they are pretty quick to write, simple to test and get added everywhere so add huge value.

###Writing defintions, types and providers and knowning what's appropriate (windows_firewall)
The windows firewall module was written to manage the built-in firewall provided by Microsoft. This is one situation, similiar to what I discussed with the facter facts above, where I wanted to provide a wrapper to the existing netsh commands. So that I what I did, wrote a manifest for the service and a defintion for the exceptions - this can be seen here (https://raw.github.com/liamjbennett/puppet-windows_firewall/master/manifests/exception.pp).

This works quite well and as an initial version meets the use-cases but it's far from elegant. This module raised the simple question: **When should a defined type be refactored into a native type?**

There is also a good rule of thumb for this: **If the effort spent munging variables and arguments is greater than the effort spent managing resources or calling exec then that should be a native type**. What this meant for the windows_firewall module is that while the main class manifest should remain as it is, the defined type for exception should be made into a native type. For me this is currently a work-in-progress and can be seen in the <a href="https://github.com/liamjbennett/puppet-windows_firewall/tree/type_refactoring">"type refactoring" branch</a> on Github.

There are lots of benifits to writing types and providers. They are pure ruby, they can be tested as plain ruby, but more importantly they have the benefits of a turing-complete language and not being limited by the Puppet DSL. It does however also provide a great framework for managing and validating arguments and making sure that your type and providers remain idenpotent. For more information on how to write custom types and providers then go and read this great book on the subject (<a href="http://www.amazon.co.uk/Puppet-Types-Providers-Dan-Bode-ebook/dp/B00ANCH2GK/">Puppet Types and Providers</a>)

###Tackling the big applications (msoffice)
For most windows infrastrcuture there come a point where you need to manage the much larger applications - you need to tackle those multi-GB applications normally distubuted via ISO. Taking on Microsoft, IBM, Oracle et al with Puppet is no small feat and is probably worth a much larger discussion but hopefully this will let you realise that such things are possible.

My first start at this was the Microsoft Office suite of applications. Most of these types of applications support silent installation to make it easy for administrators to deploy via group policy. We don't want to distrubute by group policy but we can use puppet to template these answer files and exec that silent installation.

Templating and Exec-ing that setup.exe is really as complicated as it gets with regards to pupept itself. You find that the remaining complexity comes from the applications itself.

But using those exec resources too is another smell. If your using more than one exec in your manifest and/or you keep calling out to the same command line tool then this is another suggest that you need to be writing more types and providers.

For larger more complicated applications you will find yourself using many of the tools in the puppet toolbox - custom types/providers, custom facts and perhaps custom functions. If you find yourself doing this try and make those thing as genric as possible and split them out into smaller modules. I am current working on a module of MSExchange [[4]](#ce43fac37be445f0bb6a6c9d74b55752) and while prototyping this with ulgy exec statements and numerous hacks - it is leading down a path to create other modules for some custom functins and facts.

The point of this is to prove that all of those huge applications or suites of applications can still be installed and managed by puppet. It takes a great deal of initial effort, experience and on-oging work but it is worth it for us all in the long run. These sorts of applications come with long installation guides and come with certifications - we don't all need to read this and take the exams if we can make puppet do all the heavy lifting for us.

###References
<ul style="list-style-type: none; padding:0; margin:0;">
  <li>
    <a name="53f76edfd65c1180adcd08fb6eb7bd45">[1] http://puppetlabs.com/blog/facter-1-7-introduces-external-facts </a>
  </li>
  <li>
    <a name="347ddd0bb5273c14a5cce0688cef7939">[2] http://technet.microsoft.com/en-us/library/bb490890.aspx </a>
  </li>
  <li>
    <a name="9d7fcbe9e40e5fac0ea095bfdfdae797">[3] https://github.com/vStone/puppet-testing-example </a>
  </li>
  <li>
    <a name="ce43fac37be445f0bb6a6c9d74b55752">[4] https://github.com/liamjbennett/puppet-msexchange </a>
  </li>
</ul>
