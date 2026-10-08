---
layout: page
title: "A Performance-Based Voting Framework for Assertion Detection in Clinical Notes"
description: "A performance-based voting framework that combines multiple pre-trained NLP models to accurately detect and classify clinical assertions."
pid: assertion-detection-voting
short_title: "Assertion detection voting framework"
importance: 14
area: clinical-nlp
category: clinical-nlp
status: Completed
tags:
  - clinical-nlp
  - assertion-detection
  - biobert
  - named-entity-recognition
  - ehr
  - ensemble-voting
team: "B. Eslami, D. Dligach, B. Strickland, N. Azarvash, M. S. Tootooni"
contact: beslami@luc.edu
related:
  - hybrid-ontology-concept-extraction
related_publications: false
---

{% include project_meta.liquid %}

<div class="proj-block" markdown="1">

## Summary

Combines models including BioBERT and BiLSTM-CNN-Char to detect and classify clinical assertions, such as polarity and subject, in clinical text.

</div>

<div class="proj-block" markdown="1">

## Data availability

MIMIC-III dataset.

</div>

{% include project_readme.liquid %}

{% include project_related.liquid %}
