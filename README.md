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
- [Scripting nodes overview](#scripting-nodes-overview)
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

***CAUTION***: when opening a tree, the existing nodes are deleted!

### Nodes and sockets

The module handles two types of classes:
- **Node** classes : by instanciating such a class, a node is created in the current tree
- **Socket** classes : the **sockets** of a node are exposed as attributes of a node class

In the example below, a node "Ico Sphere" is created and the two output sockets are used to set two python variables:

``` python
with GeoNodes("Demo") as tree:
    # Node class instanciation
    node = tree.IcoSphere(radius=2, subdivisions=3)

    # Getting the two output sockets of the node
    sphere = node.mesh
    uvmap = node.uv_map
```

**Sockets** instances are then used as input sockets of for other nodes:

``` python
with GeoNodes("Demo") as tree:
    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    node = tree.SetMaterial(geometry=sphere, material="Material")
```

**Sockets** also expose methods to create nodes in a more 'pythonist' style:

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
- When several sockets of a node share the same name, their python name is suffixed with **_i** starting from the second one:
  - `Math` has up to 3 input sockets named "Value", their python names are `value`, `value_1` and ` value_2`.
  - ***Note*** : the numbering is done for the "enabled" sockets. A node such as "Store Named Attribute" has several sockets sharing the name "Attribute" but only one at a time is enabled (the one the type of which corresponds to the data type). In that case, the node class `StoreNamedAttribute` has only one socket named `value` which points to the enabled one.
 
### Links, input and output sockets

A link is created between two nodes by **setting an input socket** with an **output socket**.

**Input sockets** are write-only attributes of the node when **Output sockets** are read-only. Hence, when a node uses the same name for an input socket and an output socket, the same name is use in the corresponding class without ambiguity.

The node "Set Shade Smooth" has an input socket and an output socket named "Geometry". The `SetShadeSmooth` class owns a single attribute named `geometry` which refers to these two sockets depending on if it is set or read:

``` python
with GeoNodes("Demo") as tree:

    sphere = tree.IcoSphere(radius=2, subdivisions=3).mesh

    node = tree.SetShadeSmooth()

    # Link output geometry of "Ico Sphere" Node into "Set Shade Smooth" input geometry
    node.geometry = sphere

    # Get the output socket of the node "Set Shade Smooth" for further use
    shaded_sphere = node.geometry
```

### Node parameters

Some nodes have parameters. The parameters are exposed as properties of the class. In the example below, the "Set Shade Smooth" node is created with "domain" parameter set to `'EDGE'` :

``` python
with GeoNodes("Demo") as tree:
    node = tree.SetShadeSmooth(domain='EDGE')
``` 
***Important*** : the behavior of some nodes can change with parameter settings. For instance, changing a parameter can disable and/or enable sockets. Hence, it is adviced to initialize the node parameters at creation time. The example illustrates why it is important :

``` python
with GeoNodes("Demo") as tree:
    
    # ----- WRONG
    
    # By default, "Store Named Attribute" data_type is 'FLOAT'
    # The following statement will plug to the FLOAT value
    node = tree.StoreNamedAttribute(name="V", value=tree.position())
    # Setting the parameter afterwards don't change the link previously created
    node.data_type = 'FLOAT_VECTOR'
    
    # ---- CORRECT
    
    node = tree.StoreNamedAttribute(name="V", value=tree.position(), data_type='FLOAT_VECTOR')
    
    # ----- BEST
    
    sphere = tree.IcoSphere().mesh
    sphere.store_named_vector("V", tree.position())
```

### Group inputs and outputs, constants

Group inputs and outputs sockets can be access as properties of the `tree`:
- **GeoNodes**:
  - `tree.input_geometry` or `tree.ig` : get the modfier input geometry socket
  - `tree.output_geometry` or `tree.og` : set the modifier output geometry socket
- **Shader**:
  - `tree.output_surface` : set the output surface BSDF socket
  - `tree.output_volume` : set the output volume BSDF socket
  - `tree.output_displacement` : set the output displacement socket

Geometry nodes tree allows custom input and output sockets. Use `xxx_input` to create custom sockets.

``` python
with GeoNodes("Demo") as tree:
    # Let's expose two parameters
    radius = tree.float_input("Radius", 1.)
    subs   = tree.int_input("Subdivisions", 3, min_value=1, max_value=6, description="Ico sphere subdivisions. Don't be too ambitious!")

    # An ico sphere
    tree.output_geometry = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
```

With a **GeoNodes** tree, any socket can be plugged to the output with the method `to_output(name)`.

Constant values, if required, can be created by calling snake case version of the input nodes:

``` python
with GeoNodes("Demo") as tree:
    pi = tree.value(3.1415926)
    count = tree.integer(50)
```

### Maths

Python operators can be used with sockets and between sockets and standard python value.

``` python
with GeoNodes("Demo") as tree:
    pi = tree.value(3.1415926)
    # Use input
    count = tree.integer_input("Count", 50)

    # Some strange but certainly smart computations
    angle = 2*pi/count
    a = tree.sin(angle/17)
    b = tree.cos((angle**2 + 67) % 5)

    # To node output
    (a + b).to_output("At last")
```

***Note*** : boolean operator such as `and` or `not` can't be used to generated nodes. One can use `+` and `*` between boolean sockets:

``` python
with GeoNodes("Demo") as tree:
    
    a = tree.bool_input("A", False)
    b = tree.bool_input("B", False)
    
    # a OR b
    c = a + b
    
    # a AND b
    d = a*b
    
    # NOT a
    e = -a
```
### wrap up

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

    # An ico sphere with our material
    sphere = tree.IcoSphere(radius=radius, subdivisions=subs).mesh
    sphere.set_material("Ico Shader")

    # Let move it upwards
    sphere.set_position(offset=(0, 0, 2))

    # We join it with the input geometry
    geo = tree.ig + sphere

    # Let's plug it into the modifier output
    tree.output_geometry = geo
```



