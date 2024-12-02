# nd

> All nodes


This class exposes all possible Geometry Nodes under their **snake_case** name.

``` python
# Node 'Set Position'
nd.set_position()
```

### Returned values

- When the node has only one output socket, this socket is returned.
- When the node has several output sockets, the node is returned.
- Output sockets can be read using their **snake_case** name:

``` python
# 'Set Position' node has  only one output socket
geometry = nd.set_position()

# 'Rotation to Axis Angle' node has two output sockets
node = nd.rotation_to_axis_angle()
axis = node.axis
angle = node.angle
```

### Methods arguments

Methods arguments are:
- the snake case name of the node sockets
- the node parameters

``` python
node = nd.set_position(geometry=None, selection=None, position=None, offset=None)

# 'Math' node has two parameters : operation and use_clamp
sum = nd.math(value=1, value_1=1, operation='ADD', use_clamp=False)
```

### Properties

Nodes with no output socket are implemented as properties:

``` python
# Node 'Index'
index = nd.index

# Node 'Special Characters'
node = nd.special_characters
line_break = node.line_break
tab = node.tab
```

## Content

- **A** : [accumulate_field](nd.md#accumulate_field) :black_small_square: [active_element](nd.md#active_element) :black_small_square: [align_euler_to_vector](nd.md#align_euler_to_vector) :black_small_square: [align_rotation_to_vector](nd.md#align_rotation_to_vector) :black_small_square: [arc](nd.md#arc) :black_small_square: [attribute_statistic](nd.md#attribute_statistic) :black_small_square: [axes_to_rotation](nd.md#axes_to_rotation) :black_small_square: [axis_angle_to_rotation](nd.md#axis_angle_to_rotation)
- **B** : [bake](nd.md#bake) :black_small_square: [bezier_segment](nd.md#bezier_segment) :black_small_square: [blackbody](nd.md#blackbody) :black_small_square: [blur_attribute](nd.md#blur_attribute) :black_small_square: [boolean](nd.md#boolean) :black_small_square: [boolean_math](nd.md#boolean_math) :black_small_square: [bounding_box](nd.md#bounding_box) :black_small_square: [brick_texture](nd.md#brick_texture)
- **C** : [capture_attribute](nd.md#capture_attribute) :black_small_square: [checker_texture](nd.md#checker_texture) :black_small_square: [clamp](nd.md#clamp) :black_small_square: [collection_info](nd.md#collection_info) :black_small_square: [color](nd.md#color) :black_small_square: [color_ramp](nd.md#color_ramp) :black_small_square: [combine_color](nd.md#combine_color) :black_small_square: [combine_matrix](nd.md#combine_matrix) :black_small_square: [combine_transform](nd.md#combine_transform) :black_small_square: [combine_xyz](nd.md#combine_xyz) :black_small_square: [compare](nd.md#compare) :black_small_square: [cone](nd.md#cone) :black_small_square: [convex_hull](nd.md#convex_hull) :black_small_square: [corners_of_edge](nd.md#corners_of_edge) :black_small_square: [corners_of_face](nd.md#corners_of_face) :black_small_square: [corners_of_vertex](nd.md#corners_of_vertex) :black_small_square: [cube](nd.md#cube) :black_small_square: [curve_circle](nd.md#curve_circle) :black_small_square: [curve_handle_positions](nd.md#curve_handle_positions) :black_small_square: [curve_length](nd.md#curve_length) :black_small_square: [curve_line](nd.md#curve_line) :black_small_square: [curve_of_point](nd.md#curve_of_point) :black_small_square: [curves_to_grease_pencil](nd.md#curves_to_grease_pencil) :black_small_square: [curve_to_mesh](nd.md#curve_to_mesh) :black_small_square: [curve_to_points](nd.md#curve_to_points) :black_small_square: [cylinder](nd.md#cylinder)
- **D** : [deform_curves_on_surface](nd.md#deform_curves_on_surface) :black_small_square: [delete_geometry](nd.md#delete_geometry) :black_small_square: [dial_gizmo](nd.md#dial_gizmo) :black_small_square: [distribute_points_in_grid](nd.md#distribute_points_in_grid) :black_small_square: [distribute_points_in_volume](nd.md#distribute_points_in_volume) :black_small_square: [distribute_points_on_faces](nd.md#distribute_points_on_faces) :black_small_square: [domain_size](nd.md#domain_size) :black_small_square: [dual_mesh](nd.md#dual_mesh) :black_small_square: [duplicate_elements](nd.md#duplicate_elements)
- **E** : [edge_paths_to_curves](nd.md#edge_paths_to_curves) :black_small_square: [edge_paths_to_selection](nd.md#edge_paths_to_selection) :black_small_square: [edges_of_corner](nd.md#edges_of_corner) :black_small_square: [edges_of_vertex](nd.md#edges_of_vertex) :black_small_square: [edges_to_face_groups](nd.md#edges_to_face_groups) :black_small_square: [endpoint_selection](nd.md#endpoint_selection) :black_small_square: [euler_to_rotation](nd.md#euler_to_rotation) :black_small_square: [evaluate_at_index](nd.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](nd.md#evaluate_on_domain) :black_small_square: [extrude_mesh](nd.md#extrude_mesh)
- **F** : [face_group_boundaries](nd.md#face_group_boundaries) :black_small_square: [face_of_corner](nd.md#face_of_corner) :black_small_square: [fill_curve](nd.md#fill_curve) :black_small_square: [fillet_curve](nd.md#fillet_curve) :black_small_square: [flip_faces](nd.md#flip_faces) :black_small_square: [float_curve](nd.md#float_curve) :black_small_square: [float_to_integer](nd.md#float_to_integer) :black_small_square: [frame](nd.md#frame)
- **G** : [gabor_texture](nd.md#gabor_texture) :black_small_square: [geometry_proximity](nd.md#geometry_proximity) :black_small_square: [geometry_to_instance](nd.md#geometry_to_instance) :black_small_square: [get_named_grid](nd.md#get_named_grid) :black_small_square: [gradient_texture](nd.md#gradient_texture) :black_small_square: [grease_pencil_to_curves](nd.md#grease_pencil_to_curves) :black_small_square: [grid](nd.md#grid) :black_small_square: [grid_to_mesh](nd.md#grid_to_mesh) :black_small_square: [group](nd.md#group) :black_small_square: [group_output](nd.md#group_output)
- **H** : [handle_type_selection](nd.md#handle_type_selection) :black_small_square: [hash_value](nd.md#hash_value)
- **I** : [ico_sphere](nd.md#ico_sphere) :black_small_square: [image](nd.md#image) :black_small_square: [image_info](nd.md#image_info) :black_small_square: [image_texture](nd.md#image_texture) :black_small_square: [import_obj](nd.md#import_obj) :black_small_square: [import_ply](nd.md#import_ply) :black_small_square: [import_stl](nd.md#import_stl) :black_small_square: [index_of_nearest](nd.md#index_of_nearest) :black_small_square: [index_switch](nd.md#index_switch) :black_small_square: [instance_on_points](nd.md#instance_on_points) :black_small_square: [instances_to_points](nd.md#instances_to_points) :black_small_square: [integer](nd.md#integer) :black_small_square: [integer_math](nd.md#integer_math) :black_small_square: [interpolate_curves](nd.md#interpolate_curves) :black_small_square: [invert_matrix](nd.md#invert_matrix) :black_small_square: [invert_rotation](nd.md#invert_rotation) :black_small_square: [is_face_planar](nd.md#is_face_planar)
- **J** : [join_geometry](nd.md#join_geometry) :black_small_square: [join_strings](nd.md#join_strings)
- **L** : [linear_gizmo](nd.md#linear_gizmo)
- **M** : [magic_texture](nd.md#magic_texture) :black_small_square: [map_range](nd.md#map_range) :black_small_square: [material](nd.md#material) :black_small_square: [material_selection](nd.md#material_selection) :black_small_square: [math](nd.md#math) :black_small_square: [matrix_determinant](nd.md#matrix_determinant) :black_small_square: [menu_switch](nd.md#menu_switch) :black_small_square: [merge_by_distance](nd.md#merge_by_distance) :black_small_square: [merge_layers](nd.md#merge_layers) :black_small_square: [mesh_boolean](nd.md#mesh_boolean) :black_small_square: [mesh_circle](nd.md#mesh_circle) :black_small_square: [mesh_line](nd.md#mesh_line) :black_small_square: [mesh_to_curve](nd.md#mesh_to_curve) :black_small_square: [mesh_to_density_grid](nd.md#mesh_to_density_grid) :black_small_square: [mesh_to_points](nd.md#mesh_to_points) :black_small_square: [mesh_to_sdf_grid](nd.md#mesh_to_sdf_grid) :black_small_square: [mesh_to_volume](nd.md#mesh_to_volume) :black_small_square: [mix](nd.md#mix) :black_small_square: [multiply_matrices](nd.md#multiply_matrices)
- **N** : [named_attribute](nd.md#named_attribute) :black_small_square: [named_layer_selection](nd.md#named_layer_selection) :black_small_square: [noise_texture](nd.md#noise_texture)
- **O** : [object_info](nd.md#object_info) :black_small_square: [offset_corner_in_face](nd.md#offset_corner_in_face) :black_small_square: [offset_point_in_curve](nd.md#offset_point_in_curve)
- **P** : [pack_uv_islands](nd.md#pack_uv_islands) :black_small_square: [points](nd.md#points) :black_small_square: [points_of_curve](nd.md#points_of_curve) :black_small_square: [points_to_curves](nd.md#points_to_curves) :black_small_square: [points_to_sdf_grid](nd.md#points_to_sdf_grid) :black_small_square: [points_to_vertices](nd.md#points_to_vertices) :black_small_square: [points_to_volume](nd.md#points_to_volume) :black_small_square: [project_point](nd.md#project_point)
- **Q** : [quadratic_bezier](nd.md#quadratic_bezier) :black_small_square: [quadrilateral](nd.md#quadrilateral) :black_small_square: [quaternion_to_rotation](nd.md#quaternion_to_rotation)
- **R** : [random_value](nd.md#random_value) :black_small_square: [raycast](nd.md#raycast) :black_small_square: [realize_instances](nd.md#realize_instances) :black_small_square: [remove_named_attribute](nd.md#remove_named_attribute) :black_small_square: [repeat_input](nd.md#repeat_input) :black_small_square: [repeat_output](nd.md#repeat_output) :black_small_square: [replace_material](nd.md#replace_material) :black_small_square: [replace_string](nd.md#replace_string) :black_small_square: [reroute](nd.md#reroute) :black_small_square: [resample_curve](nd.md#resample_curve) :black_small_square: [reverse_curve](nd.md#reverse_curve) :black_small_square: [rgb_curves](nd.md#rgb_curves) :black_small_square: [rotate_euler](nd.md#rotate_euler) :black_small_square: [rotate_instances](nd.md#rotate_instances) :black_small_square: [rotate_rotation](nd.md#rotate_rotation) :black_small_square: [rotate_vector](nd.md#rotate_vector) :black_small_square: [rotation](nd.md#rotation) :black_small_square: [rotation_to_axis_angle](nd.md#rotation_to_axis_angle) :black_small_square: [rotation_to_euler](nd.md#rotation_to_euler) :black_small_square: [rotation_to_quaternion](nd.md#rotation_to_quaternion)
- **S** : [sample_curve](nd.md#sample_curve) :black_small_square: [sample_grid](nd.md#sample_grid) :black_small_square: [sample_grid_index](nd.md#sample_grid_index) :black_small_square: [sample_index](nd.md#sample_index) :black_small_square: [sample_nearest](nd.md#sample_nearest) :black_small_square: [sample_nearest_surface](nd.md#sample_nearest_surface) :black_small_square: [sample_uv_surface](nd.md#sample_uv_surface) :black_small_square: [scale_elements](nd.md#scale_elements) :black_small_square: [scale_instances](nd.md#scale_instances) :black_small_square: [sdf_grid_boolean](nd.md#sdf_grid_boolean) :black_small_square: [separate_color](nd.md#separate_color) :black_small_square: [separate_components](nd.md#separate_components) :black_small_square: [separate_geometry](nd.md#separate_geometry) :black_small_square: [separate_matrix](nd.md#separate_matrix) :black_small_square: [separate_transform](nd.md#separate_transform) :black_small_square: [separate_xyz](nd.md#separate_xyz) :black_small_square: [set_curve_normal](nd.md#set_curve_normal) :black_small_square: [set_curve_radius](nd.md#set_curve_radius) :black_small_square: [set_curve_tilt](nd.md#set_curve_tilt) :black_small_square: [set_face_set](nd.md#set_face_set) :black_small_square: [set_geometry_name](nd.md#set_geometry_name) :black_small_square: [set_handle_positions](nd.md#set_handle_positions) :black_small_square: [set_handle_type](nd.md#set_handle_type) :black_small_square: [set_id](nd.md#set_id) :black_small_square: [set_instance_transform](nd.md#set_instance_transform) :black_small_square: [set_material](nd.md#set_material) :black_small_square: [set_material_index](nd.md#set_material_index) :black_small_square: [set_point_radius](nd.md#set_point_radius) :black_small_square: [set_position](nd.md#set_position) :black_small_square: [set_selection](nd.md#set_selection) :black_small_square: [set_shade_smooth](nd.md#set_shade_smooth) :black_small_square: [set_spline_cyclic](nd.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](nd.md#set_spline_resolution) :black_small_square: [set_spline_type](nd.md#set_spline_type) :black_small_square: [shortest_edge_paths](nd.md#shortest_edge_paths) :black_small_square: [simulation_input](nd.md#simulation_input) :black_small_square: [simulation_output](nd.md#simulation_output) :black_small_square: [slice_string](nd.md#slice_string) :black_small_square: [sort_elements](nd.md#sort_elements) :black_small_square: [spiral](nd.md#spiral) :black_small_square: [split_edges](nd.md#split_edges) :black_small_square: [split_to_instances](nd.md#split_to_instances) :black_small_square: [star](nd.md#star) :black_small_square: [store_named_attribute](nd.md#store_named_attribute) :black_small_square: [store_named_grid](nd.md#store_named_grid) :black_small_square: [string](nd.md#string) :black_small_square: [string_length](nd.md#string_length) :black_small_square: [string_to_curves](nd.md#string_to_curves) :black_small_square: [subdivide_curve](nd.md#subdivide_curve) :black_small_square: [subdivide_mesh](nd.md#subdivide_mesh) :black_small_square: [subdivision_surface](nd.md#subdivision_surface) :black_small_square: [switch](nd.md#switch)
- **T** : [transform_direction](nd.md#transform_direction) :black_small_square: [transform_geometry](nd.md#transform_geometry) :black_small_square: [transform_gizmo](nd.md#transform_gizmo) :black_small_square: [transform_point](nd.md#transform_point) :black_small_square: [translate_instances](nd.md#translate_instances) :black_small_square: [transpose_matrix](nd.md#transpose_matrix) :black_small_square: [triangulate](nd.md#triangulate) :black_small_square: [trim_curve](nd.md#trim_curve)
- **U** : [uv_sphere](nd.md#uv_sphere) :black_small_square: [uv_unwrap](nd.md#uv_unwrap)
- **V** : [value_to_string](nd.md#value_to_string) :black_small_square: [vector](nd.md#vector) :black_small_square: [vector_curves](nd.md#vector_curves) :black_small_square: [vector_math](nd.md#vector_math) :black_small_square: [vector_rotate](nd.md#vector_rotate) :black_small_square: [vertex_of_corner](nd.md#vertex_of_corner) :black_small_square: [viewer](nd.md#viewer) :black_small_square: [volume_cube](nd.md#volume_cube) :black_small_square: [volume_to_mesh](nd.md#volume_to_mesh) :black_small_square: [voronoi_texture](nd.md#voronoi_texture)
- **W** : [warning](nd.md#warning) :black_small_square: [wave_texture](nd.md#wave_texture) :black_small_square: [white_noise_texture](nd.md#white_noise_texture)

## Methods



----------
### accumulate_field()

> classmethod

``` python
accumulate_field(value=None, group_id=None, data_type='FLOAT', domain='POINT')
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group Index)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### active_element()

> classmethod

``` python
active_element(domain='POINT')
```

> Node [Active Element](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/active_element.html)

#### Arguments:
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### align_euler_to_vector()

> classmethod

``` python
align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```

> Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/deprecated/align_euler_to_vector.html)

#### Arguments:
- **rotation** (_Vector_ = None) : socket 'Rotation' (Rotation)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **axis** (_str_ = X) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### align_rotation_to_vector()

> classmethod

``` python
align_rotation_to_vector(rotation=None, factor=None, vector=None, axis='Z', pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### arc()

> classmethod

``` python
arc(resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, mode='RADIUS')
```

> Node [Arc](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **start_angle** (_Float_ = None) : socket 'Start Angle' (Start Angle)
- **sweep_angle** (_Float_ = None) : socket 'Sweep Angle' (Sweep Angle)
- **connect_center** (_Boolean_ = None) : socket 'Connect Center' (Connect Center)
- **invert_arc** (_Boolean_ = None) : socket 'Invert Arc' (Invert Arc)
- **mode** (_str_ = RADIUS) : Node.mode in ('POINTS', 'RADIUS')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### attribute_statistic()

> classmethod

``` python
attribute_statistic(geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT')
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **attribute** (_Float_ = None) : socket 'Attribute' (Attribute)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'FLOAT_VECTOR')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### axes_to_rotation()

> classmethod

``` python
axes_to_rotation(primary_axis_1=None, secondary_axis_1=None, primary_axis='Z', secondary_axis='X')
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Arguments:
- **primary_axis_1** (_Vector_ = None) : socket 'Primary Axis' (Primary Axis)
- **secondary_axis_1** (_Vector_ = None) : socket 'Secondary Axis' (Secondary Axis)
- **primary_axis** (_str_ = Z) : Node.primary_axis in ('X', 'Y', 'Z')
- **secondary_axis** (_str_ = X) : Node.secondary_axis in ('X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### axis_angle_to_rotation()

> classmethod

``` python
axis_angle_to_rotation(axis=None, angle=None)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

#### Arguments:
- **axis** (_Vector_ = None) : socket 'Axis' (Axis)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### bake()

> classmethod

``` python
bake(geometry=None, active_index=0, active_item=None, bake_items=None)
```

> Node [Bake](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bake.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Item_0)
- **active_index** (_int_ = 0) : Node.active_index
- **active_item** (_NodeGeometryBakeItem_ = None) : Node.active_item
- **bake_items** (_bpy_prop_collection_ = None) : Node.bake_items



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### bezier_segment()

> classmethod

``` python
bezier_segment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

> Node ERROR: Node 'Bézier Segment' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **start_handle** (_Vector_ = None) : socket 'Start Handle' (Start Handle)
- **end_handle** (_Vector_ = None) : socket 'End Handle' (End Handle)
- **end** (_Vector_ = None) : socket 'End' (End)
- **mode** (_str_ = POSITION) : Node.mode in ('POSITION', 'OFFSET')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### blackbody()

> classmethod

``` python
blackbody(temperature=None)
```

> Node [Blackbody](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/blackbody.html)

#### Arguments:
- **temperature** (_Float_ = None) : socket 'Temperature' (Temperature)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### blur_attribute()

> classmethod

``` python
blur_attribute(value=None, iterations=None, weight=None, data_type='FLOAT')
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **iterations** (_Integer_ = None) : socket 'Iterations' (Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### boolean()

> classmethod

``` python
boolean(boolean=False)
```

> Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html)

#### Arguments:
- **boolean** (_bool_ = False) : Node.boolean



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### boolean_math()

> classmethod

``` python
boolean_math(boolean=None, boolean_1=None, operation='AND')
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (Boolean)
- **boolean_1** (_Boolean_ = None) : socket 'Boolean' (Boolean_001)
- **operation** (_str_ = AND) : Node.operation in ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### bounding_box()

> classmethod

``` python
bounding_box(geometry=None)
```

> Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bounding_box.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### brick_texture()

> classmethod

``` python
brick_texture(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None)
```

> Node [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **color1** (_Color_ = None) : socket 'Color1' (Color1)
- **color2** (_Color_ = None) : socket 'Color2' (Color2)
- **mortar** (_Color_ = None) : socket 'Mortar' (Mortar)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **mortar_size** (_Float_ = None) : socket 'Mortar Size' (Mortar Size)
- **mortar_smooth** (_Float_ = None) : socket 'Mortar Smooth' (Mortar Smooth)
- **bias** (_Float_ = None) : socket 'Bias' (Bias)
- **brick_width** (_Float_ = None) : socket 'Brick Width' (Brick Width)
- **row_height** (_Float_ = None) : socket 'Row Height' (Row Height)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **offset** (_float_ = 0.5) : Node.offset
- **offset_frequency** (_int_ = 2) : Node.offset_frequency
- **squash** (_float_ = 1.0) : Node.squash
- **squash_frequency** (_int_ = 2) : Node.squash_frequency
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### capture_attribute()

> classmethod

``` python
capture_attribute(geometry=None, active_index=0, active_item=None, capture_items=None, domain='POINT')
```

> Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **active_index** (_int_ = 0) : Node.active_index
- **active_item** (_NoneType_ = None) : Node.active_item
- **capture_items** (_bpy_prop_collection_ = None) : Node.capture_items
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### checker_texture()

> classmethod

``` python
checker_texture(vector=None, color1=None, color2=None, scale=None, color_mapping=None, texture_mapping=None)
```

> Node [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **color1** (_Color_ = None) : socket 'Color1' (Color1)
- **color2** (_Color_ = None) : socket 'Color2' (Color2)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### clamp()

> classmethod

``` python
clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **min** (_Float_ = None) : socket 'Min' (Min)
- **max** (_Float_ = None) : socket 'Max' (Max)
- **clamp_type** (_str_ = MINMAX) : Node.clamp_type in ('MINMAX', 'RANGE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### collection_info()

> classmethod

``` python
collection_info(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

> Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html)

#### Arguments:
- **collection** (_Collection_ = None) : socket 'Collection' (Collection)
- **separate_children** (_Boolean_ = None) : socket 'Separate Children' (Separate Children)
- **reset_children** (_Boolean_ = None) : socket 'Reset Children' (Reset Children)
- **transform_space** (_str_ = ORIGINAL) : Node.transform_space in ('ORIGINAL', 'RELATIVE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### color()

> classmethod

``` python
color(value=None)
```

> Node [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html)

#### Arguments:
- **value** (_bpy_prop_array_ = None) : Node.value



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### color_ramp()

> classmethod

``` python
color_ramp(fac=None, color_ramp=None)
```

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (Fac)
- **color_ramp** (_ColorRamp_ = None) : Node.color_ramp



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### combine_color()

> classmethod

``` python
combine_color(red=None, green=None, blue=None, alpha=None, mode='RGB')
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **red** (_Float_ = None) : socket 'Red' (Red)
- **green** (_Float_ = None) : socket 'Green' (Green)
- **blue** (_Float_ = None) : socket 'Blue' (Blue)
- **alpha** (_Float_ = None) : socket 'Alpha' (Alpha)
- **mode** (_str_ = RGB) : Node.mode in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### combine_matrix()

> classmethod

``` python
combine_matrix(column_1_row_1=None, column_1_row_2=None, column_1_row_3=None, column_1_row_4=None, column_2_row_1=None, column_2_row_2=None, column_2_row_3=None, column_2_row_4=None, column_3_row_1=None, column_3_row_2=None, column_3_row_3=None, column_3_row_4=None, column_4_row_1=None, column_4_row_2=None, column_4_row_3=None, column_4_row_4=None)
```

> Node [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html)

#### Arguments:
- **column_1_row_1** (_Float_ = None) : socket 'Column 1 Row 1' (Column 1 Row 1)
- **column_1_row_2** (_Float_ = None) : socket 'Column 1 Row 2' (Column 1 Row 2)
- **column_1_row_3** (_Float_ = None) : socket 'Column 1 Row 3' (Column 1 Row 3)
- **column_1_row_4** (_Float_ = None) : socket 'Column 1 Row 4' (Column 1 Row 4)
- **column_2_row_1** (_Float_ = None) : socket 'Column 2 Row 1' (Column 2 Row 1)
- **column_2_row_2** (_Float_ = None) : socket 'Column 2 Row 2' (Column 2 Row 2)
- **column_2_row_3** (_Float_ = None) : socket 'Column 2 Row 3' (Column 2 Row 3)
- **column_2_row_4** (_Float_ = None) : socket 'Column 2 Row 4' (Column 2 Row 4)
- **column_3_row_1** (_Float_ = None) : socket 'Column 3 Row 1' (Column 3 Row 1)
- **column_3_row_2** (_Float_ = None) : socket 'Column 3 Row 2' (Column 3 Row 2)
- **column_3_row_3** (_Float_ = None) : socket 'Column 3 Row 3' (Column 3 Row 3)
- **column_3_row_4** (_Float_ = None) : socket 'Column 3 Row 4' (Column 3 Row 4)
- **column_4_row_1** (_Float_ = None) : socket 'Column 4 Row 1' (Column 4 Row 1)
- **column_4_row_2** (_Float_ = None) : socket 'Column 4 Row 2' (Column 4 Row 2)
- **column_4_row_3** (_Float_ = None) : socket 'Column 4 Row 3' (Column 4 Row 3)
- **column_4_row_4** (_Float_ = None) : socket 'Column 4 Row 4' (Column 4 Row 4)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### combine_transform()

> classmethod

``` python
combine_transform(translation=None, rotation=None, scale=None)
```

> Node [Combine Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_transform.html)

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### combine_xyz()

> classmethod

``` python
combine_xyz(x=None, y=None, z=None)
```

> Node [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html)

#### Arguments:
- **x** (_Float_ = None) : socket 'X' (X)
- **y** (_Float_ = None) : socket 'Y' (Y)
- **z** (_Float_ = None) : socket 'Z' (Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### compare()

> classmethod

``` python
compare(a=None, b=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **a** (_Float_ = None) : socket 'A' (A)
- **b** (_Float_ = None) : socket 'B' (B)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')
- **mode** (_str_ = ELEMENT) : Node.mode in ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION')
- **operation** (_str_ = GREATER_THAN) : Node.operation in ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### cone()

> classmethod

``` python
cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```

> Node [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cone.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (Vertices)
- **side_segments** (_Integer_ = None) : socket 'Side Segments' (Side Segments)
- **fill_segments** (_Integer_ = None) : socket 'Fill Segments' (Fill Segments)
- **radius_top** (_Float_ = None) : socket 'Radius Top' (Radius Top)
- **radius_bottom** (_Float_ = None) : socket 'Radius Bottom' (Radius Bottom)
- **depth** (_Float_ = None) : socket 'Depth' (Depth)
- **fill_type** (_str_ = NGON) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### convex_hull()

> classmethod

``` python
convex_hull(geometry=None)
```

> Node [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### corners_of_edge()

> classmethod

``` python
corners_of_edge(edge_index=None, weights=None, sort_index=None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### corners_of_face()

> classmethod

``` python
corners_of_face(face_index=None, weights=None, sort_index=None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### corners_of_vertex()

> classmethod

``` python
corners_of_vertex(vertex_index=None, weights=None, sort_index=None)
```

> Node [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### cube()

> classmethod

``` python
cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```

> Node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html)

#### Arguments:
- **size** (_Vector_ = None) : socket 'Size' (Size)
- **vertices_x** (_Integer_ = None) : socket 'Vertices X' (Vertices X)
- **vertices_y** (_Integer_ = None) : socket 'Vertices Y' (Vertices Y)
- **vertices_z** (_Integer_ = None) : socket 'Vertices Z' (Vertices Z)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_circle()

> classmethod

``` python
curve_circle(resolution=None, radius=None, mode='RADIUS')
```

> Node [Curve Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html)

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **mode** (_str_ = RADIUS) : Node.mode in ('POINTS', 'RADIUS')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_handle_positions()

> classmethod

``` python
curve_handle_positions(relative=None)
```

> Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_handle_positions.html)

#### Arguments:
- **relative** (_Boolean_ = None) : socket 'Relative' (Relative)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_length()

> classmethod

``` python
curve_length(curve=None)
```

> Node [Curve Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_length.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_line()

> classmethod

``` python
curve_line(start=None, end=None, mode='POINTS')
```

> Node [Curve Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html)

#### Arguments:
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **end** (_Vector_ = None) : socket 'End' (End)
- **mode** (_str_ = POINTS) : Node.mode in ('POINTS', 'DIRECTION')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_of_point()

> classmethod

``` python
curve_of_point(point_index=None)
```

> Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (Point Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curves_to_grease_pencil()

> classmethod

``` python
curves_to_grease_pencil(curves=None, instances_as_layers=None)
```

> Node [Curves to Grease Pencil](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curves_to_grease_pencil.html)

#### Arguments:
- **curves** (_Geometry_ = None) : socket 'Curves' (Curves)
- **instances_as_layers** (_Boolean_ = None) : socket 'Instances as Layers' (Instances as Layers)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_to_mesh()

> classmethod

``` python
curve_to_mesh(curve=None, profile_curve=None, fill_caps=None)
```

> Node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **profile_curve** (_Geometry_ = None) : socket 'Profile Curve' (Profile Curve)
- **fill_caps** (_Boolean_ = None) : socket 'Fill Caps' (Fill Caps)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### curve_to_points()

> classmethod

``` python
curve_to_points(curve=None, count=None, mode='COUNT')
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **mode** (_str_ = COUNT) : Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### cylinder()

> classmethod

``` python
cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```

> Node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cylinder.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (Vertices)
- **side_segments** (_Integer_ = None) : socket 'Side Segments' (Side Segments)
- **fill_segments** (_Integer_ = None) : socket 'Fill Segments' (Fill Segments)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **depth** (_Float_ = None) : socket 'Depth' (Depth)
- **fill_type** (_str_ = NGON) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### deform_curves_on_surface()

> classmethod

``` python
deform_curves_on_surface(curves=None)
```

> Node [Deform Curves on Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html)

#### Arguments:
- **curves** (_Geometry_ = None) : socket 'Curves' (Curves)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### delete_geometry()

> classmethod

``` python
delete_geometry(geometry=None, selection=None, domain='POINT', mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### dial_gizmo()

> classmethod

``` python
dial_gizmo(*value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY')
```

> Node ERROR: Node 'Dial Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **up** (_Vector_ = None) : socket 'Up' (Up)
- **screen_space** (_Boolean_ = None) : socket 'Screen Space' (Screen Space)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### distribute_points_in_grid()

> classmethod

``` python
distribute_points_in_grid(grid=None, density=None, seed=None, mode='DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (Grid)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **mode** (_str_ = DENSITY_RANDOM) : Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### distribute_points_in_volume()

> classmethod

``` python
distribute_points_in_volume(volume=None, density=None, seed=None, mode='DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Arguments:
- **volume** (_Geometry_ = None) : socket 'Volume' (Volume)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **mode** (_str_ = DENSITY_RANDOM) : Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### distribute_points_on_faces()

> classmethod

``` python
distribute_points_on_faces(mesh=None, selection=None, density=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **distribute_method** (_str_ = RANDOM) : Node.distribute_method in ('RANDOM', 'POISSON')
- **use_legacy_normal** (_bool_ = False) : Node.use_legacy_normal



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### domain_size()

> classmethod

``` python
domain_size(geometry=None, component='MESH')
```

> Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **component** (_str_ = MESH) : Node.component in ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### dual_mesh()

> classmethod

``` python
dual_mesh(mesh=None, keep_boundaries=None)
```

> Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/dual_mesh.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **keep_boundaries** (_Boolean_ = None) : socket 'Keep Boundaries' (Keep Boundaries)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### duplicate_elements()

> classmethod

``` python
duplicate_elements(geometry=None, selection=None, amount=None, domain='POINT')
```

> Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **amount** (_Integer_ = None) : socket 'Amount' (Amount)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### edge_paths_to_curves()

> classmethod

``` python
edge_paths_to_curves(mesh=None, start_vertices=None, next_vertex_index=None)
```

> Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### edge_paths_to_selection()

> classmethod

``` python
edge_paths_to_selection(start_vertices=None, next_vertex_index=None)
```

> Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html)

#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### edges_of_corner()

> classmethod

``` python
edges_of_corner(corner_index=None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (Corner Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### edges_of_vertex()

> classmethod

``` python
edges_of_vertex(vertex_index=None, weights=None, sort_index=None)
```

> Node [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### edges_to_face_groups()

> classmethod

``` python
edges_to_face_groups(boundary_edges=None)
```

> Node [Edges to Face Groups](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edges_to_face_groups.html)

#### Arguments:
- **boundary_edges** (_Boolean_ = None) : socket 'Boundary Edges' (Boundary Edges)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### endpoint_selection()

> classmethod

``` python
endpoint_selection(start_size=None, end_size=None)
```

> Node [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/endpoint_selection.html)

#### Arguments:
- **start_size** (_Integer_ = None) : socket 'Start Size' (Start Size)
- **end_size** (_Integer_ = None) : socket 'End Size' (End Size)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### euler_to_rotation()

> classmethod

``` python
euler_to_rotation(euler=None)
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

#### Arguments:
- **euler** (_Vector_ = None) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(index=None, value=None, data_type='FLOAT', domain='POINT')
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value=None, data_type='FLOAT', domain='POINT')
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### extrude_mesh()

> classmethod

``` python
extrude_mesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (Individual)
- **mode** (_str_ = FACES) : Node.mode in ('VERTICES', 'EDGES', 'FACES')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### face_group_boundaries()

> classmethod

``` python
face_group_boundaries(face_group_id=None)
```

> Node [Face Group Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_group_boundaries.html)

#### Arguments:
- **face_group_id** (_Integer_ = None) : socket 'Face Group ID' (Face Set)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### face_of_corner()

> classmethod

``` python
face_of_corner(corner_index=None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (Corner Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### fill_curve()

> classmethod

``` python
fill_curve(curve=None, group_id=None, mode='TRIANGLES')
```

> Node [Fill Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **mode** (_str_ = TRIANGLES) : Node.mode in ('TRIANGLES', 'NGONS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### fillet_curve()

> classmethod

``` python
fillet_curve(curve=None, radius=None, limit_radius=None, mode='BEZIER')
```

> Node [Fillet Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **limit_radius** (_Boolean_ = None) : socket 'Limit Radius' (Limit Radius)
- **mode** (_str_ = BEZIER) : Node.mode in ('BEZIER', 'POLY')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### flip_faces()

> classmethod

``` python
flip_faces(mesh=None, selection=None)
```

> Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### float_curve()

> classmethod

``` python
float_curve(factor=None, value=None, mapping=None)
```

> Node ERROR: Node 'Float Curve' not found

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **mapping** (_CurveMapping_ = None) : Node.mapping



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### float_to_integer()

> classmethod

``` python
float_to_integer(float=None, rounding_mode='ROUND')
```

> Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)

#### Arguments:
- **float** (_Float_ = None) : socket 'Float' (Float)
- **rounding_mode** (_str_ = ROUND) : Node.rounding_mode in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### frame()

> classmethod

``` python
frame(label_size=20, shrink=True, text=None)
```

> Node [Frame](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/frame.html)

#### Arguments:
- **label_size** (_int_ = 20) : Node.label_size
- **shrink** (_bool_ = True) : Node.shrink
- **text** (_NoneType_ = None) : Node.text

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### gabor_texture()

> classmethod

``` python
gabor_texture(vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, gabor_type='2D')
```

> Node [Gabor Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gabor.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **frequency** (_Float_ = None) : socket 'Frequency' (Frequency)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (Anisotropy)
- **orientation** (_Float_ = None) : socket 'Orientation' (Orientation 2D)
- **gabor_type** (_str_ = 2D) : Node.gabor_type in ('2D', '3D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### geometry_proximity()

> classmethod

``` python
geometry_proximity(geometry=None, group_id=None, sample_position=None, sample_group_id=None, target_element='FACES')
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Target)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (Sample Group ID)
- **target_element** (_str_ = FACES) : Node.target_element in ('POINTS', 'EDGES', 'FACES')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### geometry_to_instance()

> classmethod

``` python
geometry_to_instance(geometry=None)
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### get_named_grid()

> classmethod

``` python
get_named_grid(volume=None, name=None, remove=None, data_type='FLOAT')
```

> Node ERROR: Node 'Get Named Grid' not found

#### Arguments:
- **volume** (_Geometry_ = None) : socket 'Volume' (Volume)
- **name** (_String_ = None) : socket 'Name' (Name)
- **remove** (_Boolean_ = None) : socket 'Remove' (Remove)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'VECTOR')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### gradient_texture()

> classmethod

``` python
gradient_texture(vector=None, color_mapping=None, gradient_type='LINEAR', texture_mapping=None)
```

> Node [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **gradient_type** (_str_ = LINEAR) : Node.gradient_type in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### grease_pencil_to_curves()

> classmethod

``` python
grease_pencil_to_curves(grease_pencil=None, layers_as_instances=None)
```

> Node [Grease Pencil to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/grease_pencil_to_curves.html)

#### Arguments:
- **grease_pencil** (_Geometry_ = None) : socket 'Grease Pencil' (Grease Pencil)
- **layers_as_instances** (_Boolean_ = None) : socket 'Layers as Instances' (Layers as Instances)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### grid()

> classmethod

``` python
grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None)
```

> Node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/grid.html)

#### Arguments:
- **size_x** (_Float_ = None) : socket 'Size X' (Size X)
- **size_y** (_Float_ = None) : socket 'Size Y' (Size Y)
- **vertices_x** (_Integer_ = None) : socket 'Vertices X' (Vertices X)
- **vertices_y** (_Integer_ = None) : socket 'Vertices Y' (Vertices Y)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### grid_to_mesh()

> classmethod

``` python
grid_to_mesh(grid=None, threshold=None, adaptivity=None)
```

> Node ERROR: Node 'Grid to Mesh' not found

#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (Grid)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### group()

> classmethod

``` python
group(node_tree=None)
```

> Node ERROR: Node 'Group' not found

#### Arguments:
- **node_tree** (_NoneType_ = None) : Node.node_tree

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### group_output()

> classmethod

``` python
group_output(is_active_output=True)
```

> Node ERROR: Node 'Group Output' not found

#### Arguments:
- **is_active_output** (_bool_ = True) : Node.is_active_output

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### handle_type_selection()

> classmethod

``` python
handle_type_selection(handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

> Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html)

#### Arguments:
- **handle_type** (_str_ = AUTO) : Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** (_set_ = {'LEFT', 'RIGHT'}) : Node.mode



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### hash_value()

> classmethod

``` python
hash_value(value=None, seed=None, data_type='INT')
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (Value)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **data_type** (_str_ = INT) : Node.data_type in ('FLOAT', 'INT', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### ico_sphere()

> classmethod

``` python
ico_sphere(radius=None, subdivisions=None)
```

> Node ERROR: Node 'Ico Sphere' not found

#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **subdivisions** (_Integer_ = None) : socket 'Subdivisions' (Subdivisions)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### image()

> classmethod

``` python
image(image=None)
```

> Node [Image](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/input/image.html)

#### Arguments:
- **image** (_NoneType_ = None) : Node.image



#### Returns:
- **Image** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### image_info()

> classmethod

``` python
image_info(image=None, frame=None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Arguments:
- **image** (_Image_ = None) : socket 'Image' (Image)
- **frame** (_Integer_ = None) : socket 'Frame' (Frame)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### image_texture()

> classmethod

``` python
image_texture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)

#### Arguments:
- **image** (_Image_ = None) : socket 'Image' (Image)
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **frame** (_Integer_ = None) : socket 'Frame' (Frame)
- **extension** (_str_ = REPEAT) : Node.extension in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
- **interpolation** (_str_ = Linear) : Node.interpolation in ('Linear', 'Closest', 'Cubic')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### import_obj()

> classmethod

``` python
import_obj(path=None)
```

> Node ERROR: Node 'Import OBJ' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (Path)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### import_ply()

> classmethod

``` python
import_ply(path=None)
```

> Node ERROR: Node 'Import PLY' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (Path)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### import_stl()

> classmethod

``` python
import_stl(path=None)
```

> Node ERROR: Node 'Import STL' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (Path)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### index_of_nearest()

> classmethod

``` python
index_of_nearest(position=None, group_id=None)
```

> Node ERROR: Node 'Index of Nearest' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### index_switch()

> classmethod

``` python
index_switch(index=None, _0=None, _1=None, data_type='GEOMETRY', index_switch_items=None)
```

> Node [Index Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/index_switch.html)

#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **_0** (_Geometry_ = None) : socket '0' (Item_0)
- **_1** (_Geometry_ = None) : socket '1' (Item_1)
- **data_type** (_str_ = GEOMETRY) : Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')
- **index_switch_items** (_bpy_prop_collection_ = None) : Node.index_switch_items



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### instance_on_points()

> classmethod

``` python
instance_on_points(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **instance** (_Geometry_ = None) : socket 'Instance' (Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### instances_to_points()

> classmethod

``` python
instances_to_points(instances=None, selection=None, position=None, radius=None)
```

> Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)

#### Arguments:
- **instances** (_Geometry_ = None) : socket 'Instances' (Instances)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### integer()

> classmethod

``` python
integer(integer=0)
```

> Node [Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/integer.html)

#### Arguments:
- **integer** (_int_ = 0) : Node.integer



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### integer_math()

> classmethod

``` python
integer_math(value=None, value_1=None, operation='ADD')
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (Value)
- **value_1** (_Integer_ = None) : socket 'Value' (Value_001)
- **operation** (_str_ = ADD) : Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### interpolate_curves()

> classmethod

``` python
interpolate_curves(guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Arguments:
- **guide_curves** (_Geometry_ = None) : socket 'Guide Curves' (Guide Curves)
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (Guide Group ID)
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **point_up** (_Vector_ = None) : socket 'Point Up' (Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (Max Neighbors)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### invert_matrix()

> classmethod

``` python
invert_matrix(matrix=None)
```

> Node [Invert Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/invert_matrix.html)

#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (Matrix)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### invert_rotation()

> classmethod

``` python
invert_rotation(rotation=None)
```

> Node [Invert Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/invert_rotation.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### is_face_planar()

> classmethod

``` python
is_face_planar(threshold=None)
```

> Node [Is Face Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### join_geometry()

> classmethod

``` python
join_geometry(*geometry)
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### join_strings()

> classmethod

``` python
join_strings(delimiter=None, strings=None)
```

> Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html)

#### Arguments:
- **delimiter** (_String_ = None) : socket 'Delimiter' (Delimiter)
- **strings** (_String_ = None) : socket 'Strings' (Strings)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### linear_gizmo()

> classmethod

``` python
linear_gizmo(*value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW')
```

> Node ERROR: Node 'Linear Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **direction** (_Vector_ = None) : socket 'Direction' (Direction)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
- **draw_style** (_str_ = ARROW) : Node.draw_style in ('ARROW', 'CROSS', 'BOX')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### magic_texture()

> classmethod

``` python
magic_texture(vector=None, scale=None, distortion=None, color_mapping=None, texture_mapping=None, turbulence_depth=2)
```

> Node [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping
- **turbulence_depth** (_int_ = 2) : Node.turbulence_depth



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### map_range()

> classmethod

``` python
map_range(value=None, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR')
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = True) : Node.clamp
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'FLOAT_VECTOR')
- **interpolation_type** (_str_ = LINEAR) : Node.interpolation_type in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### material()

> classmethod

``` python
material(material=None)
```

> Node [Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/material.html)

#### Arguments:
- **material** (_NoneType_ = None) : Node.material



#### Returns:
- **Material** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### material_selection()

> classmethod

``` python
material_selection(material=None)
```

> Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)

#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (Material)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### math()

> classmethod

``` python
math(value=None, value_1=None, operation='ADD', use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **value_1** (_Float_ = None) : socket 'Value' (Value_001)
- **operation** (_str_ = ADD) : Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
- **use_clamp** (_bool_ = False) : Node.use_clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### matrix_determinant()

> classmethod

``` python
matrix_determinant(matrix=None)
```

> Node [Matrix Determinant](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/matrix_determinant.html)

#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (Matrix)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### menu_switch()

> classmethod

``` python
menu_switch(menu=None, a=None, b=None, active_index=1, data_type='GEOMETRY')
```

> Node [Menu Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/menu_switch.html)

#### Arguments:
- **menu** (_Menu_ = None) : socket 'Menu' (Menu)
- **a** (_Geometry_ = None) : socket 'A' (Item_0)
- **b** (_Geometry_ = None) : socket 'B' (Item_1)
- **active_index** (_int_ = 1) : Node.active_index
- **data_type** (_str_ = GEOMETRY) : Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### merge_by_distance()

> classmethod

``` python
merge_by_distance(geometry=None, selection=None, distance=None, mode='ALL')
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **distance** (_Float_ = None) : socket 'Distance' (Distance)
- **mode** (_str_ = ALL) : Node.mode in ('ALL', 'CONNECTED')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### merge_layers()

> classmethod

``` python
merge_layers(grease_pencil=None, mode='MERGE_BY_NAME')
```

> Node [Merge Layers](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/merge_layers.html)

#### Arguments:
- **grease_pencil** (_Geometry_ = None) : socket 'Grease Pencil' (Grease Pencil)
- **mode** (_str_ = MERGE_BY_NAME) : Node.mode in ('MERGE_BY_NAME', 'MERGE_BY_ID')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_boolean()

> classmethod

``` python
mesh_boolean(mesh_1=None, mesh_2=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', solver='FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **mesh_1** (_Geometry_ = None) : socket 'Mesh 1' (Mesh 1)
- **mesh_2** (_Geometry_ = None) : socket 'Mesh 2' (Mesh 2)
- **self_intersection** (_Boolean_ = None) : socket 'Self Intersection' (Self Intersection)
- **hole_tolerant** (_Boolean_ = None) : socket 'Hole Tolerant' (Hole Tolerant)
- **operation** (_str_ = DIFFERENCE) : Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')
- **solver** (_str_ = FLOAT) : Node.solver in ('EXACT', 'FLOAT')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_circle()

> classmethod

``` python
mesh_circle(vertices=None, radius=None, fill_type='NONE')
```

> Node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (Vertices)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **fill_type** (_str_ = NONE) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_line()

> classmethod

``` python
mesh_line(count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

> Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **start_location** (_Vector_ = None) : socket 'Start Location' (Start Location)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **count_mode** (_str_ = TOTAL) : Node.count_mode in ('TOTAL', 'RESOLUTION')
- **mode** (_str_ = OFFSET) : Node.mode in ('OFFSET', 'END_POINTS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_to_curve()

> classmethod

``` python
mesh_to_curve(mesh=None, selection=None)
```

> Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_to_density_grid()

> classmethod

``` python
mesh_to_density_grid(mesh=None, density=None, voxel_size=None, gradient_width=None)
```

> Node ERROR: Node 'Mesh to Density Grid' not found

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (Voxel Size)
- **gradient_width** (_Float_ = None) : socket 'Gradient Width' (Gradient Width)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_to_points()

> classmethod

``` python
mesh_to_points(mesh=None, selection=None, position=None, radius=None, mode='VERTICES')
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **mode** (_str_ = VERTICES) : Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_to_sdf_grid()

> classmethod

``` python
mesh_to_sdf_grid(mesh=None, voxel_size=None, band_width=None)
```

> Node ERROR: Node 'Mesh to SDF Grid' not found

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (Voxel Size)
- **band_width** (_Integer_ = None) : socket 'Band Width' (Band Width)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mesh_to_volume()

> classmethod

``` python
mesh_to_volume(mesh=None, density=None, voxel_amount=None, interior_band_width=None, resolution_mode='VOXEL_AMOUNT')
```

> Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **interior_band_width** (_Float_ = None) : socket 'Interior Band Width' (Interior Band Width)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### mix()

> classmethod

``` python
mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM')
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **a** (_Float_ = None) : socket 'A' (A_Float)
- **b** (_Float_ = None) : socket 'B' (B_Float)
- **blend_type** (_str_ = MIX) : Node.blend_type in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- **clamp_factor** (_bool_ = True) : Node.clamp_factor
- **clamp_result** (_bool_ = False) : Node.clamp_result
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'VECTOR', 'RGBA', 'ROTATION')
- **factor_mode** (_str_ = UNIFORM) : Node.factor_mode in ('UNIFORM', 'NON_UNIFORM')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### multiply_matrices()

> classmethod

``` python
multiply_matrices(matrix=None, matrix_1=None)
```

> Node [Multiply Matrices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/multiply_matrices.html)

#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (Matrix)
- **matrix_1** (_Matrix_ = None) : socket 'Matrix' (Matrix_001)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### named_attribute()

> classmethod

``` python
named_attribute(name=None, data_type='FLOAT')
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Arguments:
- **name** (_String_ = None) : socket 'Name' (Name)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### named_layer_selection()

> classmethod

``` python
named_layer_selection(name=None)
```

> Node ERROR: Node 'Named Layer Selection' not found

#### Arguments:
- **name** (_String_ = None) : socket 'Name' (Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### noise_texture()

> classmethod

``` python
noise_texture(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, color_mapping=None, noise_dimensions='3D', noise_type='FBM', normalize=True, texture_mapping=None)
```

> Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (Lacunarity)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **noise_dimensions** (_str_ = 3D) : Node.noise_dimensions in ('1D', '2D', '3D', '4D')
- **noise_type** (_str_ = FBM) : Node.noise_type in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
- **normalize** (_bool_ = True) : Node.normalize
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### object_info()

> classmethod

``` python
object_info(object=None, as_instance=None, transform_space='ORIGINAL')
```

> Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html)

#### Arguments:
- **object** (_Object_ = None) : socket 'Object' (Object)
- **as_instance** (_Boolean_ = None) : socket 'As Instance' (As Instance)
- **transform_space** (_str_ = ORIGINAL) : Node.transform_space in ('ORIGINAL', 'RELATIVE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### offset_corner_in_face()

> classmethod

``` python
offset_corner_in_face(corner_index=None, offset=None)
```

> Node [Offset Corner in Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/offset_corner_in_face.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (Corner Index)
- **offset** (_Integer_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### offset_point_in_curve()

> classmethod

``` python
offset_point_in_curve(point_index=None, offset=None)
```

> Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/offset_point_in_curve.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (Point Index)
- **offset** (_Integer_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### pack_uv_islands()

> classmethod

``` python
pack_uv_islands(uv=None, selection=None, margin=None, rotate=None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Arguments:
- **uv** (_Vector_ = None) : socket 'UV' (UV)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **margin** (_Float_ = None) : socket 'Margin' (Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (Rotate)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points()

> classmethod

``` python
points(count=None, position=None, radius=None)
```

> Node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points_of_curve()

> classmethod

``` python
points_of_curve(curve_index=None, weights=None, sort_index=None)
```

> Node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points_to_curves()

> classmethod

``` python
points_to_curves(points=None, curve_group_id=None, weight=None)
```

> Node [Points to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_curves.html)

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points_to_sdf_grid()

> classmethod

``` python
points_to_sdf_grid(points=None, radius=None, voxel_size=None)
```

> Node ERROR: Node 'Points to SDF Grid' not found

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (Voxel Size)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points_to_vertices()

> classmethod

``` python
points_to_vertices(points=None, selection=None)
```

> Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### points_to_volume()

> classmethod

``` python
points_to_volume(points=None, density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### project_point()

> classmethod

``` python
project_point(vector=None, transform=None)
```

> Node [Project Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/project_point.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **transform** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### quadratic_bezier()

> classmethod

``` python
quadratic_bezier(resolution=None, start=None, middle=None, end=None)
```

> Node ERROR: Node 'Quadratic Bézier' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **start** (_Vector_ = None) : socket 'Start' (Start)
- **middle** (_Vector_ = None) : socket 'Middle' (Middle)
- **end** (_Vector_ = None) : socket 'End' (End)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### quadrilateral()

> classmethod

``` python
quadrilateral(width=None, height=None, mode='RECTANGLE')
```

> Node [Quadrilateral](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html)

#### Arguments:
- **width** (_Float_ = None) : socket 'Width' (Width)
- **height** (_Float_ = None) : socket 'Height' (Height)
- **mode** (_str_ = RECTANGLE) : Node.mode in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### quaternion_to_rotation()

> classmethod

``` python
quaternion_to_rotation(w=None, x=None, y=None, z=None)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

#### Arguments:
- **w** (_Float_ = None) : socket 'W' (W)
- **x** (_Float_ = None) : socket 'X' (X)
- **y** (_Float_ = None) : socket 'Y' (Y)
- **z** (_Float_ = None) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### random_value()

> classmethod

``` python
random_value(min=None, max=None, id=None, seed=None, data_type='FLOAT')
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (Min_001)
- **max** (_Float_ = None) : socket 'Max' (Max_001)
- **id** (_Integer_ = None) : socket 'ID' (ID)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### raycast()

> classmethod

``` python
raycast(target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED')
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

#### Arguments:
- **target_geometry** (_Geometry_ = None) : socket 'Target Geometry' (Target Geometry)
- **attribute** (_Float_ = None) : socket 'Attribute' (Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (Ray Length)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **mapping** (_str_ = INTERPOLATED) : Node.mapping in ('INTERPOLATED', 'NEAREST')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### realize_instances()

> classmethod

``` python
realize_instances(geometry=None, selection=None, realize_all=None, depth=None)
```

> Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **realize_all** (_Boolean_ = None) : socket 'Realize All' (Realize All)
- **depth** (_Integer_ = None) : socket 'Depth' (Depth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### remove_named_attribute()

> classmethod

``` python
remove_named_attribute(geometry=None, name=None, pattern_mode='EXACT')
```

> Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **name** (_String_ = None) : socket 'Name' (Name)
- **pattern_mode** (_str_ = EXACT) : Node.pattern_mode in ('EXACT', 'WILDCARD')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### repeat_input()

> classmethod

``` python
repeat_input(iterations=None, pair_with_output=None, paired_output=None)
```

> Node ERROR: Node 'Repeat Input' not found

#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (Iterations)
- **pair_with_output** (_bpy_func_ = None) : Node.pair_with_output
- **paired_output** (_NoneType_ = None) : Node.paired_output

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### repeat_output()

> classmethod

``` python
repeat_output(geometry=None, active_index=0, active_item=None, inspection_index=0, repeat_items=None)
```

> Node ERROR: Node 'Repeat Output' not found

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Item_0)
- **active_index** (_int_ = 0) : Node.active_index
- **active_item** (_RepeatItem_ = None) : Node.active_item
- **inspection_index** (_int_ = 0) : Node.inspection_index
- **repeat_items** (_bpy_prop_collection_ = None) : Node.repeat_items



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### replace_material()

> classmethod

``` python
replace_material(geometry=None, old=None, new=None)
```

> Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **old** (_Material_ = None) : socket 'Old' (Old)
- **new** (_Material_ = None) : socket 'New' (New)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### replace_string()

> classmethod

``` python
replace_string(string=None, find=None, replace=None)
```

> Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/replace_string.html)

#### Arguments:
- **string** (_String_ = None) : socket 'String' (String)
- **find** (_String_ = None) : socket 'Find' (Find)
- **replace** (_String_ = None) : socket 'Replace' (Replace)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### reroute()

> classmethod

``` python
reroute(input=None)
```

> Node [Reroute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/reroute.html)

#### Arguments:
- **input** (_Color_ = None) : socket 'Input' (Input)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### resample_curve()

> classmethod

``` python
resample_curve(curve=None, selection=None, count=None, mode='COUNT')
```

> Node [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **mode** (_str_ = COUNT) : Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### reverse_curve()

> classmethod

``` python
reverse_curve(curve=None, selection=None)
```

> Node [Reverse Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/reverse_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rgb_curves()

> classmethod

``` python
rgb_curves(fac=None, color=None, mapping=None)
```

> Node [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/rgb_curves.html)

#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (Fac)
- **color** (_Color_ = None) : socket 'Color' (Color)
- **mapping** (_CurveMapping_ = None) : Node.mapping



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotate_euler()

> classmethod

``` python
rotate_euler(rotation=None, rotate_by=None, rotation_type='EULER', space='OBJECT')
```

> Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/deprecated/rotate_euler.html)

#### Arguments:
- **rotation** (_Vector_ = None) : socket 'Rotation' (Rotation)
- **rotate_by** (_Vector_ = None) : socket 'Rotate By' (Rotate By)
- **rotation_type** (_str_ = EULER) : Node.rotation_type in ('AXIS_ANGLE', 'EULER')
- **space** (_str_ = OBJECT) : Node.space in ('OBJECT', 'LOCAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotate_instances()

> classmethod

``` python
rotate_instances(instances=None, selection=None, rotation=None, pivot_point=None, local_space=None)
```

> Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)

#### Arguments:
- **instances** (_Geometry_ = None) : socket 'Instances' (Instances)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **pivot_point** (_Vector_ = None) : socket 'Pivot Point' (Pivot Point)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotate_rotation()

> classmethod

``` python
rotate_rotation(rotation=None, rotate_by=None, rotation_space='GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)
- **rotation_space** (_str_ = GLOBAL) : Node.rotation_space in ('GLOBAL', 'LOCAL')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotate_vector()

> classmethod

``` python
rotate_vector(vector=None, rotation=None)
```

> Node [Rotate Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_vector.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotation()

> classmethod

``` python
rotation(rotation_euler=None)
```

> Node [Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/rotation.html)

#### Arguments:
- **rotation_euler** (_Euler_ = None) : Node.rotation_euler



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotation_to_axis_angle()

> classmethod

``` python
rotation_to_axis_angle(rotation=None)
```

> Node ERROR: Node 'Rotation to Axis Angle' not found

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotation_to_euler()

> classmethod

``` python
rotation_to_euler(rotation=None)
```

> Node [Rotation to Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_euler.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### rotation_to_quaternion()

> classmethod

``` python
rotation_to_quaternion(rotation=None)
```

> Node [Rotation to Quaternion](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_quaternion.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_curve()

> classmethod

``` python
sample_curve(curves=None, value=None, factor=None, curve_index=None, data_type='FLOAT', mode='FACTOR', use_all_curves=False)
```

> Node [Sample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html)

#### Arguments:
- **curves** (_Geometry_ = None) : socket 'Curves' (Curves)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (Curve Index)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **mode** (_str_ = FACTOR) : Node.mode in ('FACTOR', 'LENGTH')
- **use_all_curves** (_bool_ = False) : Node.use_all_curves



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_grid()

> classmethod

``` python
sample_grid(grid=None, position=None, data_type='FLOAT', interpolation_mode='TRILINEAR')
```

> Node ERROR: Node 'Sample Grid' not found

#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (Grid)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR')
- **interpolation_mode** (_str_ = TRILINEAR) : Node.interpolation_mode in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_grid_index()

> classmethod

``` python
sample_grid_index(grid=None, x=None, y=None, z=None, data_type='FLOAT')
```

> Node ERROR: Node 'Sample Grid Index' not found

#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (Grid)
- **x** (_Integer_ = None) : socket 'X' (X)
- **y** (_Integer_ = None) : socket 'Y' (Y)
- **z** (_Integer_ = None) : socket 'Z' (Z)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_index()

> classmethod

``` python
sample_index(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT')
```

> Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **index** (_Integer_ = None) : socket 'Index' (Index)
- **clamp** (_bool_ = False) : Node.clamp
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_nearest()

> classmethod

``` python
sample_nearest(geometry=None, sample_position=None, domain='POINT')
```

> Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Sample Position)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_nearest_surface()

> classmethod

``` python
sample_nearest_surface(mesh=None, value=None, group_id=None, sample_position=None, sample_group_id=None, data_type='FLOAT')
```

> Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Sample Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (Sample Group ID)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sample_uv_surface()

> classmethod

``` python
sample_uv_surface(mesh=None, value=None, uv_map=None, sample_uv=None, data_type='FLOAT')
```

> Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **uv_map** (_Vector_ = None) : socket 'UV Map' (Source UV Map)
- **sample_uv** (_Vector_ = None) : socket 'Sample UV' (Sample UV)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### scale_elements()

> classmethod

``` python
scale_elements(geometry=None, selection=None, scale=None, center=None, domain='FACE', scale_mode='UNIFORM')
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **domain** (_str_ = FACE) : Node.domain in ('FACE', 'EDGE')
- **scale_mode** (_str_ = UNIFORM) : Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### scale_instances()

> classmethod

``` python
scale_instances(instances=None, selection=None, scale=None, center=None, local_space=None)
```

> Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)

#### Arguments:
- **instances** (_Geometry_ = None) : socket 'Instances' (Instances)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sdf_grid_boolean()

> classmethod

``` python
sdf_grid_boolean(grid_1=None, grid_2=None, operation='DIFFERENCE')
```

> Node ERROR: Node 'SDF Grid Boolean' not found

#### Arguments:
- **grid_1** (_Float_ = None) : socket 'Grid 1' (Grid 1)
- **grid_2** (_Float_ = None) : socket 'Grid 2' (Grid 2)
- **operation** (_str_ = DIFFERENCE) : Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_color()

> classmethod

``` python
separate_color(color=None, mode='RGB')
```

> Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (Color)
- **mode** (_str_ = RGB) : Node.mode in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_components()

> classmethod

``` python
separate_components(geometry=None)
```

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_geometry()

> classmethod

``` python
separate_geometry(geometry=None, selection=None, domain='POINT')
```

> Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_matrix()

> classmethod

``` python
separate_matrix(matrix=None)
```

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (Matrix)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_transform()

> classmethod

``` python
separate_transform(transform=None)
```

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### separate_xyz()

> classmethod

``` python
separate_xyz(vector=None)
```

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_curve_normal()

> classmethod

``` python
set_curve_normal(curve=None, selection=None, mode='MINIMUM_TWIST')
```

> Node [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **mode** (_str_ = MINIMUM_TWIST) : Node.mode in ('MINIMUM_TWIST', 'Z_UP', 'FREE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_curve_radius()

> classmethod

``` python
set_curve_radius(curve=None, selection=None, radius=None)
```

> Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_radius.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_curve_tilt()

> classmethod

``` python
set_curve_tilt(curve=None, selection=None, tilt=None)
```

> Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_tilt.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **tilt** (_Float_ = None) : socket 'Tilt' (Tilt)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_face_set()

> classmethod

``` python
set_face_set(mesh=None, selection=None, face_set=None)
```

> Node [Set Face Set](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_face_set.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **face_set** (_Integer_ = None) : socket 'Face Set' (Face Set)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_geometry_name()

> classmethod

``` python
set_geometry_name(geometry=None, name=None)
```

> Node [Set Geometry Name](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_geometry_name.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **name** (_String_ = None) : socket 'Name' (Name)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_handle_positions()

> classmethod

``` python
set_handle_positions(curve=None, selection=None, position=None, offset=None, mode='LEFT')
```

> Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **mode** (_str_ = LEFT) : Node.mode in ('LEFT', 'RIGHT')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_handle_type()

> classmethod

``` python
set_handle_type(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

> Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **handle_type** (_str_ = AUTO) : Node.handle_type in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
- **mode** (_set_ = {'LEFT', 'RIGHT'}) : Node.mode



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_id()

> classmethod

``` python
set_id(geometry=None, selection=None, id=None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **id** (_Integer_ = None) : socket 'ID' (ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_instance_transform()

> classmethod

``` python
set_instance_transform(instances=None, selection=None, transform=None)
```

> Node [Set Instance Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/set_instance_transform.html)

#### Arguments:
- **instances** (_Geometry_ = None) : socket 'Instances' (Instances)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **transform** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_material()

> classmethod

``` python
set_material(geometry=None, selection=None, material=None)
```

> Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **material** (_Material_ = None) : socket 'Material' (Material)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_material_index()

> classmethod

``` python
set_material_index(geometry=None, selection=None, material_index=None)
```

> Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **material_index** (_Integer_ = None) : socket 'Material Index' (Material Index)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_point_radius()

> classmethod

``` python
set_point_radius(points=None, selection=None, radius=None)
```

> Node [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)

#### Arguments:
- **points** (_Geometry_ = None) : socket 'Points' (Points)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_position()

> classmethod

``` python
set_position(geometry=None, selection=None, position=None, offset=None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_selection()

> classmethod

``` python
set_selection(geometry=None, selection=None, domain='POINT')
```

> Node [Set Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_selection.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_shade_smooth()

> classmethod

``` python
set_shade_smooth(geometry=None, selection=None, shade_smooth=None, domain='FACE')
```

> Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **shade_smooth** (_Boolean_ = None) : socket 'Shade Smooth' (Shade Smooth)
- **domain** (_str_ = FACE) : Node.domain in ('EDGE', 'FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_spline_cyclic()

> classmethod

``` python
set_spline_cyclic(geometry=None, selection=None, cyclic=None)
```

> Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **cyclic** (_Boolean_ = None) : socket 'Cyclic' (Cyclic)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_spline_resolution()

> classmethod

``` python
set_spline_resolution(geometry=None, selection=None, resolution=None)
```

> Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### set_spline_type()

> classmethod

``` python
set_spline_type(curve=None, selection=None, spline_type='POLY')
```

> Node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **spline_type** (_str_ = POLY) : Node.spline_type in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### shortest_edge_paths()

> classmethod

``` python
shortest_edge_paths(end_vertex=None, edge_cost=None)
```

> Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/shortest_edge_paths.html)

#### Arguments:
- **end_vertex** (_Boolean_ = None) : socket 'End Vertex' (End Vertex)
- **edge_cost** (_Float_ = None) : socket 'Edge Cost' (Edge Cost)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### simulation_input()

> classmethod

``` python
simulation_input(pair_with_output=None, paired_output=None)
```

> Node ERROR: Node 'Simulation Input' not found

#### Arguments:
- **pair_with_output** (_bpy_func_ = None) : Node.pair_with_output
- **paired_output** (_NoneType_ = None) : Node.paired_output



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### simulation_output()

> classmethod

``` python
simulation_output(skip=None, geometry=None, active_index=0, active_item=None, state_items=None)
```

> Node ERROR: Node 'Simulation Output' not found

#### Arguments:
- **skip** (_Boolean_ = None) : socket 'Skip' (Skip)
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Item_0)
- **active_index** (_int_ = 0) : Node.active_index
- **active_item** (_SimulationStateItem_ = None) : Node.active_item
- **state_items** (_bpy_prop_collection_ = None) : Node.state_items



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### slice_string()

> classmethod

``` python
slice_string(string=None, position=None, length=None)
```

> Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/slice_string.html)

#### Arguments:
- **string** (_String_ = None) : socket 'String' (String)
- **position** (_Integer_ = None) : socket 'Position' (Position)
- **length** (_Integer_ = None) : socket 'Length' (Length)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### sort_elements()

> classmethod

``` python
sort_elements(geometry=None, selection=None, group_id=None, sort_weight=None, domain='POINT')
```

> Node [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (Sort Weight)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### spiral()

> classmethod

``` python
spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None)
```

> Node ERROR: Node 'Spiral' not found

#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (Resolution)
- **rotations** (_Float_ = None) : socket 'Rotations' (Rotations)
- **start_radius** (_Float_ = None) : socket 'Start Radius' (Start Radius)
- **end_radius** (_Float_ = None) : socket 'End Radius' (End Radius)
- **height** (_Float_ = None) : socket 'Height' (Height)
- **reverse** (_Boolean_ = None) : socket 'Reverse' (Reverse)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### split_edges()

> classmethod

``` python
split_edges(mesh=None, selection=None)
```

> Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### split_to_instances()

> classmethod

``` python
split_to_instances(geometry=None, selection=None, group_id=None, domain='POINT')
```

> Node [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### star()

> classmethod

``` python
star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

> Node [Star](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/star.html)

#### Arguments:
- **points** (_Integer_ = None) : socket 'Points' (Points)
- **inner_radius** (_Float_ = None) : socket 'Inner Radius' (Inner Radius)
- **outer_radius** (_Float_ = None) : socket 'Outer Radius' (Outer Radius)
- **twist** (_Float_ = None) : socket 'Twist' (Twist)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### store_named_attribute()

> classmethod

``` python
store_named_attribute(geometry=None, selection=None, name=None, value=None, data_type='FLOAT', domain='POINT')
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **name** (_String_ = None) : socket 'Name' (Name)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2', 'INT8', 'QUATERNION', 'FLOAT4X4')
- **domain** (_str_ = POINT) : Node.domain in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### store_named_grid()

> classmethod

``` python
store_named_grid(volume=None, name=None, grid=None, data_type='FLOAT')
```

> Node ERROR: Node 'Store Named Grid' not found

#### Arguments:
- **volume** (_Geometry_ = None) : socket 'Volume' (Volume)
- **name** (_String_ = None) : socket 'Name' (Name)
- **grid** (_Float_ = None) : socket 'Grid' (Grid)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'FLOAT_VECTOR', 'FLOAT2')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### string()

> classmethod

``` python
string(string='')
```

> Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

#### Arguments:
- **string** (_str_ = ) : Node.string



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### string_length()

> classmethod

``` python
string_length(string=None)
```

> Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_length.html)

#### Arguments:
- **string** (_String_ = None) : socket 'String' (String)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### string_to_curves()

> classmethod

``` python
string_to_curves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT')
```

> Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html)

#### Arguments:
- **string** (_String_ = None) : socket 'String' (String)
- **size** (_Float_ = None) : socket 'Size' (Size)
- **character_spacing** (_Float_ = None) : socket 'Character Spacing' (Character Spacing)
- **word_spacing** (_Float_ = None) : socket 'Word Spacing' (Word Spacing)
- **line_spacing** (_Float_ = None) : socket 'Line Spacing' (Line Spacing)
- **text_box_width** (_Float_ = None) : socket 'Text Box Width' (Text Box Width)
- **align_x** (_str_ = LEFT) : Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- **align_y** (_str_ = TOP_BASELINE) : Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- **font** (_VectorFont_ = None) : Node.font
- **overflow** (_str_ = OVERFLOW) : Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- **pivot_mode** (_str_ = BOTTOM_LEFT) : Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### subdivide_curve()

> classmethod

``` python
subdivide_curve(curve=None, cuts=None)
```

> Node [Subdivide Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/subdivide_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **cuts** (_Integer_ = None) : socket 'Cuts' (Cuts)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### subdivide_mesh()

> classmethod

``` python
subdivide_mesh(mesh=None, level=None)
```

> Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivide_mesh.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **level** (_Integer_ = None) : socket 'Level' (Level)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### subdivision_surface()

> classmethod

``` python
subdivision_surface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES')
```

> Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivision_surface.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **level** (_Integer_ = None) : socket 'Level' (Level)
- **edge_crease** (_Float_ = None) : socket 'Edge Crease' (Edge Crease)
- **vertex_crease** (_Float_ = None) : socket 'Vertex Crease' (Vertex Crease)
- **boundary_smooth** (_str_ = ALL) : Node.boundary_smooth in ('PRESERVE_CORNERS', 'ALL')
- **uv_smooth** (_str_ = PRESERVE_BOUNDARIES) : Node.uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### switch()

> classmethod

``` python
switch(switch=None, false=None, true=None, input_type='GEOMETRY')
```

> Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)

#### Arguments:
- **switch** (_Boolean_ = None) : socket 'Switch' (Switch)
- **false** (_Geometry_ = None) : socket 'False' (False)
- **true** (_Geometry_ = None) : socket 'True' (True)
- **input_type** (_str_ = GEOMETRY) : Node.input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### transform_direction()

> classmethod

``` python
transform_direction(direction=None, transform=None)
```

> Node [Transform Direction](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_direction.html)

#### Arguments:
- **direction** (_Vector_ = None) : socket 'Direction' (Direction)
- **transform** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### transform_geometry()

> classmethod

``` python
transform_geometry(geometry=None, translation=None, rotation=None, scale=None, transform=None)
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **transform** (_Matrix_ = None) : socket 'Transform' (Scale)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### transform_gizmo()

> classmethod

``` python
transform_gizmo(*value, position=None, rotation=None, use_rotation=True, use_scale=True, use_translation=True)
```

> Node ERROR: Node 'Transform Gizmo' not found

#### Arguments:
- **value** (_Matrix_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **use_rotation** (_bool or triplet of bools_ = True) : use_rotation_x, use_rotation_y, use_rotation_z
- **use_scale** (_bool or triplet of bools_ = True) : use_scale_x, use_scale_y, use_scale_z
- **use_translation** (_bool or triplet of bools_ = True) : use_translation_x, translation_y, use_translation_z



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### transform_point()

> classmethod

``` python
transform_point(vector=None, transform=None)
```

> Node [Transform Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_point.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **transform** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### translate_instances()

> classmethod

``` python
translate_instances(instances=None, selection=None, translation=None, local_space=None)
```

> Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)

#### Arguments:
- **instances** (_Geometry_ = None) : socket 'Instances' (Instances)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### transpose_matrix()

> classmethod

``` python
transpose_matrix(matrix=None)
```

> Node [Transpose Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transpose_matrix.html)

#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (Matrix)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### triangulate()

> classmethod

``` python
triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL')
```

> Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/triangulate.html)

#### Arguments:
- **mesh** (_Geometry_ = None) : socket 'Mesh' (Mesh)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **minimum_vertices** (_Integer_ = None) : socket 'Minimum Vertices' (Minimum Vertices)
- **ngon_method** (_str_ = BEAUTY) : Node.ngon_method in ('BEAUTY', 'CLIP')
- **quad_method** (_str_ = SHORTEST_DIAGONAL) : Node.quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### trim_curve()

> classmethod

``` python
trim_curve(curve=None, selection=None, start=None, end=None, mode='FACTOR')
```

> Node [Trim Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **start** (_Float_ = None) : socket 'Start' (Start)
- **end** (_Float_ = None) : socket 'End' (End)
- **mode** (_str_ = FACTOR) : Node.mode in ('FACTOR', 'LENGTH')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### uv_sphere()

> classmethod

``` python
uv_sphere(segments=None, rings=None, radius=None)
```

> Node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/uv_sphere.html)

#### Arguments:
- **segments** (_Integer_ = None) : socket 'Segments' (Segments)
- **rings** (_Integer_ = None) : socket 'Rings' (Rings)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### uv_unwrap()

> classmethod

``` python
uv_unwrap(selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Arguments:
- **selection** (_Boolean_ = None) : socket 'Selection' (Selection)
- **seam** (_Boolean_ = None) : socket 'Seam' (Seam)
- **margin** (_Float_ = None) : socket 'Margin' (Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (Fill Holes)
- **method** (_str_ = ANGLE_BASED) : Node.method in ('ANGLE_BASED', 'CONFORMAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### value_to_string()

> classmethod

``` python
value_to_string(value=None, decimals=None)
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **decimals** (_Integer_ = None) : socket 'Decimals' (Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### vector()

> classmethod

``` python
vector(vector=None)
```

> Node [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/vector.html)

#### Arguments:
- **vector** (_Vector_ = None) : Node.vector



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### vector_curves()

> classmethod

``` python
vector_curves(fac=None, vector=None, mapping=None)
```

> Node [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_curves.html)

#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (Fac)
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **mapping** (_CurveMapping_ = None) : Node.mapping



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### vector_math()

> classmethod

``` python
vector_math(vector=None, vector_1=None, operation='ADD')
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **vector_1** (_Vector_ = None) : socket 'Vector' (Vector_001)
- **operation** (_str_ = ADD) : Node.operation in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### vector_rotate()

> classmethod

``` python
vector_rotate(vector=None, center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE')
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **axis** (_Vector_ = None) : socket 'Axis' (Axis)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **invert** (_bool_ = False) : Node.invert
- **rotation_type** (_str_ = AXIS_ANGLE) : Node.rotation_type in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### vertex_of_corner()

> classmethod

``` python
vertex_of_corner(corner_index=None)
```

> Node [Vertex of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/vertex_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (Corner Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(geometry=None, value=None, data_type='FLOAT', domain='AUTO')
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Arguments:
- **geometry** (_Geometry_ = None) : socket 'Geometry' (Geometry)
- **value** (_Float_ = None) : socket 'Value' (Value)
- **data_type** (_str_ = FLOAT) : Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')
- **domain** (_str_ = AUTO) : Node.domain in ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### volume_cube()

> classmethod

``` python
volume_cube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

> Node [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/primitives/volume_cube.html)

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **background** (_Float_ = None) : socket 'Background' (Background)
- **min** (_Vector_ = None) : socket 'Min' (Min)
- **max** (_Vector_ = None) : socket 'Max' (Max)
- **resolution_x** (_Integer_ = None) : socket 'Resolution X' (Resolution X)
- **resolution_y** (_Integer_ = None) : socket 'Resolution Y' (Resolution Y)
- **resolution_z** (_Integer_ = None) : socket 'Resolution Z' (Resolution Z)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### volume_to_mesh()

> classmethod

``` python
volume_to_mesh(volume=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **volume** (_Geometry_ = None) : socket 'Volume' (Volume)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)
- **resolution_mode** (_str_ = GRID) : Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### voronoi_texture()

> classmethod

``` python
voronoi_texture(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, color_mapping=None, distance='EUCLIDEAN', feature='F1', normalize=False, texture_mapping=None, voronoi_dimensions='3D')
```

> Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (Lacunarity)
- **randomness** (_Float_ = None) : socket 'Randomness' (Randomness)
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **distance** (_str_ = EUCLIDEAN) : Node.distance in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** (_str_ = F1) : Node.feature in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **normalize** (_bool_ = False) : Node.normalize
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping
- **voronoi_dimensions** (_str_ = 3D) : Node.voronoi_dimensions in ('1D', '2D', '3D', '4D')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### warning()

> classmethod

``` python
warning(show=None, message=None, warning_type='ERROR')
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Arguments:
- **show** (_Boolean_ = None) : socket 'Show' (Show)
- **message** (_String_ = None) : socket 'Message' (Message)
- **warning_type** (_str_ = ERROR) : Node.warning_type



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### wave_texture()

> classmethod

``` python
wave_texture(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', color_mapping=None, rings_direction='X', texture_mapping=None, wave_profile='SIN', wave_type='BANDS')
```

> Node [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (Distortion)
- **detail** (_Float_ = None) : socket 'Detail' (Detail)
- **detail_scale** (_Float_ = None) : socket 'Detail Scale' (Detail Scale)
- **detail_roughness** (_Float_ = None) : socket 'Detail Roughness' (Detail Roughness)
- **phase_offset** (_Float_ = None) : socket 'Phase Offset' (Phase Offset)
- **bands_direction** (_str_ = X) : Node.bands_direction in ('X', 'Y', 'Z', 'DIAGONAL')
- **color_mapping** (_ColorMapping_ = None) : Node.color_mapping
- **rings_direction** (_str_ = X) : Node.rings_direction in ('X', 'Y', 'Z', 'SPHERICAL')
- **texture_mapping** (_TexMapping_ = None) : Node.texture_mapping
- **wave_profile** (_str_ = SIN) : Node.wave_profile in ('SIN', 'SAW', 'TRI')
- **wave_type** (_str_ = BANDS) : Node.wave_type in ('BANDS', 'RINGS')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>

----------
### white_noise_texture()

> classmethod

``` python
white_noise_texture(vector=None, noise_dimensions='3D')
```

> Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **noise_dimensions** (_str_ = 3D) : Node.noise_dimensions in ('1D', '2D', '3D', '4D')



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [nd](nd.md#nd) :black_small_square: [Content](nd.md#content) :black_small_square: [Methods](nd.md#methods)</sub>