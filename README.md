# geonodes

![geonodes](docs/getting_started/images/bandeau.png)

> Current guides follow the decorator API and have been checked with **Blender 5.3 Beta**.
> Blender 5.2.0 uses the legacy implementation.

**Geometry Nodes** is a powerful **Blender** feature allowing the creation of amazing 3D models.
However, nodes trees can rapidly look like a _spaghetti plate_ difficult to understand and to maintain;
complex formulas are not easy to build; and debugging can be a headache.<br>

> The purpose of **_geonodes_** is to to create geometry nodes with python scripts.<br>

You keep the full power of Blender _Geometry Nodes_ but with the elegance of Python.

## ✨ Features

- Pythonic API for Geometry Nodes

    - Object oriented API

        - Sockets are classes
        - Nodes are methodds and propetries

    - Full node tree construction via code
    - Designed for readability and composability

- Support for:

  - Geometry Nodes and Shaders
  - Modidiers, Groups and Tools
  - Panels to build clean user interface
  - Layouts to group and comment your trees

## Further reading

- [Documentation](https://al1brn.github.io/geonodes/)
- [Overview](https://al1brn.github.io/geonodes/getting_started/overview/)
- [Installation](https://al1brn.github.io/geonodes/getting_started/installation/)
- [API reference](https://al1brn.github.io/geonodes/api)

## Better a demo than long words

The following script creates a surface from a grid by computing
`z = sin(d)/d` where `d=sqrt(x^2 + y^2)` is the vertex distance to the center.

<img src="docs/getting_started/images/hello_world_black.png" width="600" class="center">

```python
from geonodes import *

# Create the Geometry Nodes named "Hello World"

@modifier('Hello World')
def hello_world(height: float = 3.0, omega: float = 2.0):

    # The surface is basically a grid 20 x 20 with a resolution 200 x 200
    grid = Mesh.Grid(vertices_x=200, vertices_y=200, size_x=20, size_y=20)
    

    # z is computed using gnmath library and operators as in pure python
    with Layout("Computing the wave"):
        pos = nd.position
        distance = gnmath.sqrt(pos.x**2 + pos.y**2)
        z = height*gnmath.sin(distance*omega)/(distance + 0.001)

    # Let's change the z coordinate of our vertices
    with Layout("Point offset and smoothness"):
        grid.offset = (0, 0, z)
        grid.faces.smooth = True

    # We are done: plugging the deformed grid as the modified geometry
    grid.out()

hello_world.build()
```

The generated nodes are shown below:

<img src="docs/getting_started/images/hello_world_nodes.png" width="600" class="center">

## Declare and organize node trees

Use `@modifier()`, `@group()`, `@tool()`, `@shader_group()` or `@shader()` to
declare a builder. Call `.build()` to construct it, or call a reusable group
inside another builder to insert a Group node. Function parameters define input
sockets; `.out()` defines outputs. Related builders can be collected in a
`Package` subclass and built with `Project.build(full=True)`.

- [Modifiers, groups and tools](docs/getting_started/modifiers_groups.md)
- [Packages](docs/getting_started/packages.md)
- [Migration guide](docs/getting_started/migration.md)
- [Shaders and output targets](docs/getting_started/shaders.md)

The current guides describe the decorator API, including additions in `core_new`.
Blender 5.2.0 selects the legacy `core`; other supported builds select `core_new`.
