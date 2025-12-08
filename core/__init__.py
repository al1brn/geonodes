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

PRODUCTION = True

if PRODUCTION:
    from .generated import nd
    from .generated import snd
    from .generated import gnmath

    from .socket_class import Input

    from .sock_boolean import Boolean
    from .sock_float import Float
    from .sock_integer import Integer
    from .sock_vector import Vector
    from .sock_rotation import Rotation
    from .sock_matrix import Matrix
    from .sock_color import Color
    from .sock_string import String

    from .sock_texture import Texture
    from .sock_collection import Collection
    from .sock_object import Object
    from .sock_image import Image
    from .sock_material import Material

    from .sock_menu import Menu

    from .sock_closure import Closure
    from .sock_bundle import Bundle

    from .geometry_class import Geometry
    from .domain_class import Domain
    from .domains import Point, Vertex, Face, Edge, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer
    from .geometries import Mesh, Curve, Cloud, Instances, GreasePencil, Volume

    from .utils import Break
    from .signature import Signature
    from .treeclass import Layout, Panel, Tree
    from .nodeclass import Node, Group, GroupF, ColorRamp, G
    #from .zones import Zone, Repeat, Simulation, ForEachElement

    from .geonodes import GeoNodes

    # ===== Shader

    from .sock_shader import Shader, VolumeShader
    from .shadernodes import ShaderNodes

    # ====================================================================================================
    # Create the dict socket_type -> SocketClass

    from .utils import SOCKET_CLASSES, GEOMETRY_CLASSES

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

    GEOMETRY_CLASSES['Geometry']     = Geometry
    GEOMETRY_CLASSES['Mesh']         = Mesh
    GEOMETRY_CLASSES['Curve']        = Curve
    GEOMETRY_CLASSES['Cloud']        = Cloud
    GEOMETRY_CLASSES['Instances']    = Instances
    GEOMETRY_CLASSES['GreasePencil'] = GreasePencil
    GEOMETRY_CLASSES['Volume']       = Volume
    



