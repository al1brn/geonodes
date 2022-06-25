# geonodes

![Scripting Geometry Nodes for Blender](docs/images/geonodes.png)

## Short

**Geometry nodes** is a powerful **Blender** feature allowing the creation of amazing 3D models.
However, nodes trees can rapidly look like a _spaghetti plate_ difficult to understand and to maintain.
Complex formulas are not easy to build and debugging can be a headache.<br>
 
> The purpose of **_geonodes_** is to to create geometry nodes with python scripts.<br>
 
You keep the full power of Blender geometry nodes but with the elegance of Python.

> **NOTE** This is yet an alpha version. It is stable, but I'm still tuning node calls implementation.

## Table of contents

- [Better a demo than long words](#better-a-demo-than-long-words)
- [Installation](#installation)
- [Documentation](#documentation)
- [Classes index](docs/index.md)

## Better a demo than long words

The following script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the distance of the vertex to the center.

```python
import geonodes as gn

with gn.Tree("Geometry Nodes") as tree:

    # Let's document our parameters
    count  = 100  # Grid resolution
    size   = 20   # Size
    omega  = 2.   # Period
    height = 2.   # Height of the surface
    
    # The base (x, y) grid
    grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)
    
    # We compute z
    with tree.layout("Computing the wave", color="dark_rose"):
        distance = gn.sqrt(grid.point.position.x**2 + grid.point.position.y**2)
        z = height * gn.sin(distance*omega)/distance
        
    # Let's change the z coordinate of our vertices
    grid.verts.position += (0, 0, z)
    
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

### Scripting geometry

A **geonodes** script generates nodes through the methods of geometry classes.

The geometry classes are:
- Geometry (root class)
- Mesh
- Curve
- Points
- Instances
- Volume

`Geometry` methods are available in all the other ones:

```python
geometry.set_shade_smooth()              # Generate the 'Set Shade Smooth' node
geometry.transform(tranlation=(1, 2, 3)) # Generates the 'Transform' node
``` 

The other classes expose methods specific to their geometry:

```python
mesh2 = mesh.union(other_mesh) # 'Mesh Boolean' with Union parameter
curve.fillet()                 # 'Fillet Curve'
```

But the majority of operations are made on the geometry **domains**:
- Mesh: verts, faces, edges, corners
- Curve : points, splines
- Points : points
- Instances : insts

```python
mesh.verts.position += (0, 0, 1)        # All the mesh points are moved 1 upwards (node 'Set Position')
cloud = mesh.faces.distribute_points()  # Node 'Distribute Points on Faces'
mesh.edges.extrude()                    # Node 'Extrude Mesh' with option 'Edges'
curve.splines.type = 'BEZIER'           # Curve splines type to BEZIER
curve.points.handle_type = 'FREE'       # Curve handle type to FREE
```








In Blender, you link geometry nodes with their output and input sockets.

In **geonodes** you manipulate the vertices fo meshes, the splines of curves

In **geonodes**:
- output sockets are the pivot **data classes**
- nodes are **methods** of these data socket classes
- A method (i.e. a geometry node) links the output socket to one input socket of the method node

For instance:

```python

# Some initialization stuff where my_mesh refers to the output socket of a node

my_mesh.set_shade_smoth()

# The node 'Set Shade Smooth' was created. The output socket my_mesh is now linked
# to the input socket of 'Set Shade Smooth'
```

For more details, see [Nodes and sockets](docs/nodes_and_sockets.md)

### Data socket classes

Basically, all geometry nodes are created by calling methods and properties of the following data classes:

#### Value data

- [Boolean](docs/sockets/Boolean.md)
- [Integer](docs/sockets/Integer.md)
- [Float](docs/sockets/Float.md)
- [Vector](docs/sockets/Vector.md)
- [Color](docs/sockets/Color.md)
- [String](docs/sockets/String.md)

#### Geometry data

All geometry data classes inherit from Geometry:

- [Geometry](docs/sockets/Geometry.md)
  - [Spline](docs/sockets/Spline.md)
  - [Curve](docs/sockets/Curve.md)
  - [Mesh](docs/sockets/Mesh.md)
  - [Points](docs/sockets/Points.md)
  - [Instances](docs/sockets/Instances.md)
  - [Volume](docs/sockets/Volume.md)

#### Other sockets
  - [Collection](docs/sockets/Boolean.md)
  - [Object](docs/sockets/Object.md)
  - [Image](docs/sockets/Image.md)
  - [Texture](docs/sockets/Texture.md)
  - [Material](docs/sockets/Material.md)

#### Fields

Fields are considered as _Data Socket_ classes properties. **geonodes** analyzes the tree to determine if a 'Capture Attribute' node is necessary or not.

For more details see [Fields](/docs/attributes.md)

### Naming

**geonodes** classes and properties are named after the Blender names.

- Nodes classes are **CamelCase** versions of Blender geometry nodes name:
  - Node _'Set Shade Smooth'_ --> `SetShadeSmooth`
- Methods calling a node are **snake_case** of the Blender name:
  - `mesh.set_shade_smooth()`
- Node sockets are **snake_case** of their Blender name:
  - Socket _'Mesh'_ --> `mesh`

For more details, refer to [Naming conventions](docs/naming.md)

