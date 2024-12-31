from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Point(Socket):

    @classmethod
    def accumulate_field(cls, value=None, group_id=None):
        """ > Class Method <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'MATRIX': 'TRANSFORM'}, 'Point.accumulate_field', 'value')
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain='POINT')
        return node._out

    def attribute_statistic(self, attribute=None):
        """ > Method <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Point.attribute_statistic', 'attribute')
        node = Node('Attribute Statistic', sockets={'Geometry': self, 'Selection': self._sel, 'Attribute': attribute}, data_type=data_type, domain='POINT')
        return node._out

    def delete_geometry_all(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode='ALL'):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Jump Method <&Node Delete Geometry>

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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode='ALL'):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount=None):
        """ > Jump Method <&Node Duplicate Elements>

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
        node = Node('Duplicate Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Amount': amount}, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls, index=None, value=None):
        """ > Class Method <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.evaluate_at_index', 'value')
        node = Node('Evaluate at Index', sockets={'Index': index, 'Value': value}, data_type=data_type, domain='POINT')
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None):
        """ > Class Method <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.evaluate_on_domain', 'value')
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain='POINT')
        return node._out

    @classmethod
    def instance_on(cls, points=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Class Method <&Node Instance on Points>

        Information
        -----------
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - points (Geometry) : socket 'Points' (id: Points)
        - instance (Geometry) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', sockets={'Points': points, 'Selection': self._sel, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def sample_index(self, value=None, index=None, clamp=False):
        """ > Method <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.sample_index', 'value')
        node = Node('Sample Index', sockets={'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='POINT')
        return node._out

    def sample_nearest(self, sample_position=None):
        """ > Method <&Node Sample Nearest>

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
        node = Node('Sample Nearest', sockets={'Geometry': self, 'Sample Position': sample_position}, domain='POINT')
        return node._out

    def separate(self):
        """ > Jump Method <&Node Separate Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'POINT'

        Returns
        -------
        - Geometry [inverted_ (Geometry)]
        """
        node = Node('Separate Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_radius(self, radius=None):
        """ > Jump Method <&Node Set Point Radius>

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
        node = Node('Set Point Radius', sockets={'Points': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id=None, sort_weight=None):
        """ > Jump Method <&Node Sort Elements>

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
        node = Node('Sort Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id=None):
        """ > Method <&Node Split to Instances>

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
        node = Node('Split to Instances', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id}, domain='POINT')
        return node._out

    def store_named_attribute(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.store_named_attribute', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.store', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='POINT')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Class Method <&Node Active Element>

        Information
        -----------
        - Parameter 'domain' : 'POINT'

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Active Element', sockets={}, domain='POINT')
        return node._out

    def set_selection(self):
        """ > Jump Method <&Node Set Selection>

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
        selection_type = utils.get_argument_data_type(selection, {'BOOLEAN': 'BOOLEAN', 'VALUE': 'FLOAT'}, 'Point.set_selection', 'selection')
        node = Node('Set Selection', sockets={'Geometry': self, 'Selection': self._sel}, domain='POINT', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def viewer(self, value=None):
        """ > Method <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'POINT'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Point.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='POINT')
        return

