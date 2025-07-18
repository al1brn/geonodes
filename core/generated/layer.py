from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Layer(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value=None, group_id=None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'MATRIX': 'TRANSFORM'}, 'Layer.accumulate_field', 'value')
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain='LAYER')
        return node._out

    def attribute_statistic(self, attribute=None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - node [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Layer.attribute_statistic', 'attribute')
        node = Node('Attribute Statistic', sockets={'Geometry': self, 'Selection': self._sel, 'Attribute': attribute}, data_type=data_type, domain='LAYER')
        return node

    @classmethod
    def field_average(cls, value=None, group_id=None, domain='POINT'):
        """ > Node <&Node Field Average>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - node [mean (Float), median (Float)]
        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Layer.field_average', 'value')
        node = Node('Field Average', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node

    @classmethod
    def field_min_max(cls, value=None, group_id=None, domain='POINT'):
        """ > Node <&Node Field Min & Max>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - node [min (Float), max (Float)]
        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR'}, 'Layer.field_min_max', 'value')
        node = Node('Field Min & Max', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node

    @classmethod
    def field_variance(cls, value=None, group_id=None, domain='POINT'):
        """ > Node <&Node Field Variance>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - node [standard_deviation (Float), variance (Float)]
        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Layer.field_variance', 'value')
        node = Node('Field Variance', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='ALL')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='EDGE_FACE')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode='ALL'):
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode=mode)
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='ALL')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='EDGE_FACE')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode='ALL'):
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount=None):
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
        node = Node('Duplicate Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Amount': amount}, domain='LAYER')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls, value=None, index=None):
        """ > Node <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.evaluate_at_index', 'value')
        node = Node('Evaluate at Index', sockets={'Value': value, 'Index': index}, data_type=data_type, domain='LAYER')
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.evaluate_on_domain', 'value')
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain='LAYER')
        return node._out

    @classmethod
    def named_selection(cls, name=None):
        """ > Node <&Node Named Layer Selection>

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Boolean
        """
        node = Node('Named Layer Selection', sockets={'Name': name})
        return node._out

    def sample_index(self, value=None, index=None, clamp=False):
        """ > Node <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.sample_index', 'value')
        node = Node('Sample Index', sockets={'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='LAYER')
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
        node = Node('Separate Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='LAYER')
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id=None):
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
        node = Node('Split to Instances', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id}, domain='LAYER')
        return node._out

    def store_named_attribute(self, name=None, value=None):
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
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.store_named_attribute', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='LAYER')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self, name=None, value=None):
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
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.store', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='LAYER')
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
        node = Node('Active Element', sockets={}, domain='LAYER')
        return node._out

    def viewer(self, value=None, ui_shortcut=0):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'LAYER'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - ui_shortcut (int): parameter 'ui_shortcut'

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Layer.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='LAYER', ui_shortcut=ui_shortcut)
        return

