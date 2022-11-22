---
layout: page
title: Careers
description: Join us!
permalink: /careers/
---

The Open Free Energy fund is currently searching for software scientists
to join our fully remote team.
Ideal candidates will be expected to have a foundation in molecular simulation
and experience developing associated software.
One or more of the following would also be beneficial:
- familiarity with alchemical free energy calculations
- knowledge of cheminformatics algorithms
- experience with Python and software engineering best practices
- track record of contributing to open source projects
- history of collaborating between different projects


For more details and how to apply, please visit the [OMSF careers page](https://omsf.io/about/careers/).

<ul class="jobs">
  {% for job in site.jobs %}
    {% assign status = job.status | downcase %}
    {% if status == "open" %}
      <li><a href="{{ job.url }}">{{ job.jobid }} - {{ job.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>

