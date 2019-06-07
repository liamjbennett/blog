+++
date = "2013-12-11"
description = ""
title = "profiles, roles, stacks and clouds"
type = "post"

+++

One of the more recent patterns in structuring out puppet manifests is: roles and profiles [[1]](#968504594f013f0067f2c0f7ec5c5fb8) [[2]](#9031aeaf735f6dffb9872a8328853a5f). The summary is this: profiles are a collection of classes/modules and roles are a collection of profiles. Having started to re-factor our own infratructure with this pattern recently there was one question that cam immediately to mind .. what's next?

Roles and profiles is all about abstraction. With roles all I have to care about is what "type" of node I am building:

    class role::www inherits role {
      include profile::tomcat
    }

But what is the next abstraction? How far can we abstract?

###Stack
Can we group together those nodes and roles? What I would like to see is the "stack" ..

    define stack::webstack(
      $node_webserver,
      $node_appserver,
      $node_dbserver
    ) {
         node $node_webserver {
           include role::webserver
         }

         node $node_appserver {
           include role::appserver
         }

         node $node_dbserver {
           include role::dbserver
         }
     }

This does use the node declarations rather than the ENC but it can allow us to scale out small indeependant infrastucture quickly.

###Cloud
Puppet also is now moving beyound the server to network swtiches and embedded hardware. Can we also extend out thinking beyond the 3-tier web stack? Can we use puppet to manage independent regions or independent clouds? I would like to see something like the following ...

    define cloud::region(
      $stack
      $network
    ) {
      include $stack

      network_route { $network:
        ensure    => 'present',
        gateway   => '10.0.2.2',
        interface => 'eth0',
        netmask   => '255.255.255.0',
        network   => '172.17.67.0'
      }
    }

Do I have any code to show? Not yet. What I have is lots and lots of questions ..

<br/><br/>
If you want to discuss this more then reach out to me on twitter <a href="https://twitter.com/liamjbennett">@liamjbennett</a>

###References
<ul style="list-style-type: none; padding:0; margin:0;">
  <li>
    <a name="968504594f013f0067f2c0f7ec5c5fb8">[1] http://www.craigdunn.org/2012/05/239/ </a>
  </li>
  <li>
    <a name="9031aeaf735f6dffb9872a8328853a5f">[2] http://www.slideshare.net/PuppetLabs/roles-talk </a>
  </li>
</ul>
