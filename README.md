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
               sockets/
               ...
```

To make the module available in your script, use `import` in your script:

```python
import geonodes as gn
```

> `gn` is the recommended alias for geonodes.

## Documentation

Uses [index](docs/index.md) to gain access to the list of availables classes.

## Scripting geometry

Geometry nodes are global functions operating on geometry passed through sockets.

**geonodes** presents the nodes sockets as classes and the nodes as methods.

Rather than thinking : _"What are the inputs of the 'Set Curve Tilt' node to change the tilt of spline #2?"_,
you take benefit of an object oriented language and simply write:

```python

curve.splines[2].tilt = 1

```

### Geometry classes

The geometry classes are:
- [Mesh](docs/api/Mesh.md)
- [Curve](docs/api/Curve.md)
- [Points](docs/api/Points.md)
- [Instances](docs/api/Instances.md)
- [Volume](docs/api/Volume.md)

### Domains

In geometry nodes, attributes refer to [domains](docs/api/Domain.md) such as Point, Corner, Face, Spline... 

**geonodes** implement [domains](https://al1brn.github.io/geonodes/domains.html) as properties of geometry classes.
- Mesh
  - [verts](docs/api/Vertex.md)
  - [faces](docs/api/Face.md)
  - [edges](docs/api/Edge.md)
  - [corners](docs/api/Corner.md)
- Curve
  - [points](docs/api/ControlPoint.md)
  - [splines](docs/api/Spline.md)
- Points cloud
  - [points](docs/api/CloudPoint.md)
- Instances
  - [insts](docs/api/Instance.md)

Attributes are properties or domain properties, for instances:

```python

mesh.verts.position += (0, 0, 1)        # All the mesh points are moved 1 upwards (node 'Set Position')
cloud = mesh.faces.distribute_points()  # Node 'Distribute Points on Faces'
mesh.edges.extrude()                    # Node 'Extrude Mesh' with option 'Edges'
curve.splines.type = 'BEZIER'           # Curve splines type to BEZIER
curve.points.handle_type = 'FREE'       # Curve handle type to FREE
instances.insts[0].position = (1, 2, 3) # The instance # 0 is set at position (1, 2, 3)

```

**Note 1:** **Mesh** and **Curve** have several domains, respectively (**verts**, **faces**, **edges**, **corners*) and (**splines**, **points**),
when **Points** and **Instances** have only one domain each, respectively **points** and **insts**.

### Values

To manipulate geometry, the available classes are:
- [Boolean](docs/api/Boolean.md)
- [Integer](docs/api/Integer.md)
- [Float](docs/api/Float.md)
- [Vector](docs/api/Vector.md)
- [Color](docs/api/Color.md)
- [String](docs/api/String.md)

These values are used as arguments of geometry and domain classes. With the notable exception of **Booleans**,
the values can be manipulated with python operators:

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:

    count = gn.Integer.Input(2, "Subdivisions")     # Creation of a modifier input parameter
    
    sphere = gn.Mesh.IcoSphere(subdivisions=count)  # Creation primitives are implemented as class static methods
    n = sphere.verts.count                          # count is generated with node 'Attribute statistic'
    v = gn.sqrt(n + 10)                             # Standard math functions are available as global functions
                                                    # standard operators can be used between values or between values and python data
    
    label = (gn.String("The square root of the number of vertices + 10 is: ") + gn.String.Value(v, 3)).to_curves().curve_instances
    
    location = gn.Vector()                          # Creation of null vector
    location += (1, v, 3)                           # Triplets can be used. Triplets can include geonodes types
    
    label.transform(translation=location, rotation=(gn.pi/2, 0, 0))
    
    tree.output_geometry = label + sphere           # Addition between geometries is implemented with the node 'Join Geometry'
                                                    # Setting the output_geometry property defines the ouput geometry
```

### Booleans

**geonodes** Booleans can't be manipulated with standard python operators:

```python
a = gn.Boolean(True)
b = gn.Boolean(False)
c = a or b            # No logical operation is performed, c has the value of a
d = gn.b_or(a, b)     # The right instruction to compute a logical operation in geometry nodes
d = a.b_or(b)         # Alternative syntax: boolean operators are also implemented as methods
```

Similary, logical operations between values can't be used:

```python
i = gn.Integer(10)
a = i == 10           # a is a python bool, not a geonodes Boolean
b = i.equal(10)       # Correct way to compare two values in geonodes
```

To ease the way to implement logical operations in geonodes, `+`, `-` and `*` can be used as alernative to `or`, `not` and `and`:

```python
a = gn.Boolean(True)
b = gn.Boolean(False)
c = a + b      # a or b
d = a * b      # a and b
e = -a         # not a
```

### Other sockets

Other data are available through the following classes:

  - [Collection](docs/api/Collection.md)
  - [Object](docs/api/Object.md)
  - [Image](docs/api/Image.md)
  - [Texture](docs/api/Texture.md)
  - [Material](docs/api/Material.md)

## Naming

**geonodes** classes and properties are named after the Blender names.

- Nodes classes are **CamelCase** versions of Blender geometry nodes name:
  - Node _'Set Shade Smooth'_ --> `SetShadeSmooth`
- Methods calling a node are **snake_case** of the Blender name:
  - `mesh.set_shade_smooth()`
- Node sockets are **snake_case** of their Blender name:
  - Socket _'Mesh'_ --> `mesh`

For more details, refer to [Naming conventions](docs/naming.md)

