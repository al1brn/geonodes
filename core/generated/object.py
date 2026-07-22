# Generated 2026-07-22 07:37:34

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


class Object(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def camera_info(self):
        """ > Node <&Node Camera Info>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Camera | `self` |

        Returns
        -------
        Matrix
            peer sockets: focal_length_ (Float), sensor_ (Vector), shift_ (Vector), clip_start_ (Float), clip_end_ (Float), focus_distance_ (Float), is_orthographic_ (Boolean), orthographic_scale_ (Float)

        """
        node = Node('Camera Info', {'Camera': self})
        return node._out

    @classmethod
    def ActiveCamera(cls):
        """ > Node <&Node Active Camera>

        Returns
        -------
        Object
        """
        node = Node('Active Camera', )
        return cls(node._out)

    def info(self,
                    as_instance: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Object Info>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Object | `self` |

        Parameters
        ----------
        as_instance : Boolean, optional
            socket 'As Instance' (id: As Instance)
        
        transform_space : Literal['Original', 'Relative']
            parameter `transform_space`
        

        Returns
        -------
        Matrix
            peer sockets: location_ (Vector), rotation_ (Rotation), scale_ (Vector), geometry_ (Geometry)

        """
        utils.check_enum_arg('Object Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Object Info', {'Object': self, 'As Instance': as_instance}, transform_space=transform_space)
        return node._out

    @classmethod
    def Self(cls):
        """ > Node <&Node Self Object>

        Returns
        -------
        Object
        """
        node = Node('Self Object', )
        return cls(node._out)

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'OBJECT'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Object
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='OBJECT')
        return node._out

    def bone_info(self,
                    bone_name: String = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Bone Info>

        **Fixed values**

        | Kind   | Name     | Value  |
        | ------ | -------- | ------ |
        | Socket | Armature | `self` |

        Parameters
        ----------
        bone_name : String, optional
            socket 'Bone Name' (id: Bone Name)
        
        transform_space : Literal['Original', 'Relative']
            parameter `transform_space`
        

        Returns
        -------
        Matrix
            peer sockets: local_pose_ (Matrix), transform_pose_ (Matrix), rest_pose_ (Matrix), rest_length_ (Float), exists_ (Boolean)

        """
        utils.check_enum_arg('Bone Info', 'transform_space', transform_space, 'bone_info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Bone Info', {'Armature': self, 'Bone Name': bone_name}, transform_space=transform_space)
        return node._out

    def list_length(self):
        """ > Node <&Node List Length>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | List        | `self`     |
        | Parameter | `data_type` | `'OBJECT'` |

        Returns
        -------
        Integer
        """
        node = Node('List Length', {'List': self}, data_type='OBJECT')
        return node._out

    def sort_list(self,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    sort_weight: Float = None):
        """ > Node <&Node Sort List>

        **Fixed values**

        | Kind      | Name          | Value      |
        | --------- | ------------- | ---------- |
        | Socket    | List          | `self`     |
        | Parameter | `socket_type` | `'OBJECT'` |

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
        Object
        """
        node = Node('Sort List', {'List': self, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, socket_type='OBJECT')
        return node._out

    def filter_list(self, selection: Boolean = None):
        """ > Node <&Node Filter List>

        **Fixed values**

        | Kind      | Name          | Value      |
        | --------- | ------------- | ---------- |
        | Socket    | List          | `self`     |
        | Parameter | `socket_type` | `'OBJECT'` |

        Parameters
        ----------
        selection : Boolean, optional
            socket 'Selection' (id: Selection)
        

        Returns
        -------
        Object
            peer sockets: inverted_ (Object)

        """
        node = Node('Filter List', {'List': self, 'Selection': selection}, socket_type='OBJECT')
        return node._out

    def get_list_item(self,
                    index: Integer = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Get List Item>

        **Fixed values**

        | Kind      | Name          | Value      |
        | --------- | ------------- | ---------- |
        | Socket    | List          | `self`     |
        | Parameter | `socket_type` | `'OBJECT'` |

        Parameters
        ----------
        index : Integer, optional
            socket 'Index' (id: Index)
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Object
        """
        utils.check_enum_arg('Get List Item', 'structure_type', structure_type, 'get_list_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        node = Node('Get List Item', {'List': self, 'Index': index}, socket_type='OBJECT', structure_type=structure_type)
        return node._out

    def implicit_conversion(self, socket_idname = 'NodeSocketColor'):
        """ > Node <&Node Implicit Conversion>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'OBJECT'` |

        Parameters
        ----------
        socket_idname : str
            parameter `socket_idname`
        

        Returns
        -------
        Object
        """
        node = Node('Implicit Conversion', {'Value': self}, data_type='OBJECT', socket_idname=socket_idname)
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = None,
        name: str = 'Object',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Object Input

        New <#Object> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`None`
            Default value

        name : str, default=`Object`
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
        Object
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketObject', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

