---
layout: post
title:  "Host a bug bounty program under $500!"
subtitle: ""
date: 2023-09-26 10:00:00

---


---

## Backstory


Security for our customers is our top priority.

As a startup, we must continually seek ways to be resourceful by investing wisely in our business while safeguarding the information of our users. By being resourceful, we can reinvest possible savings into other initiatives that would improve the experience of our users and fuel the growth of the business.

It is clear that bug bounties can be a valuable source of information about potential security issues in our system and provide us with the opportunity to close the gaps that might leave our users vulnerable to attack.

In 2018, we launched a bug bounty program. we've done our research, figured out what we want to offer, and gotten all of our ducks in a row. But now comes the hard part: actually running the program!

Previously, we received reports from users about possible problems with accounts or other parts of the site through a dedicated **email** address. We faced the following challenges with this approach:

1.  Keeping track of the reports;
2.  There are major parts of the report missing, such as the class, CVSS, PoC, etc.
3.  Trigger mails on changes in the state of the report such as triage, ask payment details etc.

## Struggle ##

We looked for some alternatives and there are some really good products out there to host bug bounty program. The main issue we found is that most of the platforms out there charge exuberant entry fees just to get onboarded ~$50k.

We also checked few open source solutions but it didn't help our purpose, to keep it simple but effective, **custom workflows** was a major requirement that we were looking for.

Many of the existing integration solutions out there are missing the flexibility to customise the forms look and feel,  handling the workflow a difficult process. we'd checked integration solutions such as Zapier with Google Forms, custom Slack notifications with Jira Service tickets etc...

We decided to go with JotForm for a few reasons:

 - First, the forms can be customised. This means that you can create forms that match the aesthetic of your site and brand, which is extremely important for creating a seamless experience.

 - Second, JotForm integrates with most of the automation and alert solutions out in market today. This makes it easy to send alerts to users when they submit reports.

 - Thirdly, JotForm doesn't cost too much—**$500 per year** for their bronze plan and they also have free plan i.e. is pretty reasonable considering all of the features you get access to, including branding, custom workflows, mail customisation with templates and payment integration via PayPal.

 - Lastly, JotForm has a dashboard where you can see trends and the analytics about received issue, labelling, and assigning the reports to the security analyst.

## Setup ##

We use GitHub Pages to host a static page that includes details such as the

-   Description
-   Scope
-   Eligibility
-   FAQs
-   Hall of Fame
-   Rewards
-   Criteria for Acceptance
-   Form for users to report bugs to us.

You can find it at: [https://security.glints.com](https://security.glints.com/) or feel free to look at code [here](https://github.com/glints-dev/bug-bounty/tree/gh-pages):

Github pages is straightforward to setup. The next step is to configure JotForm, head over to [https://www.jotform.com/](https://www.jotform.com/) to create an account and enable two-factor authentication.

You can design and add the form fields as per your requirements. We like the Bugcrowd report structure and use it in report form. You can clone or import it in your account, this template is public and available at [https://www.jotform.com/form-templates/ur/bug-bounty-submission](https://www.jotform.com/form-templates/ur/bug-bounty-submission), don't forget to edit the options for Assets and Platform in your newly created form to match with your defined bug bounty scope. Once the form is ready, head over to the settings tab for further configuration for mail and workflow.

> Next, Under Form Settings tab, Set form status to **Enable**. After reports are sent, we need to send two emails through _autoresponders_. In one mail we acknowledge that we have received the report by sending an email to the reporter's address(reporter@xyz.com) and in another mail we send a message containing all the details of the report to our email(security@org.com).

![](https://tech.glints.com/content/images/2023/09/image-2.png)

> Go to Emails tab and click on Add Email. Let's configure the acknowledgment mail by creating an **Autoresponder Email**. You will need to make changes such as Subject, Content, Sender Name, Reply-to Address, Recipient Address.

![](https://tech.glints.com/content/images/2023/09/image-1.png)

![](https://tech.glints.com/content/images/2023/09/image-3.png)

> Similarly create another email **Notification Email** for sending the report to security team, also don't miss to make changes as per your requirement.

![](https://tech.glints.com/content/images/2023/09/image-4.png)

> It is also recommended to set a Thank You page once the form is submitted.

![](https://tech.glints.com/content/images/2023/09/image-5.png)

Let's move to the workflow section, which is the gist of this post. This will allow us to manage bug bounty reports in a similar way to how HackerOne and Bugcrowd allows.

As of 2023, Jotform does not have a workflow export feature. However, you may create your own workflow using the tools on the jotform site. The process is fairly straightforward and involves dragging and dropping elements into place until you achieve the desired result. The heavy lifting has been done for you; all you need to do is follow along with this guide and you should be good to go!

> To create the workflow and attach it with out submission form, go to [https://www.jotform.com/myapprovals](https://www.jotform.com/myapprovals) and click on **Create Approval**

for example check the one shown below, customise it as your current requirement.

Also don't forget to make the changes in the template for each action along with the **Recipient Email**, let's say if the report is _Not Applicable or Out of Scope_, the email template would look like this:

    Hi {firstName}
     
    Thank you for participating in our <company name> Bug Bounty Program.
     
    We have reviewed your bug report and would like to inform you that this bug is out of scope of our bug bounty program.
     
    We request you to kindly refer to our bug bounty page at Scope for updated information on scope and details of our bug bounty program.
     
    If you are able to abuse this functionality in order to gain access to sensitive data, or impact the system's integrity, please reply with some detailed reproduction steps and we will be happy to reconsider your report.
     
    We appreciate your help in keeping Glints and our customers safe and secure.
     
    Regards,
    <company name> Security Team

on the similar lines for other action, such as:  
\- Request to validate fix  
\- Triage  
\- Request Payment details etc.  
  
Create the email template accordingly in the approval workflow.

Once the form and approval flow is ready, attach it with the form that you've cloned earlier.

![](https://tech.glints.com/content/images/2023/09/image-7.png)

When bug bounty hunter sends a report using this form, all the details will be displayed in the dashboard called **Inbox**. You can assign the form to individual members of your team and also label it. Filtering and mass operation on issues is also possible.

![](https://tech.glints.com/content/images/2023/09/download--2-.png)

Thanks for reading this post! We hope you found it helpful. If you have any comments or questions, please let me know in the comments below. Until next time…

