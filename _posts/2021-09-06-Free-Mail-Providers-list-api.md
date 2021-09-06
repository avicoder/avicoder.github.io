---
layout: post
title: "Free Email Provider List"
subtitle: "with api"
date: 2021-09-06 00:00:00
---

[![CircleCI](https://circleci.com/gh/avicoder/avicoder.github.io/tree/master.svg?style=svg)](https://circleci.com/gh/avicoder/avicoder.github.io/tree/master)

Using this API endpoint

    https://avicoder.me/api/mailproviders.json

, a user can retrieve a list of free email providers. The information here is not exhaustive and is based on the gist people have provided.

Daily updates are made to it.

<div class="language-plaintext highlighter-rouge">
<div class="highlight"><pre class="highlight">
<code class="hljs javascript">
<div id="myData"></div>
</code></pre></div></div>

 <script>
 var getJSON = function(url, callback) {
     var xhr = new XMLHttpRequest();
     xhr.open('GET', url, true);
     xhr.responseType = 'json';
     xhr.onload = function() {
       var status = xhr.status;
       if (status === 200) {
         callback(null, xhr.response);
       } else {
         callback(status, xhr.response);
       }
     };
     xhr.send();
 };

getJSON('https://avicoder.me/api/mailproviders.json',
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
    var mainContainer = document.getElementById("myData");
    for (var i = 0; i < data.result.length; i++) {
                var div = document.createElement("div");
                div.innerHTML = data['result'][i];
                mainContainer.appendChild(div);
            }
          }
});
 </script>

Thank you
