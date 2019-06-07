+++
date = "2014-09-01"
description = ""
title = "testing puppet with beaker pt 2 - the windows story"
type = "post"
categories = ["puppet","testing"]
+++

The second installment in the series on the Beaker testing tool.

This post covers the work that was done to enhance the tool for testing windows systems.

This was originally posted at: http://tech.opentable.co.uk/blog/2014/09/01/testing-puppet-with-beaker-pt-dot-2-the-windows-story/

---

In [part one](/blog/2014/04/04/testing-puppet-with-beaker/) we discussed our first steps into the world of acceptance testing our Puppet manifests.
By using Beaker we able to test managing local users on our Linux boxes. This was a positive experience for us. It allowed us to get to grips with the basics of configuring
Beaker to run tests and configuring our node sets to run those tests against. In this post, we will be discussing how we went about getting Beaker working with Windows.

As many of your reading this will be aware, OpenTable currently has quite a large Windows infrastructure and we are using Puppet extensively to maintain that environment.
We are also moving forward with releasing as many of our modules open source onto the [Puppet Forge](https://forge.puppetlabs.com/opentable) as possible (11 out of 18 of which are Windows
exclusive). What this means is that there was no way that we could ignore trying to use Beaker to test our manifests against Windows. We knew that we would have to support
many different versions and editions of Windows out there in the community as well that the ones we have to support internally.

This was going to be a challenge (configuration management with Windows usually is) but we were up for it.

