# Generated 2026-07-20 17:00:26

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

    def children(self, recursive: Boolean = None):
        """ > Node <&Node Collection Children>

        **Fixed values**

        | Kind   | Name       | Value  |
        | ------ | ---------- | ------ |
        | Socket | Collection | `self` |

        Parameters
        ----------
        recursive : Boolean, optional
            socket 'Recursive' (id: Recursive)
        

        Returns
        -------
        Collection
            peer sockets: objects_ (Object)

        """
        node = Node('Collection Children', {'Collection': self, 'Recursive': recursive})
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

    def list_length(self):
        """ > Node <&Node List Length>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | List        | `self`         |
        | Parameter | `data_type` | `'COLLECTION'` |

        Returns
        -------
        Integer
        """
        node = Node('List Length', {'List': self}, data_type='COLLECTION')
        return node._out

    def sort_list(self,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    sort_weight: Float = None):
        """ > Node <&Node Sort List>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | List          | `self`         |
        | Parameter | `socket_type` | `'COLLECTION'` |

        Parameters
        ----------
        selection : Boolean, optional
            socket 'Selection' (id: Selection)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sort_weight : Float, optional
            socket 'Sort Weight' (id: Sort Weight)
        

        Returns
        -------
        Collection
        """
        node = Node('Sort List', {'List': self, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, socket_type='COLLECTION')
        return node._out

    def filter_list(self, selection: Boolean = None):
        """ > Node <&Node Filter List>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | List          | `self`         |
        | Parameter | `socket_type` | `'COLLECTION'` |

        Parameters
        ----------
        selection : Boolean, optional
            socket 'Selection' (id: Selection)
        

        Returns
        -------
        Collection
            peer sockets: inverted_ (Collection)

        """
        node = Node('Filter List', {'List': self, 'Selection': selection}, socket_type='COLLECTION')
        return node._out

    def get_list_item(self,
                    index: Integer = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Get List Item>

        **Fixed values**

        | Kind      | Name          | Value          |
        | --------- | ------------- | -------------- |
        | Socket    | List          | `self`         |
        | Parameter | `socket_type` | `'COLLECTION'` |

        Parameters
        ----------
        index : Integer, optional
            socket 'Index' (id: Index)
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Collection
        """
        utils.check_enum_arg('Get List Item', 'structure_type', structure_type, 'get_list_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        node = Node('Get List Item', {'List': self, 'Index': index}, socket_type='COLLECTION', structure_type=structure_type)
        return node._out

    def implicit_conversion(self, socket_idname = 'NodeSocketColor'):
        """ > Node <&Node Implicit Conversion>

        **Fixed values**

        | Kind      | Name        | Value          |
        | --------- | ----------- | -------------- |
        | Socket    | Value       | `self`         |
        | Parameter | `data_type` | `'COLLECTION'` |

        Parameters
        ----------
        socket_idname : str
            parameter `socket_idname`
        

        Returns
        -------
        Collection
        """
        node = Node('Implicit Conversion', {'Value': self}, data_type='COLLECTION', socket_idname=socket_idname)
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

