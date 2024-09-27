""" > Scripting nodes

$ DOC toc_max_depth = 1

### Tree

Scripting nodes starts by instantianting a <!Tree>, either a <!GeoNodes"Geometry nodes tree> or
a <!ShaderNodes"Shader nodes tree>:

``` python
with GeoNodes("Geometry Nodes"):
    pass
```

Exiting from a tree context can be done by raising the <!Break> exception.

### Node class

Once the current tree instantiated, nodes can be created by instancianting a <!Node> class, for instance:

``` python
with GeoNodes("Geometry Nodes"):
    node = Node('Set Position', {'Geometry': ..., 'Selection': ..., 'Offset': ...})
    result = node.geometry
```

#### Special nodes

<!Group> is used to call a group. <!GroupF> does the same by exposing the **snake_name** name of
the called group.

Use <!Layout> class to group nodes in a Layout:

``` python
with Layout("This a description"):
    # Nodes created in the context blocks are placed in the layout
    pass
```

#### Zones

Zones are create using <!Repeat> and <!Simulation>.

#### nd et snd classes

The special class <!nd> (for _nodes_) exposes all nodes by the **snake_case** name.

Use <!snd> (for _shader nodes_) when scripting <!ShaderNodes>.

### Sockets

A better and more pythonistic way to script nodes, is to use a <!Socket> subclass among:

- Data sockets:
  - <!Boolean>
  - <!Integer>
  - <!Float>
  - <!Color>
  - <!Vector>
  - <!Rotation>
  - <!Matrix>
  - <!String>
  - <!Menu>
- Blender resources:
  - <!Collection>
  - <!Object>
  - <!Image>
  - <!Material>
  - <!Texture>
- <!Geometry> socket:
  - <!Mesh>
  - <!Curve>
  - <!Cloud>
  - <!Instances>
  - <!Volume>
- Shaders specific:
  - <!Shader>
  - <!VolumeShader>

``` python
geometry = Geometry()
# Create a 'Set Position' node by calling the method of Geometry
moved_geometry = geometry.set_position(...)
```

#### Domains

Geometries have specific <!Domain>:
- <!Vertex> (<!Mesh> <!Mesh#points> property)
- <!Edge>  (<!Mesh> <!Mesh#edges> property)
- <!Face>  (<!Mesh> <!Mesh#faces> property)
- <!Corner>  (<!Mesh> <!Mesh#corners> property)
- <!SplinePoint> (<!Curve> <!Curve#points> property)
- <!Spline> (<!Curve> <!Curve#splines> property)
- <!CloudPoint> (<!Cloud> <!Cloud#points> property)
- <!Instance> (<!Instances> <!Instances#insts> property)

> [!NOTE]
> Domains are never instancied directly but by their geometry.

``` python
# A Mesh is instantiated with four domains
cube = Mesh.Cube()
# Extrusion of faces
extruded_cube = cube.faces.extrude()
```

#### maths

The module <!gnmath> provides math functions and be uses as standard python **math** library.
"""

import numpy as np

pi     = np.pi
tau    = 2*np.pi
halfpi = np.pi/2
d30    = np.pi/6
d45    = np.pi/4
d60    = np.pi/3
d90    = halfpi
d180   = pi
d270   = np.pi*1.5
d360   = tau
e      = np.e

from .geonodes.treeclass import Layout, Break, Tree, Node, Group, GroupF
from .geonodes.zones import Repeat, Simulation

from .geonodes.geonodes import GeoNodes

from .geonodes.staticclass import nd
from .geonodes import gnmath

from .geonodes.socketclass import Socket, String, Material, Image, Object, Collection, Menu

from .geonodes.booleanclass import Boolean
from .geonodes.colorclass import Color
from .geonodes.floatclass import Integer, Float
from .geonodes.textures import Texture
from .geonodes.vectorclass import Vector, Rotation, Matrix
from .geonodes.geometryclass import Geometry, Mesh, Curve, Cloud, Instances, Volume
from .geonodes.geometryclass import Domain, Vertex, Edge, Face, Corner, SplinePoint, Spline, CloudPoint, Instance


# ----------------------------------------------------------------------------------------------------
# Shader

from .shadernodes.shadernodes import ShaderNodes, snd
from .shadernodes.shaderclass import Shader, VolumeShader
