# Generated 2026-01-06 09:49:06

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


class Corner:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float | Integer | Vector | Matrix) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAccumulateField', value)
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='CORNER')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - attribute (Float | Vector) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAttributeStatistic', attribute)
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [median_ (Float)]
        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAverage', value)
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Integer | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [max_ (Float)]
        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldMinAndMax', value)
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [variance_ (Float)]
        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldVariance', value)
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def edges(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [previous_edge_index_ (Integer)]
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def next_edge_index(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - next_edge_index
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node.next_edge_index

    @classmethod
    def previous_edge_index(cls, corner_index: Integer = None):
        """ > Node <&Node Edges of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - previous_edge_index
        """
        node = Node('Edges of Corner', {'Corner Index': corner_index})
        return node.previous_edge_index

    @classmethod
    def face(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer [index_in_face_ (Integer)]
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def face_index(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - face_index
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node.face_index

    @classmethod
    def index_in_face(cls, corner_index: Integer = None):
        """ > Node <&Node Face of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - index_in_face
        """
        node = Node('Face of Corner', {'Corner Index': corner_index})
        return node.index_in_face

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAtIndex', value)
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='CORNER')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldOnDomain', value)
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='CORNER')
        return node._out

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'CORNERS'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='CORNERS')
        return node._out

    @classmethod
    def offset_in_face(cls, corner_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Corner in Face>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Integer
        """
        node = Node('Offset Corner in Face', {'Corner Index': corner_index, 'Offset': offset})
        return node._out

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeSampleIndex', value)
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='CORNER')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Nearest', {'Geometry': self, 'Sample Position': sample_position}, domain='CORNER')
        return node._out

    def store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store_uv(self, name: String = None, value: Vector = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : 'FLOAT2'
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Vector) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type='FLOAT2', domain='CORNER')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def pack_uv_islands(cls,
                    uv: Vector = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None):
        """ > Node <&Node Pack UV Islands>

        Information
        -----------
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - uv (Vector) : socket 'UV' (id: UV)
        - margin (Float) : socket 'Margin' (id: Margin)
        - rotate (Boolean) : socket 'Rotate' (id: Rotate)
        - method (menu='Bounding Box') : ('Bounding Box', 'Convex Hull', 'Exact Shape')

        Returns
        -------
        - Vector
        """
        node = Node('Pack UV Islands', {'UV': uv, 'Selection': self.get_selection(), 'Margin': margin, 'Rotate': rotate, 'Method': method})
        return node._out

    @classmethod
    def uv_unwrap(cls,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal'] = None):
        """ > Node <&Node UV Unwrap>

        Information
        -----------
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - seam (Boolean) : socket 'Seam' (id: Seam)
        - margin (Float) : socket 'Margin' (id: Margin)
        - fill_holes (Boolean) : socket 'Fill Holes' (id: Fill Holes)
        - method (menu='Angle Based') : ('Angle Based', 'Conformal')

        Returns
        -------
        - Vector
        """
        node = Node('UV Unwrap', {'Selection': self.get_selection(), 'Seam': seam, 'Margin': margin, 'Fill Holes': fill_holes, 'Method': method})
        return node._out

    @classmethod
    def vertex_index(cls, corner_index: Integer = None):
        """ > Node <&Node Vertex of Corner>

        Arguments
        ---------
        - corner_index (Integer) : socket 'Corner Index' (id: Corner Index)

        Returns
        -------
        - Integer
        """
        node = Node('Vertex of Corner', {'Corner Index': corner_index})
        return node._out

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'CORNER'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

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

        Information
        -----------
        - Socket 'Mesh' : self
        - Parameter 'domain' : 'CORNER'
        - Parameter 'mode' : 'FREE'

        Arguments
        ---------
        - custom_normal (Vector) : socket 'Custom Normal' (id: Custom Normal)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain='CORNER', mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

