---
layout: page
title: "Economic Impact of AI Stroke Triage CDS"
description: "Decision model of the cost impact of implementing AI-based prehospital stroke triage."
pid: stroke-cds-cost-model
short_title: "Economic impact of AI triage"
importance: 5
area: prehospital-stroke
category: prehospital-stroke
status: Active
tags:
  - stroke
  - ems
  - health-economics
  - cost-effectiveness
  - decision-modeling
team: "M. Saban, M. Ahmad, U. Dincer, A. Kasaie, T. Markossian, S. Tootooni"
repo: stroke-cds-cost-model
contact: msaban@luc.edu
related:
  - stroke-triage-ml
  - stroke-neds-cost-burden
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Models the downstream cost and outcome consequences of correct versus incorrect prehospital stroke routing under an AI decision support tool. Parameters are drawn from the literature.

</div>

<div class="proj-block" markdown="1">

## Data availability

Model inputs are derived from published literature and licensed datasets. Tables and code are in the repository.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
