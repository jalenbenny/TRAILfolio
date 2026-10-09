---
layout: page
title: "EMS Workflow Determinant Assessment (CFIR)"
description: "CFIR guided pre-implementation assessment of EMS workflow determinants for an AI stroke triage tool."
pid: stroke-ems-workflow-cfir
short_title: "EMS workflow assessment (CFIR)"
importance: 3
area: prehospital-stroke
category: prehospital-stroke
status: Active
tags:
  - stroke
  - ems
  - implementation
  - qualitative
  - cfir
team: "M. Saban, A. Kasaie, P. Olalekan, E. Morrato, S. Tootooni"
repo: stroke-ems-workflow-cfir
contact: msaban@luc.edu
related:
  - stroke-triage-ml
  - stroke-codesign-paramedics
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

25 semi-structured interviews with 20 EMS participants in Illinois Chicagoland EMS regions, coded against the Consolidated Framework for Implementation Research.

</div>

<div class="proj-block" markdown="1">

## Data availability

Transcripts are not shared. The repository holds the interview guide, codebook, and analysis documentation.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
