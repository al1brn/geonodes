""" Scripting nodes

Scripting nodes starts by instantianting a <!Tree>, either a <!GeoNodes"Geometry nodes tree> or
a <!ShaderNodes"Shader nodes tree>:
    
``` python
with GeoNodes("Geometry Nodes"):
    pass
```

Once the current tree instantiated, nodes can be created by instancianting a <!Node> class, for instance:    

``` python
with GeoNodes("Geometry Nodes"):
    node = Node('Set Position', {'Geometry': ..., 'Selection': ..., 'Offset': ...})
    result = node.geometry
```

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
- Blender resources:
  - <!Collection>
  - <!Object>
  - <!Image>
  - <!Material>
  - <!Texture>
- And of course a <!Geometry> socket:
  - <!Mesh>
  - <!Curve>
  - <!Cloud>
  - <!Instances>
  - <!Volume>
  
``` python
geometry = Geometry()
# Create a 'Set Position' node by calling the method of Geometry
moved_geometry = geometry.set_position(...)
```

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

# ----------------------------------------------------------------------------------------------------
# Shader

from .shadernodes.shadernodes import ShaderNodes, snd
from .shadernodes.shaderclass import Shader, VolumeShader
