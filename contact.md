---
layout: page
title: Contact
image: assets/images/projects2.jpg
nav-menu: true
order: 6
show_at: home
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">
        <h1>Contact</h1>
        <hr class="major"/>

        <div class="row">
            <div class="6u 12u$(small)">
                <div class="contact-method">
                    <span class="icon alt fa-envelope"></span>
                    <h3>Email</h3>
                    {{ site.email }}
                </div>
            </div>
            <div class="6u 12u$(small)">
                <div class="contact-method">
                    <span class="icon alt fa-home"></span>
                    <h3>Address</h3>
                    <span>
                    {% if site.street_address %}
                        {{ site.street_address }}<br />
                    {% endif %}
                    {% if site.city %}
                        {{ site.city }},
                    {% endif %}
                    {% if site.state %}
                        {{ site.state }} 
                    {% endif %}
                    {% if site.zip_code %}
                        {{ site.zip_code }}<br />
                    {% endif %}
                    </span>
                </div>
            </div>
        </div>
    </div>
</section>

</div>

