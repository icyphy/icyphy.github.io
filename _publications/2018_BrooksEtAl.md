---
collection: publications
ID: 'BrooksEtAl:18:Accessors'
author: 'Christopher Brooks, Chadlia Jerad, Hokeun Kim, Edward A. Lee, Marten Lohstroh, Victor Nouvellet, Beth Osyk, and Matt Weber'
title: "A Component Architecture for the Internet of Things"
journal: 'Proceedings of the IEEE'
volume: '106'
number: '9'
pages: '1527-1542'
month: 'September'
abstract: "In this paper, we describe a component-based software architecture for the Internet of Things in which proxies for Things and services that we call 'accessors' interact with one another under a concurrent, time-stamped, discrete-event (DE) semantics. These proxies are analogous to web pages, which proxy a cloud-based service such as a bank, but instead of being designed to interface those services with humans, accessors are designed to interface services and Things with other services and Things. A deterministic DE semantics is combined with a widely used pattern for handling network interactions that we call asynchronous atomic callbacks (AACs). AAC enables many concurrent pending requests to be active at once without blocking and without the treacherous concurrency pitfalls of threads. In effect, our architecture combines AAC with actors where the actor model has been endowed with a temporal semantics. We show how this architecture can leverage the previously reported secure swarm toolkit (SST) to achieve stateof- the-art authentication, authorization, and encryption of interactions across networks."
paperurl: 'https://doi.org/10.1109/JPROC.2018.2812598'
year: '2018'
ENTRYTYPE: 'article'
---
