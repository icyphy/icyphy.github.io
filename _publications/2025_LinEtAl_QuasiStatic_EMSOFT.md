---
collection: publications
ID: 'LinEtAl:25:QuasiStatic'
author: 'Shaokai Lin, Erling Jellum, Mirco Theile, Tassilo Tanneberger, Binqi Sun, Chadlia Jerad, Yimo Xu, Guangyu Feng, Magnus Mæhlum, Jian-Jia Chen, Martin Schoeberl, Linh Thi Xuan Phan, Jeronimo Castrillon, Sanjit A. Seshia, Edward A. Lee'
title: "Quasi-Static Scheduling for Deterministic Timed Concurrent Models on Multi-Core Hardware"
journal: 'ACM Transactions on Embedded Computing Systems'
volume: '24'
number: '5s'
month: 'September'
pages: '1-25'
paperurl: 'https://doi.org/10.1145/3762653'
abstract: "To design performant, expressive, and reliable cyber-physical systems (CPSs), researchers extensively perform quasi-static scheduling for concurrent models of computation (MoCs) on multi-core hardware. However, these quasi-static scheduling approaches are developed independently for their corresponding MoCs, despite commonality in the approaches. To help generalize the use of quasi-static scheduling to new and emerging MoCs, this paper proposes a unified approach for a class of deterministic timed concurrent models (DTCMs), including prominent models such as synchronous dataflow (SDF), Boolean-controlled dataflow (BDF), scenario-aware dataflow (SADF), and Logical Execution Time (LET). In contrast to scheduling techniques tailored exclusively to specific MoCs, our unified approach leverages a common intermediate formalism called state space finite automata (SSFA), bridging the gap between high-level MoCs and executable schedules. Once identified as DTCMs, new MoCs can directly adopt SSFA-based scheduling, significantly easing adoption. We show that quasi-static schedules facilitated by SSFA are provably free from timing anomalies and enable straightforward worst-case makespan analysis. We demonstrate the approach using the reactor model—an emerging discrete-event MoC—programmed using the Lingua Franca (LF) language. Experiments show that quasi-statically scheduled LF programs exhibit lower runtime overhead compared to the dynamically scheduled LF programs, and that the analyzable worst-case makespans enable compile-time deadline checking."
doi: '10.1145/3762653'
year: '2025'
ENTRYTYPE: 'article'
---
