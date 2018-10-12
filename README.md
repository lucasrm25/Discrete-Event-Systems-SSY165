# Discrete-Event-Systems-SSY165
Repository for the course "Discrete Event Systems (SSY165)" at Chalmers University of Technology


## Assignment 1: Automaton and Petri Nets

Implementation of a package for working with automatons and petri nets has been developed.
Among other, the following functions have been implemented:

Automaton class and helper functions, including:
- Reachability
- Coreachability
- Synchronization
- Plot

Petri Nets class and helper functions, including:
- Reachability
- Coreachability
- Synchronization
- Reachability Graph
- Plot


## Assignment 2: 

The objective of this assignment is to extend the results already obtained in Assignment 1 by including uncontrollable events and generating a supervisor that is both nonblocking and controllable. This will be achieved by implementing two algorithms already presented in the lecture notes in Python, but also implementing a new function that generates uncontrollable states.

Implemented functions:

- Safe state synthesis: Create a nonblocking and controllable Supervisor S from the synchronization of plants P=P1||P2||... and system specifications Sp=Sp1||Sp2||...