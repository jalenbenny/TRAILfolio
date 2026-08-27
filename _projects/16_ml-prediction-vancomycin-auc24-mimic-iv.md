---
layout: page
title: "Machine Learning Prediction of Vancomycin AUC24 Using Vanco24-Derived Labels in MIMIC-IV"
description: "XGBoost model predicting future vancomycin AUC24 from clinical and dosing variables, trained on Vanco24-derived AUC labels across a large MIMIC-IV cohort."
importance: 16
category: vancomycin
status: Active
tags:
  - vancomycin
  - machine-learning
  - xgboost
  - mimic-iv
  - auc
  - pharmacokinetics
team: "Dhruvin A. Patel, Samie Tootooni"
related_publications: false
---

Applies the Vanco24 Bayesian engine to a large MIMIC-IV cohort to generate individualized AUC24 labels, then trains XGBoost and comparison models to predict future AUC24.

**Data availability:** MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in repo, code and configs only.

**Contact:** [dpatel96@luc.edu](mailto:dpatel96@luc.edu)
