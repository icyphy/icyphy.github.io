---
collection: publications
ID: 'DonovanEtAl:24:DDE'
author: 'Peter Donovan, Erling Jellum, Byeonggil Jun, Hokeun Kim, Edward A. Lee,
Shaokai Lin, Marten Lohstroh, Anirudh Rengarajan'
title: "Strongly-Consistent Distributed Discrete-event Systems"
journal: 'arXiv:2405.12117v1 [cs.DC]'
month: 'May'
abstract: "Discrete-event (DE) systems are concurrent programs where components communicate via tagged events, where tags are drawn from a totally ordered set. Reactors are an emerging model of computation based on DE and realized in the opensource coordination language Lingua Franca. Distributed DE (DDE) systems are DE systems where the components (reactors) communicate over networks. The prior art has required that for DDE systems with cycles, each cycle must contain at least one logical delay, where the tag of events is incremented. Such delays, however, are not required by the elegant fixed-point semantics of DE. The only requirement is that the program be constructive, meaning it is free of causality cycles. This paper gives a way to coordinate the execution of DDE systems that can execute any constructive program, even one with zero-delay cycles. It provides a formal model that exposes exactly the information that must be shared across networks for such execution to be possible. Furthermore, it describes a concrete implementation that is an extension of the coordination mechanisms in Lingua Franca."
paperurl: 'https://arxiv.org/abs/2405.12117'
year: '2024'
ENTRYTYPE: 'article'
---

