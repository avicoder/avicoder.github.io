---
layout: post
title:  "Security Roadmap, Strategies and Challenges"
subtitle: "My Learnings - Part-1"
date: 2022-08-06 10:00:00

---

*It's hard to develop a cybersecurity roadmap since several elements need to be considered, such as compliance and risk posture, policy framework, detection and response capabilities, resilience and recovery after a breach.*

Hi Everyone 👋 , in this **part-series** I’m gonna to be sharing about developing a security roadmap, that usually comes after asking some relevant questions. Also, I'll talk about what good security looks like, because it's hard to make a good roadmap if you don't really know what you're aiming for. I'll talk about where to start and how to get there.

Let's discuss what executives typically ask...

<img src="/images/d-1.png" height="50%" width="50%">

>Are we Compliant?

You can be compliant, but that doesn't mean you're secure, but you can get there and there's a lot in compliance requirements and standards etc. that'll help you out. In the end, it won't make a lot of difference unless you live and breathe it.

>Are we Secure?

In the same token, you can be compliant and still be secure, and we see that quite a bit of the time, when people have very good security practices and operations in their organization, but they're bad at documenting stuff, so from a compliance standpoint, they won't be compliant but still secure.

>How much progress did we make in making us more secure?

How did we do compared to last year? That's a tough one since the landscape in which we worked last year was different. As you know, the attacks that we saw last year might have been a few, but now we may see attacks that are vastly different from what we saw in the past. Information Security is a dynamic discipline, which means that everything changes and everything stays the same, so all the processes, procedures, and things we do from an operational perspective don't really change that much over time. However, attacks, how we respond to them, do change every day, so it's a bit of both.

In the last 12 months if you didn't change your security effort, you were doing a great job dealing with the types of attacks you were seeing, but if you're still doing the same thing, then there's a fair chance that the attacks have outpaced you.

>What would we do in case of a breach?

This is a great question because they're trying to figure out if you're prepared for an attack since their awareness has been raised. Whenever there's an incident, we see people like you asking this question.


When executives ask all these questions above, there's actually a subtext to the questions that they're actually asking. 

*When they ask for “Are we compliant?” they're really asking...*

 - In order to achieve or exceed our goals, what standards must we meet?
 - Have we met them yet?
 - How are we doing? Do we continue to meet with them? 


*On the similar footsteps “Are you secure?”*

 - What are the current risks and how well do we understand them?
 - Are we aware of our key assets?  
 - What are we doing to protect those key assets? 

That’s the question really being asked!!

*“How much progress did we make in making us more secure?”*

- Over the past year, what has changed?
- What are we doing to meet these new challenges?
- What are the areas where we need to improve?


*“What would we do in case of a breach?”*

 - How have we handled incidents that have actually occurred?
 - What did we learn and how are we adapting?
 - Were there any changes we made to ensure we met the challenge? 


In essence, that's what the executive is asking when he's asking any one of these four questions, but if you ask them on their own they can be difficult to understand, but if you combine them, they give you a clearer picture of where the organization fits into the security structure.

<img src="/images/d-2.png" height="50%" width="50%">

## What does good security look like?

>Good security needs to be proactive

In a lot of companies, security teams are purely reactive, they react to new features and projects request for assessment. We've all probably run into the situation where someone comes up to your desk just before the weekend and says “hey, this project needs to go live in a few hours, can you please approve it? 😰”. Our security team needs to change from a reactive to a proactive one.

>Security should not be Obstructive. 

Often, in-your-face security generates obstacles to the business, so our role as security team is to ensure that the business is able to do what it needs to do in a secure manner. Nobody has ever thanked a security team for saying "No" constantly. Obviously there are times when saying No is the right thing to do because there are plenty of things from a security perspective that are bad ideas, but ideally you'll have a security team that can actually contribute to the success of the organization.

>Security Coverage is one of the main pillars.

The right coverage needs to happen,with tools and solutions that are in place, we let it run and then in many organizations it is just there for the rest of the year. We come across systems that after it's been implemented it's never been touched, well it does what it's supposed to do but they do need kind of a little bit of love.

>Implement technology/controls correctly

If your organization is at the point where you have firewalls and anti-viruses - for instance, if you have firewalls, then your next purchase won't be one that grabs everything and analyzes it all - there is probably a technology use between the two that you will want to consider.

>Minimize the Risk

There is a need for us to understand what the risks are. We need to understand what we will be able to do about these risks in order to minimize them as much as possible.

>Cost Effectiveness

Security solutions must be cost-effective. If it is going to cost 2-3 times as much as the annual revenue of the company, it is probably not going to be of much use to the company.

>Responding to current threats

