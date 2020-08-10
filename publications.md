---
title: Publications
layout: landing
description: 'Publications from iCyPhy'
image: assets/images/publications.jpg
nav-menu: true
order: 3
---

<div class="main">
	<div class="inner">

		<header class="major">
			<h2>Featured Publications</h2>
		</header>

{% assign rows = site.people.size | divided_by: 4.0 | ceil %}
{% for i in (1..rows) %}
  {% assign offset = forloop.index0 | times: 4 %}
  <div class= "row">
    {% for post in site.posts limit:4 offset:offset %}
      {% include person_entry.html %}
    {% endfor %}
  </div>
{% endfor %}


	</div>
</div>
