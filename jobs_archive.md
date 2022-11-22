---
layout: page
title: Job posting archive
permalink: jobs/
---


<ul class="jobs">
  {% for job in site.jobs %}
    <li><a href="{{ job.url }}">{{ job.jobid }} - {{ job.title }}</a></li>
  {% endfor %}
</ul>

