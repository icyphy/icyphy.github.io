---
collection: publications
ID: 'Lee:21:CAL'
author: 'Edward A. Lee, Soroush Bateni, Shaokai Lin, Marten Lohstroh, Christian Menard'
title: "Quantifying and Generalizing the CAP Theorem"
journal: 'arXiv:2109.07771 [cs.DC]'
month: 'September'
abstract: "In distributed applications, Brewer's CAP theorem tells us that when networks become partitioned, there is a tradeoff between consistency and availability. Consistency is agreement on the values of shared variables across a system, and availability is the ability to respond to reads and writes accessing those shared variables. We quantify these concepts, giving numerical values to inconsistency and unavailability. Recognizing that network partitioning is not an all-or-nothing proposition, we replace the P in CAP with L, a numerical measure of apparent latency, and derive the CAL theorem, an algebraic relation between inconsistency, unavailability, and apparent latency. This relation shows that if latency becomes unbounded (e.g., the network becomes partitioned), then one of inconsistency and unavailability must also become unbounded, and hence the CAP theorem is a special case of the CAL theorem. We describe two distributed coordination mechanisms, which we have implemented as an extension of the Lingua Franca coordination language, that support arbitrary tradeoffs between consistency and availability as apparent latency varies. With centralized coordination, inconsistency remains bounded by a chosen numerical value at the cost that unavailability becomes unbounded under network partitioning. With decentralized coordination, unavailability remains bounded by a chosen numerical quantity at the cost that inconsistency becomes unbounded under network partitioning. Our centralized coordination mechanism is an extension of techniques that have historically been used for distributed simulation, an application where consistency is paramount. Our decentralized coordination mechanism is an extension of techniques that have been used in distributed databases when availability is paramount."
paperurl: 'https://arxiv.org/abs/2109.07771'
year: '2021'
ENTRYTYPE: 'article'
---

