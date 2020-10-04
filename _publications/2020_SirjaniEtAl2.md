---
collection: publications
ID: 'SirjaniEtAl:20:ModelChecking'
author: 'Marjan Sirjani, Ehsan Khamespanah, and Edward A. Lee'
title: "Model Checking Software in Cyberphysical Systems"
booktitle: 'IEEE Computers, Software, and Applications Conference (COMPSAC)'
month: 'July'
abstract: "Model checking a software system is about verifying that the state trajectory of every execution of the software satisfies formally specified properties. The set of possible executions is modeled as a transition system. Each 'state' in the transition system represents an assignment of values to variables, and a state trajectory (a path through the transition system) is a sequence of such assignments. For cyberphysical systems (CPSs), however, we are more interested in the state of the physical system than the values of the software variables. The value of model checking the software therefore depends on the relationship between the state of the software and the state of the physical system. This relationship can be complex because of the real-time nature of the physical plant, the sensors and actuators, and the software that is almost always concurrent and distributed. In this paper, we study different ways to construct a transition system model for the distributed and concurrent software components of a CPS. We describe a logical-time based transition system model, which is commonly used for verifying programs written in synchronous languages, and derive the conditions under which such a model faithfully reflects physical states. When these conditions are not met (a common situation), a finer-grained event-based transition system model may be required. Even this finer-grained model, however, may not be sufficiently faithful, and the transition system model needs to be refined further to express not only the properties of the software, but also the properties of the hardware on which it runs. We illustrate these tradeoffs using a coordination language called Lingua Franca that is well-suited to extracting transition system models at these various levels of granularity, and we extend the Timed Rebeca language and its tool Afra to perform this extraction and then to perform model checking."
paperurl: 'https://ptolemy.berkeley.edu/publications/papers/20/SirjaniEtal_VerificationOfCPS_Compsac_Preprint.pdf'
year: '2020'
ENTRYTYPE: 'inproceedings'
---

