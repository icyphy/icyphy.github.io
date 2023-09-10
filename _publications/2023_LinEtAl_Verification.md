---
collection: publications
ID: 'LinEtAl:23:Verification'
author: 'Shaokai Lin, Yatin A. Manerkar, Marten Lohstroh, Elizabeth Polgreen, Sheng-Jung Yu, Chadlia Jerad, Edward A. Lee, Sanjit A. Seshia'
title: "Towards Building Verifiable CPS using Lingua Franca"
journal: 'ACM Transactions on Embedded Computing Systems (TECS)'
month: 'September'
abstract: "Formal verification of cyber-physical systems (CPS) is challenging because it has to consider real-time and concurrency aspects that are often absent in ordinary software. Moreover, the software in CPS is often complex and low-level, making it hard to assure that a formal model of the system used for verification is a faithful representation of the actual implementation, which can undermine the value of a verification result. To address this problem, we propose a methodology for building verifiable CPS based on the principle that a formal model of the software can be derived automatically from its implementation. Our approach requires that the system implementation is specified in Lingua Franca (LF), a polyglot coordination language tailored for real-time, concurrent CPS, which we made amenable to the specification of safety properties via annotations in the code. The program structure and the deterministic semantics of LF enable automatic construction of formal axiomatic models directly from LF programs. The generated models are automatically checked using Bounded Model Checking (BMC) by the verification engine Uclid5 using the Z3 SMT solver. The proposed technique enables checking a well-defined fragment of Safety Metric Temporal Logic (Safety MTL) formulas. To ensure the completeness of BMC, we present a method to derive an upper bound on the completeness threshold of an axiomatic model based on the semantics of LF. We implement our approach in the LF Verifier and evaluate it using a benchmark suite with 22 programs sampled from real-life applications and benchmarks for Erlang, Lustre, actor-oriented languages, and RTOSes. The LF Verifier correctly checks 21 out of 22 programs automatically."
paperurl: 'https://dl.acm.org/doi/10.1145/3609134'
year: '2023'
ENTRYTYPE: 'article'
---
