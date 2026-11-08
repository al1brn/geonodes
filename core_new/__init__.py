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

__version__ = "5.3.0"

# Backward-compatible alias. The package version is defined only by __version__.
version = __version__

from .constants import blender_version
from .common import blender, treearrange, utils

PRODUCTION = True

if PRODUCTION:
    from .environment import ModuleFacade
    gnmath = ModuleFacade('gnmath')


    from .geonodes.domains.attribute import Attribute

    from .root.socket import Socket
    from .root.input import Input

    from .root.boolean import Boolean
    from .root.float import Float
    from .root.integer import Integer
    from .root.vector import Vector
    from .root.rotation import Rotation
    from .root.matrix import Matrix
    from .root.color import Color
    from .root.string import String

    from .root.texture import Texture
    from .root.collection import Collection
    from .root.object import Object
    from .root.image import Image
    from .root.material import Material
    from .root.font import Font
    from .root.sound import Sound

    from .root.menu import Menu

    from .root.closure import Closure
    from .root.bundle import Bundle

    from .root.geometry import Geometry
    from .geonodes.domains.domain import Domain
    from .geonodes.domains import Point, Vertex, Face, Edge, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer
    from .geonodes.sockets.geometries import Mesh, Curve, Cloud, Instances, GreasePencil, Volume

    from .common.utils import Break
    from .common.signature import Signature
    from .root.tree import Layout, Panel, Tree
    from .root.node import Node, Group, ColorRamp, G
    from .root.zone import simulation, repeat

    from .geonodes.geonodes import GeoNodes

    # ===== Shader

    from .root.shader import Shader, VolumeShader
    from .shadernodes.shadernodes import ShaderNodes
    from .decorators import Package, geo_group, geo_modifier, shader_group, shader_material

    # ====================================================================================================
    # Create the dict socket_type -> SocketClass

    from .common.utils import SOCKET_CLASSES, GEOMETRY_CLASSES

    SOCKET_CLASSES[Geometry.SOCKET_TYPE]    = Geometry
    SOCKET_CLASSES[Boolean.SOCKET_TYPE]     = Boolean
    SOCKET_CLASSES[Bundle.SOCKET_TYPE]      = Bundle
    SOCKET_CLASSES[Closure.SOCKET_TYPE]     = Closure
    SOCKET_CLASSES[Collection.SOCKET_TYPE]  = Collection
    SOCKET_CLASSES[Color.SOCKET_TYPE]       = Color
    SOCKET_CLASSES[Float.SOCKET_TYPE]       = Float
    SOCKET_CLASSES[Image.SOCKET_TYPE]       = Image
    SOCKET_CLASSES[Integer.SOCKET_TYPE]     = Integer
    SOCKET_CLASSES[Material.SOCKET_TYPE]    = Material
    SOCKET_CLASSES[Matrix.SOCKET_TYPE]      = Matrix
    SOCKET_CLASSES[Menu.SOCKET_TYPE]        = Menu
    SOCKET_CLASSES[Object.SOCKET_TYPE]      = Object
    SOCKET_CLASSES[Rotation.SOCKET_TYPE]    = Rotation
    SOCKET_CLASSES[Shader.SOCKET_TYPE]      = Shader
    SOCKET_CLASSES[String.SOCKET_TYPE]      = String
    SOCKET_CLASSES[Vector.SOCKET_TYPE]      = Vector
    SOCKET_CLASSES[Font.SOCKET_TYPE]        = Font
    SOCKET_CLASSES[Sound.SOCKET_TYPE]       = Sound

    GEOMETRY_CLASSES['Geometry']     = Geometry
    GEOMETRY_CLASSES['Mesh']         = Mesh
    GEOMETRY_CLASSES['Curve']        = Curve
    GEOMETRY_CLASSES['Cloud']        = Cloud
    GEOMETRY_CLASSES['Instances']    = Instances
    GEOMETRY_CLASSES['GreasePencil'] = GreasePencil
    GEOMETRY_CLASSES['Volume']       = Volume
    



# Concrete classes are loaded after all shared roots and registries exist.
from . import environment as _environment
for _name, _value in list(globals().items()):
    if isinstance(_value, _environment.EnvironmentType) and _name not in ("Socket", "Domain"):
        _environment.ROOTS[_name] = _value
nd = ModuleFacade('static_nd', 'nd')
_environment.READY = True
