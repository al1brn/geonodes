from geonodes.nodes import nodes
import geonodes.core.domain as geodom

class Domain(geodom.Domain):
    @property
    def ID(self):
        """

                """

        return self.attribute_node(nodes.ID()).ID


    @ID.setter
    def ID(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=attr_value))


    def accumulate_field(self, value=None, group_index=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        node = self.attribute_node(nodes.AccumulateField(value=value, group_index=group_index, data_type=data_type_, domain=self.domain))
        return node.leading, node.trailing, node.total


    def attribute_max(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).max


    def attribute_mean(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).mean


    def attribute_median(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).median


    def attribute_min(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).min


    def attribute_range(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).range


    def attribute_statistic(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain)


    def attribute_std(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).standard_deviation


    def attribute_sum(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).sum


    def attribute_var(self, attribute=None):
        """

                """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain).variance


    def capture_attribute(self, value=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.socket_stack(nodes.CaptureAttribute(geometry=self.data_socket, value=value, data_type=data_type_, domain=self.domain)).node.attribute


    @property
    def domain_index(self):
        """

                """

        return self.attribute_node(nodes.Index()).index


    def field_at_index(self, index=None, value=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.FieldAtIndex(index=index, value=value, data_type=data_type_, domain=self.domain)).value


    def get_named_boolean(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='BOOLEAN')).attribute


    def get_named_color(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR')).attribute


    def get_named_float(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT')).attribute


    def get_named_integer(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='INT')).attribute


    def get_named_vector(self, name=None):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR')).attribute


    @property
    def index(self):
        """

                """

        return self.attribute_node(nodes.Index()).index


    def interpolate(self, value=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.InterpolateDomain(value=value, data_type=data_type_, domain=self.domain)).value


    @property
    def material_index(self):
        """

                """

        return self.attribute_node(nodes.MaterialIndex()).material_index


    def material_selection(self, material=None):
        """

                """

        return self.attribute_node(nodes.MaterialSelection(material=material)).selection


    def named_attribute(self, name=None, data_type='FLOAT'):
        """

                """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type=data_type)).attribute


    @property
    def normal(self):
        """

                """

        return self.attribute_node(nodes.Normal()).normal


    @property
    def position(self):
        """

                """

        return self.attribute_node(nodes.Position()).position


    @position.setter
    def position(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=attr_value, offset=None))


    def random_boolean(self, probability=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')).value


    def random_float(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT')).value


    def random_integer(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT')).value


    def random_vector(self, min=None, max=None, ID=None, seed=None):
        """

                """

        return self.attribute_node(nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR')).value


    def remove_named_attribute(self, name=None):
        """

                """

        return self.socket_stack(nodes.RemoveNamedAttribute(geometry=self.data_socket, name=name))


    def sample_index(self, value=None, index=None, clamp=False):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.SampleIndex(geometry=self.data_socket, value=value, index=index, clamp=clamp, data_type=data_type_, domain=self.domain).value


    def set_ID(self, ID=None):
        """

                """

        return self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=ID))


    def set_material_index(self, material_index=None):
        """

                """

        return self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=material_index))


    def set_named_boolean(self, name=None, value=None):
        """

                """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='BOOLEAN', domain=self.domain))


    def set_named_color(self, name=None, value=None):
        """

                """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_COLOR', domain=self.domain))


    def set_named_float(self, name=None, value=None):
        """

                """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT', domain=self.domain))


    def set_named_integer(self, name=None, value=None):
        """

                """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='INT', domain=self.domain))


    def set_named_vector(self, name=None, value=None):
        """

                """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type='FLOAT_VECTOR', domain=self.domain))


    def set_position(self, position=None, offset=None):
        """

                """

        return self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=position, offset=offset))


    def store_named_attribute(self, name=None, value=None):
        """

                """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, name=name, value=value, data_type=data_type_, domain=self.domain))




