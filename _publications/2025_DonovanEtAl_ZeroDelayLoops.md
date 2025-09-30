---
collection: publications
ID: 'DonovanEtAl:25:ZeroDelay'
author: 'Peter Donovan, Erling Jellum, Byeonggil Jun, Hokeun Kim, Lee Edward, Shaokai Lin, Marten Lohstroh, and Anirudh Rengarajan'
title: "Zero-Delay Cycles in Distributed Discrete-Event Systems using Lingua Franca"
journal: 'ACM Transactions on Modeling and Computer Simulation'
volume: 'to appear'
month: 'August'
paperurl: 'https://doi.org/10.1145/3762653'
abstract: "Discrete-event (DE) systems are concurrent programs where components communicate via tagged events, where tags are drawn from a totally ordered set. Distributed DE (DDE) systems are DE systems where the components (reactors) communicate over networks. Most execution platforms require that for DDE systems with cycles, each cycle must contain at least one logical delay, where the tag of events is incremented. Some impose an even stronger constraint, that no component produce outputs with the same timestamp as a triggering input (the “lookahead” for the component must be greater than zero). Such restrictions, however, are not required by the elegant fixed-point semantics of DE. The only fundamental requirement is that the program be constructive, meaning it is free from causality cycles. In this paper, we propose a way to coordinate the execution of DDE systems that can execute any constructive program, even one with zero-delay cycles (ZDC), facilitating the elegant programming of strongly consistent distributed real-time systems. The proposed coordination provides a formal model that exposes exactly the information that must be shared across networks for such execution to be possible. Our solution avoids speculative execution and rollback, making it suitable for situations that do not tolerate rollback, such as deployment (vs. simulation) of cyber-physical systems (CPS’s). We describe an extension to the coordination mechanisms in Lingua Franca, a recent DE-based coordination language, to support ZDC."
doi: '10.1145/3762653'
year: '2025'
ENTRYTYPE: 'article'
---
