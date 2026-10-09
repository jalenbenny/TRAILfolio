---
layout: page
title: "EMS Stroke Triage Models"
description: "Supervised models on routinely collected structured EMS encounter data that flag stroke and severe stroke at first patient contact."
pid: stroke-triage-ml
short_title: "EMS stroke triage models"
importance: 1
area: prehospital-stroke
category: prehospital-stroke
status: Completed
tags:
  - stroke
  - ems
  - prehospital
  - machine-learning
  - triage
team: "M. Saban, G. Hiura, P. de la Pena, D. Heiferman, O. Akbilgic, M. Cichon, S. Tootooni"
repo: stroke-triage-ml
contact: msaban@luc.edu
related:
  - stroke-ems-narrative-nlp
  - stroke-ems-workflow-cfir
  - stroke-codesign-paramedics
  - stroke-cds-cost-model
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Machine learning models trained on routinely collected structured prehospital EMS records to predict stroke and severe stroke before hospital arrival.

</div>

<div class="proj-block" markdown="1">

## Data availability

Uses an EMS dataset with PHI. Code and config only.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