class Vertex(Domain):
    def corners(self, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.CornersOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def corners_index(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.CornersOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index)).corner_index


    def corners_total(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.CornersOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index)).total


    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='MESH').point_count


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def edges(self, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.EdgesOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index))
        return node.edge_index, node.total


    def edges_index(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.EdgesOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index)).edge_index


    def edges_total(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.EdgesOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index)).total


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

                """

        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='VERTICES')).node
        return node.top, node.side


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        import geonodes as gn
        return gn.Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    def merge_by_distance(self, distance=None, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.MergeByDistance(geometry=self.data_socket, selection=self.selection, distance=distance, mode=mode))


    @property
    def neighbors(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors


    @property
    def neighbors_face_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors.face_count


    @property
    def neighbors_vertex_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshvertexneighbors'):
            self._c_geometrynodeinputmeshvertexneighbors = self.attribute_node(nodes.VertexNeighbors())
        return self._c_geometrynodeinputmeshvertexneighbors.vertex_count


    def proximity(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='POINTS')).distance


    def sample_nearest(self, sample_position=None):
        """

                """

        return nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain).index


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def to_points(self, position=None, radius=None, mode='VERTICES'):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.MeshToPoints(mesh=self.data_socket, selection=self.selection, position=position, radius=radius, mode=mode).points)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
        """

                """

        import geonodes as gn
        return gn.Volume(nodes.MeshToVolume(mesh=self.data_socket, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode).volume)




class Face(Domain):
    @property
    def area(self):
        """

                """

        return self.attribute_node(nodes.FaceArea())


    def corners(self, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.CornersOfFace(face_index=self.selection_index, weights=weights, sort_index=sort_index))
        return node.corner_index, node.total


    def corners_index(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.CornersOfFace(face_index=self.selection_index, weights=weights, sort_index=sort_index)).corner_index


    def corners_total(self, weights=None, sort_index=None):
        """

                """

        return self.attribute_node(nodes.CornersOfFace(face_index=self.selection_index, weights=weights, sort_index=sort_index)).total


    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='MESH').face_count


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):
        """

                """

        import geonodes as gn
        node = nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=distance_min, density_max=density_max, density=None, density_factor=density_factor, seed=seed, distribute_method='POISSON')
        return gn.Points(node.points), node.normal, node.rotation


    def distribute_points_random(self, density=None, seed=None):
        """

                """

        import geonodes as gn
        node = nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=None, density_max=None, density=density, density_factor=None, seed=seed, distribute_method='RANDOM')
        return gn.Points(node.points), node.normal, node.rotation


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

                """

        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='FACES')).node
        return node.top, node.side


    def face_set_boundaries(self):
        """

                """

        return self.attribute_node(nodes.FaceSetBoundaries(face_set=self.selection_index)).boundary_edges


    def flip(self):
        """

                """

        return self.socket_stack(nodes.FlipFaces(mesh=self.data_socket, selection=self.selection))


    def is_planar(self, threshold=None):
        """

                """

        return self.attribute_node(nodes.FaceIsPlanar(threshold=threshold)).planar


    @property
    def island(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland


    @property
    def island_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_count


    @property
    def island_index(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshisland'):
            self._c_geometrynodeinputmeshisland = self.attribute_node(nodes.MeshIsland())
        return self._c_geometrynodeinputmeshisland.island_index


    @property
    def material(self):
        """

                """

        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def neighbors(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors


    @property
    def neighbors_face_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors.face_count


    @property
    def neighbors_vertex_count(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshfaceneighbors'):
            self._c_geometrynodeinputmeshfaceneighbors = self.attribute_node(nodes.FaceNeighbors())
        return self._c_geometrynodeinputmeshfaceneighbors.vertex_count


    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        """

                """

        return self.attribute_node(nodes.PackUvIslands(uv=uv, selection=self.selection, margin=margin, rotate=rotate)).uv


    def proximity(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='FACES')).distance


    def sample_nearest(self, sample_position=None):
        """

                """

        return nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain).index


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """

                """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """

                """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def set_material(self, material=None):
        """

                """

        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_shade_smooth(self, shade_smooth=None):
        """

                """

        return self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=shade_smooth))


    @property
    def shade_smooth(self):
        """

                """

        return self.attribute_node(nodes.IsShadeSmooth()).smooth


    @shade_smooth.setter
    def shade_smooth(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=attr_value))


    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """

                """

        return self.socket_stack(nodes.Triangulate(mesh=self.data_socket, selection=self.selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))


    def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """

                """

        return self.attribute_node(nodes.UvUnwrap(selection=self.selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method)).uv




