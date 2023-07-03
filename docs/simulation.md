# Simulation

> Tutorial on how to create a simulation zone.

## Objective

We want to randomly create curves at the surface of the input geometry:
- Generate random points
- At each step, extruding each point randomly on the surface
- Transforming the curves to get some interesting effects

## How the create a simulation zone

A simulation zone is made of two nodes: **Simulation Input** and **Simulation Output**.
These two nodes have the same input and output sockets with one exception: the **input node** as an additional output socket : **Delta Time**


