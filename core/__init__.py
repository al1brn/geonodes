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
    from .generated import nd
    from .generated import snd
    from .generated import gnmath

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

    from .geometry_class import Geometry
    from .domain_class import Domain
    from .domains import Point, Vertex, Face, Edge, Corner, SplinePoint, Spline, CloudPoint, Instance, Layer
    from .geometries import Mesh, Curve, Cloud, Instances, GreasePencil, Volume

    from .treeclass import Layout, Panel, Break, Tree, Node, Group, GroupF, ColorRamp, G
    from .zones import Zone, Repeat, Simulation, ForEachElement

    from .geonodes import GeoNodes

    # ===== Shader

    from .sock_shader import Shader, VolumeShader
    from .shadernodes import ShaderNodes
