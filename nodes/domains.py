from geonodes.nodes import nodes
import geonodes.core.domain as geodom

class Domain(geodom.Domain):
    @property
    def ID(self):
        """ Node ID.

        Node reference [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
        Developer reference [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

        Returns:
            socket `ID`
        """
        return self.attribute_node(nodes.ID()).ID


    @ID.setter
    def ID(self, attr_value):
        """ Node SetID.

        Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
        Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

        Node implemented as property setter.

        Args:
            attr_value: ID

        """
        self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=attr_value))


    def accumulate_field(self, value=None, group_index=None):
        """ Node AccumulateField.

        Node reference [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html)
        Developer reference [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

        Args:
            value: ['Vector', 'Float', 'Integer']
            group_index: Integer

        Returns:
            tuple ('leading', 'trailing', 'total')
        """
        data_type_ = self.value_data_type(value, 'FLOAT')
        node = self.attribute_node(nodes.AccumulateField(value=value, group_index=group_index, data_type=data_type_, domain=self.domain))
        return node.leading, node.trailing, node.total


    def attribute_max(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `max`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).max


    def attribute_mean(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `mean`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).mean


    def attribute_median(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `median`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).median


    def attribute_min(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `min`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).min


    def attribute_range(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `range`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).range


    def attribute_statistic(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain)


    def attribute_std(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `standard_deviation`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).standard_deviation


    def attribute_sum(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `sum`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).sum


    def attribute_var(self, attribute=None):
        """ Node AttributeStatistic.

        Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
        Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        Args:
            attribute: ['Float', 'Vector']

        Returns:
            socket `variance`
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).variance


    def capture_attribute(self, value=None):
        """ Node CaptureAttribute.

        Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
        Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

        Args:
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            socket `attribute`
        """
        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.socket_stack(nodes.CaptureAttribute(geometry=self.data_socket, value=value, data_type=data_type_, domain=self.domain)).node.attribute


    def delete(self, mode='ALL'):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Args:
            mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    @property
    def domain_index(self):
        """ Node Index.

        Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
        Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

        Returns:
            socket `index`
        """
        return self.attribute_node(nodes.Index()).index


    def duplicate(self, amount=None):
        """ Node DuplicateElements.

        Node reference [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
        Developer reference [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        Args:
            amount: Integer

        Returns:
            socket `duplicate_index`
        """
        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def field_at_index(self, index=None, value=None):
        """ Node FieldAtIndex.

        Node reference [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
        Developer reference [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

        Args:
            index: Integer
            value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

        Returns:
            socket `value`
        """
        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.FieldAtIndex(index=index, value=value, data_type=data_type_, domain=self.domain)).value


    def get_named_boolean(self, name=None):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='BOOLEAN')).attribute


    def get_named_color(self, name=None):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR')).attribute


    def get_named_float(self, name=None):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT')).attribute


    def get_named_integer(self, name=None):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='INT')).attribute


    def get_named_vector(self, name=None):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR')).attribute


    @property
    def index(self):
        """ Node Index.

        Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
        Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

        Returns:
            socket `index`
        """
        return self.attribute_node(nodes.Index()).index


    @property
    def material_index(self):
        """ Node MaterialIndex.

        Node reference [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
        Developer reference [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

        Returns:
            socket `material_index`
        """
        return self.attribute_node(nodes.MaterialIndex()).material_index


    def material_selection(self, material=None):
        """ Node MaterialSelection.

        Node reference [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
        Developer reference [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

        Args:
            material: Material

        Returns:
            socket `selection`
        """
        return self.attribute_node(nodes.MaterialSelection(material=material)).selection


    def named_attribute(self, name=None, data_type='FLOAT'):
        """ Node NamedAttribute.

        Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
        Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        Args:
            name: String
            data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

        Returns:
            socket `attribute`
        """
        return self.attribute_node(nodes.NamedAttribute(name=name, data_type=data_type)).attribute


    @property
    def normal(self):
        """ Node Normal.

        Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
        Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

        Returns:
            socket `normal`
        """
        return self.attribute_node(nodes.Normal()).normal


    @property
    def position(self):
        """ Node Position.

        Node reference [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
        Developer reference [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

        Returns:
            socket `position`
        """
        return self.attribute_node(nodes.Position()).position


    @position.setter
    def position(self, attr_value):
        """ Node SetPosition.

        Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
        Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        Node implemented as property setter.

        Args:
            attr_value: position

        """
        self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=attr_value, offset=None))


    def random_boolean(self, probability=None, ID=None, seed=None):
        """ Node RandomValue.

        Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
        Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        Args:
            probability: Float
            ID: Integer
            seed: Integer

        Returns:
            socket `value`
        """
        return self.attribute_node(nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')).value


    def random_float(self, min=None, max=None, ID=None, seed=None):
        """ Node RandomValue.

        Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
        Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        Args:
            min: ['Vector', 'Float', 'Integer']
            max: ['Vector', 'Float', 'Integer']
            ID: Integer
            seed: Integer

        Returns:
            socket `value`
        """
        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT')).value


    def random_integer(self, min=None, max=None, ID=None, seed=None):
        """ Node RandomValue.

        Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
        Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        Args:
            min: ['Vector', 'Float', 'Integer']
            max: ['Vector', 'Float', 'Integer']
            ID: Integer
            seed: Integer

        Returns:
            socket `value`
        """
        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT')).value


    def random_vector(self, min=None, max=None, ID=None, seed=None):
        """ Node RandomValue.

        Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
        Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        Args:
            min: ['Vector', 'Float', 'Integer']
            max: ['Vector', 'Float', 'Integer']
            ID: Integer
            seed: Integer

        Returns:
            socket `value`
        """
        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR')).value


    def remove_named_attribute(self, name=None):
        """ Node RemoveNamedAttribute.

        Node reference [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
        Developer reference [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

        Args:
            name: String

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.RemoveNamedAttribute(geometry=self.data_socket, name=name))


    def sample_index(self, value=None, index=None, clamp=False):
        """ Node SampleIndex.

        Node reference [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
        Developer reference [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

        Args:
            value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
            index: Integer
            clamp (bool): False

        Returns:
            socket `value`
        """
        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleIndex(geometry=self.data_socket, value=value, index=index, clamp=clamp, data_type=data_type_, domain=self.domain).value


    def sample_nearest(self, sample_position=None):
        """ Node SampleNearest.

        Node reference [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
        Developer reference [GeometryNodeSampleNearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

        Args:
            sample_position: Vector

        Returns:
            socket `index`
        """
        return nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain).index


    def separate(self, geometry=None):
        """ Node SeparateGeometry.

        Node reference [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
        Developer reference [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        Args:
            geometry: Geometry

        Returns:
            tuple ('selection', 'inverted')
        """
        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def set_ID(self, ID=None):
        """ Node SetID.

        Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
        Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

        Args:
            ID: Integer

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=ID))


    def set_material_index(self, material_index=None):
        """ Node SetMaterialIndex.

        Node reference [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
        Developer reference [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        Args:
            material_index: Integer

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=material_index))


    def set_named_boolean(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='BOOLEAN', domain=self.domain))


    def set_named_color(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_COLOR', domain=self.domain))


    def set_named_float(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT', domain=self.domain))


    def set_named_integer(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='INT', domain=self.domain))


    def set_named_vector(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_VECTOR', domain=self.domain))


    def set_position(self, position=None, offset=None):
        """ Node SetPosition.

        Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
        Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        Args:
            position: Vector
            offset: Vector

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=position, offset=offset))


    def store_named_attribute(self, name=None, value=None):
        """ Node StoreNamedAttribute.

        Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
        Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        Args:
            name: String
            value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        Returns:
            node with sockets ['geometry']
        """
        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type=data_type_, domain=self.domain))




class Vertex(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.point_count


    def delete_all(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ Node ExtrudeMesh.

        Node reference [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
        Developer reference [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        Args:
            offset: Vector
            offset_scale: Float
            individual: Boolean

        Returns:
            tuple ('top', 'side')
        """
        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='VERTICES')).node
        return node.top, node.side


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Node InstanceOnPoints.

        Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
        Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        Args:
            instance: Geometry
            pick_instance: Boolean
            instance_index: Integer
            rotation: Vector
            scale: Vector

        Returns:
            socket `instances` [Instances](Instances.md)
        """
        return Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    def merge_by_distance(self, distance=None, mode='ALL'):
        """ Node MergeByDistance.

        Node reference [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)
        Developer reference [GeometryNodeMergeByDistance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

        Args:
            distance: Float
            mode (str): 'ALL' in [ALL, CONNECTED]

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.MergeByDistance(geometry=self.data_socket, selection=self.selection, distance=distance, mode=mode))


    @property
    def neighbors(self):
        """ Node VertexNeighbors.

        Node reference [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html)
        Developer reference [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

        Returns:
            node with sockets ['vertex_count', 'face_count']
        """
        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors


    @property
    def neighbors_face_count(self):
        """ Node VertexNeighbors.

        Node reference [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html)
        Developer reference [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

        Returns:
            socket `face_count`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors.face_count


    @property
    def neighbors_vertex_count(self):
        """ Node VertexNeighbors.

        Node reference [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html)
        Developer reference [GeometryNodeInputMeshVertexNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

        Returns:
            socket `vertex_count`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors.vertex_count


    def to_points(self, position=None, radius=None, mode='VERTICES'):
        """ Node MeshToPoints.

        Node reference [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)
        Developer reference [GeometryNodeMeshToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

        Args:
            position: Vector
            radius: Float
            mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

        Returns:
            socket `points` [Points](Points.md)
        """
        return Points(nodes.MeshToPoints(mesh=self.data_socket, selection=self.selection, position=position, radius=radius, mode=mode).points)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
        """ Node MeshToVolume.

        Node reference [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html)
        Developer reference [GeometryNodeMeshToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

        Args:
            density: Float
            voxel_size: Float
            voxel_amount: Float
            exterior_band_width: Float
            interior_band_width: Float
            fill_volume: Boolean
            resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        Returns:
            socket `volume` [Volume](Volume.md)
        """
        return Volume(nodes.MeshToVolume(mesh=self.data_socket, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode).volume)




class Face(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.face_count


    @property
    def area(self):
        """ Node FaceArea.

        Node reference [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html)
        Developer reference [GeometryNodeInputMeshFaceArea](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)

        Returns:
            node with sockets ['area']
        """
        return self.attribute_node(nodes.FaceArea())


    def delete_all(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):
        """ Node DistributePointsOnFaces.

        Node reference [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
        Developer reference [GeometryNodeDistributePointsOnFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

        Args:
            distance_min: Float
            density_max: Float
            density_factor: Float
            seed: Integer

        Returns:
            tuple ('points', 'normal', 'rotation')
        """
        node = nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=distance_min, density_max=density_max, density=None, density_factor=density_factor, seed=seed, distribute_method='POISSON')
        return Points(node.points), node.normal, node.rotation


    def distribute_points_random(self, density=None, seed=None):
        """ Node DistributePointsOnFaces.

        Node reference [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
        Developer reference [GeometryNodeDistributePointsOnFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

        Args:
            density: Float
            seed: Integer

        Returns:
            tuple ('points', 'normal', 'rotation')
        """
        node = nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=None, density_max=None, density=density, density_factor=None, seed=seed, distribute_method='RANDOM')
        return Points(node.points), node.normal, node.rotation


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ Node ExtrudeMesh.

        Node reference [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
        Developer reference [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        Args:
            offset: Vector
            offset_scale: Float
            individual: Boolean

        Returns:
            tuple ('top', 'side')
        """
        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='FACES')).node
        return node.top, node.side


    def face_set_boundaries(self):
        """ Node FaceSetBoundaries.

        Node reference [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)
        Developer reference [GeometryNodeMeshFaceSetBoundaries](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

        Returns:
            socket `boundary_edges`
        """
        return self.attribute_node(nodes.FaceSetBoundaries(face_set=self.selection_index)).boundary_edges


    def flip(self):
        """ Node FlipFaces.

        Node reference [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html)
        Developer reference [GeometryNodeFlipFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

        Returns:
            node with sockets ['mesh']
        """
        return self.socket_stack(nodes.FlipFaces(mesh=self.data_socket, selection=self.selection))


    def is_planar(self, threshold=None):
        """ Node FaceIsPlanar.

        Node reference [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html)
        Developer reference [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

        Args:
            threshold: Float

        Returns:
            socket `planar`
        """
        return self.attribute_node(nodes.FaceIsPlanar(threshold=threshold)).planar


    @property
    def island(self):
        """ Node MeshIsland.

        Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
        Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        Returns:
            node with sockets ['island_index', 'island_count']
        """
        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland


    @property
    def island_count(self):
        """ Node MeshIsland.

        Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
        Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        Returns:
            socket `island_count`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_count


    @property
    def island_index(self):
        """ Node MeshIsland.

        Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
        Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        Returns:
            socket `island_index`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_index


    @property
    def material(self):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        'material' is a write only property.
        Raise an exception if attempt to read.

        """
        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Node implemented as property setter.

        Args:
            attr_value: material

        """
        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def neighbors(self):
        """ Node FaceNeighbors.

        Node reference [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
        Developer reference [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)

        Returns:
            node with sockets ['vertex_count', 'face_count']
        """
        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors


    @property
    def neighbors_face_count(self):
        """ Node FaceNeighbors.

        Node reference [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
        Developer reference [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)

        Returns:
            socket `face_count`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors.face_count


    @property
    def neighbors_vertex_count(self):
        """ Node FaceNeighbors.

        Node reference [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
        Developer reference [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)

        Returns:
            socket `vertex_count`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors.vertex_count


    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        """ Node PackUvIslands.

        Node reference [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)
        Developer reference [GeometryNodeUVPackIslands](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

        Args:
            uv: Vector
            margin: Float
            rotate: Boolean

        Returns:
            socket `uv`
        """
        return self.attribute_node(nodes.PackUvIslands(uv=uv, selection=self.selection, margin=margin, rotate=rotate)).uv


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ Node ScaleElements.

        Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
        Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        Args:
            scale: Float
            center: Vector
            axis: Vector

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """ Node ScaleElements.

        Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
        Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        Args:
            scale: Float
            center: Vector

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    def set_material(self, material=None):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Args:
            material: Material

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_shade_smooth(self, shade_smooth=None):
        """ Node SetShadeSmooth.

        Node reference [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html)
        Developer reference [GeometryNodeSetShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

        Args:
            shade_smooth: Boolean

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=shade_smooth))


    @property
    def shade_smooth(self):
        """ Node IsShadeSmooth.

        Node reference [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html)
        Developer reference [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

        Returns:
            socket `smooth`
        """
        return self.attribute_node(nodes.IsShadeSmooth()).smooth


    @shade_smooth.setter
    def shade_smooth(self, attr_value):
        """ Node SetShadeSmooth.

        Node reference [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html)
        Developer reference [GeometryNodeSetShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

        Node implemented as property setter.

        Args:
            attr_value: shade_smooth

        """
        self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=attr_value))


    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """ Node Triangulate.

        Node reference [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html)
        Developer reference [GeometryNodeTriangulate](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

        Args:
            minimum_vertices: Integer
            ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
            quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

        Returns:
            node with sockets ['mesh']
        """
        return self.socket_stack(nodes.Triangulate(mesh=self.data_socket, selection=self.selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))


    def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """ Node UvUnwrap.

        Node reference [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html)
        Developer reference [GeometryNodeUVUnwrap](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

        Args:
            seam: Boolean
            margin: Float
            fill_holes: Boolean
            method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

        Returns:
            socket `uv`
        """
        return self.attribute_node(nodes.UvUnwrap(selection=self.selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method)).uv




class Edge(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.edge_count


    @property
    def angle(self):
        """ Node EdgeAngle.

        Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
        Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        Returns:
            node with sockets ['unsigned_angle', 'signed_angle']
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle


    def delete_all(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """ Node DeleteGeometry.

        Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
        Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """ Node EdgePathsToCurves.

        Node reference [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)
        Developer reference [GeometryNodeEdgePathsToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

        Args:
            start_vertices: Boolean
            next_vertex_index: Integer

        Returns:
            socket `curves` [Curve](Curve.md)
        """
        return Curve(self.attribute_node(nodes.EdgePathsToCurves(mesh=self.data_socket, start_vertices=start_vertices, next_vertex_index=next_vertex_index)).curves)


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """ Node ExtrudeMesh.

        Node reference [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
        Developer reference [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        Args:
            offset: Vector
            offset_scale: Float
            individual: Boolean

        Returns:
            tuple ('top', 'side')
        """
        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='EDGES')).node
        return node.top, node.side


    @property
    def neighbors(self):
        """ Node EdgeNeighbors.

        Node reference [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html)
        Developer reference [GeometryNodeInputMeshEdgeNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)

        Returns:
            socket `face_count`
        """
        return self.attribute_node(nodes.EdgeNeighbors()).face_count


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ Node ScaleElements.

        Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
        Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        Args:
            scale: Float
            center: Vector
            axis: Vector

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """ Node ScaleElements.

        Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
        Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        Args:
            scale: Float
            center: Vector

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    @property
    def signed_angle(self):
        """ Node EdgeAngle.

        Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
        Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        Returns:
            socket `signed_angle`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle.signed_angle


    def split(self):
        """ Node SplitEdges.

        Node reference [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html)
        Developer reference [GeometryNodeSplitEdges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

        Returns:
            node with sockets ['mesh']
        """
        return self.socket_stack(nodes.SplitEdges(mesh=self.data_socket, selection=self.selection))


    def to_curve(self):
        """ Node MeshToCurve.

        Node reference [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
        Developer reference [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

        Returns:
            socket `curve` [Curve](Curve.md)
        """
        return Curve(nodes.MeshToCurve(mesh=self.data_socket, selection=self.selection).curve)


    @property
    def unsigned_angle(self):
        """ Node EdgeAngle.

        Node reference [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
        Developer reference [GeometryNodeInputMeshEdgeAngle](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        Returns:
            socket `unsigned_angle`
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle.unsigned_angle


    @property
    def vertices(self):
        """ Node EdgeVertices.

        Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
        Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

        Returns:
            node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        return self._c_geometrynodeinputmeshedgevertices


    @property
    def vertices_index(self):
        """ Node EdgeVertices.

        Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
        Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

        Returns:
            tuple ('vertex_index_1', 'vertex_index_2')
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        node = self._c_geometrynodeinputmeshedgevertices
        return node.vertex_index_1, node.vertex_index_2


    @property
    def vertices_position(self):
        """ Node EdgeVertices.

        Node reference [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
        Developer reference [GeometryNodeInputMeshEdgeVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

        Returns:
            tuple ('position_1', 'position_2')
        """
        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        node = self._c_geometrynodeinputmeshedgevertices
        return node.position_1, node.position_2




class Corner(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.face_corner_count




class Spline(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.spline_count


    @property
    def cyclic(self):
        """ Node IsSplineCyclic.

        Node reference [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html)
        Developer reference [GeometryNodeInputSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)

        Returns:
            socket `cyclic`
        """
        return self.as_attribute(nodes.IsSplineCyclic()).cyclic


    @cyclic.setter
    def cyclic(self, attr_value):
        """ Node SetSplineCyclic.

        Node reference [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
        Developer reference [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

        Node implemented as property setter.

        Args:
            attr_value: cyclic

        """
        self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=attr_value))


    @property
    def length(self):
        """ Node SplineLength.

        Node reference [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html)
        Developer reference [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)

        Returns:
            tuple ('length', 'point_count')
        """
        node = self.attribute_node(nodes.SplineLength())
        return node.length, node.point_count


    @property
    def material(self):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        'material' is a write only property.
        Raise an exception if attempt to read.

        """
        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Node implemented as property setter.

        Args:
            attr_value: material

        """
        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def normal(self):
        """ Node Normal.

        Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
        Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

        Returns:
            socket `normal`
        """
        return self.attribute_node(nodes.Normal()).normal


    @normal.setter
    def normal(self, attr_value):
        """ Node SetCurveNormal.

        Node reference [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
        Developer reference [GeometryNodeSetCurveNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

        Node implemented as property setter.

        Args:
            attr_value: mode

        """
        self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=attr_value))


    def points(self, weights=None, sort_index=None):
        """ Node PointsOfCurve.

        Node reference [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html)
        Developer reference [GeometryNodePointsOfCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

        Args:
            weights: Float
            sort_index: Integer

        Returns:
            tuple ('point_index', 'total')
        """
        node = self.attribute_node(nodes.PointsOfCurve(curve_index=self.selection_index, weights=weights, sort_index=sort_index))
        return node.point_index, node.total


    def resample(self, count=None, length=None, mode='COUNT'):
        """ Node ResampleCurve.

        Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
        Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        Args:
            count: Integer
            length: Float
            mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=length, mode=mode))


    def resample_count(self, count=None):
        """ Node ResampleCurve.

        Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
        Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        Args:
            count: Integer

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=0.1, mode='COUNT'))


    def resample_evaluated(self):
        """ Node ResampleCurve.

        Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
        Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=0.1, mode='EVALUATED'))


    def resample_length(self, length=None):
        """ Node ResampleCurve.

        Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
        Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        Args:
            length: Float

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=length, mode='LENGTH'))


    @property
    def resolution(self):
        """ Node SplineResolution.

        Node reference [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html)
        Developer reference [GeometryNodeInputSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)

        Returns:
            socket `resolution`
        """
        return self.attribute_node(nodes.SplineResolution()).resolution


    @resolution.setter
    def resolution(self, attr_value):
        """ Node SetSplineResolution.

        Node reference [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
        Developer reference [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

        Node implemented as property setter.

        Args:
            attr_value: resolution

        """
        self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=attr_value))


    def set_cyclic(self, cyclic=None):
        """ Node SetSplineCyclic.

        Node reference [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
        Developer reference [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

        Args:
            cyclic: Boolean

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=cyclic))


    def set_material(self, material=None):
        """ Node SetMaterial.

        Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
        Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Args:
            material: Material

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_normal(self, mode='MINIMUM_TWIST'):
        """ Node SetCurveNormal.

        Node reference [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
        Developer reference [GeometryNodeSetCurveNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

        Args:
            mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=mode))


    def set_resolution(self, resolution=None):
        """ Node SetSplineResolution.

        Node reference [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
        Developer reference [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

        Args:
            resolution: Integer

        Returns:
            node with sockets ['geometry']
        """
        return self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=resolution))


    def set_type(self, spline_type='POLY'):
        """ Node SetSplineType.

        Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
        Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        Args:
            spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=spline_type))


    @property
    def type(self):
        """ Node SetSplineType.

        Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
        Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        'type' is a write only property.
        Raise an exception if attempt to read.

        """
        raise Exception("Error: 'type' is a write only property of class Curve!")


    @type.setter
    def type(self, attr_value):
        """ Node SetSplineType.

        Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
        Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        Node implemented as property setter.

        Args:
            attr_value: spline_type

        """
        self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=attr_value))




class ControlPoint(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.point_count


    def curve(self):
        """ Node CurveOfPoint.

        Node reference [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html)
        Developer reference [GeometryNodeCurveOfPoint](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

        Returns:
            tuple ('curve_index', 'index_in_curve')
        """
        node = self.attribute_node(nodes.CurveOfPoint(point_index=self.selection_index))
        return node.curve_index, node.index_in_curve


    def endpoint_selection(self, start_size=None, end_size=None):
        """ Node EndpointSelection.

        Node reference [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)
        Developer reference [GeometryNodeCurveEndpointSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)

        Args:
            start_size: Integer
            end_size: Integer

        Returns:
            socket `selection`
        """
        return self.attribute_node(nodes.EndpointSelection(start_size=start_size, end_size=end_size)).selection


    def handle_positions(self, relative=None):
        """ Node CurveHandlePositions.

        Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
        Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        Args:
            relative: Boolean

        Returns:
            node with sockets ['left', 'right']
        """
        return self.as_attribute(nodes.CurveHandlePositions(relative=relative))


    def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['selection']
        """
        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.handle_type_selection_node(handle_type=handle_type, mode=mode)


    def handle_type_selection_free(self, left=True, right=True):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['selection']
        """
        return self.handle_type_selection(left=left, right=right, handle_type='FREE')


    def handle_type_selection_auto(self, left=True, right=True):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['selection']
        """
        return self.handle_type_selection(left=left, right=right, handle_type='AUTO')


    def handle_type_selection_vector(self, left=True, right=True):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['selection']
        """
        return self.handle_type_selection(left=left, right=right, handle_type='VECTOR')


    def handle_type_selection_align(self, left=True, right=True):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['selection']
        """
        return self.handle_type_selection(left=left, right=right, handle_type='ALIGN')


    def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ Node HandleTypeSelection.

        Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
        Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            socket `selection`
        """
        return self.attribute_node(nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)).selection


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Node InstanceOnPoints.

        Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
        Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        Args:
            instance: Geometry
            pick_instance: Boolean
            instance_index: Integer
            rotation: Vector
            scale: Vector

        Returns:
            socket `instances` [Instances](Instances.md)
        """
        return Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    @property
    def left_handle_positions(self):
        """ Node CurveHandlePositions.

        Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
        Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        Returns:
            socket `left`
        """
        return self.attribute_node(nodes.CurveHandlePositions(relative=None)).left


    @left_handle_positions.setter
    def left_handle_positions(self, attr_value):
        """ Node SetHandlePositions.

        Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
        Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        Args:
            attr_value: position

        """
        self.socket_stack(nodes.SetHandlePositions(curve=curve, selection=self.selection, position=attr_value, offset=offset, mode='LEFT'))


    def offset(self, offset=None):
        """ Node OffsetPointInCurve.

        Node reference [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html)
        Developer reference [GeometryNodeOffsetPointInCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

        Args:
            offset: Integer

        Returns:
            tuple ('is_valid_offset', 'point_index')
        """
        node = self.attribute_node(nodes.OffsetPointInCurve(point_index=self.selection_index, offset=offset))
        return node.is_valid_offset, node.point_index


    @property
    def parameter(self):
        """ Node SplineParameter.

        Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
        Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

        Returns:
            tuple ('factor', 'length', 'index')
        """
        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        node = self._c_geometrynodesplineparameter
        return node.factor, node.length, node.index


    @property
    def parameter_factor(self):
        """ Node SplineParameter.

        Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
        Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

        Returns:
            socket `factor`
        """
        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.factor


    @property
    def parameter_index(self):
        """ Node SplineParameter.

        Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
        Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

        Returns:
            socket `index`
        """
        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.index


    @property
    def parameter_length(self):
        """ Node SplineParameter.

        Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
        Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

        Returns:
            socket `length`
        """
        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.length


    @property
    def radius(self):
        """ Node Radius.

        Node reference [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
        Developer reference [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

        Returns:
            socket `radius`
        """
        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """ Node SetCurveRadius.

        Node reference [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
        Developer reference [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

        Node implemented as property setter.

        Args:
            attr_value: radius

        """
        self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=attr_value))


    @property
    def right_handle_positions(self):
        """ Node CurveHandlePositions.

        Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
        Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        Returns:
            socket `right`
        """
        return self.attribute_node(nodes.CurveHandlePositions(relative=None)).right


    @right_handle_positions.setter
    def right_handle_positions(self, attr_value):
        """ Node SetHandlePositions.

        Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
        Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        Args:
            attr_value: position

        """
        self.socket_stack(nodes.SetHandlePositions(curve=curve, selection=self.selection, position=attr_value, offset=offset, mode='RIGHT'))


    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """ Node SetHandlePositions.

        Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
        Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Args:
            position: Vector
            offset: Vector
            mode (str): 'LEFT' in [LEFT, RIGHT]

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode=mode))


    def set_handle_positions_left(self, curve=None, position=None, offset=None):
        """ Node SetHandlePositions.

        Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
        Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Args:
            curve: Curve
            position: Vector
            offset: Vector

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetHandlePositions(curve=curve, selection=self.selection, position=position, offset=offset, mode='LEFT'))


    def set_handle_positions_right(self, curve=None, position=None, offset=None):
        """ Node SetHandlePositions.

        Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
        Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Args:
            curve: Curve
            position: Vector
            offset: Vector

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetHandlePositions(curve=curve, selection=self.selection, position=position, offset=offset, mode='RIGHT'))


    def set_handle_type(self, left=True, right=True, handle_type='AUTO'):
        """ Node SetHandleType.

        Node reference [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
        Developer reference [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

        Args:
            curve: Curve
            selection: Boolean
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['curve']
        """
        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.set_handle_type_node(handle_type=handle_type, mode=mode)


    def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ Node SetHandleType.

        Node reference [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
        Developer reference [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

        Args:
            handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode (set): {'RIGHT', 'LEFT'}

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=handle_type, mode=mode))


    def set_radius(self, radius=None):
        """ Node SetCurveRadius.

        Node reference [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
        Developer reference [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

        Args:
            radius: Float

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=radius))


    def set_tilt(self, tilt=None):
        """ Node SetCurveTilt.

        Node reference [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
        Developer reference [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

        Args:
            tilt: Float

        Returns:
            node with sockets ['curve']
        """
        return self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=tilt))


    @property
    def tangent(self):
        """ Node CurveTangent.

        Node reference [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html)
        Developer reference [GeometryNodeInputTangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)

        Returns:
            socket `tangent`
        """
        return self.attribute_node(nodes.CurveTangent()).tangent


    @property
    def tilt(self):
        """ Node CurveTilt.

        Node reference [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html)
        Developer reference [GeometryNodeInputCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)

        Returns:
            socket `tilt`
        """
        return self.attribute_node(nodes.CurveTilt()).tilt


    @tilt.setter
    def tilt(self, attr_value):
        """ Node SetCurveTilt.

        Node reference [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
        Developer reference [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

        Node implemented as property setter.

        Args:
            attr_value: tilt

        """
        self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=attr_value))




class CloudPoint(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.data_socket.point_count


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ Node InstanceOnPoints.

        Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
        Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        Args:
            instance: Geometry
            pick_instance: Boolean
            instance_index: Integer
            rotation: Vector
            scale: Vector

        Returns:
            socket `instances` [Instances](Instances.md)
        """
        return Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    @property
    def radius(self):
        """ Node Radius.

        Node reference [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
        Developer reference [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

        Returns:
            socket `radius`
        """
        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """ Node SetPointRadius.

        Node reference [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)
        Developer reference [GeometryNodeSetPointRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

        Node implemented as property setter.

        Args:
            attr_value: radius

        """
        self.socket_stack(nodes.SetPointRadius(points=self.data_socket, selection=self.selection, radius=attr_value))


    def to_vertices(self, points=None):
        """ Node PointsToVertices.

        Node reference [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)
        Developer reference [GeometryNodePointsToVertices](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

        Args:
            points: Points

        Returns:
            socket `mesh` [Mesh](Mesh.md)
        """
        return Mesh(nodes.PointsToVertices(points=points, selection=self.selection).mesh)




class Instance(Domain):
    def __len__(self):
        """ Node DomainSize.

        Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
        Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        Args:
            geometry: Geometry
            component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

        Returns:
            node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
        """
        return self.sata_socker.instance_count


    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """ Node RotateInstances.

        Node reference [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)
        Developer reference [GeometryNodeRotateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)

        Args:
            rotation: Vector
            pivot_point: Vector
            local_space: Boolean

        Returns:
            node with sockets ['instances']
        """
        return self.socket_stack(nodes.RotateInstances(instances=self.data_socket, selection=self.selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))


    @property
    def rotation(self):
        """ Node InstanceRotation.

        Node reference [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html)
        Developer reference [GeometryNodeInputInstanceRotation](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)

        Returns:
            socket `rotation`
        """
        return self.attribute_node(nodes.InstanceRotation()).rotation


    @property
    def scale(self):
        """ Node InstanceScale.

        Node reference [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html)
        Developer reference [GeometryNodeInputInstanceScale](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)

        Returns:
            socket `scale`
        """
        return self.attribute_node(nodes.InstanceScale()).scale


    def set_scale(self, scale=None, center=None, local_space=None):
        """ Node ScaleInstances.

        Node reference [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)
        Developer reference [GeometryNodeScaleInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)

        Args:
            scale: Vector
            center: Vector
            local_space: Boolean

        Returns:
            node with sockets ['instances']
        """
        return self.socket_stack(nodes.ScaleInstances(instances=self.data_socket, selection=self.selection, scale=scale, center=center, local_space=local_space))


    def to_points(self, position=None, radius=None):
        """ Node InstancesToPoints.

        Node reference [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)
        Developer reference [GeometryNodeInstancesToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)

        Args:
            position: Vector
            radius: Float

        Returns:
            socket `points` [Points](Points.md)
        """
        return Points(nodes.InstancesToPoints(instances=self.data_socket, selection=self.selection, position=position, radius=radius).points)


    def translate(self, translation=None, local_space=None):
        """ Node TranslateInstances.

        Node reference [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)
        Developer reference [GeometryNodeTranslateInstances](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)

        Args:
            translation: Vector
            local_space: Boolean

        Returns:
            node with sockets ['instances']
        """
        return self.socket_stack(nodes.TranslateInstances(instances=self.data_socket, selection=self.selection, translation=translation, local_space=local_space))




