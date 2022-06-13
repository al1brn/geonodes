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
- [Classes index](docs/index.md)

## Better a demo than long words

The following script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the distance of the vertex to the center.

```python
# Import the geonodes module
# gn is the suggested alias
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
        distance = gn.sqrt(grid.position.x**2 + grid.position.y**2)
        z = height * gn.sin(distance*omega)/distance
        
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

### Nodes and sockets

Geometry nodes are linked between their output and input sockets.

In **geonodes**:
- output sockets are the central **data classes**
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

### Naming

**geonodes** classes and properties are named after the Blender names.

- Nodes classes are **CamelCase** versions of Blender geometry nodes name:
  - Node _'Set Shade Smooth'_ --> `SetShadeSmooth`
- Methods calling a node are **snake_case** of the Blender name:
  - `mesh.set_shade_smooth()`
- Node sockets are **snake_case** of their Blender name:
  - Socket _'Mesh'_ --> `mesh`

For more details, refer to [Naming conventions TBD](docs/naming.md)

