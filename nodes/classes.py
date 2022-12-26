from geonodes.nodes import nodes
import geonodes.core.datasockets as geosocks
from geonodes.nodes.domains import Vertex, Edge, Face, Corner, ControlPoint, Spline, CloudPoint, Instance

class Geometry(geosocks.Geometry):
    @classmethod
    def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL'):
        """

        > Node: [Collection Info](GeometryNodeCollectionInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

        #### Args:
        - collection: Collection
        - separate_children: Boolean
        - reset_children: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - socket `geometry`


        """

        return cls(nodes.CollectionInfo(collection=collection, separate_children=separate_children, reset_children=reset_children, transform_space=transform_space).geometry)


    @property
    def ID(self):
        """

        > Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

        #### Returns:
        - socket `ID`


        """

        return self.attribute_node(nodes.ID()).ID


    def attribute_statistic(self, selection=None, attribute=None, domain='POINT'):
        """

        > Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        #### Args:
        - selection: Boolean
        - attribute: ['Float', 'Vector']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self, selection=selection, attribute=attribute, data_type=data_type_, domain=domain)


    @property
    def bounding_box(self):
        """

        > Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

        #### Returns:
        - socket `bounding_box` of class Mesh


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return gn.Mesh(self._c_geometrynodeboundbox.bounding_box)


    @property
    def bounding_box_min(self):
        """

        > Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

        #### Returns:
        - socket `min`


        """

        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return self._c_geometrynodeboundbox.min


    @property
    def bounding_box_min(self):
        """

        > Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

        #### Returns:
        - socket `max`


        """

        if not hasattr(self, '_c_geometrynodeboundbox'):
            self._c_geometrynodeboundbox = nodes.BoundingBox(geometry=self)
        return self._c_geometrynodeboundbox.max


    def capture_attribute(self, value=None, domain='POINT'):
        """

        > Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

        #### Args:
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - socket `attribute`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.stack(nodes.CaptureAttribute(geometry=self, value=value, data_type=data_type_, domain=domain)).node.attribute


    @staticmethod
    def capture_attribute_node(geometry=None, value=None, data_type='FLOAT', domain='POINT'):
        """

        > Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

        #### Args:
        - geometry: Geometry
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - node with sockets ['geometry', 'attribute']


        """

        return nodes.CaptureAttribute(geometry=geometry, value=value, data_type=data_type, domain=domain)


    @property
    def convex_hull(self):
        """

        > Node: [Convex Hull](GeometryNodeConvexHull.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

        #### Returns:
        - socket `convex_hull` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.ConvexHull(geometry=self).convex_hull)


    @property
    def curve_component(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - socket `curve` of class Curve


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Curve(self._c_geometrynodeseparatecomponents.curve)


    def delete(self, selection=None, domain='POINT', mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - selection: Boolean
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode=mode))


    @property
    def domain_size(self, component='MESH'):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component=component)
        return self._c_geometrynodeattributedomainsize


    def duplicate(self, selection=None, amount=None, domain='POINT'):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - selection: Boolean
        - amount: Integer
        - domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

        #### Returns:
        - socket `duplicate_index`


        """

        return self.stack(nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain=domain)).node.duplicate_index


    def field_at_index(self, index=None, value=None, domain='POINT'):
        """

        > Node: [Field at Index](GeometryNodeFieldAtIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

        #### Args:
        - index: Integer
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.FieldAtIndex(index=index, value=value, data_type=data_type_, domain=domain)).value


    @property
    def index(self):
        """

        > Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

        #### Returns:
        - socket `index`


        """

        return self.attribute_node(nodes.Index()).index


    @property
    def instances_component(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - socket `instances` of class Instances


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Instances(self._c_geometrynodeseparatecomponents.instances)


    def interpolate_domain(self, value=None, domain='POINT'):
        """

        > Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.InterpolateDomain(value=value, data_type=data_type_, domain=domain)).value


    @property
    def is_viewport(self):
        """

        > Node: [Is Viewport](GeometryNodeIsViewport.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

        #### Returns:
        - socket `is_viewport`


        """

        return self.attribute_node(nodes.IsViewport()).is_viewport


    def join(*geometry):
        """

        > Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

        #### Args:
        - geometry: <m>Geometry

        #### Returns:
        - socket `geometry`


        """

        self = geometry[0]

        return nodes.JoinGeometry(*geometry).geometry


    @property
    def material_index(self):
        """

        > Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

        #### Returns:
        - socket `material_index`


        """

        return self.attribute_node(nodes.MaterialIndex()).material_index


    def material_selection(self, material=None):
        """

        > Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

        #### Args:
        - material: Material

        #### Returns:
        - socket `selection`


        """

        return self.attribute_node(nodes.MaterialSelection(material=material)).selection


    def merge_by_distance(self, selection=None, distance=None, mode='ALL'):
        """

        > Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

        #### Args:
        - selection: Boolean
        - distance: Float
        - mode (str): 'ALL' in [ALL, CONNECTED]

        #### Returns:
        - self


        """

        return self.stack(nodes.MergeByDistance(geometry=self, selection=selection, distance=distance, mode=mode))


    @property
    def mesh_component(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Mesh(self._c_geometrynodeseparatecomponents.mesh)


    def named_attribute(self, name=None, data_type='FLOAT'):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String
        - data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type=data_type)).attribute


    def named_boolean(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='BOOLEAN')).attribute


    def named_color(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR')).attribute


    def named_float(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT')).attribute


    def named_integer(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='INT')).attribute


    def named_vector(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR')).attribute


    @property
    def normal(self):
        """

        > Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

        #### Returns:
        - socket `normal`


        """

        return self.attribute_node(nodes.Normal()).normal


    @property
    def points_component(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - socket `point_cloud` of class Points


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Points(self._c_geometrynodeseparatecomponents.point_cloud)


    @property
    def position(self):
        """

        > Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

        #### Returns:
        - socket `position`


        """

        return self.attribute_node(nodes.Position()).position


    def proximity(self, target=None, source_position=None, target_element='FACES'):
        """

        > Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

        #### Args:
        - target: Geometry
        - source_position: Vector
        - target_element (str): 'FACES' in [POINTS, EDGES, FACES]

        #### Returns:
        - socket `distance`


        """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element=target_element)).distance


    def proximity_edges(self, target=None, source_position=None):
        """

        > Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

        #### Args:
        - target: Geometry
        - source_position: Vector

        #### Returns:
        - socket `distance`


        """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='EDGES')).distance


    def proximity_faces(self, target=None, source_position=None):
        """

        > Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

        #### Args:
        - target: Geometry
        - source_position: Vector

        #### Returns:
        - socket `distance`


        """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='FACES')).distance


    def proximity_points(self, target=None, source_position=None):
        """

        > Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

        #### Args:
        - target: Geometry
        - source_position: Vector

        #### Returns:
        - socket `distance`


        """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='POINTS')).distance


    @property
    def radius(self):
        """

        > Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

        #### Returns:
        - socket `radius`


        """

        return self.attribute_node(nodes.Radius()).radius


    @staticmethod
    def random_boolean(probability=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - probability: Float
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value


    @staticmethod
    def random_float(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT').value


    @staticmethod
    def random_integer(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT').value


    @staticmethod
    def random_vector(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value


    def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """

        > Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

        #### Args:
        - target_geometry: Geometry
        - attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - source_position: Vector
        - ray_direction: Vector
        - ray_length: Float
        - mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

        #### Returns:
        - node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping=mapping))


    def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

        > Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

        #### Args:
        - target_geometry: Geometry
        - attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - source_position: Vector
        - ray_direction: Vector
        - ray_length: Float

        #### Returns:
        - node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='INTERPOLATED'))


    def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

        > Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

        #### Args:
        - target_geometry: Geometry
        - attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - source_position: Vector
        - ray_direction: Vector
        - ray_length: Float

        #### Returns:
        - node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='NEAREST'))


    def remove_named_attribute(self, name=None):
        """

        > Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - self


        """

        return self.stack(nodes.RemoveNamedAttribute(geometry=self, name=name))


    def replace_material(self, old=None, new=None):
        """

        > Node: [Replace Material](GeometryNodeReplaceMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

        #### Args:
        - old: Material
        - new: Material

        #### Returns:
        - self


        """

        return self.stack(nodes.ReplaceMaterial(geometry=self, old=old, new=new))


    def sample_index(self, value=None, index=None, clamp=False, domain='POINT'):
        """

        > Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - index: Integer
        - clamp (bool): False
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type=data_type_, domain=domain).value


    def sample_nearest(self, sample_position=None, domain='POINT'):
        """

        > Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

        #### Args:
        - sample_position: Vector
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

        #### Returns:
        - socket `index`


        """

        return nodes.SampleNearest(geometry=self, sample_position=sample_position, domain=domain).index


    def separate(self, selection=None, domain='POINT'):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        #### Args:
        - selection: Boolean
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - tuple ('`selection`', '`inverted`')


        """

        node = nodes.SeparateGeometry(geometry=self, selection=selection, domain=domain)
        return node.selection, node.inverted


    @property
    def separate_components(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']


        """

        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return self._c_geometrynodeseparatecomponents


    def set_ID(self, selection=None, ID=None):
        """

        > Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

        #### Args:
        - selection: Boolean
        - ID: Integer

        #### Returns:
        - self


        """

        return self.stack(nodes.SetID(geometry=self, selection=selection, ID=ID))


    def set_material(self, selection=None, material=None):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        #### Args:
        - selection: Boolean
        - material: Material

        #### Returns:
        - self


        """

        return self.stack(nodes.SetMaterial(geometry=self, selection=selection, material=material))


    def set_material_index(self, selection=None, material_index=None):
        """

        > Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        #### Args:
        - selection: Boolean
        - material_index: Integer

        #### Returns:
        - self


        """

        return self.stack(nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index))


    def set_position(self, selection=None, position=None, offset=None):
        """

        > Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        #### Args:
        - selection: Boolean
        - position: Vector
        - offset: Vector

        #### Returns:
        - self


        """

        return self.stack(nodes.SetPosition(geometry=self, selection=selection, position=position, offset=offset))


    def store_named_attribute(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type=data_type_, domain=domain))


    def store_named_boolean(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='BOOLEAN', domain=domain))


    def store_named_color(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_COLOR', domain=domain))


    def store_named_float(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT', domain=domain))


    def store_named_integer(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='INT', domain=domain))


    def store_named_vector(self, name=None, value=None, domain='POINT'):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.StoreNamedAttribute(geometry=self, name=name, value=value, data_type='FLOAT_VECTOR', domain=domain))


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Geometry

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='GEOMETRY').output


    def to_instance(*geometry):
        """

        > Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

        #### Args:
        - geometry: <m>Geometry

        #### Returns:
        - socket `instances` of class Instances


        """

        import geonodes as gn
        return gn.Instances(nodes.GeometryToInstance(*geometry).instances)


    def transform(self, translation=None, rotation=None, scale=None):
        """

        > Node: [Transform](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

        #### Args:
        - translation: Vector
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - self


        """

        return self.stack(nodes.Transform(geometry=self, translation=translation, rotation=rotation, scale=scale))


    def view(self, value=None, domain='AUTO'):
        """

        > Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

        #### Args:
        - value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
        - domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - node with sockets []


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.Viewer(geometry=self, value=value, data_type=data_type_, domain=domain)


    def viewer(self, value=None, domain='AUTO'):
        """

        > Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

        #### Args:
        - value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
        - domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - node with sockets []


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.Viewer(geometry=self, value=value, data_type=data_type_, domain=domain)


    @property
    def volume_component(self):
        """

        > Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        if not hasattr(self, '_c_geometrynodeseparatecomponents'):
            self._c_geometrynodeseparatecomponents = nodes.SeparateComponents(geometry=self)
        return gn.Volume(self._c_geometrynodeseparatecomponents.volume)




class Mesh(Geometry):
    @classmethod
    def Circle(cls, vertices=None, radius=None, fill_type='NONE'):
        """

        > Node: [Mesh Circle](GeometryNodeMeshCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)

        #### Args:
        - vertices: Integer
        - radius: Float
        - fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type).mesh)


    @staticmethod
    def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):
        """

        > Node: [Cone](GeometryNodeMeshCone.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)

        #### Args:
        - vertices: Integer
        - side_segments: Integer
        - fill_segments: Integer
        - radius_top: Float
        - radius_bottom: Float
        - depth: Float
        - fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCone.webp)

        #### Returns:
        - tuple ('`mesh`', '`top`', '`bottom`', '`side`')


        """

        import geonodes as gn
        node = nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)
        return gn.Mesh(node.mesh), node.top, node.bottom, node.side


    @classmethod
    def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):
        """

        > Node: [Cube](GeometryNodeMeshCube.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)

        #### Args:
        - size: Vector
        - vertices_x: Integer
        - vertices_y: Integer
        - vertices_z: Integer

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z).mesh)


    @staticmethod
    def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):
        """

        > Node: [Cylinder](GeometryNodeMeshCylinder.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)

        #### Args:
        - vertices: Integer
        - side_segments: Integer
        - fill_segments: Integer
        - radius: Float
        - depth: Float
        - fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCylinder.webp)

        #### Returns:
        - tuple ('`mesh`', '`top`', '`bottom`', '`side`')


        """

        import geonodes as gn
        node = nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)
        return gn.Mesh(node.mesh), node.top, node.bottom, node.side


    @classmethod
    def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):
        """

        > Node: [Grid](GeometryNodeMeshGrid.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)

        #### Args:
        - size_x: Float
        - size_y: Float
        - vertices_x: Integer
        - vertices_y: Integer

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y).mesh)


    @classmethod
    def IcoSphere(cls, radius=None, subdivisions=None):
        """

        > Node: [Ico Sphere](GeometryNodeMeshIcoSphere.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)

        #### Args:
        - radius: Float
        - subdivisions: Integer

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.IcoSphere(radius=radius, subdivisions=subdivisions).mesh)


    @classmethod
    def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):
        """

        > Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

        #### Args:
        - count: Integer
        - resolution: Float
        - start_location: Vector
        - offset: Vector
        - count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
        - mode (str): 'OFFSET' in [OFFSET, END_POINTS]

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.MeshLine(count=count, resolution=resolution, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode).mesh)


    @classmethod
    def LineEndPoints(cls, count=None, start_location=None, end_location=None):
        """

        > Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

        #### Args:
        - count: Integer
        - start_location: Vector
        - end_location: Vector

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=end_location, count_mode='TOTAL', mode='END_POINTS').mesh)


    @classmethod
    def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):
        """

        > Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

        #### Args:
        - resolution: Float
        - start_location: Vector
        - end_location: Vector

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.MeshLine(count=None, resolution=resolution, start_location=start_location, offset=end_location, count_mode='RESOLUTION', mode='END_POINTS').mesh)


    @classmethod
    def LineOffset(cls, count=None, start_location=None, offset=None):
        """

        > Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

        #### Args:
        - count: Integer
        - start_location: Vector
        - offset: Vector

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.MeshLine(count=count, resolution=None, start_location=start_location, offset=offset, count_mode='TOTAL', mode='OFFSET').mesh)


    @classmethod
    def UVSphere(cls, segments=None, rings=None, radius=None):
        """

        > Node: [UV Sphere](GeometryNodeMeshUVSphere.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)

        #### Args:
        - segments: Integer
        - rings: Integer
        - radius: Float

        #### Returns:
        - socket `mesh`


        """

        return cls(nodes.UvSphere(segments=segments, rings=rings, radius=radius).mesh)


    def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):
        """

        > Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

        #### Args:
        - mesh_2: <m>Geometry
        - self_intersection: Boolean
        - hole_tolerant: Boolean

        #### Returns:
        - socket `intersecting_edges`


        """

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE')).node.intersecting_edges


    def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):
        """

        > Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

        #### Args:
        - mesh_2: <m>Geometry
        - self_intersection: Boolean
        - hole_tolerant: Boolean

        #### Returns:
        - socket `intersecting_edges`


        """

        self = mesh_2[0]

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT')).node.intersecting_edges


    def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):
        """

        > Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

        #### Args:
        - mesh_2: <m>Geometry
        - self_intersection: Boolean
        - hole_tolerant: Boolean

        #### Returns:
        - socket `intersecting_edges`


        """

        self = mesh_2[0]

        return self.stack(nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION')).node.intersecting_edges


    @property
    def corner_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `face_corner_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.face_corner_count


    def corners_of_face(self, face_index=None, weights=None, sort_index=None):
        """

        > Node: [Corners of Face](GeometryNodeCornersOfFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

        #### Args:
        - face_index: Integer
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

        #### Returns:
        - tuple ('`corner_index`', '`total`')


        """

        node = self.attribute_node(nodes.CornersOfFace(face_index=face_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None):
        """

        > Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

        #### Args:
        - vertex_index: Integer
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

        #### Returns:
        - tuple ('`corner_index`', '`total`')


        """

        node = self.attribute_node(nodes.CornersOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def delete_all(self, selection=None, domain='POINT'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - selection: Boolean
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ALL'))


    def delete_edges(self, selection=None, domain='POINT'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - selection: Boolean
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='EDGE_FACE'))


    def delete_faces(self, selection=None, domain='POINT'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - selection: Boolean
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

        #### Returns:
        - self


        """

        return self.stack(nodes.DeleteGeometry(geometry=self, selection=selection, domain=domain, mode='ONLY_FACE'))


    def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):
        """

        > Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

        #### Args:
        - selection: Boolean
        - distance_min: Float
        - density_max: Float
        - density: Float
        - density_factor: Float
        - seed: Integer
        - distribute_method (str): 'RANDOM' in [RANDOM, POISSON]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

        #### Returns:
        - tuple ('`points`', '`normal`', '`rotation`')


        """

        import geonodes as gn
        node = nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)
        return gn.Points(node.points), node.normal, node.rotation


    @property
    def domain_size(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize


    def dual_mesh(self, keep_boundaries=None):
        """

        > Node: [Dual Mesh](GeometryNodeDualMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)

        #### Args:
        - keep_boundaries: Boolean

        #### Returns:
        - socket `dual_mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries).dual_mesh)


    @property
    def edge_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `edge_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.edge_count


    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """

        > Node: [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

        #### Args:
        - start_vertices: Boolean
        - next_vertex_index: Integer

        #### Returns:
        - socket `curves` of class Curve


        """

        import geonodes as gn
        return gn.Curve(nodes.EdgePathsToCurves(mesh=self, start_vertices=start_vertices, next_vertex_index=next_vertex_index).curves)


    def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):
        """

        > Node: [Edge Paths to Selection](GeometryNodeEdgePathsToSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)

        #### Args:
        - start_vertices: Boolean
        - next_vertex_index: Integer

        #### Returns:
        - socket `selection`


        """

        return nodes.EdgePathsToSelection(start_vertices=start_vertices, next_vertex_index=next_vertex_index).selection


    def edges_of_corner(self, corner_index=None):
        """

        > Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

        #### Args:
        - corner_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

        #### Returns:
        - tuple ('`next_edge_index`', '`previous_edge_index`')


        """

        node = self.attribute_node(nodes.EdgesOfCorner(corner_index=corner_index))
        return node.next_edge_index, node.previous_edge_index


    def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None):
        """

        > Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

        #### Args:
        - vertex_index: Integer
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

        #### Returns:
        - tuple ('`edge_index`', '`total`')


        """

        node = self.attribute_node(nodes.EdgesOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index))
        return node.edge_index, node.total


    def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):
        """

        > Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        #### Args:
        - selection: Boolean
        - offset: Vector
        - offset_scale: Float
        - individual: Boolean
        - mode (str): 'FACES' in [VERTICES, EDGES, FACES]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        #### Returns:
        - tuple ('`top`', '`side`')


        """

        node = self.stack(nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)).node
        return node.top, node.side


    @property
    def face_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `face_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.face_count


    def face_is_planar(self, threshold=None):
        """

        > Node: [Face is Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

        #### Args:
        - threshold: Float

        #### Returns:
        - socket `planar`


        """

        return self.attribute_node(nodes.FaceIsPlanar(threshold=threshold)).planar


    def face_of_corner(self, corner_index=None):
        """

        > Node: [Face of Corner](GeometryNodeFaceOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

        #### Args:
        - corner_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

        #### Returns:
        - tuple ('`face_index`', '`index_in_face`')


        """

        node = self.attribute_node(nodes.FaceOfCorner(corner_index=corner_index))
        return node.face_index, node.index_in_face


    def face_set_boundaries(self, face_set=None):
        """

        > Node: [Face Set Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

        #### Args:
        - face_set: Integer

        #### Returns:
        - socket `boundary_edges`


        """

        return self.attribute_node(nodes.FaceSetBoundaries(face_set=face_set)).boundary_edges


    def flip_faces(self, selection=None):
        """

        > Node: [Flip Faces](GeometryNodeFlipFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.FlipFaces(mesh=self, selection=selection))


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - selection: Boolean
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def is_shade_smooth(self):
        """

        > Node: [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

        #### Returns:
        - socket `smooth`


        """

        return self.attribute_node(nodes.IsShadeSmooth()).smooth


    @property
    def island(self):
        """

        > Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        #### Returns:
        - node with sockets ['island_index', 'island_count']


        """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland


    @property
    def island_count(self):
        """

        > Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        #### Returns:
        - socket `island_count`


        """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_count


    @property
    def island_index(self):
        """

        > Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        #### Returns:
        - socket `island_index`


        """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_index


    def offset_corner_in_face(self, corner_index=None, offset=None):
        """

        > Node: [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

        #### Args:
        - corner_index: Integer
        - offset: Integer

        #### Returns:
        - socket `corner_index`


        """

        return self.attribute_node(nodes.OffsetCornerInFace(corner_index=corner_index, offset=offset)).corner_index


    def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):
        """

        > Node: [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

        #### Args:
        - uv: Vector
        - selection: Boolean
        - margin: Float
        - rotate: Boolean

        #### Returns:
        - socket `uv`


        """

        return self.attribute_node(nodes.PackUvIslands(uv=uv, selection=selection, margin=margin, rotate=rotate)).uv


    @property
    def point_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='MESH')
        return self._c_geometrynodeattributedomainsize.point_count


    def sample_nearest_surface(self, value=None, sample_position=None):
        """

        > Node: [Sample Nearest Surface](GeometryNodeSampleNearestSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - sample_position: Vector

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type=data_type_).value


    def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):
        """

        > Node: [Sample UV Surface](GeometryNodeSampleUVSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - source_uv_map: Vector
        - sample_uv: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        #### Returns:
        - tuple ('`value`', '`is_valid`')


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        node = nodes.SampleUvSurface(mesh=self, value=value, source_uv_map=source_uv_map, sample_uv=sample_uv, data_type=data_type_)
        return node.value, node.is_valid


    def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - selection: Boolean
        - scale: Float
        - center: Vector
        - axis: Vector
        - domain (str): 'FACE' in [FACE, EDGE]
        - scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

        #### Returns:
        - self


        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode=scale_mode))


    def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - selection: Boolean
        - scale: Float
        - center: Vector
        - axis: Vector
        - domain (str): 'FACE' in [FACE, EDGE]

        #### Returns:
        - self


        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=axis, domain=domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - selection: Boolean
        - scale: Float
        - center: Vector
        - domain (str): 'FACE' in [FACE, EDGE]

        #### Returns:
        - self


        """

        return self.stack(nodes.ScaleElements(geometry=self, selection=selection, scale=scale, center=center, axis=None, domain=domain, scale_mode='UNIFORM'))


    def set_shade_smooth(self, selection=None, shade_smooth=None):
        """

        > Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

        #### Args:
        - selection: Boolean
        - shade_smooth: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.SetShadeSmooth(geometry=self, selection=selection, shade_smooth=shade_smooth))


    def shortest_edge_paths(self, end_vertex=None, edge_cost=None):
        """

        > Node: [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)

        #### Args:
        - end_vertex: Boolean
        - edge_cost: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.webp)

        #### Returns:
        - tuple ('`next_vertex_index`', '`total_cost`')


        """

        node = self.attribute_node(nodes.ShortestEdgePaths(end_vertex=end_vertex, edge_cost=edge_cost))
        return node.next_vertex_index, node.total_cost


    def split_edges(self, selection=None):
        """

        > Node: [Split Edges](GeometryNodeSplitEdges.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.SplitEdges(mesh=self, selection=selection))


    def subdivide(self, level=None):
        """

        > Node: [Subdivide Mesh](GeometryNodeSubdivideMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)

        #### Args:
        - level: Integer

        #### Returns:
        - self


        """

        return self.stack(nodes.SubdivideMesh(mesh=self, level=level))


    def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):
        """

        > Node: [Subdivision Surface](GeometryNodeSubdivisionSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)

        #### Args:
        - level: Integer
        - edge_crease: Float
        - vertex_crease: Float
        - boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
        - uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

        #### Returns:
        - self


        """

        return self.stack(nodes.SubdivisionSurface(mesh=self, level=level, edge_crease=edge_crease, vertex_crease=vertex_crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth))


    def to_curve(self, selection=None):
        """

        > Node: [Mesh to Curve](GeometryNodeMeshToCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - socket `curve` of class Curve


        """

        import geonodes as gn
        return gn.Curve(nodes.MeshToCurve(mesh=self, selection=selection).curve)


    def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):
        """

        > Node: [Mesh to Points](GeometryNodeMeshToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

        #### Args:
        - selection: Boolean
        - position: Vector
        - radius: Float
        - mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode).points)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
        """

        > Node: [Mesh to Volume](GeometryNodeMeshToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

        #### Args:
        - density: Float
        - voxel_size: Float
        - voxel_amount: Float
        - exterior_band_width: Float
        - interior_band_width: Float
        - fill_volume: Boolean
        - resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.MeshToVolume(mesh=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode).volume)


    def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """

        > Node: [Triangulate](GeometryNodeTriangulate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

        #### Args:
        - selection: Boolean
        - minimum_vertices: Integer
        - ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
        - quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

        #### Returns:
        - self


        """

        return self.stack(nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))


    def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """

        > Node: [UV Unwrap](GeometryNodeUVUnwrap.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

        #### Args:
        - selection: Boolean
        - seam: Boolean
        - margin: Float
        - fill_holes: Boolean
        - method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

        #### Returns:
        - socket `uv`


        """

        return self.attribute_node(nodes.UvUnwrap(selection=selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method)).uv


    def vertex_of_corner(self, corner_index=None):
        """

        > Node: [Vertex of Corner](GeometryNodeVertexOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

        #### Args:
        - corner_index: Integer

        #### Returns:
        - socket `vertex_index`


        """

        return self.attribute_node(nodes.VertexOfCorner(corner_index=corner_index)).vertex_index




class Curve(Geometry):
    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """

        > Node: [Arc](GeometryNodeCurveArc.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

        #### Args:
        - resolution: Integer
        - radius: Float
        - start_angle: Float
        - sweep_angle: Float
        - connect_center: Boolean
        - invert_arc: Boolean

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.Arc(resolution=resolution, start=None, middle=None, end=None, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, offset_angle=None, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    @classmethod
    def ArcFromPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """

        > Node: [Arc](GeometryNodeCurveArc.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/arc.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)

        #### Args:
        - resolution: Integer
        - start: Vector
        - middle: Vector
        - end: Vector
        - offset_angle: Float
        - connect_center: Boolean
        - invert_arc: Boolean

        #### Returns:
        - node with sockets ['curve', 'center', 'normal', 'radius']


        """

        return nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, radius=None, start_angle=None, sweep_angle=None, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')


    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """

        > Node: [Bezier Segment](GeometryNodeCurvePrimitiveBezierSegment.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)

        #### Args:
        - resolution: Integer
        - start: Vector
        - start_handle: Vector
        - end_handle: Vector
        - end: Vector
        - mode (str): 'POSITION' in [POSITION, OFFSET]

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)


    @classmethod
    def Circle(cls, resolution=None, radius=None):
        """

        > Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

        #### Args:
        - resolution: Integer
        - radius: Float

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.CurveCircle(resolution=resolution, point_1=None, point_2=None, point_3=None, radius=radius, mode='RADIUS').curve)


    @staticmethod
    def CircleFromPoints(resolution=None, point_1=None, point_2=None, point_3=None):
        """

        > Node: [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)

        #### Args:
        - resolution: Integer
        - point_1: Vector
        - point_2: Vector
        - point_3: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

        #### Returns:
        - tuple ('`curve`', '`center`')


        """

        import geonodes as gn
        node = nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=None, mode='POINTS')
        return gn.Curve(node.curve), node.center


    @classmethod
    def Line(cls, start=None, end=None):
        """

        > Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

        #### Args:
        - start: Vector
        - end: Vector

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.CurveLine(start=start, end=end, direction=None, length=None, mode='POINTS').curve)


    @classmethod
    def LineDirection(cls, start=None, direction=None, length=None):
        """

        > Node: [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)

        #### Args:
        - start: Vector
        - direction: Vector
        - length: Float

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.CurveLine(start=start, end=None, direction=direction, length=length, mode='DIRECTION').curve)


    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """

        > Node: [Quadratic Bezier](GeometryNodeCurveQuadraticBezier.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)

        #### Args:
        - resolution: Integer
        - start: Vector
        - middle: Vector
        - end: Vector

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)


    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """

        > Node: [Quadrilateral](GeometryNodeCurvePrimitiveQuadrilateral.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadrilateral.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)

        #### Args:
        - width: Float
        - height: Float
        - bottom_width: Float
        - top_width: Float
        - offset: Float
        - bottom_height: Float
        - top_height: Float
        - point_1: Vector
        - point_2: Vector
        - point_3: Vector
        - point_4: Vector
        - mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)


    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """

        > Node: [Spiral](GeometryNodeCurveSpiral.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/curve_spiral.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)

        #### Args:
        - resolution: Integer
        - rotations: Float
        - start_radius: Float
        - end_radius: Float
        - height: Float
        - reverse: Boolean

        #### Returns:
        - socket `curve`


        """

        return cls(nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)


    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """

        > Node: [Star](GeometryNodeCurveStar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)

        #### Args:
        - points: Integer
        - inner_radius: Float
        - outer_radius: Float
        - twist: Float

        #### Returns:
        - node with sockets ['curve', 'outer_points']


        """

        return nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)


    def curve_of_point(self, point_index=None):
        """

        > Node: [Curve of Point](GeometryNodeCurveOfPoint.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

        #### Args:
        - point_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

        #### Returns:
        - tuple ('`curve_index`', '`index_in_curve`')


        """

        node = self.attribute_node(nodes.CurveOfPoint(point_index=point_index))
        return node.curve_index, node.index_in_curve


    def deform_on_surface(self):
        """

        > Node: [Deform Curves on Surface](GeometryNodeDeformCurvesOnSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/deform_curves_on_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)

        #### Returns:
        - self


        """

        return self.stack(nodes.DeformCurvesOnSurface(curves=self))


    @property
    def domain_size(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize


    def fill(self, mode='TRIANGLES'):
        """

        > Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

        #### Args:
        - mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=self, mode=mode).mesh)


    def fill_ngons(self):
        """

        > Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=self, mode='NGONS').mesh)


    def fill_triangles(self):
        """

        > Node: [Fill Curve](GeometryNodeFillCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.FillCurve(curve=self, mode='TRIANGLES').mesh)


    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """

        > Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

        #### Args:
        - count: Integer
        - radius: Float
        - limit_radius: Boolean
        - mode (str): 'BEZIER' in [BEZIER, POLY]

        #### Returns:
        - self


        """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))


    def fillet_bezier(self, radius=None, limit_radius=None):
        """

        > Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

        #### Args:
        - radius: Float
        - limit_radius: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.FilletCurve(curve=self, count=1, radius=radius, limit_radius=limit_radius, mode='BEZIER'))


    def fillet_poly(self, count=None, radius=None, limit_radius=None):
        """

        > Node: [Fillet Curve](GeometryNodeFilletCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)

        #### Args:
        - count: Integer
        - radius: Float
        - limit_radius: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode='POLY'))


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - selection: Boolean
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    @property
    def length(self):
        """

        > Node: [Curve Length](GeometryNodeCurveLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)

        #### Returns:
        - socket `length`


        """

        return nodes.CurveLength(curve=self).length


    def offset_point(self, point_index=None, offset=None):
        """

        > Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

        #### Args:
        - point_index: Integer
        - offset: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

        #### Returns:
        - tuple ('`is_valid_offset`', '`point_index`')


        """

        node = self.attribute_node(nodes.OffsetPointInCurve(point_index=point_index, offset=offset))
        return node.is_valid_offset, node.point_index


    @property
    def point_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize.point_count


    def points_of_curve(self, curve_index=None, weights=None, sort_index=None):
        """

        > Node: [Points of Curve](GeometryNodePointsOfCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

        #### Args:
        - curve_index: Integer
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

        #### Returns:
        - tuple ('`point_index`', '`total`')


        """

        node = self.attribute_node(nodes.PointsOfCurve(curve_index=curve_index, weights=weights, sort_index=sort_index))
        return node.point_index, node.total


    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - selection: Boolean
        - count: Integer
        - length: Float
        - mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

        #### Returns:
        - self


        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))


    def resample_count(self, selection=None, count=None):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - selection: Boolean
        - count: Integer

        #### Returns:
        - self


        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=0.1, mode='COUNT'))


    def resample_evaluated(self, selection=None):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=10, length=0.1, mode='EVALUATED'))


    def resample_length(self, selection=None, length=None):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - selection: Boolean
        - length: Float

        #### Returns:
        - self


        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=10, length=length, mode='LENGTH'))


    def reverse(self, selection=None):
        """

        > Node: [Reverse Curve](GeometryNodeReverseCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.ReverseCurve(curve=self, selection=selection))


    def sample(self, value=None, factor=None, length=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False):
        """

        > Node: [Sample Curve](GeometryNodeSampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - factor: Float
        - length: Float
        - curve_index: Integer
        - data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
        - mode (str): 'FACTOR' in [FACTOR, LENGTH]
        - use_all_curves (bool): False

        #### Returns:
        - self


        """

        return self.stack(nodes.SampleCurve(curves=self, value=value, factor=factor, length=length, curve_index=curve_index, data_type=data_type, mode=mode, use_all_curves=use_all_curves))


    @property
    def spline_count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `spline_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='CURVE')
        return self._c_geometrynodeattributedomainsize.spline_count


    def subdivide(self, cuts=None):
        """

        > Node: [Subdivide Curve](GeometryNodeSubdivideCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)

        #### Args:
        - cuts: Integer

        #### Returns:
        - self


        """

        return self.stack(nodes.SubdivideCurve(curve=self, cuts=cuts))


    def to_mesh(self, profile_curve=None, fill_caps=None):
        """

        > Node: [Curve to Mesh](GeometryNodeCurveToMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)

        #### Args:
        - profile_curve: Geometry
        - fill_caps: Boolean

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh)


    def to_points(self, count=None, length=None, mode='COUNT'):
        """

        > Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

        #### Args:
        - count: Integer
        - length: Float
        - mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

        #### Returns:
        - tuple ('`points`', '`tangent`', '`normal`', '`rotation`')


        """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_count(self, count=None):
        """

        > Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

        #### Args:
        - count: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

        #### Returns:
        - tuple ('`points`', '`tangent`', '`normal`', '`rotation`')


        """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=count, length=0.1, mode='COUNT')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_evaluated(self):
        """

        > Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

        #### Returns:
        - tuple ('`points`', '`tangent`', '`normal`', '`rotation`')


        """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=10, length=0.1, mode='EVALUATED')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def to_points_length(self, length=None):
        """

        > Node: [Curve to Points](GeometryNodeCurveToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)

        #### Args:
        - length: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

        #### Returns:
        - tuple ('`points`', '`tangent`', '`normal`', '`rotation`')


        """

        import geonodes as gn
        node = nodes.CurveToPoints(curve=self, count=10, length=length, mode='LENGTH')
        return gn.Points(node.points), node.tangent, node.normal, node.rotation


    def trim(self, start=None, end=None, mode='FACTOR'):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - mode (str): 'FACTOR' in [FACTOR, LENGTH]

        #### Returns:
        - self


        """

        return self.stack(nodes.TrimCurve(curve=self, start0=start, start1=start, end0=start, end1=end, mode=mode))


    def trim_factor(self, start=None, end=None):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - start: Float
        - end: Float

        #### Returns:
        - self


        """

        return self.stack(nodes.TrimCurve(curve=self, start0=start, start1=None, end0=end, end1=None, mode='FACTOR'))


    def trim_length(self, start=None, end=None):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - start: Float
        - end: Float

        #### Returns:
        - self


        """

        return self.stack(nodes.TrimCurve(curve=self, start0=None, start1=start, end0=None, end1=end, mode='LENGTH'))




class Points(Geometry):
    @classmethod
    def Points(cls, count=None, position=None, radius=None):
        """

        > Node: [Points](GeometryNodePoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)

        #### Args:
        - count: Integer
        - position: Vector
        - radius: Float

        #### Returns:
        - socket `geometry`


        """

        return cls(nodes.Points(count=count, position=position, radius=radius).geometry)


    @property
    def domain_size(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='POINTCLOUD')
        return self._c_geometrynodeattributedomainsize.point_count


    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - selection: Boolean
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def set_point_radius(self, selection=None, radius=None):
        """

        > Node: [Set Point Radius](GeometryNodeSetPointRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

        #### Args:
        - selection: Boolean
        - radius: Float

        #### Returns:
        - self


        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius))


    def to_vertices(self, selection=None):
        """

        > Node: [Points to Vertices](GeometryNodePointsToVertices.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

        #### Args:
        - selection: Boolean

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.PointsToVertices(points=self, selection=selection).mesh)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """

        > Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

        #### Args:
        - density: Float
        - voxel_size: Float
        - voxel_amount: Float
        - radius: Float
        - resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume)


    def to_volume_amount(self, density=None, voxel_amount=None, radius=None):
        """

        > Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

        #### Args:
        - density: Float
        - voxel_amount: Float
        - radius: Float

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=None, voxel_amount=voxel_amount, radius=radius, resolution_mode='VOXEL_AMOUNT').volume)


    def to_volume_size(self, density=None, voxel_size=None, radius=None):
        """

        > Node: [Points to Volume](GeometryNodePointsToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)

        #### Args:
        - density: Float
        - voxel_size: Float
        - radius: Float

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=None, radius=radius, resolution_mode='VOXEL_SIZE').volume)




class Instances(Geometry):
    @classmethod
    def InstanceOnPoints(cls, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - points: Points
        - selection: Boolean
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return cls(nodes.InstanceOnPoints(points=points, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    @property
    def domain_size(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `instance_count`


        """

        if not hasattr(self, '_c_geometrynodeattributedomainsize'):
            self._c_geometrynodeattributedomainsize = nodes.DomainSize(geometry=self, component='INSTANCES')
        return self._c_geometrynodeattributedomainsize.instance_count


    def on_points(self, points=None, selection=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - points: Points
        - selection: Boolean
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=points, selection=selection, instance=self, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def realize(self, legacy_behavior=False):
        """

        > Node: [Realize Instances](GeometryNodeRealizeInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)

        #### Args:
        - legacy_behavior (bool): False

        #### Returns:
        - socket `geometry`


        """

        return nodes.RealizeInstances(geometry=self, legacy_behavior=legacy_behavior).geometry


    def rotate(self, selection=None, rotation=None, pivot_point=None, local_space=None):
        """

        > Node: [Rotate Instances](GeometryNodeRotateInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)

        #### Args:
        - selection: Boolean
        - rotation: Vector
        - pivot_point: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.RotateInstances(instances=self, selection=selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))


    @property
    def rotation(self):
        """

        > Node: [Instance Rotation](GeometryNodeInputInstanceRotation.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)

        #### Returns:
        - socket `rotation`


        """

        return self.attribute_node(nodes.InstanceRotation()).rotation


    @property
    def scale(self):
        """

        > Node: [Instance Scale](GeometryNodeInputInstanceScale.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)

        #### Returns:
        - socket `scale`


        """

        return self.attribute_node(nodes.InstanceScale()).scale


    def set_scale(self, selection=None, scale=None, center=None, local_space=None):
        """

        > Node: [Scale Instances](GeometryNodeScaleInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)

        #### Args:
        - selection: Boolean
        - scale: Vector
        - center: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.ScaleInstances(instances=self, selection=selection, scale=scale, center=center, local_space=local_space))


    def to_points(self, selection=None, position=None, radius=None):
        """

        > Node: [Instances to Points](GeometryNodeInstancesToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)

        #### Args:
        - selection: Boolean
        - position: Vector
        - radius: Float

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.InstancesToPoints(instances=self, selection=selection, position=position, radius=radius).points)


    def translate(self, selection=None, translation=None, local_space=None):
        """

        > Node: [Translate Instances](GeometryNodeTranslateInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)

        #### Args:
        - selection: Boolean
        - translation: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.stack(nodes.TranslateInstances(instances=self, selection=selection, translation=translation, local_space=local_space))




class Float(geosocks.Float):
    @classmethod
    def Frame(cls):
        """

        > Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

        #### Returns:
        - socket `frame`


        """

        return cls(nodes.SceneTime().frame)


    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return cls(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT').value)


    @classmethod
    def Seconds(cls):
        """

        > Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

        #### Returns:
        - socket `seconds`


        """

        return cls(nodes.SceneTime().seconds)


    @classmethod
    def Value(cls):
        """

        > Node: [Value](ShaderNodeValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)

        #### Returns:
        - socket `value`


        """

        return cls(nodes.Value().value)


    def abs(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def absolute(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def arccos(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arccosine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arcsin(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arcsine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arctan(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def arctan2(self, value1=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value1: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp).value


    def arctangent(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def ceiling(self):
        """

        > Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        #### Returns:
        - socket `integer`


        """

        return nodes.FloatToInteger(float=self, rounding_mode='CEILING').integer


    def clamp(self, min=None, max=None, clamp_type='MINMAX'):
        """

        > Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        #### Args:
        - min: Float
        - max: Float
        - clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

        #### Returns:
        - socket `result`


        """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type).result


    def clamp_min_max(self, min=None, max=None):
        """

        > Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        #### Args:
        - min: Float
        - max: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type='MINMAX').result


    def clamp_range(self, min=None, max=None):
        """

        > Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

        #### Args:
        - min: Float
        - max: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Clamp(value=self, min=min, max=max, clamp_type='RANGE').result


    @property
    def color_ramp(self):
        """

        > Node: [ColorRamp](ShaderNodeValToRGB.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

        #### Returns:
        - node with sockets ['color', 'alpha']


        """

        return nodes.ColorRamp(fac=self)


    def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float
        - operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation=operation).result


    def cos(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def cosh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp).value


    def cosine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL').result


    def exp(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def exponent(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def fact(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def float_curve(self, factor=None):
        """

        > Node: [Float Curve](ShaderNodeFloatCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)

        #### Args:
        - factor: Float

        #### Returns:
        - socket `value`


        """

        return nodes.FloatCurve(factor=factor, value=self).value


    def floor(self):
        """

        > Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        #### Returns:
        - socket `integer`


        """

        return nodes.FloatToInteger(float=self, rounding_mode='FLOOR').integer


    def fraction(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def greater_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL').result


    def greater_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN').result


    def inverse_sqrt(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp).value


    def less_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL').result


    def less_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN').result


    def log(self, base=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - base: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def logarithm(self, base=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - base: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - steps: ['Float', 'Vector']
        - clamp (bool): True
        - interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

        #### Returns:
        - socket `result`


        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type).result


    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='LINEAR').result


    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHSTEP').result


    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='SMOOTHERSTEP').result


    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - steps: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=None, clamp=clamp, data_type='FLOAT', interpolation_type='STEPPED').result


    def math_ceil(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp).value


    def math_compare(self, value=None, epsilon=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - epsilon: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp).value


    def math_floor(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp).value


    def math_greater_than(self, threshold=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - threshold: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp).value


    def math_less_than(self, threshold=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - threshold: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp).value


    def math_round(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp).value


    def math_trunc(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def math_truncate(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def max(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def maximum(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def min(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def minimum(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def mix(self, factor=None, value=None, clamp_factor=True):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - value: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=value, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM').result


    def modulo(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp).value


    def mul_add(self, multiplier=None, addend=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - multiplier: Float
        - addend: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def multiply_add(self, multiplier=None, addend=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - multiplier: Float
        - addend: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def not_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL').result


    def ping_pong(self, scale=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - scale: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp).value


    def pow(self, exponent=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - exponent: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def power(self, exponent=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - exponent: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def round(self):
        """

        > Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        #### Returns:
        - socket `integer`


        """

        return nodes.FloatToInteger(float=self, rounding_mode='ROUND').integer


    def sign(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp).value


    def sin(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sinh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp).value


    def smooth_maximum(self, value=None, distance=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - distance: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp).value


    def smooth_minimum(self, value=None, distance=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - distance: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp).value


    def snap(self, increment=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - increment: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp).value


    def sqrt(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp).value


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Float

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='FLOAT').output


    def tan(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tangent(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tanh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp).value


    def to_degrees(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp).value


    def to_integer(self, rounding_mode='ROUND'):
        """

        > Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        #### Args:
        - rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

        #### Returns:
        - socket `integer`


        """

        return nodes.FloatToInteger(float=self, rounding_mode=rounding_mode).integer


    def to_radians(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp).value


    def to_string(self, decimals=None):
        """

        > Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

        #### Args:
        - decimals: Integer

        #### Returns:
        - socket `string`


        """

        return nodes.ValueToString(value=self, decimals=decimals).string


    def truncate(self):
        """

        > Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

        #### Returns:
        - socket `integer`


        """

        return nodes.FloatToInteger(float=self, rounding_mode='TRUNCATE').integer


    def wrap(self, max=None, min=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - max: Float
        - min: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp).value




class Color(geosocks.Color):
    @classmethod
    def Color(cls):
        """

        > Node: [Color](FunctionNodeInputColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)

        #### Returns:
        - socket `color`


        """

        return cls(nodes.Color().color)


    @classmethod
    def HSL(cls, hue=None, saturation=None, lightness=None, alpha=None):
        """

        > Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

        #### Args:
        - hue: Float
        - saturation: Float
        - lightness: Float
        - alpha: Float

        #### Returns:
        - socket `color`


        """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=lightness, alpha=alpha, mode='HSV').color)


    @classmethod
    def HSV(cls, hue=None, saturation=None, value=None, alpha=None):
        """

        > Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

        #### Args:
        - hue: Float
        - saturation: Float
        - value: Float
        - alpha: Float

        #### Returns:
        - socket `color`


        """

        return cls(nodes.CombineColor(red=hue, green=saturation, blue=value, alpha=alpha, mode='HSV').color)


    @classmethod
    def RGB(cls, red=None, green=None, blue=None, alpha=None):
        """

        > Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

        #### Args:
        - red: Float
        - green: Float
        - blue: Float
        - alpha: Float

        #### Returns:
        - socket `color`


        """

        return cls(nodes.CombineColor(red=red, green=green, blue=blue, alpha=alpha, mode='RGB').color)


    def brighter(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='RGBA', mode='ELEMENT', operation='BRIGHTER').result


    def darker(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='RGBA', mode='ELEMENT', operation='DARKER').result


    def equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result


    def equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='RGBA', mode='ELEMENT', operation='EQUAL').result


    def mix(self, factor=None, color=None, blend_type='MIX', clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type=blend_type, clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_add(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='ADD', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_burn(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='BURN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_color(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='COLOR', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_darken(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DARKEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_difference(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DIFFERENCE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_divide(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DIVIDE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_dodge(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='DODGE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_hue(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='HUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_lighten(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='LIGHTEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_linear_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='LINEAR_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_multiply(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='MULTIPLY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_overlay(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='OVERLAY', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_saturation(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SATURATION', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_screen(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SCREEN', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_soft_light(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SOFT_LIGHT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_subtract(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='SUBTRACT', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    def mix_value(self, factor=None, color=None, clamp_factor=True, clamp_result=False):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - color: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - clamp_result (bool): False

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=color, blend_type='VALUE', clamp_factor=clamp_factor, clamp_result=clamp_result, data_type='RGBA', factor_mode='UNIFORM').result


    @property
    def rgb_curves(self, fac=None):
        """

        > Node: [RGB Curves](ShaderNodeRGBCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

        #### Returns:
        - node with sockets ['color']


        """

        return nodes.RgbCurves(fac=fac, color=self)


    def separate_color(self, mode='RGB'):
        """

        > Node: [Separate Color](FunctionNodeSeparateColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

        #### Args:
        - mode (str): 'RGB' in [RGB, HSV, HSL]

        #### Returns:
        - node with sockets ['red', 'green', 'blue', 'alpha']


        """

        return nodes.SeparateColor(color=self, mode=mode)


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Color

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='RGBA').output




class Vector(geosocks.Vector):
    @classmethod
    def AlignToVector(cls, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """

        > Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

        #### Args:
        - factor: Float
        - vector: Vector
        - axis (str): 'X' in [X, Y, Z]
        - pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

        #### Returns:
        - socket `rotation`


        """

        return cls(nodes.AlignEulerToVector(rotation=None, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis).rotation)


    @classmethod
    def Combine(cls, x=None, y=None, z=None):
        """

        > Node: [Combine XYZ](ShaderNodeCombineXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)

        #### Args:
        - x: Float
        - y: Float
        - z: Float

        #### Returns:
        - socket `vector`


        """

        return cls(nodes.CombineXyz(x=x, y=y, z=z).vector)


    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return cls(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value)


    @classmethod
    def Vector(cls, vector=[0.0, 0.0, 0.0]):
        """

        > Node: [Vector](FunctionNodeInputVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)

        #### Args:
        - vector (list): [0.0, 0.0, 0.0]

        #### Returns:
        - socket `vector`


        """

        return cls(nodes.Vector(vector=vector).vector)


    def abs(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE').vector


    def absolute(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='ABSOLUTE').vector


    def add(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='ADD').vector


    def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):
        """

        > Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

        #### Args:
        - factor: Float
        - vector: Vector
        - axis (str): 'X' in [X, Y, Z]
        - pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

        #### Returns:
        - self


        """

        return self.stack(nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis))


    def average_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='EQUAL').result


    def average_greater_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_EQUAL').result


    def average_greater_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='GREATER_THAN').result


    def average_less_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_EQUAL').result


    def average_less_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='AVERAGE', operation='LESS_THAN').result


    def average_not_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='AVERAGE', operation='NOT_EQUAL').result


    def ceil(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='CEIL').vector


    def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float
        - angle: Float
        - epsilon: Float
        - mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
        - operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation=operation).result


    def cos(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE').vector


    def cosine(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='COSINE').vector


    def cross(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT').vector


    def cross_product(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='CROSS_PRODUCT').vector


    def curves(self, fac=None):
        """

        > Node: [Vector Curves](ShaderNodeVectorCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)

        #### Args:
        - fac: Float

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorCurves(fac=fac, vector=self).vector


    def direction_equal(self, b=None, angle=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='EQUAL').result


    def direction_greater_equal(self, b=None, angle=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_EQUAL').result


    def direction_greater_than(self, b=None, angle=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='GREATER_THAN').result


    def direction_less_equal(self, b=None, angle=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_EQUAL').result


    def direction_less_than(self, b=None, angle=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=None, data_type='VECTOR', mode='DIRECTION', operation='LESS_THAN').result


    def direction_not_equal(self, b=None, angle=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - angle: Float
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=angle, epsilon=epsilon, data_type='VECTOR', mode='DIRECTION', operation='NOT_EQUAL').result


    def distance(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `value`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DISTANCE').value


    def div(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE').vector


    def divide(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DIVIDE').vector


    def dot(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `value`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT').value


    def dot_product(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `value`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='DOT_PRODUCT').value


    def dot_product_equal(self, b=None, c=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='EQUAL').result


    def dot_product_greater_equal(self, b=None, c=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_EQUAL').result


    def dot_product_greater_than(self, b=None, c=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='GREATER_THAN').result


    def dot_product_less_equal(self, b=None, c=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_EQUAL').result


    def dot_product_less_than(self, b=None, c=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=None, data_type='VECTOR', mode='DOT_PRODUCT', operation='LESS_THAN').result


    def dot_product_not_equal(self, b=None, c=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - c: Float
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=c, angle=None, epsilon=epsilon, data_type='VECTOR', mode='DOT_PRODUCT', operation='NOT_EQUAL').result


    def elements_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='EQUAL').result


    def elements_greater_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_EQUAL').result


    def elements_greater_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='GREATER_THAN').result


    def elements_less_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_EQUAL').result


    def elements_less_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='ELEMENT', operation='LESS_THAN').result


    def elements_not_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='ELEMENT', operation='NOT_EQUAL').result


    def face_forward(self, incident=None, reference=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - incident: Vector
        - reference: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=incident, vector2=reference, scale=None, operation='FACEFORWARD').vector


    def floor(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FLOOR').vector


    def fract(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION').vector


    def fraction(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='FRACTION').vector


    @property
    def length(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `value`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='LENGTH').value


    def length_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='EQUAL').result


    def length_greater_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_EQUAL').result


    def length_greater_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='GREATER_THAN').result


    def length_less_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_EQUAL').result


    def length_less_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='VECTOR', mode='LENGTH', operation='LESS_THAN').result


    def length_not_equal(self, b=None, epsilon=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - epsilon: Float

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=epsilon, data_type='VECTOR', mode='LENGTH', operation='NOT_EQUAL').result


    def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - steps: ['Float', 'Vector']
        - clamp (bool): True
        - interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

        #### Returns:
        - socket `vector`


        """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type).vector


    def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `vector`


        """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='LINEAR').vector


    def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `vector`


        """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHSTEP').vector


    def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `vector`


        """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=None, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='SMOOTHERSTEP').vector


    def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):
        """

        > Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

        #### Args:
        - from_min: ['Float', 'Vector']
        - from_max: ['Float', 'Vector']
        - to_min: ['Float', 'Vector']
        - to_max: ['Float', 'Vector']
        - steps: ['Float', 'Vector']
        - clamp (bool): True

        #### Returns:
        - socket `vector`


        """

        return nodes.MapRange(value=None, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, steps=steps, vector=self, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type='STEPPED').vector


    def max(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM').vector


    def maximum(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MAXIMUM').vector


    def min(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM').vector


    def minimum(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MINIMUM').vector


    def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - vector: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True
        - factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode=factor_mode).result


    def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - factor: ['Float', 'Vector']
        - vector: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=factor, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='NON_UNIFORM').result


    def mix_uniform(self, vector=None, clamp_factor=True):
        """

        > Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

        #### Args:
        - vector: ['Float', 'Vector', 'Color']
        - clamp_factor (bool): True

        #### Returns:
        - socket `result`


        """

        return nodes.Mix(factor=None, a=self, b=vector, blend_type='MIX', clamp_factor=clamp_factor, clamp_result=False, data_type='VECTOR', factor_mode='UNIFORM').result


    def modulo(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MODULO').vector


    def mul(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY').vector


    def mul_add(self, multiplier=None, addend=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - multiplier: Vector
        - addend: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD').vector


    def multiply(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='MULTIPLY').vector


    def multiply_add(self, multiplier=None, addend=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - multiplier: Vector
        - addend: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=multiplier, vector2=addend, scale=None, operation='MULTIPLY_ADD').vector


    def normalize(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='NORMALIZE').vector


    def project(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='PROJECT').vector


    def reflect(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='REFLECT').vector


    def refract(self, vector=None, ior=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector
        - ior: Float

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=ior, operation='REFRACT').vector


    def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):
        """

        > Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

        #### Args:
        - center: Vector
        - axis: Vector
        - angle: Float
        - invert (bool): False

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=None, invert=invert, rotation_type='AXIS_ANGLE').vector


    def rotate_euler(self, center=None, rotation=None, invert=False):
        """

        > Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

        #### Args:
        - center: Vector
        - rotation: Vector
        - invert (bool): False

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=None, rotation=rotation, invert=invert, rotation_type='EULER_XYZ').vector


    def rotate_x(self, center=None, angle=None, invert=False):
        """

        > Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

        #### Args:
        - center: Vector
        - angle: Float
        - invert (bool): False

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='X_AXIS').vector


    def rotate_y(self, center=None, angle=None, invert=False):
        """

        > Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

        #### Args:
        - center: Vector
        - angle: Float
        - invert (bool): False

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Y_AXIS').vector


    def rotate_z(self, center=None, angle=None, invert=False):
        """

        > Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

        #### Args:
        - center: Vector
        - angle: Float
        - invert (bool): False

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Z_AXIS').vector


    def scale(self, scale=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - scale: Float

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=scale, operation='SCALE').vector


    @property
    def separate(self):
        """

        > Node: [Separate XYZ](ShaderNodeSeparateXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)

        #### Returns:
        - node with sockets ['x', 'y', 'z']


        """

        if not hasattr(self, '_c_shadernodeseparatexyz'):
            self._c_shadernodeseparatexyz = nodes.SeparateXyz(vector=self)
        return self._c_shadernodeseparatexyz


    def sin(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE').vector


    def sine(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='SINE').vector


    def snap(self, increment=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - increment: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=increment, vector2=None, scale=None, operation='SNAP').vector


    def sub(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT').vector


    def subtract(self, vector=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - vector: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=vector, vector2=None, scale=None, operation='SUBTRACT').vector


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Vector

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='VECTOR').output


    def tan(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT').vector


    def tangent(self):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=None, vector2=None, scale=None, operation='TANGENT').vector


    def wrap(self, max=None, min=None):
        """

        > Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

        #### Args:
        - max: Vector
        - min: Vector

        #### Returns:
        - socket `vector`


        """

        return nodes.VectorMath(vector0=self, vector1=max, vector2=min, scale=None, operation='WRAP').vector




class Boolean(geosocks.Boolean):
    @classmethod
    def Boolean(cls, boolean=False):
        """

        > Node: [Boolean](FunctionNodeInputBool.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)

        #### Args:
        - boolean (bool): False

        #### Returns:
        - socket `boolean`


        """

        return cls(nodes.Boolean(boolean=boolean).boolean)


    @classmethod
    def Random(cls, probability=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - probability: Float
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return cls(nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value)


    def b_and(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND').boolean


    def b_not(self):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=None, operation='NOT').boolean


    def b_or(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR').boolean


    def imply(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY').boolean


    def nand(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND').boolean


    def nimply(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY').boolean


    def nor(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR').boolean


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Boolean

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='BOOLEAN').output


    def xnor(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR').boolean


    def xor(self, boolean1=None):
        """

        > Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

        #### Args:
        - boolean1: Boolean

        #### Returns:
        - socket `boolean`


        """

        return nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR').boolean




class Integer(geosocks.Integer):
    @classmethod
    def Integer(cls, integer=0):
        """

        > Node: [Integer](FunctionNodeInputInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)

        #### Args:
        - integer (int): 0

        #### Returns:
        - socket `integer`


        """

        return cls(nodes.Integer(integer=integer).integer)


    @classmethod
    def Random(cls, min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return cls(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='IN').value)


    def abs(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def absolute(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ABSOLUTE', use_clamp=clamp).value


    def arccos(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arccosine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCCOSINE', use_clamp=clamp).value


    def arcsin(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arcsine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCSINE', use_clamp=clamp).value


    def arctan(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def arctan2(self, value1=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value1: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value1, value2=None, operation='ARCTAN2', use_clamp=clamp).value


    def arctangent(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='ARCTANGENT', use_clamp=clamp).value


    def compare(self, b=None, operation='GREATER_THAN'):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']
        - operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation=operation).result


    def cos(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def cosh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSH', use_clamp=clamp).value


    def cosine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='COSINE', use_clamp=clamp).value


    def equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='EQUAL').result


    def exp(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def exponent(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='EXPONENT', use_clamp=clamp).value


    def fact(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def fraction(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FRACT', use_clamp=clamp).value


    def greater_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL').result


    def greater_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='GREATER_THAN').result


    def inverse_sqrt(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='INVERSE_SQRT', use_clamp=clamp).value


    def less_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL').result


    def less_than(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='LESS_THAN').result


    def log(self, base=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - base: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def logarithm(self, base=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - base: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=base, value2=None, operation='LOGARITHM', use_clamp=clamp).value


    def math_ceil(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='CEIL', use_clamp=clamp).value


    def math_compare(self, value=None, epsilon=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - epsilon: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=epsilon, operation='COMPARE', use_clamp=clamp).value


    def math_floor(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='FLOOR', use_clamp=clamp).value


    def math_greater_than(self, threshold=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - threshold: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='GREATER_THAN', use_clamp=clamp).value


    def math_less_than(self, threshold=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - threshold: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=threshold, value2=None, operation='LESS_THAN', use_clamp=clamp).value


    def math_round(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='ROUND', use_clamp=clamp).value


    def math_trunc(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def math_truncate(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='TRUNC', use_clamp=clamp).value


    def max(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def maximum(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MAXIMUM', use_clamp=clamp).value


    def min(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def minimum(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MINIMUM', use_clamp=clamp).value


    def modulo(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='MODULO', use_clamp=clamp).value


    def mul_add(self, multiplier=None, addend=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - multiplier: Float
        - addend: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def multiply_add(self, multiplier=None, addend=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - multiplier: Float
        - addend: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=multiplier, value2=addend, operation='MULTIPLY_ADD', use_clamp=clamp).value


    def not_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL').result


    def ping_pong(self, scale=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - scale: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=scale, value2=None, operation='PINGPONG', use_clamp=clamp).value


    def pow(self, exponent=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - exponent: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def power(self, exponent=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - exponent: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=exponent, value2=None, operation='POWER', use_clamp=clamp).value


    def sign(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SIGN', use_clamp=clamp).value


    def sin(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sine(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINE', use_clamp=clamp).value


    def sinh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='SINH', use_clamp=clamp).value


    def smooth_maximum(self, value=None, distance=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - distance: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MAX', use_clamp=clamp).value


    def smooth_minimum(self, value=None, distance=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - distance: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=distance, operation='SMOOTH_MIN', use_clamp=clamp).value


    def snap(self, increment=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - increment: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=increment, value2=None, operation='SNAP', use_clamp=clamp).value


    def sqrt(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='SQRT', use_clamp=clamp).value


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Integer

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='INT').output


    def tan(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tangent(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANGENT', use_clamp=clamp).value


    def tanh(self, value=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - value: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=value, value2=None, operation='TANH', use_clamp=clamp).value


    def to_degrees(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='DEGREES', use_clamp=clamp).value


    def to_radians(self, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=None, value2=None, operation='RADIANS', use_clamp=clamp).value


    def to_string(self):
        """

        > Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

        #### Returns:
        - socket `string`


        """

        return nodes.ValueToString(value=self, decimals=0).string


    def wrap(self, max=None, min=None, clamp=False):
        """

        > Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

        #### Args:
        - max: Float
        - min: Float
        - clamp (bool): False

        #### Returns:
        - socket `value`


        """

        return nodes.Math(value0=self, value1=max, value2=min, operation='WRAP', use_clamp=clamp).value




class Material(geosocks.Material):
    @classmethod
    def Material(cls):
        """

        > Node: [Material](GeometryNodeInputMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)

        #### Returns:
        - socket `material`


        """

        return cls(nodes.Material().material)


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Material

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='MATERIAL').output




class Object(geosocks.Object):
    @classmethod
    def Self(cls):
        """

        > Node: [Self Object](GeometryNodeSelfObject.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/self_object.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)

        #### Returns:
        - socket `self_object`


        """

        return cls(nodes.SelfObject().self_object)


    def geometry(self, as_instance=None, transform_space='ORIGINAL'):
        """

        > Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

        #### Args:
        - as_instance: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - socket `geometry`


        """

        return nodes.ObjectInfo(object=self.bobject, as_instance=as_instance, transform_space=transform_space).geometry


    def info(self, as_instance=None, transform_space='ORIGINAL'):
        """

        > Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

        #### Args:
        - as_instance: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - node with sockets ['location', 'rotation', 'scale', 'geometry']


        """

        return nodes.ObjectInfo(object=self.bobject, as_instance=as_instance, transform_space=transform_space)


    def location(self, as_instance=None, transform_space='ORIGINAL'):
        """

        > Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

        #### Args:
        - as_instance: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - socket `location`


        """

        return nodes.ObjectInfo(object=self.bobject, as_instance=as_instance, transform_space=transform_space).location


    def rotation(self, as_instance=None, transform_space='ORIGINAL'):
        """

        > Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

        #### Args:
        - as_instance: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - socket `rotation`


        """

        return nodes.ObjectInfo(object=self.bobject, as_instance=as_instance, transform_space=transform_space).rotation


    def scale(self, as_instance=None, transform_space='ORIGINAL'):
        """

        > Node: [Object Info](GeometryNodeObjectInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/object_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)

        #### Args:
        - as_instance: Boolean
        - transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

        #### Returns:
        - socket `scale`


        """

        return nodes.ObjectInfo(object=self.bobject, as_instance=as_instance, transform_space=transform_space).scale


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Object

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='OBJECT').output




class String(geosocks.String):
    @staticmethod
    def LineBreak():
        """

        > Node: [Special Characters](FunctionNodeInputSpecialCharacters.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)

        #### Returns:
        - socket `line_break`


        """

        return nodes.SpecialCharacters().line_break


    @classmethod
    def String(cls, string=''):
        """

        > Node: [String](FunctionNodeInputString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html)

        #### Args:
        - string (str): ''

        #### Returns:
        - socket `string`


        """

        return cls(nodes.String(string=string).string)


    @staticmethod
    def Tab():
        """

        > Node: [Special Characters](FunctionNodeInputSpecialCharacters.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)

        #### Returns:
        - socket `tab`


        """

        return nodes.SpecialCharacters().tab


    def equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='EQUAL').result


    def join(self, *strings):
        """

        > Node: [Join Strings](GeometryNodeStringJoin.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

        #### Args:
        - strings: <m>String

        #### Returns:
        - socket `string`


        """

        return nodes.JoinStrings(*strings, delimiter=self).string


    @property
    def length(self):
        """

        > Node: [String Length](FunctionNodeStringLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)

        #### Returns:
        - socket `length`


        """

        return nodes.StringLength(string=self).length


    def not_equal(self, b=None):
        """

        > Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

        #### Args:
        - b: ['Float', 'Integer', 'Vector', 'Color', 'String']

        #### Returns:
        - socket `result`


        """

        return nodes.Compare(a=self, b=b, c=None, angle=None, epsilon=None, data_type='STRING', mode='ELEMENT', operation='NOT_EQUAL').result


    def replace(self, find=None, replace=None):
        """

        > Node: [Replace String](FunctionNodeReplaceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)

        #### Args:
        - find: String
        - replace: String

        #### Returns:
        - socket `string`


        """

        return nodes.ReplaceString(string=self, find=find, replace=replace).string


    def slice(self, position=None, length=None):
        """

        > Node: [Slice String](FunctionNodeSliceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)

        #### Args:
        - position: Integer
        - length: Integer

        #### Returns:
        - socket `string`


        """

        return nodes.SliceString(string=self, position=position, length=length).string


    def string_join(*strings, delimiter=None):
        """

        > Node: [Join Strings](GeometryNodeStringJoin.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

        #### Args:
        - strings: <m>String
        - delimiter: String

        #### Returns:
        - socket `string`


        """

        return nodes.JoinStrings(*strings, delimiter=delimiter).string


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: String

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='STRING').output


    def to_curves(self, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):
        """

        > Node: [String to Curves](GeometryNodeStringToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)

        #### Args:
        - size: Float
        - character_spacing: Float
        - word_spacing: Float
        - line_spacing: Float
        - text_box_width: Float
        - text_box_height: Float
        - align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
        - align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
        - overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
        - pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

        #### Returns:
        - tuple ('`curve_instances`', '`line`', '`pivot_point`')


        """

        import geonodes as gn
        node = nodes.StringToCurves(string=self, size=size, character_spacing=character_spacing, word_spacing=word_spacing, line_spacing=line_spacing, text_box_width=text_box_width, text_box_height=text_box_height, align_x=align_x, align_y=align_y, overflow=overflow, pivot_mode=pivot_mode)
        return gn.Instances(node.curve_instances), node.line, node.pivot_point




class Volume(Geometry):
    @classmethod
    def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):
        """

        > Node: [Volume Cube](GeometryNodeVolumeCube.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)

        #### Args:
        - density: Float
        - background: Float
        - min: Vector
        - max: Vector
        - resolution_x: Integer
        - resolution_y: Integer
        - resolution_z: Integer

        #### Returns:
        - socket `volume`


        """

        return cls(nodes.VolumeCube(density=density, background=background, min=min, max=max, resolution_x=resolution_x, resolution_y=resolution_y, resolution_z=resolution_z).volume)


    def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM'):
        """

        > Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

        #### Args:
        - density: Float
        - seed: Integer
        - spacing: Vector
        - threshold: Float
        - mode (str): 'DENSITY_RANDOM' in [DENSITY_RANDOM, DENSITY_GRID]

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=spacing, threshold=threshold, mode=mode).points)


    def distribute_points_grid(self, spacing=None, threshold=None):
        """

        > Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

        #### Args:
        - spacing: Vector
        - threshold: Float

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=None, seed=None, spacing=spacing, threshold=threshold, mode='DENSITY_GRID').points)


    def distribute_points_random(self, density=None, seed=None):
        """

        > Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

        #### Args:
        - density: Float
        - seed: Integer

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=None, threshold=None, mode='DENSITY_RANDOM').points)


    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """

        > Node: [Volume to Mesh](GeometryNodeVolumeToMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)

        #### Args:
        - voxel_size: Float
        - voxel_amount: Float
        - threshold: Float
        - adaptivity: Float
        - resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh)




class Texture(geosocks.Texture):
    @staticmethod
    def brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2):
        """

        > Node: [Brick Texture](ShaderNodeTexBrick.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)

        #### Args:
        - vector: Vector
        - color1: Color
        - color2: Color
        - mortar: Color
        - scale: Float
        - mortar_size: Float
        - mortar_smooth: Float
        - bias: Float
        - brick_width: Float
        - row_height: Float
        - offset (float): 0.5
        - offset_frequency (int): 2
        - squash (float): 1.0
        - squash_frequency (int): 2

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexBrick.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.BrickTexture(vector=vector, color1=color1, color2=color2, mortar=mortar, scale=scale, mortar_size=mortar_size, mortar_smooth=mortar_smooth, bias=bias, brick_width=brick_width, row_height=row_height, offset=offset, offset_frequency=offset_frequency, squash=squash, squash_frequency=squash_frequency)
        return node.color, node.fac


    @staticmethod
    def checker(vector=None, color1=None, color2=None, scale=None):
        """

        > Node: [Checker Texture](ShaderNodeTexChecker.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)

        #### Args:
        - vector: Vector
        - color1: Color
        - color2: Color
        - scale: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.CheckerTexture(vector=vector, color1=color1, color2=color2, scale=scale)
        return node.color, node.fac


    @staticmethod
    def gradient(vector=None, gradient_type='LINEAR'):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector
        - gradient_type (str): 'LINEAR' in [LINEAR, QUADRATIC, EASING, DIAGONAL, SPHERICAL, QUADRATIC_SPHERE, RADIAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type=gradient_type)
        return node.color, node.fac


    @staticmethod
    def gradient_diagonal(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='DIAGONAL')
        return node.color, node.fac


    @staticmethod
    def gradient_easing(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='EASING')
        return node.color, node.fac


    @staticmethod
    def gradient_linear(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='LINEAR')
        return node.color, node.fac


    @staticmethod
    def gradient_quadratic(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC')
        return node.color, node.fac


    @staticmethod
    def gradient_quadratic_sphere(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='QUADRATIC_SPHERE')
        return node.color, node.fac


    @staticmethod
    def gradient_radial(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='RADIAL')
        return node.color, node.fac


    @staticmethod
    def gradient_spherical(vector=None):
        """

        > Node: [Gradient Texture](ShaderNodeTexGradient.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.GradientTexture(vector=vector, gradient_type='SPHERICAL')
        return node.color, node.fac


    @staticmethod
    def image(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """

        > Node: [Image Texture](GeometryNodeImageTexture.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

        #### Args:
        - image: Image
        - vector: Vector
        - frame: Integer
        - extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
        - interpolation (str): 'Linear' in [Linear, Closest, Cubic]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

        #### Returns:
        - tuple ('`color`', '`alpha`')


        """

        node = nodes.ImageTexture(image=image, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return node.color, node.alpha


    @staticmethod
    def magic(vector=None, scale=None, distortion=None, turbulence_depth=2):
        """

        > Node: [Magic Texture](ShaderNodeTexMagic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - turbulence_depth (int): 2

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.MagicTexture(vector=vector, scale=scale, distortion=distortion, turbulence_depth=turbulence_depth)
        return node.color, node.fac


    @staticmethod
    def musgrave(vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM'):
        """

        > Node: [Musgrave Texture](ShaderNodeTexMusgrave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)

        #### Args:
        - vector: Vector
        - w: Float
        - scale: Float
        - detail: Float
        - dimension: Float
        - lacunarity: Float
        - offset: Float
        - gain: Float
        - musgrave_dimensions (str): '3D' in [1D, 2D, 3D, 4D]
        - musgrave_type (str): 'FBM' in [MULTIFRACTAL, RIDGED_MULTIFRACTAL, HYBRID_MULTIFRACTAL, FBM, HETERO_TERRAIN]

        #### Returns:
        - socket `fac`


        """

        return nodes.MusgraveTexture(vector=vector, w=w, scale=scale, detail=detail, dimension=dimension, lacunarity=lacunarity, offset=offset, gain=gain, musgrave_dimensions=musgrave_dimensions, musgrave_type=musgrave_type).fac


    @staticmethod
    def noise(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D'):
        """

        > Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        #### Args:
        - vector: Vector
        - w: Float
        - scale: Float
        - detail: Float
        - roughness: Float
        - distortion: Float
        - noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions=noise_dimensions)
        return node.color, node.fac


    @staticmethod
    def noise_1D(w=None, scale=None, detail=None, roughness=None, distortion=None):
        """

        > Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        #### Args:
        - w: Float
        - scale: Float
        - detail: Float
        - roughness: Float
        - distortion: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.NoiseTexture(vector=None, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='1D')
        return node.color, node.fac


    @staticmethod
    def noise_2D(vector=None, scale=None, detail=None, roughness=None, distortion=None):
        """

        > Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - detail: Float
        - roughness: Float
        - distortion: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='2D')
        return node.color, node.fac


    @staticmethod
    def noise_3D(vector=None, scale=None, detail=None, roughness=None, distortion=None):
        """

        > Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - detail: Float
        - roughness: Float
        - distortion: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.NoiseTexture(vector=vector, w=None, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='3D')
        return node.color, node.fac


    @staticmethod
    def noise_4D(vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None):
        """

        > Node: [Noise Texture](ShaderNodeTexNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)

        #### Args:
        - vector: Vector
        - w: Float
        - scale: Float
        - detail: Float
        - roughness: Float
        - distortion: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.NoiseTexture(vector=vector, w=w, scale=scale, detail=detail, roughness=roughness, distortion=distortion, noise_dimensions='4D')
        return node.color, node.fac


    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Texture

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='TEXTURE').output


    @staticmethod
    def voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

        > Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        #### Args:
        - vector: Vector
        - w: Float
        - scale: Float
        - smoothness: Float
        - exponent: Float
        - randomness: Float
        - distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
        - feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
        - voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

        #### Returns:
        - tuple ('`distance`', '`color`', '`position`', '`w`')


        """

        node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position, node.w


    @staticmethod
    def voronoi_1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

        > Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        #### Args:
        - w: Float
        - scale: Float
        - smoothness: Float
        - exponent: Float
        - randomness: Float
        - distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
        - feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
        - voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

        #### Returns:
        - tuple ('`distance`', '`color`', '`w`')


        """

        node = nodes.VoronoiTexture(vector=None, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.w


    @staticmethod
    def voronoi_2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

        > Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - smoothness: Float
        - exponent: Float
        - randomness: Float
        - distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
        - feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
        - voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

        #### Returns:
        - tuple ('`distance`', '`color`', '`position`')


        """

        node = nodes.VoronoiTexture(vector=vector, w=None, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position


    @staticmethod
    def voronoi_3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

        > Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - smoothness: Float
        - exponent: Float
        - randomness: Float
        - distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
        - feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
        - voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

        #### Returns:
        - tuple ('`distance`', '`color`', '`position`')


        """

        node = nodes.VoronoiTexture(vector=vector, w=None, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position


    @staticmethod
    def voronoi_4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):
        """

        > Node: [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)

        #### Args:
        - vector: Vector
        - w: Float
        - scale: Float
        - smoothness: Float
        - exponent: Float
        - randomness: Float
        - distance (str): 'EUCLIDEAN' in [EUCLIDEAN, MANHATTAN, CHEBYCHEV, MINKOWSKI]
        - feature (str): 'F1' in [F1, F2, SMOOTH_F1, DISTANCE_TO_EDGE, N_SPHERE_RADIUS]
        - voronoi_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

        #### Returns:
        - tuple ('`distance`', '`color`', '`position`', '`w`')


        """

        node = nodes.VoronoiTexture(vector=vector, w=w, scale=scale, smoothness=smoothness, exponent=exponent, randomness=randomness, distance=distance, feature=feature, voronoi_dimensions=voronoi_dimensions)
        return node.distance, node.color, node.position, node.w


    @staticmethod
    def wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - bands_direction (str): 'X' in [X, Y, Z, DIAGONAL]
        - rings_direction (str): 'X' in [X, Y, Z, SPHERICAL]
        - wave_profile (str): 'SIN' in [SIN, SAW, TRI]
        - wave_type (str): 'BANDS' in [BANDS, RINGS]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=bands_direction, rings_direction=rings_direction, wave_profile=wave_profile, wave_type=wave_type)
        return node.color, node.fac


    @staticmethod
    def wave_bands(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, DIAGONAL]
        - wave_profile (str): 'SIN' in [SIN, SAW, TRI]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile=wave_profile, wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, DIAGONAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='SAW', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, DIAGONAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='SIN', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_bands_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, DIAGONAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction=direction, rings_direction='X', wave_profile='TRI', wave_type='BANDS')
        return node.color, node.fac


    @staticmethod
    def wave_rings(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X', wave_profile='SIN'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, SPHERICAL]
        - wave_profile (str): 'SIN' in [SIN, SAW, TRI]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile=wave_profile, wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_saw(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, SPHERICAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='SAW', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_sine(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, SPHERICAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='SIN', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def wave_rings_triangle(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, direction='X'):
        """

        > Node: [Wave Texture](ShaderNodeTexWave.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)

        #### Args:
        - vector: Vector
        - scale: Float
        - distortion: Float
        - detail: Float
        - detail_scale: Float
        - detail_roughness: Float
        - phase_offset: Float
        - direction (str): 'X' in [X, Y, Z, SPHERICAL]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

        #### Returns:
        - tuple ('`color`', '`fac`')


        """

        node = nodes.WaveTexture(vector=vector, scale=scale, distortion=distortion, detail=detail, detail_scale=detail_scale, detail_roughness=detail_roughness, phase_offset=phase_offset, bands_direction='X', rings_direction=direction, wave_profile='TRI', wave_type='RINGS')
        return node.color, node.fac


    @staticmethod
    def white_noise(vector=None, w=None, noise_dimensions='3D'):
        """

        > Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        #### Args:
        - vector: Vector
        - w: Float
        - noise_dimensions (str): '3D' in [1D, 2D, 3D, 4D]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

        #### Returns:
        - tuple ('`value`', '`color`')


        """

        node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions=noise_dimensions)
        return node.value, node.color


    @staticmethod
    def white_noise_1D(w=None):
        """

        > Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        #### Args:
        - w: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

        #### Returns:
        - tuple ('`value`', '`color`')


        """

        node = nodes.WhiteNoiseTexture(vector=None, w=w, noise_dimensions='1D')
        return node.value, node.color


    @staticmethod
    def white_noise_2D(vector=None):
        """

        > Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

        #### Returns:
        - tuple ('`value`', '`color`')


        """

        node = nodes.WhiteNoiseTexture(vector=vector, w=None, noise_dimensions='2D')
        return node.value, node.color


    @staticmethod
    def white_noise_3D(vector=None):
        """

        > Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        #### Args:
        - vector: Vector

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

        #### Returns:
        - tuple ('`value`', '`color`')


        """

        node = nodes.WhiteNoiseTexture(vector=vector, w=None, noise_dimensions='3D')
        return node.value, node.color


    @staticmethod
    def white_noise_4D(vector=None, w=None):
        """

        > Node: [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)

        #### Args:
        - vector: Vector
        - w: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

        #### Returns:
        - tuple ('`value`', '`color`')


        """

        node = nodes.WhiteNoiseTexture(vector=vector, w=w, noise_dimensions='3D')
        return node.value, node.color




class Image(geosocks.Image):
    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Image

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='IMAGE').output


    def texture(self, vector=None, frame=None, extension='REPEAT', interpolation='Linear'):
        """

        > Node: [Image Texture](GeometryNodeImageTexture.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)

        #### Args:
        - vector: Vector
        - frame: Integer
        - extension (str): 'REPEAT' in [REPEAT, EXTEND, CLIP]
        - interpolation (str): 'Linear' in [Linear, Closest, Cubic]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

        #### Returns:
        - tuple ('`color`', '`alpha`')


        """

        node = nodes.ImageTexture(image=self, vector=vector, frame=frame, extension=extension, interpolation=interpolation)
        return node.color, node.alpha




class Collection(geosocks.Collection):
    def switch(self, switch=None, true=None):
        """

        > Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

        #### Args:
        - switch: Boolean
        - true: Collection

        #### Returns:
        - socket `output`


        """

        return nodes.Switch(switch=switch, false=self, true=true, input_type='COLLECTION').output




