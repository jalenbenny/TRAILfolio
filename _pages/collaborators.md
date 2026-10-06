---
layout: page
title: collaborators
permalink: /collaborators/
description: Clinical, academic, and community partners who work with the TRAIL Lab.
nav: true
nav_order: 5
---

<style>
  .collab-wrap { overflow-x: auto; }
  .collab-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
  .collab-table th { text-align: left; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.7; padding: 0.6rem 0.8rem; border-bottom: 2px solid rgba(127,127,127,0.35); }
  .collab-table td { vertical-align: top; padding: 0.8rem; border-bottom: 1px solid rgba(127,127,127,0.2); }
  .collab-table ul { margin: 0; padding-left: 1.1rem; }
  .collab-ph { font-size: 0.7rem; padding: 0.1rem 0.5rem; border-radius: 999px; border: 1px dashed rgba(127,127,127,0.6); margin-left: 0.4rem; }
</style>

<p>The TRAIL Lab works with clinicians, health systems, and researchers at other institutions. The table lists each collaborator, their rank and institution, the projects we share, and what the lab contributes.</p>

<div class="collab-wrap">
<table class="collab-table">
  <thead>
    <tr><th>Collaborator</th><th>Rank</th><th>Institution</th><th>Projects</th><th>Our involvement</th></tr>
  </thead>
  <tbody>
  {% for c in site.data.collaborators %}
    <tr>
      <td>
        {% if c.url and c.url != "" %}<a href="{{ c.url }}">{{ c.name }}</a>{% else %}{{ c.name }}{% endif %}
        {% if c.placeholder %}<span class="collab-ph">placeholder</span>{% endif %}
      </td>
      <td>{{ c.rank }}</td>
      <td>{{ c.institution }}</td>
      <td><ul>{% for p in c.projects %}<li>{{ p }}</li>{% endfor %}</ul></td>
      <td>{{ c.involvement }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>
</div>

<p>Interested in collaborating? Contact Dr. Tootooni at <a href="mailto:mtootooni@luc.edu">mtootooni@luc.edu</a>.</p>
