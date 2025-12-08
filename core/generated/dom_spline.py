# Generated 2025-12-08 09:52:50

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


class Spline:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - value (Float | Integer | Vector | Matrix) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAccumulateField', value)
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='CURVE')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - attribute (Float | Vector) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAttributeStatistic', attribute)
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='CURVE')
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
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'SPLINE'

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (id: Amount)

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='SPLINE')
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
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAtIndex', value)
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='CURVE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldOnDomain', value)
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='CURVE')
        return node._out

    @classmethod
    def points_of_curve(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def point_index(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - point_index
        """
        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.point_index

    @classmethod
    def points_total(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - total
        """
        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'CURVE'

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
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='CURVE')
        return node._out

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'

        Returns
        -------
        - Geometry [inverted_ (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE')
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id: Integer = None, sort_weight: Float = None):
        """ > Node <&Node Sort Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (id: Sort Weight)

        Returns
        -------
        - Geometry
        """
        node = Node('Sort Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='CURVE')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    @property
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - Float [point_count_ (Integer)]
        """
        node = Node('Spline Length', )
        return node._out

    @classmethod
    @property
    def length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - length
        """
        node = Node('Spline Length', )
        return node.length

    @classmethod
    @property
    def point_count(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - point_count
        """
        node = Node('Spline Length', )
        return node.point_count

    @classmethod
    @property
    def parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - Float [length_ (Float), index_ (Integer)]
        """
        node = Node('Spline Parameter', )
        return node._out

    @classmethod
    @property
    def parameter_factor(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - factor
        """
        node = Node('Spline Parameter', )
        return node.factor

    @classmethod
    @property
    def parameter_length(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - length
        """
        node = Node('Spline Parameter', )
        return node.length

    @classmethod
    @property
    def parameter_index(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - index
        """
        node = Node('Spline Parameter', )
        return node.index

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='CURVE')
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
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CURVE')
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
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='CURVE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_selection(self):
        """ > Node <&Node Set Selection>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'CURVE'
        - Parameter 'selection_type' : depending on 'selection' type

        Returns
        -------
        - Geometry
        """
        selection_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeToolSetSelection', selection)
        node = Node('Set Selection', {'Geometry': self, 'Selection': self.get_selection()}, domain='CURVE', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'CURVE'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

        """
        node = Node('Viewer', named_sockets, domain='CURVE', ui_shortcut=ui_shortcut, **sockets)
        return

    @property
    def material_index(self):
        """ Property get node <Node Set Material Index>
        """
        return Node('Material Index', {})._out

    @material_index.setter
    def material_index(self, material_index: Integer = None):
        """ > Node <&Node Set Material Index>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - material_index (Integer) : socket 'Material Index' (id: Material Index)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def tilt(self):
        """ Property get node <Node Set Curve Tilt>
        """
        return Node('Curve Tilt', {})._out

    @tilt.setter
    def tilt(self, tilt: Float = None):
        """ > Node <&Node Set Curve Tilt>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - tilt (Float) : socket 'Tilt' (id: Tilt)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Tilt', {'Curve': self, 'Selection': self.get_selection(), 'Tilt': tilt})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def normal(self):
        """ Write only property for node <Node Set Curve Normal>
        """
        raise NodeError('Property Spline.normal is write only.')

    @normal.setter
    def normal(self, mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Normal' : ignored

        Arguments
        ---------
        - mode (menu='Minimum Twist') : ('Minimum Twist', 'Z Up', 'Free')

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', {'Curve': self, 'Selection': self.get_selection(), 'Mode': mode, 'Normal': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def is_cyclic(self):
        """ Property get node <Node Set Spline Cyclic>
        """
        return Node('Is Spline Cyclic', {})._out

    @is_cyclic.setter
    def is_cyclic(self, cyclic: Boolean = None):
        """ > Node <&Node Set Spline Cyclic>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - cyclic (Boolean) : socket 'Cyclic' (id: Cyclic)

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Cyclic', {'Geometry': self, 'Selection': self.get_selection(), 'Cyclic': cyclic})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def resolution(self):
        """ Property get node <Node Set Spline Resolution>
        """
        return Node('Spline Resolution', {})._out

    @resolution.setter
    def resolution(self, resolution: Integer = None):
        """ > Node <&Node Set Spline Resolution>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Resolution', {'Geometry': self, 'Selection': self.get_selection(), 'Resolution': resolution})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def type(self):
        """ Write only property for node <Node Set Spline Type>
        """
        raise NodeError('Property Spline.type is write only.')

    @type.setter
    def type(self, spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY'):
        """ > Node <&Node Set Spline Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - spline_type (str): parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', {'Curve': self, 'Selection': self.get_selection()}, spline_type=spline_type)
        self._jump(node._out)
        return self._domain_to_geometry

