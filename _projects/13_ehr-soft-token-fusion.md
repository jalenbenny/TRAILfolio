---
layout: page
title: "Structured-to-LLM Soft Token Representation"
description: "A learned projector that maps structured EHR records into soft tokens in a frozen LLM embedding space. Trains the projector to encode a structured patient record as a small set of soft tokens ingestible by an LLM, supervised with next-token loss over serialized record text."
importance: 13
category: llm
status: Active
date: 2025-01-15
tags:
  - llm
  - ehr
  - representation-learning
  - multimodal
  - fusion
  - nlp
team: "M. Saban, W. Yoon, T. Miller, S. Tootooni, D. Dligach"
github: TootooniLab/ehr-soft-token-fusion
related_publications: false
---

A learned projector that maps structured EHR records into soft tokens in a frozen LLM embedding space. Trains the projector to encode a structured patient record as a small set of soft tokens ingestible by an LLM, supervised with next-token loss over serialized record text.

**Data availability:** MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in the repo, code and configs only.
