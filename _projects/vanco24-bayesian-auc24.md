---
layout: page
title: "A Bayesian-Driven Two-Compartment Model Algorithm for Vancomycin AUC24 Calculation"
description: "Bayesian two-compartment pharmacokinetic engine (Vanco24) for individualized vancomycin AUC24 estimation from EHR data."
pid: vanco24-bayesian-auc24
short_title: "Vanco24 Bayesian AUC24"
importance: 7
area: critical-care-dosing
category: critical-care-dosing
status: Active
tags:
  - vancomycin
  - pharmacokinetics
  - bayesian
  - two-compartment
  - auc
  - precision-dosing
team: "D. A. Patel, N. Azarvash, E. F. Barreto, K. B. Kashani, S. Tootooni"
repo: vanco24-bayesian-two-compartment-auc24
contact: dpatel96@luc.edu
related:
  - ml-prediction-vanco-auc24
  - ai-medication-management-review
related_publications: false
---

{% include project_meta.liquid %}

## Summary

Implements an a posteriori Bayesian estimation framework on the log scale, using published population priors, to calculate individualized two-compartment vancomycin AUC24.

## Data availability

Validation cohorts include PHI-restricted clinical data that are not shared. The repository holds the engine code and documentation.

{% include project_readme.liquid %}

{% include project_related.liquid %}
