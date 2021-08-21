---
author: "liamjbennett"
title: "Puppet on Windows - part 1"
date: "2013-10-06"
description: ""
tags: ["puppet"]
ShowToc: false
ShowBreadCrumbs: false
expiryDate: "2015-12-01"
---

I have recently spent some time working with puppet, in particular working on writing modules for Windows and I wanted to share some of my thoughts and experiences that I learnt along the way.

###Finding useful information
When I got starting writing my first module the thing that I realised was that at the time there was very little information out there of people using puppet on Windows. Thankfully in the past few months this has changed and I wanted to point you in the direction of some very useful resources:

* <a href="http://puppetlabs.com/blog/part-top-questions-on-puppet-and-windows">http://puppetlabs.com/blog/part-top-questions-on-puppet-and-windows</a>
* <a href="http://www.slideshare.net/PuppetLabs/puppet-and-windowspuppetconf2013">http://www.slideshare.net/PuppetLabs/puppet-and-windowspuppetconf2013</a>
* <a href="http://www.slideshare.net/PuppetLabs/chocolatey-puppet-conf2013">http://www.slideshare.net/PuppetLabs/chocolatey-puppet-conf2013</a>
* <a href="http://vimeo.com/68226718">Paul Stack: Windows - Having its ass kicked by Puppet and PowerShell since 2012</a>

###Your 3 new friends: Powershell, MSDN and the Registry
This really depends what background your coming from. If your a developer or operations engineer from a Windows background and your just starting to use puppet, well then you probably know this already. If however your a coming from a Linux background and your looking to expand your puppet infrastructure to cover you Windows environments (and this was me) then you've got some learning to do.

