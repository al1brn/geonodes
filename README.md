# geonodes

![Scripting Geometry Nodes for Blender](docs/images/geonodes.png)

## Short

**Geometry nodes** is a powerful **Blender** feature allowing the creation of amazing 3D models.
However, nodes trees can rapidly look like a _spaghetti plate_ difficult to understand and to maintain.
Complex formulas are not easy to build and debugging can be a headache.<br>
 
> The purpose of **_geonodes_** is to to create geometry nodes with python scripts.<br>
 
You keep the full power of Blender geometry nodes but with the elegance of Python.

## Table of contents

- [Better a demo than long words](#better-a-demo-than-long-words)
- [Installation](#installation)
- [Documentation](#documentation)
- [Scripting nodes overview][#Scripting-nodes-overview]
- [API reference](docs/index.md)
- Tutorials by examples:
  - [Getting started](docs/getting_started.md) with the "Hello world" script
  - [Building an arrow](docs/arrow.md)
  - [4D project](4d/4d%20project.md): a"big" project using **geonodes** to create 4D geometry modifiers.
  - [Simulation](docs/simulation.md) : how to create and use a simulation zone

## Better a demo than long words

The following script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the distance of the vertex to the center.

```python
from geonodes import GeoNodes, Shader

with GeoNodes("Hello World", clear=True) as tree:
    
    # Let's document our parameters
    count  = 100  # Grid resolution
    size   = 20   # Size
    omega  = 2.   # Period
    height = 2.   # Height of the surface
    
    
    # The base (x, y) grid
    grid = tree.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size).mesh
    
    # We compute z
    with tree.layout("Computing the wave"):
        # Separate XYZ the position vector 
        s_pos = tree.position().separate_xyz()
        # Compute the distance
        distance = tree.sqrt(s_pos.x**2 + s_pos.y**2)
        # Height in z
        z = height * tree.sin(distance*omega)/distance
        
    # Let's change the z coordinate of our vertices
    grid.set_position(offset=(0, 0, z))
    
    # We are done: plugging the deformed grid as the modified geometry
    tree.output_geometry = grid.set_shade_smooth()     
```

> See [Demo details](docs/demo_1.md)

The generated nodes and the result of the Geometry nodes modifier is given below:

<img src="docs/images/demo_intro.png" width="600" class="center">

## Installation

**geonode** is a python package. To install it, copy the package folder **geonodes** in `scripts/modules`.

The Blender `scripts` folder is defined in Blender preferences, see: [Blender File Paths settings](https://docs.blender.org/manual/en/latest/editors/preferences/file_paths.html).

> Note that **geonodes** is a python module, not an Blender addon

After the install, the Blender scripts hierarchy should look like:
```
.../scripts/
       modules/
           geonodes/
               __init__.py
               core/
               nodes/
               ...
```

To make the module available in your script, use `import` in your script:

```python
import geonodes as gn
```

or

``` python
from geonodes import GeoNodes, Shader
```

> `gn` is the recommended alias for geonodes.

## Documentation

Uses [index](docs/index.md) to gain access to the list of availables classes.

## Scripting nodes overview

All nodes belong to a tree. Four tree types are available:
- `GeoNodes` : Geometry Nodes
- `Shader` : Material Nodes
- `Compositor` : Compositor Nodes
- `Texture` : Texture Nodes

### Creating a new tree

A tree is created using the with statement:

``` python
# A new geometry nodes modifier
with GeoNodes("Geometry Nodes name", options) as tree:
    ...

# A new material
with Shader("Material") as tree:
    ...
```

###CAUTION### : when opening a tree, the existing nodes are deleted!

### Nodes and sockets

The module handles two types of classes:
- ##Node## classes : by instanciating such a class, a node is created in the current tree
- ##Socket## classes : the #sockets## of a node are exposed as attributes the node class

In the example below, a node "Ico Sphere" is created and the two output sockets are used to set two python variables:

``` python
with GeoNodes("Demo") as tree:
    # Node class instanciation
    node = tree.IcoSphere(radius=2, subdivisions=3)

    # Getting the two output sockets of the node
    sphere = node.mesh
    uvmap = node.uv_map
```

##Sockets## instances are then used as input sockets of for other nodes:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    node = tree.SetMaterial(geometry=sphere, material="Material")
```

##Sockets## also expose methods to create node in a more 'pythonist' style:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    # The two following statements are equivalent

    sphere = tree.SetMaterial(geometry=sphere, material="Material").geometry

    sphere.set_material("Material")
```

### Naming conventions

The name of the classes, sockets and methods are built with the following coventions: 
- Nodes classes are **CamelCase** versions of the node name:
  - Node _'Set Shade Smooth'_ --> `SetShadeSmooth`
- Methods calling a node are **snake_case** of the Blender name:
  - `mesh.set_shade_smooth()`
- Node sockets are **snake_case** of their Blender name:
  - Socket _'Mesh'_ --> `mesh`



Inside the with statement block, nodes can be created by using the camel case version of their label:

```python
with GeoNodes("Demo") as tree:
     # Create an Ico Sphere with default initial values
     node = tree.IcoSphere()
```

At initialization time, the sockets can be set using arguments. The arguments are the snake case of the socket names:

```python
with GeoNodes("Demo") as tree:
    # Create an Ico Sphere with custom initial values
    node = tree.IcoSphere(radius=2, subdivisions=3)
```

The sockets can also be set afterwards:

``` python
with GeoNodes("Demo") as tree:
    node = tree.IcoSphere()
    node.radius=2
    node.subdivisions = 3
``` 

The sphere geometry can be read from the node output socket name:


Other nodes can be created using the geometry as input. Rather than using the node class name, one can use a method of the socket.
The following example shows two ways to create the node "Set Material":
- Creating the node with `SetMaterial`
- Using the method `set_material` of the `Geometry` class

``` python
with GeoNodes("Demo") as tree:
    node = tree.IcoSphere(radius=2, subdivisions=3)
    sphere = node.mesh
    uvmap = node.uv_map
    
    sphere = tree.SetMaterial(geometry=sphere, material="Material").geometry
    
    # or, better
    
    sphere.set_material("Material")
```

In addition to create the node, the `set_material` method makes the python `sphere` variable points to the output socket of the newly created node:
- Before calling `set_material` method : `sphere` is the `IcoSphere.mesh` socket
- After calling `set_material` method : `sphere` is the `SetMaterial.geometry` socket

Note that in this example, the `material` socket accepts:
- `None` to keep the material socket empty
- A string as the name of an existing Material
- A Blender Material object
- A socket

To plug a geometry to the group input node as the result of the Geometry Node modifier, use the socket `tree.output_geometry`:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh
    sphere.set_material("Material")
    tree.output_geometry = sphere
```

Similary, input geometry can be read from the input node using the `tree.input_geometry` socket.
Custom parameters can be created using `tree.xxx_input` methods as shown in the example below:

``` python
from geonodes import GeoNodes, Shader

# Let's build a shader specific to our amazing Geometry Nodes modifier

with Shader("Ico Shader") as tree:
    node = tree.PrincipledBSDF(base_color=(.1, .2, .3), roughness=.1)
    tree.output_surface = node.bsdf

# A variable Ico Sphere using our shader

with GeoNodes("Demo") as tree:
    # Let's expose two parameters
    radius = tree.float_input("Radius", 1.)
    subs   = tree.int_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico sphere subdivisions. Don't be too ambitious!")

    # An ico sphere with out material
    sphere = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
    sphere.set_material("Ico Shader")

    # Let's plug it into the modifier output
    tree.output_geometry = sphere
```

## Naming

**geonodes** classes and properties are named after the Blender names.


