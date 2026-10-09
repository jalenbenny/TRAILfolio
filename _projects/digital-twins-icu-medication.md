---
layout: page
title: "Toward Digital Twins in the Intensive Care Unit: A Medication Management Case Study"
description: "Fine-tuning LLaMA-3 with LoRA on specialty-specific ICU physician notes to produce digital twin medication recommendations."
pid: digital-twins-icu-medication
short_title: "Digital twins for ICU medication management"
importance: 10
area: critical-care-dosing
category: critical-care-dosing
status: Completed
tags:
  - digital-twins
  - large-language-models
  - intensive-care-unit
team: "B. Eslami, M. Afshar, S. Tootooni, T. Miller, M. Churpek, Y. Gao, D. Dligach"
contact: beslami@luc.edu
related:
  - ai-medication-management-review
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Shows that fine-tuning LLaMA-3 with LoRA on specialty-specific ICU physician notes from the medical ICU produces more accurate digital twin treatment recommendations than models trained on other specialties.

</div>

<div class="proj-block" markdown="1">

## Data availability

MIMIC-III dataset.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
