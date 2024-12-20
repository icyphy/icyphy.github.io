---
collection: publications
ID: 'KwokEtAl:24:HPRM'
author: 'Jacky Kwok, Shulu Li, Marten Lohstroh, Edward A. Lee'
title: "HPRM: High-Performance Robotic Middleware for Intelligent Autonomous Systems"
journal: 'arXiv:2412.01799v1 [cs.RO]'
month: 'Dec'
abstract: "The rise of intelligent autonomous systems, especially in robotics and autonomous agents, has created a critical need for robust communication middleware that can ensure real-time processing of extensive sensor data. Current robotics middleware like Robot Operating System (ROS) 2 faces challenges with nondeterminism and high communication latency when dealing with large data across multiple subscribers on a multi-core compute platform. To address these issues, we present High-Performance Robotic Middleware (HPRM), built on top of the deterministic coordination language Lingua Franca (LF). HPRM employs optimizations including an in-memory object store for efficient zero-copy transfer of large payloads, adaptive serialization to minimize serialization overhead, and an eager protocol with real-time sockets to reduce handshake latency. Benchmarks show HPRM achieves up to 173x lower latency than ROS2 when broadcasting large messages to multiple nodes. We then demonstrate the benefits of HPRM by integrating it with the CARLA simulator and running reinforcement learning agents along with object detection workloads. In the CARLA autonomous driving application, HPRM attains 91.1% lower latency than ROS2. The deterministic coordination semantics of HPRM, combined with its optimized IPC mechanisms, enable efficient and predictable real-time communication for intelligent autonomous systems."
paperurl: 'https://arxiv.org/abs/2412.01799'
year: '2024'
ENTRYTYPE: 'article'
---

