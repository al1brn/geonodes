"""
This file is part of the geonodes distribution (https://github.com/al1brn/geonodes).
Copyright (c) 2025 Alain Bernard.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

$ DOC transparent

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : geonodes
-----------------
- GeoNodes class

Subclass of Tree which is used to create Geometry Nodes trees.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"

from . treeclass import Tree
from . import constants
from . scripterror import NodeError
from . treeinterface import TreeInterface

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


    def set_output_geometry(self, value, name=None):

        self._interface.set_out_geometry(name=name)
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
