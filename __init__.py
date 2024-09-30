""" > Scripting nodes

$ DOC toc_max_depth = 1

### Initialize a tree

- <!GeoNodes> and <!ShaderNodes> : scripting nodes starts by instantianting a <!Tree>
- <!Break> : exiting from a tree context can be done by raising this exception

### Create nodes

- <!Node> : base class to create any node in a tree
- <!Group> : create a <*Node Group> node
- <!GroupF> : a different way to create a <*Node Group> node
- <!Layout> : to place nodes in a frame
- <!Repeat> and <!Simulation> : create a <!Zone>

### Libraries

- <!gnmath> : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- <!nd> (for _nodes_) : this special class expses one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- <!snd> (for _shader nodes_) : same as <!nd> for shader node

### Sockets

Rather than using <!Node> class, scripting nodes is done by using <!Socket> classes:

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
from .geonodes.zones import Zone, Repeat, Simulation

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
