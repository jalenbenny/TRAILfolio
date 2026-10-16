---
layout: page
title: products
permalink: /products/
description: Software, models, datasets, and tools built by the TRAIL Lab.
nav: true
nav_order: 4.5
---

<style>
  .prod-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(18rem, 1fr)); gap: 1.1rem; margin: 1.2rem 0 1.6rem; }
  .prod-card { border: 1px solid rgba(127,127,127,0.3); border-radius: 12px; padding: 1.1rem 1.2rem; display: flex; flex-direction: column; gap: 0.55rem; }
  .prod-top { display: flex; align-items: center; justify-content: space-between; gap: 0.5rem; flex-wrap: wrap; }
  .prod-type { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #4fa3c7; }
  .prod-status { font-size: 0.72rem; padding: 0.1rem 0.55rem; border-radius: 999px; border: 1px solid rgba(127,127,127,0.5); }
  .prod-name { font-size: 1.1rem; font-weight: 700; margin: 0; }
  .prod-desc { font-size: 0.9rem; margin: 0; opacity: 0.9; }
  .prod-projects { font-size: 0.8rem; opacity: 0.75; margin: 0; }
  .prod-ph { font-size: 0.7rem; padding: 0.1rem 0.5rem; border-radius: 999px; border: 1px dashed rgba(127,127,127,0.6); margin-left: 0.4rem; font-weight: 400; }
  .prod-link { font-size: 0.85rem; margin-top: auto; }
</style>

<p>The TRAIL Lab turns its research into tools others can use. This page lists the software, trained models, datasets, and ontologies the lab has built, along with the projects they came from.</p>

<div class="prod-grid">
{% for p in site.data.products %}
  <div class="prod-card">
    <div class="prod-top">
      <span class="prod-type">{{ p.type }}</span>
      {% if p.status and p.status != "" %}<span class="prod-status">{{ p.status }}</span>{% endif %}
    </div>
    <h3 class="prod-name">
      {% if p.url and p.url != "" %}<a href="{{ p.url }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
      {% if p.placeholder %}<span class="prod-ph">placeholder</span>{% endif %}
    </h3>
    <p class="prod-desc">{{ p.description }}</p>
    {% if p.projects and p.projects.size > 0 %}<p class="prod-projects">From: {{ p.projects | join: ", " }}</p>{% endif %}
    {% if p.url and p.url != "" %}<a class="prod-link" href="{{ p.url }}">View product</a>{% endif %}
  </div>
{% endfor %}
</div>

<p>Questions about using a product? Contact Dr. Tootooni at <a href="mailto:mtootooni@luc.edu">mtootooni@luc.edu</a>.</p>
