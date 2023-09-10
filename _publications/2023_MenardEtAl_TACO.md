---
collection: publications
ID: 'MenardEtAl:23:Determinisitic'
author: 'Christian Menard, Marten Lohstroh, Soroush Bateni, Matthew Chorlian, Arthur Deng, Peter Donovan, Clément Fournier, Shaokai Lin, Felix Suchert, Tassilo Tanneberger, Hokeun Kim, Jeronimo Castrillon, Edward A. Lee'
title: "High-Performance Deterministic Concurrency using Lingua Franca"
journal: 'ACM Transactions on Architecture and Code Optimization (TACO)'
month: 'August'
abstract: "Actor frameworks and similar reactive programming techniques are widely used for building concurrent systems. They promise to be efficient and scale well to a large number of cores or nodes in a distributed system. However, they also expose programmers to nondeterminism, which often makes implementations hard to understand, debug, and test. The recently proposed reactor model is a promising alternative that enables deterministic concurrency. In this paper, we present an efficient, parallel implementation of reactors and demonstrate that the determinacy of reactors does not imply a loss in performance. To show this, we evaluate Lingua Franca (LF), a reactor-oriented coordination language. LF equips mainstream programming languages with a deterministic concurrency model that automatically takes advantage of opportunities to exploit parallelism. Our implementation of the Savina benchmark suite demonstrates that, in terms of execution time, the runtime performance of LF programs even exceeds popular and highly optimized actor frameworks. We compare against Akka and CAF, which LF outperforms by 1.86x and 1.42x, respectively."
paperurl: 'https://dl.acm.org/doi/10.1145/3617687'
year: '2023'
ENTRYTYPE: 'article'
---
