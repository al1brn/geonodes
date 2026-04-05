# Generated 2026-04-05 13:07:21

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


class Collection(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def info(self,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Collection Info>

        **Fixed values**

        | Kind   | Name       | Value  |
        | ------ | ---------- | ------ |
        | Socket | Collection | `self` |

        Parameters
        ----------
        separate_children : Boolean, optional
            socket 'Separate Children' (id: Separate Children)
        
        reset_children : Boolean, optional
            socket 'Reset Children' (id: Reset Children)
        
        transform_space : Literal['Original', 'Relative']
            parameter `transform_space`
        

        Returns
        -------
        Instances
        """
        utils.check_enum_arg('Collection Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = self._cache('Collection Info', {'Collection': self, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | Value       | `self`         |
        | Parameter | `data_type` | `'COLLECTION'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Collection
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='COLLECTION')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = None,
        name: str = 'Collection',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Collection Input

        New <#Collection> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`None`
            Default value

        name : str, default=`Collection`
            Input socket name

        tip : str, default=`''`
            Property description

        panel : str, default=``
            Panel name

        optional_label : bool, default=`False`
            Property optional_label

        hide_value : bool, default=`False`
            Property hide_value

        hide_in_modifier : bool, default=`False`
            Property hide_in_modifier


        Returns
        -------
        Collection
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketCollection', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

