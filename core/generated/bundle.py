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


class Bundle(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'BUNDLE'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Bundle
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='BUNDLE')
        return node._out

    def join(self, *bundle: Bundle):
        """ > Node <&Node Join Bundle>

        Parameters
        ----------
        bundle : Bundle, optional
            socket 'Bundle' (id: Bundle)
        

        Returns
        -------
        Bundle
        """
        node = Node('Join Bundle', {'Bundle': [self] + list(bundle)})
        return node._out

    @classmethod
    def Combine(cls, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&Node Combine Bundle>

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        define_signature : bool
            parameter `define_signature`
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        Bundle
        """
        node = Node('Combine Bundle', named_sockets, define_signature=define_signature, **sockets)
        return cls(node._out)

    def separate_bundle(self, named_sockets: dict = {}, define_signature = False, **sockets):
        """ > Node <&Node Separate Bundle>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Bundle | `self` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        define_signature : bool
            parameter `define_signature`
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        node []
        """
        node = Node('Separate Bundle', {'Bundle': self, **named_sockets}, define_signature=define_signature, **sockets)
        return node

    def get_item(self,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Get Bundle Item>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Bundle | `self` |

        Parameters
        ----------
        path : String, optional
            socket 'Path' (id: Path)
        
        remove : Boolean, optional
            socket 'Remove' (id: Remove)
        
        socket_type : Literal['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Rotation', 'Matrix', 'String', 'Menu', 'Object', 'Image', 'Geometry', 'Collection', 'Material', 'Bundle', 'Closure', 'Font']
            parameter `socket_type`
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Item
        """
        utils.check_enum_arg('Get Bundle Item', 'socket_type', socket_type, 'get_item', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'))
        utils.check_enum_arg('Get Bundle Item', 'structure_type', structure_type, 'get_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        node = Node('Get Bundle Item', {'Bundle': self, 'Path': path, 'Remove': remove}, socket_type=socket_type, structure_type=structure_type)
        self._jump(node._out)
        return node.Item

    def set_item(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Store Bundle Item>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name          | Value         |
        | --------- | ------------- | ------------- |
        | Socket    | Bundle        | `self`        |
        | Parameter | `socket_type` | `socket_type` |

        Parameters
        ----------
        path : String, optional
            socket 'Path' (id: Path)
        
        item : Float, optional
            socket 'Item' (id: Item)
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Bundle
        """
        utils.check_enum_arg('Store Bundle Item', 'structure_type', structure_type, 'set_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        socket_type = SocketType(item).class_name
        node = Node('Store Bundle Item', {'Bundle': self, 'Path': path, 'Item': item}, socket_type=socket_type, structure_type=structure_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def store_item(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Store Bundle Item>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name          | Value         |
        | --------- | ------------- | ------------- |
        | Socket    | Bundle        | `self`        |
        | Parameter | `socket_type` | `socket_type` |

        Parameters
        ----------
        path : String, optional
            socket 'Path' (id: Path)
        
        item : Float, optional
            socket 'Item' (id: Item)
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Bundle
        """
        utils.check_enum_arg('Store Bundle Item', 'structure_type', structure_type, 'store_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        socket_type = SocketType(item).class_name
        node = Node('Store Bundle Item', {'Bundle': self, 'Path': path, 'Item': item}, socket_type=socket_type, structure_type=structure_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def join_bundle(self, *bundle: Bundle):
        """ > Node <&ShaderNode Join Bundle>

        Parameters
        ----------
        bundle : Bundle, optional
            socket 'Bundle' (id: Bundle)
        

        Returns
        -------
        Bundle
        """
        node = Node('Join Bundle', {'Bundle': [self] + list(bundle)})
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

        Parameters
        ----------
        name : str, default=`Bundle`
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
        Bundle
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketBundle', name=name, tip=tip, panel=panel,
            optional_label=optional_label, hide_value=hide_value, hide_in_modifier=hide_in_modifier)

