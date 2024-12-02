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

from .staticclass import StaticClass
from ..geonodes.treeclass import Tree, Node
from ..geonodes.scripterror import NodeError

class snd(StaticClass):

    @classmethod
    def sharp_face(cls, attribute_type: str ='GEOMETRY') -> Node:
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='sharp_face', attribute_type=attribute_type)

    @classmethod
    def uvmap(cls, attribute_type: str ='GEOMETRY') -> Node:
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='UVMap', attribute_type=attribute_type)

    @classmethod
    def position(cls, attribute_type: str ='GEOMETRY') -> Node:
        """ Node 'Attribute' (ShaderNodeAttribute)
        - attribute_type in ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        """
        return cls.attribute(attribute_name='position', attribute_type=attribute_type)


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
            return self.output_node

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

