---
layout: page
title: "Stroke Center Access by Drive Time"
description: "Using an OSRM server to calculate drive times from block groups to hospitals."
pid: stroke-center-drivetime
short_title: "Stroke center access by drive time"
importance: 23
area: health-systems-equity
category: health-systems-equity
status: Active
tags:
  - stroke
  - geospatial
  - drive-time
  - access
team: "M. Ahmad, M. Saban, S. Tootooni"
repo: stroke-center-drivetime
contact: mahmad12@luc.edu
related:
  - stroke-neds-cost-burden
related_publications: false
---

{% include project_meta.liquid %}

## Summary

Uses OSRM to calculate drive time from block groups to hospitals of various stroke center certifications, replacing a Euclidean distance approach.

## Data availability

Public data. The repository includes Illinois hospitals and stroke designations, and all code used in the analysis.

{% include project_readme.liquid %}

{% include project_related.liquid %}
