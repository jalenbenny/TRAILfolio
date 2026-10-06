---
layout: page
title: "Structured-to-LLM Soft Token Representation"
description: "Learned projector that maps structured EHR records into soft tokens in a frozen LLM embedding space."
pid: ehr-soft-token-fusion
short_title: "Soft token EHR representation"
importance: 26
area: emerging-ai
category: emerging-ai
status: Active
tags:
  - llm
  - ehr
  - representation-learning
  - multimodal
  - fusion
  - nlp
team: "M. Saban, W. Yoon, T. Miller, S. Tootooni, D. Dligach"
repo: ehr-soft-token-fusion
contact: msaban@luc.edu
related:
  - mimic-multimodal-fusion
related_publications: false
---

{% include project_meta.liquid %}

## Summary

Explores training a projector that encodes a structured patient record as a small set of soft tokens ingestible by an LLM, supervised with next-token loss over serialized records.

## Data availability

MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in the repository, only code and configs.

{% include project_readme.liquid %}

{% include project_related.liquid %}
