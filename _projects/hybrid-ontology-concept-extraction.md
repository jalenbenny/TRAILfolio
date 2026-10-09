---
layout: page
title: "A Hybrid Language Framework for Ontology-Based Clinical Concept Extraction"
description: "A hybrid ontology-based framework combining SparkNLP, SentenceBERT embeddings, zero-shot LLMs, and UMLS/SNOMED CT normalization for clinical concept extraction."
pid: hybrid-ontology-concept-extraction
short_title: "Ontology-based concept extraction"
importance: 13
area: clinical-nlp
category: clinical-nlp
status: Active
tags:
  - clinical-concept-extraction
  - large-language-models
  - umls-normalization
  - snomed-ct
  - named-entity-recognition
team: "B. Eslami, D. Dligach, N. Azarvash, P. de la Pena, B. Strickland, S. Tootooni"
repo: concept-extraction
contact: beslami@luc.edu
related:
  - assertion-detection-voting
  - ccmapper-chief-complaints
  - mediqa-synur-2026
  - caroli-ontology-llm-validation
  - stroke-ems-narrative-nlp
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

Combines SparkNLP, SentenceBERT embeddings, zero-shot LLMs (LLaMA3-8B and Mistral-7B), and UMLS/SNOMED CT normalization for clinical concept extraction.

</div>

<div class="proj-block" markdown="1">

## Data availability

MIMIC-III dataset.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
