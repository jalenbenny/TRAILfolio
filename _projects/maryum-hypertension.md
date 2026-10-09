---
layout: page
title: "Clinical Note Topics and Therapeutic Inertia in Hypertension"
description: "Using statistical methods to identify associations between clinical note topics and therapeutic inertia."
pid: maryum-hypertension
short_title: "Note topics and therapeutic inertia"
importance: 22
area: health-systems-equity
category: health-systems-equity
status: Active
tags:
  - therapeutic-inertia
  - clinical-notes
  - topic-selection
  - hypertension
team: "M. Ahmad, B. Eslami, S. Tootooni"
repo: therapeutic-inertia-NLP
contact: mahmad12@luc.edu
related:
  - llm-topic-modeling-clinical
  - adi-hypertension-therapeutic-inertia
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Uses statistical methods to identify associations between clinical note topics and therapeutic inertia in hypertension care.

</div>

<div class="proj-block" markdown="1">

## Data availability

Therapeutic Inertia dataset.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
