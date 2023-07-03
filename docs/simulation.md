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

<img src="images/simulation_zone.png" width="600" class="center">

The nodes are created by instanciating a **Simulation** class. The class constructor takes one mandatory argument: the geometry to use in the simulation zone. It accepts addition keyword arguments corresponding to the additional sockets to use in the simulation. In the following example, a simulation zone is created with one vector to be used in the simulation loops:

<img src="images/simulation_creation.png" width="600" class="center">

``` python
import geonodes as gn

with gn.Tree("Simul") as tree:

  # Create a simulation zone for the input geometry with one socket initialized to (0, 0, 0)

  simul = gn.Simulation(tree.ig, position=(0, 0, 0))

```

The input and output nodes can be accessed with the **input** and **output** attributes:

``` python
import geonodes as gn

with gn.Tree("Simul") as tree:
  simul = gn.Simulation(tree.ig, position=(0, 0, 0))
  node = simul.input  # Simulation input node
  node = simul.output # Simulation output node

```

## Accessing the sockets

With the exception of **delta_time** output socket of the input simulation node, the socket names have four meanings:
- input socket of the input node: ``` simul.input.geometry = var```
- output socket of the input node : ``` var = simul.input.geometry ```
- input socket of the output node : ``` simul.input.geometry = var```
- output socket of the output node : ``` var = simul.input.geometry ```

To ease code writing, the Simulation instance exposes attributes for sockets used within the simulation:


``` python
with gn.Tree("Simul") as tree:
  simul = gn.Simulation(tree.ig, position=(0, 0, 0))

  v = simul.input.position # Output socket of simulation input node
  v = simul.position       # Same

  simul.output.position = v # Input socket of the simulation output node
  simul.position = v        # Same

  # Outside the simulation zone, the result can read through output node

  my_vector = simul.output.position
```

### Note

**Simulation** class exposes shortcuts for the simulation output geometry:

``` python
  # Resulting geometry through output node
  geo = simul.output.geometry

  # Or throughy Simulation shortcuts
  geo = simul.output_geometry
  geo = simul.og
```

## Do nothing simulation

The *do nothing* simulation can be created with:

``` python
import geonodes as gn

with gn.Tree("Do nothing simulation") as tree:
  # Create the simulation zone with tree input geometry as 
  simul = gn.Simulation(tree.ig)

  # Link the two simulation nodes
  simul.geometry = simul.geometry

  # The simulated geometry is use as tree output
  tree.og = simul.og
```

## Something more interesting

pass















