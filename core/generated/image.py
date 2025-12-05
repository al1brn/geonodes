# Generated 2025-12-04 08:23:30

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
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


class Image(Socket):
    """"
    $DOC SET hidden
    """
    def info(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - node [width (Integer), height (Integer), has_alpha (Boolean), frame_count (Integer), fps (Float)]
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node

    def width(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - width
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node.width

    def height(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - height
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node.height

    def has_alpha(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - has_alpha
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node.has_alpha

    def frame_count(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - frame_count
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node.frame_count

    def fps(self, frame: Integer = None):
        """ > Node <&Node Image Info>

        Information
        -----------
        - Socket 'Image' : self

        Arguments
        ---------
        - frame (Integer) : socket 'Frame' (id: Frame)

        Returns
        -------
        - fps
        """
        node = self._cache('Image Info', {'Image': self, 'Frame': frame})
        return node.fps

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'IMAGE'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Image
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='IMAGE')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = None,
        name: str = 'Image',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default: object = None,
         ):
        """ > Image Input

        New <#Image> input with subtype 'NONE'.

        Aguments
        --------
        - value  (object = None) : Default value
        - name  (str = 'Image') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier
        - default  (object = None) : Property default_value

        Returns
        -------
        - Image
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketImage', value=value, name=name, tip=tip,
            panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default=default)

