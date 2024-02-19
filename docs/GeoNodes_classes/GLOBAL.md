# Global functions

***A*** : [abs](#abs) [add](#add) [align_euler_to_vector](#align_euler_to_vector) [arccos](#arccos) [arcsin](#arcsin) [arctan](#arctan) [arctan2](#arctan2) [axis_angle_to_rotation](#axis_angle_to_rotation)

***B*** : [band](#band) [bezier_segment](#bezier_segment) [blur_attribute](#blur_attribute) [bnot](#bnot) [boolean](#boolean) [boolean_math](#boolean_math) [bor](#bor)

***C*** : [ceil](#ceil) [clamp](#clamp) [collection_info](#collection_info) [color](#color) [combine_color](#combine_color) [combine_hsl](#combine_hsl) [combine_hsv](#combine_hsv) [combine_rgb](#combine_rgb) [combine_xyz](#combine_xyz) [compare](#compare) [convex_hull](#convex_hull) [cos](#cos) [cosh](#cosh) [curve_length](#curve_length) [curve_line](#curve_line) [curve_tangent](#curve_tangent) [curve_tilt](#curve_tilt) [curve_to_mesh](#curve_to_mesh)

***D*** : [deform_curves_on_surface](#deform_curves_on_surface) [degrees](#degrees) [delete_geometry](#delete_geometry) [distribute_points_in_volume](#distribute_points_in_volume) [divide](#divide) [dual_mesh](#dual_mesh)

***E*** : [edge_angle](#edge_angle) [edge_neighbors](#edge_neighbors) [edge_paths_to_curves](#edge_paths_to_curves) [edge_paths_to_selection](#edge_paths_to_selection) [edge_vertices](#edge_vertices) [edges_to_face_groups](#edges_to_face_groups) [endpoint_selection](#endpoint_selection) [euler_to_rotation](#euler_to_rotation) [evaluate_at_index](#evaluate_at_index) [evaluate_on_domain](#evaluate_on_domain) [exp](#exp)

***F*** : [face_area](#face_area) [face_group_boundaries](#face_group_boundaries) [face_neighbors](#face_neighbors) [face_set](#face_set) [fill_curve](#fill_curve) [fillet_curve](#fillet_curve) [flip_faces](#flip_faces) [float_curve](#float_curve) [float_to_integer](#float_to_integer) [floor](#floor) [floored_modulo](#floored_modulo) [fract](#fract) [frame](#frame)

***G*** : [geometry_to_instance](#geometry_to_instance)

***H*** : [handle_type_selection](#handle_type_selection)

***I*** : [id](#id) [image](#image) [imply](#imply) [index](#index) [instance_on_points](#instance_on_points) [instance_rotation](#instance_rotation) [instance_scale](#instance_scale) [instances_to_points](#instances_to_points) [integer](#integer) [inverse_sqrt](#inverse_sqrt) [invert_rotation](#invert_rotation) [is_edge_smooth](#is_edge_smooth) [is_face_planar](#is_face_planar) [is_face_smooth](#is_face_smooth) [is_spline_cyclic](#is_spline_cyclic) [is_viewport](#is_viewport)

***J*** : [join_geometry](#join_geometry) [join_strings](#join_strings)

***L*** : [log](#log)

***M*** : [material](#material) [material_index](#material_index) [material_selection](#material_selection) [math](#math) [math_compare](#math_compare) [math_greater_than](#math_greater_than) [math_less_than](#math_less_than) [max](#max) [mean_filter_sdf_volume](#mean_filter_sdf_volume) [merge_by_distance](#merge_by_distance) [mesh_circle](#mesh_circle) [mesh_island](#mesh_island) [mesh_line](#mesh_line) [mesh_to_curve](#mesh_to_curve) [mesh_to_points](#mesh_to_points) [mesh_to_sdf_volume](#mesh_to_sdf_volume) [mesh_to_volume](#mesh_to_volume) [min](#min) [mix](#mix) [mod](#mod) [multiply](#multiply) [multiply_add](#multiply_add) [musgrave_texture](#musgrave_texture)

***N*** : [named_boolean](#named_boolean) [named_color](#named_color) [named_float](#named_float) [named_int](#named_int) [named_quaternion](#named_quaternion) [named_vector](#named_vector) [nand](#nand) [nimply](#nimply) [nor](#nor) [normal](#normal)

***O*** : [offset_corner_in_face](#offset_corner_in_face) [offset_sdf_volume](#offset_sdf_volume)

***P*** : [pack_uv_islands](#pack_uv_islands) [pingpong](#pingpong) [points](#points) [points_to_curves](#points_to_curves) [points_to_sdf_volume](#points_to_sdf_volume) [points_to_vertices](#points_to_vertices) [points_to_volume](#points_to_volume) [position](#position) [power](#power)

***Q*** : [quadratic_bezier](#quadratic_bezier) [quadrilateral](#quadrilateral) [quaternion_to_rotation](#quaternion_to_rotation)

***R*** : [radians](#radians) [radius](#radius) [random_boolean](#random_boolean) [random_float](#random_float) [random_int](#random_int) [random_value](#random_value) [random_vector](#random_vector) [realize_instances](#realize_instances) [remove_named_attribute](#remove_named_attribute) [repeat_output](#repeat_output) [replace_material](#replace_material) [replace_string](#replace_string) [reroute](#reroute) [resample_curve](#resample_curve) [reverse_curve](#reverse_curve) [rgb_curves](#rgb_curves) [rotate_euler](#rotate_euler) [rotate_instances](#rotate_instances) [rotate_vector](#rotate_vector) [rotation_to_euler](#rotation_to_euler) [round](#round)

***S*** : [sample_index](#sample_index) [sample_nearest](#sample_nearest) [sample_nearest_surface](#sample_nearest_surface) [sample_volume](#sample_volume) [scale_elements](#scale_elements) [scale_instances](#scale_instances) [scene_time](#scene_time) [sdf_volume_sphere](#sdf_volume_sphere) [selection](#selection) [self_object](#self_object) [set_curve_normal](#set_curve_normal) [set_curve_radius](#set_curve_radius) [set_curve_tilt](#set_curve_tilt) [set_face_set](#set_face_set) [set_handle_positions](#set_handle_positions) [set_handle_type](#set_handle_type) [set_id](#set_id) [set_material](#set_material) [set_material_index](#set_material_index) [set_point_radius](#set_point_radius) [set_position](#set_position) [set_selection](#set_selection) [set_shade_smooth](#set_shade_smooth) [set_spline_cyclic](#set_spline_cyclic) [set_spline_resolution](#set_spline_resolution) [set_spline_type](#set_spline_type) [sign](#sign) [signed_distance](#signed_distance) [simulation_output](#simulation_output) [sin](#sin) [sinh](#sinh) [slice_string](#slice_string) [smooth_max](#smooth_max) [smooth_min](#smooth_min) [snap](#snap) [special_characters](#special_characters) [spiral](#spiral) [spline_length](#spline_length) [spline_parameter](#spline_parameter) [spline_resolution](#spline_resolution) [split_edges](#split_edges) [sqrt](#sqrt) [store_named_attribute](#store_named_attribute) [string](#string) [string_length](#string_length) [subdivide_curve](#subdivide_curve) [subdivide_mesh](#subdivide_mesh) [subdivision_surface](#subdivision_surface) [subtract](#subtract) [switch](#switch)

***T*** : [tan](#tan) [tanh](#tanh) [transform_geometry](#transform_geometry) [translate_instances](#translate_instances) [triangulate](#triangulate) [trim_curve](#trim_curve) [trunc](#trunc)

***U*** : [uv_unwrap](#uv_unwrap)

***V*** : [value](#value) [value_to_string](#value_to_string) [vector](#vector) [vector_curves](#vector_curves) [vector_rotate](#vector_rotate) [vertex_neighbors](#vertex_neighbors) [vertex_of_corner](#vertex_of_corner) [volume_cube](#volume_cube) [volume_to_mesh](#volume_to_mesh)

***W*** : [wrap](#wrap)

***X*** : [xnor](#xnor) [xor](#xor)

***_*** : [_3d_cursor](#_3d_cursor)

## _3d_cursor

> _3DCursor, return node

``` python
def _3d_cursor(node_label=None, node_color=None):
```
Node
 - class_name : [_3DCursor](/docs/GeoNodes_classes/_3DCursor.md)
 - bl_idname : GeometryNodeTool3DCursor

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## abs

> Math, value=self, operation='ABSOLUTE'

``` python
def abs(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ABSOLUTE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## add

> Math, value=self, operation='ADD'

``` python
def add(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## align_euler_to_vector

> AlignEulerToVector, return single output socket

``` python
def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', node_label=None, node_color=None):
```
Node
 - class_name : [AlignEulerToVector](/docs/GeoNodes_classes/AlignEulerToVector.md)
 - bl_idname : FunctionNodeAlignEulerToVector

Arguments
 - rotation : None
 - factor : None
 - vector : None
 - axis : 'X'
 - pivot_axis : 'AUTO'
 - node_label : None
 - node_color : None

Node initialization
 - rotation : rotation
 - factor : factor
 - vector : vector
 - axis : axis
 - pivot_axis : pivot_axis
 - node_label : node_label
 - node_color : node_color

## arccos

> Math, value=self, operation='ARCCOSINE'

``` python
def arccos(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCCOSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arcsin

> Math, value=self, operation='ARCSINE'

``` python
def arcsin(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arctan

> Math, value=self, operation='ARCTANGENT'

``` python
def arctan(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ARCTANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## arctan2

> Math, value=self, operation='ARCTAN2'

``` python
def arctan2(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'ARCTAN2'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## axis_angle_to_rotation

> AxisAngleToRotation, return single output socket

``` python
def axis_angle_to_rotation(axis=None, angle=None, node_label=None, node_color=None):
```
Node
 - class_name : [AxisAngleToRotation](/docs/GeoNodes_classes/AxisAngleToRotation.md)
 - bl_idname : FunctionNodeAxisAngleToRotation

Arguments
 - axis : None
 - angle : None
 - node_label : None
 - node_color : None

Node initialization
 - axis : axis
 - angle : angle
 - node_label : node_label
 - node_color : node_color

## band

> BooleanMath, boolean=self, operation='AND'

``` python
def band(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'AND'
 - node_label : node_label
 - node_color : node_color

## bezier_segment

> BezierSegment, return single output socket

``` python
def bezier_segment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label=None, node_color=None):
```
Node
 - class_name : [BezierSegment](/docs/GeoNodes_classes/BezierSegment.md)
 - bl_idname : GeometryNodeCurvePrimitiveBezierSegment

Arguments
 - resolution : None
 - start : None
 - start_handle : None
 - end_handle : None
 - end : None
 - mode : 'POSITION'
 - node_label : None
 - node_color : None

Node initialization
 - resolution : resolution
 - start : start
 - start_handle : start_handle
 - end_handle : end_handle
 - end : end
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## blur_attribute

> BlurAttribute, return single output socket

``` python
def blur_attribute(value=None, iterations=None, weight=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [BlurAttribute](/docs/GeoNodes_classes/BlurAttribute.md)
 - bl_idname : GeometryNodeBlurAttribute

Arguments
 - value : None
 - iterations : None
 - weight : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - iterations : iterations
 - weight : weight
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

## bnot

> BooleanMath, boolean=self, operation='NOT'

``` python
def bnot(boolean=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - operation : 'NOT'
 - node_label : node_label
 - node_color : node_color

## boolean

> Boolean, return socket

``` python
def boolean(boolean, node_label=None, node_color=None):
```
Node
 - class_name : [Boolean](/docs/GeoNodes_classes/Boolean.md)
 - bl_idname : FunctionNodeInputBool

## boolean_math

> BooleanMath, return single output socket

``` python
def boolean_math(boolean=None, boolean_1=None, operation='AND', node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - operation : 'AND'
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : operation
 - node_label : node_label
 - node_color : node_color

## bor

> BooleanMath, boolean=self, operation='OR'

``` python
def bor(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'OR'
 - node_label : node_label
 - node_color : node_color

## ceil

> Math, value=self, operation='CEIL'

``` python
def ceil(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'CEIL'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## clamp

> Clamp, return single output socket

``` python
def clamp(value=None, min=None, max=None, clamp_type='MINMAX', node_label=None, node_color=None):
```
Node
 - class_name : [Clamp](/docs/GeoNodes_classes/Clamp.md)
 - bl_idname : ShaderNodeClamp

Arguments
 - value : None
 - min : None
 - max : None
 - clamp_type : 'MINMAX'
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - min : min
 - max : max
 - clamp_type : clamp_type
 - node_label : node_label
 - node_color : node_color

## collection_info

> CollectionInfo, return single output socket

``` python
def collection_info(collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', node_label=None, node_color=None):
```
Node
 - class_name : [CollectionInfo](/docs/GeoNodes_classes/CollectionInfo.md)
 - bl_idname : GeometryNodeCollectionInfo

Arguments
 - collection : None
 - separate_children : None
 - reset_children : None
 - transform_space : 'ORIGINAL'
 - node_label : None
 - node_color : None

Node initialization
 - collection : collection
 - separate_children : separate_children
 - reset_children : reset_children
 - transform_space : transform_space
 - node_label : node_label
 - node_color : node_color

## color

> Color, return socket

``` python
def color(color, node_label=None, node_color=None):
```
Node
 - class_name : [Color](/docs/GeoNodes_classes/Color.md)
 - bl_idname : FunctionNodeInputColor

## combine_color

> CombineColor, return single output socket

``` python
def combine_color(red=None, green=None, blue=None, alpha=None, mode='RGB', node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/GeoNodes_classes/CombineColor.md)
 - bl_idname : FunctionNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - alpha : None
 - mode : 'RGB'
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - alpha : alpha
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## combine_hsl

> CombineColor, mode='HSL'

``` python
def combine_hsl(red=None, green=None, blue=None, alpha=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/GeoNodes_classes/CombineColor.md)
 - bl_idname : FunctionNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - alpha : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - alpha : alpha
 - mode : 'HSL'
 - node_label : node_label
 - node_color : node_color

## combine_hsv

> CombineColor, mode='HSV'

``` python
def combine_hsv(red=None, green=None, blue=None, alpha=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/GeoNodes_classes/CombineColor.md)
 - bl_idname : FunctionNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - alpha : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - alpha : alpha
 - mode : 'HSV'
 - node_label : node_label
 - node_color : node_color

## combine_rgb

> CombineColor, mode='RGB'

``` python
def combine_rgb(red=None, green=None, blue=None, alpha=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineColor](/docs/GeoNodes_classes/CombineColor.md)
 - bl_idname : FunctionNodeCombineColor

Arguments
 - red : None
 - green : None
 - blue : None
 - alpha : None
 - node_label : None
 - node_color : None

Node initialization
 - red : red
 - green : green
 - blue : blue
 - alpha : alpha
 - mode : 'RGB'
 - node_label : node_label
 - node_color : node_color

## combine_xyz

> CombineXYZ, return single output socket

``` python
def combine_xyz(x=None, y=None, z=None, node_label=None, node_color=None):
```
Node
 - class_name : [CombineXYZ](/docs/GeoNodes_classes/CombineXYZ.md)
 - bl_idname : ShaderNodeCombineXYZ

Arguments
 - x : None
 - y : None
 - z : None
 - node_label : None
 - node_color : None

Node initialization
 - x : x
 - y : y
 - z : z
 - node_label : node_label
 - node_color : node_color

## compare

> Compare, return single output socket

``` python
def compare(a=None, b=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', node_label=None, node_color=None):
```
Node
 - class_name : [Compare](/docs/GeoNodes_classes/Compare.md)
 - bl_idname : FunctionNodeCompare

Arguments
 - a : None
 - b : None
 - epsilon : None
 - data_type : 'FLOAT'
 - mode : 'ELEMENT'
 - operation : 'GREATER_THAN'
 - node_label : None
 - node_color : None

Node initialization
 - a : a
 - b : b
 - epsilon : epsilon
 - data_type : data_type
 - mode : mode
 - operation : operation
 - node_label : node_label
 - node_color : node_color

## convex_hull

> ConvexHull, return single output socket

``` python
def convex_hull(geometry=None, node_label=None, node_color=None):
```
Node
 - class_name : [ConvexHull](/docs/GeoNodes_classes/ConvexHull.md)
 - bl_idname : GeometryNodeConvexHull

Arguments
 - geometry : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - node_label : node_label
 - node_color : node_color

## cos

> Math, value=self, operation='COSINE'

``` python
def cos(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'COSINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## cosh

> Math, value=self, operation='COSH'

``` python
def cosh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'COSH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## curve_length

> CurveLength, return single output socket

``` python
def curve_length(curve=None, node_label=None, node_color=None):
```
Node
 - class_name : [CurveLength](/docs/GeoNodes_classes/CurveLength.md)
 - bl_idname : GeometryNodeCurveLength

Arguments
 - curve : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - node_label : node_label
 - node_color : node_color

## curve_line

> CurveLine, return single output socket

``` python
def curve_line(start=None, end=None, direction=None, length=None, mode='POINTS', node_label=None, node_color=None):
```
Node
 - class_name : [CurveLine](/docs/GeoNodes_classes/CurveLine.md)
 - bl_idname : GeometryNodeCurvePrimitiveLine

Arguments
 - start : None
 - end : None
 - direction : None
 - length : None
 - mode : 'POINTS'
 - node_label : None
 - node_color : None

Node initialization
 - start : start
 - end : end
 - direction : direction
 - length : length
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## curve_tangent

> CurveTangent, return socket

``` python
def curve_tangent(node_label=None, node_color=None):
```
Node
 - class_name : [CurveTangent](/docs/GeoNodes_classes/CurveTangent.md)
 - bl_idname : GeometryNodeInputTangent

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## curve_tilt

> CurveTilt, return socket

``` python
def curve_tilt(node_label=None, node_color=None):
```
Node
 - class_name : [CurveTilt](/docs/GeoNodes_classes/CurveTilt.md)
 - bl_idname : GeometryNodeInputCurveTilt

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## curve_to_mesh

> CurveToMesh, return single output socket

``` python
def curve_to_mesh(curve=None, profile_curve=None, fill_caps=None, node_label=None, node_color=None):
```
Node
 - class_name : [CurveToMesh](/docs/GeoNodes_classes/CurveToMesh.md)
 - bl_idname : GeometryNodeCurveToMesh

Arguments
 - curve : None
 - profile_curve : None
 - fill_caps : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - profile_curve : profile_curve
 - fill_caps : fill_caps
 - node_label : node_label
 - node_color : node_color

## deform_curves_on_surface

> DeformCurvesOnSurface, return single output socket

``` python
def deform_curves_on_surface(curves=None, node_label=None, node_color=None):
```
Node
 - class_name : [DeformCurvesOnSurface](/docs/GeoNodes_classes/DeformCurvesOnSurface.md)
 - bl_idname : GeometryNodeDeformCurvesOnSurface

Arguments
 - curves : None
 - node_label : None
 - node_color : None

Node initialization
 - curves : curves
 - node_label : node_label
 - node_color : node_color

## degrees

> Math, value=self, operation='DEGREES'

``` python
def degrees(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'DEGREES'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## delete_geometry

> DeleteGeometry, return single output socket

``` python
def delete_geometry(geometry=None, selection=None, domain='POINT', mode='ALL', node_label=None, node_color=None):
```
Node
 - class_name : [DeleteGeometry](/docs/GeoNodes_classes/DeleteGeometry.md)
 - bl_idname : GeometryNodeDeleteGeometry

Arguments
 - geometry : None
 - selection : None
 - domain : 'POINT'
 - mode : 'ALL'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - selection : self._get_selection(selection)
 - domain : domain
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## distribute_points_in_volume

> DistributePointsInVolume, return single output socket

``` python
def distribute_points_in_volume(volume=None, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM', node_label=None, node_color=None):
```
Node
 - class_name : [DistributePointsInVolume](/docs/GeoNodes_classes/DistributePointsInVolume.md)
 - bl_idname : GeometryNodeDistributePointsInVolume

Arguments
 - volume : None
 - density : None
 - seed : None
 - spacing : None
 - threshold : None
 - mode : 'DENSITY_RANDOM'
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - density : density
 - seed : seed
 - spacing : spacing
 - threshold : threshold
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## divide

> Math, value=self, operation='DIVIDE'

``` python
def divide(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'DIVIDE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## dual_mesh

> DualMesh, return single output socket

``` python
def dual_mesh(mesh=None, keep_boundaries=None, node_label=None, node_color=None):
```
Node
 - class_name : [DualMesh](/docs/GeoNodes_classes/DualMesh.md)
 - bl_idname : GeometryNodeDualMesh

Arguments
 - mesh : None
 - keep_boundaries : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - keep_boundaries : keep_boundaries
 - node_label : node_label
 - node_color : node_color

## edge_angle

> EdgeAngle, return node

``` python
def edge_angle(node_label=None, node_color=None):
```
Node
 - class_name : [EdgeAngle](/docs/GeoNodes_classes/EdgeAngle.md)
 - bl_idname : GeometryNodeInputMeshEdgeAngle

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## edge_neighbors

> EdgeNeighbors, return socket

``` python
def edge_neighbors(node_label=None, node_color=None):
```
Node
 - class_name : [EdgeNeighbors](/docs/GeoNodes_classes/EdgeNeighbors.md)
 - bl_idname : GeometryNodeInputMeshEdgeNeighbors

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## edge_paths_to_curves

> EdgePathsToCurves, return single output socket

``` python
def edge_paths_to_curves(mesh=None, start_vertices=None, next_vertex_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgePathsToCurves](/docs/GeoNodes_classes/EdgePathsToCurves.md)
 - bl_idname : GeometryNodeEdgePathsToCurves

Arguments
 - mesh : None
 - start_vertices : None
 - next_vertex_index : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - start_vertices : start_vertices
 - next_vertex_index : next_vertex_index
 - node_label : node_label
 - node_color : node_color

## edge_paths_to_selection

> EdgePathsToSelection, return single output socket

``` python
def edge_paths_to_selection(start_vertices=None, next_vertex_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgePathsToSelection](/docs/GeoNodes_classes/EdgePathsToSelection.md)
 - bl_idname : GeometryNodeEdgePathsToSelection

Arguments
 - start_vertices : None
 - next_vertex_index : None
 - node_label : None
 - node_color : None

Node initialization
 - start_vertices : start_vertices
 - next_vertex_index : next_vertex_index
 - node_label : node_label
 - node_color : node_color

## edge_vertices

> EdgeVertices, return node

``` python
def edge_vertices(node_label=None, node_color=None):
```
Node
 - class_name : [EdgeVertices](/docs/GeoNodes_classes/EdgeVertices.md)
 - bl_idname : GeometryNodeInputMeshEdgeVertices

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## edges_to_face_groups

> EdgesToFaceGroups, return single output socket

``` python
def edges_to_face_groups(boundary_edges=None, node_label=None, node_color=None):
```
Node
 - class_name : [EdgesToFaceGroups](/docs/GeoNodes_classes/EdgesToFaceGroups.md)
 - bl_idname : GeometryNodeEdgesToFaceGroups

Arguments
 - boundary_edges : None
 - node_label : None
 - node_color : None

Node initialization
 - boundary_edges : boundary_edges
 - node_label : node_label
 - node_color : node_color

## endpoint_selection

> EndpointSelection, return single output socket

``` python
def endpoint_selection(start_size=None, end_size=None, node_label=None, node_color=None):
```
Node
 - class_name : [EndpointSelection](/docs/GeoNodes_classes/EndpointSelection.md)
 - bl_idname : GeometryNodeCurveEndpointSelection

Arguments
 - start_size : None
 - end_size : None
 - node_label : None
 - node_color : None

Node initialization
 - start_size : start_size
 - end_size : end_size
 - node_label : node_label
 - node_color : node_color

## euler_to_rotation

> EulerToRotation, return single output socket

``` python
def euler_to_rotation(euler=None, node_label=None, node_color=None):
```
Node
 - class_name : [EulerToRotation](/docs/GeoNodes_classes/EulerToRotation.md)
 - bl_idname : FunctionNodeEulerToRotation

Arguments
 - euler : None
 - node_label : None
 - node_color : None

Node initialization
 - euler : euler
 - node_label : node_label
 - node_color : node_color

## evaluate_at_index

> EvaluateAtIndex, return single output socket

``` python
def evaluate_at_index(index=None, value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [EvaluateAtIndex](/docs/GeoNodes_classes/EvaluateAtIndex.md)
 - bl_idname : GeometryNodeFieldAtIndex

Arguments
 - index : None
 - value : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - index : index
 - value : value
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## evaluate_on_domain

> EvaluateOnDomain, return single output socket

``` python
def evaluate_on_domain(value=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [EvaluateOnDomain](/docs/GeoNodes_classes/EvaluateOnDomain.md)
 - bl_idname : GeometryNodeFieldOnDomain

Arguments
 - value : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## exp

> Math, value=self, operation='EXPONENT'

``` python
def exp(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'EXPONENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## face_area

> FaceArea, return socket

``` python
def face_area(node_label=None, node_color=None):
```
Node
 - class_name : [FaceArea](/docs/GeoNodes_classes/FaceArea.md)
 - bl_idname : GeometryNodeInputMeshFaceArea

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## face_group_boundaries

> FaceGroupBoundaries, return single output socket

``` python
def face_group_boundaries(face_group_id=None, node_label=None, node_color=None):
```
Node
 - class_name : [FaceGroupBoundaries](/docs/GeoNodes_classes/FaceGroupBoundaries.md)
 - bl_idname : GeometryNodeMeshFaceSetBoundaries

Arguments
 - face_group_id : None
 - node_label : None
 - node_color : None

Node initialization
 - face_group_id : face_group_id
 - node_label : node_label
 - node_color : node_color

## face_neighbors

> FaceNeighbors, return node

``` python
def face_neighbors(node_label=None, node_color=None):
```
Node
 - class_name : [FaceNeighbors](/docs/GeoNodes_classes/FaceNeighbors.md)
 - bl_idname : GeometryNodeInputMeshFaceNeighbors

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## face_set

> FaceSet, return node

``` python
def face_set(node_label=None, node_color=None):
```
Node
 - class_name : [FaceSet](/docs/GeoNodes_classes/FaceSet.md)
 - bl_idname : GeometryNodeToolFaceSet

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## fill_curve

> FillCurve, return single output socket

``` python
def fill_curve(curve=None, mode='TRIANGLES', node_label=None, node_color=None):
```
Node
 - class_name : [FillCurve](/docs/GeoNodes_classes/FillCurve.md)
 - bl_idname : GeometryNodeFillCurve

Arguments
 - curve : None
 - mode : 'TRIANGLES'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## fillet_curve

> FilletCurve, return single output socket

``` python
def fillet_curve(curve=None, radius=None, limit_radius=None, count=None, mode='BEZIER', node_label=None, node_color=None):
```
Node
 - class_name : [FilletCurve](/docs/GeoNodes_classes/FilletCurve.md)
 - bl_idname : GeometryNodeFilletCurve

Arguments
 - curve : None
 - radius : None
 - limit_radius : None
 - count : None
 - mode : 'BEZIER'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - radius : radius
 - limit_radius : limit_radius
 - count : count
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## flip_faces

> FlipFaces, return single output socket

``` python
def flip_faces(mesh=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [FlipFaces](/docs/GeoNodes_classes/FlipFaces.md)
 - bl_idname : GeometryNodeFlipFaces

Arguments
 - mesh : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## float_curve

> FloatCurve, return single output socket

``` python
def float_curve(factor=None, value=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [FloatCurve](/docs/GeoNodes_classes/FloatCurve.md)
 - bl_idname : ShaderNodeFloatCurve

Arguments
 - factor : None
 - value : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - value : value
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## float_to_integer

> FloatToInteger, return single output socket

``` python
def float_to_integer(float=None, rounding_mode='ROUND', node_label=None, node_color=None):
```
Node
 - class_name : [FloatToInteger](/docs/GeoNodes_classes/FloatToInteger.md)
 - bl_idname : FunctionNodeFloatToInt

Arguments
 - float : None
 - rounding_mode : 'ROUND'
 - node_label : None
 - node_color : None

Node initialization
 - float : float
 - rounding_mode : rounding_mode
 - node_label : node_label
 - node_color : node_color

## floor

> Math, value=self, operation='FLOOR'

``` python
def floor(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'FLOOR'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## floored_modulo

> Math, value=self, operation='FLOORED_MODULO'

``` python
def floored_modulo(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'FLOORED_MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## fract

> Math, value=self, operation='FRACT'

``` python
def fract(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'FRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## frame

> Frame, return node

``` python
def frame(label_size=20, shrink=True, text=None, node_label=None, node_color=None):
```
Node
 - class_name : [Frame](/docs/GeoNodes_classes/Frame.md)
 - bl_idname : NodeFrame

Arguments
 - label_size : 20
 - shrink : True
 - text : None
 - node_label : None
 - node_color : None

Node initialization
 - label_size : label_size
 - shrink : shrink
 - text : text
 - node_label : node_label
 - node_color : node_color

## geometry_to_instance

> GeometryToInstance, return single output socket

``` python
def geometry_to_instance(*args, geometry=None, node_label=None, node_color=None):
```
Node
 - class_name : [GeometryToInstance](/docs/GeoNodes_classes/GeometryToInstance.md)
 - bl_idname : GeometryNodeGeometryToInstance

Arguments
 - *args : 
 - geometry : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - geometry : geometry
 - node_label : node_label
 - node_color : node_color

## handle_type_selection

> HandleTypeSelection, return socket

``` python
def handle_type_selection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):
```
Node
 - class_name : [HandleTypeSelection](/docs/GeoNodes_classes/HandleTypeSelection.md)
 - bl_idname : GeometryNodeCurveHandleTypeSelection

Arguments
 - handle_type : 'AUTO'
 - mode : {'RIGHT', 'LEFT'}
 - node_label : None
 - node_color : None

Node initialization
 - handle_type : handle_type
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## id

> ID, return socket

``` python
def id(node_label=None, node_color=None):
```
Node
 - class_name : [ID](/docs/GeoNodes_classes/ID.md)
 - bl_idname : GeometryNodeInputID

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## image

> Image, return socket

``` python
def image(image, node_label=None, node_color=None):
```
Node
 - class_name : [Image](/docs/GeoNodes_classes/Image.md)
 - bl_idname : GeometryNodeInputImage

## imply

> BooleanMath, boolean=self, operation='IMPLY'

``` python
def imply(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'IMPLY'
 - node_label : node_label
 - node_color : node_color

## index

> Index, return socket

``` python
def index(node_label=None, node_color=None):
```
Node
 - class_name : [Index](/docs/GeoNodes_classes/Index.md)
 - bl_idname : GeometryNodeInputIndex

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## instance_on_points

> InstanceOnPoints, return single output socket

``` python
def instance_on_points(points=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [InstanceOnPoints](/docs/GeoNodes_classes/InstanceOnPoints.md)
 - bl_idname : GeometryNodeInstanceOnPoints

Arguments
 - points : None
 - instance : None
 - pick_instance : None
 - instance_index : None
 - rotation : None
 - scale : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - instance : instance
 - pick_instance : pick_instance
 - instance_index : instance_index
 - rotation : rotation
 - scale : scale
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## instance_rotation

> InstanceRotation, return socket

``` python
def instance_rotation(node_label=None, node_color=None):
```
Node
 - class_name : [InstanceRotation](/docs/GeoNodes_classes/InstanceRotation.md)
 - bl_idname : GeometryNodeInputInstanceRotation

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## instance_scale

> InstanceScale, return socket

``` python
def instance_scale(node_label=None, node_color=None):
```
Node
 - class_name : [InstanceScale](/docs/GeoNodes_classes/InstanceScale.md)
 - bl_idname : GeometryNodeInputInstanceScale

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## instances_to_points

> InstancesToPoints, return single output socket

``` python
def instances_to_points(instances=None, position=None, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [InstancesToPoints](/docs/GeoNodes_classes/InstancesToPoints.md)
 - bl_idname : GeometryNodeInstancesToPoints

Arguments
 - instances : None
 - position : None
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : instances
 - position : position
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## integer

> Integer, return socket

``` python
def integer(integer, node_label=None, node_color=None):
```
Node
 - class_name : [Integer](/docs/GeoNodes_classes/Integer.md)
 - bl_idname : FunctionNodeInputInt

## inverse_sqrt

> Math, value=self, operation='INVERSE_SQRT'

``` python
def inverse_sqrt(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'INVERSE_SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## invert_rotation

> InvertRotation, return single output socket

``` python
def invert_rotation(rotation=None, node_label=None, node_color=None):
```
Node
 - class_name : [InvertRotation](/docs/GeoNodes_classes/InvertRotation.md)
 - bl_idname : FunctionNodeInvertRotation

Arguments
 - rotation : None
 - node_label : None
 - node_color : None

Node initialization
 - rotation : rotation
 - node_label : node_label
 - node_color : node_color

## is_edge_smooth

> IsEdgeSmooth, return socket

``` python
def is_edge_smooth(node_label=None, node_color=None):
```
Node
 - class_name : [IsEdgeSmooth](/docs/GeoNodes_classes/IsEdgeSmooth.md)
 - bl_idname : GeometryNodeInputEdgeSmooth

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## is_face_planar

> IsFacePlanar, return single output socket

``` python
def is_face_planar(threshold=None, node_label=None, node_color=None):
```
Node
 - class_name : [IsFacePlanar](/docs/GeoNodes_classes/IsFacePlanar.md)
 - bl_idname : GeometryNodeInputMeshFaceIsPlanar

Arguments
 - threshold : None
 - node_label : None
 - node_color : None

Node initialization
 - threshold : threshold
 - node_label : node_label
 - node_color : node_color

## is_face_smooth

> IsFaceSmooth, return socket

``` python
def is_face_smooth(node_label=None, node_color=None):
```
Node
 - class_name : [IsFaceSmooth](/docs/GeoNodes_classes/IsFaceSmooth.md)
 - bl_idname : GeometryNodeInputShadeSmooth

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## is_spline_cyclic

> IsSplineCyclic, return socket

``` python
def is_spline_cyclic(node_label=None, node_color=None):
```
Node
 - class_name : [IsSplineCyclic](/docs/GeoNodes_classes/IsSplineCyclic.md)
 - bl_idname : GeometryNodeInputSplineCyclic

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## is_viewport

> IsViewport, return socket

``` python
def is_viewport(node_label=None, node_color=None):
```
Node
 - class_name : [IsViewport](/docs/GeoNodes_classes/IsViewport.md)
 - bl_idname : GeometryNodeIsViewport

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## join_geometry

> JoinGeometry, return single output socket

``` python
def join_geometry(*args, geometry=None, node_label=None, node_color=None):
```
Node
 - class_name : [JoinGeometry](/docs/GeoNodes_classes/JoinGeometry.md)
 - bl_idname : GeometryNodeJoinGeometry

Arguments
 - *args : 
 - geometry : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - geometry : geometry
 - node_label : node_label
 - node_color : node_color

## join_strings

> JoinStrings, return single output socket

``` python
def join_strings(*args, delimiter=None, strings=None, node_label=None, node_color=None):
```
Node
 - class_name : [JoinStrings](/docs/GeoNodes_classes/JoinStrings.md)
 - bl_idname : GeometryNodeStringJoin

Arguments
 - *args : 
 - delimiter : None
 - strings : None
 - node_label : None
 - node_color : None

Node initialization
 - *args : 
 - delimiter : delimiter
 - strings : strings
 - node_label : node_label
 - node_color : node_color

## log

> Math, value=self, operation='LOGARITHM'

``` python
def log(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'LOGARITHM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## material

> Material, return socket

``` python
def material(material, node_label=None, node_color=None):
```
Node
 - class_name : [Material](/docs/GeoNodes_classes/Material.md)
 - bl_idname : GeometryNodeInputMaterial

## material_index

> MaterialIndex, return socket

``` python
def material_index(node_label=None, node_color=None):
```
Node
 - class_name : [MaterialIndex](/docs/GeoNodes_classes/MaterialIndex.md)
 - bl_idname : GeometryNodeInputMaterialIndex

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## material_selection

> MaterialSelection, return single output socket

``` python
def material_selection(material=None, node_label=None, node_color=None):
```
Node
 - class_name : [MaterialSelection](/docs/GeoNodes_classes/MaterialSelection.md)
 - bl_idname : GeometryNodeMaterialSelection

Arguments
 - material : None
 - node_label : None
 - node_color : None

Node initialization
 - material : material
 - node_label : node_label
 - node_color : node_color

## math

> Math, return single output socket

``` python
def math(value=None, value_1=None, value_2=None, operation='ADD', use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - operation : 'ADD'
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : operation
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## math_compare

> Math, value=self, operation='COMPARE'

``` python
def math_compare(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'COMPARE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## math_greater_than

> Math, value=self, operation='GREATER_THAN'

``` python
def math_greater_than(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'GREATER_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## math_less_than

> Math, value=self, operation='LESS_THAN'

``` python
def math_less_than(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'LESS_THAN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## max

> Math, value=self, operation='MAXIMUM'

``` python
def max(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MAXIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## mean_filter_sdf_volume

> MeanFilterSDFVolume, return single output socket

``` python
def mean_filter_sdf_volume(volume=None, iterations=None, width=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeanFilterSDFVolume](/docs/GeoNodes_classes/MeanFilterSDFVolume.md)
 - bl_idname : GeometryNodeMeanFilterSDFVolume

Arguments
 - volume : None
 - iterations : None
 - width : None
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - iterations : iterations
 - width : width
 - node_label : node_label
 - node_color : node_color

## merge_by_distance

> MergeByDistance, return single output socket

``` python
def merge_by_distance(geometry=None, distance=None, selection=None, mode='ALL', node_label=None, node_color=None):
```
Node
 - class_name : [MergeByDistance](/docs/GeoNodes_classes/MergeByDistance.md)
 - bl_idname : GeometryNodeMergeByDistance

Arguments
 - geometry : None
 - distance : None
 - selection : None
 - mode : 'ALL'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - distance : distance
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## mesh_circle

> MeshCircle, return single output socket

``` python
def mesh_circle(vertices=None, radius=None, fill_type='NONE', node_label=None, node_color=None):
```
Node
 - class_name : [MeshCircle](/docs/GeoNodes_classes/MeshCircle.md)
 - bl_idname : GeometryNodeMeshCircle

Arguments
 - vertices : None
 - radius : None
 - fill_type : 'NONE'
 - node_label : None
 - node_color : None

Node initialization
 - vertices : vertices
 - radius : radius
 - fill_type : fill_type
 - node_label : node_label
 - node_color : node_color

## mesh_island

> MeshIsland, return node

``` python
def mesh_island(node_label=None, node_color=None):
```
Node
 - class_name : [MeshIsland](/docs/GeoNodes_classes/MeshIsland.md)
 - bl_idname : GeometryNodeInputMeshIsland

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## mesh_line

> MeshLine, return single output socket

``` python
def mesh_line(count=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', node_label=None, node_color=None):
```
Node
 - class_name : [MeshLine](/docs/GeoNodes_classes/MeshLine.md)
 - bl_idname : GeometryNodeMeshLine

Arguments
 - count : None
 - start_location : None
 - offset : None
 - count_mode : 'TOTAL'
 - mode : 'OFFSET'
 - node_label : None
 - node_color : None

Node initialization
 - count : count
 - start_location : start_location
 - offset : offset
 - count_mode : count_mode
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## mesh_to_curve

> MeshToCurve, return single output socket

``` python
def mesh_to_curve(mesh=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [MeshToCurve](/docs/GeoNodes_classes/MeshToCurve.md)
 - bl_idname : GeometryNodeMeshToCurve

Arguments
 - mesh : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## mesh_to_points

> MeshToPoints, return single output socket

``` python
def mesh_to_points(mesh=None, position=None, radius=None, selection=None, mode='VERTICES', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToPoints](/docs/GeoNodes_classes/MeshToPoints.md)
 - bl_idname : GeometryNodeMeshToPoints

Arguments
 - mesh : None
 - position : None
 - radius : None
 - selection : None
 - mode : 'VERTICES'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - position : position
 - radius : radius
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## mesh_to_sdf_volume

> MeshToSDFVolume, return single output socket

``` python
def mesh_to_sdf_volume(mesh=None, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToSDFVolume](/docs/GeoNodes_classes/MeshToSDFVolume.md)
 - bl_idname : GeometryNodeMeshToSDFVolume

Arguments
 - mesh : None
 - voxel_amount : None
 - half_band_width : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - voxel_amount : voxel_amount
 - half_band_width : half_band_width
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

## mesh_to_volume

> MeshToVolume, return single output socket

``` python
def mesh_to_volume(mesh=None, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [MeshToVolume](/docs/GeoNodes_classes/MeshToVolume.md)
 - bl_idname : GeometryNodeMeshToVolume

Arguments
 - mesh : None
 - density : None
 - voxel_amount : None
 - interior_band_width : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - density : density
 - voxel_amount : voxel_amount
 - interior_band_width : interior_band_width
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

## min

> Math, value=self, operation='MINIMUM'

``` python
def min(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MINIMUM'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## mix

> Mix, return single output socket

``` python
def mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False, data_type='FLOAT', factor_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [Mix](/docs/GeoNodes_classes/Mix.md)
 - bl_idname : ShaderNodeMix

Arguments
 - factor : None
 - a : None
 - b : None
 - blend_type : 'MIX'
 - clamp_factor : True
 - clamp_result : False
 - data_type : 'FLOAT'
 - factor_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - factor : factor
 - a : a
 - b : b
 - blend_type : blend_type
 - clamp_factor : clamp_factor
 - clamp_result : clamp_result
 - data_type : data_type
 - factor_mode : factor_mode
 - node_label : node_label
 - node_color : node_color

## mod

> Math, value=self, operation='MODULO'

``` python
def mod(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MODULO'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## multiply

> Math, value=self, operation='MULTIPLY'

``` python
def multiply(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'MULTIPLY'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## multiply_add

> Math, value=self, operation='MULTIPLY_ADD'

``` python
def multiply_add(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'MULTIPLY_ADD'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## musgrave_texture

> MusgraveTexture, return single output socket

``` python
def musgrave_texture(vector=None, scale=None, detail=None, dimension=None, lacunarity=None, w=None, offset=None, gain=None, color_mapping=None, musgrave_dimensions='3D', musgrave_type='FBM', texture_mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [MusgraveTexture](/docs/GeoNodes_classes/MusgraveTexture.md)
 - bl_idname : ShaderNodeTexMusgrave

Arguments
 - vector : None
 - scale : None
 - detail : None
 - dimension : None
 - lacunarity : None
 - w : None
 - offset : None
 - gain : None
 - color_mapping
 - musgrave_dimensions : '3D'
 - musgrave_type : 'FBM'
 - texture_mapping
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - scale : scale
 - detail : detail
 - dimension : dimension
 - lacunarity : lacunarity
 - w : w
 - offset : offset
 - gain : gain
 - color_mapping : color_mapping
 - musgrave_dimensions : musgrave_dimensions
 - musgrave_type : musgrave_type
 - texture_mapping : texture_mapping
 - node_label : node_label
 - node_color : node_color

## named_boolean

> NamedAttribute, data_type='BOOLEAN'

``` python
def named_boolean(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'BOOLEAN'
 - node_label : node_label
 - node_color : node_color

## named_color

> NamedAttribute, data_type='FLOAT_COLOR'

``` python
def named_color(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'FLOAT_COLOR'
 - node_label : node_label
 - node_color : node_color

## named_float

> NamedAttribute, data_type='FLOAT'

``` python
def named_float(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'FLOAT'
 - node_label : node_label
 - node_color : node_color

## named_int

> NamedAttribute, data_type='INT'

``` python
def named_int(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'INT'
 - node_label : node_label
 - node_color : node_color

## named_quaternion

> NamedAttribute, data_type='QUATERNION'

``` python
def named_quaternion(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'QUATERNION'
 - node_label : node_label
 - node_color : node_color

## named_vector

> NamedAttribute, data_type='FLOAT_VECTOR'

``` python
def named_vector(name=None, node_label=None, node_color=None):
```
Node
 - class_name : [NamedAttribute](/docs/GeoNodes_classes/NamedAttribute.md)
 - bl_idname : GeometryNodeInputNamedAttribute

Arguments
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - name : name
 - data_type : 'FLOAT_VECTOR'
 - node_label : node_label
 - node_color : node_color

## nand

> BooleanMath, boolean=self, operation='NAND'

``` python
def nand(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'NAND'
 - node_label : node_label
 - node_color : node_color

## nimply

> BooleanMath, boolean=self, operation='NIMPLY'

``` python
def nimply(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'NIMPLY'
 - node_label : node_label
 - node_color : node_color

## nor

> BooleanMath, boolean=self, operation='NOR'

``` python
def nor(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'NOR'
 - node_label : node_label
 - node_color : node_color

## normal

> Normal, return socket

``` python
def normal(node_label=None, node_color=None):
```
Node
 - class_name : [Normal](/docs/GeoNodes_classes/Normal.md)
 - bl_idname : GeometryNodeInputNormal

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## offset_corner_in_face

> OffsetCornerInFace, return single output socket

``` python
def offset_corner_in_face(corner_index=None, offset=None, node_label=None, node_color=None):
```
Node
 - class_name : [OffsetCornerInFace](/docs/GeoNodes_classes/OffsetCornerInFace.md)
 - bl_idname : GeometryNodeOffsetCornerInFace

Arguments
 - corner_index : None
 - offset : None
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : corner_index
 - offset : offset
 - node_label : node_label
 - node_color : node_color

## offset_sdf_volume

> OffsetSDFVolume, return single output socket

``` python
def offset_sdf_volume(volume=None, distance=None, node_label=None, node_color=None):
```
Node
 - class_name : [OffsetSDFVolume](/docs/GeoNodes_classes/OffsetSDFVolume.md)
 - bl_idname : GeometryNodeOffsetSDFVolume

Arguments
 - volume : None
 - distance : None
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - distance : distance
 - node_label : node_label
 - node_color : node_color

## pack_uv_islands

> PackUVIslands, return single output socket

``` python
def pack_uv_islands(uv=None, margin=None, rotate=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [PackUVIslands](/docs/GeoNodes_classes/PackUVIslands.md)
 - bl_idname : GeometryNodeUVPackIslands

Arguments
 - uv : None
 - margin : None
 - rotate : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - uv : uv
 - margin : margin
 - rotate : rotate
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## pingpong

> Math, value=self, operation='PINGPONG'

``` python
def pingpong(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'PINGPONG'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## points

> Points, return single output socket

``` python
def points(count=None, position=None, radius=None, node_label=None, node_color=None):
```
Node
 - class_name : [Points](/docs/GeoNodes_classes/Points.md)
 - bl_idname : GeometryNodePoints

Arguments
 - count : None
 - position : None
 - radius : None
 - node_label : None
 - node_color : None

Node initialization
 - count : count
 - position : position
 - radius : radius
 - node_label : node_label
 - node_color : node_color

## points_to_curves

> PointsToCurves, return single output socket

``` python
def points_to_curves(points=None, curve_group_id=None, weight=None, node_label=None, node_color=None):
```
Node
 - class_name : [PointsToCurves](/docs/GeoNodes_classes/PointsToCurves.md)
 - bl_idname : GeometryNodePointsToCurves

Arguments
 - points : None
 - curve_group_id : None
 - weight : None
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - curve_group_id : curve_group_id
 - weight : weight
 - node_label : node_label
 - node_color : node_color

## points_to_sdf_volume

> PointsToSDFVolume, return single output socket

``` python
def points_to_sdf_volume(points=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [PointsToSDFVolume](/docs/GeoNodes_classes/PointsToSDFVolume.md)
 - bl_idname : GeometryNodePointsToSDFVolume

Arguments
 - points : None
 - voxel_amount : None
 - radius : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - voxel_amount : voxel_amount
 - radius : radius
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

## points_to_vertices

> PointsToVertices, return single output socket

``` python
def points_to_vertices(points=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [PointsToVertices](/docs/GeoNodes_classes/PointsToVertices.md)
 - bl_idname : GeometryNodePointsToVertices

Arguments
 - points : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## points_to_volume

> PointsToVolume, return single output socket

``` python
def points_to_volume(points=None, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):
```
Node
 - class_name : [PointsToVolume](/docs/GeoNodes_classes/PointsToVolume.md)
 - bl_idname : GeometryNodePointsToVolume

Arguments
 - points : None
 - density : None
 - voxel_amount : None
 - radius : None
 - voxel_size : None
 - resolution_mode : 'VOXEL_AMOUNT'
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - density : density
 - voxel_amount : voxel_amount
 - radius : radius
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

## position

> Position, return socket

``` python
def position(node_label=None, node_color=None):
```
Node
 - class_name : [Position](/docs/GeoNodes_classes/Position.md)
 - bl_idname : GeometryNodeInputPosition

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## power

> Math, value=self, operation='POWER'

``` python
def power(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'POWER'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## quadratic_bezier

> QuadraticBezier, return single output socket

``` python
def quadratic_bezier(resolution=None, start=None, middle=None, end=None, node_label=None, node_color=None):
```
Node
 - class_name : [QuadraticBezier](/docs/GeoNodes_classes/QuadraticBezier.md)
 - bl_idname : GeometryNodeCurveQuadraticBezier

Arguments
 - resolution : None
 - start : None
 - middle : None
 - end : None
 - node_label : None
 - node_color : None

Node initialization
 - resolution : resolution
 - start : start
 - middle : middle
 - end : end
 - node_label : node_label
 - node_color : node_color

## quadrilateral

> Quadrilateral, return single output socket

``` python
def quadrilateral(width=None, height=None, offset=None, bottom_width=None, top_width=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', node_label=None, node_color=None):
```
Node
 - class_name : [Quadrilateral](/docs/GeoNodes_classes/Quadrilateral.md)
 - bl_idname : GeometryNodeCurvePrimitiveQuadrilateral

Arguments
 - width : None
 - height : None
 - offset : None
 - bottom_width : None
 - top_width : None
 - bottom_height : None
 - top_height : None
 - point_1 : None
 - point_2 : None
 - point_3 : None
 - point_4 : None
 - mode : 'RECTANGLE'
 - node_label : None
 - node_color : None

Node initialization
 - width : width
 - height : height
 - offset : offset
 - bottom_width : bottom_width
 - top_width : top_width
 - bottom_height : bottom_height
 - top_height : top_height
 - point_1 : point_1
 - point_2 : point_2
 - point_3 : point_3
 - point_4 : point_4
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## quaternion_to_rotation

> QuaternionToRotation, return single output socket

``` python
def quaternion_to_rotation(w=None, x=None, y=None, z=None, node_label=None, node_color=None):
```
Node
 - class_name : [QuaternionToRotation](/docs/GeoNodes_classes/QuaternionToRotation.md)
 - bl_idname : FunctionNodeQuaternionToRotation

Arguments
 - w : None
 - x : None
 - y : None
 - z : None
 - node_label : None
 - node_color : None

Node initialization
 - w : w
 - x : x
 - y : y
 - z : z
 - node_label : node_label
 - node_color : node_color

## radians

> Math, value=self, operation='RADIANS'

``` python
def radians(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'RADIANS'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## radius

> Radius, return socket

``` python
def radius(node_label=None, node_color=None):
```
Node
 - class_name : [Radius](/docs/GeoNodes_classes/Radius.md)
 - bl_idname : GeometryNodeInputRadius

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## random_boolean

> RandomValue, data_type='BOOLEAN'

``` python
def random_boolean(probability=None, ID=None, seed=None, node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/GeoNodes_classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - probability : None
 - ID : None
 - seed : None
 - node_label : None
 - node_color : None

Node initialization
 - probability : probability
 - ID : ID
 - seed : seed
 - data_type : 'BOOLEAN'
 - node_label : node_label
 - node_color : node_color

## random_float

> RandomValue, data_type='FLOAT'

``` python
def random_float(min=None, max=None, ID=None, seed=None, node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/GeoNodes_classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - min : None
 - max : None
 - ID : None
 - seed : None
 - node_label : None
 - node_color : None

Node initialization
 - min : min
 - max : max
 - ID : ID
 - seed : seed
 - data_type : 'FLOAT'
 - node_label : node_label
 - node_color : node_color

## random_int

> RandomValue, data_type='INT'

``` python
def random_int(min=None, max=None, ID=None, seed=None, node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/GeoNodes_classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - min : None
 - max : None
 - ID : None
 - seed : None
 - node_label : None
 - node_color : None

Node initialization
 - min : min
 - max : max
 - ID : ID
 - seed : seed
 - data_type : 'INT'
 - node_label : node_label
 - node_color : node_color

## random_value

> RandomValue, return single output socket

``` python
def random_value(min=None, max=None, ID=None, seed=None, probability=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/GeoNodes_classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - min : None
 - max : None
 - ID : None
 - seed : None
 - probability : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - min : min
 - max : max
 - ID : ID
 - seed : seed
 - probability : probability
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

## random_vector

> RandomValue, data_type='FLOAT_VECTOR'

``` python
def random_vector(min=None, max=None, ID=None, seed=None, node_label=None, node_color=None):
```
Node
 - class_name : [RandomValue](/docs/GeoNodes_classes/RandomValue.md)
 - bl_idname : FunctionNodeRandomValue

Arguments
 - min : None
 - max : None
 - ID : None
 - seed : None
 - node_label : None
 - node_color : None

Node initialization
 - min : min
 - max : max
 - ID : ID
 - seed : seed
 - data_type : 'FLOAT_VECTOR'
 - node_label : node_label
 - node_color : node_color

## realize_instances

> RealizeInstances, return single output socket

``` python
def realize_instances(geometry=None, node_label=None, node_color=None):
```
Node
 - class_name : [RealizeInstances](/docs/GeoNodes_classes/RealizeInstances.md)
 - bl_idname : GeometryNodeRealizeInstances

Arguments
 - geometry : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - node_label : node_label
 - node_color : node_color

## remove_named_attribute

> RemoveNamedAttribute, return single output socket

``` python
def remove_named_attribute(geometry=None, name=None, node_label=None, node_color=None):
```
Node
 - class_name : [RemoveNamedAttribute](/docs/GeoNodes_classes/RemoveNamedAttribute.md)
 - bl_idname : GeometryNodeRemoveAttribute

Arguments
 - geometry : None
 - name : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - name : name
 - node_label : node_label
 - node_color : node_color

## repeat_output

> RepeatOutput, return single output socket

``` python
def repeat_output(geometry=None, active_index=0, active_item=None, inspection_index=0, repeat_items=None, node_label=None, node_color=None):
```
Node
 - class_name : [RepeatOutput](/docs/GeoNodes_classes/RepeatOutput.md)
 - bl_idname : GeometryNodeRepeatOutput

Arguments
 - geometry : None
 - active_index : 0
 - active_item
 - inspection_index : 0
 - repeat_items
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - active_index : active_index
 - active_item : active_item
 - inspection_index : inspection_index
 - repeat_items : repeat_items
 - node_label : node_label
 - node_color : node_color

## replace_material

> ReplaceMaterial, return single output socket

``` python
def replace_material(geometry=None, old=None, new=None, node_label=None, node_color=None):
```
Node
 - class_name : [ReplaceMaterial](/docs/GeoNodes_classes/ReplaceMaterial.md)
 - bl_idname : GeometryNodeReplaceMaterial

Arguments
 - geometry : None
 - old : None
 - new : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - old : old
 - new : new
 - node_label : node_label
 - node_color : node_color

## replace_string

> ReplaceString, return single output socket

``` python
def replace_string(string=None, find=None, replace=None, node_label=None, node_color=None):
```
Node
 - class_name : [ReplaceString](/docs/GeoNodes_classes/ReplaceString.md)
 - bl_idname : FunctionNodeReplaceString

Arguments
 - string : None
 - find : None
 - replace : None
 - node_label : None
 - node_color : None

Node initialization
 - string : string
 - find : find
 - replace : replace
 - node_label : node_label
 - node_color : node_color

## reroute

> Reroute, return single output socket

``` python
def reroute(input=None, node_label=None, node_color=None):
```
Node
 - class_name : [Reroute](/docs/GeoNodes_classes/Reroute.md)
 - bl_idname : NodeReroute

Arguments
 - input : None
 - node_label : None
 - node_color : None

Node initialization
 - input : input
 - node_label : node_label
 - node_color : node_color

## resample_curve

> ResampleCurve, return single output socket

``` python
def resample_curve(curve=None, count=None, length=None, selection=None, mode='COUNT', node_label=None, node_color=None):
```
Node
 - class_name : [ResampleCurve](/docs/GeoNodes_classes/ResampleCurve.md)
 - bl_idname : GeometryNodeResampleCurve

Arguments
 - curve : None
 - count : None
 - length : None
 - selection : None
 - mode : 'COUNT'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - count : count
 - length : length
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## reverse_curve

> ReverseCurve, return single output socket

``` python
def reverse_curve(curve=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [ReverseCurve](/docs/GeoNodes_classes/ReverseCurve.md)
 - bl_idname : GeometryNodeReverseCurve

Arguments
 - curve : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## rgb_curves

> RGBCurves, return single output socket

``` python
def rgb_curves(fac=None, color=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [RGBCurves](/docs/GeoNodes_classes/RGBCurves.md)
 - bl_idname : ShaderNodeRGBCurve

Arguments
 - fac : None
 - color : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - color : color
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## rotate_euler

> RotateEuler, return single output socket

``` python
def rotate_euler(rotation=None, rotate_by=None, space='OBJECT', node_label=None, node_color=None):
```
Node
 - class_name : [RotateEuler](/docs/GeoNodes_classes/RotateEuler.md)
 - bl_idname : FunctionNodeRotateEuler

Arguments
 - rotation : None
 - rotate_by : None
 - space : 'OBJECT'
 - node_label : None
 - node_color : None

Node initialization
 - rotation : rotation
 - rotate_by : rotate_by
 - space : space
 - node_label : node_label
 - node_color : node_color

## rotate_instances

> RotateInstances, return single output socket

``` python
def rotate_instances(instances=None, rotation=None, pivot_point=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [RotateInstances](/docs/GeoNodes_classes/RotateInstances.md)
 - bl_idname : GeometryNodeRotateInstances

Arguments
 - instances : None
 - rotation : None
 - pivot_point : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : instances
 - rotation : rotation
 - pivot_point : pivot_point
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## rotate_vector

> RotateVector, return single output socket

``` python
def rotate_vector(vector=None, rotation=None, node_label=None, node_color=None):
```
Node
 - class_name : [RotateVector](/docs/GeoNodes_classes/RotateVector.md)
 - bl_idname : FunctionNodeRotateVector

Arguments
 - vector : None
 - rotation : None
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - rotation : rotation
 - node_label : node_label
 - node_color : node_color

## rotation_to_euler

> RotationToEuler, return single output socket

``` python
def rotation_to_euler(rotation=None, node_label=None, node_color=None):
```
Node
 - class_name : [RotationToEuler](/docs/GeoNodes_classes/RotationToEuler.md)
 - bl_idname : FunctionNodeRotationToEuler

Arguments
 - rotation : None
 - node_label : None
 - node_color : None

Node initialization
 - rotation : rotation
 - node_label : node_label
 - node_color : node_color

## round

> Math, value=self, operation='ROUND'

``` python
def round(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'ROUND'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## sample_index

> SampleIndex, return single output socket

``` python
def sample_index(geometry=None, value=None, index=None, clamp=False, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleIndex](/docs/GeoNodes_classes/SampleIndex.md)
 - bl_idname : GeometryNodeSampleIndex

Arguments
 - geometry : None
 - value : None
 - index : None
 - clamp : False
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - value : value
 - index : index
 - clamp : clamp
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## sample_nearest

> SampleNearest, return single output socket

``` python
def sample_nearest(geometry=None, sample_position=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleNearest](/docs/GeoNodes_classes/SampleNearest.md)
 - bl_idname : GeometryNodeSampleNearest

Arguments
 - geometry : None
 - sample_position : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - sample_position : sample_position
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## sample_nearest_surface

> SampleNearestSurface, return single output socket

``` python
def sample_nearest_surface(mesh=None, value=None, sample_position=None, data_type='FLOAT', node_label=None, node_color=None):
```
Node
 - class_name : [SampleNearestSurface](/docs/GeoNodes_classes/SampleNearestSurface.md)
 - bl_idname : GeometryNodeSampleNearestSurface

Arguments
 - mesh : None
 - value : None
 - sample_position : None
 - data_type : 'FLOAT'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - value : value
 - sample_position : sample_position
 - data_type : data_type
 - node_label : node_label
 - node_color : node_color

## sample_volume

> SampleVolume, return single output socket

``` python
def sample_volume(volume=None, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR', node_label=None, node_color=None):
```
Node
 - class_name : [SampleVolume](/docs/GeoNodes_classes/SampleVolume.md)
 - bl_idname : GeometryNodeSampleVolume

Arguments
 - volume : None
 - grid : None
 - position : None
 - grid_type : 'FLOAT'
 - interpolation_mode : 'TRILINEAR'
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - grid : grid
 - position : position
 - grid_type : grid_type
 - interpolation_mode : interpolation_mode
 - node_label : node_label
 - node_color : node_color

## scale_elements

> ScaleElements, return single output socket

``` python
def scale_elements(geometry=None, scale=None, center=None, axis=None, selection=None, domain='FACE', scale_mode='UNIFORM', node_label=None, node_color=None):
```
Node
 - class_name : [ScaleElements](/docs/GeoNodes_classes/ScaleElements.md)
 - bl_idname : GeometryNodeScaleElements

Arguments
 - geometry : None
 - scale : None
 - center : None
 - axis : None
 - selection : None
 - domain : 'FACE'
 - scale_mode : 'UNIFORM'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - scale : scale
 - center : center
 - axis : axis
 - selection : self._get_selection(selection)
 - domain : domain
 - scale_mode : scale_mode
 - node_label : node_label
 - node_color : node_color

## scale_instances

> ScaleInstances, return single output socket

``` python
def scale_instances(instances=None, scale=None, center=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [ScaleInstances](/docs/GeoNodes_classes/ScaleInstances.md)
 - bl_idname : GeometryNodeScaleInstances

Arguments
 - instances : None
 - scale : None
 - center : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : instances
 - scale : scale
 - center : center
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## scene_time

> SceneTime, return node

``` python
def scene_time(node_label=None, node_color=None):
```
Node
 - class_name : [SceneTime](/docs/GeoNodes_classes/SceneTime.md)
 - bl_idname : GeometryNodeInputSceneTime

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## sdf_volume_sphere

> SDFVolumeSphere, return single output socket

``` python
def sdf_volume_sphere(radius=None, voxel_size=None, half_band_width=None, node_label=None, node_color=None):
```
Node
 - class_name : [SDFVolumeSphere](/docs/GeoNodes_classes/SDFVolumeSphere.md)
 - bl_idname : GeometryNodeSDFVolumeSphere

Arguments
 - radius : None
 - voxel_size : None
 - half_band_width : None
 - node_label : None
 - node_color : None

Node initialization
 - radius : radius
 - voxel_size : voxel_size
 - half_band_width : half_band_width
 - node_label : node_label
 - node_color : node_color

## selection

> Selection, return socket

``` python
def selection(node_label=None, node_color=None):
```
Node
 - class_name : [Selection](/docs/GeoNodes_classes/Selection.md)
 - bl_idname : GeometryNodeToolSelection

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## self_object

> SelfObject, return socket

``` python
def self_object(node_label=None, node_color=None):
```
Node
 - class_name : [SelfObject](/docs/GeoNodes_classes/SelfObject.md)
 - bl_idname : GeometryNodeSelfObject

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## set_curve_normal

> SetCurveNormal, return single output socket

``` python
def set_curve_normal(curve=None, selection=None, mode='MINIMUM_TWIST', node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveNormal](/docs/GeoNodes_classes/SetCurveNormal.md)
 - bl_idname : GeometryNodeSetCurveNormal

Arguments
 - curve : None
 - selection : None
 - mode : 'MINIMUM_TWIST'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## set_curve_radius

> SetCurveRadius, return single output socket

``` python
def set_curve_radius(curve=None, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveRadius](/docs/GeoNodes_classes/SetCurveRadius.md)
 - bl_idname : GeometryNodeSetCurveRadius

Arguments
 - curve : None
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_curve_tilt

> SetCurveTilt, return single output socket

``` python
def set_curve_tilt(curve=None, tilt=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetCurveTilt](/docs/GeoNodes_classes/SetCurveTilt.md)
 - bl_idname : GeometryNodeSetCurveTilt

Arguments
 - curve : None
 - tilt : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - tilt : tilt
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_face_set

> SetFaceSet, return single output socket

``` python
def set_face_set(mesh=None, face_set=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetFaceSet](/docs/GeoNodes_classes/SetFaceSet.md)
 - bl_idname : GeometryNodeToolSetFaceSet

Arguments
 - mesh : None
 - face_set : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - face_set : face_set
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_handle_positions

> SetHandlePositions, return single output socket

``` python
def set_handle_positions(curve=None, position=None, offset=None, selection=None, mode='LEFT', node_label=None, node_color=None):
```
Node
 - class_name : [SetHandlePositions](/docs/GeoNodes_classes/SetHandlePositions.md)
 - bl_idname : GeometryNodeSetCurveHandlePositions

Arguments
 - curve : None
 - position : None
 - offset : None
 - selection : None
 - mode : 'LEFT'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - position : position
 - offset : offset
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## set_handle_type

> SetHandleType, return single output socket

``` python
def set_handle_type(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):
```
Node
 - class_name : [SetHandleType](/docs/GeoNodes_classes/SetHandleType.md)
 - bl_idname : GeometryNodeCurveSetHandles

Arguments
 - curve : None
 - selection : None
 - handle_type : 'AUTO'
 - mode : {'RIGHT', 'LEFT'}
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - selection : self._get_selection(selection)
 - handle_type : handle_type
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## set_id

> SetID, return single output socket

``` python
def set_id(geometry=None, ID=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetID](/docs/GeoNodes_classes/SetID.md)
 - bl_idname : GeometryNodeSetID

Arguments
 - geometry : None
 - ID : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - ID : ID
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_material

> SetMaterial, return single output socket

``` python
def set_material(geometry=None, material=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetMaterial](/docs/GeoNodes_classes/SetMaterial.md)
 - bl_idname : GeometryNodeSetMaterial

Arguments
 - geometry : None
 - material : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - material : material
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_material_index

> SetMaterialIndex, return single output socket

``` python
def set_material_index(geometry=None, material_index=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetMaterialIndex](/docs/GeoNodes_classes/SetMaterialIndex.md)
 - bl_idname : GeometryNodeSetMaterialIndex

Arguments
 - geometry : None
 - material_index : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - material_index : material_index
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_point_radius

> SetPointRadius, return single output socket

``` python
def set_point_radius(points=None, radius=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetPointRadius](/docs/GeoNodes_classes/SetPointRadius.md)
 - bl_idname : GeometryNodeSetPointRadius

Arguments
 - points : None
 - radius : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - points : points
 - radius : radius
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_position

> SetPosition, return single output socket

``` python
def set_position(geometry=None, position=None, offset=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetPosition](/docs/GeoNodes_classes/SetPosition.md)
 - bl_idname : GeometryNodeSetPosition

Arguments
 - geometry : None
 - position : None
 - offset : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - position : position
 - offset : offset
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_selection

> SetSelection, return single output socket

``` python
def set_selection(geometry=None, selection=None, domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [SetSelection](/docs/GeoNodes_classes/SetSelection.md)
 - bl_idname : GeometryNodeToolSetSelection

Arguments
 - geometry : None
 - selection : None
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## set_shade_smooth

> SetShadeSmooth, return single output socket

``` python
def set_shade_smooth(geometry=None, shade_smooth=None, selection=None, domain='FACE', node_label=None, node_color=None):
```
Node
 - class_name : [SetShadeSmooth](/docs/GeoNodes_classes/SetShadeSmooth.md)
 - bl_idname : GeometryNodeSetShadeSmooth

Arguments
 - geometry : None
 - shade_smooth : None
 - selection : None
 - domain : 'FACE'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - shade_smooth : shade_smooth
 - selection : self._get_selection(selection)
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## set_spline_cyclic

> SetSplineCyclic, return single output socket

``` python
def set_spline_cyclic(geometry=None, cyclic=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineCyclic](/docs/GeoNodes_classes/SetSplineCyclic.md)
 - bl_idname : GeometryNodeSetSplineCyclic

Arguments
 - geometry : None
 - cyclic : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - cyclic : cyclic
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_spline_resolution

> SetSplineResolution, return single output socket

``` python
def set_spline_resolution(geometry=None, resolution=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineResolution](/docs/GeoNodes_classes/SetSplineResolution.md)
 - bl_idname : GeometryNodeSetSplineResolution

Arguments
 - geometry : None
 - resolution : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - resolution : resolution
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## set_spline_type

> SetSplineType, return single output socket

``` python
def set_spline_type(curve=None, selection=None, spline_type='POLY', node_label=None, node_color=None):
```
Node
 - class_name : [SetSplineType](/docs/GeoNodes_classes/SetSplineType.md)
 - bl_idname : GeometryNodeCurveSplineType

Arguments
 - curve : None
 - selection : None
 - spline_type : 'POLY'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - selection : self._get_selection(selection)
 - spline_type : spline_type
 - node_label : node_label
 - node_color : node_color

## sign

> Math, value=self, operation='SIGN'

``` python
def sign(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SIGN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## signed_distance

> SignedDistance, return socket

``` python
def signed_distance(node_label=None, node_color=None):
```
Node
 - class_name : [SignedDistance](/docs/GeoNodes_classes/SignedDistance.md)
 - bl_idname : GeometryNodeInputSignedDistance

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## simulation_output

> SimulationOutput, return single output socket

``` python
def simulation_output(skip=None, geometry=None, active_index=0, active_item=None, state_items=None, node_label=None, node_color=None):
```
Node
 - class_name : [SimulationOutput](/docs/GeoNodes_classes/SimulationOutput.md)
 - bl_idname : GeometryNodeSimulationOutput

Arguments
 - skip : None
 - geometry : None
 - active_index : 0
 - active_item
 - state_items
 - node_label : None
 - node_color : None

Node initialization
 - skip : skip
 - geometry : geometry
 - active_index : active_index
 - active_item : active_item
 - state_items : state_items
 - node_label : node_label
 - node_color : node_color

## sin

> Math, value=self, operation='SINE'

``` python
def sin(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SINE'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## sinh

> Math, value=self, operation='SINH'

``` python
def sinh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SINH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## slice_string

> SliceString, return single output socket

``` python
def slice_string(string=None, position=None, length=None, node_label=None, node_color=None):
```
Node
 - class_name : [SliceString](/docs/GeoNodes_classes/SliceString.md)
 - bl_idname : FunctionNodeSliceString

Arguments
 - string : None
 - position : None
 - length : None
 - node_label : None
 - node_color : None

Node initialization
 - string : string
 - position : position
 - length : length
 - node_label : node_label
 - node_color : node_color

## smooth_max

> Math, value=self, operation='SMOOTH_MAX'

``` python
def smooth_max(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'SMOOTH_MAX'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## smooth_min

> Math, value=self, operation='SMOOTH_MIN'

``` python
def smooth_min(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'SMOOTH_MIN'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## snap

> Math, value=self, operation='SNAP'

``` python
def snap(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'SNAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## special_characters

> SpecialCharacters, return node

``` python
def special_characters(node_label=None, node_color=None):
```
Node
 - class_name : [SpecialCharacters](/docs/GeoNodes_classes/SpecialCharacters.md)
 - bl_idname : FunctionNodeInputSpecialCharacters

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## spiral

> Spiral, return single output socket

``` python
def spiral(resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, node_label=None, node_color=None):
```
Node
 - class_name : [Spiral](/docs/GeoNodes_classes/Spiral.md)
 - bl_idname : GeometryNodeCurveSpiral

Arguments
 - resolution : None
 - rotations : None
 - start_radius : None
 - end_radius : None
 - height : None
 - reverse : None
 - node_label : None
 - node_color : None

Node initialization
 - resolution : resolution
 - rotations : rotations
 - start_radius : start_radius
 - end_radius : end_radius
 - height : height
 - reverse : reverse
 - node_label : node_label
 - node_color : node_color

## spline_length

> SplineLength, return node

``` python
def spline_length(node_label=None, node_color=None):
```
Node
 - class_name : [SplineLength](/docs/GeoNodes_classes/SplineLength.md)
 - bl_idname : GeometryNodeSplineLength

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## spline_parameter

> SplineParameter, return node

``` python
def spline_parameter(node_label=None, node_color=None):
```
Node
 - class_name : [SplineParameter](/docs/GeoNodes_classes/SplineParameter.md)
 - bl_idname : GeometryNodeSplineParameter

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## spline_resolution

> SplineResolution, return socket

``` python
def spline_resolution(node_label=None, node_color=None):
```
Node
 - class_name : [SplineResolution](/docs/GeoNodes_classes/SplineResolution.md)
 - bl_idname : GeometryNodeInputSplineResolution

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## split_edges

> SplitEdges, return single output socket

``` python
def split_edges(mesh=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [SplitEdges](/docs/GeoNodes_classes/SplitEdges.md)
 - bl_idname : GeometryNodeSplitEdges

Arguments
 - mesh : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## sqrt

> Math, value=self, operation='SQRT'

``` python
def sqrt(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'SQRT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## store_named_attribute

> StoreNamedAttribute, return single output socket

``` python
def store_named_attribute(geometry=None, name=None, value=None, selection=None, data_type='FLOAT', domain='POINT', node_label=None, node_color=None):
```
Node
 - class_name : [StoreNamedAttribute](/docs/GeoNodes_classes/StoreNamedAttribute.md)
 - bl_idname : GeometryNodeStoreNamedAttribute

Arguments
 - geometry : None
 - name : None
 - value : None
 - selection : None
 - data_type : 'FLOAT'
 - domain : 'POINT'
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - name : name
 - value : value
 - selection : self._get_selection(selection)
 - data_type : data_type
 - domain : domain
 - node_label : node_label
 - node_color : node_color

## string

> String, return socket

``` python
def string(string, node_label=None, node_color=None):
```
Node
 - class_name : [String](/docs/GeoNodes_classes/String.md)
 - bl_idname : FunctionNodeInputString

## string_length

> StringLength, return single output socket

``` python
def string_length(string=None, node_label=None, node_color=None):
```
Node
 - class_name : [StringLength](/docs/GeoNodes_classes/StringLength.md)
 - bl_idname : FunctionNodeStringLength

Arguments
 - string : None
 - node_label : None
 - node_color : None

Node initialization
 - string : string
 - node_label : node_label
 - node_color : node_color

## subdivide_curve

> SubdivideCurve, return single output socket

``` python
def subdivide_curve(curve=None, cuts=None, node_label=None, node_color=None):
```
Node
 - class_name : [SubdivideCurve](/docs/GeoNodes_classes/SubdivideCurve.md)
 - bl_idname : GeometryNodeSubdivideCurve

Arguments
 - curve : None
 - cuts : None
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - cuts : cuts
 - node_label : node_label
 - node_color : node_color

## subdivide_mesh

> SubdivideMesh, return single output socket

``` python
def subdivide_mesh(mesh=None, level=None, node_label=None, node_color=None):
```
Node
 - class_name : [SubdivideMesh](/docs/GeoNodes_classes/SubdivideMesh.md)
 - bl_idname : GeometryNodeSubdivideMesh

Arguments
 - mesh : None
 - level : None
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - level : level
 - node_label : node_label
 - node_color : node_color

## subdivision_surface

> SubdivisionSurface, return single output socket

``` python
def subdivision_surface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', node_label=None, node_color=None):
```
Node
 - class_name : [SubdivisionSurface](/docs/GeoNodes_classes/SubdivisionSurface.md)
 - bl_idname : GeometryNodeSubdivisionSurface

Arguments
 - mesh : None
 - level : None
 - edge_crease : None
 - vertex_crease : None
 - boundary_smooth : 'ALL'
 - uv_smooth : 'PRESERVE_BOUNDARIES'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - level : level
 - edge_crease : edge_crease
 - vertex_crease : vertex_crease
 - boundary_smooth : boundary_smooth
 - uv_smooth : uv_smooth
 - node_label : node_label
 - node_color : node_color

## subtract

> Math, value=self, operation='SUBTRACT'

``` python
def subtract(value=None, value_1=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - operation : 'SUBTRACT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## switch

> Switch, return single output socket

``` python
def switch(switch=None, false=None, true=None, input_type='GEOMETRY', node_label=None, node_color=None):
```
Node
 - class_name : [Switch](/docs/GeoNodes_classes/Switch.md)
 - bl_idname : GeometryNodeSwitch

Arguments
 - switch : None
 - false : None
 - true : None
 - input_type : 'GEOMETRY'
 - node_label : None
 - node_color : None

Node initialization
 - switch : switch
 - false : false
 - true : true
 - input_type : input_type
 - node_label : node_label
 - node_color : node_color

## tan

> Math, value=self, operation='TANGENT'

``` python
def tan(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TANGENT'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## tanh

> Math, value=self, operation='TANH'

``` python
def tanh(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TANH'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## transform_geometry

> TransformGeometry, return single output socket

``` python
def transform_geometry(geometry=None, translation=None, rotation=None, scale=None, node_label=None, node_color=None):
```
Node
 - class_name : [TransformGeometry](/docs/GeoNodes_classes/TransformGeometry.md)
 - bl_idname : GeometryNodeTransform

Arguments
 - geometry : None
 - translation : None
 - rotation : None
 - scale : None
 - node_label : None
 - node_color : None

Node initialization
 - geometry : geometry
 - translation : translation
 - rotation : rotation
 - scale : scale
 - node_label : node_label
 - node_color : node_color

## translate_instances

> TranslateInstances, return single output socket

``` python
def translate_instances(instances=None, translation=None, local_space=None, selection=None, node_label=None, node_color=None):
```
Node
 - class_name : [TranslateInstances](/docs/GeoNodes_classes/TranslateInstances.md)
 - bl_idname : GeometryNodeTranslateInstances

Arguments
 - instances : None
 - translation : None
 - local_space : None
 - selection : None
 - node_label : None
 - node_color : None

Node initialization
 - instances : instances
 - translation : translation
 - local_space : local_space
 - selection : self._get_selection(selection)
 - node_label : node_label
 - node_color : node_color

## triangulate

> Triangulate, return single output socket

``` python
def triangulate(mesh=None, minimum_vertices=None, selection=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', node_label=None, node_color=None):
```
Node
 - class_name : [Triangulate](/docs/GeoNodes_classes/Triangulate.md)
 - bl_idname : GeometryNodeTriangulate

Arguments
 - mesh : None
 - minimum_vertices : None
 - selection : None
 - ngon_method : 'BEAUTY'
 - quad_method : 'SHORTEST_DIAGONAL'
 - node_label : None
 - node_color : None

Node initialization
 - mesh : mesh
 - minimum_vertices : minimum_vertices
 - selection : self._get_selection(selection)
 - ngon_method : ngon_method
 - quad_method : quad_method
 - node_label : node_label
 - node_color : node_color

## trim_curve

> TrimCurve, return single output socket

``` python
def trim_curve(curve=None, start=None, end=None, selection=None, mode='FACTOR', node_label=None, node_color=None):
```
Node
 - class_name : [TrimCurve](/docs/GeoNodes_classes/TrimCurve.md)
 - bl_idname : GeometryNodeTrimCurve

Arguments
 - curve : None
 - start : None
 - end : None
 - selection : None
 - mode : 'FACTOR'
 - node_label : None
 - node_color : None

Node initialization
 - curve : curve
 - start : start
 - end : end
 - selection : self._get_selection(selection)
 - mode : mode
 - node_label : node_label
 - node_color : node_color

## trunc

> Math, value=self, operation='TRUNC'

``` python
def trunc(value=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - operation : 'TRUNC'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## uv_unwrap

> UVUnwrap, return single output socket

``` python
def uv_unwrap(seam=None, margin=None, fill_holes=None, selection=None, method='ANGLE_BASED', node_label=None, node_color=None):
```
Node
 - class_name : [UVUnwrap](/docs/GeoNodes_classes/UVUnwrap.md)
 - bl_idname : GeometryNodeUVUnwrap

Arguments
 - seam : None
 - margin : None
 - fill_holes : None
 - selection : None
 - method : 'ANGLE_BASED'
 - node_label : None
 - node_color : None

Node initialization
 - seam : seam
 - margin : margin
 - fill_holes : fill_holes
 - selection : self._get_selection(selection)
 - method : method
 - node_label : node_label
 - node_color : node_color

## value

> Value, return socket

``` python
def value(value, node_label=None, node_color=None):
```
Node
 - class_name : [Value](/docs/GeoNodes_classes/Value.md)
 - bl_idname : ShaderNodeValue

## value_to_string

> ValueToString, return single output socket

``` python
def value_to_string(value=None, decimals=None, node_label=None, node_color=None):
```
Node
 - class_name : [ValueToString](/docs/GeoNodes_classes/ValueToString.md)
 - bl_idname : FunctionNodeValueToString

Arguments
 - value : None
 - decimals : None
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - decimals : decimals
 - node_label : node_label
 - node_color : node_color

## vector

> Vector, return socket

``` python
def vector(vector, node_label=None, node_color=None):
```
Node
 - class_name : [Vector](/docs/GeoNodes_classes/Vector.md)
 - bl_idname : FunctionNodeInputVector

## vector_curves

> VectorCurves, return single output socket

``` python
def vector_curves(fac=None, vector=None, mapping=None, node_label=None, node_color=None):
```
Node
 - class_name : [VectorCurves](/docs/GeoNodes_classes/VectorCurves.md)
 - bl_idname : ShaderNodeVectorCurve

Arguments
 - fac : None
 - vector : None
 - mapping
 - node_label : None
 - node_color : None

Node initialization
 - fac : fac
 - vector : vector
 - mapping : mapping
 - node_label : node_label
 - node_color : node_color

## vector_rotate

> VectorRotate, return single output socket

``` python
def vector_rotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', node_label=None, node_color=None):
```
Node
 - class_name : [VectorRotate](/docs/GeoNodes_classes/VectorRotate.md)
 - bl_idname : ShaderNodeVectorRotate

Arguments
 - vector : None
 - center : None
 - axis : None
 - angle : None
 - rotation : None
 - invert : False
 - rotation_type : 'AXIS_ANGLE'
 - node_label : None
 - node_color : None

Node initialization
 - vector : vector
 - center : center
 - axis : axis
 - angle : angle
 - rotation : rotation
 - invert : invert
 - rotation_type : rotation_type
 - node_label : node_label
 - node_color : node_color

## vertex_neighbors

> VertexNeighbors, return node

``` python
def vertex_neighbors(node_label=None, node_color=None):
```
Node
 - class_name : [VertexNeighbors](/docs/GeoNodes_classes/VertexNeighbors.md)
 - bl_idname : GeometryNodeInputMeshVertexNeighbors

Arguments
 - node_label : None
 - node_color : None

Node initialization
 - node_label : node_label
 - node_color : node_color

## vertex_of_corner

> VertexOfCorner, return single output socket

``` python
def vertex_of_corner(corner_index=None, node_label=None, node_color=None):
```
Node
 - class_name : [VertexOfCorner](/docs/GeoNodes_classes/VertexOfCorner.md)
 - bl_idname : GeometryNodeVertexOfCorner

Arguments
 - corner_index : None
 - node_label : None
 - node_color : None

Node initialization
 - corner_index : corner_index
 - node_label : node_label
 - node_color : node_color

## volume_cube

> VolumeCube, return single output socket

``` python
def volume_cube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None, node_label=None, node_color=None):
```
Node
 - class_name : [VolumeCube](/docs/GeoNodes_classes/VolumeCube.md)
 - bl_idname : GeometryNodeVolumeCube

Arguments
 - density : None
 - background : None
 - min : None
 - max : None
 - resolution_x : None
 - resolution_y : None
 - resolution_z : None
 - node_label : None
 - node_color : None

Node initialization
 - density : density
 - background : background
 - min : min
 - max : max
 - resolution_x : resolution_x
 - resolution_y : resolution_y
 - resolution_z : resolution_z
 - node_label : node_label
 - node_color : node_color

## volume_to_mesh

> VolumeToMesh, return single output socket

``` python
def volume_to_mesh(volume=None, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None):
```
Node
 - class_name : [VolumeToMesh](/docs/GeoNodes_classes/VolumeToMesh.md)
 - bl_idname : GeometryNodeVolumeToMesh

Arguments
 - volume : None
 - threshold : None
 - adaptivity : None
 - voxel_amount : None
 - voxel_size : None
 - resolution_mode : 'GRID'
 - node_label : None
 - node_color : None

Node initialization
 - volume : volume
 - threshold : threshold
 - adaptivity : adaptivity
 - voxel_amount : voxel_amount
 - voxel_size : voxel_size
 - resolution_mode : resolution_mode
 - node_label : node_label
 - node_color : node_color

## wrap

> Math, value=self, operation='WRAP'

``` python
def wrap(value=None, value_1=None, value_2=None, use_clamp=False, node_label=None, node_color=None):
```
Node
 - class_name : [Math](/docs/GeoNodes_classes/Math.md)
 - bl_idname : ShaderNodeMath

Arguments
 - value : None
 - value_1 : None
 - value_2 : None
 - use_clamp : False
 - node_label : None
 - node_color : None

Node initialization
 - value : value
 - value_1 : value_1
 - value_2 : value_2
 - operation : 'WRAP'
 - use_clamp : use_clamp
 - node_label : node_label
 - node_color : node_color

## xnor

> BooleanMath, boolean=self, operation='XNOR'

``` python
def xnor(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'XNOR'
 - node_label : node_label
 - node_color : node_color

## xor

> BooleanMath, boolean=self, operation='XOR'

``` python
def xor(boolean=None, boolean_1=None, node_label=None, node_color=None):
```
Node
 - class_name : [BooleanMath](/docs/GeoNodes_classes/BooleanMath.md)
 - bl_idname : FunctionNodeBooleanMath

Arguments
 - boolean : None
 - boolean_1 : None
 - node_label : None
 - node_color : None

Node initialization
 - boolean : boolean
 - boolean_1 : boolean_1
 - operation : 'XOR'
 - node_label : node_label
 - node_color : node_color
