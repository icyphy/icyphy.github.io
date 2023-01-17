---
collection: publications
ID: 'MenardEtAl:23:Determinisitic'
author: 'Christian Menard, Marten Lohstroh, Soroush Bateni, Matthew Chorlian, Arthur Deng, Peter Donovan, Clément Fournier, Shaokai Lin, Felix Suchert, Tassilo Tanneberger, Hokeun Kim, Jeronimo Castrillon, Edward A. Lee'
title: "High-Performance Deterministic Concurrency using Lingua Franca"
journal: 'arXiv:2301.02444 [cs.PL]'
month: 'January'
abstract: "Actor frameworks and similar reactive programming techniques are widely used for building concurrent systems. They promise to be efficient and scale well to a large number of cores or nodes in a distributed system. However, they also expose programmers to nondeterminism, which often makes implementations hard to understand, debug, and test. The recently proposed reactor model is a promising alternative that enables efficient deterministic concurrency. In this paper, we show that determinacy does neither imply a loss in expressivity nor in performance. To show this, we evaluate Lingua Franca (LF), a reactor-oriented coordination language that equips mainstream programming languages with a concurrency model that automatically takes advantage of opportunities to exploit parallelism that do not introduce nondeterminism. Our implementation of the Savina benchmark suite demonstrates that, in terms of execution time, the runtime performance of LF programs even exceeds popular and highly optimized actor frameworks. We compare against Akka and CAF, which LF outperforms by 1.86x and 1.42x, respectively."
paperurl: 'https://arxiv.org/abs/2301.02444'
year: '2023'
ENTRYTYPE: 'article'
---

