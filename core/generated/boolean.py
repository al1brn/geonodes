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


class Boolean(Socket):

    __slots__ = Socket.__slots__

    """"
    $DOC SET hidden
    """
    def band(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Boolean     | `self`  |
        | Parameter | `operation` | `'AND'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='AND')
        return node._out

    def bor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value  |
        | --------- | ----------- | ------ |
        | Socket    | Boolean     | `self` |
        | Parameter | `operation` | `'OR'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='OR')
        return node._out

    def bnot(self):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Boolean     | `self`  |
        | Parameter | `operation` | `'NOT'` |

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self}, operation='NOT')
        return node._out

    def not_and(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Boolean     | `self`   |
        | Parameter | `operation` | `'NAND'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NAND')
        return node._out

    def nor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Boolean     | `self`  |
        | Parameter | `operation` | `'NOR'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NOR')
        return node._out

    def xnor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value    |
        | --------- | ----------- | -------- |
        | Socket    | Boolean     | `self`   |
        | Parameter | `operation` | `'XNOR'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='XNOR')
        return node._out

    def xor(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value   |
        | --------- | ----------- | ------- |
        | Socket    | Boolean     | `self`  |
        | Parameter | `operation` | `'XOR'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='XOR')
        return node._out

    def imply(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Boolean     | `self`    |
        | Parameter | `operation` | `'IMPLY'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='IMPLY')
        return node._out

    def nimply(self, boolean: Boolean = None):
        """ > Node <&Node Boolean Math>

        **Fixed values**

        | Kind      | Name        | Value      |
        | --------- | ----------- | ---------- |
        | Socket    | Boolean     | `self`     |
        | Parameter | `operation` | `'NIMPLY'` |

        Parameters
        ----------
        boolean : Boolean, optional
            socket 'Boolean' (id: Boolean_001)
        

        Returns
        -------
        Boolean
        """
        node = Node('Boolean Math', {'Boolean': self, 'Boolean_001': boolean}, operation='NIMPLY')
        return node._out

    @classmethod
    def Random(cls, probability: Float = None, id: Integer = None, seed: Integer = None):
        """ > Node <&Node Random Value>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        probability : Float, optional
            socket 'Probability' (id: Probability)
        
        id : Integer, optional
            socket 'ID' (id: ID)
        
        seed : Integer, optional
            socket 'Seed' (id: Seed)
        

        Returns
        -------
        Boolean
        """
        node = Node('Random Value', {'Probability': probability, 'ID': id, 'Seed': seed}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def Named(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Boolean
        """
        node = Node('Named Attribute', {'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @classmethod
    def NamedAttribute(cls, name: String = None):
        """ > Node <&Node Named Attribute>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        

        Returns
        -------
        Boolean
        """
        node = Node('Named Attribute', {'Name': name}, data_type='BOOLEAN')
        return cls(node._out)

    @utils.classproperty
    def is_viewport(cls):
        """ > Node <&Node Is Viewport>

        Returns
        -------
        Boolean
        """
        node = Node('Is Viewport', )
        return node._out

    def uv_unwrap(self,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None):
        """ > Node <&Node UV Unwrap>

        **Fixed values**

        | Kind   | Name      | Value  |
        | ------ | --------- | ------ |
        | Socket | Selection | `self` |

        Parameters
        ----------
        seam : Boolean, optional
            socket 'Seam' (id: Seam)
        
        margin : Float, optional
            socket 'Margin' (id: Margin)
        
        fill_holes : Boolean, optional
            socket 'Fill Holes' (id: Fill Holes)
        
        method : menu='Angle Based', optional
            ('Angle Based', 'Conformal', 'Minimum Stretch')
        
        iterations : Integer, optional
            socket 'Iterations' (id: Iterations)
        
        no_flip : Boolean, optional
            socket 'No Flip' (id: No Flip)
        

        Returns
        -------
        Vector
        """
        node = Node('UV Unwrap', {'Selection': self, 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes, 'Method': method, 'Iterations': iterations, 'No Flip': no_flip})
        return node._out

    def error(self, message: String = None):
        """ > Node <&Node Warning>

        **Fixed values**

        | Kind      | Name           | Value     |
        | --------- | -------------- | --------- |
        | Socket    | Show           | `self`    |
        | Parameter | `warning_type` | `'ERROR'` |

        Parameters
        ----------
        message : String, optional
            socket 'Message' (id: Message)
        

        Returns
        -------
        Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='ERROR')
        return node._out

    def warning(self, message: String = None):
        """ > Node <&Node Warning>

        **Fixed values**

        | Kind      | Name           | Value       |
        | --------- | -------------- | ----------- |
        | Socket    | Show           | `self`      |
        | Parameter | `warning_type` | `'WARNING'` |

        Parameters
        ----------
        message : String, optional
            socket 'Message' (id: Message)
        

        Returns
        -------
        Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='WARNING')
        return node._out

    def info(self, message: String = None):
        """ > Node <&Node Warning>

        **Fixed values**

        | Kind      | Name           | Value    |
        | --------- | -------------- | -------- |
        | Socket    | Show           | `self`   |
        | Parameter | `warning_type` | `'INFO'` |

        Parameters
        ----------
        message : String, optional
            socket 'Message' (id: Message)
        

        Returns
        -------
        Boolean
        """
        node = Node('Warning', {'Show': self, 'Message': message}, warning_type='INFO')
        return node._out

    def sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None):
        """ > Node <&Node Sample Grid>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        interpolation : menu='Trilinear', optional
            ('Nearest Neighbor', 'Trilinear', 'Triquadratic')
        

        Returns
        -------
        Boolean
        """
        node = Node('Sample Grid', {'Grid': self, 'Position': position, 'Interpolation': interpolation}, data_type='BOOLEAN')
        return node._out

    def sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None):
        """ > Node <&Node Sample Grid Index>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        x : Integer, optional
            socket 'X' (id: X)
        
        y : Integer, optional
            socket 'Y' (id: Y)
        
        z : Integer, optional
            socket 'Z' (id: Z)
        

        Returns
        -------
        Boolean
        """
        node = Node('Sample Grid Index', {'Grid': self, 'X': x, 'Y': y, 'Z': z}, data_type='BOOLEAN')
        return node._out

    def field_to_grid(self, named_sockets: dict = {}, **sockets):
        """ > Node <&Node Field to Grid>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Topology    | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        sockets : dict, default={}
            Socket created with python name attributes

        Returns
        -------
        None
        """
        node = Node('Field to Grid', {'Topology': self, **named_sockets}, data_type='BOOLEAN', **sockets)
        return node._out

    def prune_grid(self, mode: Literal['Inactive', 'Threshold', 'SDF'] = None):
        """ > Node <&Node Prune Grid>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        mode : menu='Threshold', optional
            ('Inactive', 'Threshold', 'SDF')
        

        Returns
        -------
        Boolean
        """
        node = Node('Prune Grid', {'Grid': self, 'Mode': mode}, data_type='BOOLEAN')
        return node._out

    def voxelize_grid(self):
        """ > Node <&Node Voxelize Grid>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Returns
        -------
        Boolean
        """
        node = Node('Voxelize Grid', {'Grid': self}, data_type='BOOLEAN')
        return node._out

    @classmethod
    def voxel_index(cls):
        """ > Node <&Node Voxel Index>

        Returns
        -------
        Integer
            peer sockets: y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_x_ (Integer), extent_y_ (Integer), extent_z_ (Integer)

        """
        node = Node('Voxel Index', )
        return node._out

    def set_grid_background(self, background: Boolean = None, update_inactive: Boolean = None):
        """ > Node <&Node Set Grid Background>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        background : Boolean, optional
            socket 'Background' (id: Background)
        
        update_inactive : Boolean, optional
            socket 'Update Inactive' (id: Update Inactive)
        

        Returns
        -------
        Boolean
        """
        node = Node('Set Grid Background', {'Grid': self, 'Background': background, 'Update Inactive': update_inactive}, data_type='BOOLEAN')
        return node._out

    def set_grid_transform(self, transform: Matrix = None):
        """ > Node <&Node Set Grid Transform>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        transform : Matrix, optional
            socket 'Transform' (id: Transform)
        

        Returns
        -------
        Boolean
            peer sockets: grid_ (Boolean)

        """
        node = Node('Set Grid Transform', {'Grid': self, 'Transform': transform}, data_type='BOOLEAN')
        return node._out

    def grid_info(self):
        """ > Node <&Node Grid Info>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Returns
        -------
        Matrix
            peer sockets: background_value_ (Boolean)

        """
        node = Node('Grid Info', {'Grid': self}, data_type='BOOLEAN')
        return node._out

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Value       | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        enable : Boolean, optional
            socket 'Enable' (id: Enable)
        

        Returns
        -------
        Boolean
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='BOOLEAN')
        return node._out

    @classmethod
    def CubeGridTopology(cls,
                    bounds_min: Vector = None,
                    bounds_max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None):
        """ > Node <&Node Cube Grid Topology>

        Parameters
        ----------
        bounds_min : Vector, optional
            socket 'Bounds Min' (id: Bounds Min)
        
        bounds_max : Vector, optional
            socket 'Bounds Max' (id: Bounds Max)
        
        resolution_x : Integer, optional
            socket 'Resolution X' (id: Resolution X)
        
        resolution_y : Integer, optional
            socket 'Resolution Y' (id: Resolution Y)
        
        resolution_z : Integer, optional
            socket 'Resolution Z' (id: Resolution Z)
        
        min_x : Integer, optional
            socket 'Min X' (id: Min X)
        
        min_y : Integer, optional
            socket 'Min Y' (id: Min Y)
        
        min_z : Integer, optional
            socket 'Min Z' (id: Min Z)
        

        Returns
        -------
        Boolean
        """
        node = Node('Cube Grid Topology', {'Bounds Min': bounds_min, 'Bounds Max': bounds_max, 'Resolution X': resolution_x, 'Resolution Y': resolution_y, 'Resolution Z': resolution_z, 'Min X': min_x, 'Min Y': min_y, 'Min Z': min_z})
        return cls(node._out)

    def clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None):
        """ > Node <&Node Clip Grid>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        min_x : Integer, optional
            socket 'Min X' (id: Min X)
        
        min_y : Integer, optional
            socket 'Min Y' (id: Min Y)
        
        min_z : Integer, optional
            socket 'Min Z' (id: Min Z)
        
        max_x : Integer, optional
            socket 'Max X' (id: Max X)
        
        max_y : Integer, optional
            socket 'Max Y' (id: Max Y)
        
        max_z : Integer, optional
            socket 'Max Z' (id: Max Z)
        

        Returns
        -------
        Boolean
        """
        node = Node('Clip Grid', {'Grid': self, 'Min X': min_x, 'Min Y': min_y, 'Min Z': min_z, 'Max X': max_x, 'Max Y': max_y, 'Max Z': max_z}, data_type='BOOLEAN')
        return node._out

    def grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None):
        """ > Node <&Node Grid Dilate & Erode>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Parameters
        ----------
        connectivity : menu='Face', optional
            ('Face', 'Edge', 'Vertex')
        
        tiles : menu='Preserve', optional
            ('Ignore', 'Expand', 'Preserve')
        
        steps : Integer, optional
            socket 'Steps' (id: Steps)
        

        Returns
        -------
        Boolean
        """
        node = Node('Grid Dilate & Erode', {'Grid': self, 'Connectivity': connectivity, 'Tiles': tiles, 'Steps': steps}, data_type='BOOLEAN')
        return node._out

    def grid_to_points(self):
        """ > Node <&Node Grid to Points>

        **Fixed values**

        | Kind      | Name        | Value       |
        | --------- | ----------- | ----------- |
        | Socket    | Grid        | `self`      |
        | Parameter | `data_type` | `'BOOLEAN'` |

        Returns
        -------
        Cloud
            peer sockets: value_ (Boolean), x_ (Integer), y_ (Integer), z_ (Integer), is_tile_ (Boolean), extent_ (Integer)

        """
        node = Node('Grid to Points', {'Grid': self}, data_type='BOOLEAN')
        return node._out

    @classmethod
    def _create_input_socket(cls,
        value: object = False,
        name: str = 'Boolean',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
        default_attribute: str = '',
        layer_selection: bool = False,
        shape: Literal['AUTO', 'SINGLE'] = 'AUTO',
         ):
        """ > Boolean Input

        New <#Boolean> input with subtype 'NONE'.

        Parameters
        ----------
        value : object, default=`False`
            Default value

        name : str, default=`Boolean`
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

        default_attribute : str, default=`''`
            Property default_attribute_name

        layer_selection : bool, default=`False`
            Property layer_selection_field

        shape : str, default=`'AUTO'`
            Property structure_type in ('AUTO', 'SINGLE')


        Returns
        -------
        Boolean
        """
        from ..treeclass import Tree

        defval = utils.python_value_for_socket(value, cls.SOCKET_TYPE)

        return Tree.current_tree().create_input_socket('NodeSocketBool', default_value = defval, name=name,
            tip=tip, panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier, default_attribute=default_attribute,
            layer_selection=layer_selection, shape=shape)

