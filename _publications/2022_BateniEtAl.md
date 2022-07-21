---
collection: publications
ID: 'BateniEtAl:22:Xronos'
author: 'Soroush Bateni, Marten Lohstroh, Hou Seng Wong, Rohan Tabish, Hokeun Kim, Shaokai Lin, Christian Menard, Cong Liu, Edward A. Lee'
title: "Xronos: Predictable Coordination for Safety-Critical Distributed Embedded Systems"
journal: 'arXiv:2207.09555 [cs.DC]'
month: 'July'
abstract: "Asynchronous frameworks for distributed embedded systems, like ROS and MQTT, are increasingly used in safety-critical applications such as autonomous driving, where the cost of unintended behavior is high. The coordination mechanism between the components in these frameworks, however, gives rise to nondeterminism, where factors such as communication timing can lead to arbitrary ordering in the handling of messages. In this paper, we demonstrate the significance of this problem in an open-source full-stack autonomous driving software, Autoware.Auto 1.0, which relies on ROS 2. We give an alternative: Xronos, an open-source framework for distributed embedded systems that has a novel coordination strategy with predictable properties under clearly stated assumptions. If these assumptions are violated, Xronos provides for application-specific fault handlers to be invoked. We port Autoware.Auto to Xronos and show that it avoids the identified problems with manageable cost in end-to-end latency. Furthermore, we compare the maximum throughput of Xronos to ROS 2 and MQTT using microbenchmarks under different settings, including on three different hardware configurations, and find that it can match or exceed those frameworks in terms of throughput."
paperurl: 'https://arxiv.org/abs/2207.09555'
year: '2022'
ENTRYTYPE: 'article'
---

