---
collection: publications
ID: 'Lee:25:LogicalTime'
author: 'Edward A. Lee'
title: 'Logical Time in Actor Systems'
booktitle: 'Concurrent Programming, Open Systems and Formal Methods: Essays Dedicated to Prof. Gul Agha to Celebrate his Scientific Career'
editor: 'Jose Meseguer, Carlos A. Varela, Nalini Venkatasubramanian'
volume: 'LNCS 16120'
publisher: 'Springer'
abstract: 'The nondeterministic ordering of message handling in the original actor model makes it difficult to achieve the consistency across a distributed sys-tem that some applications require. This paper explores a number of mitigations, focusing primarily on the use of logical time to define a semantic ordering for messages. A variety of coordination mechanisms can ensure that messages are handled in logical time order, but they all come with costs. A fundamental trade-off (the CAL theorem) makes it impossible to achieve consistency without paying a price in availability, where the price depends on the latencies introduced by network communication, computation overhead, and clock synchronization error. This paper shows how to use the Lingua Franca coordination language to navigate this tradeoff, and particularly how to ensure eventual consistency while bounding unavailability with manageable risk.'
paperurl: 'https://eecs.berkeley.edu/~eal/publications/LeeTimeAghaFestschriftPreprint2025.pdf'
year: '2025'
doi: '10.1007/978-3-032-05291-9_16'
ENTRYTYPE: 'inproceedings'
---
