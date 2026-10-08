---
layout: page
title: "Multimodal EHR Fusion for Outcome Prediction"
description: "Early, intermediate, and late fusion of structured EHR data with clinical notes for 30-day mortality prediction."
pid: mimic-multimodal-fusion
short_title: "Multimodal EHR fusion"
importance: 25
area: emerging-ai
category: emerging-ai
status: Active
tags:
  - multimodal
  - fusion
  - ehr
  - nlp
  - mimic-iv
team: "M. Saban, W. Yoon, T. Miller, S. Tootooni, D. Dligach"
repo: ehr-multimodal-fusion
contact: msaban@luc.edu
related:
  - ehr-soft-token-fusion
related_publications: false
---

{% include project_meta.liquid %}

## Summary

Benchmarks unimodal baselines against three fusion strategies on MIMIC-IV, combining tabular models over structured records with transformer encoders over discharge summaries.

## Data availability

MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in the repository, only code and configs.

{% include project_readme.liquid %}

{% include project_related.liquid %}
