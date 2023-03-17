---
collection: publications
ID: 'JellumEtAl:23:Beyond'
author: 'Jellum, Erling Rennemo and Lin, Shaokai and Donovan, Peter and Soyer, Efsane and Shakir, Fuzail and Bryne, Torleiv and Orlandic, Milica and Lohstroh, Marten and Lee, Edward A.'
title: "Beyond the Threaded Programming Model on Real-Time Operating Systems"
booktitle: 'Workshop on Next Generation Real-Time Embedded Systems (NG-RES)'
month: 'January 18'
editor: 'Terraneo, Federico and Cattaneo, Daniele'
pages: '3:1-3:13'
abstract: 'The use of a real-time operating system (RTOS) raises the abstraction level for embedded systems design when compared to traditional bare-metal programming, resulting in simpler and more reusable application code. Modern RTOSes for resource-constrained platforms, like Zephyr and FreeRTOS, also offer threading support, but this kind of shared memory concurrency is a poor fit for expressing the reactive and interactive behaviors that are common in embedded systems. To address this, alternative concurrency models like the actor model or communicating sequential processes have been proposed. While those alternatives enable reactive design patterns, they fail to deliver determinism and do not address timing. This makes it difficult to verify that implemented behavior is as intended and impossible to specify timing constraints in a portable way. This makes it hard to create reusable library components out of common embedded design patterns, forcing developers to keep reinventing the wheel for each application and each platform. In this paper, we introduce the embedded target of Lingua Franca (LF) as a means to move beyond the threaded programming model provided by RTOSes and improve the state of the art in embedded programming. LF is based on the reactor model of computation, which is reactive, deterministic, and timed, providing a means to express concurrency and timing in a platform-independent way. We compare the performance of LF versus threaded C code - both running on Zephyr - in terms of response time, timing precision, throughput, and memory footprint.'
paperurl: 'https://doi.org/10.4230/OASIcs.NG-RES.2023.3'
year: '2023'
doi: '10.4230/OASIcs.NG-RES.2023.3'
ENTRYTYPE: 'inproceedings'
---

