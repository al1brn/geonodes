# Generated 2026-04-05 12:44:34

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


class Corner:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        value : Float | Integer | Vector | Matrix, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        

        Returns
        -------
        Float
            peer sockets: trailing_ (Float), total_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeAccumulateField')
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='CORNER')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        **Fixed values**

        | Kind      | Name        | Value                 |
        | --------- | ----------- | --------------------- |
        | Socket    | Geometry    | `self`                |
        | Socket    | Selection   | `self[selection]`     |
        | Parameter | `data_type` | from `attribute` type |
        | Parameter | `domain`    | `'CORNER'`            |

        Parameters
        ----------
        attribute : Float | Vector, optional
            socket 'Attribute' (id: Attribute)
        

        Returns
        -------
        Float
            peer sockets: median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(attribute, 'GeometryNodeAttributeStatistic')
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: median_ (Float)

        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAverage')
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Integer | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: max_ (Float)

        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldMinAndMax')
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: variance_ (Float)

        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldVariance')
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def edges(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
            peer sockets: previous_edge_index_ (Integer)

        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def next_edge_index(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        next_edge_index
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node.next_edge_index

    @classmethod
    def previous_edge_index(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        previous_edge_index
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node.previous_edge_index

    @classmethod
    def face(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
            peer sockets: index_in_face_ (Integer)

        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def face_index(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        face_index
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node.face_index

    @classmethod
    def index_in_face(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        index_in_face
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node.index_in_face

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAtIndex')
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldOnDomain')
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='CORNER')
        return node._out

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'CORNERS'`       |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='CORNERS')
        return node._out

    @classmethod
    def offset_in_face(cls, corner_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Corner in Face>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        
        offset : Integer, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Integer
        """
        node = Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})
        return node._out

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        
        clamp : bool
            parameter `clamp`
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleIndex')
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='CORNER')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        **Fixed values**

        | Kind      | Name     | Value      |
        | --------- | -------- | ---------- |
        | Socket    | Geometry | `self`     |
        | Parameter | `domain` | `'CORNER'` |

        Parameters
        ----------
        sample_position : Vector, optional
            socket 'Sample Position' (id: Sample Position)
        

        Returns
        -------
        Integer
        """
        node = Node('Sample Nearest', {'Geometry': self, 'Sample Position': sample_position}, domain='CORNER')
        return node._out

    def store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store_uv(self, name: String = None, value: Vector = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | `'FLOAT2'`        |
        | Parameter | `domain`    | `'CORNER'`        |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Vector, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type='FLOAT2', domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def pack_uv_islands(cls,
                    uv: Vector = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None):
        """ > Node <&Node Pack UV Islands>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        uv : Vector, optional
            socket 'UV' (id: UV)
        
        margin : Float, optional
            socket 'Margin' (id: Margin)
        
        rotate : Boolean, optional
            socket 'Rotate' (id: Rotate)
        
        method : menu='Bounding Box', optional
            ('Bounding Box', 'Convex Hull', 'Exact Shape')
        
        bottom_left : Vector, optional
            socket 'Bottom Left' (id: Bottom Left)
        
        top_right : Vector, optional
            socket 'Top Right' (id: Top Right)
        

        Returns
        -------
        Vector
        """
        node = Node('Pack UV Islands', {'UV': uv, 'Selection': self.get_selection(), 'Margin': margin, 'Rotate': rotate, 'Method': method, 'Bottom Left': bottom_left, 'Top Right': top_right})
        return node._out

    @classmethod
    def uv_unwrap(cls,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None):
        """ > Node <&Node UV Unwrap>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Selection | `self[selection]` |

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
        node = Node('UV Unwrap', {'Selection': self.get_selection(), 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes, 'Method': method, 'Iterations': iterations, 'No Flip': no_flip})
        return node._out

    @classmethod
    def vertex_index(cls, corner_index: Integer = None):
        """ > Node <&Node Vertex of Corner>

        Parameters
        ----------
        corner_index : Integer, optional
            socket 'Corner Index' (id: Corner Index)
        

        Returns
        -------
        Integer
        """
        node = Node('Vertex of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        **Fixed values**

        | Kind      | Name     | Value      |
        | --------- | -------- | ---------- |
        | Parameter | `domain` | `'CORNER'` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        ui_shortcut : int
            parameter `ui_shortcut`
        
        sockets : dict, default={}
            Socket created with python name attributes

        """
        node = Node('Viewer', named_sockets, domain='CORNER', ui_shortcut=ui_shortcut, **sockets)
        return

    @property
    def normal(self):
        """ Write only property for node <Node Set Mesh Normal>
        """
        raise NodeError('Property Corner.normal is write only.')

    @normal.setter
    def normal(self, custom_normal: Vector = None):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name     | Value      |
        | --------- | -------- | ---------- |
        | Socket    | Mesh     | `self`     |
        | Parameter | `domain` | `'CORNER'` |
        | Parameter | `mode`   | `'FREE'`   |

        Parameters
        ----------
        custom_normal : Vector, optional
            socket 'Custom Normal' (id: Custom Normal)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain='CORNER', mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

