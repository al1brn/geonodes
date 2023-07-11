# Class Simulation

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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

A working demo:
    
``` python
import geondes as gn

with gn.Tree("Simulation demo", auto_capture=False) as tree:
    
    with gn.Simulation(mesh=gn.Mesh(tree.ig)) as simul:
        simul.mesh.verts.position_offset = gn.Vector.Random(-1, 1, seed=tree.frame).scale(.1)
        
tree.og = simul.mesh
```

#### Args:
- **kwargs : variables to use within the loop. Each key word creates a variable accessible within the simulation step
- and, once the simulation closed, as the result of the simulation.




### Constructor

```python
Simulation(self, **kwargs)
```

## Content

**Class and static methods**

[Fluid](#Fluid) | [Trajectories](#Trajectories) | [func_attraction](#func_attraction) | [func_bounce](#func_bounce) | [func_gravity](#func_gravity) | [func_group](#func_group) | [func_repulsion](#func_repulsion) | [func_stick_on_surface](#func_stick_on_surface) | [func_surface_flow](#func_surface_flow) | [func_turbulence](#func_turbulence) | [func_viscosity](#func_viscosity)

**Methods**

[close](#close)

## Class and static methods

### Fluid

```python
@classmethod
def Fluid(cls, cloud, velocity=0, life=50, setup={}, acceleration={}, finish={})
```

 Constructor building a basic simulation zone for fluid simulation.

**Note**: the name of the geometry is '*cloud*'. Use ``` simul.cloud ``` to access to the points animated by the simulation.

The nodes generated perform the standard operations:
- add new points at each step
- delete points older thant the life parameter
- update the velocity with the acceleration
- update the particles position with the updated velocity
    
The acceleration nodes are generated through functions passed as argument.
An template of the acceleration function must be:
    
``` python
def gen(simul):
```

The following example build a simple simulation from a mesh, with random initial speed and a gravity.
    
``` python
import geonodes as gn

with gn.Tree("Fluid", auto_capture=False) as tree:
    
    # Input geometry is supposed to be a mesh
    
    mesh = gn.Mesh(tree.ig)
    
    # Generate points on the surface
    
    points = mesh.faces.distribute_points(10).points
    
    # Random speed
    
    velocity = gn.Vector.Random((-1, -1, -1), (1, 1, 1), seed=tree.frame)
    
    # Fluid simulation with gravity
    
    simul = gn.Simulation.Fluid(points, velocity, 50, 
        acceleration=gn.Simulation.func_gravity((0, 0, -10)),
        )
    
    tree.og = mesh + simul.cloud 
```

Simulation offers basic acceleration functions:
- func_gravity      : constant acceleration
- func_turbulence   : noisy acceleration
- func_viscosity    : acceleration decreasing the speed
- func_repulsion    : repulsion from the nearest particle
- func_attraction   : attraction / repulsion from a location
- func_surface_flow : acceleration along a surface slope
- func_bounce       : bounce on a surface
- func_group        : use a custom group to perform computations inside the simulation loop
    
Custom nodes can be added at the begining and at the end of the simulation step with the arguments **setup** and **finish**.

The same process is used to generate complementory nodes for the set up and the finalization of the zone.

For instance, the following simulation simulates a fluid flowing on a surface:
    
``` python
import geonodes as gn

with gn.Tree("Flow", auto_capture=False) as tree:

    # The surface on which fluid will flow

    mesh = gn.Mesh(tree.ig)
    
    # Particles generation with null initial speed
    
    points   = mesh.faces.distribute_points(density=.1, seed=tree.frame).points
    velocity = gn.Vector()
    
    # Simulation with flow with viscosity and repulsion
    # Finish by making sure the particles stay on the surface and killing outside particles
    
    simul = gn.Simulation.Fluid(points, velocity, 30, 
        acceleration={
        'flow'      : gn.Simulation.func_surface_flow(mesh, gravity=(0, 0, -10)),
        'viscosity' : gn.Simulation.func_viscosity(.2),
        'repulsion' : gn.Simulation.func_repulsion(.2),
        },
        finish = {
        'stick'     : gn.Simulation.func_stick_on_surface(mesh, kill_outside=True),
        }
    )
    
    # Mesh and particles
    
    tree.og = mesh + simul.cloud
```

#### Args:
- cloud (Points): the points generated at each steap
- velocity (Vector) : the points velocity
- life (Integer) : particles life
- setup (dict or function) : function generating setup nodes or dict of such functions
- acceleration (dict or function) : function generating acceleration nodes or dict of such functions
- finish (dict or function) : function generating finalization nodes or dict of such functions




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Trajectories

```python
@classmethod
def Trajectories(cls, simul, count=10)
```

 This constructor build a simulation zone building curves tracking points of another simulation zone.

#### Args:
- simul (Simulation) : the simulation zone having a geometry of type Points
- count (int=10) : the number of frames to use for tracking




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_attraction

```python
@staticmethod
def func_attraction(location=(0, 0, 0), intensity=10, exponent=-2, d_min=.2)
```

 Returns a function which builds an attraction acceleration towards the given location.

The attraction can be used to simulate Newton gravity law with ``` exponent = -2```.

The acceleration is computed with ``` a = intensity / distance**exponent ```

To avoid infinite accelerations, the distance is minimized with d_min.

Note that if the intensity is negative, the attractor becomes a repulsor!

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_attraction(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={
    'gravity'    : gn.Simulation.func_gravity(),
    'attraction' : gn.Simulation.func_attraction(...),
    })
```

#### Args:
- location (Vector) : location of the attractor
- intensity (Float) : intensity of the attraction
- exponent (Float) : exponent parameter of the acceleration
- d_min (Float) : minimum distance to avoid infinite accelerations

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_bounce

```python
@staticmethod
def func_bounce(mesh, distance=.1, damp=0.)
```

 Returns a function creating a bounce simulation onto a mesh.

The created nodes test if the points are below the closest surface. If it is the case,
it places the points on the external side of the face an reflect the speed with the normal to thge surface.

The function returned by this method can be used as the setpt argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(setup=gn.Simulation.func_bounce(...))    


#### Args:
- mesh (Mesh)       : the surface
- distance (float)  : distance from the surface
- damp (float)      : damp factor

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_gravity

```python
@staticmethod
def func_gravity(gravity=(0, 0, -10))
```

 Returns a function which builds a constant acceleration.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_gravity(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={'gravity': gn.Simulation.func_gravity(...)})
```

#### Args:
- gravity (Vector) : the gravity vector

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_group

```python
@staticmethod
def func_group(group_name, in_delta_time=None, in_cloud=None, out_cloud=None, out_socket=None)
```

 Returns a function creating a Group node of the given name and connect sockets.

The Group can have input sockets for delta_time and cloud used in a fluid simulation.
It can have an output sockets for cloud if the cloud has been changed.

An additional output socket can be specified if the node must return a value such as an acceleration.

If the sockets exist with this name, they will be connected automatically. If they have differente names,
they must be provided using in_... and out_... arguments, for instance:
- ``` in_cloud = None ``` : the cloud will be plugged to the input socket named 'cloud', 'points' or 'geometry' if it exists
- ``` out_cloud = 'geometry' ``` : the cloud will be plugged to the input socket named 'vector'

The same is done for the output socket: variables are updated to match to the corresponding outpout sockets.

If the out_socket argument is not node, the generated function return the correspondint outpout socket of the group node.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_group("Custom Acceleration", out_socket='acceleration())    
```

#### Args:
- group_name (string) : the name of the Group node
- out_socket (str=None) : name of the output socket of the created group node to return
- in_delta_time (str=None) : nema of the *delta time* input socket
- in_cloud (str=None) : nema of the *cloud* input socket
- in_velocity (str=None) : nema of the *velocity* input socket
- in_age (str=None) : nema of the *age* input socket
- out_cloud (str=None) : nema of the *cloud* output socket
- out_velocity (str=None) : nema of the *velocity* output socket
- out_age (str=None) : nema of the *age* output socket

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_repulsion

```python
@staticmethod
def func_repulsion(intensity=1, exponent=2, d_min=.1, d_max=1)
```

 Returns a function which builds a repulstion acceleration with the nearest particle.

The repulsion is base on the vector between the particle and its nearest neighbor.
The acceleration is computed with the formula: ``` a = intensity * distance**(-exponent) ```

To avoid division by zero, distance is minimized by the argument d_min.
The repulsion is null when the distance is greater thant d_max

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_repulsion(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={
    'gravity'   : gn.Simulation.func_gravity(),
    'repulsion' : gn.Simulation.func_repulsion(...),
    })
```

#### Args:
- intensity (Float) : intensity of the repulstion
- exponent (Float) : exponent parameter of the acceleration
- d_min (Float) : minimum distance to avoid infinite acceleration
- d_max (Float) : repulsion maximum distance

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_stick_on_surface

```python
@staticmethod
def func_stick_on_surface(mesh, kill_outside=False, z_max=50)
```

 Returns a function building nodes which place the particles on the surface.

The algorithm using the raycats node to project the particles onto the surface, ```z_max``` is the latitude from which to project the particles.

if particles are outside the surface, they can be deleted if kiil_outside is True.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(finish=gn.Simulation.func_stick_on_surface(...))    
```

or, if more than one finish function is required

``` python
simul = gn.Simulation.Fluid(finish={
    'stick' : gn.Simulation.func_stick_on_surface(...),
    })
```

#### Args:
- mesh (Mesh) : the surface
- kill_outside (bool) : delete or not the particles outside the surface
- z_max (float) : the altitude higher that the surface to raycast from

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_surface_flow

```python
@staticmethod
def func_surface_flow(mesh, gravity=(0, 0, -10))
```

 Returns a function which builds an acceleration following the surface slope.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_surface_flow(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={
    'viscosity'  : gn.Simulation.func_viscosity(),
    'flow'       : gn.Simulation.func_surface_flow(...),
    })
```

#### Args:
- mesh (Mesh)       : the surface
- gravity (Vector)  : gravity vector
- intensity (Float) : intensity of the attraction
- exponent (Float) : exponent parameter of the acceleration
- d_min (Float) : minimum distance to avoid infinite accelerations

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_turbulence

```python
@staticmethod
def func_turbulence(intensity=1, scale=.2, offset=(0, 0, 0), w=0.)
```

 Returns a function which builds a turbulencce for acceleration.

The turbulence makes use of a 'Noise 4D' texture initialized with the function arguments.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_turbulence(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={
    'gravity'   : gn.Simulation.func_gravity(),
    'turbulence': gn.Simulation.func_turbulence(...),
    })
```

#### Args:
- intensity (Float) : intensity of the turbulence
- scale (Float) : scale of Noise node
- offset (Vector) : offset to apply in the 'Vector' socket of the noise node
- w (Float) : value of the 'W' socket of the noise node

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### func_viscosity

```python
@staticmethod
def func_viscosity(intensity=1, exponent=2)
```

 Returns a function which builds an acceleration simulating viscosity.

The viscosity is a function of the velocity: ``` acc = -intensitty * speed**exponent ```

This raw formula can return an acceleration which accelerates the particle in the other direction.
To avoid this behavior, the acceleration norm is capped to ``` speed/delta_time ```.

The function returned by this method can be used as an argument in a simulation zone creation method:

``` python    
simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_viscosity(...))    
```

or, if more than one acceleration function is required

``` python
simul = gn.Simulation.Fluid(acceleration={
    'gravity'   : gn.Simulation.func_gravity(),
    'viscosity' : gn.Simulation.func_viscosity(...),
    })
```

#### Args:
- intensity (Float) : intensity of the viscosity
- exponent (Float) : exponent parameter of the acceleration

#### Returns:
- function(**kwargs) : nodes generator




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### close

```python
def close(self)
```

 Closing the simulation zone.

Two operations are performed when "closing" a simulation zone:
- connect the simulation variales to the input sockets of the output node
- map the corresponding variables of the Simulation instance to the output sockets of the output node

Basically, this correspond to this pseudo code:
``` python
simul.output.geometry = simul.geometry # connect simul.geometry to the input socket of output node
simul.geometry = simul.output.geometry # simul.gemetry points now to the output socket of output node
```

In addition, the 'delta_time' attribute is deleted to avoid use outside the simulation.




<sub>Go to [top](#class-Simulation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

