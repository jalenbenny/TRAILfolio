---
layout: page
title: "MEDIQA-SYNUR 2026 Shared Task System"
description: "Hybrid retrieval and LLM verification system for open-source schema-guided clinical information extraction of synthetic nursing transcripts."
pid: mediqa-synur-2026
short_title: "MEDIQA-SYNUR 2026"
importance: 17
area: clinical-nlp
category: clinical-nlp
status: Completed
tags:
  - nlp
  - llm
  - information-extraction
  - retrieval
  - nursing
  - shared-task
team: "M. Saban, A. Yaghoubi, B. Eslami, S. Tootooni, D. Dligach"
repo: mediqa-synur-2026
contact: msaban@luc.edu
related:
  - hybrid-ontology-concept-extraction
related_publications: false
---

{% include project_meta.liquid %}

{% assign has_readme = site.data.readmes[page.pid] %}
{% unless has_readme %}

<div class="proj-block" markdown="1">

## Summary

The Lakefront AI Ramblers entry to the MEDIQA-SYNUR 2026 shared task, combining lexical and dense retrieval with an LLM verification stage on an open-source model.

</div>

<div class="proj-block" markdown="1">

## Data availability

Task data are distributed by the shared task organizers and not redistributed here. Code and config only.

</div>

{% endunless %}

{% include project_readme.liquid %}

{% include project_related.liquid %}
