---
layout: page
title: projects
permalink: /projects/
description: Active and past research projects. Filter by tag or browse by category.
nav: true
nav_order: 4
display_categories: [stroke, dosing, nlp, llm, multimodal, ai-evaluation, nephrology, aki, parkinsons, hypertension, vancomycin, critical-care]
horizontal: false
---

<!-- pages/projects.md -->

{% assign all_tags = site.projects | map: "tags" | flatten | uniq | sort %}
{% include tag_filter.liquid container_id="projects-list" tags=all_tags %}

<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}
<div class="row row-cols-1 row-cols-md-3">
{% for project in sorted_projects %}
<div class="col mb-4 tag-filter-item" data-filter-group="projects-list" data-tags="{{ project.tags | join: ',' }}">
  {% include projects.liquid %}
</div>
{% endfor %}
</div>
</div>
