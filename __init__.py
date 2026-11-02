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

import bpy

COMPATIBLE_BLENDER_VERSION = (5, 2, 0)
BLENDER_VERSION = bpy.app.version

if BLENDER_VERSION == COMPATIBLE_BLENDER_VERSION:
    from . import core as core_module
else:
    try:
        from . import core_new as core_module
        print("Geonodes info: Working with new core")
    except:
        from . import core as core_module
        print("CAUTION: impossible to load 'core_new' module")


PRODUCTION = core_module.PRODUCTION
__version__ = core_module.__version__
blender_version = core_module.blender_version

if PRODUCTION:
    
    Break = core_module.Break
    blender = core_module.blender

    Signature = core_module.Signature

    Attribute = core_module.Attribute
    Socket = core_module.Socket
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
    geo_group = core_module.geo_group
    geo_modifier = core_module.geo_modifier
    shader_group = core_module.shader_group
    shader_material = core_module.shader_material

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
