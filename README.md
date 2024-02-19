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



