# Simulation

``` python
Simulation(sockets={}, **kwargs)
```

> Create a simulation zone**

This class Simulation generates the two nodes of a simulation zone: simulation input and output nodes.
The simulation exposes as class attributes the geometry and the simulation variables used in the simulation zone.

The key of the keyword arguments is used to name the sockets of the input and output node.

``` python
simul = Simulation(geometry=mesh, speed=(0, 0, 0))
simul.geometry  # The geometry within the simulation zone
simul.speed     # The speed within the simulation zone
```

When the simulation loop is terminated, the changes on the simulation variables must be connected to
the output nodes : ` simul.output.geometry = simul.geometry `. This is done automatically with the 'close' method :

``` python
simul = Simulation(geometry=mesh, speed=(0, 0, 0))
simul.geometry.faces.shade_smooth = True
simul.speed += (0, 0, 1)
simul.close()
```

Bettter use the context manager through a `with` statement:

``` python
with gn.Simulation(geometry=mesh, speed=(0, 0, 0)) as simul:
    simul.geometry.faces.shade_smooth = True
    simul.speed += (0, 0, 1)
```

Once the simulation is closed, the variables are the output sockets of the simulation output node.
They can be used to get the result of a simulation step:

``` python
with gn.Simulation(geometry=mesh) as simul:
    # simul.geometry refers to the geometry inside the simulation zone
    simul.geometry.faces.shade_smooth = True

# Outside the simulation zone, the geometry refers to the result of the simulation
# Let's connect the result of the simulation to the output of the tree
tree.og = simul.geometry
```

### A working demo:

``` python
from geonodes.nodes import GeoNodes

with GeoNodes("Simulation demo") as tree:

    with tree.Simulation(tree.ig) as simul:
        simul.geometry.VERTS.set_position(offset = tree.Random(-1, 1, seed=tree.frame).scale(.1))

tree.og = simul.geometry
```

Args:
- **kwargs : variables to use within the loop. Each key word creates a variable accessible within the simulation step
  and, once the simulation closed, as the result of the simulation.

#### Arguments:
- **sockets** ( = {})
- **kwargs**