class Edge(Domain):
    @property
    def angle(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle


    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='MESH').edge_count


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """

                """

        import geonodes as gn
        return gn.Curve(self.attribute_node(nodes.EdgePathsToCurves(mesh=self.data_socket, start_vertices=start_vertices, next_vertex_index=next_vertex_index)).curves)


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

                """

        node = self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='EDGES')).node
        return node.top, node.side


    @property
    def neighbors(self):
        """

                """

        return self.attribute_node(nodes.EdgeNeighbors()).face_count


    def proximity(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='EDGES')).distance


    def sample_nearest(self, sample_position=None):
        """

                """

        return nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain).index


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """

                """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """

                """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    @property
    def signed_angle(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle.signed_angle


    def split(self):
        """

                """

        return self.socket_stack(nodes.SplitEdges(mesh=self.data_socket, selection=self.selection))


    def to_curve(self):
        """

                """

        import geonodes as gn
        return gn.Curve(nodes.MeshToCurve(mesh=self.data_socket, selection=self.selection).curve)


    @property
    def unsigned_angle(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgeangle'):
            self._c_geometrynodeinputmeshedgeangle = self.attribute_node(nodes.EdgeAngle())
        return self._c_geometrynodeinputmeshedgeangle.unsigned_angle


    @property
    def vertices(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        return self._c_geometrynodeinputmeshedgevertices


    @property
    def vertices_index(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        node = self._c_geometrynodeinputmeshedgevertices
        return node.vertex_index_1, node.vertex_index_2


    @property
    def vertices_position(self):
        """

                """

        if not hasattr(self, '_c_geometrynodeinputmeshedgevertices'):
            self._c_geometrynodeinputmeshedgevertices = self.attribute_node(nodes.EdgeVertices())
        node = self._c_geometrynodeinputmeshedgevertices
        return node.position_1, node.position_2




class Corner(Domain):
    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='MESH').face_corner_count


    def edges(self):
        """

                """

        node = self.attribute_node(nodes.EdgesOfCorner(corner_index=self.selection_index))
        return node.next_edge_index, node.previous_edge_index


    def face(self):
        """

                """

        node = self.attribute_node(nodes.FaceOfCorner(corner_index=self.selection_index))
        return node.face_index, node.index_in_face


    @property
    def face_index(self):
        """

                """

        return self.attribute_node(nodes.FaceOfCorner(corner_index=self.selection_index)).face_index


    @property
    def index_in_face(self):
        """

                """

        return self.attribute_node(nodes.FaceOfCorner(corner_index=self.selection_index)).index_in_face


    @property
    def next_vertex(self):
        """

                """

        return self.attribute_node(nodes.EdgesOfCorner(corner_index=self.selection_index)).next_edge_index


    def offset_in_face(self, offset=None):
        """

                """

        return self.attribute_node(nodes.OffsetCornerInFace(corner_index=self.selection_index, offset=offset)).corner_index


    @property
    def previous_vertex(self):
        """

                """

        return self.attribute_node(nodes.EdgesOfCorner(corner_index=self.selection_index)).previous_edge_index


    def sample_nearest(self, sample_position=None):
        """

                """

        return nodes.SampleNearest(geometry=self.data_socket, sample_position=sample_position, domain=self.domain).index


    @property
    def vertex_index(self):
        """

                """

        return self.attribute_node(nodes.VertexOfCorner(corner_index=self.selection_index)).vertex_index




class Spline(Domain):
    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='CURVE').spline_count


    @property
    def cyclic(self):
        """

                """

        return self.attribute_node(nodes.IsSplineCyclic()).cyclic


    @cyclic.setter
    def cyclic(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=attr_value))


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain='SPLINE')).node.duplicate_index


    @property
    def length(self):
        """

                """

        node = self.attribute_node(nodes.SplineLength())
        return node.length, node.point_count


    @property
    def material(self):
        """

                """

        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def normal(self):
        """

                """

        return self.attribute_node(nodes.Normal()).normal


    @normal.setter
    def normal(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=attr_value))


    def points(self, weights=None, sort_index=None):
        """

                """

        node = self.attribute_node(nodes.PointsOfCurve(curve_index=self.selection_index, weights=weights, sort_index=sort_index))
        return node.point_index, node.total


    def resample(self, count=None, length=None, mode='COUNT'):
        """

                """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=length, mode=mode))


    def resample_count(self, count=None):
        """

                """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=0.1, mode='COUNT'))


    def resample_evaluated(self):
        """

                """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=0.1, mode='EVALUATED'))


    def resample_length(self, length=None):
        """

                """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=length, mode='LENGTH'))


    @property
    def resolution(self):
        """

                """

        return self.attribute_node(nodes.SplineResolution()).resolution


    @resolution.setter
    def resolution(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=attr_value))


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def set_cyclic(self, cyclic=None):
        """

                """

        return self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=cyclic))


    def set_material(self, material=None):
        """

                """

        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_normal(self, mode='MINIMUM_TWIST'):
        """

                """

        return self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=mode))


    def set_resolution(self, resolution=None):
        """

                """

        return self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=resolution))


    def set_type(self, spline_type='POLY'):
        """

                """

        return self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=spline_type))


    @property
    def type(self):
        """

                """

        raise Exception("Error: 'type' is a write only property of class Curve!")


    @type.setter
    def type(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=attr_value))




class ControlPoint(Domain):
    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='CURVE').point_count


    def curve(self):
        """

                """

        node = self.attribute_node(nodes.CurveOfPoint(point_index=self.selection_index))
        return node.curve_index, node.index_in_curve


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def endpoint_selection(self, start_size=None, end_size=None):
        """

                """

        return self.attribute_node(nodes.EndpointSelection(start_size=start_size, end_size=end_size)).selection


    def handle_positions(self, relative=None):
        """

                """

        return self.attribute_node(nodes.CurveHandlePositions(relative=relative))


    def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):
        """

                """

        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.handle_type_selection_node(handle_type=handle_type, mode=mode)


    def handle_type_selection_free(self, left=True, right=True):
        """

                """

        return self.handle_type_selection(left=left, right=right, handle_type='FREE')


    def handle_type_selection_auto(self, left=True, right=True):
        """

                """

        return self.handle_type_selection(left=left, right=right, handle_type='AUTO')


    def handle_type_selection_vector(self, left=True, right=True):
        """

                """

        return self.handle_type_selection(left=left, right=right, handle_type='VECTOR')


    def handle_type_selection_align(self, left=True, right=True):
        """

                """

        return self.handle_type_selection(left=left, right=right, handle_type='ALIGN')


    def handle_type_selection_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """

                """

        return self.attribute_node(nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)).selection


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        import geonodes as gn
        return gn.Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    @property
    def left_handle_positions(self):
        """

                """

        return self.attribute_node(nodes.CurveHandlePositions(relative=None)).left


    @left_handle_positions.setter
    def left_handle_positions(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=attr_value, offset=None, mode='LEFT'))


    def offset(self, offset=None):
        """

                """

        node = self.attribute_node(nodes.OffsetPointInCurve(point_index=self.selection_index, offset=offset))
        return node.is_valid_offset, node.point_index


    @property
    def parameter(self):
        """

                """

        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        node = self._c_geometrynodesplineparameter
        return node.factor, node.length, node.index


    @property
    def parameter_factor(self):
        """

                """

        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.factor


    @property
    def parameter_index(self):
        """

                """

        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.index


    @property
    def parameter_length(self):
        """

                """

        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter.length


    def proximity(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='POINTS')).distance


    @property
    def radius(self):
        """

                """

        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=attr_value))


    @property
    def right_handle_positions(self):
        """

                """

        return self.attribute_node(nodes.CurveHandlePositions(relative=None)).right


    @right_handle_positions.setter
    def right_handle_positions(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=attr_value, offset=None, mode='RIGHT'))


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """

                """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode=mode))


    def set_handle_positions_left(self, position=None, offset=None):
        """

                """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode='LEFT'))


    def set_handle_positions_right(self, position=None, offset=None):
        """

                """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode='RIGHT'))


    def set_handle_type(self, left=True, right=True, handle_type='AUTO'):
        """

                """

        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.set_handle_type_node(handle_type=handle_type, mode=mode)


    def set_handle_type_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """

                """

        return self.socket_stack(nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=handle_type, mode=mode))


    def set_radius(self, radius=None):
        """

                """

        return self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=radius))


    def set_tilt(self, tilt=None):
        """

                """

        return self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=tilt))


    @property
    def tangent(self):
        """

                """

        return self.attribute_node(nodes.CurveTangent()).tangent


    @property
    def tilt(self):
        """

                """

        return self.attribute_node(nodes.CurveTilt()).tilt


    @tilt.setter
    def tilt(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=attr_value))




class CloudPoint(Domain):
    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='POINTCLOUD').point_count


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

                """

        import geonodes as gn
        return gn.Instances(nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances)


    def proximity(self, target=None, source_position=None):
        """

                """

        return self.attribute_node(nodes.GeometryProximity(target=target, source_position=source_position, target_element='POINTS')).distance


    @property
    def radius(self):
        """

                """

        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """

                """

        self.socket_stack(nodes.SetPointRadius(points=self.data_socket, selection=self.selection, radius=attr_value))


    def to_vertices(self, points=None):
        """

                """

        import geonodes as gn
        return gn.Mesh(nodes.PointsToVertices(points=points, selection=self.selection).mesh)




