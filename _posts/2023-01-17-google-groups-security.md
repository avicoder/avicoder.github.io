---
layout: post
title:  "Security of Google Groups"
subtitle: ""
date: 2023-01-17 10:00:00

---
Here we go again!

I'm back with another series of discussion topics. This time it's Google Workspace.

Alphabet has a variety of applications for organisations that help you work with your teams and clients, but one of the most powerful is Google Workspace.

![Goole Workspace](https://raw.githubusercontent.com/avicoder/avicoder.github.io/master/images/google-workspace.png)

There are a ton of applications that allow you to access your emails, calendars and contacts from anywhere with an internet connection. It also makes it easy for you to share files with other members of your team or company.

But there's a problem. Let me explain to you why: when you navigate to "https://groups.google.com/a/{org_domain}/g/{group_name}" and able to view all the conversations that are happening inside the organisation. That's because of a common misconfiguration while setting the sharing options. 

![Goole Workspace](https://raw.githubusercontent.com/avicoder/avicoder.github.io/master/images/google-sharing.png)

Many companies mistakenly think that "public on the internet" means that their communications are available only within the organization; they don't realize that anyone can see them if they know where to look, which is not a problem with a few lines of automation. 

Based on the HTTP Status Code if:

 - The group will return `403` if it exists and is private.
 - The group will return `200` if it exists and is public.
 - `302` will be returned if the group does not exist.

I ran a one-liner on the top 1 million sites with common DL/Group names such as:
 - support
 - help
 - people
 - security etc.
and found 100s of instances.

Digging deeper into the conversation reveals more obscure and difficult-to-find Google groups with internal information. 

```bash
cat 1m.txt | while read line; do  result=`curl -s -o /dev/null -w "%{http_code}\n" https://groups.google.com/a/$line/g/support`; if [ $result -eq "200" ]; then echo "\n$line\n## HIT ###";fi; done
```

If your conversations are publicly accessible, all someone needs to do is guess at the URL for your group within your organization and then they have access to all of your confidential information! 

So what do you do? To protect yourself and your company, make sure you've selected "Private" under "Accessing groups from outside the organization."

Until next time ...

Avi
👋
