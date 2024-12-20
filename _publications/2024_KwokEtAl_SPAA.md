---
collection: publications
ID: 'KowkEtAl:24:ParML'
author: 'Jacky Kwok, Marten Lohstroh, Edward A. Lee'
title: "Efficient Parallel Reinforcement Learning Framework Using the Reactor Model"
booktitle: 'Proceedings of the 36th ACM Symposium on Parallelism in Algorithms and Architectures (SPAA)'
month: 'June'
abstract: "Parallel Reinforcement Learning (RL) frameworks are essential for mapping RL workloads to multiple computational resources, allowing for faster generation of samples, estimation of values, and policy improvement. These computational paradigms require a seamless integration of training, serving, and simulation workloads. Existing frameworks, such as Ray, are not managing this orchestration efficiently, especially in RL tasks that demand intensive input/output and synchronization between actors on a single node. In this study, we have proposed a solution implementing the reactor model, which enforces a set of actors to have a fixed communication pattern. This allows the scheduler to eliminate work needed for synchronization, such as acquiring and releasing locks for each actor or sending and processing coordination-related messages. Our framework, Lingua Franca (LF), a coordination language based on the reactor model, also supports true parallelism in Python and provides a unified interface that allows users to automatically generate dataflow graphs for RL tasks. In comparison to Ray on a single-node multi-core compute platform, LF achieves 1.21x and 11.62x higher simulation throughput in OpenAI Gym and Atari environments, reduces the average training time of synchronized parallel Q-learning by 31.2%, and accelerates multi-agent RL inference by 5.12x."
paperurl: 'https://dl.acm.org/doi/10.1145/3626183.3659967'
year: '2024'
ENTRYTYPE: 'inproceedings'
---

