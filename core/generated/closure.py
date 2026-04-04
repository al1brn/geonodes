# Generated 2026-04-04 12:37:35

from __future__ import annotations
from .. sockettype import SocketType
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
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Closure(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Value       | `self`      |
        | Parameter | `data_type` | `'CLOSURE'` |

        Parameters
        ---------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Closure
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='CLOSURE')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Closure',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Closure Input

        New <#Closure> input with subtype 'NONE'.

        Aguments
        --------
        - name  (str = 'Closure') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Closure
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketClosure', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier)

