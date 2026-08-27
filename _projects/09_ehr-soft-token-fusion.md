---
layout: page
title: "Structured-to-LLM Soft Token Representation"
description: "Learned projector that maps structured EHR records into soft tokens in a frozen LLM embedding space."
importance: 9
category: llm
status: Active
tags:
  - llm
  - ehr
  - representation-learning
  - multimodal
  - fusion
  - nlp
team: "M. Saban, W. Yoon, T. Miller, S. Tootooni, D. Dligach"
related_publications: false
---

Explores training of a projector that encodes a structured patient record as a small set of soft tokens ingestible by an LLM, supervised with next-token loss over serialized records.

**Data availability:** MIMIC-IV requires PhysioNet credentials and a data use agreement. No data in repo, just code/configs.

**Contact:** [msaban@luc.edu](mailto:msaban@luc.edu)
