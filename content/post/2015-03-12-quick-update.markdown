+++
title = "[Quick Update] - 12-Mar-2015"
date = "2015-03-12T08:50:00Z"

+++

It has recently been commented by a few individuals that I am a poor communicator of some of the interesting things that I am usually hacking on. I guess they are right and I thought that rather than wait and do a big-bang style blog post of the usual multi-thousand word variety that I would start trying to write these little posts in about 30 minutes and see how that works out. By the time your reading this I will have likely already written several and managed to build up a least a little motivation in writing again.

\* \* \*

With all that in mind, what have I actually been working on recently?

#### The slow road towards linux on the desktop
Like almost all of my peers, it seems that for a number of years now I have been spending 40+ hours a week curled up with my macbook only to be dissatisfied with the operating system that it comes with. I have already seen a number people start to make the transition to Linux or BSD on the desktop and I think that 2015 might be the year for me (if you’re reading this after 2015 - don’t laugh too hard because I really meant it). With that target in mind I have been spending some time reducing my tooling to only those things that are cross-platform, preferring the command-line and making a note of all those things that I might have to keep OS X around for. So far in the past few months I have changed my password manager (1password to lastpass) my editor (atom to tmux+vim) and made a good list of things I like on OS X (RoyalTSX and VMware fusion) none of which seems to be blocking my transition. I am sure that this little project might turn into one of those big-bang blogs - but don’t hold your breath ;)

#### A few more updates with testing puppet on windows
So I wrote (this) post a while back and I have continue to work on the project and getting the changes that need to made into the master branch of beaker for everyone to use easily. This is almost done now so over the next few weeks you should be able to really start testing those modules - with our packer images of course.

#### Updates to those packer images
From the download numbers it seems like a number of your like using those windows images that I created so I am very happy about that. If you go and take another look at the page on atlas you should see that there a number of new versions there now that you might want to play with. We unfortunately had to temporally close-source the packer templates behind those images while we dealt with an issue with the bitvise installation, although expect this to be open again very soon. In addition to that I am very excited with the things going on over at the packer-community project. It seems like the plugins are now there so that we will eventually be able to remove the bitvise dependency completely, which is exciting.

\* \* \*

Ok, so that’s enough for this first 30-minute update, but don’t worry I have plenty more updates to come in the following days so stay tuned for that.
