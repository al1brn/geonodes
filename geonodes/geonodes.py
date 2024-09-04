"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : geonodes
-----------------
- Implement Geometry Nodes tree

classes
-------
- GeoNodes      : Geometry Nodes tree

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""


""""
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


from .treeclass import Break, Layout, Node, Group, GroupF, Tree
from .floatclass import Float, Integer
from .socketclass import Material, Image, Object, Collection, String, Menu
from .booleanclass import Boolean
from .vectorclass import Vector, Rotation, Matrix
from .colorclass import Color
from .geometryclass import Geometry, Mesh, Curve, Cloud, Instances, Volume
from .zones import Repeat, Simulation
from .textures import Texture
from . import gnmath
from . import macros
from .staticclass_gn import nd
"""

from .treeclass import Tree


class GeoNodes(Tree):
    def __init__(self, tree_name, clear=True, fake_user=False, is_group=False, prefix=None):

        super().__init__(tree_name, tree_type='GeometryNodeTree', clear=clear, fake_user=fake_user, is_group=is_group, prefix=prefix)

        self._btree.is_modifier = not is_group

    # =============================================================================================================================
    # Geometry I/O
    # Geometry is the first socket which must be GEOMETRY

    @property
    def has_input_geometry(self):
        return self.first_io_socket_is_geometry('INPUT')

    @property
    def has_output_geometry(self):
        return self.first_io_socket_is_geometry('OUTPUT')

    def get_input_geometry(self, name=None, description=None):

        io_socket = self.io_socket_exists('NodeSocketGeometry', 'INPUT')
        if io_socket is None:
            if name is None:
                name = 'Geometry'
            io_socket = self.new_io_socket('NodeSocketGeometry', 'INPUT', name)
            if description is not None:
                io_socket.description = description

        # ----- As the first

        self._btree.interface.move(io_socket, 0)

        return self.input_node[0]

    def set_output_geometry(self, value, name=None):

        if self.has_output_geometry:
            io_socket = self.io_socket_exists('NodeSocketGeometry', 'INPUT')

        else:
            if name is None:
                name = utils.get_socket_type(value).title()

            io_socket = self.new_io_socket('NodeSocketGeometry', 'OUTPUT', name)

            # ----- As the first

            self._btree.interface.move(io_socket, 0)

        if value is not None:
            self.link(value, self.output_node._bnode.inputs[0])

    # =============================================================================================================================
    # Input and output geometry

    @property
    def geometry(self):
        return self.get_input_geometry()

    @geometry.setter
    def geometry(self, value):
        self.set_output_geometry(value)
