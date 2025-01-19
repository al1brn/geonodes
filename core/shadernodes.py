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

module : shadernodes
--------------------
- ShaderNodes class

Subclass of Tree which is used to create shader trees.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12
- update :   2025/01/18 : Bug in output_node
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.1"
__blender_version__ = "4.3.0"

"""
Created on 2024/07/26

@author: alain

-----------------------------------------------------
Scripting Shader Nodes
-----------------------------------------------------

module : shadernodes
--------------------
- Implement Shader Nodes tree

classes
-------
- ShaderNodes      : Geometry Nodes tree
- nd               : Overrides static class with addition methods

functions
---------

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

from typing import Callable, Any, Iterable, List, Optional

from . import constants

from .treeclass import Tree, Node
from .scripterror import NodeError
from .treeinterface import TreeInterface

class ShaderNodes(Tree):
    def __init__(self, tree_name: str, clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: Optional[str] = None):
        """ > ShaderNodes
        """

        s = """ > Shader Nodes

        Arguments
        ---------
        - tree_name (str) : Shader Nodes name
        - clear (bool = True) : clear the tree content
        - fake_user (bool = False) : set fake_user flag
        - is_group (bool = False) : tree is a group
        - prefix (str = None) : name prefix
        """

        super().__init__(tree_name, tree_type='ShaderNodeTree', clear=clear, fake_user=fake_user, is_group=is_group, prefix=prefix)

    # =============================================================================================================================
    # Input Node

    @property
    def input_node(self) -> Node:
        if not self._is_group:
            raise NodeError(f"ShaderNodes '{self._material.name}' is not a group, it doesn't have an input node")
        return super().input_node

    # ====================================================================================================
    # Tree output

    @property
    def output_node(self) -> Node:
        if self._is_group:
            return super().output_node

        for node in self._nodes:
            if node._bnode.bl_idname ==  'ShaderNodeOutputMaterial':
                return node
        return Node('ShaderNodeOutputMaterial')

    def get_output_node(self, target: str ='ALL') -> Node:
        # target in ('ALL', 'EEVEE', 'CYCLES')

        for node in self._nodes:
            if node._bnode.bl_idname ==  'ShaderNodeOutputMaterial':
                if node._bnode.target == target:
                    return node
        return Node('ShaderNodeOutputMaterial', target=target)

    def set_surface(self, value: Any, target: str ='ALL') -> None:
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Surface': value})

    def set_volume(self, value: Any, target: str ='ALL') -> None:
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Volume': value})

    def set_displacement(self, value: Any, target: str ='ALL') -> None:
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Displacement': value})

    def set_thickness(self, value: Any, target: str ='ALL') -> None:
        node = self.get_output_node(target=target)
        node.set_input_sockets({'Thickness': value})

    @property
    def surface(self) -> None:
        raise NodeError(f"Material 'surface' is write only")

    @surface.setter
    def surface(self, value: Any) -> None:
        if isinstance(value, tuple):
            self.set_surface(value[0], target=value[1])
        else:
            self.set_surface(value)

    @property
    def volume(self) -> None:
        raise NodeError(f"Material 'volume' is write only")

    @volume.setter
    def volume(self, value: Any) -> None:
        if isinstance(value, tuple):
            self.set_volume(value[0], target=value[1])
        else:
            self.set_volume(value)

    @property
    def displacement(self) -> None:
        raise NodeError(f"Material 'displacement' is write only")

    @displacement.setter
    def displacement(self, value: Any) -> None:
        if isinstance(value, tuple):
            self.set_displacement(value[0], target=value[1])
        else:
            self.set_displacement(value)

    @property
    def thickness(self) -> None:
        raise NodeError(f"Material 'displacement' is write only")

    @thickness.setter
    def thickness(self, value: Any) -> None:
        if isinstance(value, tuple):
            self.set_thickness(value[0], target=value[1])
        else:
            self.set_thickness(value)

    def aov_output(self, name: Optional[str] =None, color: Optional[Any] =None, value: Optional[Any] =None) -> None:
        node = Node('AOV Output', {'Color': color, 'Value': value}, aov_name=name)