class Instance(Domain):
    @property
    def count(self, geometry=None):
        """

                """

        return nodes.DomainSize(geometry=geometry, component='INSTANCES').instance_count


    def delete(self, mode='ALL'):
        """

                """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

                """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """

                """

        return self.socket_stack(nodes.RotateInstances(instances=self.data_socket, selection=self.selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))


    @property
    def rotation(self):
        """

                """

        return self.attribute_node(nodes.InstanceRotation()).rotation


    @property
    def scale(self):
        """

                """

        return self.attribute_node(nodes.InstanceScale()).scale


    def separate(self, geometry=None):
        """

                """

        node = nodes.SeparateGeometry(geometry=geometry, selection=self.selection, domain=self.domain)
        return node.selection, node.inverted


    def set_scale(self, scale=None, center=None, local_space=None):
        """

                """

        return self.socket_stack(nodes.ScaleInstances(instances=self.data_socket, selection=self.selection, scale=scale, center=center, local_space=local_space))


    def to_points(self, position=None, radius=None):
        """

                """

        import geonodes as gn
        return gn.Points(nodes.InstancesToPoints(instances=self.data_socket, selection=self.selection, position=position, radius=radius).points)


    def translate(self, translation=None, local_space=None):
        """

                """

        return self.socket_stack(nodes.TranslateInstances(instances=self.data_socket, selection=self.selection, translation=translation, local_space=local_space))




