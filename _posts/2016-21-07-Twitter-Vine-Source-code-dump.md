---
layout: post
title: "Twitter's Vine Source code dump"
subtitle: "6 Seconds are not enough"
date: 2016-07-22 10:00:00
---
Hello Hackers!

Today I am going to disclose a long awaited bug, which I found in *Twitter's Vine*.

I started participating in various VRPs in 2015 and have been very active since then. Especially in the Twitter Bug bounty program since their response is quick and they release bounty as soon as the bug is __triaged__.

As Vine is within the scope of Twitter VRP, I started looking at the various points of entry I could access.

Discovering subdomains is an important part of reconnaissance, which of late, are mostly automated with various tools.

But I prefer:

 - Subbrute
 - Virustotal.com
 - Dnsdumster.com
 - Dnsdb.org
 - Censys.io
 - CSP headers

Censys.io gave me an interesting URL https://docker.vineapp.com in its result.

![Censys](https://i.imgur.com/TqYfrj7.png)

When I tried to access it via the browser, it shows /* private docker registry */ in the response.

![docker.vineapp.com](https://i.imgur.com/tzqQULl.png)

If it is supposed to be private, then why is it publicly accessible? There has to be some thing else to going on here. On googling /* private docker registry */ I get to know that the docker provides a functionality which allows a developer to host and share images through the web.

I've worked on docker earlier and the experience helped me realize that there could be some chances of finding code in these images. The chances that developers frequently use it to share data, as they do not have to go through the process of setting up the environment again on their local machines, was quite high. However, since I wasn't too familiar with docker APIs, I faced some trouble while accessing images endpoints. The ones I could access, unfortunately, were not giving any useful results.

After figuring out that this docker registry is not using the latest version(V2) and the endpoints are different from previous ones, I needed to use V1 documentation to access them. Only after that was I able to get some useful response from the server.

I started by querying search API endpoint which reveals that around 80+ images are hosted.That was the good sign.

![search](https://i.imgur.com/QS9FUDs.png)

Next thing was to install docker client on my Ubuntu VM and download those images. The search results show a lot of images, however, I decided to download vinewww just because it looks like public_html. This may contain the Vine source.

	sudo docker pull https://docker.vineapp.com:443/library/vinewww

![docker-images](https://i.imgur.com/AcoA7y7.png)

After the download was completed, I ran docker image vinewww with interactive shell and got inside the running docker image.

`ls` in vinewww shows MVC(flask) is used.

![docket-it](https://i.imgur.com/TykNTsl.png) 

I was able to see the entire source code of vine, its API keys and third party keys and secrets. Even running the image without any parameter was letting me host a replica of VINE locally.

![showtime](https://i.imgur.com/qqAsoI2.png)


Till then, keep hacking ;)

PS : Special thanks to @thanmayeerao

Timeline
=====
 - March 21,2016 - Bug Reported through Hackerone
 - March 22,2016 - Need more info
 - March 31,2016 - Full exploitation shown
 - March 31,2016 - Bug fixed (within 5 min)
 - April 2,2016  - $10080 Bounty awarded 



