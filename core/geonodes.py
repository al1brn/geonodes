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
from .socket_class import Material, Image, Object, Collection, String, Menu
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
from geonodes.core import constants
from geonodes.core.scripterror import NodeError
from .treeinterface import TreeInterface

class GeoNodes(Tree):
    def __init__(self, tree_name: str, clear: bool=True, fake_user: bool=False, is_group: bool=False, prefix: str | None=None):
        """ > Geometry Nodes

        Arguments
        ---------
        - tree_name (str) : Geometry Nodes name
        - clear (bool = True) : clear the tree content
        - fake_user (bool = False) : set fake_user flag
        - is_group (bool = False) : tree is a group
        - prefix (str = None) : name prefix
        """

        super().__init__(tree_name, tree_type='GeometryNodeTree', clear=clear, fake_user=fake_user, is_group=is_group, prefix=prefix)

        self._btree.is_modifier = not is_group

    # =============================================================================================================================
    # Tool

    @classmethod
    def Tool(cls, tree_name, clear=True, fake_user=False, object_mode=True, edit_mode=False, sculpt_mode=False,
        mesh=True, curve=False, cloud=False, wait_for_click=False):
        """ > Tool Geometry Nodes

        Arguments
        ---------
        - tree_name (str) : Geometry Nodes namde
        - clear (bool = True) : clear the tree content
        - fake_user (bool = False) : set fake_user flag
        - object_mode (bool = True) : tool available in object mode
        - edit_mode (bool = False) : tool available in edit mode
        - sculpt_mode (bool = False) : tool available in sculpt mode
        - mesh (bool = True) : mesh tool
        - curve (bool = False) : curve tool
        - cloud (bool = False) : cloud tool
        - wait_for_click (bool = False) : wait for click flag

        Returns
        -------
        - GeoNodes
        """

        geonodes = cls(tree_name, clear=clear, fake_user=fake_user)

        geonodes._btree.is_tool = True

        geonodes._btree.is_mode_object = object_mode
        geonodes._btree.is_mode_edit   = edit_mode
        geonodes._btree.is_mode_sculpt = sculpt_mode

        geonodes._btree.is_type_mesh        = mesh
        geonodes._btree.is_type_curve       = curve
        geonodes._btree.is_type_point_cloud = cloud

        geonodes._btree.use_wait_for_click = wait_for_click

        return geonodes

    @property
    def is_tool(self):
        """ > Is a tool

        Returns
        -------
        - bool : True if tree is a tool
        """
        return self._btree.is_tool

    def check_node_validity(self, bnode):

        super().check_node_validity(bnode)

        if self.is_tool:
            if bnode.name in constants.MODIFIER_ONLY:
                raise NodeError(f"Node '{bnode.name}' is specific to Modifiers, if can't be used in the Tool tree '{self._btree.name}'.")
        else:
            if bnode.name in constants.TOOL_ONLY:
                raise NodeError(f"Node '{bnode.name}' is specific to Tools, it can't be used in the Modifier tree '{self._btree.name}'.")

    # =============================================================================================================================
    # End of construction

    def pop(self, clean=True):

        if self._btree.is_modifier:
            self._interface.set_in_geometry(create = False)
            self._interface.set_out_geometry()
            _ = self.output_node

        super().pop(clean=clean)


    # =============================================================================================================================
    # Geometry I/O
    # Geometry is the first socket which must be GEOMETRY

    #@property
    #def has_input_geometry(self):
    #    return self.first_io_socket_is_geometry('INPUT')

    #@property
    #def has_output_geometry(self):
    #    return self.first_io_socket_is_geometry('OUTPUT')

    def get_input_geometry(self, name=None, description=None):

        self._interface.set_in_geometry(name=name, create=True)
        return self.input_node[0]


        # OLD

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

        self._interface.set_out_geometry(name=name)
        if value is not None:
            self.link(value, self.output_node._bnode.inputs[0])

        return

        # OLD

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
