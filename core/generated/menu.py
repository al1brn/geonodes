# Generated 2025-12-08 08:30:17

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Menu(Socket):
    """"
    $DOC SET hidden
    """
    def menu_switch(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Menu Switch>

        Information
        -----------
        - Socket 'Menu' : self
        - Parameter 'data_type' : depending on 'a' type

        Returns
        -------
        - Geometry [a_ (Boolean), b_ (Boolean)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeMenuSwitch', a)
        node = Node('Menu Switch', data_type=data_type)
        node._bnode.enum_items.clear()
        node.menu = menu
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'MENU'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Menu
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='MENU')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = None,
        name: str = 'Menu',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        expanded: bool = False,
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Menu Input

        New <#Menu> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = None) : Default value
        - name  (str = 'Menu') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - expanded  (bool = False) : Property menu_expanded
        - shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

        Returns
        -------
        - Menu
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketMenu', default_value = defval, name=name,
            tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, expanded=expanded, shape=shape)

