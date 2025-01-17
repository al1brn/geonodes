""" > Scripting nodes

$ DOC toc_max_depth = 1

### Initialize a tree

- <!GeoNodes> and <!ShaderNodes> : scripting nodes starts by instantianting a <!Tree>
- <!Break> : exiting from a tree context can be done by raising this exception

### Create nodes

- <!Node> : base class to create any node in a tree
- <!Group> : create a <*Node Group> node
- <!G> : a different way to create a <*Node Group> node
- <!Layout> : to place nodes in a frame
- <!Panel> : to place inputs into a panel
- <!Repeat>, <!Simulation> and <!ForEachElement>: create a <!Zone>
- Specific node : <!ColorRamp>

### Libraries

- <!gnmath> : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- <!nd> (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- <!snd> (for _shader nodes_) : same as <!nd> for shader node

### Sockets

Rather than using <!Node> class, scripting nodes is done by using <!Socket> classes:

- Data sockets:
  - <!Attribute"Attributes>:
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
  - <!GreasePencil>
  - <!Cloud>
  - <!Instances>
  - <!Volume>
- Shaders specific:
  - <!Shader>
  - <!VolumeShader>

#### Domains

Geometries have specific <!Domain>:
- <!Mesh> :
  - <!Vertex> : property <!Mesh#points>
  - <!Edge> : property <!Mesh#edges>
  - <!Face> : property <!Mesh#faces>
  - <!Corner> : property <!Mesh#corners>
- <!Curve> :
  - <!SplinePoint> : property <!Curve#points>
  - <!Spline> : property <!Curve#splines>
- <!GreasePencil> :
  - <!Layer> : property <!GreasePencil#layers>
- <!Cloud> :
  - <!CloudPoint> : property <!Cloud#points>
- <!Instances> :
  - <!Instance> : property <!Instances#insts>

#### Demos
- Of course, start with <!demos#helloworld"Hello World>

#### Cross reference

- <!Cross Reference> : to see how each Geometry Node can be scripted
- <!Shader Cross Reference> : to see how each Shader Node can be scripted
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


if True:
    from .core import Boolean, Float, Integer, Vector, Rotation, Matrix, Color, String
    from .core import Texture, Collection, Object, Image, Material
    from .core import Menu
    from .core import Geometry, Domain
    from .core import Point, Vertex, Face, Edge, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer
    from .core import Mesh, Curve, Cloud, Instances, GreasePencil, Volume

    from .core import Layout, Panel, Break, Tree, Node, Group, GroupF, G, ColorRamp
    from .core import Zone, Repeat, Simulation, ForEachElement

    from .core import GeoNodes

    from .core import gnmath, nd

    from .core.pyswitch import If, Else, Elif


# ----------------------------------------------------------------------------------------------------
# Shader

if True:
    from .core import snd, Shader, VolumeShader, ShaderNodes

# ----------------------------------------------------------------------------------------------------
# Register

if True:
    from .core import treearrange
    treearrange.register()