## The Preliminaries
### Serverspec
The first step was looking at Serverspec. Serverspec is a Ruby gem that provides extensions to RSpec that allow you to test the actual state of your servers, either locally
or from the outside in via SSH. What we needed to know was did it support Windows? The answer was thankfully a resounding "Yes!". All the [resource types](http://serverspec.org/resource_types.html) that you might want to test including file, service and user are available and supported on Windows. There are also a couple of Windows specific ones such as iis_website, Windows_feature and Windows_registry_key. We even added our own to support [Windows_scheduled_task](https://github.com/serverspec/serverspec/pull/403/files). Interestingly Serverspec also supports WinRM as an alternative to SSH when you are testing from the outside-in but we will go back into that later. As long as your using Serverspec > 1.6 you will have all the Windows support you might need.

### Packer
Step two was to build some Windows Vagrant boxes to test against. The documentation on the [wiki](http://github.com/puppetlabs/beaker/wiki) was (at the time) a bit slim when it came
to building test boxes but we knew we needed Cygwin so we went ahead and created the boxes that we needed. All our boxes are created with Packer [and are open sourced on GitHub](http://github.com/opentable/packer-images). They have also been [published to Vagrant Cloud](http://vagrantcloud.com/opentable)
so you can download pre-built images and get up and running quickly (version 1.x images contain the Cygwin installation).

### Beaker
So far, so good. We hit a couple of issues in our initial test runs with Beaker: missing module_path, installation using the msi and 32-bit Windows support - but these were very
small issues and we were happy to be able to contribute back some changes ([234](https://github.com/puppetlabs/beaker/pull/234),
[235](https://github.com/puppetlabs/beaker/pull/235), [236](https://github.com/puppetlabs/beaker/pull/236)). We were very happy and managed to get out first module tested,
the [cross-platform module puppet-puppetversion](http://github.com/opentable/puppet-puppetversion/) for doing Puppet upgrades.

## The First Example
Let's take a more detailed look at those puppetversion tests, how we configured Beaker to run and how it changed for the Windows support. I am going to assume at this point that
you already have some familiarity with Beaker; if not and this is your first steps into the testing tool then I would suggest going back and read [part one](/blog/2014/04/04/testing-puppet-with-beaker/) of this series which contains a little bit of background to this and some useful resources for getting started.

The first thing that we needed to change for Windows was our [spec_accepentance.rb file](https://raw.githubusercontent.com/opentable/puppet-puppetversion/master/spec/spec_helper_acceptance.rb).

Step one was to include the appropriate Serverspec helpers. What this does is let Serverspec know that we are executing on Windows so that underlying resources work correctly. We are also telling
server spec here to communicate using WinRM.

    require 'beaker-rspec/spec_helper'
    require 'beaker-rspec/helpers/serverspec'
    require 'winrm'

    hosts.each do |host|
      case host['platform']
        when /windows/
          include Serverspec::Helper::Windows
          include Serverspec::Helper::WinRM

          version = ENV['PUPPET_VERSION'] || '3.4.3'

          install_puppet(:version => version)

      else
        install_puppet
      end
    end

    ...


The next step is to configure WinRM so that it can connect properly. In our case this meant connecting to Vagrant boxes.

    ...

    RSpec.configure do |c|
      ...
      hosts.each do |host|
        c.host = host

        if host['platform'] =~ /windows/
          endpoint = "http://127.0.0.1:5985/wsman"
          c.winrm = ::WinRM::WinRMWebService.new(endpoint, :ssl, :user => 'vagrant', :pass => 'vagrant', :basic_auth_only => true)
          c.winrm.set_timeout 300
        end

        ...
      end
    end

    ...

Now let's look at one of the tests themselves.

The first part should look pretty familiar. We use the face('osfamily') helper in Beaker to make sure that the test itself is only ever executed for our Windows hosts. We are then running an apply_manifest two times in order to validate that the manifest is idempotent. The only different here is that we are specifying a custom Windows-specific module_path.

    ...
    require 'spec_helper_acceptance'

    describe 'puppetversion', :unless => UNSUPPORTED_PLATFORMS.include?(fact('osfamily')) do
      ...

      context 'upgrade on windows', :if => fact('osfamily').eql?('windows') do

      it 'should install the new version' do
        pp = <<-PP
          class { 'puppetversion':
            version => '3.5.1',
            time_delay => 1
          }
        PP

        apply_manifest(pp, :modulepath => 'C:/ProgramData/PuppetLabs/puppet/etc/modules', :catch_failures => true)
        expect(apply_manifest(pp, :modulepath => 'C:/ProgramData/PuppetLabs/puppet/etc/modules', :catch_failures => true).exit_code).to be_zero
      end

The next part is where we actually perform the bulk of the tests. In the case of this module, we are testing
that the scheduled task has run and that Puppet has been upgraded to the appropriate version. We are making use
of the Windows_scheduled_task resource that we created earlier:

      describe Windows_scheduled_task('puppet upgrade task') do
        it { should exist }
      end

      #This will fail if your laptop (and therefor the Vagrant vm) is not running on AC power
      describe package('puppet') do
        it {
          sleep(240) #Wait for the task to execute
          should be_installed.with_version('3.5.1')
        }
      end

      describe Windows_scheduled_task('puppet upgrade task') do
        it {
          pp = <<-PP
            class { 'puppetversion':
              version => '3.5.1'
            }
          PP

          apply_manifest(pp, :modulepath => 'C:/ProgramData/PuppetLabs/puppet/etc/modules', :catch_failures => true)

          should_not exist
        }
      end
    end

The final part was to configure the nodeset file for the Windows box that we wanted to run our test against:

    HOSTS:
      windows-2008R2-serverstandard-x64:
      roles:
        - agent
      platform: windows-server-amd64
      box : opentable/win-2008r2-standard-amd64-nocm
      box_url : opentable/win-2008r2-standard-amd64-nocm
      hypervisor : vagrant
      user: vagrant
    CONFIG:
      log_level: verbose
      type: git

This was working well for us so we continued on to our next module.

The next module we chose to look at was [puppet-Windowsfeature](http://github.com/opentable/puppet-Windowsfeature).

The test we have implemented in this moudle looks like this:

    require 'spec_helper_acceptance'

    describe 'Windowsfeature' do
      context 'windows feature should be installed' do
        it 'should install .net 3.5 feature' do

          pp = <<-PP
            Windowsfeature { 'as-net-framework': }
          PP

          apply_manifest(pp, :catch_failures => true)
          expect(apply_manifest(pp, :catch_failures => true).exit_code).to be_zero
        end

        describe Windows_feature('as-net-framework') do
          it { should be_installed.by('powershell') }
        end
      end
    end

This module was a little more tricky. Why? Installing Windows features requires elevated permissions. What this meant is that when Beaker attempted to SSH into our Windows box and our Puppet module ran its underlying PowerShell we were faced with a harsh and non-descriptive **"Access is denied error"**.

## SSH
Not all SSH daemons are created equal. To understand the "Access is denied error" we were seeing and why it happens you need to understand a little bit about how sshd on Cygwin works. You can read all about the details from the Cygwin forum archives ([[1]](http://cygwin.com/ml/cygwin/2004-09/msg00087.html), [[2]](http://cygwin.com/ml/cygwin/2006-06/msg00862.html), [[3]](http://thread.gmane.org/gmane.os.cygwin/128472), [[4]](https://cygwin.com/cygwin-ug-net/ntsec.html#ntsec-nopasswd1)) but TLDR; is that you need to use a username and password rather than private key authentication in order to get reasonable admin permissions. Having said all that, and having read all the documentation about the issue above we were still facing the same problem so we had to look at alternative options.

There are several paths you can go down and I want to tell you about them here to save you a similar yak shave:

### OpenSSH for Windows
A thinner alternative than having to install the full Cygwin stack using OpenSSH for Windows is the same OpenSSH implementation. The issue here however is that it doesn’t contain some of the Unix binaries required for Beaker to function. You can work around this if you have Git for Windows installed on your machine by putting its bin directory on your path but overall this doesn’t really solve any of the issues we were facing. We get a lighter footprint on the machine but still the same error as before

### Bitvise SSH Server
[Bitvise SSH Server](http://www.bitvise.com/ssh-server-download) is an alternative SSH implementation (of which there are many more listed on [Wikipedia](http://en.wikipedia.org/wiki/Comparison_of_SSH_servers)). It resolves the permissions issue (it deals with the elevation internally) and has the benefit that it provides a proper command shell rather than a emulated bash shell. It also means we don’t have to have any binaries on there that we don’t need - a big plus. It would mean that we needed to make a few small changes to Beaker in order to replace some of the internal bash command with Windows alternatives but this was not a big task to do and is something we could contribute back.

### WinRM
Could we do away with SSH altogether? It eliminates the problem we were facing and also means we don’t have to install anything on our Windows boxes - it’s all built in already. This would be an ideal solution but does all our tooling support it? I’ll discuss this in a little bit more detail later.

### Not use Beaker at all
The nuclear option. If we couldn’t get anything to work we could not use Beaker at all, we could try and use Test Kitchen (with [test-kitchen-puppet](https://github.com/neillturner/kitchen-puppet)) or some hand-rolled solution. Not the best idea, for us or the community but we though we might have to go down this path at one point. We even added [Windows support to test-kitchen-puppet](https://github.com/liamjbennett/kitchen-puppet/tree/Windows_support) as part our diversion in this direction.

## What worked in the end:
So we went down all these avenues and decided that the best option for us was to use Bitvise. It fixed the problem we were facing but it meant that we had some work ahead of us:
1. We had to rebuild all our Windows images with Bitvise rather than Cygwin ([vagrantcloud.com/opentable](https://vagrantcloud.com/opentable) - version 2.x images now have this)
2. We had to make some changes to Beaker to support using a standard Windows command shell rather than a Unix shell:

   - [https://github.com/puppetlabs/beaker/pull/419](https://github.com/puppetlabs/beaker/pull/419) – configure_puppet method
   - [https://github.com/puppetlabs/beaker/pull/419](https://github.com/puppetlabs/beaker/pull/420) – host_entry method
   - [https://github.com/puppetlabs/beaker/pull/419](https://github.com/puppetlabs/beaker/pull/418) – Vagrant box_version
   - [https://github.com/puppetlabs/beaker/pull/419](https://github.com/puppetlabs/beaker/pull/424) – Bitvise SSH

With it finally working we had something that looked like this:

##Second Example

Well with all the changes we implemented there were actually very few changes that we needed to make to our actual tests code.

No adjustments are needed for our spec_acceptance.rb file.

No adjustments are required for our spec file (show above).

The main change we made was in the nodeset file:

    HOSTS:
      win-2008R2-std:
      roles:
        - default
        - agent
      platform: Windows-server-amd64
      box: opentable/win-2008r2-standard-amd64-nocm
      hypervisor: vagrant
      user: vagrant
      ip: '10.255.33.129'
      communicator: bitvise
    CONFIG:
      log_level: verbose
      type: git

The biggest change you will see here is the addition of the 'communicator' option. What this does is to allows us to actively select to use either Cygwin or Bitvise. This means that in our case we want to use Bitvise SSH as this fixes the error we were seeing and it's the version of SSH now installed on your newer Vagrant boxes. Bitvise is the only supported option at the moment (in our Beaker fork) but it is likely that this will soon support WinRM as well.

Things to note here:
* The name of the Windows host defined in the node set must be the same as the name of the Windows hostname - if it is not then when Vagrant boots up it will change the hostname
which will put Windows into a "restart pending" state.

## The Future and WinRM
Most modern versions of Windows server have WinRM enabled by default but if you are using an older version or you are attempting to test a client then you will need to make sure
that this is enabled on your boxes. This is still the direction that we would like to go long-term as it is the most Windows-friendly approach but there are few road blocks in
the way of doing so right now:

1. Packer doesn’t set support WinRM as a communication method. This is being actively worked on and you can follow the work here:

    - [https://github.com/mitchellh/packer/issues/451](https://github.com/mitchellh/packer/issues/451)
    - [https://github.com/dylanmei/packer-communicator-winrm](https://github.com/dylanmei/packer-communicator-winrm)

2. Beaker doesn’t yet support WinRM as a communication protocol. This is currently being discussed internally after we raised the idea. The work that we have completed for
Bitvise support will go some way it allowing other providers, such as wirm going forward and therefore WinRM support should be coming in the near future.

## Summary
Using Beaker to test modules for Windows has been a long and complicated journey. I have attempted to cover here all the problems that you might run into when trying to do this for yourselves and provide some good examples to get you going. You will soon see this being rolled out to all of the OpenTable open source modules shortly so you will have some complete working examples to reference. We will continue to work with PuppetLabs in improving Beaker (and its Windows support) in order to make this a easy process for everyone.

For any questions or comments then please reach out to me on twitter [@liamjbennett](https://twitter.com/liamjbennett)