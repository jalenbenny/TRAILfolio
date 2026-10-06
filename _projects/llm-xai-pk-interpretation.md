---
layout: page
title: "LLM-Mediated Explainable AI for Clinician-Facing Interpretation of Pharmacokinetic Model Predictions"
description: "Framework that translates machine learning model explanations, such as SHAP, into plain-language narratives for clinicians using an LLM."
pid: llm-xai-pk-interpretation
short_title: "LLM explanations for PK models"
importance: 9
area: critical-care-dosing
category: critical-care-dosing
status: Active
tags:
  - llm
  - explainable-ai
  - interpretability
  - shap
  - clinician-facing
  - pharmacokinetics
team: "D. A. Patel, S. Tootooni"
repo: llm-mediated-xai-pk-interpretation
contact: dpatel96@luc.edu
related:
  - ml-prediction-vanco-auc24
related_publications: false
---

{% include project_meta.liquid %}

## Summary

Wraps standard interpretability outputs, such as SHAP feature attributions and counterfactuals, with an LLM layer that converts them into clear, clinician-facing plain-language explanations.

## Data availability

Uses the same restricted clinical datasets as the underlying prediction models. The repository holds pipeline code and prompt templates.

{% include project_readme.liquid %}

{% include project_related.liquid %}
