# Generated 2026-01-03 16:39:50

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


class Point:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float | Integer | Vector | Matrix) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAccumulateField', value)
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='POINT')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - attribute (Float | Vector) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAttributeStatistic', attribute)
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='POINT')
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

    def delete_geometry_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (id: Amount)

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAtIndex', value)
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='POINT')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldOnDomain', value)
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='POINT')
        return node._out

    def instance_on(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Instances) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', {'Points': self, 'Selection': self.get_selection(), 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
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
        - Parameter 'domain' : 'POINT'

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
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='POINT')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Nearest', {'Geometry': self, 'Sample Position': sample_position}, domain='POINT')
        return node._out

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Returns
        -------
        - node [selection (Geometry), inverted (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT')
        self._jump(node._out)
        return node

    def set_radius(self, radius: Float = None):
        """ > Node <&Node Set Point Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Set Point Radius', {'Points': self, 'Selection': self.get_selection(), 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id: Integer = None, sort_weight: Float = None):
        """ > Node <&Node Sort Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (id: Sort Weight)

        Returns
        -------
        - Geometry
        """
        node = Node('Sort Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='POINT')
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
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='POINT')
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
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Node <&Node Active Element>

        Information
        -----------
        - Parameter 'domain' : 'POINT'

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Active Element', domain='POINT')
        return node._out

    def set_selection(self):
        """ > Node <&Node Set Selection>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'
        - Parameter 'selection_type' : depending on 'selection' type

        Returns
        -------
        - Geometry
        """
        selection_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeToolSetSelection', selection)
        node = Node('Set Selection', {'Geometry': self, 'Selection': self.get_selection()}, domain='POINT', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

        """
        node = Node('Viewer', named_sockets, domain='POINT', ui_shortcut=ui_shortcut, **sockets)
        return

    @property
    def position(self):
        """ Property get node <Node Set Position>
        """
        return Node('Position', {})._out

    @position.setter
    def position(self, position: Vector = None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Offset' : ignored

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def offset(self):
        """ Write only property for node <Node Set Position>
        """
        raise NodeError('Property Point.offset is write only.')

    @offset.setter
    def offset(self, offset: Vector = None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Position' : ignored

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': None, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def normal(self):
        """ Write only property for node <Node Set Mesh Normal>
        """
        raise NodeError('Property Point.normal is write only.')

    @normal.setter
    def normal(self, custom_normal: Vector = None):
        """ > Node <&Node Set Mesh Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Parameter 'domain' : 'POINT'
        - Parameter 'mode' : 'FREE'

        Arguments
        ---------
        - custom_normal (Vector) : socket 'Custom Normal' (id: Custom Normal)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Mesh Normal', {'Mesh': self, 'Custom Normal': custom_normal}, domain='POINT', mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

