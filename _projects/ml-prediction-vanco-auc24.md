---
layout: page
title: "Machine Learning Prediction of Vancomycin AUC24 Using Vanco24-Derived Labels in MIMIC-IV"
description: "XGBoost model predicting future vancomycin AUC24 from clinical and dosing variables, trained on Vanco24-derived AUC labels across a large MIMIC-IV cohort."
pid: ml-prediction-vanco-auc24
short_title: "ML prediction of vancomycin AUC24"
importance: 8
area: critical-care-dosing
category: critical-care-dosing
status: Active
tags:
  - vancomycin
  - machine-learning
  - xgboost
  - mimic-iv
  - auc
  - pharmacokinetics
team: "D. A. Patel, S. Tootooni"
repo: ml-prediction-vancomycin-auc24-mimic-iv
contact: dpatel96@luc.edu
related:
  - vanco24-bayesian-auc24
  - llm-xai-pk-interpretation
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Applies the Vanco24 Bayesian engine to a large MIMIC-IV cohort to generate individualized AUC24 labels, then trains XGBoost and comparison models to predict future AUC.

</div>

<div class="proj-block" markdown="1">

## Data availability

MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in the repository, only code and configs.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
