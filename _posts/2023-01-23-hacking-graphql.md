---
layout: post
title:  "Learning and Breaking GraphQL"
subtitle: ""
date: 2023-01-23 10:00:00

---


---
tldr;

`Apollo's Odyessy GraphQL Assessment had a security vulnerability that allowed anyone to view the correct answer before submitting the final report.` 

---


### Learning

I developed a interest in learning more about GraphQL in the past couple of years, for the simple reason that it is still quite a new technology for some of the application developers, and due to its flexibility to adapt to customer needs, it's a technology that is experiencing a significant growth in popularity.

Even though I have done quite a bit of bug bounty work and pentesting around GraphQL, I have not been well versed in the development using GraphQL. My first step was to browse through their official documentation and tutorials. You can find a number of worthwhile resources on their site, including a blog series covering everything from the basics to advanced concepts like custom scalars and directives.

Later, I was presented with a fantastic book. It was straightforward and gave me a better understanding of GraphQL. I was eager to get my hands dirty and came across the [Apollo Odyssey Learning Platform](https://www.apollographql.com/tutorials/), it offers hands-on GraphQL tutorials.

<center><iframe type="text/html" sandbox="allow-scripts allow-same-origin allow-popups" width="165" height="275" frameborder="0" style="max-width:100%" src="https://read.amazon.com/kp/card?asin=B07K5TF5LP&preview=inline&linkCode=kpe&ref_=cm_sw_r_kb_dp_YD426Q7JD4ZYSBJ50S6J" ></iframe></center>

I completed it in a couple of weeks and the course provided me with everything that I needed to know about how GraphQL works behind-the-scenes as well as how it can be exploited by attackers who want access to your data or want to disrupt your services by sending bad requests through your API endpoint(s).

Apollo Odyessy also provides a certification if you score seventy or above marks in the final assessement. Due to my familiarity with GraphQL, it was a breeze.

<img src="/images/odyessy-2.svg" height="12%" width="12%">

### Breaking

Let's now get to the hacking part. After getting familiar with how GraphQL works at a high level, I decided that it was time for me to start breaking something! So naturally my first instinct was "to look for compaies  that uses GraphQL extensively" and I was looking for a target. However what would be a better target than Apollo's own website? haha.

As I explored and intercepted the traffic on the Exam page using the Burp suite, I noticed that when someone selected any option for the given question, a request was sent immediately. As part of the response to these requests, there is an interesting parameter called "correct" whose value will reveal whether the current answer is correct or not. The fact that anyone can run this request multiple times before submitting the final report makes it possible for the correct option to be iterated simply by iterating it again.

*Request body*

```json
{
  "operationName": "SetOdysseyResponse",
  "variables": {
    "userId": "gh.██████████████████████████████",
    "response": {
      "attemptId": "fa0d9916█████████████████████6",
      "questionId": "mcq-res-calls-1",
      "values": []
    }
  },
  mutation SetOdysseyResponse($response: OdysseyResponseInput!, $userId: ID!) {
  user(id: $userId) {
    response: setOdysseyResponse(response: $response) {
      ...ResponseFragment
      __typename
    }
    __typename
  }
}

fragment ResponseFragment on OdysseyResponse {
  id
  questionId
  correct
  values {
    id
    value
    __typename
  }
  __typename
}
```

*Response*

```json
{
  "data": {
    "user": {
      "response": {
        "id": "22748",
        "questionId": "mcq-res-calls-1",
        "correct": true,
        "values": [],
        "__typename": "OdysseyResponse"
      },
      "__typename": "UserMutation"
    }
  }
}
```

Issues
 - `correct` should not be reflected to mutation response.
 - It is also possible to nest all the options and get the correct answers easily

It is worth mentioning that if these parameters are not restricted, someone with a knowledge of the schema could request the values of them to receive more information.

Using this method, anyone can easily pass this assessment with a score of 100/100 after going through all the questions.

I immediatly reported this to the [Apollo](https://community.apollographql.com/t/where-to-report-a-security-vulnerability-in-odyssey-platform/4472) through twitter and their support forum. They were quite prompt in response and acknowleged it as a valid issue.

While fixing it from their end did take some time, they did a great job.

My next few posts will also explain how to leverage tools in SAST and DAST to continuously check graphQL security in an organisation.


~ avi