# Generated 2025-12-06 09:50:17

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


class Layer(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float | Integer | Vector | Matrix) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAccumulateField', value)
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='LAYER')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - attribute (Float | Vector) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - node [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAttributeStatistic', attribute)
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='LAYER')
        return node

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
        - node [mean (Float), median (Float)]
        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAverage', value)
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node

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
        - node [min (Float), max (Float)]
        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldMinAndMax', value)
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node

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
        - node [standard_deviation (Float), variance (Float)]
        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldVariance', value)
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node

    def delete_geometry_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (id: Amount)

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='LAYER')
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
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAtIndex', value)
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='LAYER')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldOnDomain', value)
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='LAYER')
        return node._out

    @classmethod
    def named_selection(cls, name: String = None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', {'Name': name})
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
        - Parameter 'domain' : 'LAYER'

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
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='LAYER')
        return node._out

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'

        Returns
        -------
        - Geometry [inverted_ (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='LAYER')
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='LAYER')
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
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='LAYER')
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
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='LAYER')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Node <&Node Active Element>

        Information
        -----------
        - Parameter 'domain' : 'LAYER'

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Active Element', domain='LAYER')
        return node._out

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

        """
        node = Node('Viewer', named_sockets, domain='LAYER', ui_shortcut=ui_shortcut, **sockets)
        return

