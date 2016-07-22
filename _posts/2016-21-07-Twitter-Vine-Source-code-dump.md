---
layout: post
title: "Twitter's Vine Source code dump"
subtitle: "6 Seconds are not enough"
date: 2016-07-22 10:00:00
---
Hello Hackers,

Today I am going to disclose a long awaited bug which I found in *Twitter's Vine*.

I started participating in various VRPs since 2015 and very active since then, specially in Twitter Bug bounty program because their quick response and releasing bounty once the bug is __triaged__.

As Vine is in the scope of Twitter VRP I started looking at what are the various entry point which I could reach.

Discovering subdomains is an important part of reconnaissance which now a days are almost automated with various tools. 

But I use:
 
 - Subbrute
 - Virustotal.com
 - Dnsdumster.com
 - Dnsdb.org
 - Censys.io
 - CSP headers

Censys.io gave me an interesting URL https://docker.vineapp.com in its result.

![Censys](https://i.imgur.com/TqYfrj7.png)

When I tried to access it in the browser it shows /* private docker registry */ in response.

![docker.vineapp.com](https://i.imgur.com/tzqQULl.png)

If it is private then why it's publicly accessible? There must be some thing else to be looked on. On googling  __/* private docker registry */__  I get to know docker provides a functionality so that developer can host and share images through web.

As I've worked on docker before that makes me realized there could be some chances of finding code in these images because developers generally uses it to share and they doesn't have to go through the process of setting up environment again on their local machine. But I wasn't very familiar with docker APIs, I had faced some trouble while accessing images endpoints and those were not giving any useful results. 

After figuring out that this docker registry is not using latest version(V2) and endpoints are different from previous one, I need to use V1 documentation to access them. Only after that I was able to get some useful response back from the server.

I started by querying search API endpoint which reveals around 80+ images are hosted.That was the good sign.

![search](https://i.imgur.com/QS9FUDs.png)


Next thing was to install docker client on my Ubuntu VM and download those images,search results shows a lot of images however I decided to download **vinewww** just because it looks like *public_html* which may contain Vine source.

	sudo docker pull https://docker.vineapp.com:443/library/vinewww

![docker-images](https://i.imgur.com/AcoA7y7.png)

After the download was completed I run docker image vinewww with interactive shell and get inside the running docker image.

`ls` in vinewww shows MVC(flask) is used.

![docket-it](https://i.imgur.com/TykNTsl.png) 

I was able to see the entire source code of vine, its API keys and third party keys and secrets. Even running the image without any parameter was letting me to host a replica of VINE locally.

![showtime](https://i.imgur.com/qqAsoI2.png)


Till then, keep hacking ;)

###Timeline

 - March 21,2016 - Bug Reported through Hackerone
 - March 22,2016 - Need more info
 - March 31,2016 - Full exploitation shown
 - March 31,2016 - Bug fixed (within 5 min)
 - April 2,2016  - $10080 Bounty awarded 



