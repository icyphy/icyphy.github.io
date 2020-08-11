---
layout: page
title: People
nav-menu: true
description: iCyPhy Center Personnel
order: 1
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>People</h1>
		</header>
        <!-- PIs -->
        <h2 id="content">Principal Investigators</h2>
        {% assign group = site.people | where_exp: "item", "item.role == 'pi'" | sort:"last_name"%}
        {% assign rows = group.size | divided_by: 4.0 | ceil %}
        {% for i in (1..rows) %}
        {% assign offset = forloop.index0 | times: 4 %}
        <div class= "row">
            {% for post in group limit:4 offset:offset %}
            {% include person_entry.html %}
            {% endfor %}
        </div>
        {% endfor %}
        <hr class="major" />
        <!-- VIFs -->
        <h2 id="content">Industrial Fellows</h2>
        {% assign group = site.people | where_exp: "item", "item.role == 'vif'" | sort:"last_name"%}
        {% assign rows = group.size | divided_by: 4.0 | ceil %}
        {% for i in (1..rows) %}
        {% assign offset = forloop.index0 | times: 4 %}
        <div class= "row">
            {% for post in group limit:4 offset:offset %}
            {% include person_entry.html %}
            {% endfor %}
        </div>
        {% endfor %}
        <hr class="major" />
        <!-- Postdocs -->
        <h2 id="content">Postdoctoral Researchers</h2>
        {% assign group = site.people | where_exp: "item", "item.role == 'postdoc'" | sort:"last_name"%}
        {% assign rows = group.size | divided_by: 4.0 | ceil %}
        {% for i in (1..rows) %}
        {% assign offset = forloop.index0 | times: 4 %}
        <div class= "row">
            {% for post in group limit:4 offset:offset %}
            {% include person_entry.html %}
            {% endfor %}
        </div>
        {% endfor %}
        <hr class="major" />
        <!-- Grads -->
		<h2 id="content">Graduate Students</h2>
		{% assign group = site.people | where_exp: "item", "item.role == 'grad'" | sort:"last_name"%}
        {% assign rows = group.size | divided_by: 4.0 | ceil %}
        {% for i in (1..rows) %}
        {% assign offset = forloop.index0 | times: 4 %}
        <div class= "row">
            {% for post in group limit:4 offset:offset %}
            {% include person_entry.html %}
            {% endfor %}
        </div>
        {% endfor %}
        <hr class="major" />
        <!-- Visiting students -->
		<h2 id="content">Visiting Students</h2>
		{% assign group = site.people | where_exp: "item", "item.role == 'vstud'" | sort:"last_name"%}
        {% assign rows = group.size | divided_by: 4.0 | ceil %}
        {% for i in (1..rows) %}
        {% assign offset = forloop.index0 | times: 4 %}
        <div class= "row">
            {% for post in group limit:4 offset:offset %}
            {% include person_entry.html %}
            {% endfor %}
        </div>
        {% endfor %}

</div>
