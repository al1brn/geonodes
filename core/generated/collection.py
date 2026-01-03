# Generated 2026-01-02 09:45:11

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


class Collection(Socket):
    """"
    $DOC SET hidden
    """
    def info(self,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL'):
        """ > Node <&Node Collection Info>

        Information
        -----------
        - Socket 'Collection' : self

        Arguments
        ---------
        - separate_children (Boolean) : socket 'Separate Children' (id: Separate Children)
        - reset_children (Boolean) : socket 'Reset Children' (id: Reset Children)
        - transform_space (str): parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']

        Returns
        -------
        - Instances
        """
        utils.check_enum_arg('Collection Info', 'transform_space', transform_space, 'info', ('ORIGINAL', 'RELATIVE'))
        node = self._cache('Collection Info', {'Collection': self, 'Separate Children': separate_children, 'Reset Children': reset_children}, transform_space=transform_space)
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'COLLECTION'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Collection
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

        Aguments
        --------
        - value  (object = None) : Default value
        - name  (str = 'Collection') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Collection
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketCollection', default_value = defval,
            name=name, tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

