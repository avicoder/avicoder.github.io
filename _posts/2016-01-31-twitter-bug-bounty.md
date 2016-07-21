---
layout: post
title:  "Twitter Bug Bounty"
subtitle: "We all started at some point"
date: 2016-01-31 10:00:00

---

Bug bounty is cool, It pays you well enough along with the recognition that we generally call Hall of Fame. However, you need to prepare yourself for its most important blocks, which are **_Patience_** and **_Constant growth in your knowledge_**. Sometimes you could catch a severe bug by just looking at the traffic in the interceptor or say just by understanding the working of application over a night. On the other hand, it could take days, months and even years depending on the lessons learnt from previous experiences.

I'm a *Programmer* , I spend most of my time doing programming but I also have a corner for Cyber Security, that motivate me to arm myself for the next big Bug Hunt. I heard a lot about **Hackerone**. I think it is the best platform for security researchers who want to make good money, as it handles everything from submitting the report to receiving monetary rewards. Twitter has a bug bounty program on Hackerone.  

I would like to share my experience of unearthing a few of the bugs that I have hunted down and for which I have received bounties and recognition from Twitter. I would urge you to read about the scope of the bugs that comes under the reward program before looking for bugs.
My first bug in Twitter was the open redirection in fabric.io that allowed the attacker to add his domain of choice and force the victim to be redirected to that domain. While it looks very simple (which it is not), I had to do a lot of fuzzing to obtain a positive result. By intercepting and analyzing the traffic after successfully log into my account the page gets redirected to a URI [https://www.fabric.io/login?redirect_url=/dashborad](https://www.fabric.io/login?redirect_url=/dashborad), which ultimately reveals the [https://www.fabric.io/dashboard](https://www.fabric.io/dashboard) page. Now if I try to access [https://www.fabric.io/login?redirect_url=/payload](https://www.fabric.io/login?redirect_url=/payload), it leads me to a 404 error page with the URI [https://www.fabric.io/payload](https://www.fabric.io/payload). After doing extensive fuzzing with the payload value I was able to redirect it by adding “@” before the desired domain name. So my payload becomes [https://www.fabric.io/login?redirect_url=@avicoder.me](https://www.fabric.io/login?redirect_url=@avicoder.me), which redirects me to the website “[avicoder.me](https://avicoder.me)”.

Link to the report: [#39631](https://hackerone.com/reports/39631)


I found another bug in Twitter’s acquisition, **_Vine_**, which is a 6-second social video-sharing website. As Twitter mobile apps also come under the scope of their bug bounty program, I started exploring mobile appsec. Mobile application testing could give you more fruitful results compared with web app, because there are few mobile application penetration testers. My coding knowledge in various languages helped me to uncover a bug in their source code, which allows the attacker to inject a snippet in JavaScript and gain access to all the permissions and resources of the Vine app. More commonly, this type of bug is called WebView Vulnerability.

WebView is an activity in Android OS that allows the application to use its native browser inside the app, so that a user doesn’t have to leave the app to see the webpage. In any WebView instance JavaScript is disabled by default. Twitter’s Vine Android app uses WebView activity with JavaScript enabled for pages like Privacy policy, terms and condition, etc. 
I decompiled the source code and, using `dex2jar`, loaded the .jar file in `JD-GUI` application. After analyzing the source code I found a class with the name webviewActivity.class. 
The trimmed code below shows the vulnerable part of the app. 

~~~
super.onCreate(paramBundle, 2130903209, false);
WebViewlocalWebView = (WebView)findViewById(2131362017);
localWebView.setWebViewClient(new WebViewClient());
localWebView.getSettings().setJavaScriptEnabled(true);
Bundle localBundle = getIntent().getExtras();
HashMaplocalHashMap;
~~~
{: .language-java}


I am pointing out the line below that enabled the JavaScript explicitly.

		localWebView.getSettings().setJavaScriptEnabled(true);

I have written a detailed explanation along with the exploitation of WebView in Github. In case you want to know more about the technical aspect of this vulnerability [here](https://github.com/vjex/WriteUp/blob/master/WebviewVuln.md). After getting a response from Twitter that the vulnerability is valid and accepted, I couldn’t stop myself from looking for the WebView vulnerability in Twitter app. I followed the same steps as in Vine. I found the vulnerability and reported it immediately with reference to the Vine report number. They accepted my bug and triaged it.However, the exploitation of this vulnerability is limited till Android OS version 4.2.2 jellybean, which corresponds to 65% of all mobile platforms at the time the bug was reported. I received the minimum payout from Twitter as it is more likely an operating system flaw rather than a flaw in the Android application itself. Google fixed this vulnerability in the later version, but not in 4.4.2 Jellybean.

The next bug in my hunting exploits is related to the insecure transmission of media files, which again I discovered in the ***Vine Android app***. When I upload a video, the traffic for media files does not go through an encrypted tunnel and is susceptible to a Man-in-the-middle attack. I was also able to see the endpoint URI of my videos stored in Vine CDN, which allowed me to download the videos. The following link is the POC for this vulnerability.

[Vine Insecure Transmission of Media Files POC](https://www.youtube.com/watch?v=iTCMhqMtroM)

{::nomarkdown}<iframe width="654" height="280" src="https://www.youtube.com/embed/iTCMhqMtroM" frameborder="0" allowfullscreen></iframe>{:/nomarkdown}

Now lets see next bug which I found in ads.twitter.com, After closely examined the traffic of ads.twitter.com with their API calls. I created some dummy Twitter accounts and associated them to a campaign. In the source code I found a URI that takes the username in the query parameter and displays the information about campaigns associated with the account. This URI is not used by the application user but is instead used by the Twitter administrator for some backend purpose; therefore, it was not captured by the interceptor. This is where looking at the source code helped me to find this hidden URI to execute admin level operations. It discloses information for any campaign such as the identities of the admin, the analyst and the manager along with information on whether credit card payment is enabled or not, which should be visible only to the original creator of the campaign. However, in this case it was publicly accessible to everyone. I just needed to change the user ID of my choice.

Link to the report: [#49806](https://hackerone.com/reports/49806)

The final bug for this blog is about the storage of username and password in plain text by the Android application of Vine. I discovered this bug by using a great OS developed by Appsec-Labs `Appuse`, which takes cares of all the customizations that are required in Android application security. It allows the user to root/unroot and intercept the request/response of the application with just a single click. It operates very well and I highly recommend Appuse because it comes with preloaded vulnerable apps that would help you to gain a basic understanding of Mobile applications. This bug was simple. I just browsed some social networking websites inside the app and looked for the SQLite database for changes. The Vine app was storing them in plain text without using any keychain for encryption, which is a bad practice. It is enabled by default and it should be disabled by the application developer.  

Link to the report: [#44727](https://hackerone.com/reports/44727)


The web is changing very fast with recently developed technologies incorporated as the need of application; for example, Facebook introduced their own language “Hack”, which is a fork of PHP but makes much better use of data structures and is much faster than PHP. Apple comes with Swift for their iOS application development. Therefore, as this change continues, there is always a chance of unearthing multiple vulnerabilities. 

In 2015, I hunted down 15 bugs in Twitter. I cannot disclose all of them, as they have not yet been fixed by Twitter and I am bound by a non-disclosure agreement; however, I will share the information about the bugs once they are fixed till then Happy Hunting.

@avicoder