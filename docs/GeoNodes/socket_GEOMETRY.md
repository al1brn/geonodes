# Socket GEOMETRY

### Properties

- [curve_length](#curve_length)
- [curve_tangent](#curve_tangent)
- [curve_tilt](#curve_tilt)
- [cyclic](#cyclic)
- [edge_neighbors](#edge_neighbors)
- [edge_smooth](#edge_smooth)
- [face_area](#face_area)
- [face_smooth](#face_smooth)
- [id](#id)
- [index](#index)
- [instance_rotation](#instance_rotation)
- [instance_scale](#instance_scale)
- [material](#material)
- [material_index](#material_index)
- [normal](#normal)
- [offset](#offset)
- [point_radius](#point_radius)
- [position](#position)
- [radius](#radius)
- [shade_smooth](#shade_smooth)
- [spline_cyclic](#spline_cyclic)
- [spline_resolution](#spline_resolution)
- [spline_type](#spline_type)
- [tilt](#tilt)

### Methods

- [attribute_statistic](#attribute_statistic)
- [attribute_statistic_float](#attribute_statistic_float)
- [attribute_statistic_vector](#attribute_statistic_vector)
- [bake](#bake)
- [blur_attribute](#blur_attribute)
- [bounding_box](#bounding_box)
- [capture_attribute](#capture_attribute)
- [capture_boolean](#capture_boolean)
- [capture_color](#capture_color)
- [capture_float](#capture_float)
- [capture_int](#capture_int)
- [capture_quaternion](#capture_quaternion)
- [capture_vector](#capture_vector)
- [convex_hull](#convex_hull)
- [corners_of_edge](#corners_of_edge)
- [corners_of_face](#corners_of_face)
- [corners_of_vertex](#corners_of_vertex)
- [curve_handle_positions](#curve_handle_positions)
- [curve_of_point](#curve_of_point)
- [curve_to_mesh](#curve_to_mesh)
- [curve_to_points](#curve_to_points)
- [deform_curves_on_surface](#deform_curves_on_surface)
- [delete_geometry](#delete_geometry)
- [distribute_points_in_volume](#distribute_points_in_volume)
- [distribute_points_on_faces](#distribute_points_on_faces)
- [domain_size](#domain_size)
- [dual_mesh](#dual_mesh)
- [duplicate_elements](#duplicate_elements)
- [edge_angle](#edge_angle)
- [edge_paths_to_curves](#edge_paths_to_curves)
- [edge_paths_to_selection](#edge_paths_to_selection)
- [edge_vertices](#edge_vertices)
- [edges_of_corner](#edges_of_corner)
- [edges_of_vertex](#edges_of_vertex)
- [edges_to_face_groups](#edges_to_face_groups)
- [endpoint_selection](#endpoint_selection)
- [evaluate_at_index](#evaluate_at_index)
- [evaluate_at_index_boolean](#evaluate_at_index_boolean)
- [evaluate_at_index_color](#evaluate_at_index_color)
- [evaluate_at_index_float](#evaluate_at_index_float)
- [evaluate_at_index_int](#evaluate_at_index_int)
- [evaluate_at_index_quaternion](#evaluate_at_index_quaternion)
- [evaluate_at_index_vector](#evaluate_at_index_vector)
- [evaluate_on_domain](#evaluate_on_domain)
- [evaluate_on_domain_boolean](#evaluate_on_domain_boolean)
- [evaluate_on_domain_color](#evaluate_on_domain_color)
- [evaluate_on_domain_float](#evaluate_on_domain_float)
- [evaluate_on_domain_int](#evaluate_on_domain_int)
- [evaluate_on_domain_quaternion](#evaluate_on_domain_quaternion)
- [evaluate_on_domain_vector](#evaluate_on_domain_vector)
- [extrude_mesh](#extrude_mesh)
- [face_group_boundaries](#face_group_boundaries)
- [face_neighbors](#face_neighbors)
- [face_of_corner](#face_of_corner)
- [fill_curve](#fill_curve)
- [fillet_curve](#fillet_curve)
- [fillet_curve_bezier](#fillet_curve_bezier)
- [fillet_curve_poly](#fillet_curve_poly)
- [flip_faces](#flip_faces)
- [geometry_proximity](#geometry_proximity)
- [geometry_to_instance](#geometry_to_instance)
- [handle_type_selection](#handle_type_selection)
- [index_of_nearest](#index_of_nearest)
- [index_switch](#index_switch)
- [instance_on_points](#instance_on_points)
- [instances_to_points](#instances_to_points)
- [interpolate_curves](#interpolate_curves)
- [is_face_planar](#is_face_planar)
- [join_geometry](#join_geometry)
- [left_handle_type_selection](#left_handle_type_selection)
- [merge_by_distance](#merge_by_distance)
- [mesh_difference](#mesh_difference)
- [mesh_intersect](#mesh_intersect)
- [mesh_island](#mesh_island)
- [mesh_to_curve](#mesh_to_curve)
- [mesh_to_points](#mesh_to_points)
- [mesh_to_volume](#mesh_to_volume)
- [mesh_union](#mesh_union)
- [named_attribute](#named_attribute)
- [named_boolean](#named_boolean)
- [named_color](#named_color)
- [named_float](#named_float)
- [named_int](#named_int)
- [named_quaternion](#named_quaternion)
- [named_vector](#named_vector)
- [offset_corner_in_face](#offset_corner_in_face)
- [offset_point_in_curve](#offset_point_in_curve)
- [points_of_curve](#points_of_curve)
- [points_to_curves](#points_to_curves)
- [points_to_vertices](#points_to_vertices)
- [points_to_volume](#points_to_volume)
- [raycast](#raycast)
- [raycast_boolean](#raycast_boolean)
- [raycast_color](#raycast_color)
- [raycast_float](#raycast_float)
- [raycast_int](#raycast_int)
- [raycast_quaternion](#raycast_quaternion)
- [raycast_vector](#raycast_vector)
- [realize_instances](#realize_instances)
- [remove_named_attribute](#remove_named_attribute)
- [replace_material](#replace_material)
- [resample_curve](#resample_curve)
- [reverse_curve](#reverse_curve)
- [right_handle_type_selection](#right_handle_type_selection)
- [rotate_instances](#rotate_instances)
- [sample_curve](#sample_curve)
- [sample_curve_boolean](#sample_curve_boolean)
- [sample_curve_boolean_factor](#sample_curve_boolean_factor)
- [sample_curve_boolean_length](#sample_curve_boolean_length)
- [sample_curve_color](#sample_curve_color)
- [sample_curve_color_factor](#sample_curve_color_factor)
- [sample_curve_color_length](#sample_curve_color_length)
- [sample_curve_float](#sample_curve_float)
- [sample_curve_float_factor](#sample_curve_float_factor)
- [sample_curve_float_length](#sample_curve_float_length)
- [sample_curve_int](#sample_curve_int)
- [sample_curve_int_factor](#sample_curve_int_factor)
- [sample_curve_int_length](#sample_curve_int_length)
- [sample_curve_quaternion](#sample_curve_quaternion)
- [sample_curve_quaternion_factor](#sample_curve_quaternion_factor)
- [sample_curve_quaternion_length](#sample_curve_quaternion_length)
- [sample_curve_vector](#sample_curve_vector)
- [sample_curve_vector_factor](#sample_curve_vector_factor)
- [sample_curve_vector_length](#sample_curve_vector_length)
- [sample_index](#sample_index)
- [sample_index_boolean](#sample_index_boolean)
- [sample_index_color](#sample_index_color)
- [sample_index_float](#sample_index_float)
- [sample_index_int](#sample_index_int)
- [sample_index_quaternion](#sample_index_quaternion)
- [sample_index_vector](#sample_index_vector)
- [sample_nearest](#sample_nearest)
- [sample_nearest_surface](#sample_nearest_surface)
- [sample_nearest_surface_boolean](#sample_nearest_surface_boolean)
- [sample_nearest_surface_color](#sample_nearest_surface_color)
- [sample_nearest_surface_float](#sample_nearest_surface_float)
- [sample_nearest_surface_int](#sample_nearest_surface_int)
- [sample_nearest_surface_quaternion](#sample_nearest_surface_quaternion)
- [sample_nearest_surface_vector](#sample_nearest_surface_vector)
- [sample_uv_surface](#sample_uv_surface)
- [sample_uv_surface_boolean](#sample_uv_surface_boolean)
- [sample_uv_surface_color](#sample_uv_surface_color)
- [sample_uv_surface_float](#sample_uv_surface_float)
- [sample_uv_surface_int](#sample_uv_surface_int)
- [sample_uv_surface_quaternion](#sample_uv_surface_quaternion)
- [sample_uv_surface_vector](#sample_uv_surface_vector)
- [scale_elements](#scale_elements)
- [scale_instances](#scale_instances)
- [separate_components](#separate_components)
- [separate_geometry](#separate_geometry)
- [set_curve_normal](#set_curve_normal)
- [set_curve_radius](#set_curve_radius)
- [set_curve_tilt](#set_curve_tilt)
- [set_handle_positions](#set_handle_positions)
- [set_handle_type](#set_handle_type)
- [set_id](#set_id)
- [set_material](#set_material)
- [set_material_index](#set_material_index)
- [set_point_radius](#set_point_radius)
- [set_position](#set_position)
- [set_shade_smooth](#set_shade_smooth)
- [set_spline_cyclic](#set_spline_cyclic)
- [set_spline_resolution](#set_spline_resolution)
- [set_spline_type](#set_spline_type)
- [shortest_edge_paths](#shortest_edge_paths)
- [sort_elements](#sort_elements)
- [spline_length](#spline_length)
- [spline_parameter](#spline_parameter)
- [split_edges](#split_edges)
- [split_to_instances](#split_to_instances)
- [store_named_attribute](#store_named_attribute)
- [store_named_boolean](#store_named_boolean)
- [store_named_byte_color](#store_named_byte_color)
- [store_named_float](#store_named_float)
- [store_named_float2](#store_named_float2)
- [store_named_float_color](#store_named_float_color)
- [store_named_int](#store_named_int)
- [store_named_quaternion](#store_named_quaternion)
- [store_named_vector](#store_named_vector)
- [subdivide_curve](#subdivide_curve)
- [subdivide_mesh](#subdivide_mesh)
- [subdivision_surface](#subdivision_surface)
- [switch](#switch)
- [transform_geometry](#transform_geometry)
- [translate_instances](#translate_instances)
- [triangulate](#triangulate)
- [trim_curve](#trim_curve)
- [uv_unwrap](#uv_unwrap)
- [vertex_neighbors](#vertex_neighbors)
- [vertex_of_corner](#vertex_of_corner)
- [viewer](#viewer)
- [viewer_boolean](#viewer_boolean)
- [viewer_color](#viewer_color)
- [viewer_float](#viewer_float)
- [viewer_int](#viewer_int)
- [viewer_quaternion](#viewer_quaternion)
- [viewer_vector](#viewer_vector)
- [volume_to_mesh](#volume_to_mesh)

## Properties

### curve_length

> Read only property

### Get


- node : [CurveLength](/docs/GeoNodes/CurveLength.md)
- self : curve
- jump : No
- return : length

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def curve_length(self):
    node = self.tree.CurveLength(curve=self, node_color=(0.3, 0.3, 0.25))
    return node.length
```
### curve_tangent

> Read only property

### Get


- node : [CurveTangent](/docs/GeoNodes/CurveTangent.md)
- self
- jump : No
- return : tangent

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def curve_tangent(self):
    node = self.tree.CurveTangent(node_color=(0.3, 0.3, 0.25))
    return node.tangent
```
### curve_tilt

> Read only property

### Get


- node : [CurveTilt](/docs/GeoNodes/CurveTilt.md)
- self
- jump : No
- return : tilt

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def curve_tilt(self):
    node = self.tree.CurveTilt(node_color=(0.3, 0.3, 0.25))
    return node.tilt
```
### cyclic

> Write only property

### Set


- node : [SetSplineCyclic](/docs/GeoNodes/SetSplineCyclic.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- cyclic : None
- selection : None

#### Source code

``` python
def cyclic(self, value):
    node = self.tree.SetSplineCyclic(geometry=self, cyclic=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### edge_neighbors

> Read only property

### Get


- node : [EdgeNeighbors](/docs/GeoNodes/EdgeNeighbors.md)
- self
- jump : No
- return : face_count

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def edge_neighbors(self):
    node = self.tree.EdgeNeighbors(node_color=(0.3, 0.3, 0.25))
    return node.face_count
```
### edge_smooth

> Read only property

### Get


- node : [IsEdgeSmooth](/docs/GeoNodes/IsEdgeSmooth.md)
- self
- jump : No
- return : smooth

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def edge_smooth(self):
    node = self.tree.IsEdgeSmooth(node_color=(0.3, 0.3, 0.25))
    return node.smooth
```
### face_area

> Read only property

### Get


- node : [FaceArea](/docs/GeoNodes/FaceArea.md)
- self
- jump : No
- return : area

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def face_area(self):
    node = self.tree.FaceArea(node_color=(0.3, 0.3, 0.25))
    return node.area
```
### face_smooth

> Read only property

### Get


- node : [IsFaceSmooth](/docs/GeoNodes/IsFaceSmooth.md)
- self
- jump : No
- return : smooth

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def face_smooth(self):
    node = self.tree.IsFaceSmooth(node_color=(0.3, 0.3, 0.25))
    return node.smooth
```
### id

> Property

### Get


- node : [ID](/docs/GeoNodes/ID.md)
- self
- jump : No
- return : id

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def id(self):
    node = self.tree.ID(node_color=(0.3, 0.3, 0.25))
    return node.id
```
### Set


- node : [SetID](/docs/GeoNodes/SetID.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- ID : None
- selection : None

#### Source code

``` python
def id(self, value):
    node = self.tree.SetID(geometry=self, id=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### index

> Read only property

### Get


- node : [Index](/docs/GeoNodes/Index.md)
- self
- jump : No
- return : index

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def index(self):
    node = self.tree.Index(node_color=(0.3, 0.3, 0.25))
    return node.index
```
### instance_rotation

> Read only property

### Get


- node : [InstanceRotation](/docs/GeoNodes/InstanceRotation.md)
- self
- jump : No
- return : rotation

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def instance_rotation(self):
    node = self.tree.InstanceRotation(node_color=(0.3, 0.3, 0.25))
    return node.rotation
```
### instance_scale

> Read only property

### Get


- node : [InstanceScale](/docs/GeoNodes/InstanceScale.md)
- self
- jump : No
- return : scale

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def instance_scale(self):
    node = self.tree.InstanceScale(node_color=(0.3, 0.3, 0.25))
    return node.scale
```
### material

> Write only property

### Set


- node : [SetMaterial](/docs/GeoNodes/SetMaterial.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- material : None
- selection : None

#### Source code

``` python
def material(self, value):
    node = self.tree.SetMaterial(geometry=self, material=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### material_index

> Property

### Get


- node : [MaterialIndex](/docs/GeoNodes/MaterialIndex.md)
- self
- jump : No
- return : material_index

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def material_index(self):
    node = self.tree.MaterialIndex(node_color=(0.3, 0.3, 0.25))
    return node.material_index
```
### Set


- node : [SetMaterialIndex](/docs/GeoNodes/SetMaterialIndex.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- material_index : None
- selection : None

#### Source code

``` python
def material_index(self, value):
    node = self.tree.SetMaterialIndex(geometry=self, material_index=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### normal

> Property

### Get


- node : [Normal](/docs/GeoNodes/Normal.md)
- self
- jump : No
- return : normal

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def normal(self):
    node = self.tree.Normal(node_color=(0.3, 0.3, 0.25))
    return node.normal
```
### Set


- node : [SetCurveNormal](/docs/GeoNodes/SetCurveNormal.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- normal : None
- selection : None

#### Source code

``` python
def normal(self, value):
    node = self.tree.SetCurveNormal(curve=self, mode=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.curve)
```
### offset

> Write only property

### Set


- node : [SetPosition](/docs/GeoNodes/SetPosition.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- position : None
- offset : None
- selection : None

#### Source code

``` python
def offset(self, value):
    node = self.tree.SetPosition(geometry=self, offset=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### point_radius

> Write only property

### Set


- node : [SetPointRadius](/docs/GeoNodes/SetPointRadius.md)
- self : points
- jump : points
- return : self

##### Arguments

- radius : None
- selection : None

#### Source code

``` python
def point_radius(self, value):
    node = self.tree.SetPointRadius(points=self, radius=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.points)
```
### position

> Property

### Get


- node : [Position](/docs/GeoNodes/Position.md)
- self
- jump : No
- return : position

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def position(self):
    node = self.tree.Position(node_color=(0.3, 0.3, 0.25))
    return node.position
```
### Set


- node : [SetPosition](/docs/GeoNodes/SetPosition.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- position : None
- offset : None
- selection : None

#### Source code

``` python
def position(self, value):
    node = self.tree.SetPosition(geometry=self, position=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### radius

> Property

### Get


- node : [Radius](/docs/GeoNodes/Radius.md)
- self
- jump : No
- return : radius

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def radius(self):
    node = self.tree.Radius(node_color=(0.3, 0.3, 0.25))
    return node.radius
```
### Set


- node : [SetCurveRadius](/docs/GeoNodes/SetCurveRadius.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- radius : None
- selection : None

#### Source code

``` python
def radius(self, value):
    node = self.tree.SetCurveRadius(curve=self, radius=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.curve)
```
### shade_smooth

> Write only property

### Set


- node : [SetShadeSmooth](/docs/GeoNodes/SetShadeSmooth.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- shade_smooth : None
- selection : None
- domain : 'FACE' in ('EDGE', 'FACE')

#### Source code

``` python
def shade_smooth(self, value):
    node = self.tree.SetShadeSmooth(geometry=self, shade_smooth=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### spline_cyclic

> Read only property

### Get


- node : [IsSplineCyclic](/docs/GeoNodes/IsSplineCyclic.md)
- self
- jump : No
- return : cyclic

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def spline_cyclic(self):
    node = self.tree.IsSplineCyclic(node_color=(0.3, 0.3, 0.25))
    return node.cyclic
```
### spline_resolution

> Property

### Get


- node : [SplineResolution](/docs/GeoNodes/SplineResolution.md)
- self
- jump : No
- return : resolution

##### Arguments

- node_color : 'ARG_NO_VALUE'

#### Source code

``` python
def spline_resolution(self):
    node = self.tree.SplineResolution(node_color=(0.3, 0.3, 0.25))
    return node.resolution
```
### Set


- node : [SetSplineResolution](/docs/GeoNodes/SetSplineResolution.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- resolution : None
- selection : None

#### Source code

``` python
def spline_resolution(self, value):
    node = self.tree.SetSplineResolution(geometry=self, resolution=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### spline_type

> Write only property

### Set


- node : [SetSplineType](/docs/GeoNodes/SetSplineType.md)
- self : curve
- jump : geometry
- return : self

##### Arguments

- selection : None

#### Source code

``` python
def spline_type(self, value):
    node = self.tree.SetSplineType(curve=self, spline_type=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.geometry)
```
### tilt

> Write only property

### Set


- node : [SetCurveTilt](/docs/GeoNodes/SetCurveTilt.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- tilt : None
- selection : None

#### Source code

``` python
def tilt(self, value):
    node = self.tree.SetCurveTilt(curve=self, tilt=value, selection=self._get_selection(None), node_color=(0.3, 0.3, 0.25))
    self.jump(node.curve)
```
## Methods

### attribute_statistic


- node : [AttributeStatistic](/docs/GeoNodes/AttributeStatistic.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- selection : None
- data_type : 'FLOAT' in ('FLOAT', 'FLOAT_VECTOR')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def attribute_statistic(self, attribute=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.AttributeStatistic(geometry=self, attribute=attribute, selection=self._get_selection(selection), data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### attribute_statistic_float


- node : [AttributeStatistic](/docs/GeoNodes/AttributeStatistic.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def attribute_statistic_float(self, attribute=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.AttributeStatistic(geometry=self, attribute=attribute, selection=self._get_selection(selection), data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### attribute_statistic_vector


- node : [AttributeStatistic](/docs/GeoNodes/AttributeStatistic.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def attribute_statistic_vector(self, attribute=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.AttributeStatistic(geometry=self, attribute=attribute, selection=self._get_selection(selection), data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### bake


- node : [Bake](/docs/GeoNodes/Bake.md)
- self : geometry
- jump : No
- return : geometry

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def bake(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.Bake(geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    return node.geometry
```
### blur_attribute


- node : [BlurAttribute](/docs/GeoNodes/BlurAttribute.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- iterations : None
- weight : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')
- node_label : None
- node_color : None

#### Source code

``` python
def blur_attribute(self, value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):
    node = self.tree.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type=data_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### bounding_box


- node : [BoundingBox](/docs/GeoNodes/BoundingBox.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def bounding_box(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.BoundingBox(geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### capture_attribute


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_attribute(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_boolean


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_boolean(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='BOOLEAN', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_color


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_color(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_float


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_float(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_int


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_int(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='INT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_quaternion


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_quaternion(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='QUATERNION', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### capture_vector


- node : [CaptureAttribute](/docs/GeoNodes/CaptureAttribute.md)
- self : geometry
- jump : geometry
- return : attribute

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def capture_vector(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CaptureAttribute(geometry=self, value=value, data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return node.attribute
```
### convex_hull


- node : [ConvexHull](/docs/GeoNodes/ConvexHull.md)
- self : geometry
- jump : No
- return : convex_hull

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def convex_hull(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.ConvexHull(geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    return node.convex_hull
```
### corners_of_edge


- node : [CornersOfEdge](/docs/GeoNodes/CornersOfEdge.md)
- self
- jump : No
- return : node

##### Arguments

- edge_index : None
- weights : None
- sort_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def corners_of_edge(self, edge_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CornersOfEdge(edge_index=edge_index, weights=weights, sort_index=sort_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### corners_of_face


- node : [CornersOfFace](/docs/GeoNodes/CornersOfFace.md)
- self
- jump : No
- return : node

##### Arguments

- face_index : None
- weights : None
- sort_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def corners_of_face(self, face_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CornersOfFace(face_index=face_index, weights=weights, sort_index=sort_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### corners_of_vertex


- node : [CornersOfVertex](/docs/GeoNodes/CornersOfVertex.md)
- self
- jump : No
- return : node

##### Arguments

- vertex_index : None
- weights : None
- sort_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CornersOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### curve_handle_positions


- node : [CurveHandlePositions](/docs/GeoNodes/CurveHandlePositions.md)
- self
- jump : No
- return : node

##### Arguments

- relative : None
- node_label : None
- node_color : None

#### Source code

``` python
def curve_handle_positions(self, relative=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CurveHandlePositions(relative=relative, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### curve_of_point


- node : [CurveOfPoint](/docs/GeoNodes/CurveOfPoint.md)
- self
- jump : No
- return : node

##### Arguments

- point_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def curve_of_point(self, point_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CurveOfPoint(point_index=point_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### curve_to_mesh


- node : [CurveToMesh](/docs/GeoNodes/CurveToMesh.md)
- self : curve
- jump : No
- return : mesh

##### Arguments

- profile_curve : None
- fill_caps : None
- node_label : None
- node_color : None

#### Source code

``` python
def curve_to_mesh(self, profile_curve=None, fill_caps=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps, node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### curve_to_points


- node : [CurveToPoints](/docs/GeoNodes/CurveToPoints.md)
- self : curve
- jump : No
- return : node

##### Arguments

- count : None
- length : None
- mode : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
- node_label : None
- node_color : None

#### Source code

``` python
def curve_to_points(self, count=None, length=None, mode='COUNT', node_label=None, node_color=None, **kwargs):
    node = self.tree.CurveToPoints(curve=self, count=count, length=length, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### deform_curves_on_surface


- node : [DeformCurvesOnSurface](/docs/GeoNodes/DeformCurvesOnSurface.md)
- self : curves
- jump : curves
- return : self

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def deform_curves_on_surface(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.DeformCurvesOnSurface(curves=self, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curves)
    return self
```
### delete_geometry


- node : [DeleteGeometry](/docs/GeoNodes/DeleteGeometry.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- mode : 'ALL' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')
- node_label : None
- node_color : None

#### Source code

``` python
def delete_geometry(self, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None, **kwargs):
    node = self.tree.DeleteGeometry(geometry=self, selection=self._get_selection(selection), domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### distribute_points_in_volume


- node : [DistributePointsInVolume](/docs/GeoNodes/DistributePointsInVolume.md)
- self : volume
- jump : No
- return : points

##### Arguments

- density : None
- seed : None
- spacing : None
- threshold : None
- mode : 'DENSITY_RANDOM' in ('DENSITY_RANDOM', 'DENSITY_GRID')
- node_label : None
- node_color : None

#### Source code

``` python
def distribute_points_in_volume(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None, **kwargs):
    node = self.tree.DistributePointsInVolume(volume=self, density=density, seed=seed, spacing=spacing, threshold=threshold, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.points
```
### distribute_points_on_faces


- node : [DistributePointsOnFaces](/docs/GeoNodes/DistributePointsOnFaces.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- density : None
- seed : None
- distance_min : None
- density_max : None
- density_factor : None
- selection : None
- distribute_method : 'RANDOM' in ('RANDOM', 'POISSON')
- use_legacy_normal : False
- node_label : None
- node_color : None

#### Source code

``` python
def distribute_points_on_faces(self, density=None, seed=None, distance_min=None, density_max=None, density_factor=None, selection=None, distribute_method='RANDOM', use_legacy_normal=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.DistributePointsOnFaces(mesh=self, density=density, seed=seed, distance_min=distance_min, density_max=density_max, density_factor=density_factor, selection=self._get_selection(selection), distribute_method=distribute_method, use_legacy_normal=use_legacy_normal, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### domain_size


- node : [DomainSize](/docs/GeoNodes/DomainSize.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- component : 'MESH' in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL')
- node_label : None
- node_color : None

#### Source code

``` python
def domain_size(self, component='MESH', node_label=None, node_color=None, **kwargs):
    node = self.tree.DomainSize(geometry=self, component=self._get_domain(component, ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### dual_mesh


- node : [DualMesh](/docs/GeoNodes/DualMesh.md)
- self : mesh
- jump : No
- return : mesh

##### Arguments

- keep_boundaries : None
- node_label : None
- node_color : None

#### Source code

``` python
def dual_mesh(self, keep_boundaries=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.DualMesh(mesh=self, keep_boundaries=keep_boundaries, node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### duplicate_elements


- node : [DuplicateElements](/docs/GeoNodes/DuplicateElements.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- amount : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def duplicate_elements(self, amount=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.DuplicateElements(geometry=self, amount=amount, selection=self._get_selection(selection), domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### edge_angle


- node : [EdgeAngle](/docs/GeoNodes/EdgeAngle.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def edge_angle(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgeAngle(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### edge_paths_to_curves


- node : [EdgePathsToCurves](/docs/GeoNodes/EdgePathsToCurves.md)
- self : mesh
- jump : No
- return : curves

##### Arguments

- start_vertices : None
- next_vertex_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgePathsToCurves(mesh=self, start_vertices=start_vertices, next_vertex_index=next_vertex_index, node_label=node_label, node_color=node_color, **kwargs)
    return node.curves
```
### edge_paths_to_selection


- node : [EdgePathsToSelection](/docs/GeoNodes/EdgePathsToSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- start_vertices : None
- next_vertex_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgePathsToSelection(start_vertices=start_vertices, next_vertex_index=next_vertex_index, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
```
### edge_vertices


- node : [EdgeVertices](/docs/GeoNodes/EdgeVertices.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def edge_vertices(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgeVertices(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### edges_of_corner


- node : [EdgesOfCorner](/docs/GeoNodes/EdgesOfCorner.md)
- self
- jump : No
- return : node

##### Arguments

- corner_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def edges_of_corner(self, corner_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgesOfCorner(corner_index=corner_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### edges_of_vertex


- node : [EdgesOfVertex](/docs/GeoNodes/EdgesOfVertex.md)
- self
- jump : No
- return : node

##### Arguments

- vertex_index : None
- weights : None
- sort_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgesOfVertex(vertex_index=vertex_index, weights=weights, sort_index=sort_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### edges_to_face_groups


- node : [EdgesToFaceGroups](/docs/GeoNodes/EdgesToFaceGroups.md)
- self
- jump : No
- return : face_group_id

##### Arguments

- boundary_edges : None
- node_label : None
- node_color : None

#### Source code

``` python
def edges_to_face_groups(self, boundary_edges=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EdgesToFaceGroups(boundary_edges=boundary_edges, node_label=node_label, node_color=node_color, **kwargs)
    return node.face_group_id
```
### endpoint_selection


- node : [EndpointSelection](/docs/GeoNodes/EndpointSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- start_size : None
- end_size : None
- node_label : None
- node_color : None

#### Source code

``` python
def endpoint_selection(self, start_size=None, end_size=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.EndpointSelection(start_size=start_size, end_size=end_size, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
```
### evaluate_at_index


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index(self, index=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_boolean


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_boolean(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='BOOLEAN', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_color


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_color(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_float


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_float(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_int


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_int(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='INT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_quaternion


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_quaternion(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='QUATERNION', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_at_index_vector


- node : [EvaluateAtIndex](/docs/GeoNodes/EvaluateAtIndex.md)
- self
- jump : No
- return : value

##### Arguments

- index : None
- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_at_index_vector(self, index=None, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateAtIndex(index=index, value=value, data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain(self, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_boolean


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_boolean(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='BOOLEAN', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_color


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_color(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_float


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_float(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_int


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_int(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='INT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_quaternion


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_quaternion(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='QUATERNION', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### evaluate_on_domain_vector


- node : [EvaluateOnDomain](/docs/GeoNodes/EvaluateOnDomain.md)
- self
- jump : No
- return : value

##### Arguments

- value : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def evaluate_on_domain_vector(self, value=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.EvaluateOnDomain(value=value, data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### extrude_mesh


- node : [ExtrudeMesh](/docs/GeoNodes/ExtrudeMesh.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- offset : None
- offset_scale : None
- individual : None
- selection : None
- mode : 'FACES' in ('VERTICES', 'EDGES', 'FACES')
- node_label : None
- node_color : None

#### Source code

``` python
def extrude_mesh(self, offset=None, offset_scale=None, individual=None, selection=None, mode='FACES', node_label=None, node_color=None, **kwargs):
    node = self.tree.ExtrudeMesh(mesh=self, offset=offset, offset_scale=offset_scale, individual=individual, selection=self._get_selection(selection), mode=self._get_domain(mode, ('VERTICES', 'EDGES', 'FACES')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### face_group_boundaries


- node : [FaceGroupBoundaries](/docs/GeoNodes/FaceGroupBoundaries.md)
- self
- jump : No
- return : boundaries_edges

##### Arguments

- face_group_id : None
- node_label : None
- node_color : None

#### Source code

``` python
def face_group_boundaries(self, face_group_id=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FaceGroupBoundaries(face_group_id=face_group_id, node_label=node_label, node_color=node_color, **kwargs)
    return node.boundaries_edges
```
### face_neighbors


- node : [FaceNeighbors](/docs/GeoNodes/FaceNeighbors.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def face_neighbors(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.FaceNeighbors(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### face_of_corner


- node : [FaceOfCorner](/docs/GeoNodes/FaceOfCorner.md)
- self
- jump : No
- return : node

##### Arguments

- corner_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def face_of_corner(self, corner_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FaceOfCorner(corner_index=corner_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### fill_curve


- node : [FillCurve](/docs/GeoNodes/FillCurve.md)
- self : curve
- jump : No
- return : mesh

##### Arguments

- group_id : None
- mode : 'TRIANGLES' in ('TRIANGLES', 'NGONS')
- node_label : None
- node_color : None

#### Source code

``` python
def fill_curve(self, group_id=None, mode='TRIANGLES', node_label=None, node_color=None, **kwargs):
    node = self.tree.FillCurve(curve=self, group_id=group_id, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### fillet_curve


- node : [FilletCurve](/docs/GeoNodes/FilletCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- radius : None
- limit_radius : None
- count : None
- mode : 'BEZIER' in ('BEZIER', 'POLY')
- node_label : None
- node_color : None

#### Source code

``` python
def fillet_curve(self, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None, **kwargs):
    node = self.tree.FilletCurve(curve=self, radius=radius, limit_radius=limit_radius, count=count, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### fillet_curve_bezier


- node : [FilletCurve](/docs/GeoNodes/FilletCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- radius : None
- limit_radius : None
- node_label : None
- node_color : None

#### Source code

``` python
def fillet_curve_bezier(self, radius=None, limit_radius=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FilletCurve(curve=self, radius=radius, limit_radius=limit_radius, mode='BEZIER', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### fillet_curve_poly


- node : [FilletCurve](/docs/GeoNodes/FilletCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- count : None
- radius : None
- limit_radius : None
- node_label : None
- node_color : None

#### Source code

``` python
def fillet_curve_poly(self, count=None, radius=None, limit_radius=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode='POLY', node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### flip_faces


- node : [FlipFaces](/docs/GeoNodes/FlipFaces.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def flip_faces(self, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.FlipFaces(mesh=self, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### geometry_proximity


- node : [GeometryProximity](/docs/GeoNodes/GeometryProximity.md)
- self : target
- jump : No
- return : node

##### Arguments

- geometry : None
- sample_position : None
- target_element : 'FACES' in ('POINTS', 'EDGES', 'FACES')
- node_label : None
- node_color : None

#### Source code

``` python
def geometry_proximity(self, geometry=None, sample_position=None, target_element='FACES', node_label=None, node_color=None, **kwargs):
    node = self.tree.GeometryProximity(geometry=geometry, sample_position=sample_position, target_element=self._get_domain(target_element, ('POINTS', 'EDGES', 'FACES')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### geometry_to_instance


- node : [GeometryToInstance](/docs/GeoNodes/GeometryToInstance.md)
- self : geometry
- jump : No
- return : instances

##### Arguments

- *args : 'ARG_NO_VALUE'
- node_label : None
- node_color : None

#### Source code

``` python
def geometry_to_instance(self, *args, node_label=None, node_color=None, **kwargs):
    node = self.tree.GeometryToInstance(*args, geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    return node.instances
```
### handle_type_selection


- node : [HandleTypeSelection](/docs/GeoNodes/HandleTypeSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : {'LEFT', 'RIGHT'}
- node_label : None
- node_color : None

#### Source code

``` python
def handle_type_selection(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, node_label=None, node_color=None, **kwargs):
    node = self.tree.HandleTypeSelection(handle_type=handle_type, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
```
### index_of_nearest


- node : [IndexOfNearest](/docs/GeoNodes/IndexOfNearest.md)
- self
- jump : No
- return : node

##### Arguments

- position : None
- group_id : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_of_nearest(self, position=None, group_id=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexOfNearest(position=position, group_id=group_id, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### index_switch


- node : [IndexSwitch](/docs/GeoNodes/IndexSwitch.md)
- self : ARG0
- jump : No
- return : output

##### Arguments

- *args : 'ARG_NO_VALUE'
- index : None
- node_label : None
- node_color : None

#### Source code

``` python
def index_switch(self, *args, index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IndexSwitch(self, *args, index=index, data_type='GEOMETRY', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### instance_on_points


- node : [InstanceOnPoints](/docs/GeoNodes/InstanceOnPoints.md)
- self : points
- jump : No
- return : instances

##### Arguments

- instance : None
- pick_instance : None
- instance_index : None
- rotation : None
- scale : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.InstanceOnPoints(points=self, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    return node.instances
```
### instances_to_points


- node : [InstancesToPoints](/docs/GeoNodes/InstancesToPoints.md)
- self : instances
- jump : No
- return : points

##### Arguments

- position : None
- radius : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def instances_to_points(self, position=None, radius=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.InstancesToPoints(instances=self, position=position, radius=radius, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    return node.points
```
### interpolate_curves


- node : [InterpolateCurves](/docs/GeoNodes/InterpolateCurves.md)
- self : guide_curves
- jump : No
- return : node

##### Arguments

- guide_up : None
- guide_group_id : None
- points : None
- point_up : None
- point_group_id : None
- max_neighbors : None
- node_label : None
- node_color : None

#### Source code

``` python
def interpolate_curves(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.InterpolateCurves(guide_curves=self, guide_up=guide_up, guide_group_id=guide_group_id, points=points, point_up=point_up, point_group_id=point_group_id, max_neighbors=max_neighbors, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### is_face_planar


- node : [IsFacePlanar](/docs/GeoNodes/IsFacePlanar.md)
- self
- jump : No
- return : planar

##### Arguments

- threshold : None
- node_label : None
- node_color : None

#### Source code

``` python
def is_face_planar(self, threshold=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.IsFacePlanar(threshold=threshold, node_label=node_label, node_color=node_color, **kwargs)
    return node.planar
```
### join_geometry


- node : [JoinGeometry](/docs/GeoNodes/JoinGeometry.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- *args : 'ARG_NO_VALUE'
- node_label : None
- node_color : None

#### Source code

``` python
def join_geometry(self, *args, node_label=None, node_color=None, **kwargs):
    node = self.tree.JoinGeometry(*args, geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### left_handle_type_selection


- node : [HandleTypeSelection](/docs/GeoNodes/HandleTypeSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- node_label : None
- node_color : None

#### Source code

``` python
def left_handle_type_selection(self, handle_type='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.HandleTypeSelection(handle_type=handle_type, mode={'LEFT'}, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
```
### merge_by_distance


- node : [MergeByDistance](/docs/GeoNodes/MergeByDistance.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- distance : None
- selection : None
- mode : 'ALL' in ('ALL', 'CONNECTED')
- node_label : None
- node_color : None

#### Source code

``` python
def merge_by_distance(self, distance=None, selection=None, mode='ALL', node_label=None, node_color=None, **kwargs):
    node = self.tree.MergeByDistance(geometry=self, distance=distance, selection=self._get_selection(selection), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### mesh_difference


- node : [MeshBoolean](/docs/GeoNodes/MeshBoolean.md)
- self : mesh_1
- jump : No
- return : mesh

##### Arguments

- *args : 'ARG_NO_VALUE'
- mesh_2 : None
- self_intersection : None
- hole_tolerant : None
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_difference(self, *args, mesh_2=None, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshBoolean(*args, mesh_1=self, mesh_2=mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### mesh_intersect


- node : [MeshBoolean](/docs/GeoNodes/MeshBoolean.md)
- self : mesh_2
- jump : No
- return : mesh

##### Arguments

- *args : 'ARG_NO_VALUE'
- self_intersection : None
- hole_tolerant : None
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_intersect(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshBoolean(*args, mesh_2=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### mesh_island


- node : [MeshIsland](/docs/GeoNodes/MeshIsland.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def mesh_island(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshIsland(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### mesh_to_curve


- node : [MeshToCurve](/docs/GeoNodes/MeshToCurve.md)
- self : mesh
- jump : No
- return : curve

##### Arguments

- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_to_curve(self, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshToCurve(mesh=self, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    return node.curve
```
### mesh_to_points


- node : [MeshToPoints](/docs/GeoNodes/MeshToPoints.md)
- self : mesh
- jump : No
- return : points

##### Arguments

- position : None
- radius : None
- selection : None
- mode : 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_to_points(self, position=None, radius=None, selection=None, mode='VERTICES', node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshToPoints(mesh=self, position=position, radius=radius, selection=self._get_selection(selection), mode=self._get_domain(mode, ('VERTICES', 'EDGES', 'FACES', 'CORNERS')), node_label=node_label, node_color=node_color, **kwargs)
    return node.points
```
### mesh_to_volume


- node : [MeshToVolume](/docs/GeoNodes/MeshToVolume.md)
- self : mesh
- jump : No
- return : volume

##### Arguments

- density : None
- voxel_amount : None
- interior_band_width : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_to_volume(self, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshToVolume(mesh=self, density=density, voxel_amount=voxel_amount, interior_band_width=interior_band_width, voxel_size=voxel_size, resolution_mode=resolution_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.volume
```
### mesh_union


- node : [MeshBoolean](/docs/GeoNodes/MeshBoolean.md)
- self : mesh_2
- jump : No
- return : mesh

##### Arguments

- *args : 'ARG_NO_VALUE'
- self_intersection : None
- hole_tolerant : None
- node_label : None
- node_color : None

#### Source code

``` python
def mesh_union(self, *args, self_intersection=None, hole_tolerant=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.MeshBoolean(*args, mesh_2=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### named_attribute


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- node_label : None
- node_color : None

#### Source code

``` python
def named_attribute(self, name=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type=data_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_boolean


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_boolean(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='BOOLEAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_color


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_color(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='FLOAT_COLOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_float


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_float(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='FLOAT', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_int


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_int(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='INT', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_quaternion


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_quaternion(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='QUATERNION', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### named_vector


- node : [NamedAttribute](/docs/GeoNodes/NamedAttribute.md)
- self
- jump : No
- return : attribute

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def named_vector(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.NamedAttribute(name=name, data_type='FLOAT_VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.attribute
```
### offset_corner_in_face


- node : [OffsetCornerInFace](/docs/GeoNodes/OffsetCornerInFace.md)
- self
- jump : No
- return : corner_index

##### Arguments

- corner_index : None
- offset : None
- node_label : None
- node_color : None

#### Source code

``` python
def offset_corner_in_face(self, corner_index=None, offset=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.OffsetCornerInFace(corner_index=corner_index, offset=offset, node_label=node_label, node_color=node_color, **kwargs)
    return node.corner_index
```
### offset_point_in_curve


- node : [OffsetPointInCurve](/docs/GeoNodes/OffsetPointInCurve.md)
- self
- jump : No
- return : node

##### Arguments

- point_index : None
- offset : None
- node_label : None
- node_color : None

#### Source code

``` python
def offset_point_in_curve(self, point_index=None, offset=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.OffsetPointInCurve(point_index=point_index, offset=offset, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### points_of_curve


- node : [PointsOfCurve](/docs/GeoNodes/PointsOfCurve.md)
- self
- jump : No
- return : node

##### Arguments

- curve_index : None
- weights : None
- sort_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def points_of_curve(self, curve_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.PointsOfCurve(curve_index=curve_index, weights=weights, sort_index=sort_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### points_to_curves


- node : [PointsToCurves](/docs/GeoNodes/PointsToCurves.md)
- self : points
- jump : No
- return : curves

##### Arguments

- curve_group_id : None
- weight : None
- node_label : None
- node_color : None

#### Source code

``` python
def points_to_curves(self, curve_group_id=None, weight=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.PointsToCurves(points=self, curve_group_id=curve_group_id, weight=weight, node_label=node_label, node_color=node_color, **kwargs)
    return node.curves
```
### points_to_vertices


- node : [PointsToVertices](/docs/GeoNodes/PointsToVertices.md)
- self : points
- jump : No
- return : mesh

##### Arguments

- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def points_to_vertices(self, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.PointsToVertices(points=self, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
### points_to_volume


- node : [PointsToVolume](/docs/GeoNodes/PointsToVolume.md)
- self : points
- jump : No
- return : volume

##### Arguments

- density : None
- voxel_amount : None
- radius : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')
- node_label : None
- node_color : None

#### Source code

``` python
def points_to_volume(self, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None, **kwargs):
    node = self.tree.PointsToVolume(points=self, density=density, voxel_amount=voxel_amount, radius=radius, voxel_size=voxel_size, resolution_mode=resolution_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.volume
```
### raycast


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type, mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_boolean


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_boolean(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_color


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_color(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_COLOR', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_float


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_float(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_int


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_int(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_quaternion


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_quaternion(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='QUATERNION', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### raycast_vector


- node : [Raycast](/docs/GeoNodes/Raycast.md)
- self : target_geometry
- jump : No
- return : node

##### Arguments

- attribute : None
- source_position : None
- ray_direction : None
- ray_length : None
- mapping : 'INTERPOLATED' in ('INTERPOLATED', 'NEAREST')
- node_label : None
- node_color : None

#### Source code

``` python
def raycast_vector(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED', node_label=None, node_color=None, **kwargs):
    node = self.tree.Raycast(target_geometry=self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### realize_instances


- node : [RealizeInstances](/docs/GeoNodes/RealizeInstances.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def realize_instances(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.RealizeInstances(geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### remove_named_attribute


- node : [RemoveNamedAttribute](/docs/GeoNodes/RemoveNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- node_label : None
- node_color : None

#### Source code

``` python
def remove_named_attribute(self, name=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.RemoveNamedAttribute(geometry=self, name=name, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### replace_material


- node : [ReplaceMaterial](/docs/GeoNodes/ReplaceMaterial.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- old : None
- new : None
- node_label : None
- node_color : None

#### Source code

``` python
def replace_material(self, old=None, new=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ReplaceMaterial(geometry=self, old=old, new=new, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### resample_curve


- node : [ResampleCurve](/docs/GeoNodes/ResampleCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- count : None
- length : None
- selection : None
- mode : 'COUNT' in ('EVALUATED', 'COUNT', 'LENGTH')
- node_label : None
- node_color : None

#### Source code

``` python
def resample_curve(self, count=None, length=None, selection=None, mode='COUNT', node_label=None, node_color=None, **kwargs):
    node = self.tree.ResampleCurve(curve=self, count=count, length=length, selection=self._get_selection(selection), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### reverse_curve


- node : [ReverseCurve](/docs/GeoNodes/ReverseCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def reverse_curve(self, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ReverseCurve(curve=self, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### right_handle_type_selection


- node : [HandleTypeSelection](/docs/GeoNodes/HandleTypeSelection.md)
- self
- jump : No
- return : selection

##### Arguments

- handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- node_label : None
- node_color : None

#### Source code

``` python
def right_handle_type_selection(self, handle_type='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.HandleTypeSelection(handle_type=handle_type, mode={'RIGHT'}, node_label=node_label, node_color=node_color, **kwargs)
    return node.selection
```
### rotate_instances


- node : [RotateInstances](/docs/GeoNodes/RotateInstances.md)
- self : instances
- jump : instances
- return : self

##### Arguments

- rotation : None
- pivot_point : None
- local_space : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def rotate_instances(self, rotation=None, pivot_point=None, local_space=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.RotateInstances(instances=self, rotation=rotation, pivot_point=pivot_point, local_space=local_space, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.instances)
    return self
```
### sample_curve


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- length : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve(self, value=None, factor=None, curve_index=None, length=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, length=length, data_type=data_type, mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_boolean


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_boolean(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='BOOLEAN', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_boolean_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_boolean_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='BOOLEAN', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_boolean_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_boolean_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='BOOLEAN', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_color


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_color(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT_COLOR', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_color_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_color_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT_COLOR', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_color_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_color_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='FLOAT_COLOR', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_float


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_float(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_float_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_float_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_float_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_float_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='FLOAT', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_int


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_int(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='INT', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_int_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_int_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='INT', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_int_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_int_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='INT', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_quaternion


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_quaternion(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='QUATERNION', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_quaternion_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_quaternion_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='QUATERNION', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_quaternion_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_quaternion_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='QUATERNION', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_vector


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_vector(self, value=None, factor=None, curve_index=None, mode='FACTOR', use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT_VECTOR', mode=mode, use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_vector_factor


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- factor : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_vector_factor(self, value=None, factor=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, factor=factor, curve_index=curve_index, data_type='FLOAT_VECTOR', mode='FACTOR', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_curve_vector_length


- node : [SampleCurve](/docs/GeoNodes/SampleCurve.md)
- self : curves
- jump : No
- return : node

##### Arguments

- value : None
- length : None
- curve_index : None
- use_all_curves : False
- node_label : None
- node_color : None

#### Source code

``` python
def sample_curve_vector_length(self, value=None, length=None, curve_index=None, use_all_curves=False, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleCurve(curves=self, value=value, length=length, curve_index=curve_index, data_type='FLOAT_VECTOR', mode='LENGTH', use_all_curves=use_all_curves, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_index


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index(self, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_boolean


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_boolean(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='BOOLEAN', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_color


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_color(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_float


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_float(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_int


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_int(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='INT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_quaternion


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_quaternion(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='QUATERNION', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_index_vector


- node : [SampleIndex](/docs/GeoNodes/SampleIndex.md)
- self : geometry
- jump : No
- return : value

##### Arguments

- value : None
- index : None
- clamp : False
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_index_vector(self, value=None, index=None, clamp=False, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleIndex(geometry=self, value=value, index=index, clamp=clamp, data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest


- node : [SampleNearest](/docs/GeoNodes/SampleNearest.md)
- self : geometry
- jump : No
- return : index

##### Arguments

- sample_position : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest(self, sample_position=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearest(geometry=self, sample_position=sample_position, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER')), node_label=node_label, node_color=node_color, **kwargs)
    return node.index
```
### sample_nearest_surface


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface(self, value=None, sample_position=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type=data_type, node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_boolean


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_boolean(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='BOOLEAN', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_color


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_color(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='FLOAT_COLOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_float


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_float(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='FLOAT', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_int


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_int(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='INT', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_quaternion


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_quaternion(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='QUATERNION', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_nearest_surface_vector


- node : [SampleNearestSurface](/docs/GeoNodes/SampleNearestSurface.md)
- self : mesh
- jump : No
- return : value

##### Arguments

- value : None
- sample_position : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_nearest_surface_vector(self, value=None, sample_position=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleNearestSurface(mesh=self, value=value, sample_position=sample_position, data_type='FLOAT_VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node.value
```
### sample_uv_surface


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface(self, value=None, uv_map=None, sample_uv=None, data_type='FLOAT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type=data_type, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_boolean


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_boolean(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='BOOLEAN', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_color


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_color(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='FLOAT_COLOR', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_float


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_float(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='FLOAT', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_int


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_int(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='INT', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_quaternion


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_quaternion(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='QUATERNION', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sample_uv_surface_vector


- node : [SampleUVSurface](/docs/GeoNodes/SampleUVSurface.md)
- self : mesh
- jump : No
- return : node

##### Arguments

- value : None
- uv_map : None
- sample_uv : None
- node_label : None
- node_color : None

#### Source code

``` python
def sample_uv_surface_vector(self, value=None, uv_map=None, sample_uv=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SampleUVSurface(mesh=self, value=value, uv_map=uv_map, sample_uv=sample_uv, data_type='FLOAT_VECTOR', node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### scale_elements


- node : [ScaleElements](/docs/GeoNodes/ScaleElements.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- scale : None
- center : None
- axis : None
- selection : None
- domain : 'FACE' in ('FACE', 'EDGE')
- scale_mode : 'UNIFORM' in ('UNIFORM', 'SINGLE_AXIS')
- node_label : None
- node_color : None

#### Source code

``` python
def scale_elements(self, scale=None, center=None, axis=None, selection=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None, **kwargs):
    node = self.tree.ScaleElements(geometry=self, scale=scale, center=center, axis=axis, selection=self._get_selection(selection), domain=self._get_domain(domain, ('FACE', 'EDGE')), scale_mode=scale_mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### scale_instances


- node : [ScaleInstances](/docs/GeoNodes/ScaleInstances.md)
- self : instances
- jump : instances
- return : self

##### Arguments

- scale : None
- center : None
- local_space : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def scale_instances(self, scale=None, center=None, local_space=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ScaleInstances(instances=self, scale=scale, center=center, local_space=local_space, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.instances)
    return self
```
### separate_components


- node : [SeparateComponents](/docs/GeoNodes/SeparateComponents.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def separate_components(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.SeparateComponents(geometry=self, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### separate_geometry


- node : [SeparateGeometry](/docs/GeoNodes/SeparateGeometry.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def separate_geometry(self, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SeparateGeometry(geometry=self, selection=self._get_selection(selection), domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### set_curve_normal


- node : [SetCurveNormal](/docs/GeoNodes/SetCurveNormal.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- normal : None
- selection : None
- mode : 'MINIMUM_TWIST' in ('MINIMUM_TWIST', 'Z_UP', 'FREE')
- node_label : None
- node_color : None

#### Source code

``` python
def set_curve_normal(self, normal=None, selection=None, mode='MINIMUM_TWIST', node_label=None, node_color=None, **kwargs):
    node = self.tree.SetCurveNormal(curve=self, normal=normal, selection=self._get_selection(selection), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### set_curve_radius


- node : [SetCurveRadius](/docs/GeoNodes/SetCurveRadius.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- radius : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_curve_radius(self, radius=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetCurveRadius(curve=self, radius=radius, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### set_curve_tilt


- node : [SetCurveTilt](/docs/GeoNodes/SetCurveTilt.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- tilt : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_curve_tilt(self, tilt=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetCurveTilt(curve=self, tilt=tilt, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### set_handle_positions


- node : [SetHandlePositions](/docs/GeoNodes/SetHandlePositions.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- position : None
- offset : None
- selection : None
- mode : 'LEFT' in ('LEFT', 'RIGHT')
- node_label : None
- node_color : None

#### Source code

``` python
def set_handle_positions(self, position=None, offset=None, selection=None, mode='LEFT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SetHandlePositions(curve=self, position=position, offset=offset, selection=self._get_selection(selection), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### set_handle_type


- node : [SetHandleType](/docs/GeoNodes/SetHandleType.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- selection : None
- handle_type : 'AUTO' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- mode : {'LEFT', 'RIGHT'}
- node_label : None
- node_color : None

#### Source code

``` python
def set_handle_type(self, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetHandleType(curve=self, selection=self._get_selection(selection), handle_type=handle_type, mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### set_id


- node : [SetID](/docs/GeoNodes/SetID.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- ID : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_id(self, ID=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetID(geometry=self, ID=ID, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_material


- node : [SetMaterial](/docs/GeoNodes/SetMaterial.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- material : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_material(self, material=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetMaterial(geometry=self, material=material, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_material_index


- node : [SetMaterialIndex](/docs/GeoNodes/SetMaterialIndex.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- material_index : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_material_index(self, material_index=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetMaterialIndex(geometry=self, material_index=material_index, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_point_radius


- node : [SetPointRadius](/docs/GeoNodes/SetPointRadius.md)
- self : points
- jump : points
- return : self

##### Arguments

- radius : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_point_radius(self, radius=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetPointRadius(points=self, radius=radius, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.points)
    return self
```
### set_position


- node : [SetPosition](/docs/GeoNodes/SetPosition.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- position : None
- offset : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_position(self, position=None, offset=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetPosition(geometry=self, position=position, offset=offset, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_shade_smooth


- node : [SetShadeSmooth](/docs/GeoNodes/SetShadeSmooth.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- shade_smooth : None
- selection : None
- domain : 'FACE' in ('EDGE', 'FACE')
- node_label : None
- node_color : None

#### Source code

``` python
def set_shade_smooth(self, shade_smooth=None, selection=None, domain='FACE', node_label=None, node_color=None, **kwargs):
    node = self.tree.SetShadeSmooth(geometry=self, shade_smooth=shade_smooth, selection=self._get_selection(selection), domain=self._get_domain(domain, ('EDGE', 'FACE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_spline_cyclic


- node : [SetSplineCyclic](/docs/GeoNodes/SetSplineCyclic.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- cyclic : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_spline_cyclic(self, cyclic=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetSplineCyclic(geometry=self, cyclic=cyclic, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_spline_resolution


- node : [SetSplineResolution](/docs/GeoNodes/SetSplineResolution.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- resolution : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def set_spline_resolution(self, resolution=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SetSplineResolution(geometry=self, resolution=resolution, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### set_spline_type


- node : [SetSplineType](/docs/GeoNodes/SetSplineType.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- selection : None
- spline_type : 'POLY' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')
- node_label : None
- node_color : None

#### Source code

``` python
def set_spline_type(self, selection=None, spline_type='POLY', node_label=None, node_color=None, **kwargs):
    node = self.tree.SetSplineType(curve=self, selection=self._get_selection(selection), spline_type=spline_type, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### shortest_edge_paths


- node : [ShortestEdgePaths](/docs/GeoNodes/ShortestEdgePaths.md)
- self
- jump : No
- return : node

##### Arguments

- end_vertex : None
- edge_cost : None
- node_label : None
- node_color : None

#### Source code

``` python
def shortest_edge_paths(self, end_vertex=None, edge_cost=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.ShortestEdgePaths(end_vertex=end_vertex, edge_cost=edge_cost, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### sort_elements


- node : [SortElements](/docs/GeoNodes/SortElements.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- group_id : None
- sort_weight : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def sort_elements(self, group_id=None, sort_weight=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SortElements(geometry=self, group_id=group_id, sort_weight=sort_weight, selection=self._get_selection(selection), domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### spline_length


- node : [SplineLength](/docs/GeoNodes/SplineLength.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def spline_length(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.SplineLength(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### spline_parameter


- node : [SplineParameter](/docs/GeoNodes/SplineParameter.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def spline_parameter(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.SplineParameter(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### split_edges


- node : [SplitEdges](/docs/GeoNodes/SplitEdges.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def split_edges(self, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SplitEdges(mesh=self, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### split_to_instances


- node : [SplitToInstances](/docs/GeoNodes/SplitToInstances.md)
- self : geometry
- jump : No
- return : instances

##### Arguments

- group_id : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def split_to_instances(self, group_id=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.SplitToInstances(geometry=self, group_id=group_id, selection=self._get_selection(selection), domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    return node.instances
```
### store_named_attribute


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'QUATERNION')
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_attribute(self, name=None, value=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type=data_type, domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_boolean


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_boolean(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='BOOLEAN', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_byte_color


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_byte_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='BYTE_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_float


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_float(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='FLOAT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_float2


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_float2(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='FLOAT2', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_float_color


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_float_color(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_int


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_int(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='INT', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_quaternion


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_quaternion(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='QUATERNION', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### store_named_vector


- node : [StoreNamedAttribute](/docs/GeoNodes/StoreNamedAttribute.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- name : None
- value : None
- selection : None
- domain : 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
- node_label : None
- node_color : None

#### Source code

``` python
def store_named_vector(self, name=None, value=None, selection=None, domain='POINT', node_label=None, node_color=None, **kwargs):
    node = self.tree.StoreNamedAttribute(geometry=self, name=name, value=value, selection=self._get_selection(selection), data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### subdivide_curve


- node : [SubdivideCurve](/docs/GeoNodes/SubdivideCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- cuts : None
- node_label : None
- node_color : None

#### Source code

``` python
def subdivide_curve(self, cuts=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SubdivideCurve(curve=self, cuts=cuts, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### subdivide_mesh


- node : [SubdivideMesh](/docs/GeoNodes/SubdivideMesh.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- level : None
- node_label : None
- node_color : None

#### Source code

``` python
def subdivide_mesh(self, level=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.SubdivideMesh(mesh=self, level=level, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### subdivision_surface


- node : [SubdivisionSurface](/docs/GeoNodes/SubdivisionSurface.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- level : None
- edge_crease : None
- vertex_crease : None
- boundary_smooth : 'ALL' in ('PRESERVE_CORNERS', 'ALL')
- uv_smooth : 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
- node_label : None
- node_color : None

#### Source code

``` python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None, **kwargs):
    node = self.tree.SubdivisionSurface(mesh=self, level=level, edge_crease=edge_crease, vertex_crease=vertex_crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### switch


- node : [Switch](/docs/GeoNodes/Switch.md)
- self : false
- jump : No
- return : output

##### Arguments

- switch : None
- true : None
- node_label : None
- node_color : None

#### Source code

``` python
def switch(self, switch=None, true=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.Switch(switch=switch, false=self, true=true, input_type='GEOMETRY', node_label=node_label, node_color=node_color, **kwargs)
    return node.output
```
### transform_geometry


- node : [TransformGeometry](/docs/GeoNodes/TransformGeometry.md)
- self : geometry
- jump : geometry
- return : self

##### Arguments

- translation : None
- rotation : None
- scale : None
- node_label : None
- node_color : None

#### Source code

``` python
def transform_geometry(self, translation=None, rotation=None, scale=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.TransformGeometry(geometry=self, translation=translation, rotation=rotation, scale=scale, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.geometry)
    return self
```
### translate_instances


- node : [TranslateInstances](/docs/GeoNodes/TranslateInstances.md)
- self : instances
- jump : instances
- return : self

##### Arguments

- translation : None
- local_space : None
- selection : None
- node_label : None
- node_color : None

#### Source code

``` python
def translate_instances(self, translation=None, local_space=None, selection=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.TranslateInstances(instances=self, translation=translation, local_space=local_space, selection=self._get_selection(selection), node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.instances)
    return self
```
### triangulate


- node : [Triangulate](/docs/GeoNodes/Triangulate.md)
- self : mesh
- jump : mesh
- return : self

##### Arguments

- minimum_vertices : None
- selection : None
- ngon_method : 'BEAUTY' in ('BEAUTY', 'CLIP')
- quad_method : 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
- node_label : None
- node_color : None

#### Source code

``` python
def triangulate(self, minimum_vertices=None, selection=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None, **kwargs):
    node = self.tree.Triangulate(mesh=self, minimum_vertices=minimum_vertices, selection=self._get_selection(selection), ngon_method=ngon_method, quad_method=quad_method, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.mesh)
    return self
```
### trim_curve


- node : [TrimCurve](/docs/GeoNodes/TrimCurve.md)
- self : curve
- jump : curve
- return : self

##### Arguments

- start : None
- end : None
- selection : None
- mode : 'FACTOR' in ('FACTOR', 'LENGTH')
- node_label : None
- node_color : None

#### Source code

``` python
def trim_curve(self, start=None, end=None, selection=None, mode='FACTOR', node_label=None, node_color=None, **kwargs):
    node = self.tree.TrimCurve(curve=self, start=start, end=end, selection=self._get_selection(selection), mode=mode, node_label=node_label, node_color=node_color, **kwargs)
    self.jump(node.curve)
    return self
```
### uv_unwrap


- node : [UVUnwrap](/docs/GeoNodes/UVUnwrap.md)
- self
- jump : No
- return : uv

##### Arguments

- seam : None
- margin : None
- fill_holes : None
- selection : None
- method : 'ANGLE_BASED' in ('ANGLE_BASED', 'CONFORMAL')
- node_label : None
- node_color : None

#### Source code

``` python
def uv_unwrap(self, seam=None, margin=None, fill_holes=None, selection=None, method='ANGLE_BASED', node_label=None, node_color=None, **kwargs):
    node = self.tree.UVUnwrap(seam=seam, margin=margin, fill_holes=fill_holes, selection=self._get_selection(selection), method=method, node_label=node_label, node_color=node_color, **kwargs)
    return node.uv
```
### vertex_neighbors


- node : [VertexNeighbors](/docs/GeoNodes/VertexNeighbors.md)
- self
- jump : No
- return : node

##### Arguments

- node_label : None
- node_color : None

#### Source code

``` python
def vertex_neighbors(self, node_label=None, node_color=None, **kwargs):
    node = self.tree.VertexNeighbors(node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### vertex_of_corner


- node : [VertexOfCorner](/docs/GeoNodes/VertexOfCorner.md)
- self
- jump : No
- return : node

##### Arguments

- corner_index : None
- node_label : None
- node_color : None

#### Source code

``` python
def vertex_of_corner(self, corner_index=None, node_label=None, node_color=None, **kwargs):
    node = self.tree.VertexOfCorner(corner_index=corner_index, node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- data_type : 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION')
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer(self, value=None, data_type='FLOAT', domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type=data_type, domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_boolean


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_boolean(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='BOOLEAN', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_color


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_color(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='FLOAT_COLOR', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_float


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_float(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='FLOAT', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_int


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_int(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='INT', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_quaternion


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_quaternion(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='QUATERNION', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### viewer_vector


- node : [Viewer](/docs/GeoNodes/Viewer.md)
- self : geometry
- jump : No
- return : node

##### Arguments

- value : None
- domain : 'AUTO' in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')
- node_label : None
- node_color : None

#### Source code

``` python
def viewer_vector(self, value=None, domain='AUTO', node_label=None, node_color=None, **kwargs):
    node = self.tree.Viewer(geometry=self, value=value, data_type='FLOAT_VECTOR', domain=self._get_domain(domain, ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER')), node_label=node_label, node_color=node_color, **kwargs)
    return node
```
### volume_to_mesh


- node : [VolumeToMesh](/docs/GeoNodes/VolumeToMesh.md)
- self : volume
- jump : No
- return : mesh

##### Arguments

- threshold : None
- adaptivity : None
- voxel_amount : None
- voxel_size : None
- resolution_mode : 'GRID' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
- node_label : None
- node_color : None

#### Source code

``` python
def volume_to_mesh(self, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None, **kwargs):
    node = self.tree.VolumeToMesh(volume=self, threshold=threshold, adaptivity=adaptivity, voxel_amount=voxel_amount, voxel_size=voxel_size, resolution_mode=resolution_mode, node_label=node_label, node_color=node_color, **kwargs)
    return node.mesh
```
