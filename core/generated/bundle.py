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

    def list_length(self):
        """ > Node <&Node List Length>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | List        | `self`     |
        | Parameter | `data_type` | `'BUNDLE'` |

        Returns
        -------
        Integer
        """
        node = Node('List Length', {'List': self}, data_type='BUNDLE')
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
        | Parameter | `socket_type` | `'BUNDLE'` |

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
        Bundle
        """
        node = Node('Sort List', {'List': self, 'Selection': selection, 'Group ID': group_id, 'Sort Weight': sort_weight}, socket_type='BUNDLE')
        return node._out

    def filter_list(self, selection: Boolean = None):
        """ > Node <&Node Filter List>

        **Fixed values**

        | Kind      | Name          | Value      |
        | --------- | ------------- | ---------- |
        | Socket    | List          | `self`     |
        | Parameter | `socket_type` | `'BUNDLE'` |

        Parameters
        ----------
        selection : Boolean, optional
            socket 'Selection' (id: Selection)
        

        Returns
        -------
        Bundle
            peer sockets: inverted_ (Bundle)

        """
        node = Node('Filter List', {'List': self, 'Selection': selection}, socket_type='BUNDLE')
        return node._out

    def get_list_item(self,
                    index: Integer = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO'):
        """ > Node <&Node Get List Item>

        **Fixed values**

        | Kind      | Name          | Value      |
        | --------- | ------------- | ---------- |
        | Socket    | List          | `self`     |
        | Parameter | `socket_type` | `'BUNDLE'` |

        Parameters
        ----------
        index : Integer, optional
            socket 'Index' (id: Index)
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Bundle
        """
        utils.check_enum_arg('Get List Item', 'structure_type', structure_type, 'get_list_item', ('AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'))
        node = Node('Get List Item', {'List': self, 'Index': index}, socket_type='BUNDLE', structure_type=structure_type)
        return node._out

    def get_item(self,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SOUND'] = 'FLOAT',
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
        
        socket_type : Literal['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Rotation', 'Matrix', 'String', 'Menu', 'Object', 'Image', 'Geometry', 'Collection', 'Material', 'Bundle', 'Closure', 'Font', 'Sound']
            parameter `socket_type`
        
        structure_type : Literal['Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single']
            parameter `structure_type`
        

        Returns
        -------
        Item
        """
        utils.check_enum_arg('Get Bundle Item', 'socket_type', socket_type, 'get_item', ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SOUND'))
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

    def xpbd_solver(self,
                    delta_time: Float = None,
                    filter: String = None,
                    simulation_to_world: Matrix = None,
                    substeps: Integer = None,
                    constraint_iterations: Integer = None,
                    solver_path: String = None,
                    begin: Float = None,
                    end: Float = None):
        """ > Node <&Node XPBD Solver>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | World | `self` |

        Parameters
        ----------
        delta_time : Float, optional
            socket 'Delta Time' (id: Delta Time)
        
        filter : String, optional
            socket 'Filter' (id: Filter)
        
        simulation_to_world : Matrix, optional
            socket 'Simulation to World' (id: Simulation to World)
        
        substeps : Integer, optional
            socket 'Substeps' (id: Substeps)
        
        constraint_iterations : Integer, optional
            socket 'Constraint Iterations' (id: Constraint Iterations)
        
        solver_path : String, optional
            socket 'Solver Path' (id: Solver Path)
        
        begin : Float, optional
            socket 'Begin' (id: Begin)
        
        end : Float, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Bundle
        """
        node = Node('XPBD Solver', {'World': self, 'Delta Time': delta_time, 'Filter': filter, 'Simulation to World': simulation_to_world, 'Substeps': substeps, 'Constraint Iterations': constraint_iterations, 'Solver Path': solver_path, 'Begin': begin, 'End': end})
        return node._out

    def get_nested_paths(self,
                    mode: Literal['All', 'Bundle Type', 'Data Type'] = None,
                    pattern_mode: Literal['Exact', 'Wildcard'] = None,
                    bundle_type: String = None,
                    data_type: Literal['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Rotation', 'Matrix', 'String', 'Menu', 'Object', 'Image', 'Geometry', 'Collection', 'Material', 'Bundle', 'Closure', 'Font', 'Sound'] = None):
        """ > Node <&Node Get Nested Bundle Paths>

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Bundle | `self` |

        Parameters
        ----------
        mode : menu='All', optional
            ('All', 'Bundle Type', 'Data Type')
        
        pattern_mode : menu='Exact', optional
            ('Exact', 'Wildcard')
        
        bundle_type : String, optional
            socket 'Bundle Type' (id: Bundle Type)
        
        data_type : menu='Float', optional
            ('Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Rotation', 'Matrix', 'String', 'Menu', 'Object', 'Image', 'Geometry', 'Collection', 'Material', 'Bundle', 'Closure', 'Font', 'Sound')
        

        Returns
        -------
        String
        """
        node = Node('Get Nested Bundle Paths', {'Bundle': self, 'Mode': mode, 'Pattern Mode': pattern_mode, 'Bundle Type': bundle_type, 'Data Type': data_type})
        return node._out

    def implicit_conversion(self, socket_idname = 'NodeSocketColor'):
        """ > Node <&Node Implicit Conversion>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Value       | `self`     |
        | Parameter | `data_type` | `'BUNDLE'` |

        Parameters
        ----------
        socket_idname : str
            parameter `socket_idname`
        

        Returns
        -------
        Bundle
        """
        node = Node('Implicit Conversion', {'Value': self}, data_type='BUNDLE', socket_idname=socket_idname)
        return node._out

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

