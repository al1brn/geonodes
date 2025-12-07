# Generated 2025-12-07 10:17:11

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


class Object(Socket):
    """"
    $DOC SET hidden
    """
    def camera_info(self):
        """ > Node <&Node Camera Info>

        Information
        -----------
        - Socket 'Camera' : self

        Returns
        -------
        - node [projection_matrix (Matrix), focal_length (Float), sensor (Vector), shift (Vector), clip_start (Float), clip_end (Float), focus_distance (Float), is_orthographic (Boolean), orthographic_scale (Float)]
        """
        node = Node('Camera Info', {'Camera': self})
        return node

    @classmethod
    def ActiveCamera(cls):
        """ > Node <&Node Active Camera>

        Returns
        -------
        - Object
        """
        node = Node('Active Camera', )
        return cls(node._out)

    def info(self,
                    as_instance: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Object Info>

        Information
        -----------
        - Socket 'Object' : self

        Arguments
        ---------
        - as_instance (Boolean) : socket 'As Instance' (id: As Instance)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - node [transform (Matrix), location (Vector), rotation (Rotation), scale (Vector), geometry (Geometry)]
        """
        utils.check_enum_arg('Object Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = Node('Object Info', {'Object': self, 'As Instance': as_instance}, transform_space=transform_space)
        return node

    @classmethod
    def Self(cls):
        """ > Node <&Node Self Object>

        Returns
        -------
        - Object
        """
        node = Node('Self Object', )
        return cls(node._out)

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'OBJECT'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Object
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='OBJECT')
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

        Aguments
        --------
        - value  (object = None) : Default value
        - name  (str = 'Object') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Object
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketObject', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