The first thing is get to know Powershell [[1]](#aaf77b1d1120543427c88d09b8b11faf)[[2]](#5a0292306a28b0000065d5004ca8f48b)[[3]](#eab9bab48399d59bf2d392eb87666917) - it's either bash for Windows or cmd on steroids depending on your point of view. Either way your going to find it very useful when trying to bend Windows to your will. Not that you need to be a master of Powershell to be productive with puppet on Windows but go and read, get familiar with how it works and get ready to google plenty. Powershell (recent versions on recent versions of Windows) allows you do do almost everything that you will want to configure from the command line. It is a feature rich language that most Windows operations people will be familiar with and best of all that means that there is plenty of code out there that makes good examples.

Next up is the big daddy of them all - the MSDN/TechNet documentation [[3]](#0533b0d73a6d8c4dbcc37b1eb665edee). This is a huge archive that contains documentation on every built in library, utility and registry setting that comes with Windows. The more you work in the Windows world the more you will find yourself staring at its pages - that's if you can find the one your looking for. A lot time was spent while writing my first Windows modules tracking down useful documentation - installation prerequisites, silent install options, config files options, registry tweaks. Digging all of this out can be time consuming but in the end totally worth it. <b></i>Do your module users a favour and put links to these documents either in your README or in your wiki - it will save the pain for us all.</i></b>

The Windows registry is the final weapon in your toolbox. If you've ever even looked at a Windows machine before then this is not news to you but your going to learn this more than you have ever done so before. Firstly it will help you in making sure your configurations are idempotent but also most Windows applications these days have both documented and undocumented registry tweaks so it would be good to expose some of them in your modules.

###The 3 classic problems: Packaging, ISOs and reboots
When discussing windows with other puppet users the three topics that always come up are windows packaging, installing large applications that are distributed via ISOs and how best to manage system changes that require reboots.

####Packaging
Packaging is a challenge on all operating systems and despite some very successful tooling like fpm [[5]](#ce0ca10e13a9f4b4e7d605b5c88574ca) it still continues to have it's problems. Windows is no exception to this. Windows has many methods for getting software onto the box: the exe, the msi, the 7zip executable, the zip file and probably a few more that I haven't even come across yet. Each is also authored with very flexible tooling which means that you will face issues like packages that will declare their dependencies while others won't and packages that install the source while other wants you to do it all yourself. Even the msi package which is by far the industry standard has it's faults. The reality is that all of these methods need to be supported because there are applications out there that continue to use them so any configuration management system needs to deal with that as gracefully possible.

Puppet's Package resource is very well suited to create this abstraction. In version 3.x it's as simple as:

    package { 'Firefox Setup 21.0':
        provider => windows,
        ensure   => installed,
        source   => 'C:\\Files\\Firefox Setup 21.0.exe',
        install_options => ['/S']
    }

While this is great for all you 3.x users, there a still a large number of users out there (myself and github included) who are working with a 2.7 code tree. Not all is lost however. Firstly if your only using msi packages then there is nothing for you to do as puppet 2.7 already has you covered with the msi provider:

    package { 'mysql':
      ensure          => installed,
      provider        => 'msi',
      source          => 'N:/packages/mysql-5.5.16-winx64.msi',
      install_options => { 'INSTALLDIR' => 'C:\mysql-5.5' },
    }

Alternatively if you still need to support those pesky exe files then Reid Vandewiele (<a href="https://twitter.com/reidmv">@reidmv</a>) has you covered with his 2.7 backport of the new windows package provider [[6]](#98434dfae6a7f26a3027b584df5932f6):

    windows_package { 'Firefox Setup 21.0':
        ensure   => installed,
        source   => 'C:\\Files\\Firefox Setup 21.0.exe',
        install_options => ['/S']
    }

<br/>
But that's not all - there is one more contender in this game of packaging - and it goes by the name of chocolatey [[7]](#d2724e80cee3722a407052b7ec51c526). Chocolatey is the self-styled apt-get for Windows - so all of your Linux admins can rejoice - and it's also built on the well supported nuget dependency management system - so all of you .NET developers can join in this party. It has a huge community of users so most of the applications and MS re-distributables that you will want are available. Best of all the author is a one Mr Rob Reynolds (<a href="https://twitter.com/ferventcoder">@ferventcoder</a>) is now one of the members of the puppet windows team at puppetlabs so we can expect excellent chocolatey support within puppet going forward. Rich Siegal (<a href="https://twitter.com/rismoney">@rismoney</a>) has already released a puppet provider for chocolatey [[8]](#bc5d64b3fb6f4fa201568b45665a5b19) which means that packages can be installed like this:

    package { 'Firefox':
        ensure          => installed,
        provider        => 'chocolatey',
        install_options => ['/S']
    }


The use of chocolatey really depends on your corporate situation. If your already supporting a private nuget repository then absolutely use chocolatey as it will save you some pain. If your not then it your choices are either configure a nuget repository, use Nexus Pro as a nuget repository, or stick to the old network share approach and the windows package provider. I am not here to say which method you should use - but you should <b>use one</b>.

####Managing those ISOs
Many windows applications, at least "Enterprise-ready" ones and all of those distributed by Microsoft itself are packaged as an .iso file. This is both a throwback of days of boxed software and burned CDs but it also serves the purpose of being a single container for what is often a multi-gigabyte installation. The problem is one of size: you don't want to be downloading 4GB iso onto your clients in order to install your applications. This leaves you with two options: Network share or mounted network drive.

#####Network share
When dealing with large files this is going to be your obvious first approach. Set-up a network share (either windows or samba) and decompress those iso files into a local directory on the share. From there you can do something as simple as this:

    exec { 'install-iso-app':
          command   => "\"\\\\fileshare\\folder\\SETUP.EXE\" /settings \"C:\\config.ini\"",
          provider  => windows,
          logoutput => true,
          require   => File["C:\\office_config.ini"]
    }

The benefit of this approach is that you probably already have this sort of share set-up already. If you've got reasonably large windows environment this probably already existing on your Windows Update (WSUS) server. By installing directly over the network (without mounting) your not exposing this network share to your end clients at all. After all you may have lots of other software on this common windows share and you may not want all of your clients/users to be able to see that.

The disadvantage of this approach is that firstly, not all applications support this approach and secondly you will have to make sure that the network server is added to your local intranet security settings. Luckily the later can be fixed using the puppetlabs-registry module [[9]](#37c5bf3536a4757afb731a719efe546b).

#####Mounted Network drive/folder
The other approach to this problem is to mount a network share either as a drive or a folder. Simon Dean has written a net_share module [[10]](#dcf341f86b8dec6f7940a2e084647e9b) for this.

    net_share {'PuppetTest':
        ensure        => present,
        path          => 'c:\puppet_test',
        remark        => 'PuppetTest',
        maximumusers  => unlimited,
        cache         => none,
        permissions   => ["${hostname}\\PuppetTest,full", "${hostname}\\PuppetTest2,full"],
    }

This approach has the benefit that packages are installed as if they were from a local drive - many applications were written making this assumption. The disadvantage as stated above is that you can unnecessarily expose other applications to your users that you may not want to. There may be ways to mitigate this by mounting then dismounting the drive pre and post-install or mounting to a hidden folder but both approaches seem like a work-around.

My thoughts on the best of these methods to use really varies depending upon the size and complexity of the applications that I am trying to work with. Up to this point I have mostly been working with the network share approach but this required making registry entries and that seems a little nasty. I think that a better approach would be to write an provider just for iso files and use that as a vehicle to work through some of these use-cases.

I will discuss my experiences of using these approaches in a future post where I discuss in more detail the modules that I have written but for now I suggest you go and look at all these available methods and choose the one that best suits your existing environment and security needs.

###Reboots
Up until very recently this a big problem for windows users. May packages require post-install reboots and for more complex applications that install their own dependencies they may require multi-reboots during an installation or upgrade run. This poses the problem of puppet should deal with this - does it skip the reboot and try to run through the rest of the catalog or does it perform the reboot in-line and perform the puppet run again? Well thankfully puppetlabs has come to the rescue with their reboot module [[11]](#daaf6e71bf1eda39b0b3d5266732efdf). This allows reboots to be added into the manifest like this:

     package { 'Microsoft .NET Framework 4.5':
       ensure          => installed,
       source          => '\\server\share\dotnetfx45_full_x86_x64.exe',
       install_options => ['/Passive', '/NoRestart'],
       provider        => windows,
     }
     reboot { 'after':
       subscribe       => Package['Microsoft .NET Framework 4.5'],
     }

Actually I like having reboots within the manifest - it helps prove my idempotence. This module is still being worked on by puppetlabs and at the time of writing there were issues for puppet users running ruby 1.8.x [[12]](#91b2bceeb7f198bd25be62f0e062fe84) but it's a great solution to the problem.


###Summary
Windows is like any other new platform - it has it's quirks and it's own sets of challenges but it also has an existing vibrant community which will be able to help with these sorts of issues and hopefully allow you to write some fantastic new modules for the forge. In part 2 of this post I will discuss the modules that I have written, my experiences of writing them and how they have evolved as both puppet and my experience has evolved.

####References
<ul style="list-style-type: none; padding:0; margin:0;">
  <li>
    <a name="aaf77b1d1120543427c88d09b8b11faf">[1]: http://technet.microsoft.com/en-us/library/bb978526.aspx </a>
  </li>
  <li>
   <a name="5a0292306a28b0000065d5004ca8f48b">[2]: http://technet.microsoft.com/en-gb/scriptcenter/powershell.aspx </a>
  </li>
  <li>
   <a name="eab9bab48399d59bf2d392eb87666917">[3]: http://www.amazon.co.uk/Windows-PowerShell-Cookbook-Scripting-Microsofts/dp/1449320686/ </a>
  </li>
  <li>
    <a name="0533b0d73a6d8c4dbcc37b1eb665edee">[4]: http://technet.microsoft.com/en-us/library/aa991542.aspx </a>
  </li>
  <li>
    <a name="ce0ca10e13a9f4b4e7d605b5c88574ca">[5]: https://github.com/jordansissel/fpm </a>
  </li>
  <li>
   <a name="98434dfae6a7f26a3027b584df5932f6">[6]: https://forge.puppetlabs.com/reidmv/windows_package </a>
  </li>
  <li>
    <a name="d2724e80cee3722a407052b7ec51c526">[7]: http://chocolatey.org/ </a>
  </li>
  <li>
   <a name="bc5d64b3fb6f4fa201568b45665a5b19">[8]: https://forge.puppetlabs.com/rismoney/chocolatey </a>
  </li>
  <li>
   <a name="37c5bf3536a4757afb731a719efe546b">[9]: https://forge.puppetlabs.com/puppetlabs/registry </a>
  </li>
  <li>
   <a name="dcf341f86b8dec6f7940a2e084647e9b">[10]: https://forge.puppetlabs.com/simondean/net_share </a>
  </li>
  <li>
    <a name="daaf6e71bf1eda39b0b3d5266732efdf">[11]: https://forge.puppetlabs.com/puppetlabs/reboot </a>
  </li>
  <li>
    <a name="91b2bceeb7f198bd25be62f0e062fe84">[12]: https://github.com/joshcooper/puppetlabs-reboot/issues/12 </a>
  </li>
</ul>
