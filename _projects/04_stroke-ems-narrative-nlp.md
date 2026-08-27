---
layout: page
title: "Stroke Narrative Information Extraction"
description: "Applies NLP to free-text EMS run narratives to detect which assessment findings were actually collected and recorded on scene or in the ambulance. The extracted narrative content supplements the structured EMS fields used by the triage models, giving a text-and-tabular view of the same encounter."
importance: 4
category: stroke
status: Active
date: 2025-06-01
tags:
  - stroke
  - nlp
  - ems
  - prehospital
team: "M. Saban, S. Tootooni"
github: TootooniLab/stroke-ems-narrative-nlp
related_publications: false
---

Applies NLP to free-text EMS run narratives to detect which assessment findings were actually collected and recorded on scene or in the ambulance. The extracted narrative content supplements the structured EMS fields used by the triage models, giving a text-and-tabular view of the same encounter.

**Data availability:** Uses the same restricted EMS dataset as the EMS Stroke Triage Models project. Narratives contain PHI and are never committed. Repo holds code, annotation, and aggregate results only.
