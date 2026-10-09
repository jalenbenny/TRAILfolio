---
layout: page
title: "Stroke Narrative Information Extraction"
description: "NLP over EMS ambulance narratives to identify what clinical information paramedics documented in the field."
pid: stroke-ems-narrative-nlp
short_title: "Stroke narrative extraction"
importance: 2
area: prehospital-stroke
category: prehospital-stroke
status: Active
tags:
  - stroke
  - nlp
  - ems
  - prehospital
team: "M. Saban, S. Tootooni"
repo: stroke-ems-narrative-nlp
contact: msaban@luc.edu
related:
  - stroke-triage-ml
  - hybrid-ontology-concept-extraction
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Applies NLP to free-text EMS run narratives to detect which assessment findings were actually collected and recorded on scene or in the ambulance. The extracted narrative content is intended to supplement the structured EMS fields used by the triage models, giving a text and tabular view of the same encounter.

</div>

<div class="proj-block" markdown="1">

## Data availability

Uses the same restricted EMS dataset. Narratives contain PHI and are never committed. The repository holds code, annotation, and aggregate results only.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
