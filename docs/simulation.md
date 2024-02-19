# Simulation

> Tutorial on how to create a simulation zone.
>
> Also refer to [Simulation](GeoNodes_classes/Simulation.md) class documentation to see generators such as Fluid which allow to quickly set up a fluid simulator.

## Objective

We want to randomly create curves at the surface of the input geometry:
- Generate random points
- At each step, extruding each point randomly on the surface
- Trying to beautify the result

## How the create a simulation zone

A simulation zone is made of two nodes: **Simulation Input** and **Simulation Output**.
These two nodes have the same input and output sockets with one exception: the **input node** has an additional output socket : **Delta Time**

<img src="images/simulation_zone.png" width="600" class="center">

The nodes are created by instanciating a **Simulation** class. The class constructor takes key word arguments used to name the sockets of the simulation zone. In the following example, a simulation zone is created with one vector to be used in the simulation loops:

<img src="images/simulation_creation.png" width="600" class="center">

``` python
from geonodes import GeoNodes

with GeoNodes("Simul") as tree:
    with tree.simulation(geometry=tree.ig, position=(0, 0, 0)) as simul:
        pass
```

The zone internal links can be manually set with:


At creation time, the *geometry* sockets inside the simulation zone are not connected. Within the `with` block, this can be done by

``` python
from geonodes import GeoNodes

with GeoNodes("Simul") as tree:
    with tree.simulation(geometry=tree.ig, position=(0, 0, 0)):
        simul.geometry = simul.geometry
        simul.position = simul.position
```

The image below shows the effect the resulting simulation zone:

<img src="images/simulation_zone_closed.png" width="600" class="center">

### With statement

Rather than explicitly clossing the simulation, the ``` with ``` statement can be preferabily used.

## Accessing the sockets

For each keyword argument, 4 sockets are created in the simulation zone:
1. **input socket of the input node** : connected with the value of the arguments
2. **output socket of the input node** : accessible through the attribute of the simulation with the name of the key word
3. **input socket of the output node** : connected when *close* method is called
4. **output socket of the output node** : accessible through the attribute of the simulation with the name of the key word

For instance, with the keyword argument ``` geometry=mesh ```:
1. The mesh geometry is connected to the input socket named 'Geometry' of the simulation input node
2. **Within the simulation zone** (i.e. before closing) use ``` simul.geometry ``` to get the geometry
3. The input socket 'Geometry' of the output node is connected with the socket pointed by ``` simul.geometry ```
4. **Outside the simulation zone** (i.e. after closing) use ``` simul.geometry ``` to get the simulated geometry

:warning: **NOTE** ``` simul.geometry ``` refers to different sockets before and after closing the simulation zone.
The use of ``` with ``` statement makes things simple.

``` python
import geonodes as gn

with gn.Tree("Simul", auto_capture=False) as tree:

    with gn.Simulation(geometry=gn.Mesh(tree.ig)) as simul:
        # Within the simulation zone, simul.geometry is the output socket of the input node        
        simul.geometry.verts.position_offset = gn.Vector.Random(-1, 1, seed=tree.frame).scale(.1)

        # Now simul.geometry points to the output socket of a 'Set Position' node
        # This will be connected to the simulation output node when closed
        
    # Outside the simulation zone, simul.geometry is the output socket of the output node
    # i.e. the result of the simulation
    tree.og = simul.geometry
```

:warning: **NOTE** within the simulation, make sure that, before closing, ``` simul.geometry ``` is the geometry that you want to connect to
simulation output node.

``` python
# Incorrect
with gn.Simulation(geometry=tree.ig) as simul:
    # Join the geometry with the simulation geometry
    geo = simul.geometry + gn.Mesh.Cube().mesh
    # simul.geometry is unchanged

# Correct
with gn.Simulation(geometry=tree.ig) as simul:
    # Join the geometry with the simulation geometry
    simul.geometry = simul.geometry + gn.Mesh.Cube().mesh
    # simul.geometry points to the result of the geometry join node
```

## Do nothing simulation

The *do nothing* simulation can be created with:

``` python
import geonodes as gn

with gn.Tree("Do nothing simulation") as tree:
  # Create the simulation zone with tree input geometry
  with gn.Simulation(geometry=tree.ig) as simul:
      pass

  # The simulated geometry is use as tree output
  tree.og = simul.geometry
```

## Something more interesting

The following tree generates random points on the faces of the input geometry. Each time, the simulation zone is executed, the last vertices are randomly extruded. The last vertex flag is stored in the named attribute "Top".

``` python
import geonodes as gn

with gn.Tree("Simul", auto_capture=False) as tree:
    
    # Points on the input geometry (allegedly a mesh)
    
    mesh = gn.Mesh(tree.ig).distribute_points_on_faces(density=gn.Float(10, "Density")).points.to_vertices()

    # We need to extrude only the last vertices
    # At the begining all the vertices are the last
    
    mesh.store_named_attribute(name="Top", value=True)
    
    # ----- The simulation zone
    
    with gn.Simulation(mesh=mesh) as simul:
    
        # Let's generate the extrusion direction by a random vector perpendicular to the normal
        
        normal = simul.mesh.verts.normal
        v = gn.Vector(gn.Texture.Noise4D(w=tree.seconds).color) - (.5, .5, .5)

        # Extrusion along this vector
        
        top  = simul.mesh.verts[mesh.verts.named_boolean("Top")].extrude(offset=normal.cross(v).scale(.1)).top
        
        # Let's update the last vertex flag
        
        simul.mesh.verts.store_named_attribute("Top", top)

        
    # ----- Outside the simulation
    # Transformation to NURBS curve
    
    curve = simul.mesh.to_curve()
    curve.splines.type = 'NURBS'

    # Removing the begining with time

    curve.splines.trim(start=gn.max(0, (tree.frame - 100)/250))
    
    # Done
    
    tree.og = curve
```

<img src="images/simulation_res1.png" width="600" class="center">

## Alternative storing a named attribute

Rather than using the named attribute, we can use a simulation state named **top**.

``` python
import geonodes as gn

with gn.Tree("Simul", auto_capture=False) as tree:
    
    # Points on the input geometry (allegedly a mesh)
    
    mesh = gn.Mesh(tree.ig).distribute_points_on_faces(density=gn.Float(10, "Density")).points.to_vertices()

    # ----- The simulation zone
    
    with gn.Simulation(mesh=mesh, top=True) as simul:
        
        # Let's generate the extrusion direction by a random vector perpendicular to the normal
        
        normal = simul.mesh.verts.normal
        v = gn.Vector(gn.Texture.Noise4D(w=tree.seconds).color) - (.5, .5, .5)

        # Extrusion along this vector
        # By setting the top result into simul.top attribute, it will be connected to the simulation output node
        
        simul.top = simul.mesh.verts[simul.top].extrude(offset=normal.cross(v).scale(.1)).top
        
    # ----- Outside the simulation
    # Transformation to NURBS curve
    
    curve = simul.mesh.to_curve()
    curve.splines.type = 'NURBS'

    # Removing the begining with time

    curve.splines.trim(start=gn.max(0, (tree.frame - 100)/250))
    
    # Done
    
    tree.og = curve 
```

The image below shows the use of **top** simulation state rather than the stored attribute:

<img src="images/simulation_top.png" width="600" class="center">






 















