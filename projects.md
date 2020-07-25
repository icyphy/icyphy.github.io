---
title: Projects
layout: page
description: 'Overview of active projects.'
image: assets/images/pic07.jpg
nav-menu: true
order: 2
show_at: home
---

<!-- Main -->
<div id="main">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h1>iCyPhy Projects</h1>
		</header>
				<p>iCyPhy projects are open, collaborative efforts, often directly involving personnel from member companies. ICyPhy is committed to open <a href="publications.html">publication</a> and open-source release of software and hardware designs using a BSD-style license and will not seek IP protection for research results unless there is an overwhelmingly compelling case that IP protection is necessary for the results to have impact.</p>
	</div>
</section>

<!-- Two -->
<section id="two" class="spotlights">
	<section>
		<a href="https://github.com/icyphy/lingua-franca/wiki" class="image">
			<img src="{% link assets/images/projects/LinguaFranca.png %}" alt="Screen image of Lingua Franca IDE" data-position="center center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Lingua Franca</h3>
				</header>
		<p>Lingua Franca is a polyglot coordination language with an explicit model of time, more deterministic concurrency, and support for efficient, fault-tolerant, distributed applications. In Lingua Franca, components called reactors (for "actors revisited") execute under a deterministic, discrete-event model of computation that combines the best features of actors, synchronous languages, and discrete-event models. The functionality of a reactor is written in an unmodified target language (currently C, C++, or TypeScript). With the C target, the Lingua Franca compiler generates efficient, low footprint code that transparently exploits multiple cores and realizing earliest-deadline-first (EDF) scheduling. With the TypeScript target, seamless integration with the Node.js ecosystem offers a wealth of high-level IoT capabilities.</p>
				<ul class="actions">
					<li><a href="https://github.com/icyphy/lingua-franca/wiki" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="https://openpapr.berkeley.edu/our-solution/" class="image">
			<img src="{% link assets/images/projects/OpenPAPR.png %}" alt="Powered purifying-air respirator" data-position="top center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>OpenPAPR</h3>
				</header>
				<p>The Covid-19 pandemic has resulted in a dramatic, global shortage across the entire "Arsenal of Health" needed for this fight, including gloves, gowns, N95 masks, samplers, reagents, face shields, respirators, ventilators, and many other medical consumables and reusables. Leveraging our experience with system design, we have designed a particular type of respirator called a PAPR (powered purifying-air respirator) that is in short supply. PAPRs are a critical piece of clinical equipment used to protect health care workers during potentially risky aerosol generating procedures including intubation. Our design is composed of readily available parts plus some 3D-printed parts and custom electronics. All designs are open source, and target production cost is $250/unit in volume.</p>
				<ul class="actions">
					<li><a href="https://openpapr.berkeley.edu/our-solution/" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="https://en.wikipedia.org/wiki/Montparnasse_derailment" class="image">
			<img src="{% link assets/images/projects/Train_wreck_at_Montparnasse_1895.jpg %}" alt="Train wreck at Gare Montparnasse in 1895" data-position="top center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>UCLID5</h3>
				</header>
				<p>Formal methods for ensuring safety and correctness of systems are facing a confluence of transformative trends. First, systems are increasingly heterogeneous, comprising some combination of hardware, software, networking, and physical processes. Second, these systems are increasingly being designed with data-driven methods. Third, automated reasoning techniques based on deduction are being combined with new techniques for inductive inference and machine learning. UCLID5 is a new system for formal modeling, verification, and synthesis that addresses the challenges and opportunities arising from this confluence. UCLID5 can model heterogeneous computational systems, provides term-level abstraction supported by satisfiability modulo theories (SMT) solvers, enables compositional reasoning, and implements the paradigm of verification by reduction to synthesis, leveraging the advances in algorithmic synthesis and machine learning.</p>
				<ul class="actions">
					<li><a href="https://cse.iitk.ac.in/users/spramod/papers/memocode18.pdf" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="https://arxiv.org/pdf/2005.01890.pdf" class="image">
			<img src="{% link assets/images/projects/IndustrialControl.png %}" alt="cooling and auxiliary regulation system configuration for a gas turbine migrated with to real-time enabled cloud" data-position="top center"/>
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Industrial Control</h3>
				</header>
				<p>Industry 4.0 is changing fundamentally data collection, storage, and analysis in industrial processes, enabling novel application such as flexible manufacturing of highly customized products. However, industrial control systems are typically tailored to the plant they control, making reuse and adaptation a challenge. We believe that modern virtualization techniques, specifically application containers, present a unique opportunity to decouple control from plants. This separation permits us to fully realize the potential for highly distributed, and transferable industrial processes even with real-time constraints arising from time-critical sub-processes. In this project, we explore the challenges and opportunities of shifting in- dustrial control software from dedicated hardware to bare-metal servers or (edge) cloud computing platforms using off-the-shelf technology. We are developing an orchestration tool that containerized applications can run on without compromising scheduled execution.</p>
				<ul class="actions">
					<li><a href="https://arxiv.org/pdf/2005.01890.pdf" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>


</div>
