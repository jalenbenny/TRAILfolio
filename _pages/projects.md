---
layout: page
title: projects
permalink: /projects/
description: The TRAIL Lab research program, organized into five areas. Each project has its own page and its own repository.
nav: true
nav_order: 4
horizontal: false
---

<style>
  .search-hidden { display: none !important; }
  .area-nav { display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0 0 1.2rem; }
  .area-nav a { font-size: 0.8rem; padding: 0.4rem 0.9rem; border-radius: 999px; border: 1px solid rgba(127,127,127,0.35); text-decoration: none; color: inherit; }
  .area-nav a:hover { border-color: #4fa3c7; background: rgba(79,163,199,0.12); }
  .site-search-input { width: 100%; font-size: 0.9rem; padding: 0.5rem 0.9rem; border-radius: 999px; border: 1px solid rgba(127,127,127,0.35); background: rgba(127,127,127,0.06); color: inherit; outline: none; box-sizing: border-box; }
  .site-search-input::placeholder { color: rgba(127,127,127,0.85); font-size: 0.85rem; }
  .site-search-input:focus { border-color: #4fa3c7; }
  .tag-details { margin: 0.8rem 0 1.5rem; }
  .tag-details summary { cursor: pointer; font-size: 0.85rem; opacity: 0.8; margin-bottom: 0.6rem; }
  .research-area { margin: 2.2rem 0; }
  .research-area h2 { font-size: 1.4rem; margin-bottom: 0.4rem; }
  .area-summary { font-size: 0.92rem; opacity: 0.85; max-width: 60rem; margin-bottom: 1rem; }
  .proj-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1rem; }
  .proj-card { display: flex; flex-direction: column; gap: 0.4rem; padding: 1rem; border-radius: 12px; border: 1px solid rgba(127,127,127,0.3); text-decoration: none; color: inherit; transition: border-color 0.15s ease, transform 0.15s ease; }
  .proj-card:hover { border-color: #4fa3c7; transform: translateY(-2px); }
  .proj-status { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; color: #4fa3c7; }
  .proj-title { font-size: 1rem; margin: 0; }
  .proj-desc { font-size: 0.85rem; margin: 0; opacity: 0.85; }
  .proj-tags { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-top: auto; }
  .proj-tag { font-size: 0.7rem; padding: 0.15rem 0.5rem; border-radius: 999px; background: rgba(127,127,127,0.14); }
  .proj-rel { font-size: 0.75rem; margin: 0.3rem 0 0; opacity: 0.7; }
</style>

<p>The TRAIL Lab research program is organized into five areas. Within each area, the projects below form a pool of related studies, and the "Connects to" line on each card shows which projects build on one another. Every project has its own page and its own GitHub repository.</p>

<nav class="area-nav">
{% for a in site.data.research_areas %}
  <a href="#{{ a.id }}">{{ a.title }}</a>
{% endfor %}
</nav>

<input type="text" id="project-search" class="site-search-input" placeholder="Search projects by title, tag, or team member...">

{% assign all_tags = site.projects | map: "tags" | flatten | uniq | sort %}
<details class="tag-details">
  <summary>Filter by tag</summary>
  {% include tag_filter.liquid container_id="projects-list" tags=all_tags %}
</details>

<div id="projects-list-wrap">
{% for a in site.data.research_areas %}
<section class="research-area" id="{{ a.id }}">
  <h2>{{ a.title }}</h2>
  <p class="area-summary">{{ a.summary }}</p>
  <div class="proj-grid">
  {% assign area_projects = site.projects | where: "area", a.id | sort: "importance" %}
  {% for project in area_projects %}
    {% assign tag_str = project.tags | join: " " %}
    {% capture search_text %}{{ project.title }} {{ project.team }} {{ tag_str }}{% endcapture %}
    <div class="tag-filter-item" data-filter-group="projects-list" data-tags="{{ project.tags | join: ',' }}" data-search="{{ search_text | downcase | escape }}">
      {% include projects.liquid %}
    </div>
  {% endfor %}
  </div>
</section>
{% endfor %}
</div>

<script>
(function () {
  var input = document.getElementById('project-search');
  var wrap = document.getElementById('projects-list-wrap');
  function refreshSections() {
    wrap.querySelectorAll('.research-area').forEach(function (sec) {
      var visible = sec.querySelectorAll('.tag-filter-item:not(.tag-filter-hidden):not(.search-hidden)').length;
      sec.classList.toggle('search-hidden', visible === 0);
    });
  }
  if (input) {
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      wrap.querySelectorAll('.tag-filter-item').forEach(function (item) {
        var text = (item.getAttribute('data-search') || item.textContent).toLowerCase();
        item.classList.toggle('search-hidden', q !== '' && text.indexOf(q) === -1);
      });
      refreshSections();
    });
  }
  var f = document.getElementById('projects-list-filter');
  if (f) f.addEventListener('click', function () { setTimeout(refreshSections, 0); });
})();
</script>
