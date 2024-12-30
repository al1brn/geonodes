from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Edge(Socket):

    @classmethod
    def accumulate_field(cls, value=None, group_id=None):
        """ > Class Method <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'MATRIX': 'TRANSFORM'}, 'Edge.accumulate_field', 'value')
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain='EDGE')
        return node._out

    def attribute_statistic(self, attribute=None):
        """ > Method <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Edge.attribute_statistic', 'attribute')
        node = Node('Attribute Statistic', sockets={'Geometry': self, 'Selection': self._sel, 'Attribute': attribute}, data_type=data_type, domain='EDGE')
        return node._out

    def delete_all(self):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ALL')
        self._jump(node._out)
        return self

    def delete_edge_face(self):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='EDGE_FACE')
        self._jump(node._out)
        return self

    def delete_only_face(self):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self

    def delete(self, mode='ALL'):
        """ > Jump Method <&Node Delete Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self

    def duplicate(self, amount=None):
        """ > Jump Method <&Node Duplicate Elements>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (id: Amount)

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        node = Node('Duplicate Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Amount': amount}, domain='EDGE')
        self._jump(node._out)
        return self

    def paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """ > Method <&Node Edge Paths to Curves>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Curve
        """
        node = Node('Edge Paths to Curves', sockets={'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def evaluate_at_index(cls, index=None, value=None):
        """ > Class Method <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.evaluate_at_index', 'value')
        node = Node('Evaluate at Index', sockets={'Index': index, 'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None):
        """ > Class Method <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.evaluate_on_domain', 'value')
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    def sample_index(self, value=None, index=None, clamp=False):
        """ > Method <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.sample_index', 'value')
        node = Node('Sample Index', sockets={'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='EDGE')
        return node._out

    def sample_nearest(self, sample_position=None):
        """ > Method <&Node Sample Nearest>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)

        Returns
        -------
        - Integer
        """
        node = Node('Sample Nearest', sockets={'Geometry': self, 'Sample Position': sample_position}, domain='EDGE')
        return node._out

    def scale(self, scale=None, center=None, scale_mode='UNIFORM'):
        """ > Jump Method <&Node Scale Elements>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - scale_mode (str): parameter 'scale_mode' in ('UNIFORM', 'SINGLE_AXIS')

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center}, domain='EDGE', scale_mode=scale_mode)
        self._jump(node._out)
        return self

    def scale_uniform(self, scale=None, center=None):
        """ > Jump Method <&Node Scale Elements>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'scale_mode' : 'UNIFORM'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center}, domain='EDGE', scale_mode='UNIFORM')
        self._jump(node._out)
        return self

    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ > Jump Method <&Node Scale Elements>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'scale_mode' : 'SINGLE_AXIS'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center, 'Axis': axis}, domain='EDGE', scale_mode='SINGLE_AXIS')
        self._jump(node._out)
        return self

    def separate(self):
        """ > Jump Method <&Node Separate Geometry>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Returns
        -------
        - Geometry [inverted_ (Geometry)]
        """
        node = Node('Separate Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE')
        self._jump(node._out)
        return self

    def set_shade_smooth(self, shade_smooth=None):
        """ > Jump Method <&Node Set Shade Smooth>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self

    def sort(self, group_id=None, sort_weight=None):
        """ > Jump Method <&Node Sort Elements>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (id: Sort Weight)

        Returns
        -------
        - Geometry
        """
        node = Node('Sort Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='EDGE')
        self._jump(node._out)
        return self

    def split(self):
        """ > Jump Method <&Node Split Edges>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Split Edges', sockets={'Mesh': self, 'Selection': self._sel})
        self._jump(node._out)
        return self

    def split_to_instances(self, group_id=None):
        """ > Method <&Node Split to Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        node = Node('Split to Instances', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id}, domain='EDGE')
        return node._out

    def store_named_attribute(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.store_named_attribute', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self

    def store(self, name=None, value=None):
        """ > Jump Method <&Node Store Named Attribute>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.store', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self

    @classmethod
    def active_element(cls):
        """ > Class Method <&Node Active Element>

        Information
        -----------
        - Parameter 'domain' : 'EDGE'

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Active Element', sockets={}, domain='EDGE')
        return node._out

    def set_selection(self):
        """ > Jump Method <&Node Set Selection>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'selection_type' : depending on 'selection' type

        Returns
        -------
        - Geometry
        """
        selection_type = utils.get_argument_data_type(selection, {'BOOLEAN': 'BOOLEAN', 'VALUE': 'FLOAT'}, 'Edge.set_selection', 'selection')
        node = Node('Set Selection', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', selection_type=selection_type)
        self._jump(node._out)
        return self

    def viewer(self, value=None):
        """ > Method <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='EDGE')
        return

    @property
    def shade_smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', sockets={})._out

    @shade_smooth.setter
    def shade_smooth(self, shade_smooth=None):
        """ > Jump Method <&Node Set Shade Smooth>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self

    @property
    def smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', sockets={})._out

    @smooth.setter
    def smooth(self, shade_smooth=None):
        """ > Jump Method <&Node Set Shade Smooth>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self

