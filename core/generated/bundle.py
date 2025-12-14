# Generated 2025-12-13 19:56:11

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


class Bundle(Socket):
    """"
    $DOC SET hidden
    """
    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'BUNDLE'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Bundle
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='BUNDLE')
        return node._out

    def join(self, *bundle: Bundle):
        """ > Node <&Node Join Bundle>

        Arguments
        ---------
        - bundle (Bundle) : socket 'Bundle' (id: Bundle)

        Returns
        -------
        - Bundle
        """
        node = Node('Join Bundle', {'Bundle': [self] + list(bundle)})
        return node._out

    @classmethod
    def Combine(cls, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&Node Combine Bundle>

        Arguments
        ---------
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - Bundle
        """
        node = Node('Combine Bundle', named_sockets, define_signature=define_signature, **sockets)
        return cls(node._out)

    def separate_bundle(self, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&Node Separate Bundle>

        Information
        -----------
        - Socket 'Bundle' : self

        Arguments
        ---------
        - define_signature (bool): parameter 'define_signature'

        Returns
        -------
        - None
        """
        node = Node('Separate Bundle', {'Bundle': self, **named_sockets}, define_signature=define_signature, **sockets)
        return node._out

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Bundle',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Bundle Input

        New <#Bundle> input with subtype 'NONE'.

        Aguments
        --------
        - name  (str = 'Bundle') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Bundle
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketBundle', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier)

