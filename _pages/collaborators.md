---
layout: page
title: collaborators
permalink: /collaborators/
description: Academic, healthcare, public health, and industry partners of the TRAIL Lab.
nav: true
nav_order: 5
---

<style>
  .collab-group { font-size: 1.15rem; font-weight: 700; margin: 2rem 0 0.4rem; padding-bottom: 0.4rem; border-bottom: 2px solid #4fa3c7; }
  .collab-row { display: grid; grid-template-columns: minmax(11rem, 16rem) 1fr; gap: 0.4rem 1.5rem; padding: 0.85rem 0; border-bottom: 1px solid rgba(127,127,127,0.2); }
  .collab-name { font-weight: 600; }
  .collab-desc { opacity: 0.9; }
  @media (max-width: 640px) { .collab-row { grid-template-columns: 1fr; } }
</style>

<p>Our research involves collaborations with academic institutions, healthcare systems, government agencies, and industry partners in the United States and internationally. These collaborations bring together expertise in artificial intelligence, data science, clinical research, and healthcare delivery, with an emphasis on interdisciplinary research and the practical application of analytical methods.</p>

{% for g in site.data.collaborators %}
<h2 class="collab-group">{{ g.title }}</h2>
{% for c in g.items %}
<div class="collab-row">
  <div class="collab-name">{% if c.url and c.url != "" %}<a href="{{ c.url }}">{{ c.name }}</a>{% else %}{{ c.name }}{% endif %}</div>
  <div class="collab-desc">{{ c.description }}</div>
</div>
{% endfor %}
{% endfor %}

<p style="margin-top: 1.6rem;">Interested in collaborating? Contact Dr. Tootooni at <a href="mailto:mtootooni@luc.edu">mtootooni@luc.edu</a>.</p>
