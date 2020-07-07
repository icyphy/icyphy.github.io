---
title: Publications
layout: page
description: 'Publications from iCyPhy.'
image: assets/images/pic07.jpg
nav-menu: true
order: 2
show_at: home
---

<div class="main">
	<div class="inner">

		<header class="major">
			<h2>Featured Publications</h2>
		</header>
		{% assign sorted = site.publications | sort: 'date' | reverse %}
		{% for post in sorted %}
		  {% include pub_entry.html %}
		{% endfor %}

	</div>
</div>