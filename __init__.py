""" > Scripting nodes

$ DOC toc_max_depth = 1

### Declare and build trees

- `@modifier()`, `@group()` and `@tool()` declare Geometry Nodes builders.
- `@shader()` and `@shader_group()` declare materials and shader groups.
- Call `.build()` to construct a tree, or `.build(full=True)` to rebuild its dependencies.
- Function parameters define input sockets; `.out()` defines Blender outputs.
- Call a decorated group inside another builder to insert a Group node.
- <!Package> organizes related builders in a class or registered collection.
- <!GeoNodes> and <!ShaderNodes> remain available for explicit <!Tree> contexts.
- <!Break> : exiting from a tree context can be done by raising this exception

### Create nodes

- <!Node> : base class to create any node in a tree
- <!Group> : create a <*Node Group> node
- <!G> : a different way to create a <*Node Group> node
- <!Layout> : to place nodes in a frame
- <!Panel> : to place inputs into a panel
- Specific node : <!ColorRamp>

### Libraries

- <!gnmath> : math library providing mathematical functions coming from nodes
  <*Node Math>, <*Node Vector Math> and <*Node Boolean Math>
- <!nd> (for _nodes_) : this special class exposes one method or property per node,
  especially useful for input nodes such as <*Node Index> or <*Node Position>
- <!nd> also selects shader nodes inside a ShaderNodes context

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
import bpy

pi     = np.pi
tau    = 2*np.pi
e      = np.e

from importlib import import_module as _import_module
from pathlib import Path as _Path
from ._versions import select_core as _select_core

BLENDER_VERSION = bpy.app.version
_core_name = _select_core(_Path(__file__).resolve().parent, BLENDER_VERSION)
core_module = _import_module('.' + _core_name, __name__)


__version__ = core_module.__version__
blender_version = core_module.blender_version

blender = core_module.blender
Break = core_module.Break

Signature = core_module.Signature

Socket = core_module.Socket
if hasattr(core_module, 'DEFAULT'):
    DEFAULT = core_module.DEFAULT
else:
    globals().pop('DEFAULT', None)

Input = core_module.Input
Boolean = core_module.Boolean
Float = core_module.Float
Integer = core_module.Integer
Vector = core_module.Vector
Rotation = core_module.Rotation
Matrix = core_module.Matrix
Color = core_module.Color
String = core_module.String
Texture = core_module.Texture
Collection = core_module.Collection
Object = core_module.Object
Image = core_module.Image
Material = core_module.Material
Font = core_module.Font
Menu = core_module.Menu
Geometry = core_module.Geometry
Domain = core_module.Domain
Point = core_module.Point
Vertex = core_module.Vertex
Face = core_module.Face
Edge = core_module.Edge
Corner = core_module.Corner
SplinePoint = core_module.SplinePoint
Spline = core_module.Spline
CloudPoint = core_module.CloudPoint
Instance = core_module.Instance
Layer = core_module.Layer
Mesh = core_module.Mesh
Curve = core_module.Curve
Cloud = core_module.Cloud
Instances = core_module.Instances
GreasePencil = core_module.GreasePencil
Volume = core_module.Volume
simulation = core_module.simulation
repeat = core_module.repeat

Layout = core_module.Layout
Panel = core_module.Panel
Tree = core_module.Tree
Node = core_module.Node
Group = core_module.Group
G = core_module.G
ColorRamp = core_module.ColorRamp
Closure = core_module.Closure
Bundle = core_module.Bundle

GeoNodes = core_module.GeoNodes
Package = core_module.Package
group = core_module.group
modifier = core_module.modifier
tool = core_module.tool
shader_group = core_module.shader_group
shader = core_module.shader

gnmath = core_module.gnmath
nd = core_module.nd

# Shader

if hasattr(core_module, 'snd'):
    snd = core_module.snd
else:
    globals().pop('snd', None)
Shader = core_module.Shader
VolumeShader = core_module.VolumeShader
ShaderNodes = core_module.ShaderNodes

# Register

treearrange = core_module.treearrange
treearrange.register()

print(
    f"geonodes {__version__}: Geometry Nodes with Python "
    f"for Blender version {'.'.join(map(str, blender_version))}"
)
