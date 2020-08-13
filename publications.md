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
		{% assign sorted = site.publications | sort: 'year' | reverse %}
		{% for post in sorted %}
		  {% include pub_entry.html %}
		{% endfor %}

	</div>
</div>