Having an understanding of what's going on in the world right now will give your security team a competitive edge towards proactiveness.

>Repeatable process

You must be able to repeat whatever you do. If you discover an XSS, you may be able to find the same issue anywhere with the help of tools and scripts sooner, so you can focus on more interesting things rather than sweating over finding the same issue on different instances a week later.

>Detailed documentation

Documentation is important and we all kind of stink at it a little bit. but it's okay to start small and then build slowly.

<img src="/images/d-3.png" height="50%" width="50%">

## What does it take to get good security?

In an organization, four main functions must take place:

 - Make sure you're taking some sort of **Risk and Compliance/Governance** to help identify what you need to protect. To do this, you need to know your assets, your risks, your controls, your metrics, your policies, etc., all documented in a rinse, lather, repeat manner.

 - There is typically some sort of **Security Architecture and Design** component within an organization, this is a team that liaises with the business more closely to understand what the requirements are, what the impacts are, how I will protect it and how will I know it's being done well. We can't emphasize enough how important it is to get into a project earlier. Instead of finding out at the end that someone has put a database somewhere in the internet and you're connecting to it over HTTP. Or, code has been downloaded from a Russian website and embedded into your core application, it would be nice to find out at the beginning rather than at the end.

 - The **Security Administration** function is all about adding users, giving them access, taking it away, and doing some reviews. In order to succeed in security administration, you typically need to have some defined processes, regular review, and maintenance procedures.
 
 - **Security operations** role is to detect,respond and identify any threats. The goal here is to gain visibility on network servers and endpoints, and make sure that the tools that cover what you're supposed to cover are configured appropriately. Respond to threats, manage them, and analyze them.


Skills and services for all of these requirements are not necessarily confined to your organization, and it's fine to get someone else to assist you. You don't necessarily have to run a security business but some of these functions must be performed and they must be handled by someone, which you can outsource easily.


<img src="/images/d-4.png" height="50%" width="50%">

## Where are we in terms of security maturity?

There's different ways of doing it and it’s obviously a very high level and to be honest the more immature you are the easier this process..

 - **Non-Existence**:  we have a Firewall we have AntiVirus if that's the answer to the question of what are you doing for information security then you're probably going to be in that non-existent. However, that makes life easy because your roadmap can take in whatever direction you want to be with minimal friction from the stakeholders.

- **Immature:** In general, you will have a Security Administration function and you may have some policies, or you might not have any policies at all but people just know what to do. People seem to know what to do quite naturally when it comes to this. You might have some technical controls beyond your firewall or your antivirus in place within the organization, you might do some threat management, we're still a fairly immature organization, there's no real strategy.

- **Doing our best:** In this case, the Security Admin function is pretty good, and you can add/remove users, modify policies, or even develop a little bit of a risk and compliance or security operations tool, these technical controls with some customization. In contrast to the default tools you bought on day one, these have actually had some thought and configuration assigned to them.

- **Getting there:** Everyone is aware of the Security Administration's policies. As part of security operations, you're getting some visibility into the network, you're having some logs and cloudtrail set up, and you're reviewing those logs. Your risk and compliance function is taking place throughout the year, and you're analyzing where you sit for the most significant risks. Getting involved in projects means you know it may not be at the end, maybe you're in the middle, but the objective is to get there as soon as possible.

- **Mature:** You start adding to get established and you've got things documented. Security operations are improved on your visibility. The policies are in place and they're regularly being reviewed. The technical controls are in place.

- **Very Mature Organization:** You're doing everything you were doing before, but now that you have metrics, you can determine whether or not things are working as they should. Your security architecture is documented. You have invested resources in automating some administrative or operational tasks. You're reducing the time it takes you to respond to incidents and noticing them more often. Perhaps you are evaluating the advanced tools deployed within your organization now that the policies are in place. 


*The next post - "part ii" of this series will discuss ways to improve security and the roadmap.*

🙏

References: 

- [McAfee](https://www.mcafee.com/enterprise/en-us/assets/data-sheets/ds-strategic-security-roadmap-plan.pdf)
- [PurpleSec](https://purplesec.us/learn/cyber-security-strategy/)
- [TechTarget](https://www.techtarget.com/searchsecurity/tip/How-to-develop-a-cybersecurity-strategy-Step-by-step-guide)
- [Shearwater](https://www.shearwater.com.au)
- [Tribe of Hackers Security Leaders](https://www.goodreads.com/book/show/49883665-tribe-of-hackers-security-leaders)
- [Cybersecurity Leadership](https://www.goodreads.com/book/show/23201316-cybersecurity-leadership)
- [A Leader's Guide to Cybersecurity](https://www.goodreads.com/book/show/52431662-a-leader-s-guide-to-cybersecurity)