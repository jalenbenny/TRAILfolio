---
layout: page
permalink: /repositories/
title: repositories
description: GitHub activity for lab members. Add each person's real GitHub username in _data/repositories.yml to populate their card.
nav: true
nav_order: 8
---

<div class="mb-3">
  <input type="text" id="repo-search" class="site-search-input" placeholder="Search lab members by name, role, or tag...">
</div>

<style>
  .search-hidden { display: none !important; }
  .site-search-input {
    width: 100%;
    font-size: 0.9rem;
    padding: 0.5rem 0.9rem;
    border-radius: 999px;
    border: 1px solid rgba(127, 127, 127, 0.35);
    background: rgba(127, 127, 127, 0.06);
    color: inherit;
    outline: none;
    box-sizing: border-box;
    transition: border-color 0.15s ease, background 0.15s ease;
  }
  .site-search-input::placeholder {
    color: rgba(127, 127, 127, 0.85);
    font-size: 0.85rem;
  }
  .site-search-input:focus {
    border-color: #4fa3c7;
    background: rgba(127, 127, 127, 0.1);
  }
</style>

{% assign all_tags = site.data.repositories.lab_members | map: "tags" | flatten | uniq | sort %}
{% include tag_filter.liquid container_id="repo-members" tags=all_tags %}

<div class="repositories">
<div class="row row-cols-1 row-cols-md-3">
{% for member in site.data.repositories.lab_members %}
<div class="col mb-4 tag-filter-item" data-filter-group="repo-members" data-tags="{{ member.tags | join: ',' }}">
  <div class="card h-100 p-3">
    <h5>{{ member.name }}</h5>
    <p class="text-muted mb-1">{{ member.role }}</p>
    {% if member.github %}
      {% include repository/repo_user.liquid username=member.github %}
    {% else %}
      <p><em>GitHub username not yet added, see _data/repositories.yml</em></p>
    {% endif %}
  </div>
</div>
{% endfor %}
</div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var input = document.getElementById('repo-search');
  if (!input) return;
  input.addEventListener('input', function () {
    var query = input.value.trim().toLowerCase();
    document.querySelectorAll('[data-filter-group="repo-members"]').forEach(function (item) {
      var text = item.textContent.toLowerCase();
      var matches = text.indexOf(query) !== -1;
      item.classList.toggle('search-hidden', !matches);
    });
  });
});
</script>
