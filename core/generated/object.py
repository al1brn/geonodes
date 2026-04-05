# Generated 2026-04-05 13:21:02

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
            peer sockets: local_pose_ (Matrix), transform_pose_ (Matrix), rest_pose_ (Matrix), rest_length_ (Float)

        """
        utils.check_enum_arg('Bone Info', 'transform_space', transform_space, 'bone_info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Bone Info', {'Armature': self, 'Bone Name': bone_name}, transform_space=transform_space)
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

