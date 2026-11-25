# Geometry Nodes cross reference

This lookup reflects the checked-in `generation2` output. Use public socket
classes and `nd` inside the corresponding active tree. Inherited methods may
also be available on specialized socket classes.

## 3D Cursor

Blender identifier: `GeometryNodeTool3DCursor`

### nd

- `nd._3d_cursor(cls)` — class method; returns `OUT`.

## Accumulate Field

Blender identifier: `GeometryNodeAccumulateField`

### nd

- `nd.accumulate_field(cls, value: Socket=None, group_id: Integer=None, data_type: T_DATA_TYPE_1='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Face

- `Face.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Corner

- `Corner.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.accumulate_field(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

## Active Camera

Blender identifier: `GeometryNodeInputActiveCamera`

### nd

- `nd.active_camera(cls)` — property; returns `OUT`.

### Object

- `Object.ActiveCamera(cls)` — class method; returns `OUT`.

## Active Element

Blender identifier: `GeometryNodeToolActiveElement`

### nd

- `nd.active_element(cls, domain: T_DOMAIN_2='POINT')` — class method; returns `OUT`.

## Advect Grid

Blender identifier: `GeometryNodeGridAdvect`

### nd

- `nd.advect_grid(cls, grid: Socket=None, velocity: Vector=None, time_step: Float=None, integration_scheme: Menu=None, limiter: Menu=None, data_type: T_DATA_TYPE_2='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.advect_grid(self, velocity: Vector=None, time_step: Float=None, integration_scheme: Menu=None, limiter: Menu=None)` — method; returns `OUT`.

### Integer

- `Integer.advect_grid(self, velocity: Vector=None, time_step: Float=None, integration_scheme: Menu=None, limiter: Menu=None)` — method; returns `OUT`.

### Vector

- `Vector.advect_grid(self, velocity: Vector=None, time_step: Float=None, integration_scheme: Menu=None, limiter: Menu=None)` — method; returns `OUT`.

## Align Rotation to Vector

Blender identifier: `FunctionNodeAlignRotationToVector`

### nd

- `nd.align_rotation_to_vector(cls, rotation: Rotation=None, vector: Vector=None, factor: Float=None, axis: T_AXIS_1='Z', pivot_axis: T_PIVOT_AXIS_1='AUTO')` — class method; returns `OUT`.

### Vector

- `Vector.align_to_vector(cls, rotation: Rotation=None, vector: Vector=None, factor: Float=None, axis: T_AXIS_1='Z', pivot_axis: T_PIVOT_AXIS_1='AUTO')` — class method; returns `OUT`.

### Rotation

- `Rotation.align_to_vector(self, vector: Vector=None, factor: Float=None, axis: T_AXIS_1='Z', pivot_axis: T_PIVOT_AXIS_1='AUTO')` — method; returns `OUT`.
- `Rotation.align_x_to_vector(self, vector: Vector=None, factor: Float=None, pivot_axis: T_PIVOT_AXIS_1='AUTO')` — method; returns `OUT`.
- `Rotation.align_y_to_vector(self, vector: Vector=None, factor: Float=None, pivot_axis: T_PIVOT_AXIS_1='AUTO')` — method; returns `OUT`.
- `Rotation.align_z_to_vector(self, vector: Vector=None, factor: Float=None, pivot_axis: T_PIVOT_AXIS_1='AUTO')` — method; returns `OUT`.

## Arc

Blender identifier: `GeometryNodeCurveArc`

### nd

- `nd.arc(cls, resolution: Integer=None, start: Vector=None, middle: Vector=None, end: Vector=None, radius: Float=None, start_angle: Float=None, sweep_angle: Float=None, offset_angle: Float=None, connect_center: Boolean=None, invert_arc: Boolean=None, mode: T_MODE_1='RADIUS')` — class method; returns `OUT`.

### Curve

- `Curve.Arc(cls, resolution: Integer=None, start: Vector=None, middle: Vector=None, end: Vector=None, radius: Float=None, start_angle: Float=None, sweep_angle: Float=None, offset_angle: Float=None, connect_center: Boolean=None, invert_arc: Boolean=None, mode: T_MODE_1='RADIUS')` — class method; returns `OUT`.

## Attribute Statistic

Blender identifier: `GeometryNodeAttributeStatistic`

### nd

- `nd.attribute_statistic(cls, geometry: Geometry=None, selection: Boolean=None, attribute: Socket=None, data_type: T_DATA_TYPE_3='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Edge

- `Edge.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Face

- `Face.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Corner

- `Corner.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Spline

- `Spline.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Instance

- `Instance.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

### Layer

- `Layer.attribute_statistic(self, attribute: Socket=None)` — method; returns `OUT`.

## Axes to Rotation

Blender identifier: `FunctionNodeAxesToRotation`

### nd

- `nd.axes_to_rotation(cls, primary_axis_1: Vector=None, secondary_axis_1: Vector=None, primary_axis: T_AXIS_1='Z', secondary_axis: T_AXIS_1='X')` — class method; returns `OUT`.

### Rotation

- `Rotation.FromAxes(cls, primary_axis_1: Vector=None, secondary_axis_1: Vector=None, primary_axis: T_AXIS_1='Z', secondary_axis: T_AXIS_1='X')` — class method; returns `OUT`.

## Axis Angle to Rotation

Blender identifier: `FunctionNodeAxisAngleToRotation`

### nd

- `nd.axis_angle_to_rotation(cls, axis: Vector=None, angle: Float=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.FromAxisAngle(cls, axis: Vector=None, angle: Float=None)` — class method; returns `OUT`.

## Bake

Blender identifier: `GeometryNodeBake`

### nd

- `nd.bake(cls, named_sockets: dict={}, **sockets)` — class method; returns `OUT`.

## Bit Math

Blender identifier: `FunctionNodeBitMath`

### nd

- `nd.bit_math(cls, a: Integer=None, b: Integer=None, shift: Integer=None, operation: T_OPERATION_1='AND')` — class method; returns `OUT`.

### gnmath

- `gnmath.bw_and(a: Integer=None, b: Integer=None)` — method; returns `OUT`.
- `gnmath.bw_or(a: Integer=None, b: Integer=None)` — method; returns `OUT`.
- `gnmath.bw_xor(a: Integer=None, b: Integer=None)` — method; returns `OUT`.
- `gnmath.bw_shift(a: Integer=None, shift: Integer=None)` — method; returns `OUT`.
- `gnmath.bw_not(a: Integer=None)` — method; returns `OUT`.
- `gnmath.bw_rotate(a: Integer=None, shift: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.bw_and(self, b: Integer=None)` — method; returns `OUT`.
- `Integer.__and__(self, other)` — method; returns `OUT`.
- `Integer.__rand__(self, other)` — method; returns `OUT`.
- `Integer.__iand__(self, other)` — method; returns `OUT`.
- `Integer.bw_or(self, b: Integer=None)` — method; returns `OUT`.
- `Integer.__or__(self, other)` — method; returns `OUT`.
- `Integer.__ror__(self, other)` — method; returns `OUT`.
- `Integer.__ior__(self, other)` — method; returns `OUT`.
- `Integer.bw_xor(self, b: Integer=None)` — method; returns `OUT`.
- `Integer.__xor__(self, other)` — method; returns `OUT`.
- `Integer.__rxor__(self, other)` — method; returns `OUT`.
- `Integer.__ixor__(self, other)` — method; returns `OUT`.
- `Integer.bw_shift(self, shift: Integer=None)` — method; returns `OUT`.
- `Integer.__lshift__(self, other)` — method; returns `OUT`.
- `Integer.__rlshift__(self, other)` — method; returns `OUT`.
- `Integer.__ilshift__(self, other)` — method; returns `OUT`.
- `Integer.__rshift__(self, other)` — method; returns `OUT`.
- `Integer.__rrshift__(self, other)` — method; returns `OUT`.
- `Integer.__irshift__(self, other)` — method; returns `OUT`.
- `Integer.bw_not(self)` — method; returns `OUT`.
- `Integer.__invert__(self)` — method; returns `OUT`.
- `Integer.bw_rotate(self, shift: Integer=None)` — method; returns `OUT`.
- `Integer.bit_math(self, b: Integer=None, shift: Integer=None, operation: T_OPERATION_1='AND')` — method; returns `OUT`.

## Blackbody

Blender identifier: `ShaderNodeBlackbody`

### nd

- `nd.blackbody(cls, temperature: Float=None)` — class method; returns `OUT`.

### Color

- `Color.Blackbody(cls, temperature: Float=None)` — class method; returns `OUT`.

## Blur Attribute

Blender identifier: `GeometryNodeBlurAttribute`

### nd

- `nd.blur_attribute(cls, value: Socket=None, iterations: Integer=None, weight: Float=None, data_type: T_DATA_TYPE_4='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.blur_attribute(self, iterations: Integer=None, weight: Float=None)` — method; returns `OUT`.

### Integer

- `Integer.blur_attribute(self, iterations: Integer=None, weight: Float=None)` — method; returns `OUT`.

### Vector

- `Vector.blur_attribute(self, iterations: Integer=None, weight: Float=None)` — method; returns `OUT`.

### Color

- `Color.blur_attribute(self, iterations: Integer=None, weight: Float=None)` — method; returns `OUT`.

## Bone Info

Blender identifier: `GeometryNodeBoneInfo`

### nd

- `nd.bone_info(cls, armature: Object=None, bone_name: String=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — class method; returns `OUT`.

### Object

- `Object.bone_info(self, bone_name: String=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — method; returns `OUT`.

## Boolean

Blender identifier: `FunctionNodeInputBool`

### nd

- `nd.boolean(cls, boolean: bool=False)` — class method; returns `OUT`.

## Boolean Math

Blender identifier: `FunctionNodeBooleanMath`

### nd

- `nd.boolean_math(cls, boolean: Boolean=None, boolean_1: Boolean=None, operation: T_OPERATION_2='AND')` — class method; returns `OUT`.

### gnmath

- `gnmath.band(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.bor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.xor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.bnot(boolean: Boolean=None)` — method; returns `OUT`.
- `gnmath.not_and(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.nor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.xnor(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.imply(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.
- `gnmath.nimply(boolean: Boolean=None, boolean_1: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.band(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__and__(self, other)` — method; returns `OUT`.
- `Boolean.__rand__(self, other)` — method; returns `OUT`.
- `Boolean.__iand__(self, other)` — method; returns `OUT`.
- `Boolean.__mul__(self, other)` — method; returns `OUT`.
- `Boolean.__rmul__(self, other)` — method; returns `OUT`.
- `Boolean.__imul__(self, other)` — method; returns `OUT`.
- `Boolean.bor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__or__(self, other)` — method; returns `OUT`.
- `Boolean.__ror__(self, other)` — method; returns `OUT`.
- `Boolean.__ior__(self, other)` — method; returns `OUT`.
- `Boolean.__add__(self, other)` — method; returns `OUT`.
- `Boolean.__radd__(self, other)` — method; returns `OUT`.
- `Boolean.__iadd__(self, other)` — method; returns `OUT`.
- `Boolean.xor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.__xor__(self, other)` — method; returns `OUT`.
- `Boolean.__rxor__(self, other)` — method; returns `OUT`.
- `Boolean.__ixor__(self, other)` — method; returns `OUT`.
- `Boolean.__sub__(self, other)` — method; returns `OUT`.
- `Boolean.__rsub__(self, other)` — method; returns `OUT`.
- `Boolean.__isub__(self, other)` — method; returns `OUT`.
- `Boolean.bnot(self)` — method; returns `OUT`.
- `Boolean.__neg__(self)` — method; returns `OUT`.
- `Boolean.__invert__(self)` — method; returns `OUT`.
- `Boolean.not_and(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.nor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.xnor(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.imply(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.nimply(self, boolean: Boolean=None)` — method; returns `OUT`.
- `Boolean.boolean_math(self, boolean: Boolean=None, operation: T_OPERATION_2='AND')` — method; returns `OUT`.

## Bounding Box

Blender identifier: `GeometryNodeBoundBox`

### nd

- `nd.bounding_box(cls, geometry: Geometry=None, use_radius: Boolean=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.bounding_box(self, use_radius: Boolean=None)` — method; returns `OUT`.

## Brick Texture

Blender identifier: `ShaderNodeTexBrick`

### nd

- `nd.brick_texture(cls, vector: Vector=None, color1: Color=None, color2: Color=None, mortar: Color=None, scale: Float=None, mortar_size: Float=None, mortar_smooth: Float=None, bias: Float=None, brick_width: Float=None, row_height: Float=None, offset_frequency: int=2, squash_frequency: int=2, offset: float=0.5, squash: float=1.0)` — class method; returns `OUT`.

### Texture

- `Texture.Brick(cls, vector: Vector=None, color1: Color=None, color2: Color=None, mortar: Color=None, scale: Float=None, mortar_size: Float=None, mortar_smooth: Float=None, bias: Float=None, brick_width: Float=None, row_height: Float=None, offset_frequency: int=2, squash_frequency: int=2, offset: float=0.5, squash: float=1.0)` — class method; returns `OUT`.

## Bézier Segment

Blender identifier: `GeometryNodeCurvePrimitiveBezierSegment`

### nd

- `nd.bezier_segment(cls, resolution: Integer=None, start: Vector=None, start_handle: Vector=None, end_handle: Vector=None, end: Vector=None, mode: T_MODE_2='POSITION')` — class method; returns `OUT`.

### Curve

- `Curve.BezierSegment(cls, resolution: Integer=None, start: Vector=None, start_handle: Vector=None, end_handle: Vector=None, end: Vector=None, mode: T_MODE_2='POSITION')` — class method; returns `OUT`.

## Camera Info

Blender identifier: `GeometryNodeCameraInfo`

### nd

- `nd.camera_info(cls, camera: Object=None)` — class method; returns `OUT`.

### Object

- `Object.camera_info(self)` — method; returns `OUT`.

## Capture Attribute

Blender identifier: `GeometryNodeCaptureAttribute`

### nd

- `nd.capture_attribute(cls, geometry: Geometry=None, selection: Boolean=None, named_sockets: dict={}, domain: T_DOMAIN_1='POINT', **sockets)` — class method; returns `OUT`.

## Checker Texture

Blender identifier: `ShaderNodeTexChecker`

### nd

- `nd.checker_texture(cls, vector: Vector=None, color1: Color=None, color2: Color=None, scale: Float=None)` — class method; returns `OUT`.

### Texture

- `Texture.Checker(cls, vector: Vector=None, color1: Color=None, color2: Color=None, scale: Float=None)` — class method; returns `OUT`.

## Clamp

Blender identifier: `ShaderNodeClamp`

### nd

- `nd.clamp(cls, value: Float=None, min: Float=None, max: Float=None, clamp_type: T_CLAMP_TYPE_1='MINMAX')` — class method; returns `OUT`.

### Float

- `Float.clamp(self, min: Float=None, max: Float=None, clamp_type: T_CLAMP_TYPE_1='MINMAX')` — method; returns `OUT`.

## Clip Grid

Blender identifier: `GeometryNodeGridClip`

### nd

- `nd.clip_grid(cls, grid: Socket=None, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None, max_x: Integer=None, max_y: Integer=None, max_z: Integer=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.clip_grid(self, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None, max_x: Integer=None, max_y: Integer=None, max_z: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.clip_grid(self, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None, max_x: Integer=None, max_y: Integer=None, max_z: Integer=None)` — method; returns `OUT`.

### Boolean

- `Boolean.clip_grid(self, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None, max_x: Integer=None, max_y: Integer=None, max_z: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.clip_grid(self, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None, max_x: Integer=None, max_y: Integer=None, max_z: Integer=None)` — method; returns `OUT`.

## Closure Input

Blender identifier: `NodeClosureInput`

### nd

- `nd.closure_input(cls)` — class method; returns `OUT`.

## Closure Output

Blender identifier: `NodeClosureOutput`

### nd

- `nd.closure_output(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

## Closure to List

Blender identifier: `GeometryNodeClosureToList`

### nd

- `nd.closure_to_list(cls, count: Integer=None, closure: Closure=None)` — class method; returns `OUT`.

### Integer

- `Integer.closure_to_list(self, closure: Closure=None)` — method; returns `OUT`.

## Cluster by Connected

Blender identifier: `GeometryNodeClusterByConnected`

### nd

- `nd.cluster_by_connected(cls, selection: Boolean=None, position: Vector=None, distance: Float=None)` — class method; returns `OUT`.

### Boolean

- `Boolean.cluster_by_connected(self, position: Vector=None, distance: Float=None)` — method; returns `OUT`.

## Cluster by Distance

Blender identifier: `GeometryNodeClusterByDistance`

### nd

- `nd.cluster_by_distance(cls, selection: Boolean=None, group_id: Integer=None, position: Vector=None, distance: Float=None)` — class method; returns `OUT`.

### Boolean

- `Boolean.cluster_by_distance(self, group_id: Integer=None, position: Vector=None, distance: Float=None)` — method; returns `OUT`.

## Collection

Blender identifier: `GeometryNodeInputCollection`

### nd

- `nd.collection(cls, collection=None)` — class method; returns `OUT`.

## Collection Children

Blender identifier: `GeometryNodeCollectionChildren`

### nd

- `nd.collection_children(cls, collection: Collection=None, recursive: Boolean=None)` — class method; returns `OUT`.

### Collection

- `Collection.collection_children(self, recursive: Boolean=None)` — method; returns `OUT`.

## Collection Info

Blender identifier: `GeometryNodeCollectionInfo`

### nd

- `nd.collection_info(cls, collection: Collection=None, separate_children: Boolean=None, reset_children: Boolean=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — class method; returns `OUT`.

### Collection

- `Collection.info(self, separate_children: Boolean=None, reset_children: Boolean=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — method; returns `OUT`.

## Color

Blender identifier: `FunctionNodeInputColor`

### nd

- `nd.color(cls, value: tuple[float, float, float, float]=(0.5, 0.5, 0.5, 1.0))` — class method; returns `OUT`.

## Color Ramp

Blender identifier: `ShaderNodeValToRGB`

### nd

- `nd.color_ramp(cls, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.color_ramp(self)` — method; returns `OUT`.

## Combine Bundle

Blender identifier: `NodeCombineBundle`

### nd

- `nd.combine_bundle(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

### Bundle

- `Bundle.Combine(cls, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

## Combine Color

Blender identifier: `FunctionNodeCombineColor`

### nd

- `nd.combine_color(cls, red: Float=None, green: Float=None, blue: Float=None, alpha: Float=None, *, hue: Float=None, saturation: Float=None, value: Float=None, lightness: Float=None, mode: T_MODE_3='RGB')` — class method; returns `OUT`.

### Color

- `Color.Combine(cls, red: Float=None, green: Float=None, blue: Float=None, alpha: Float=None, *, hue: Float=None, saturation: Float=None, value: Float=None, lightness: Float=None, mode: T_MODE_3='RGB')` — class method; returns `OUT`.
- `Color.CombineRGB(cls, red: Float=None, green: Float=None, blue: Float=None, alpha: Float=None)` — class method; returns `OUT`.
- `Color.CombineHSV(cls, hue: Float=None, saturation: Float=None, value: Float=None, alpha: Float=None)` — class method; returns `OUT`.
- `Color.CombineHSL(cls, hue: Float=None, saturation: Float=None, lightness: Float=None, alpha: Float=None)` — class method; returns `OUT`.

## Combine List

Blender identifier: `GeometryNodeCombineList`

### nd

- `nd.combine_list(cls, *items, data_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.combine_list(self, *items)` — method; returns `OUT`.

### Integer

- `Integer.combine_list(self, *items)` — method; returns `OUT`.

### Boolean

- `Boolean.combine_list(self, *items)` — method; returns `OUT`.

### Vector

- `Vector.combine_list(self, *items)` — method; returns `OUT`.

### Color

- `Color.combine_list(self, *items)` — method; returns `OUT`.

### Rotation

- `Rotation.combine_list(self, *items)` — method; returns `OUT`.

### Matrix

- `Matrix.combine_list(self, *items)` — method; returns `OUT`.

### String

- `String.combine_list(self, *items)` — method; returns `OUT`.

### Menu

- `Menu.combine_list(self, *items)` — method; returns `OUT`.

### Object

- `Object.combine_list(self, *items)` — method; returns `OUT`.

### Image

- `Image.combine_list(self, *items)` — method; returns `OUT`.

### Geometry

- `Geometry.combine_list(self, *items)` — method; returns `OUT`.

### Collection

- `Collection.combine_list(self, *items)` — method; returns `OUT`.

### Material

- `Material.combine_list(self, *items)` — method; returns `OUT`.

### Bundle

- `Bundle.combine_list(self, *items)` — method; returns `OUT`.

### Closure

- `Closure.combine_list(self, *items)` — method; returns `OUT`.

### Font

- `Font.combine_list(self, *items)` — method; returns `OUT`.

### Sound

- `Sound.combine_list(self, *items)` — method; returns `OUT`.

## Combine Matrix

Blender identifier: `FunctionNodeCombineMatrix`

### nd

- `nd.combine_matrix(cls, column_1_row_1: Float=None, column_1_row_2: Float=None, column_1_row_3: Float=None, column_1_row_4: Float=None, column_2_row_1: Float=None, column_2_row_2: Float=None, column_2_row_3: Float=None, column_2_row_4: Float=None, column_3_row_1: Float=None, column_3_row_2: Float=None, column_3_row_3: Float=None, column_3_row_4: Float=None, column_4_row_1: Float=None, column_4_row_2: Float=None, column_4_row_3: Float=None, column_4_row_4: Float=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.Combine(cls, column_1_row_1: Float=None, column_1_row_2: Float=None, column_1_row_3: Float=None, column_1_row_4: Float=None, column_2_row_1: Float=None, column_2_row_2: Float=None, column_2_row_3: Float=None, column_2_row_4: Float=None, column_3_row_1: Float=None, column_3_row_2: Float=None, column_3_row_3: Float=None, column_3_row_4: Float=None, column_4_row_1: Float=None, column_4_row_2: Float=None, column_4_row_3: Float=None, column_4_row_4: Float=None)` — class method; returns `OUT`.

## Combine Transform

Blender identifier: `FunctionNodeCombineTransform`

### nd

- `nd.combine_transform(cls, translation: Vector=None, rotation: Rotation=None, scale: Vector=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.CombineTransform(cls, translation: Vector=None, rotation: Rotation=None, scale: Vector=None)` — class method; returns `OUT`.

## Combine XYZ

Blender identifier: `ShaderNodeCombineXYZ`

### nd

- `nd.combine_xyz(cls, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

### Vector

- `Vector.CombineXYZ(cls, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

## Comment

Blender identifier: `NodeComment`

### nd

- `nd.comment(cls, text: str='## Comment')` — class method; returns `NODE`.

## Compare

Blender identifier: `FunctionNodeCompare`

### nd

- `nd.compare(cls, a: Socket=None, b: Socket=None, epsilon: Float=None, c: Float=None, angle: Float=None, data_type: T_DATA_TYPE_7='FLOAT', operation: T_OPERATION_3='GREATER_THAN', mode: T_MODE_4='ELEMENT')` — class method; returns `OUT`.

### Float

- `Float.less_than(self, b: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__lt__(self, other)` — method; returns `OUT`.
- `Float.less_equal(self, b: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__le__(self, other)` — method; returns `OUT`.
- `Float.greater_than(self, b: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__gt__(self, other)` — method; returns `OUT`.
- `Float.greater_equal(self, b: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__ge__(self, other)` — method; returns `OUT`.
- `Float.equal(self, b: Float=None, epsilon: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__eq__(self, other)` — method; returns `OUT`.
- `Float.not_equal(self, b: Float=None, epsilon: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Float.__ne__(self, other)` — method; returns `OUT`.
- `Float.compare(self, b: Float=None, epsilon: Float=None, operation: T_OPERATION_3='GREATER_THAN', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Integer

- `Integer.less_than(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__lt__(self, other)` — method; returns `OUT`.
- `Integer.less_equal(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__le__(self, other)` — method; returns `OUT`.
- `Integer.greater_than(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__gt__(self, other)` — method; returns `OUT`.
- `Integer.greater_equal(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__ge__(self, other)` — method; returns `OUT`.
- `Integer.equal(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__eq__(self, other)` — method; returns `OUT`.
- `Integer.not_equal(self, b: Integer=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Integer.__ne__(self, other)` — method; returns `OUT`.
- `Integer.compare(self, b: Integer=None, operation: T_OPERATION_3='GREATER_THAN', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Vector

- `Vector.less_than(self, b: Vector=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__lt__(self, other)` — method; returns `OUT`.
- `Vector.less_equal(self, b: Vector=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__le__(self, other)` — method; returns `OUT`.
- `Vector.greater_than(self, b: Vector=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__gt__(self, other)` — method; returns `OUT`.
- `Vector.greater_equal(self, b: Vector=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__ge__(self, other)` — method; returns `OUT`.
- `Vector.equal(self, b: Vector=None, epsilon: Float=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__eq__(self, other)` — method; returns `OUT`.
- `Vector.not_equal(self, b: Vector=None, epsilon: Float=None, c: Float=None, angle: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Vector.__ne__(self, other)` — method; returns `OUT`.
- `Vector.compare(self, b: Vector=None, c: Float=None, angle: Float=None, epsilon: Float=None, operation: T_OPERATION_3='GREATER_THAN', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Color

- `Color.equal(self, b: Color=None, epsilon: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Color.__eq__(self, other)` — method; returns `OUT`.
- `Color.not_equal(self, b: Color=None, epsilon: Float=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Color.__ne__(self, other)` — method; returns `OUT`.
- `Color.brighter(self, b: Color=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Color.__gt__(self, other)` — method; returns `OUT`.
- `Color.darker(self, b: Color=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Color.__lt__(self, other)` — method; returns `OUT`.
- `Color.compare(self, b: Color=None, epsilon: Float=None, operation: T_OPERATION_8='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### String

- `String.equal(self, b: String=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `String.__eq__(self, other)` — method; returns `OUT`.
- `String.not_equal(self, b: String=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `String.__ne__(self, other)` — method; returns `OUT`.
- `String.compare(self, b: String=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Object

- `Object.equal(self, b: Object=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Object.__eq__(self, other)` — method; returns `OUT`.
- `Object.not_equal(self, b: Object=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Object.__ne__(self, other)` — method; returns `OUT`.
- `Object.compare(self, b: Object=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Image

- `Image.equal(self, b: Image=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Image.__eq__(self, other)` — method; returns `OUT`.
- `Image.not_equal(self, b: Image=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Image.__ne__(self, other)` — method; returns `OUT`.
- `Image.compare(self, b: Image=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Collection

- `Collection.equal(self, b: Collection=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Collection.__eq__(self, other)` — method; returns `OUT`.
- `Collection.not_equal(self, b: Collection=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Collection.__ne__(self, other)` — method; returns `OUT`.
- `Collection.compare(self, b: Collection=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Material

- `Material.equal(self, b: Material=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Material.__eq__(self, other)` — method; returns `OUT`.
- `Material.not_equal(self, b: Material=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Material.__ne__(self, other)` — method; returns `OUT`.
- `Material.compare(self, b: Material=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Font

- `Font.equal(self, b: Font=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Font.__eq__(self, other)` — method; returns `OUT`.
- `Font.not_equal(self, b: Font=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Font.__ne__(self, other)` — method; returns `OUT`.
- `Font.compare(self, b: Font=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

### Sound

- `Sound.equal(self, b: Sound=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Sound.__eq__(self, other)` — method; returns `OUT`.
- `Sound.not_equal(self, b: Sound=None, mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.
- `Sound.__ne__(self, other)` — method; returns `OUT`.
- `Sound.compare(self, b: Sound=None, operation: T_OPERATION_9='EQUAL', mode: T_MODE_4='ELEMENT')` — method; returns `OUT`.

## Cone

Blender identifier: `GeometryNodeMeshCone`

### nd

- `nd.cone(cls, vertices: Integer=None, side_segments: Integer=None, fill_segments: Integer=None, radius_top: Float=None, radius_bottom: Float=None, depth: Float=None, fill_type: T_FILL_TYPE_1='NGON')` — class method; returns `OUT`.

### Mesh

- `Mesh.Cone(cls, vertices: Integer=None, side_segments: Integer=None, fill_segments: Integer=None, radius_top: Float=None, radius_bottom: Float=None, depth: Float=None, fill_type: T_FILL_TYPE_1='NGON')` — class method; returns `OUT`.

## Construct Curves

Blender identifier: `GeometryNodeConstructCurves`

### nd

- `nd.construct_curves(cls, positions: Vector=None, curve_offsets: Integer=None)` — class method; returns `OUT`.

### Curve

- `Curve.ConstructCurves(cls, positions: Vector=None, curve_offsets: Integer=None)` — class method; returns `OUT`.

## Convex Hull

Blender identifier: `GeometryNodeConvexHull`

### nd

- `nd.convex_hull(cls, geometry: Geometry=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.convex_hull(self)` — method; returns `OUT`.

## Corners of Edge

Blender identifier: `GeometryNodeCornersOfEdge`

### nd

- `nd.corners_of_edge(cls, edge_index: Integer=None, weights: Float=None, sort_index: Integer=None)` — class method; returns `OUT`.

## Corners of Face

Blender identifier: `GeometryNodeCornersOfFace`

### nd

- `nd.corners_of_face(cls, face_index: Integer=None, weights: Float=None, sort_index: Integer=None)` — class method; returns `OUT`.

## Corners of Vertex

Blender identifier: `GeometryNodeCornersOfVertex`

### nd

- `nd.corners_of_vertex(cls, vertex_index: Integer=None, weights: Float=None, sort_index: Integer=None)` — class method; returns `OUT`.

## Cube

Blender identifier: `GeometryNodeMeshCube`

### nd

- `nd.cube(cls, size: Vector=None, vertices_x: Integer=None, vertices_y: Integer=None, vertices_z: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.Cube(cls, size: Vector=None, vertices_x: Integer=None, vertices_y: Integer=None, vertices_z: Integer=None)` — class method; returns `OUT`.

## Cube Grid Topology

Blender identifier: `GeometryNodeCubeGridTopology`

### nd

- `nd.cube_grid_topology(cls, bounds_min: Vector=None, bounds_max: Vector=None, resolution_x: Integer=None, resolution_y: Integer=None, resolution_z: Integer=None, min_x: Integer=None, min_y: Integer=None, min_z: Integer=None)` — class method; returns `OUT`.

## Curve Circle

Blender identifier: `GeometryNodeCurvePrimitiveCircle`

### nd

- `nd.curve_circle(cls, resolution: Integer=None, point_1: Vector=None, point_2: Vector=None, point_3: Vector=None, radius: Float=None, mode: T_MODE_1='RADIUS')` — class method; returns `OUT`.

### Curve

- `Curve.Circle(cls, resolution: Integer=None, point_1: Vector=None, point_2: Vector=None, point_3: Vector=None, radius: Float=None, mode: T_MODE_1='RADIUS')` — class method; returns `OUT`.

## Curve Handle Positions

Blender identifier: `GeometryNodeInputCurveHandlePositions`

### nd

- `nd.curve_handle_positions(cls, relative: Boolean=None)` — class method; returns `OUT`.

### Curve

- `Curve.left_handle_position(self)` — property; returns `Left`.
- `Curve.left_handle_offset(self)` — property; returns `Left`.
- `Curve.right_handle_position(self)` — property; returns `Right`.
- `Curve.right_handle_offset(self)` — property; returns `Right`.

## Curve Length

Blender identifier: `GeometryNodeCurveLength`

### nd

- `nd.curve_length(cls, curve: Curve=None)` — class method; returns `OUT`.

### Curve

- `Curve.length(self)` — method; returns `OUT`.

## Curve Line

Blender identifier: `GeometryNodeCurvePrimitiveLine`

### nd

- `nd.curve_line(cls, start: Vector=None, end: Vector=None, direction: Vector=None, length: Float=None, mode: T_MODE_5='POINTS')` — class method; returns `OUT`.

### Curve

- `Curve.Line(cls, start: Vector=None, end: Vector=None, direction: Vector=None, length: Float=None, mode: T_MODE_5='POINTS')` — class method; returns `OUT`.

## Curve Tangent

Blender identifier: `GeometryNodeInputTangent`

### nd

- `nd.curve_tangent(cls)` — property; returns `OUT`.

## Curve Tilt

Blender identifier: `GeometryNodeInputCurveTilt`

### nd

- `nd.curve_tilt(cls)` — property; returns `OUT`.

### Spline

- `Spline.tilt(self)` — property; returns `OUT`.

### Curve

- `Curve.tilt(self)` — property; returns `OUT`.

## Curve of Point

Blender identifier: `GeometryNodeCurveOfPoint`

### nd

- `nd.curve_of_point(cls, point_index: Integer=None)` — class method; returns `OUT`.

## Curve to Mesh

Blender identifier: `GeometryNodeCurveToMesh`

### nd

- `nd.curve_to_mesh(cls, curve: Curve=None, profile_curve: Curve=None, scale: Float=None, fill_caps: Boolean=None, miter_scale: Boolean=None, miter_scale_limit: Float=None)` — class method; returns `OUT`.

### Curve

- `Curve.to_mesh(self, profile_curve: Curve=None, scale: Float=None, fill_caps: Boolean=None, miter_scale: Boolean=None, miter_scale_limit: Float=None)` — method; returns `OUT`.

## Curve to Points

Blender identifier: `GeometryNodeCurveToPoints`

### nd

- `nd.curve_to_points(cls, curve: Curve=None, count: Integer=None, length: Float=None, mode: T_MODE_6='COUNT')` — class method; returns `OUT`.

### Curve

- `Curve.to_points(self, count: Integer=None, length: Float=None, mode: T_MODE_6='COUNT')` — method; returns `OUT`.

## Curves to Grease Pencil

Blender identifier: `GeometryNodeCurvesToGreasePencil`

### nd

- `nd.curves_to_grease_pencil(cls, curves: Curve=None, selection: Boolean=None, instances_as_layers: Boolean=None)` — class method; returns `OUT`.

### Curve

- `Curve.to_grease_pencil(self, instances_as_layers: Boolean=None)` — method; returns `OUT`.

## Cylinder

Blender identifier: `GeometryNodeMeshCylinder`

### nd

- `nd.cylinder(cls, vertices: Integer=None, side_segments: Integer=None, fill_segments: Integer=None, radius: Float=None, depth: Float=None, fill_type: T_FILL_TYPE_1='NGON')` — class method; returns `OUT`.

### Mesh

- `Mesh.Cylinder(cls, vertices: Integer=None, side_segments: Integer=None, fill_segments: Integer=None, radius: Float=None, depth: Float=None, fill_type: T_FILL_TYPE_1='NGON')` — class method; returns `OUT`.

## Deactivate Voxels

Blender identifier: `GeometryNodeGridDeactivateVoxels`

### nd

- `nd.deactivate_voxels(cls, grid: Socket=None, selection: Boolean=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.deactivate_voxels(self, selection: Boolean=None)` — method; returns `OUT`.

### Integer

- `Integer.deactivate_voxels(self, selection: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.deactivate_voxels(self, selection: Boolean=None)` — method; returns `OUT`.

### Vector

- `Vector.deactivate_voxels(self, selection: Boolean=None)` — method; returns `OUT`.

## Deform Curves on Surface

Blender identifier: `GeometryNodeDeformCurvesOnSurface`

### nd

- `nd.deform_curves_on_surface(cls, curves: Curve=None)` — class method; returns `OUT`.

### Curve

- `Curve.deform_on_surface(self)` — method; returns `OUT`.

## Delete Geometry

Blender identifier: `GeometryNodeDeleteGeometry`

### nd

- `nd.delete_geometry(cls, geometry: Geometry=None, selection: Boolean=None, mode: T_MODE_7='ALL', domain: T_DOMAIN_3='POINT')` — class method; returns `OUT`.

### Point

- `Point.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

### Edge

- `Edge.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

### Face

- `Face.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

### Spline

- `Spline.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

### Instance

- `Instance.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

### Layer

- `Layer.delete(self, mode: T_MODE_7='ALL')` — method; returns `OUT`.

## Dial Gizmo

Blender identifier: `GeometryNodeGizmoDial`

### nd

- `nd.dial_gizmo(cls, *value: Float, position: Vector=None, up: Vector=None, screen_space: Boolean=None, radius: Float=None, color_id: T_COLOR_ID_1='PRIMARY')` — class method; returns `OUT`.

### Float

- `Float.dial_gizmo(self, *value: Float, position: Vector=None, up: Vector=None, screen_space: Boolean=None, radius: Float=None, color_id: T_COLOR_ID_1='PRIMARY')` — method; returns `OUT`.

## Distribute Points in Grid

Blender identifier: `GeometryNodeDistributePointsInGrid`

### nd

- `nd.distribute_points_in_grid(cls, grid: Float=None, density: Float=None, seed: Integer=None, spacing: Vector=None, threshold: Float=None, mode: T_MODE_8='DENSITY_RANDOM')` — class method; returns `OUT`.

### Cloud

- `Cloud.DistributePointsInGrid(cls, grid: Float=None, density: Float=None, seed: Integer=None, spacing: Vector=None, threshold: Float=None, mode: T_MODE_8='DENSITY_RANDOM')` — class method; returns `OUT`.

## Distribute Points in Volume

Blender identifier: `GeometryNodeDistributePointsInVolume`

### nd

- `nd.distribute_points_in_volume(cls, volume: Volume=None, density: Float=None, seed: Integer=None, spacing: Vector=None, threshold: Float=None, mode: Menu=None)` — class method; returns `OUT`.

### Volume

- `Volume.distribute_points_in(self, density: Float=None, seed: Integer=None, spacing: Vector=None, threshold: Float=None, mode: Menu=None)` — method; returns `OUT`.

## Distribute Points on Faces

Blender identifier: `GeometryNodeDistributePointsOnFaces`

### nd

- `nd.distribute_points_on_faces(cls, mesh: Mesh=None, selection: Boolean=None, distance_min: Float=None, density_max: Float=None, density: Float=None, density_factor: Float=None, seed: Integer=None, distribute_method: T_DISTRIBUTE_METHOD_1='RANDOM')` — class method; returns `OUT`.

### Face

- `Face.distribute_points(self, distance_min: Float=None, density_max: Float=None, density: Float=None, density_factor: Float=None, seed: Integer=None, distribute_method: T_DISTRIBUTE_METHOD_1='RANDOM')` — method; returns `OUT`.

## Domain Size

Blender identifier: `GeometryNodeAttributeDomainSize`

### nd

- `nd.domain_size(cls, geometry: Geometry=None, component: T_COMPONENT_1='MESH')` — class method; returns `OUT`.

### Geometry

- `Geometry.domain_size(self, component: T_COMPONENT_1='MESH')` — method; returns `OUT`.

### Mesh

- `Mesh.domain_size(self)` — method; returns `OUT`.

### Cloud

- `Cloud.domain_size(self)` — method; returns `OUT`.

### Curve

- `Curve.domain_size(self)` — method; returns `OUT`.

### Instances

- `Instances.domain_size(self)` — method; returns `OUT`.

### GreasePencil

- `GreasePencil.domain_size(self)` — method; returns `OUT`.

## Dual Mesh

Blender identifier: `GeometryNodeDualMesh`

### nd

- `nd.dual_mesh(cls, mesh: Mesh=None, keep_boundaries: Boolean=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.dual(self, keep_boundaries: Boolean=None)` — method; returns `OUT`.

## Duplicate Elements

Blender identifier: `GeometryNodeDuplicateElements`

### nd

- `nd.duplicate_elements(cls, geometry: Geometry=None, selection: Boolean=None, amount: Integer=None, domain: T_DOMAIN_4='POINT')` — class method; returns `OUT`.

### Point

- `Point.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

### Face

- `Face.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.duplicate_elements(self, amount: Integer=None)` — method; returns `OUT`.

## Edge Angle

Blender identifier: `GeometryNodeInputMeshEdgeAngle`

### nd

- `nd.edge_angle(cls)` — class method; returns `OUT`.

## Edge Neighbors

Blender identifier: `GeometryNodeInputMeshEdgeNeighbors`

### nd

- `nd.edge_neighbors(cls)` — property; returns `OUT`.

## Edge Paths to Curves

Blender identifier: `GeometryNodeEdgePathsToCurves`

### nd

- `nd.edge_paths_to_curves(cls, mesh: Mesh=None, start_vertices: Boolean=None, next_vertex_index: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.to_curves(self, start_vertices: Boolean=None, next_vertex_index: Integer=None)` — method; returns `OUT`.

## Edge Paths to Selection

Blender identifier: `GeometryNodeEdgePathsToSelection`

### nd

- `nd.edge_paths_to_selection(cls, start_vertices: Boolean=None, next_vertex_index: Integer=None)` — class method; returns `OUT`.

## Edge Vertices

Blender identifier: `GeometryNodeInputMeshEdgeVertices`

### nd

- `nd.edge_vertices(cls)` — class method; returns `OUT`.

## Edges of Corner

Blender identifier: `GeometryNodeEdgesOfCorner`

### nd

- `nd.edges_of_corner(cls, corner_index: Integer=None)` — class method; returns `OUT`.

## Edges of Vertex

Blender identifier: `GeometryNodeEdgesOfVertex`

### nd

- `nd.edges_of_vertex(cls, vertex_index: Integer=None, weights: Float=None, sort_index: Integer=None)` — class method; returns `OUT`.

## Edges to Face Groups

Blender identifier: `GeometryNodeEdgesToFaceGroups`

### nd

- `nd.edges_to_face_groups(cls, boundary_edges: Boolean=None)` — class method; returns `OUT`.

## Enable Output

Blender identifier: `NodeEnableOutput`

### nd

- `nd.enable_output(cls, enable: Boolean=None, value: Socket=None, data_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Integer

- `Integer.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Vector

- `Vector.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Color

- `Color.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Rotation

- `Rotation.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Matrix

- `Matrix.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### String

- `String.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Menu

- `Menu.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Object

- `Object.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Image

- `Image.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Geometry

- `Geometry.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Collection

- `Collection.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Material

- `Material.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Bundle

- `Bundle.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Closure

- `Closure.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Font

- `Font.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

### Sound

- `Sound.enable_output(self, enable: Boolean=None)` — method; returns `OUT`.

## Endpoint Selection

Blender identifier: `GeometryNodeCurveEndpointSelection`

### nd

- `nd.endpoint_selection(cls, start_size: Integer=None, end_size: Integer=None)` — class method; returns `OUT`.

## Euler to Rotation

Blender identifier: `FunctionNodeEulerToRotation`

### nd

- `nd.euler_to_rotation(cls, euler: Vector=None)` — class method; returns `OUT`.

### Vector

- `Vector.to_rotation(self)` — method; returns `OUT`.

### Rotation

- `Rotation.FromEuler(cls, euler: Vector=None)` — class method; returns `OUT`.

## Evaluate Closure

Blender identifier: `NodeEvaluateClosure`

### nd

- `nd.evaluate_closure(cls, closure: Closure=None, named_sockets: dict={}, define_signature: bool=False, **sockets)` — class method; returns `OUT`.

### Closure

- `Closure.evaluate(self, named_sockets: dict={}, define_signature: bool=False, **sockets)` — method; returns `OUT`.

## Evaluate at Index

Blender identifier: `GeometryNodeFieldAtIndex`

### nd

- `nd.evaluate_at_index(cls, value: Socket=None, index: Integer=None, domain: T_DOMAIN_1='POINT', data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Point

- `Point.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Face

- `Face.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Corner

- `Corner.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.evaluate_at_index(self, value: Socket=None, index: Integer=None)` — method; returns `OUT`.

## Evaluate on Domain

Blender identifier: `GeometryNodeFieldOnDomain`

### nd

- `nd.evaluate_on_domain(cls, value: Socket=None, domain: T_DOMAIN_1='POINT', data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Point

- `Point.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Edge

- `Edge.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Face

- `Face.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Corner

- `Corner.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Spline

- `Spline.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Instance

- `Instance.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

### Layer

- `Layer.evaluate_on_domain(self, value: Socket=None)` — method; returns `OUT`.

## Extrude Mesh

Blender identifier: `GeometryNodeExtrudeMesh`

### nd

- `nd.extrude_mesh(cls, mesh: Mesh=None, selection: Boolean=None, offset: Vector=None, offset_scale: Float=None, individual: Boolean=None, mode: T_MODE_9='FACES')` — class method; returns `OUT`.

### Mesh

- `Mesh.extrude(self, offset: Vector=None, offset_scale: Float=None, individual: Boolean=None, mode: T_MODE_9='FACES')` — method; returns `OUT`.

### Vertex

- `Vertex.extrude(self, offset: Vector=None, offset_scale: Float=None)` — method; returns `OUT`.

### Edge

- `Edge.extrude(self, offset: Vector=None, offset_scale: Float=None)` — method; returns `OUT`.

### Face

- `Face.extrude(self, offset: Vector=None, offset_scale: Float=None, individual: Boolean=None)` — method; returns `OUT`.

## Face Area

Blender identifier: `GeometryNodeInputMeshFaceArea`

### nd

- `nd.face_area(cls)` — property; returns `OUT`.

## Face Group Boundaries

Blender identifier: `GeometryNodeMeshFaceSetBoundaries`

### nd

- `nd.face_group_boundaries(cls, face_group_id: Integer=None)` — class method; returns `OUT`.

## Face Neighbors

Blender identifier: `GeometryNodeInputMeshFaceNeighbors`

### nd

- `nd.face_neighbors(cls)` — class method; returns `OUT`.

## Face Set

Blender identifier: `GeometryNodeToolFaceSet`

### nd

- `nd.face_set(cls)` — class method; returns `OUT`.

## Face of Corner

Blender identifier: `GeometryNodeFaceOfCorner`

### nd

- `nd.face_of_corner(cls, corner_index: Integer=None)` — class method; returns `OUT`.

## Field Average

Blender identifier: `GeometryNodeFieldAverage`

### nd

- `nd.field_average(cls, value: Socket=None, group_id: Integer=None, data_type: T_DATA_TYPE_3='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Face

- `Face.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Corner

- `Corner.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.field_average(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

## Field Min & Max

Blender identifier: `GeometryNodeFieldMinAndMax`

### nd

- `nd.field_min_max(cls, value: Socket=None, group_id: Integer=None, data_type: T_DATA_TYPE_9='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Face

- `Face.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Corner

- `Corner.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.field_min_max(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

## Field Variance

Blender identifier: `GeometryNodeFieldVariance`

### nd

- `nd.field_variance(cls, value: Socket=None, group_id: Integer=None, data_type: T_DATA_TYPE_3='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Face

- `Face.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Corner

- `Corner.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.field_variance(self, value: Socket=None, group_id: Integer=None)` — method; returns `OUT`.

## Field to Grid

Blender identifier: `GeometryNodeFieldToGrid`

### nd

- `nd.field_to_grid(cls, topology: Socket=None, named_sockets: dict={}, data_type: T_DATA_TYPE_5='FLOAT', **sockets)` — class method; returns `OUT`.

### Float

- `Float.field_to_grid(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

### Integer

- `Integer.field_to_grid(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

### Boolean

- `Boolean.field_to_grid(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

### Vector

- `Vector.field_to_grid(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

## Field to List

Blender identifier: `GeometryNodeFieldToList`

### nd

- `nd.field_to_list(cls, count: Integer=None, named_sockets: dict={}, **sockets)` — class method; returns `OUT`.

### Integer

- `Integer.field_to_list(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

## Fill Curve

Blender identifier: `GeometryNodeFillCurve`

### nd

- `nd.fill_curve(cls, curve: Curve=None, group_id: Integer=None, mode: Menu=None, fill_rule: Menu=None)` — class method; returns `OUT`.

### Curve

- `Curve.fill(self, group_id: Integer=None, mode: Menu=None, fill_rule: Menu=None)` — method; returns `OUT`.

## Fillet Curve

Blender identifier: `GeometryNodeFilletCurve`

### nd

- `nd.fillet_curve(cls, curve: Curve=None, radius: Float=None, limit_radius: Boolean=None, count: Integer=None, mode: Menu=None)` — class method; returns `OUT`.

### Curve

- `Curve.fillet(self, radius: Float=None, limit_radius: Boolean=None, count: Integer=None, mode: Menu=None)` — method; returns `OUT`.

## Filter List

Blender identifier: `GeometryNodeFilterList`

### nd

- `nd.filter_list(cls, list: Socket=None, selection: Boolean=None, socket_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Integer

- `Integer.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Vector

- `Vector.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Color

- `Color.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Rotation

- `Rotation.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Matrix

- `Matrix.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### String

- `String.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Menu

- `Menu.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Object

- `Object.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Image

- `Image.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Geometry

- `Geometry.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Collection

- `Collection.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Material

- `Material.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Bundle

- `Bundle.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Closure

- `Closure.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Font

- `Font.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

### Sound

- `Sound.filter_list(self, selection: Boolean=None)` — method; returns `OUT`.

## Find in String

Blender identifier: `FunctionNodeFindInString`

### nd

- `nd.find_in_string(cls, string: String=None, search: String=None, mode: Menu=None)` — class method; returns `OUT`.

### String

- `String.find_in_string(self, search: String=None, mode: Menu=None)` — method; returns `OUT`.

## Flip Faces

Blender identifier: `GeometryNodeFlipFaces`

### nd

- `nd.flip_faces(cls, mesh: Mesh=None, selection: Boolean=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.flip_faces(self)` — method; returns `OUT`.

## Float Curve

Blender identifier: `ShaderNodeFloatCurve`

### nd

- `nd.float_curve(cls, value: Float=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.float_curve(self, value: Float=None)` — method; returns `OUT`.

## Float to Integer

Blender identifier: `FunctionNodeFloatToInt`

### nd

- `nd.float_to_integer(cls, float: Float=None, rounding_mode: T_ROUNDING_MODE_1='ROUND')` — class method; returns `OUT`.

### Float

- `Float.to_integer(self, rounding_mode: T_ROUNDING_MODE_1='ROUND')` — method; returns `OUT`.

### Integer

- `Integer.FromFloat(cls, float: Float=None, rounding_mode: T_ROUNDING_MODE_1='ROUND')` — class method; returns `OUT`.

## Font

Blender identifier: `GeometryNodeInputFont`

### nd

- `nd.font(cls, font=None)` — class method; returns `OUT`.

## Format String

Blender identifier: `FunctionNodeFormatString`

### nd

- `nd.format_string(cls, format: String=None, named_sockets: dict={}, **sockets)` — class method; returns `OUT`.

### String

- `String.format(self, named_sockets: dict={}, **sockets)` — method; returns `OUT`.

## Frame

Blender identifier: `NodeFrame`

### nd

- `nd.frame(cls, text=None, shrink: bool=True, label_size: int=20)` — class method; returns `NODE`.

## Gabor Texture

Blender identifier: `ShaderNodeTexGabor`

### nd

- `nd.gabor_texture(cls, vector: Vector=None, scale: Float=None, frequency: Float=None, anisotropy: Float=None, orientation: Socket=None, gabor_type: T_GABOR_TYPE_1='2D')` — class method; returns `OUT`.

### Texture

- `Texture.Gabor(cls, vector: Vector=None, scale: Float=None, frequency: Float=None, anisotropy: Float=None, orientation: Socket=None, gabor_type: T_GABOR_TYPE_1='2D')` — class method; returns `OUT`.

## Gamma

Blender identifier: `ShaderNodeGamma`

### nd

- `nd.gamma(cls, color: Color=None, gamma: Float=None)` — class method; returns `OUT`.

### Color

- `Color.gamma(self, gamma: Float=None)` — method; returns `OUT`.

## Geometry Materials

Blender identifier: `GeometryNodeGeometryMaterials`

### nd

- `nd.geometry_materials(cls, geometry: Geometry=None, component_type: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.materials(self, component_type: Menu=None)` — method; returns `OUT`.

## Geometry Proximity

Blender identifier: `GeometryNodeProximity`

### nd

- `nd.geometry_proximity(cls, geometry: Geometry=None, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None, target_element: T_TARGET_ELEMENT_1='FACES')` — class method; returns `OUT`.

### Geometry

- `Geometry.proximity(self, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None, target_element: T_TARGET_ELEMENT_1='FACES')` — method; returns `OUT`.
- `Geometry.proximity_points(self, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None)` — method; returns `OUT`.
- `Geometry.proximity_edges(self, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None)` — method; returns `OUT`.
- `Geometry.proximity_faces(self, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None)` — method; returns `OUT`.

## Geometry to Instance

Blender identifier: `GeometryNodeGeometryToInstance`

### nd

- `nd.geometry_to_instance(cls, *geometry: Geometry)` — class method; returns `OUT`.

### Geometry

- `Geometry.to_instance(self, *geometry: Geometry)` — method; returns `OUT`.

## Get Attribute Names

Blender identifier: `GeometryNodeGetAttributeNames`

### nd

- `nd.get_attribute_names(cls, geometry: Geometry=None, filter_data_type: Boolean=None, filter_domain: Boolean=None, data_type: Menu=None, domain: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.get_attribute_names(self, filter_data_type: Boolean=None, filter_domain: Boolean=None, data_type: Menu=None, domain: Menu=None)` — method; returns `OUT`.

## Get Bundle Item

Blender identifier: `NodeGetBundleItem`

### nd

- `nd.get_item(cls, bundle: Bundle=None, path: String=None, remove: Boolean=None, socket_type: T_DATA_TYPE_6='FLOAT', shape: T_STRUCTURE_TYPE_1='AUTO')` — class method; returns `Item`.

### Bundle

- `Bundle.get_item(self, path: String=None, remove: Boolean=None, socket_type: T_DATA_TYPE_6='FLOAT', shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `Item`.

## Get Geometry Bundle

Blender identifier: `GeometryNodeGetGeometryBundle`

### nd

- `nd.get_geometry_bundle(cls, geometry: Geometry=None, remove: Boolean=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.get_bundle(self, remove: Boolean=None)` — method; returns `OUT`.
- `Geometry.bundle(self)` — property; returns `Bundle`.

## Get Geometry Component

Blender identifier: `GeometryNodeGetGeometryComponent`

### nd

- `nd.get_geometry_component(cls, geometry: Geometry=None, remove: Boolean=None, type: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.get_component(self, remove: Boolean=None, type: Menu=None)` — method; returns `OUT`.

## Get Grid Names

Blender identifier: `GeometryNodeGetGridNames`

### nd

- `nd.get_grid_names(cls, volume: Volume=None)` — class method; returns `OUT`.

### Volume

- `Volume.get_grid_names(self)` — method; returns `OUT`.

## Get List Item

Blender identifier: `GeometryNodeListGetItem`

### nd

- `nd.get_list_item(cls, list: Socket=None, index: Integer=None, socket_type: T_DATA_TYPE_6='FLOAT', shape: T_STRUCTURE_TYPE_1='AUTO')` — class method; returns `OUT`.

### Float

- `Float.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Integer

- `Integer.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Boolean

- `Boolean.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Vector

- `Vector.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Color

- `Color.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Rotation

- `Rotation.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Matrix

- `Matrix.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### String

- `String.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Menu

- `Menu.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Object

- `Object.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Image

- `Image.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Geometry

- `Geometry.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Collection

- `Collection.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Material

- `Material.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Bundle

- `Bundle.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Closure

- `Closure.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Font

- `Font.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

### Sound

- `Sound.get_list_item(self, index: Integer=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

## Get Named Grid

Blender identifier: `GeometryNodeGetNamedGrid`

### nd

- `nd.get_named_grid(cls, volume: Volume=None, name: String=None, remove: Boolean=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Volume

- `Volume.get_named_grid(self, name: String=None, remove: Boolean=None, data_type: T_DATA_TYPE_5='FLOAT')` — method; returns `OUT`.

## Get Nested Bundle Paths

Blender identifier: `NodeGetNestedBundlePaths`

### nd

- `nd.get_nested_bundle_paths(cls, bundle: Bundle=None, bundle_type: String=None, mode: Menu=None, pattern_mode: Menu=None, data_type: Menu=None)` — class method; returns `OUT`.

### Bundle

- `Bundle.get_nested_paths(self, bundle_type: String=None, mode: Menu=None, pattern_mode: Menu=None, data_type: Menu=None)` — method; returns `OUT`.

## Get Vector Component

Blender identifier: `FunctionNodeGetVectorComponent`

### nd

- `nd.get_vector_component(cls, vector: Vector=None, index: Integer=None)` — class method; returns `OUT`.

### Vector

- `Vector.get_component(self, index: Integer=None)` — method; returns `OUT`.

## Gradient Texture

Blender identifier: `ShaderNodeTexGradient`

### nd

- `nd.gradient_texture(cls, vector: Vector=None, gradient_type: T_GRADIENT_TYPE_1='LINEAR')` — class method; returns `OUT`.

### Texture

- `Texture.Gradient(cls, vector: Vector=None, gradient_type: T_GRADIENT_TYPE_1='LINEAR')` — class method; returns `OUT`.

## Grease Pencil Color

Blender identifier: `GeometryNodeGreasePencilColor`

### nd

- `nd.grease_pencil_color(cls)` — class method; returns `OUT`.

## Grease Pencil Draw Time

Blender identifier: `GeometryNodeGreasePencilDrawTime`

### nd

- `nd.grease_pencil_draw_time(cls)` — class method; returns `OUT`.

## Grease Pencil Fill ID

Blender identifier: `GeometryNodeGreasePencilFillID`

### nd

- `nd.grease_pencil_fill_id(cls)` — property; returns `OUT`.

## Grease Pencil Opacity

Blender identifier: `GeometryNodeGreasePencilOpacity`

### nd

- `nd.grease_pencil_opacity(cls)` — class method; returns `OUT`.

## Grease Pencil Stroke Softness

Blender identifier: `GeometryNodeGreasePencilStrokeSoftness`

### nd

- `nd.grease_pencil_stroke_softness(cls)` — property; returns `OUT`.

## Grease Pencil Stroke Visibility

Blender identifier: `GeometryNodeGreasePencilStrokeVisibility`

### nd

- `nd.grease_pencil_stroke_visibility(cls)` — property; returns `OUT`.

## Grease Pencil to Curves

Blender identifier: `GeometryNodeGreasePencilToCurves`

### nd

- `nd.grease_pencil_to_curves(cls, grease_pencil: GreasePencil=None, selection: Boolean=None, layers_as_instances: Boolean=None)` — class method; returns `OUT`.

### GreasePencil

- `GreasePencil.to_curves(self, layers_as_instances: Boolean=None)` — method; returns `OUT`.

## Grid

Blender identifier: `GeometryNodeMeshGrid`

### nd

- `nd.grid(cls, size_x: Float=None, size_y: Float=None, vertices_x: Integer=None, vertices_y: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.Grid(cls, size_x: Float=None, size_y: Float=None, vertices_x: Integer=None, vertices_y: Integer=None)` — class method; returns `OUT`.

## Grid Curl

Blender identifier: `GeometryNodeGridCurl`

### nd

- `nd.grid_curl(cls, grid: Vector=None)` — class method; returns `OUT`.

### Vector

- `Vector.grid_curl(self)` — method; returns `OUT`.

## Grid Dilate & Erode

Blender identifier: `GeometryNodeGridDilateAndErode`

### nd

- `nd.grid_dilate_erode(cls, grid: Socket=None, steps: Integer=None, connectivity: Menu=None, tiles: Menu=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.grid_dilate_erode(self, steps: Integer=None, connectivity: Menu=None, tiles: Menu=None)` — method; returns `OUT`.

### Integer

- `Integer.grid_dilate_erode(self, steps: Integer=None, connectivity: Menu=None, tiles: Menu=None)` — method; returns `OUT`.

### Boolean

- `Boolean.grid_dilate_erode(self, steps: Integer=None, connectivity: Menu=None, tiles: Menu=None)` — method; returns `OUT`.

### Vector

- `Vector.grid_dilate_erode(self, steps: Integer=None, connectivity: Menu=None, tiles: Menu=None)` — method; returns `OUT`.

## Grid Divergence

Blender identifier: `GeometryNodeGridDivergence`

### nd

- `nd.grid_divergence(cls, grid: Vector=None)` — class method; returns `OUT`.

### Vector

- `Vector.grid_divergence(self)` — method; returns `OUT`.

## Grid Gradient

Blender identifier: `GeometryNodeGridGradient`

### nd

- `nd.grid_gradient(cls, grid: Float=None)` — class method; returns `OUT`.

### Float

- `Float.grid_gradient(self)` — method; returns `OUT`.

## Grid Info

Blender identifier: `GeometryNodeGridInfo`

### nd

- `nd.grid_info(cls, grid: Socket=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.grid_info(self)` — method; returns `OUT`.

### Integer

- `Integer.grid_info(self)` — method; returns `OUT`.

### Boolean

- `Boolean.grid_info(self)` — method; returns `OUT`.

### Vector

- `Vector.grid_info(self)` — method; returns `OUT`.

## Grid Laplacian

Blender identifier: `GeometryNodeGridLaplacian`

### nd

- `nd.grid_laplacian(cls, grid: Float=None)` — class method; returns `OUT`.

### Float

- `Float.grid_laplacian(self)` — method; returns `OUT`.

## Grid Mean

Blender identifier: `GeometryNodeGridMean`

### nd

- `nd.grid_mean(cls, grid: Socket=None, width: Integer=None, iterations: Integer=None, data_type: T_DATA_TYPE_2='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.grid_mean(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.grid_mean(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.grid_mean(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

## Grid Median

Blender identifier: `GeometryNodeGridMedian`

### nd

- `nd.grid_median(cls, grid: Socket=None, width: Integer=None, iterations: Integer=None, data_type: T_DATA_TYPE_2='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.grid_median(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.grid_median(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.grid_median(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

## Grid Solve Poisson

Blender identifier: `GeometryNodeGridSolvePoisson`

### nd

- `nd.grid_solve_poisson(cls, grid: Float=None, max_iterations: Integer=None, error_threshold: Float=None, boundary_value: Float=None, boundary_gradient: Vector=None, boundary_factor: Float=None, threshold_mode: Menu=None, boundary: Menu=None)` — class method; returns `OUT`.

### Float

- `Float.grid_solve_poisson(self, max_iterations: Integer=None, error_threshold: Float=None, boundary_value: Float=None, boundary_gradient: Vector=None, boundary_factor: Float=None, threshold_mode: Menu=None, boundary: Menu=None)` — method; returns `OUT`.

## Grid Topology Boolean

Blender identifier: `GeometryNodeGridTopologyBoolean`

### nd

- `nd.grid_topology_boolean(cls, *grid_2: Socket, grid_1: Socket=None, operation: Menu=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.grid_topology_boolean(self, *grid_2: Float, operation: Menu=None)` — method; returns `OUT`.

### Integer

- `Integer.grid_topology_boolean(self, *grid_2: Integer, operation: Menu=None)` — method; returns `OUT`.

### Boolean

- `Boolean.grid_topology_boolean(self, *grid_2: Boolean, operation: Menu=None)` — method; returns `OUT`.

### Vector

- `Vector.grid_topology_boolean(self, *grid_2: Vector, operation: Menu=None)` — method; returns `OUT`.

## Grid to Mesh

Blender identifier: `GeometryNodeGridToMesh`

### nd

- `nd.grid_to_mesh(cls, grid: Float=None, threshold: Float=None, adaptivity: Float=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.FromGrid(cls, grid: Float=None, threshold: Float=None, adaptivity: Float=None)` — class method; returns `OUT`.

## Grid to Points

Blender identifier: `GeometryNodeGridToPoints`

### nd

- `nd.grid_to_points(cls, grid: Socket=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Cloud

- `Cloud.FromGrid(cls, grid: Socket=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

## Handle Type Selection

Blender identifier: `GeometryNodeCurveHandleTypeSelection`

### nd

- `nd.handle_type_selection(cls, handle_type: T_HANDLE_TYPE_1='AUTO', mode: set[Literal['LEFT', 'RIGHT']]={'LEFT', 'RIGHT'})` — class method; returns `OUT`.

## Hash Value

Blender identifier: `FunctionNodeHashValue`

### nd

- `nd.hash_value(cls, value: Socket=None, seed: Integer=None, data_type: T_DATA_TYPE_10='INT')` — class method; returns `OUT`.

### Float

- `Float.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### Color

- `Color.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### Rotation

- `Rotation.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### Matrix

- `Matrix.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

### String

- `String.hash_value(self, seed: Integer=None)` — method; returns `OUT`.

## ID

Blender identifier: `GeometryNodeInputID`

### nd

- `nd.id(cls)` — property; returns `OUT`.

### Geometry

- `Geometry.id(self)` — property; returns `OUT`.

## Ico Sphere

Blender identifier: `GeometryNodeMeshIcoSphere`

### nd

- `nd.ico_sphere(cls, radius: Float=None, subdivisions: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.IcoSphere(cls, radius: Float=None, subdivisions: Integer=None)` — class method; returns `OUT`.

## Image

Blender identifier: `GeometryNodeInputImage`

### nd

- `nd.image(cls, image=None)` — class method; returns `OUT`.

## Image Info

Blender identifier: `GeometryNodeImageInfo`

### nd

- `nd.image_info(cls, image: Image=None, frame: Integer=None)` — class method; returns `OUT`.

### Image

- `Image.info(self, frame: Integer=None)` — method; returns `OUT`.

## Image Texture

Blender identifier: `GeometryNodeImageTexture`

### nd

- `nd.image_texture(cls, image: Image=None, vector: Vector=None, frame: Integer=None, interpolation: T_INTERPOLATION_1='Linear', extension: T_EXTENSION_1='REPEAT')` — class method; returns `OUT`.

### Texture

- `Texture.Image(cls, image: Image=None, vector: Vector=None, frame: Integer=None, interpolation: T_INTERPOLATION_1='Linear', extension: T_EXTENSION_1='REPEAT')` — class method; returns `OUT`.

## Implicit Conversion

Blender identifier: `NodeImplicitConversion`

### nd

- `nd.implicit_conversion(cls, value: Socket=None, socket_idname: str='NodeSocketColor', data_type: T_DATA_TYPE_6='RGBA')` — class method; returns `OUT`.

### Float

- `Float.implicit_conversion(self, socket_idname: str='NodeSocketFloat')` — method; returns `OUT`.

### Integer

- `Integer.implicit_conversion(self, socket_idname: str='NodeSocketInt')` — method; returns `OUT`.

### Boolean

- `Boolean.implicit_conversion(self, socket_idname: str='NodeSocketBool')` — method; returns `OUT`.

### Vector

- `Vector.implicit_conversion(self, socket_idname: str='NodeSocketVector')` — method; returns `OUT`.

### Color

- `Color.implicit_conversion(self, socket_idname: str='NodeSocketColor')` — method; returns `OUT`.

### Rotation

- `Rotation.implicit_conversion(self, socket_idname: str='NodeSocketRotation')` — method; returns `OUT`.

### Matrix

- `Matrix.implicit_conversion(self, socket_idname: str='NodeSocketMatrix')` — method; returns `OUT`.

### String

- `String.implicit_conversion(self, socket_idname: str='NodeSocketString')` — method; returns `OUT`.

### Menu

- `Menu.implicit_conversion(self, socket_idname: str='NodeSocketMenu')` — method; returns `OUT`.

### Object

- `Object.implicit_conversion(self, socket_idname: str='NodeSocketObject')` — method; returns `OUT`.

### Image

- `Image.implicit_conversion(self, socket_idname: str='NodeSocketImage')` — method; returns `OUT`.

### Geometry

- `Geometry.implicit_conversion(self, socket_idname: str='NodeSocketGeometry')` — method; returns `OUT`.

### Collection

- `Collection.implicit_conversion(self, socket_idname: str='NodeSocketCollection')` — method; returns `OUT`.

### Material

- `Material.implicit_conversion(self, socket_idname: str='NodeSocketMaterial')` — method; returns `OUT`.

### Bundle

- `Bundle.implicit_conversion(self, socket_idname: str='NodeSocketBundle')` — method; returns `OUT`.

### Closure

- `Closure.implicit_conversion(self, socket_idname: str='NodeSocketClosure')` — method; returns `OUT`.

### Font

- `Font.implicit_conversion(self, socket_idname: str='NodeSocketFont')` — method; returns `OUT`.

### Sound

- `Sound.implicit_conversion(self, socket_idname: str='NodeSocketSound')` — method; returns `OUT`.

## Import CSV

Blender identifier: `GeometryNodeImportCSV`

### nd

- `nd.import_csv(cls, path: String=None, delimiter: String=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.ImportCSV(cls, path: String=None, delimiter: String=None)` — class method; returns `OUT`.

## Import OBJ

Blender identifier: `GeometryNodeImportOBJ`

### nd

- `nd.import_obj(cls, path: String=None)` — class method; returns `OUT`.

### Instances

- `Instances.ImportOBJ(cls, path: String=None)` — class method; returns `OUT`.

## Import PLY

Blender identifier: `GeometryNodeImportPLY`

### nd

- `nd.import_ply(cls, path: String=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.ImportPLY(cls, path: String=None)` — class method; returns `OUT`.

## Import SPZ

Blender identifier: `GeometryNodeImportSPZ`

### nd

- `nd.import_spz(cls, path: String=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.ImportSPZ(cls, path: String=None)` — class method; returns `OUT`.

## Import STL

Blender identifier: `GeometryNodeImportSTL`

### nd

- `nd.import_stl(cls, path: String=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.ImportSTL(cls, path: String=None)` — class method; returns `OUT`.

## Import Text

Blender identifier: `GeometryNodeImportText`

### nd

- `nd.import_text(cls, path: String=None)` — class method; returns `OUT`.

## Import VDB

Blender identifier: `GeometryNodeImportVDB`

### nd

- `nd.import_vdb(cls, path: String=None)` — class method; returns `OUT`.

### Volume

- `Volume.ImportVDB(cls, path: String=None)` — class method; returns `OUT`.

## Index

Blender identifier: `GeometryNodeInputIndex`

### nd

- `nd.index(cls)` — property; returns `OUT`.

## Index Switch

Blender identifier: `GeometryNodeIndexSwitch`

### nd

- `nd.index_switch(cls, *items, index: Integer=None, data_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Boolean

- `Boolean.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Color

- `Color.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Rotation

- `Rotation.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Matrix

- `Matrix.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### String

- `String.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Menu

- `Menu.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Object

- `Object.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Image

- `Image.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Geometry

- `Geometry.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Collection

- `Collection.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Material

- `Material.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Bundle

- `Bundle.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Closure

- `Closure.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Font

- `Font.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

### Sound

- `Sound.index_switch(self, *items, index: Integer=None)` — method; returns `OUT`.

## Index of Nearest

Blender identifier: `GeometryNodeIndexOfNearest`

### nd

- `nd.index_of_nearest(cls, position: Vector=None, group_id: Integer=None)` — class method; returns `OUT`.

### Vector

- `Vector.index_of_nearest(self, group_id: Integer=None)` — method; returns `OUT`.

## Instance Bounds

Blender identifier: `GeometryNodeInputInstanceBounds`

### nd

- `nd.instance_bounds(cls, use_radius: Boolean=None)` — class method; returns `OUT`.

## Instance Reference

Blender identifier: `GeometryNodeInputInstanceReference`

### nd

- `nd.instance_reference(cls)` — property; returns `OUT`.

## Instance Rotation

Blender identifier: `GeometryNodeInputInstanceRotation`

### nd

- `nd.instance_rotation(cls)` — property; returns `OUT`.

## Instance Scale

Blender identifier: `GeometryNodeInputInstanceScale`

### nd

- `nd.instance_scale(cls)` — property; returns `OUT`.

## Instance Transform

Blender identifier: `GeometryNodeInstanceTransform`

### nd

- `nd.instance_transform(cls)` — property; returns `OUT`.

### Instance

- `Instance.transform(self)` — property; returns `OUT`.

## Instance on Points

Blender identifier: `GeometryNodeInstanceOnPoints`

### nd

- `nd.instance_on_points(cls, points: Cloud=None, selection: Boolean=None, instance: Instances=None, pick_instance: Boolean=None, instance_index: Integer=None, rotation: Rotation=None, scale: Vector=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.instance_on_points(self, instance: Instances=None, pick_instance: Boolean=None, instance_index: Integer=None, rotation: Rotation=None, scale: Vector=None)` — method; returns `OUT`.

## Instances to Points

Blender identifier: `GeometryNodeInstancesToPoints`

### nd

- `nd.instances_to_points(cls, instances: Instances=None, selection: Boolean=None, position: Vector=None, radius: Float=None)` — class method; returns `OUT`.

### Instances

- `Instances.to_points(self, position: Vector=None, radius: Float=None)` — method; returns `OUT`.

## Integer

Blender identifier: `FunctionNodeInputInt`

### nd

- `nd.integer(cls, integer: int=0)` — class method; returns `OUT`.

## Integer Math

Blender identifier: `FunctionNodeIntegerMath`

### nd

- `nd.integer_math(cls, value: Integer=None, value_1: Integer=None, addend: Integer=None, *, base: Integer=None, multiplier: Integer=None, exponent: Integer=None, operation: T_OPERATION_4='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.iadd(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.isubtract(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.imultiply(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.idivide(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.ipower(base: Integer=None, exponent: Integer=None)` — method; returns `OUT`.
- `gnmath.imodulo(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.iabs(value: Integer=None)` — method; returns `OUT`.
- `gnmath.negate(value: Integer=None)` — method; returns `OUT`.
- `gnmath.imultiply_add(value: Integer=None, multiplier: Integer=None, addend: Integer=None)` — method; returns `OUT`.
- `gnmath.isign(value: Integer=None)` — method; returns `OUT`.
- `gnmath.imin(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.imax(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_round(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_floor(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.divide_ceil(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.ifloored_modulo(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.gcd(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.
- `gnmath.lcm(value: Integer=None, value_1: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.add(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__add__(self, other)` — method; returns `OUT`.
- `Integer.__radd__(self, other)` — method; returns `OUT`.
- `Integer.__iadd__(self, other)` — method; returns `OUT`.
- `Integer.subtract(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__sub__(self, other)` — method; returns `OUT`.
- `Integer.__rsub__(self, other)` — method; returns `OUT`.
- `Integer.__isub__(self, other)` — method; returns `OUT`.
- `Integer.multiply(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__mul__(self, other)` — method; returns `OUT`.
- `Integer.__rmul__(self, other)` — method; returns `OUT`.
- `Integer.__imul__(self, other)` — method; returns `OUT`.
- `Integer.divide(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__floordiv__(self, other)` — method; returns `OUT`.
- `Integer.__rfloordiv__(self, other)` — method; returns `OUT`.
- `Integer.__ifloordiv__(self, other)` — method; returns `OUT`.
- `Integer.power(self, exponent: Integer=None)` — method; returns `OUT`.
- `Integer.__pow__(self, other)` — method; returns `OUT`.
- `Integer.__rpow__(self, other)` — method; returns `OUT`.
- `Integer.__ipow__(self, other)` — method; returns `OUT`.
- `Integer.modulo(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.__mod__(self, other)` — method; returns `OUT`.
- `Integer.__rmod__(self, other)` — method; returns `OUT`.
- `Integer.__imod__(self, other)` — method; returns `OUT`.
- `Integer.abs(self)` — method; returns `OUT`.
- `Integer.__abs__(self)` — method; returns `OUT`.
- `Integer.negate(self)` — method; returns `OUT`.
- `Integer.__neg__(self)` — method; returns `OUT`.
- `Integer.multiply_add(self, multiplier: Integer=None, addend: Integer=None)` — method; returns `OUT`.
- `Integer.sign(self)` — method; returns `OUT`.
- `Integer.min(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.max(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_round(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_floor(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.divide_ceil(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.floored_modulo(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.gcd(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.lcm(self, value: Integer=None)` — method; returns `OUT`.
- `Integer.integer_math(self, value: Integer=None, addend: Integer=None, *, multiplier: Integer=None, exponent: Integer=None, operation: T_OPERATION_4='ADD')` — method; returns `OUT`.

## Interpolate Curves

Blender identifier: `GeometryNodeInterpolateCurves`

### nd

- `nd.interpolate_curves(cls, guide_curves: Curve=None, guide_up: Vector=None, guide_group_id: Integer=None, points: Cloud=None, point_up: Vector=None, point_group_id: Integer=None, max_neighbors: Integer=None)` — class method; returns `OUT`.

### Curve

- `Curve.interpolate(self, guide_up: Vector=None, guide_group_id: Integer=None, points: Cloud=None, point_up: Vector=None, point_group_id: Integer=None, max_neighbors: Integer=None)` — method; returns `OUT`.

## Invert Matrix

Blender identifier: `FunctionNodeInvertMatrix`

### nd

- `nd.invert_matrix(cls, matrix: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.invert(self)` — method; returns `OUT`.

## Invert Rotation

Blender identifier: `FunctionNodeInvertRotation`

### nd

- `nd.invert_rotation(cls, rotation: Rotation=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.invert(self)` — method; returns `OUT`.

## Is Edge Smooth

Blender identifier: `GeometryNodeInputEdgeSmooth`

### nd

- `nd.is_edge_smooth(cls)` — property; returns `OUT`.

### Edge

- `Edge.shade_smooth(self)` — property; returns `OUT`.
- `Edge.smooth(self)` — property; returns `OUT`.

## Is Face Planar

Blender identifier: `GeometryNodeInputMeshFaceIsPlanar`

### nd

- `nd.is_face_planar(cls, threshold: Float=None)` — class method; returns `OUT`.

## Is Face Smooth

Blender identifier: `GeometryNodeInputShadeSmooth`

### nd

- `nd.is_face_smooth(cls)` — property; returns `OUT`.

### Face

- `Face.shade_smooth(self)` — property; returns `OUT`.
- `Face.smooth(self)` — property; returns `OUT`.

## Is Spline Cyclic

Blender identifier: `GeometryNodeInputSplineCyclic`

### nd

- `nd.is_spline_cyclic(cls)` — property; returns `OUT`.

### Spline

- `Spline.is_cyclic(self)` — property; returns `OUT`.

### Curve

- `Curve.is_cyclic(self)` — property; returns `OUT`.

## Is Viewport

Blender identifier: `GeometryNodeIsViewport`

### nd

- `nd.is_viewport(cls)` — property; returns `OUT`.

## Join Bundle

Blender identifier: `NodeJoinBundle`

### nd

- `nd.join_bundle(cls, *bundle: Bundle)` — class method; returns `OUT`.

### Bundle

- `Bundle.join(self, *bundle: Bundle)` — method; returns `OUT`.

## Join Geometry

Blender identifier: `GeometryNodeJoinGeometry`

### nd

- `nd.join_geometry(cls, *geometry: Geometry)` — class method; returns `OUT`.

### Geometry

- `Geometry.join(self, *geometry: Geometry)` — method; returns `OUT`.

## Join Strings

Blender identifier: `GeometryNodeStringJoin`

### nd

- `nd.join_strings(cls, *strings: String, delimiter: String=None)` — class method; returns `OUT`.

### String

- `String.join(self, *strings: String)` — method; returns `OUT`.

## Linear Gizmo

Blender identifier: `GeometryNodeGizmoLinear`

### nd

- `nd.linear_gizmo(cls, *value: Float, position: Vector=None, direction: Vector=None, color_id: T_COLOR_ID_1='PRIMARY', draw_style: T_DRAW_STYLE_1='ARROW')` — class method; returns `OUT`.

### Float

- `Float.linear_gizmo(self, *value: Float, position: Vector=None, direction: Vector=None, color_id: T_COLOR_ID_1='PRIMARY', draw_style: T_DRAW_STYLE_1='ARROW')` — method; returns `OUT`.

## List Length

Blender identifier: `GeometryNodeListLength`

### nd

- `nd.list_length(cls, list: Socket=None, data_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.list_length(self)` — method; returns `OUT`.

### Integer

- `Integer.list_length(self)` — method; returns `OUT`.

### Boolean

- `Boolean.list_length(self)` — method; returns `OUT`.

### Vector

- `Vector.list_length(self)` — method; returns `OUT`.

### Color

- `Color.list_length(self)` — method; returns `OUT`.

### Rotation

- `Rotation.list_length(self)` — method; returns `OUT`.

### Matrix

- `Matrix.list_length(self)` — method; returns `OUT`.

### String

- `String.list_length(self)` — method; returns `OUT`.

### Menu

- `Menu.list_length(self)` — method; returns `OUT`.

### Object

- `Object.list_length(self)` — method; returns `OUT`.

### Image

- `Image.list_length(self)` — method; returns `OUT`.

### Geometry

- `Geometry.list_length(self)` — method; returns `OUT`.

### Collection

- `Collection.list_length(self)` — method; returns `OUT`.

### Material

- `Material.list_length(self)` — method; returns `OUT`.

### Bundle

- `Bundle.list_length(self)` — method; returns `OUT`.

### Closure

- `Closure.list_length(self)` — method; returns `OUT`.

### Font

- `Font.list_length(self)` — method; returns `OUT`.

### Sound

- `Sound.list_length(self)` — method; returns `OUT`.

## Magic Texture

Blender identifier: `ShaderNodeTexMagic`

### nd

- `nd.magic_texture(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, turbulence_depth: int=2)` — class method; returns `OUT`.

### Texture

- `Texture.Magic(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, turbulence_depth: int=2)` — class method; returns `OUT`.

## Map Range

Blender identifier: `ShaderNodeMapRange`

### nd

- `nd.map_range(cls, value: Float=None, from_min: Socket=None, from_max: Socket=None, to_min: Socket=None, to_max: Socket=None, steps: Socket=None, vector: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR', data_type: T_DATA_TYPE_3='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.map_range(self, from_min: Float=None, from_max: Float=None, to_min: Float=None, to_max: Float=None, steps: Float=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.
- `Float.interpolate(self, to_min: Float=None, to_max: Float=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.

### Vector

- `Vector.map_range(self, from_min: Vector=None, from_max: Vector=None, to_min: Vector=None, to_max: Vector=None, steps: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.
- `Vector.interpolate(self, to_min: Vector=None, to_max: Vector=None, clamp: bool=True, interpolation_type: T_INTERPOLATION_TYPE_1='LINEAR')` — method; returns `OUT`.

## Match String

Blender identifier: `FunctionNodeMatchString`

### nd

- `nd.match_string(cls, string: String=None, key: String=None, operation: Menu=None)` — class method; returns `OUT`.

### String

- `String.match(self, key: String=None, operation: Menu=None)` — method; returns `OUT`.

## Material

Blender identifier: `GeometryNodeInputMaterial`

### nd

- `nd.material(cls, material=None)` — class method; returns `OUT`.

## Material Index

Blender identifier: `GeometryNodeInputMaterialIndex`

### nd

- `nd.material_index(cls)` — property; returns `OUT`.

### Face

- `Face.material_index(self)` — property; returns `OUT`.

### Mesh

- `Mesh.material_index(self)` — property; returns `OUT`.

### Spline

- `Spline.material_index(self)` — property; returns `OUT`.

## Material Selection

Blender identifier: `GeometryNodeMaterialSelection`

### nd

- `nd.material_selection(cls, material: Material=None)` — class method; returns `OUT`.

### Material

- `Material.material_selection(self)` — method; returns `OUT`.

## Math

Blender identifier: `ShaderNodeMath`

### nd

- `nd.math(cls, value: Float=None, value_1: Float=None, addend: Float=None, *, base: Float=None, degrees: Float=None, radians: Float=None, multiplier: Float=None, exponent: Float=None, base_1: Float=None, threshold: Float=None, max: Float=None, increment: Float=None, scale: Float=None, epsilon: Float=None, distance: Float=None, min: Float=None, use_clamp: bool=False, operation: T_OPERATION_5='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.add(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.subtract(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.multiply(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.divide(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.power(base: Float=None, exponent: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.modulo(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.abs(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.round(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.trunc(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.floor(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.ceil(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.multiply_add(value: Float=None, multiplier: Float=None, addend: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.log(value: Float=None, base: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sqrt(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.inverse_sqrt(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.exp(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.min(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.max(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sign(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.smooth_min(value: Float=None, value_1: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.smooth_max(value: Float=None, value_1: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.fract(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.floored_modulo(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.wrap(value: Float=None, max: Float=None, min: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.snap(value: Float=None, increment: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.pingpong(value: Float=None, scale: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sin(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.cos(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.tan(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.asin(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.acos(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.arctangent(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.atan2(value: Float=None, value_1: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.sinh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.cosh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.tanh(value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.radians(degrees: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.degrees(radians: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.math_less_than(value: Float=None, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.math_greater_than(value: Float=None, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `gnmath.math_compare(value: Float=None, value_1: Float=None, epsilon: Float=None, use_clamp: bool=False)` — method; returns `OUT`.

### Float

- `Float.add(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__add__(self, other)` — method; returns `OUT`.
- `Float.__radd__(self, other)` — method; returns `OUT`.
- `Float.__iadd__(self, other)` — method; returns `OUT`.
- `Float.subtract(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__sub__(self, other)` — method; returns `OUT`.
- `Float.__rsub__(self, other)` — method; returns `OUT`.
- `Float.__isub__(self, other)` — method; returns `OUT`.
- `Float.multiply(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__mul__(self, other)` — method; returns `OUT`.
- `Float.__rmul__(self, other)` — method; returns `OUT`.
- `Float.__imul__(self, other)` — method; returns `OUT`.
- `Float.__neg__(self)` — method; returns `OUT`.
- `Float.divide(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__truediv__(self, other)` — method; returns `OUT`.
- `Float.__rtruediv__(self, other)` — method; returns `OUT`.
- `Float.__itruediv__(self, other)` — method; returns `OUT`.
- `Float.power(self, exponent: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__pow__(self, other)` — method; returns `OUT`.
- `Float.__rpow__(self, other)` — method; returns `OUT`.
- `Float.__ipow__(self, other)` — method; returns `OUT`.
- `Float.modulo(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__mod__(self, other)` — method; returns `OUT`.
- `Float.__rmod__(self, other)` — method; returns `OUT`.
- `Float.__imod__(self, other)` — method; returns `OUT`.
- `Float.abs(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__abs__(self)` — method; returns `OUT`.
- `Float.round(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__round__(self)` — method; returns `OUT`.
- `Float.trunc(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__trunc__(self)` — method; returns `OUT`.
- `Float.floor(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__floor__(self)` — method; returns `OUT`.
- `Float.ceil(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.__ceil__(self)` — method; returns `OUT`.
- `Float.multiply_add(self, multiplier: Float=None, addend: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.log(self, base: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sqrt(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.inverse_sqrt(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.exp(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.min(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.max(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sign(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.smooth_min(self, value: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.smooth_max(self, value: Float=None, distance: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.fract(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.floored_modulo(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.wrap(self, max: Float=None, min: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.snap(self, increment: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.pingpong(self, scale: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sin(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.cos(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.tan(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.asin(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.acos(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.arctangent(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.atan2(self, value: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.sinh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.cosh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.tanh(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.radians(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.degrees(self, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.math_less_than(self, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.math_greater_than(self, threshold: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.math_compare(self, value: Float=None, epsilon: Float=None, use_clamp: bool=False)` — method; returns `OUT`.
- `Float.math(self, value: Float=None, addend: Float=None, *, multiplier: Float=None, exponent: Float=None, base: Float=None, threshold: Float=None, max: Float=None, increment: Float=None, scale: Float=None, epsilon: Float=None, distance: Float=None, min: Float=None, use_clamp: bool=False, operation: T_OPERATION_5='ADD')` — method; returns `OUT`.

## Matrix Determinant

Blender identifier: `FunctionNodeMatrixDeterminant`

### nd

- `nd.matrix_determinant(cls, matrix: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.determinant(self)` — method; returns `OUT`.

## Matrix SVD

Blender identifier: `FunctionNodeMatrixSVD`

### nd

- `nd.matrix_svd(cls, matrix: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.matrix_svd(self)` — method; returns `OUT`.

## Menu

Blender identifier: `FunctionNodeInputMenu`

### nd

- `nd.menu(cls, value: str='')` — class method; returns `OUT`.

## Menu Switch

Blender identifier: `GeometryNodeMenuSwitch`

### nd

- `nd.menu_switch(cls, named_sockets: dict={}, menu: Menu=None, data_type: T_DATA_TYPE_6='GEOMETRY', **sockets)` — class method; returns `OUT`.

### Float

- `Float.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Integer

- `Integer.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Boolean

- `Boolean.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Vector

- `Vector.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Color

- `Color.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Rotation

- `Rotation.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Matrix

- `Matrix.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### String

- `String.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Menu

- `Menu.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Object

- `Object.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Image

- `Image.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Geometry

- `Geometry.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Collection

- `Collection.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Material

- `Material.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Bundle

- `Bundle.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Closure

- `Closure.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Font

- `Font.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

### Sound

- `Sound.menu_switch(self, named_sockets: dict={}, menu: Menu=None, **sockets)` — method; returns `OUT`.

## Merge Layers

Blender identifier: `GeometryNodeMergeLayers`

### nd

- `nd.merge_layers(cls, grease_pencil: GreasePencil=None, selection: Boolean=None, group_id: Integer=None, mode_1: Menu=None, mode: T_MODE_10='MERGE_BY_NAME')` — class method; returns `OUT`.

### GreasePencil

- `GreasePencil.merge_layers(self, group_id: Integer=None, mode_1: Menu=None, mode: T_MODE_10='MERGE_BY_NAME')` — method; returns `OUT`.

## Merge Points

Blender identifier: `GeometryNodeMergePoints`

### nd

- `nd.merge_points(cls, geometry: Geometry=None, selection: Boolean=None, merge_id: Integer=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.merge_points(self, merge_id: Integer=None)` — method; returns `OUT`.

## Merge by Distance

Blender identifier: `GeometryNodeMergeByDistance`

### nd

- `nd.merge_by_distance(cls, geometry: Geometry=None, selection: Boolean=None, distance: Float=None, mode: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.merge_by_distance(self, distance: Float=None, mode: Menu=None)` — method; returns `OUT`.

## Mesh Bevel

Blender identifier: `GeometryNodeMeshBevel`

### nd

- `nd.mesh_bevel(cls, mesh: Mesh=None, selection: Boolean=None, start_left_offset: Float=None, start_right_offset: Float=None, end_left_offset: Float=None, end_right_offset: Float=None, offset: Float=None, miter: Boolean=None, spread: Float=None, segments: Integer=None, shape: Float=None, profile: Geometry=None, affect_kind: Menu=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.bevel(self, start_left_offset: Float=None, start_right_offset: Float=None, end_left_offset: Float=None, end_right_offset: Float=None, offset: Float=None, miter: Boolean=None, spread: Float=None, segments: Integer=None, shape: Float=None, profile: Geometry=None, affect_kind: Menu=None)` — method; returns `OUT`.

## Mesh Boolean

Blender identifier: `GeometryNodeMeshBoolean`

### nd

- `nd.mesh_boolean(cls, *mesh: Mesh, mesh_1: Mesh=None, self_intersection: Boolean=None, hole_tolerant: Boolean=None, operation: T_OPERATION_6='DIFFERENCE', solver: T_SOLVER_1='FLOAT')` — class method; returns `OUT`.

### Mesh

- `Mesh.boolean(self, *mesh: Mesh, self_intersection: Boolean=None, hole_tolerant: Boolean=None, operation: T_OPERATION_6='DIFFERENCE', solver: T_SOLVER_1='FLOAT')` — method; returns `OUT`.
- `Mesh.intersect(self, *mesh: Mesh, self_intersection: Boolean=None, hole_tolerant: Boolean=None, solver: T_SOLVER_1='FLOAT')` — method; returns `OUT`.
- `Mesh.union(self, *mesh: Mesh, self_intersection: Boolean=None, hole_tolerant: Boolean=None, solver: T_SOLVER_1='FLOAT')` — method; returns `OUT`.
- `Mesh.difference(self, *mesh_2: Mesh, self_intersection: Boolean=None, hole_tolerant: Boolean=None, solver: T_SOLVER_1='FLOAT')` — method; returns `OUT`.

## Mesh Circle

Blender identifier: `GeometryNodeMeshCircle`

### nd

- `nd.mesh_circle(cls, vertices: Integer=None, radius: Float=None, fill_type: T_FILL_TYPE_1='NONE')` — class method; returns `OUT`.

### Mesh

- `Mesh.Circle(cls, vertices: Integer=None, radius: Float=None, fill_type: T_FILL_TYPE_1='NONE')` — class method; returns `OUT`.

## Mesh Island

Blender identifier: `GeometryNodeInputMeshIsland`

### nd

- `nd.mesh_island(cls)` — class method; returns `OUT`.

## Mesh Line

Blender identifier: `GeometryNodeMeshLine`

### nd

- `nd.mesh_line(cls, count: Integer=None, resolution: Float=None, start_location: Vector=None, offset: Vector=None, *, end_location: Vector=None, mode: T_MODE_11='OFFSET', count_mode: T_COUNT_MODE_1='TOTAL')` — class method; returns `OUT`.

### Mesh

- `Mesh.Line(cls, count: Integer=None, resolution: Float=None, start_location: Vector=None, offset: Vector=None, *, end_location: Vector=None, mode: T_MODE_11='OFFSET', count_mode: T_COUNT_MODE_1='TOTAL')` — class method; returns `OUT`.

## Mesh to Curve

Blender identifier: `GeometryNodeMeshToCurve`

### nd

- `nd.mesh_to_curve(cls, mesh: Mesh=None, selection: Boolean=None, mode: T_MODE_12='EDGES')` — class method; returns `OUT`.

### Mesh

- `Mesh.to_curve(self, mode: T_MODE_12='EDGES')` — method; returns `OUT`.

## Mesh to Density Grid

Blender identifier: `GeometryNodeMeshToDensityGrid`

### nd

- `nd.mesh_to_density_grid(cls, mesh: Mesh=None, density: Float=None, voxel_size: Float=None, gradient_width: Float=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.to_density_grid(self, density: Float=None, voxel_size: Float=None, gradient_width: Float=None)` — method; returns `OUT`.

## Mesh to Points

Blender identifier: `GeometryNodeMeshToPoints`

### nd

- `nd.mesh_to_points(cls, mesh: Mesh=None, selection: Boolean=None, position: Vector=None, radius: Float=None, mode: T_MODE_13='VERTICES')` — class method; returns `OUT`.

### Geometry

- `Geometry.to_points(self, position: Vector=None, radius: Float=None, mode: T_MODE_13='VERTICES')` — method; returns `OUT`.

### Vertex

- `Vertex.to_points(self, position: Vector=None, radius: Float=None)` — method; returns `OUT`.

### Edge

- `Edge.to_points(self, position: Vector=None, radius: Float=None)` — method; returns `OUT`.

### Face

- `Face.to_points(self, position: Vector=None, radius: Float=None)` — method; returns `OUT`.

### Corner

- `Corner.to_points(self, position: Vector=None, radius: Float=None)` — method; returns `OUT`.

## Mesh to SDF Grid

Blender identifier: `GeometryNodeMeshToSDFGrid`

### nd

- `nd.mesh_to_sdf_grid(cls, mesh: Mesh=None, voxel_size: Float=None, band_width: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.to_sdf_grid(self, voxel_size: Float=None, band_width: Integer=None)` — method; returns `OUT`.

## Mesh to Volume

Blender identifier: `GeometryNodeMeshToVolume`

### nd

- `nd.mesh_to_volume(cls, mesh: Mesh=None, density: Float=None, voxel_size: Float=None, voxel_amount: Float=None, interior_band_width: Float=None, resolution_mode: Menu=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.to_volume(self, density: Float=None, voxel_size: Float=None, voxel_amount: Float=None, interior_band_width: Float=None, resolution_mode: Menu=None)` — method; returns `OUT`.

## Mix

Blender identifier: `ShaderNodeMix`

### nd

- `nd.mix(cls, a: Socket=None, b: Socket=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, data_type: T_DATA_TYPE_11='FLOAT', factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.

### Float

- `Float.Mix(cls, a: Float=None, b: Float=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Float.mix(self, b: Float=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

### Vector

- `Vector.Mix(cls, a: Vector=None, b: Vector=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Vector.mix(self, b: Vector=None, factor: Socket=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

### Color

- `Color.Mix(cls, a: Color=None, b: Color=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Color.mix(self, b: Color=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

### Rotation

- `Rotation.Mix(cls, a: Rotation=None, b: Rotation=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.
- `Rotation.mix(self, b: Rotation=None, factor: Float=None, clamp_factor: bool=True, clamp_result: bool=False, factor_mode: T_FACTOR_MODE_1='UNIFORM', blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

## Mix (Legacy)

Blender identifier: `ShaderNodeMixRGB`

### nd

- `nd.mix_legacy_(cls, color1: Color=None, color2: Color=None, factor: Float=None, use_alpha: bool=False, use_clamp: bool=False, blend_type: T_BLEND_TYPE_1='MIX')` — class method; returns `OUT`.

### Float

- `Float.mix_legacy_(self, color1: Color=None, color2: Color=None, use_alpha: bool=False, use_clamp: bool=False, blend_type: T_BLEND_TYPE_1='MIX')` — method; returns `OUT`.

## Mouse Position

Blender identifier: `GeometryNodeToolMousePosition`

### nd

- `nd.mouse_position(cls)` — class method; returns `OUT`.

## Multiply Matrices

Blender identifier: `FunctionNodeMatrixMultiply`

### nd

- `nd.multiply_matrices(cls, matrix: Matrix=None, matrix_1: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.multiply(self, matrix: Matrix=None)` — method; returns `OUT`.

## NURBS Order

Blender identifier: `GeometryNodeNURBSOrder`

### nd

- `nd.nurbs_order(cls)` — property; returns `OUT`.

## NURBS Weight

Blender identifier: `GeometryNodeNURBSWeight`

### nd

- `nd.nurbs_weight(cls)` — property; returns `OUT`.

## Named Attribute

Blender identifier: `GeometryNodeInputNamedAttribute`

### nd

- `nd.named_attribute(cls, name: String=None, data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

## Named Layer Selection

Blender identifier: `GeometryNodeInputNamedLayerSelection`

### nd

- `nd.named_layer_selection(cls, name: String=None)` — class method; returns `OUT`.

## Noise Texture

Blender identifier: `ShaderNodeTexNoise`

### nd

- `nd.noise_texture(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, offset: Float=None, gain: Float=None, distortion: Float=None, normalize: bool=True, noise_dimensions: T_NOISE_DIMENSIONS_1='3D', noise_type: T_NOISE_TYPE_1='FBM')` — class method; returns `OUT`.

### Texture

- `Texture.Noise(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, offset: Float=None, gain: Float=None, distortion: Float=None, normalize: bool=True, noise_dimensions: T_NOISE_DIMENSIONS_1='3D', noise_type: T_NOISE_TYPE_1='FBM')` — class method; returns `OUT`.

## Normal

Blender identifier: `GeometryNodeInputNormal`

### nd

- `nd.normal(cls)` — property; returns `Normal`.
- `nd.true_normal(cls)` — property; returns `True Normal`.

## Object

Blender identifier: `GeometryNodeInputObject`

### nd

- `nd.object(cls, object=None)` — class method; returns `OUT`.

## Object Info

Blender identifier: `GeometryNodeObjectInfo`

### nd

- `nd.object_info(cls, object: Object=None, as_instance: Boolean=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — class method; returns `OUT`.

### Object

- `Object.info(self, as_instance: Boolean=None, transform_space: T_TRANSFORM_SPACE_1='ORIGINAL')` — method; returns `OUT`.

## Offset Corner in Face

Blender identifier: `GeometryNodeOffsetCornerInFace`

### nd

- `nd.offset_corner_in_face(cls, corner_index: Integer=None, offset: Integer=None)` — class method; returns `OUT`.

## Offset Point in Curve

Blender identifier: `GeometryNodeOffsetPointInCurve`

### nd

- `nd.offset_point_in_curve(cls, point_index: Integer=None, offset: Integer=None)` — class method; returns `OUT`.

## Pack UV Islands

Blender identifier: `GeometryNodeUVPackIslands`

### nd

- `nd.pack_uv_islands(cls, uv: Vector=None, selection: Boolean=None, margin: Float=None, rotate: Boolean=None, bottom_left: Vector=None, top_right: Vector=None, method: Menu=None)` — class method; returns `OUT`.

### Vector

- `Vector.pack_uv_islands(self, selection: Boolean=None, margin: Float=None, rotate: Boolean=None, bottom_left: Vector=None, top_right: Vector=None, method: Menu=None)` — method; returns `OUT`.

## Points

Blender identifier: `GeometryNodePoints`

### nd

- `nd.points(cls, count: Integer=None, position: Vector=None, radius: Float=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.Points(cls, count: Integer=None, position: Vector=None, radius: Float=None)` — class method; returns `OUT`.

## Points of Curve

Blender identifier: `GeometryNodePointsOfCurve`

### nd

- `nd.points_of_curve(cls, curve_index: Integer=None, weights: Float=None, sort_index: Integer=None)` — class method; returns `OUT`.

## Points to Curves

Blender identifier: `GeometryNodePointsToCurves`

### nd

- `nd.points_to_curves(cls, points: Cloud=None, curve_group_id: Integer=None, weight: Float=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.to_curves(self, curve_group_id: Integer=None, weight: Float=None)` — method; returns `OUT`.

## Points to SDF Grid

Blender identifier: `GeometryNodePointsToSDFGrid`

### nd

- `nd.points_to_sdf_grid(cls, points: Cloud=None, radius: Float=None, voxel_size: Float=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.to_sdf_grid(self, radius: Float=None, voxel_size: Float=None)` — method; returns `OUT`.

## Points to Vertices

Blender identifier: `GeometryNodePointsToVertices`

### nd

- `nd.points_to_vertices(cls, points: Cloud=None, selection: Boolean=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.to_vertices(self)` — method; returns `OUT`.

## Points to Volume

Blender identifier: `GeometryNodePointsToVolume`

### nd

- `nd.points_to_volume(cls, points: Cloud=None, density: Float=None, voxel_size: Float=None, voxel_amount: Float=None, radius: Float=None, resolution_mode: Menu=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.to_volume(self, density: Float=None, voxel_size: Float=None, voxel_amount: Float=None, radius: Float=None, resolution_mode: Menu=None)` — method; returns `OUT`.

## Position

Blender identifier: `GeometryNodeInputPosition`

### nd

- `nd.position(cls)` — property; returns `OUT`.

### Geometry

- `Geometry.position(self)` — property; returns `OUT`.

### Point

- `Point.position(self)` — property; returns `OUT`.

## Project Point

Blender identifier: `FunctionNodeProjectPoint`

### nd

- `nd.project_point(cls, vector: Vector=None, transform: Matrix=None)` — class method; returns `OUT`.

### Vector

- `Vector.project_point(self, transform: Matrix=None)` — method; returns `OUT`.

## Prune Grid

Blender identifier: `GeometryNodeGridPrune`

### nd

- `nd.prune_grid(cls, grid: Socket=None, threshold: Socket=None, mode: Menu=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.prune_grid(self, threshold: Float=None, mode: Menu=None)` — method; returns `OUT`.

### Integer

- `Integer.prune_grid(self, threshold: Integer=None, mode: Menu=None)` — method; returns `OUT`.

### Boolean

- `Boolean.prune_grid(self, mode: Menu=None)` — method; returns `OUT`.

### Vector

- `Vector.prune_grid(self, threshold: Vector=None, mode: Menu=None)` — method; returns `OUT`.

## Quadratic Bézier

Blender identifier: `GeometryNodeCurveQuadraticBezier`

### nd

- `nd.quadratic_bezier(cls, resolution: Integer=None, start: Vector=None, middle: Vector=None, end: Vector=None)` — class method; returns `OUT`.

### Curve

- `Curve.QuadraticBezier(cls, resolution: Integer=None, start: Vector=None, middle: Vector=None, end: Vector=None)` — class method; returns `OUT`.

## Quadrilateral

Blender identifier: `GeometryNodeCurvePrimitiveQuadrilateral`

### nd

- `nd.quadrilateral(cls, width: Float=None, height: Float=None, bottom_width: Float=None, top_width: Float=None, offset: Float=None, bottom_height: Float=None, top_height: Float=None, point_1: Vector=None, point_2: Vector=None, point_3: Vector=None, point_4: Vector=None, mode: T_MODE_14='RECTANGLE')` — class method; returns `OUT`.

### Curve

- `Curve.Quadrilateral(cls, width: Float=None, height: Float=None, bottom_width: Float=None, top_width: Float=None, offset: Float=None, bottom_height: Float=None, top_height: Float=None, point_1: Vector=None, point_2: Vector=None, point_3: Vector=None, point_4: Vector=None, mode: T_MODE_14='RECTANGLE')` — class method; returns `OUT`.

## Quaternion to Rotation

Blender identifier: `FunctionNodeQuaternionToRotation`

### nd

- `nd.quaternion_to_rotation(cls, w: Float=None, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.FromQuaternion(cls, w: Float=None, x: Float=None, y: Float=None, z: Float=None)` — class method; returns `OUT`.

## RGB Curves

Blender identifier: `ShaderNodeRGBCurve`

### nd

- `nd.rgb_curves(cls, color: Color=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.rgb_curves(self, color: Color=None)` — method; returns `OUT`.

## Radial Tiling

Blender identifier: `ShaderNodeRadialTiling`

### nd

- `nd.radial_tiling(cls, vector: Vector=None, sides: Float=None, roundness: Float=None, normalize: bool=False)` — class method; returns `OUT`.

### Vector

- `Vector.radial_tiling(self, sides: Float=None, roundness: Float=None, normalize: bool=False)` — method; returns `OUT`.

## Radius

Blender identifier: `GeometryNodeInputRadius`

### nd

- `nd.radius(cls)` — property; returns `OUT`.

### Cloud

- `Cloud.radius(self)` — property; returns `OUT`.

### CloudPoint

- `CloudPoint.radius(self)` — property; returns `OUT`.

### Curve

- `Curve.radius(self)` — property; returns `OUT`.

### SplinePoint

- `SplinePoint.radius(self)` — property; returns `OUT`.

## Random Value

Blender identifier: `FunctionNodeRandomValue`

### nd

- `nd.random_value(cls, min: Socket=None, probability: Float=None, max: Socket=None, id: Integer=None, seed: Integer=None, data_type: T_DATA_TYPE_12='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.Random(cls, min: Float=None, max: Float=None, id: Integer=None, seed: Integer=None)` — class method; returns `OUT`.

### Integer

- `Integer.Random(cls, min: Integer=None, max: Integer=None, id: Integer=None, seed: Integer=None)` — class method; returns `OUT`.

### Boolean

- `Boolean.Random(cls, probability: Float=None, id: Integer=None, seed: Integer=None)` — class method; returns `OUT`.

### Vector

- `Vector.Random(cls, min: Vector=None, max: Vector=None, id: Integer=None, seed: Integer=None)` — class method; returns `OUT`.

## Rasterize Points

Blender identifier: `GeometryNodeRasterizePoints`

### nd

- `nd.rasterize_points(cls, points: Cloud=None, voxel_size: Float=None, matrix: Matrix=None, position: Vector=None, named_sockets: dict={}, grid_transform_mode: Menu=None, kernel_type: Menu=None, **sockets)` — class method; returns `OUT`.

### Cloud

- `Cloud.rasterize_points(self, voxel_size: Float=None, matrix: Matrix=None, position: Vector=None, named_sockets: dict={}, grid_transform_mode: Menu=None, kernel_type: Menu=None, **sockets)` — method; returns `OUT`.

## Raycast

Blender identifier: `GeometryNodeRaycast`

### nd

- `nd.raycast(cls, target_geometry: Geometry=None, attribute: Socket=None, source_position: Vector=None, ray_direction: Vector=None, ray_length: Float=None, interpolation: Menu=None, data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Geometry

- `Geometry.raycast(self, attribute: Socket=None, source_position: Vector=None, ray_direction: Vector=None, ray_length: Float=None, interpolation: Menu=None)` — method; returns `OUT`.

## Realize Instances

Blender identifier: `GeometryNodeRealizeInstances`

### nd

- `nd.realize_instances(cls, geometry: Geometry=None, selection: Boolean=None, realize_all: Boolean=None, depth: Integer=None, preserve_normals: Boolean=None, realize_to_point_domain: bool=False)` — class method; returns `OUT`.

### Geometry

- `Geometry.realize(self, realize_all: Boolean=None, depth: Integer=None, preserve_normals: Boolean=None, realize_to_point_domain: bool=False)` — method; returns `OUT`.

## Remove Named Attribute

Blender identifier: `GeometryNodeRemoveAttribute`

### nd

- `nd.remove_named_attribute(cls, geometry: Geometry=None, name: String=None, pattern_mode: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.remove(self, name: String=None, pattern_mode: Menu=None)` — method; returns `OUT`.
- `Geometry.remove_named_attribute(self, name: String=None, pattern_mode: Menu=None)` — method; returns `OUT`.

## Rename Attribute

Blender identifier: `GeometryNodeRenameAttribute`

### nd

- `nd.rename_attribute(cls, geometry: Geometry=None, old: String=None, new: String=None, overwrite: Boolean=None, mode: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.rename_attribute(self, old: String=None, new: String=None, overwrite: Boolean=None, mode: Menu=None)` — method; returns `OUT`.

## Replace Material

Blender identifier: `GeometryNodeReplaceMaterial`

### nd

- `nd.replace_material(cls, geometry: Geometry=None, old: Material=None, new: Material=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.replace_material(self, old: Material=None, new: Material=None)` — method; returns `OUT`.

## Replace String

Blender identifier: `FunctionNodeReplaceString`

### nd

- `nd.replace_string(cls, string: String=None, find: String=None, replace: String=None)` — class method; returns `OUT`.

### String

- `String.replace(self, find: String=None, replace: String=None)` — method; returns `OUT`.

## Resample Curve

Blender identifier: `GeometryNodeResampleCurve`

### nd

- `nd.resample_curve(cls, curve: Curve=None, selection: Boolean=None, count: Integer=None, length: Float=None, mode: Menu=None, keep_last_segment: bool=True)` — class method; returns `OUT`.

### Curve

- `Curve.resample(self, count: Integer=None, length: Float=None, mode: Menu=None, keep_last_segment: bool=True)` — method; returns `OUT`.

## Reverse Curve

Blender identifier: `GeometryNodeReverseCurve`

### nd

- `nd.reverse_curve(cls, curve: Curve=None, selection: Boolean=None)` — class method; returns `OUT`.

### Curve

- `Curve.reverse(self)` — method; returns `OUT`.

## Reverse String

Blender identifier: `FunctionNodeReverseString`

### nd

- `nd.reverse_string(cls, string: String=None)` — class method; returns `OUT`.

### String

- `String.reverse(self)` — method; returns `OUT`.

## Rotate Instances

Blender identifier: `GeometryNodeRotateInstances`

### nd

- `nd.rotate_instances(cls, instances: Instances=None, selection: Boolean=None, rotation: Rotation=None, pivot_point: Vector=None, local_space: Boolean=None)` — class method; returns `OUT`.

### Instances

- `Instances.rotate(self, rotation: Rotation=None, pivot_point: Vector=None, local_space: Boolean=None)` — method; returns `OUT`.

## Rotate Rotation

Blender identifier: `FunctionNodeRotateRotation`

### nd

- `nd.rotate_rotation(cls, rotation: Rotation=None, rotate_by: Rotation=None, rotation_space: T_ROTATION_SPACE_1='GLOBAL')` — class method; returns `OUT`.

### Rotation

- `Rotation.rotate(self, rotate_by: Rotation=None, rotation_space: T_ROTATION_SPACE_1='GLOBAL')` — method; returns `OUT`.

## Rotate Vector

Blender identifier: `FunctionNodeRotateVector`

### nd

- `nd.rotate_vector(cls, vector: Vector=None, rotation: Rotation=None)` — class method; returns `OUT`.

### Vector

- `Vector.rotate(self, rotation: Rotation=None)` — method; returns `OUT`.

### Rotation

- `Rotation.rotate_vector(self, vector: Vector=None)` — method; returns `OUT`.

## Rotation

Blender identifier: `FunctionNodeInputRotation`

### nd

- `nd.rotation(cls, rotation_euler: tuple[float, float, float]=None)` — class method; returns `OUT`.

## Rotation to Axis Angle

Blender identifier: `FunctionNodeRotationToAxisAngle`

### nd

- `nd.rotation_to_axis_angle(cls, rotation: Rotation=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.to_axis_angle(self)` — method; returns `OUT`.

## Rotation to Euler

Blender identifier: `FunctionNodeRotationToEuler`

### nd

- `nd.rotation_to_euler(cls, rotation: Rotation=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.to_euler(self)` — method; returns `OUT`.

### Vector

- `Vector.FromRotation(cls, rotation: Rotation=None)` — class method; returns `OUT`.

## Rotation to Quaternion

Blender identifier: `FunctionNodeRotationToQuaternion`

### nd

- `nd.rotation_to_quaternion(cls, rotation: Rotation=None)` — class method; returns `OUT`.

### Rotation

- `Rotation.to_quaternion(self)` — method; returns `OUT`.

## SDF Grid Boolean

Blender identifier: `GeometryNodeSDFGridBoolean`

### nd

- `nd.sdf_grid_boolean(cls, *grid: Float, grid_1: Float=None, operation: T_OPERATION_6='DIFFERENCE')` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_boolean(self, *grid: Float, operation: T_OPERATION_6='DIFFERENCE')` — method; returns `OUT`.

## SDF Grid Fillet

Blender identifier: `GeometryNodeSDFGridFillet`

### nd

- `nd.sdf_grid_fillet(cls, grid: Float=None, iterations: Integer=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_fillet(self, iterations: Integer=None)` — method; returns `OUT`.

## SDF Grid Laplacian

Blender identifier: `GeometryNodeSDFGridLaplacian`

### nd

- `nd.sdf_grid_laplacian(cls, grid: Float=None, iterations: Integer=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_laplacian(self, iterations: Integer=None)` — method; returns `OUT`.

## SDF Grid Mean

Blender identifier: `GeometryNodeSDFGridMean`

### nd

- `nd.sdf_grid_mean(cls, grid: Float=None, width: Integer=None, iterations: Integer=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_mean(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

## SDF Grid Mean Curvature

Blender identifier: `GeometryNodeSDFGridMeanCurvature`

### nd

- `nd.sdf_grid_mean_curvature(cls, grid: Float=None, iterations: Integer=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_mean_curvature(self, iterations: Integer=None)` — method; returns `OUT`.

## SDF Grid Median

Blender identifier: `GeometryNodeSDFGridMedian`

### nd

- `nd.sdf_grid_median(cls, grid: Float=None, width: Integer=None, iterations: Integer=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_median(self, width: Integer=None, iterations: Integer=None)` — method; returns `OUT`.

## SDF Grid Offset

Blender identifier: `GeometryNodeSDFGridOffset`

### nd

- `nd.sdf_grid_offset(cls, grid: Float=None, distance: Float=None)` — class method; returns `OUT`.

### Float

- `Float.sdf_grid_offset(self, distance: Float=None)` — method; returns `OUT`.

## Sample Curve

Blender identifier: `GeometryNodeSampleCurve`

### nd

- `nd.sample_curve(cls, curves: Curve=None, value: Socket=None, length: Float=None, curve_index: Integer=None, factor: Float=None, use_all_curves: bool=False, mode: T_MODE_15='FACTOR', data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Curve

- `Curve.sample(self, value: Socket=None, length: Float=None, curve_index: Integer=None, factor: Float=None, use_all_curves: bool=False, mode: T_MODE_15='FACTOR')` — method; returns `OUT`.
- `Curve.sample_factor(self, value: Socket=None, curve_index: Integer=None, factor: Float=None, use_all_curves: bool=False)` — method; returns `OUT`.
- `Curve.sample_length(self, value: Socket=None, length: Float=None, curve_index: Integer=None, use_all_curves: bool=False)` — method; returns `OUT`.

## Sample Grid

Blender identifier: `GeometryNodeSampleGrid`

### nd

- `nd.sample_grid(cls, grid: Socket=None, position: Vector=None, interpolation: Menu=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.sample_grid(self, position: Vector=None, interpolation: Menu=None)` — method; returns `OUT`.

### Integer

- `Integer.sample_grid(self, position: Vector=None, interpolation: Menu=None)` — method; returns `OUT`.

### Boolean

- `Boolean.sample_grid(self, position: Vector=None, interpolation: Menu=None)` — method; returns `OUT`.

### Vector

- `Vector.sample_grid(self, position: Vector=None, interpolation: Menu=None)` — method; returns `OUT`.

## Sample Grid Index

Blender identifier: `GeometryNodeSampleGridIndex`

### nd

- `nd.sample_grid_index(cls, grid: Socket=None, x: Integer=None, y: Integer=None, z: Integer=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.sample_grid_index(self, x: Integer=None, y: Integer=None, z: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.sample_grid_index(self, x: Integer=None, y: Integer=None, z: Integer=None)` — method; returns `OUT`.

### Boolean

- `Boolean.sample_grid_index(self, x: Integer=None, y: Integer=None, z: Integer=None)` — method; returns `OUT`.

### Vector

- `Vector.sample_grid_index(self, x: Integer=None, y: Integer=None, z: Integer=None)` — method; returns `OUT`.

## Sample Index

Blender identifier: `GeometryNodeSampleIndex`

### nd

- `nd.sample_index(cls, geometry: Geometry=None, value: Socket=None, index: Integer=None, clamp: bool=False, data_type: T_DATA_TYPE_8='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Edge

- `Edge.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Face

- `Face.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Corner

- `Corner.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Spline

- `Spline.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Instance

- `Instance.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

### Layer

- `Layer.sample_index(self, value: Socket=None, index: Integer=None, clamp: bool=False)` — method; returns `OUT`.

## Sample Nearest

Blender identifier: `GeometryNodeSampleNearest`

### nd

- `nd.sample_nearest(cls, geometry: Geometry=None, sample_position: Vector=None, domain: T_DOMAIN_5='POINT')` — class method; returns `OUT`.

### Point

- `Point.sample_nearest(self, sample_position: Vector=None)` — method; returns `OUT`.

### Edge

- `Edge.sample_nearest(self, sample_position: Vector=None)` — method; returns `OUT`.

### Face

- `Face.sample_nearest(self, sample_position: Vector=None)` — method; returns `OUT`.

### Corner

- `Corner.sample_nearest(self, sample_position: Vector=None)` — method; returns `OUT`.

## Sample Nearest Surface

Blender identifier: `GeometryNodeSampleNearestSurface`

### nd

- `nd.sample_nearest_surface(cls, mesh: Mesh=None, value: Socket=None, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None, data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Mesh

- `Mesh.sample_nearest_surface(self, value: Socket=None, group_id: Integer=None, sample_position: Vector=None, sample_group_id: Integer=None)` — method; returns `OUT`.

## Sample Sound Frequencies

Blender identifier: `GeometryNodeSampleSoundFrequencies`

### nd

- `nd.sample_sound_frequencies(cls, sound: Sound=None, time: Float=None, all_channels: Boolean=None, channel: Integer=None, low: Float=None, high: Float=None, fft_size: Menu=None, window_function: Menu=None)` — class method; returns `OUT`.

### Sound

- `Sound.sample_sound_frequencies(self, time: Float=None, all_channels: Boolean=None, channel: Integer=None, low: Float=None, high: Float=None, fft_size: Menu=None, window_function: Menu=None)` — method; returns `OUT`.

## Sample UV Surface

Blender identifier: `GeometryNodeSampleUVSurface`

### nd

- `nd.sample_uv_surface(cls, mesh: Mesh=None, value: Socket=None, uv_map: Vector=None, sample_uv: Vector=None, data_type: T_DATA_TYPE_8='FLOAT')` — class method; returns `OUT`.

### Mesh

- `Mesh.sample_uv_surface(self, value: Socket=None, uv_map: Vector=None, sample_uv: Vector=None)` — method; returns `OUT`.

## Scale Elements

Blender identifier: `GeometryNodeScaleElements`

### nd

- `nd.scale_elements(cls, geometry: Geometry=None, selection: Boolean=None, scale: Float=None, center: Vector=None, axis: Vector=None, scale_mode: Menu=None, domain: T_DOMAIN_6='FACE')` — class method; returns `OUT`.

### Face

- `Face.scale(self, scale: Float=None, center: Vector=None, axis: Vector=None, scale_mode: Menu=None)` — method; returns `OUT`.

### Edge

- `Edge.scale(self, scale: Float=None, center: Vector=None, axis: Vector=None, scale_mode: Menu=None)` — method; returns `OUT`.

## Scale Instances

Blender identifier: `GeometryNodeScaleInstances`

### nd

- `nd.scale_instances(cls, instances: Instances=None, selection: Boolean=None, scale: Vector=None, center: Vector=None, local_space: Boolean=None)` — class method; returns `OUT`.

### Instances

- `Instances.scale(self, scale: Vector=None, center: Vector=None, local_space: Boolean=None)` — method; returns `OUT`.

## Scene Time

Blender identifier: `GeometryNodeInputSceneTime`

### nd

- `nd.scene_time(cls)` — class method; returns `OUT`.

## Selection

Blender identifier: `GeometryNodeToolSelection`

### nd

- `nd.selection(cls)` — class method; returns `OUT`.

## Self Object

Blender identifier: `GeometryNodeSelfObject`

### nd

- `nd.self_object(cls)` — property; returns `OUT`.

### Object

- `Object.SelfObject(cls)` — class method; returns `OUT`.

## Separate Bundle

Blender identifier: `NodeSeparateBundle`

### nd

- `nd.separate_bundle(cls, bundle: Bundle=None, define_signature: bool=False)` — class method; returns `OUT`.

### Bundle

- `Bundle.separate(self, define_signature: bool=False)` — method; returns `OUT`.

## Separate Color

Blender identifier: `FunctionNodeSeparateColor`

### nd

- `nd.separate_color(cls, color: Color=None, mode: T_MODE_3='RGB')` — class method; returns `OUT`.

### Color

- `Color.separate(self, mode: T_MODE_3='RGB')` — method; returns `OUT`.

## Separate Components

Blender identifier: `GeometryNodeSeparateComponents`

### nd

- `nd.separate_components(cls, geometry: Geometry=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.separate_components(self)` — method; returns `NODE`.
- `Geometry.separate_mesh(self)` — method; returns `Mesh`.
- `Geometry.separate_curve(self)` — method; returns `Curve`.
- `Geometry.separate_point_cloud(self)` — method; returns `Point Cloud`.
- `Geometry.separate_instances(self)` — method; returns `Instances`.
- `Geometry.separate_volume(self)` — method; returns `Volume`.
- `Geometry.separate_grease_pencil(self)` — method; returns `Grease Pencil`.

## Separate Geometry

Blender identifier: `GeometryNodeSeparateGeometry`

### nd

- `nd.separate_geometry(cls, geometry: Geometry=None, selection: Boolean=None, domain: T_DOMAIN_3='POINT')` — class method; returns `OUT`.

### Point

- `Point.separate(self)` — method; returns `cls`.

### Edge

- `Edge.separate(self)` — method; returns `cls`.

### Face

- `Face.separate(self)` — method; returns `cls`.

### Spline

- `Spline.separate(self)` — method; returns `cls`.

### Instance

- `Instance.separate(self)` — method; returns `cls`.

### Layer

- `Layer.separate(self)` — method; returns `cls`.

## Separate Matrix

Blender identifier: `FunctionNodeSeparateMatrix`

### nd

- `nd.separate_matrix(cls, matrix: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.separate(self)` — method; returns `OUT`.

## Separate Transform

Blender identifier: `FunctionNodeSeparateTransform`

### nd

- `nd.separate_transform(cls, transform: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.separate_transform(self)` — method; returns `OUT`.
- `Matrix.separate_translation(self)` — method; returns `Translation`.
- `Matrix.separate_rotation(self)` — method; returns `Rotation`.
- `Matrix.separate_scale(self)` — method; returns `Scale`.

## Separate XYZ

Blender identifier: `ShaderNodeSeparateXYZ`

### nd

- `nd.separate_xyz(cls, vector: Vector=None)` — class method; returns `OUT`.

### Vector

- `Vector.separate_xyz(self)` — method; returns `OUT`.

## Set Curve Normal

Blender identifier: `GeometryNodeSetCurveNormal`

### nd

- `nd.set_curve_normal(cls, curve: Curve=None, selection: Boolean=None, normal: Vector=None, mode: Menu=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_normal(self, normal: Vector=None, mode: Menu=None)` — method; returns `OUT`.
- `Curve.normal(self, normal: Vector=None)` — setter; returns `None`.

### Spline

- `Spline.normal(self, normal: Vector=None)` — setter; returns `None`.

## Set Curve Radius

Blender identifier: `GeometryNodeSetCurveRadius`

### nd

- `nd.set_curve_radius(cls, curve: Curve=None, selection: Boolean=None, radius: Float=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_radius(self, radius: Float=None)` — method; returns `OUT`.
- `Curve.radius(self, radius: Float=None)` — setter; returns `None`.

### SplinePoint

- `SplinePoint.radius(self, radius: Float=None)` — setter; returns `None`.

## Set Curve Tilt

Blender identifier: `GeometryNodeSetCurveTilt`

### nd

- `nd.set_curve_tilt(cls, curve: Curve=None, selection: Boolean=None, tilt: Float=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_tilt(self, tilt: Float=None)` — method; returns `OUT`.
- `Curve.tilt(self, tilt: Float=None)` — setter; returns `None`.

### Spline

- `Spline.tilt(self, tilt: Float=None)` — setter; returns `None`.

## Set Face Set

Blender identifier: `GeometryNodeToolSetFaceSet`

### nd

- `nd.set_face_set(cls, mesh: Mesh=None, selection: Boolean=None, face_set: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.set_face_set(self, face_set: Integer=None)` — method; returns `OUT`.

## Set Geometry Bundle

Blender identifier: `GeometryNodeSetGeometryBundle`

### nd

- `nd.set_geometry_bundle(cls, geometry: Geometry=None, bundle: Bundle=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_bundle(self, bundle: Bundle=None)` — method; returns `OUT`.
- `Geometry.bundle(self, bundle: Bundle=None)` — setter; returns `None`.

## Set Geometry Name

Blender identifier: `GeometryNodeSetGeometryName`

### nd

- `nd.set_geometry_name(cls, geometry: Geometry=None, name: String=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_name(self, name: String=None)` — method; returns `OUT`.
- `Geometry.name(self, name: String=None)` — setter; returns `None`.

## Set Grease Pencil Color

Blender identifier: `GeometryNodeSetGreasePencilColor`

### nd

- `nd.set_grease_pencil_color(cls, grease_pencil: GreasePencil=None, selection: Boolean=None, color: Color=None, opacity: Float=None, mode_1: Menu=None, mode: T_MODE_16='STROKE')` — class method; returns `OUT`.

### GreasePencil

- `GreasePencil.set_grease_pencil_color(self, color: Color=None, opacity: Float=None, mode_1: Menu=None, mode: T_MODE_16='STROKE')` — method; returns `OUT`.
- `GreasePencil.stroke_color(self, color: Color=None)` — setter; returns `None`.
- `GreasePencil.fill_color(self, color: Color=None)` — setter; returns `None`.

## Set Grease Pencil Depth

Blender identifier: `GeometryNodeSetGreasePencilDepth`

### nd

- `nd.set_grease_pencil_depth(cls, grease_pencil: GreasePencil=None, depth_order_1: Menu=None, depth_order: T_GABOR_TYPE_1='2D')` — class method; returns `OUT`.

### GreasePencil

- `GreasePencil.set_grease_pencil_depth(self, depth_order_1: Menu=None, depth_order: T_GABOR_TYPE_1='2D')` — method; returns `OUT`.
- `GreasePencil.depth(self, depth_order: Menu=None)` — setter; returns `None`.

## Set Grease Pencil Softness

Blender identifier: `GeometryNodeSetGreasePencilSoftness`

### nd

- `nd.set_grease_pencil_softness(cls, grease_pencil: GreasePencil=None, selection: Boolean=None, softness: Float=None)` — class method; returns `OUT`.

### GreasePencil

- `GreasePencil.set_grease_pencil_softness(self, softness: Float=None)` — method; returns `OUT`.
- `GreasePencil.softness(self, softness: Float=None)` — setter; returns `None`.

## Set Grid Background

Blender identifier: `GeometryNodeSetGridBackground`

### nd

- `nd.set_grid_background(cls, grid: Socket=None, background: Socket=None, update_inactive: Boolean=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.set_grid_background(self, background: Float=None, update_inactive: Boolean=None)` — method; returns `OUT`.

### Integer

- `Integer.set_grid_background(self, background: Integer=None, update_inactive: Boolean=None)` — method; returns `OUT`.

### Boolean

- `Boolean.set_grid_background(self, background: Boolean=None, update_inactive: Boolean=None)` — method; returns `OUT`.

### Vector

- `Vector.set_grid_background(self, background: Vector=None, update_inactive: Boolean=None)` — method; returns `OUT`.

## Set Grid Transform

Blender identifier: `GeometryNodeSetGridTransform`

### nd

- `nd.set_grid_transform(cls, grid: Socket=None, transform: Matrix=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.set_grid_transform(self, transform: Matrix=None)` — method; returns `OUT`.

### Integer

- `Integer.set_grid_transform(self, transform: Matrix=None)` — method; returns `OUT`.

### Boolean

- `Boolean.set_grid_transform(self, transform: Matrix=None)` — method; returns `OUT`.

### Vector

- `Vector.set_grid_transform(self, transform: Matrix=None)` — method; returns `OUT`.

## Set Handle Positions

Blender identifier: `GeometryNodeSetCurveHandlePositions`

### nd

- `nd.set_handle_positions(cls, curve: Curve=None, selection: Boolean=None, position: Vector=None, offset: Vector=None, mode: T_MODE_17='LEFT')` — class method; returns `OUT`.

### Curve

- `Curve.set_handle_positions(self, position: Vector=None, offset: Vector=None, mode: T_MODE_17='LEFT')` — method; returns `OUT`.
- `Curve.left_handle_position(self, position: Vector=None)` — setter; returns `None`.
- `Curve.left_handle_offset(self, offset: Vector=None)` — setter; returns `None`.
- `Curve.right_handle_position(self, position: Vector=None)` — setter; returns `None`.
- `Curve.right_handle_offset(self, offset: Vector=None)` — setter; returns `None`.

## Set Handle Type

Blender identifier: `GeometryNodeCurveSetHandles`

### nd

- `nd.set_handle_type(cls, curve: Curve=None, selection: Boolean=None, handle_type: T_HANDLE_TYPE_1='AUTO', mode: set[Literal['LEFT', 'RIGHT']]={'LEFT', 'RIGHT'})` — class method; returns `OUT`.

### Curve

- `Curve.set_handle_type(self, handle_type: T_HANDLE_TYPE_1='AUTO', mode: set[Literal['LEFT', 'RIGHT']]={'LEFT', 'RIGHT'})` — method; returns `OUT`.
- `Curve.handle_type(self, handle_type: T_HANDLE_TYPE_1='AUTO')` — setter; returns `None`.
- `Curve.left_handle_type(self, handle_type: T_HANDLE_TYPE_1='AUTO')` — setter; returns `None`.
- `Curve.right_handle_type(self, handle_type: T_HANDLE_TYPE_1='AUTO')` — setter; returns `None`.

## Set ID

Blender identifier: `GeometryNodeSetID`

### nd

- `nd.set_id(cls, geometry: Geometry=None, selection: Boolean=None, id: Integer=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_id(self, id: Integer=None)` — method; returns `OUT`.
- `Geometry.id(self, id: Integer=None)` — setter; returns `None`.

## Set Instance Transform

Blender identifier: `GeometryNodeSetInstanceTransform`

### nd

- `nd.set_instance_transform(cls, instances: Instances=None, selection: Boolean=None, transform: Matrix=None)` — class method; returns `OUT`.

### Instances

- `Instances.set_instance_transform(self, transform: Matrix=None)` — method; returns `OUT`.

### Instance

- `Instance.transform(self, transform: Matrix=None)` — setter; returns `None`.

## Set Material

Blender identifier: `GeometryNodeSetMaterial`

### nd

- `nd.set_material(cls, geometry: Geometry=None, selection: Boolean=None, material: Material=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_material(self, material: Material=None)` — method; returns `OUT`.
- `Geometry.material(self, material: Material=None)` — setter; returns `None`.

### Face

- `Face.material(self, material: Material=None)` — setter; returns `None`.

### Edge

- `Edge.material(self, material: Material=None)` — setter; returns `None`.

## Set Material Index

Blender identifier: `GeometryNodeSetMaterialIndex`

### nd

- `nd.set_material_index(cls, geometry: Geometry=None, selection: Boolean=None, material_index: Integer=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_material_index(self, material_index: Integer=None)` — method; returns `OUT`.

### Face

- `Face.material_index(self, material_index: Integer=None)` — setter; returns `None`.

### Mesh

- `Mesh.material_index(self, material_index: Integer=None)` — setter; returns `None`.

### Spline

- `Spline.material_index(self, material_index: Integer=None)` — setter; returns `None`.

## Set Mesh Normal

Blender identifier: `GeometryNodeSetMeshNormal`

### nd

- `nd.set_mesh_normal(cls, mesh: Mesh=None, remove_custom: Boolean=None, custom_normal: Vector=None, edge_sharpness: Boolean=None, face_sharpness: Boolean=None, mode: T_MODE_18='SHARPNESS', domain: T_DOMAIN_7='POINT')` — class method; returns `OUT`.

### Point

- `Point.set_normal(self, remove_custom: Boolean=None, custom_normal: Vector=None, edge_sharpness: Boolean=None, face_sharpness: Boolean=None, mode: T_MODE_18='SHARPNESS')` — method; returns `OUT`.
- `Point.normal(self, custom_normal: Vector=None)` — setter; returns `None`.

### Face

- `Face.set_normal(self, remove_custom: Boolean=None, custom_normal: Vector=None, edge_sharpness: Boolean=None, face_sharpness: Boolean=None, mode: T_MODE_18='SHARPNESS')` — method; returns `OUT`.
- `Face.normal(self, custom_normal: Vector=None)` — setter; returns `None`.

### Corner

- `Corner.set_normal(self, remove_custom: Boolean=None, custom_normal: Vector=None, edge_sharpness: Boolean=None, face_sharpness: Boolean=None, mode: T_MODE_18='SHARPNESS')` — method; returns `OUT`.
- `Corner.normal(self, custom_normal: Vector=None)` — setter; returns `None`.

### Mesh

- `Mesh.normal(self, custom_normal: Vector=None)` — setter; returns `None`.

## Set NURBS Order

Blender identifier: `GeometryNodeSetNURBSOrder`

### nd

- `nd.set_nurbs_order(cls, curves: Curve=None, selection: Boolean=None, order: Integer=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_nurbs_order(self, order: Integer=None)` — method; returns `OUT`.

## Set NURBS Weight

Blender identifier: `GeometryNodeSetNURBSWeight`

### nd

- `nd.set_nurbs_weight(cls, curves: Curve=None, selection: Boolean=None, weight: Float=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_nurbs_weight(self, weight: Float=None)` — method; returns `OUT`.

## Set Point Cloud Type

Blender identifier: `GeometryNodePointsSetType`

### nd

- `nd.set_point_cloud_type(cls, points: Cloud=None, type: Menu=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.set_point_type(self, type: Menu=None)` — method; returns `OUT`.

## Set Point Radius

Blender identifier: `GeometryNodeSetPointRadius`

### nd

- `nd.set_point_radius(cls, points: Cloud=None, selection: Boolean=None, radius: Float=None)` — class method; returns `OUT`.

### Cloud

- `Cloud.set_point_radius(self, radius: Float=None)` — method; returns `OUT`.
- `Cloud.radius(self, radius: Float=None)` — setter; returns `None`.

### CloudPoint

- `CloudPoint.radius(self, radius: Float=None)` — setter; returns `None`.

## Set Position

Blender identifier: `GeometryNodeSetPosition`

### nd

- `nd.set_position(cls, geometry: Geometry=None, selection: Boolean=None, position: Vector=None, offset: Vector=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.set_position(self, position: Vector=None, offset: Vector=None)` — method; returns `OUT`.
- `Geometry.position(self, position: Vector=None)` — setter; returns `None`.
- `Geometry.offset(self, offset: Vector=None)` — setter; returns `None`.

### Point

- `Point.position(self, position: Vector=None)` — setter; returns `None`.
- `Point.offset(self, offset: Vector=None)` — setter; returns `None`.

## Set Selection

Blender identifier: `GeometryNodeToolSetSelection`

### nd

- `nd.set_selection(cls, geometry: Geometry=None, selection: Socket=None, domain: T_DOMAIN_8='POINT', selection_type: T_SELECTION_TYPE_1='BOOLEAN')` — class method; returns `OUT`.

### Point

- `Point.set_selection(self, selection_type: T_SELECTION_TYPE_1='BOOLEAN')` — method; returns `OUT`.

### Edge

- `Edge.set_selection(self, selection_type: T_SELECTION_TYPE_1='BOOLEAN')` — method; returns `OUT`.

### Face

- `Face.set_selection(self, selection_type: T_SELECTION_TYPE_1='BOOLEAN')` — method; returns `OUT`.

### Spline

- `Spline.set_selection(self, selection_type: T_SELECTION_TYPE_1='BOOLEAN')` — method; returns `OUT`.

## Set Shade Smooth

Blender identifier: `GeometryNodeSetShadeSmooth`

### nd

- `nd.set_shade_smooth(cls, mesh: Mesh=None, selection: Boolean=None, shade_smooth: Boolean=None, domain: T_DOMAIN_6='FACE')` — class method; returns `OUT`.

### Edge

- `Edge.set_shade_smooth(self, shade_smooth: Boolean=None)` — method; returns `OUT`.
- `Edge.shade_smooth(self, shade_smooth: Boolean=None)` — setter; returns `None`.
- `Edge.smooth(self, shade_smooth: Boolean=None)` — setter; returns `None`.

### Face

- `Face.set_shade_smooth(self, shade_smooth: Boolean=None)` — method; returns `OUT`.
- `Face.shade_smooth(self, shade_smooth: Boolean=None)` — setter; returns `None`.
- `Face.smooth(self, shade_smooth: Boolean=None)` — setter; returns `None`.

## Set Spline Cyclic

Blender identifier: `GeometryNodeSetSplineCyclic`

### nd

- `nd.set_spline_cyclic(cls, curve: Curve=None, selection: Boolean=None, cyclic: Boolean=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_spline_cyclic(self, cyclic: Boolean=None)` — method; returns `OUT`.
- `Curve.is_cyclic(self, cyclic: Boolean=None)` — setter; returns `None`.

### Spline

- `Spline.is_cyclic(self, cyclic: Boolean=None)` — setter; returns `None`.

## Set Spline Resolution

Blender identifier: `GeometryNodeSetSplineResolution`

### nd

- `nd.set_spline_resolution(cls, curve: Curve=None, selection: Boolean=None, resolution: Integer=None)` — class method; returns `OUT`.

### Curve

- `Curve.set_spline_resolution(self, resolution: Integer=None)` — method; returns `OUT`.
- `Curve.resolution(self, resolution: Integer=None)` — setter; returns `None`.

### Spline

- `Spline.resolution(self, resolution: Integer=None)` — setter; returns `None`.

## Set Spline Type

Blender identifier: `GeometryNodeCurveSplineType`

### nd

- `nd.set_spline_type(cls, curve: Curve=None, selection: Boolean=None, spline_type: T_SPLINE_TYPE_1='POLY')` — class method; returns `OUT`.

### Curve

- `Curve.set_spline_type(self, spline_type: T_SPLINE_TYPE_1='POLY')` — method; returns `OUT`.
- `Curve.type(self, spline_type: T_SPLINE_TYPE_1='POLY')` — setter; returns `None`.

### Spline

- `Spline.type(self, spline_type: T_SPLINE_TYPE_1='POLY')` — setter; returns `None`.

## Set String Case

Blender identifier: `FunctionNodeSetStringCase`

### nd

- `nd.set_string_case(cls, string: String=None, case: Menu=None)` — class method; returns `OUT`.

### String

- `String.set_string_case(self, case: Menu=None)` — method; returns `OUT`.

## Shortest Edge Paths

Blender identifier: `GeometryNodeInputShortestEdgePaths`

### nd

- `nd.shortest_edge_paths(cls, end_vertex: Boolean=None, edge_cost: Float=None)` — class method; returns `OUT`.

## Slice String

Blender identifier: `FunctionNodeSliceString`

### nd

- `nd.slice_string(cls, string: String=None, position: Integer=None, length: Integer=None)` — class method; returns `OUT`.

### String

- `String.slice(self, position: Integer=None, length: Integer=None)` — method; returns `OUT`.

## Sort Elements

Blender identifier: `GeometryNodeSortElements`

### nd

- `nd.sort_elements(cls, geometry: Geometry=None, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None, domain: T_DOMAIN_9='POINT')` — class method; returns `OUT`.

### Point

- `Point.sort(self, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Edge

- `Edge.sort(self, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Face

- `Face.sort(self, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Spline

- `Spline.sort(self, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Instance

- `Instance.sort(self, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

## Sort List

Blender identifier: `GeometryNodeSortList`

### nd

- `nd.sort_list(cls, list: Socket=None, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None, socket_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Integer

- `Integer.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Boolean

- `Boolean.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Vector

- `Vector.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Color

- `Color.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Rotation

- `Rotation.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Matrix

- `Matrix.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### String

- `String.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Menu

- `Menu.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Object

- `Object.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Image

- `Image.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Geometry

- `Geometry.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Collection

- `Collection.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Material

- `Material.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Bundle

- `Bundle.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Closure

- `Closure.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Font

- `Font.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

### Sound

- `Sound.sort_list(self, selection: Boolean=None, group_id: Integer=None, sort_weight: Float=None)` — method; returns `OUT`.

## Special Characters

Blender identifier: `FunctionNodeInputSpecialCharacters`

### nd

- `nd.special_characters(cls)` — class method; returns `OUT`.

### String

- `String.line_break(cls)` — property; returns `Line Break`.
- `String.tab(cls)` — property; returns `Tab`.

## Spiral

Blender identifier: `GeometryNodeCurveSpiral`

### nd

- `nd.spiral(cls, resolution: Integer=None, rotations: Float=None, start_radius: Float=None, end_radius: Float=None, height: Float=None, reverse: Boolean=None)` — class method; returns `OUT`.

### Curve

- `Curve.Spiral(cls, resolution: Integer=None, rotations: Float=None, start_radius: Float=None, end_radius: Float=None, height: Float=None, reverse: Boolean=None)` — class method; returns `OUT`.

## Spline Length

Blender identifier: `GeometryNodeSplineLength`

### nd

- `nd.spline_length(cls)` — class method; returns `OUT`.

## Spline Parameter

Blender identifier: `GeometryNodeSplineParameter`

### nd

- `nd.spline_parameter(cls)` — class method; returns `OUT`.

## Spline Resolution

Blender identifier: `GeometryNodeInputSplineResolution`

### nd

- `nd.spline_resolution(cls)` — property; returns `OUT`.

### Spline

- `Spline.resolution(self)` — property; returns `OUT`.

### Curve

- `Curve.resolution(self)` — property; returns `OUT`.

## Split Edges

Blender identifier: `GeometryNodeSplitEdges`

### nd

- `nd.split_edges(cls, mesh: Mesh=None, selection: Boolean=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.split_edges(self)` — method; returns `OUT`.

## Split String

Blender identifier: `FunctionNodeSplitString`

### nd

- `nd.split_string(cls, string: String=None, separator: String=None)` — class method; returns `OUT`.

### String

- `String.split(self, separator: String=None)` — method; returns `OUT`.

## Split to Instances

Blender identifier: `GeometryNodeSplitToInstances`

### nd

- `nd.split_to_instances(cls, geometry: Geometry=None, selection: Boolean=None, group_id: Integer=None, domain: T_DOMAIN_3='POINT')` — class method; returns `OUT`.

### Point

- `Point.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

### Edge

- `Edge.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

### Face

- `Face.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

### Spline

- `Spline.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

### Instance

- `Instance.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

### Layer

- `Layer.split_to_instances(self, group_id: Integer=None)` — method; returns `OUT`.

## Star

Blender identifier: `GeometryNodeCurveStar`

### nd

- `nd.star(cls, points: Integer=None, inner_radius: Float=None, outer_radius: Float=None, twist: Float=None)` — class method; returns `OUT`.

### Curve

- `Curve.Star(cls, points: Integer=None, inner_radius: Float=None, outer_radius: Float=None, twist: Float=None)` — class method; returns `OUT`.

## Store Bundle Item

Blender identifier: `NodeStoreBundleItem`

### nd

- `nd.store_item(cls, bundle: Bundle=None, path: String=None, item: Socket=None, socket_type: T_DATA_TYPE_6='FLOAT', shape: T_STRUCTURE_TYPE_1='AUTO')` — class method; returns `OUT`.

### Bundle

- `Bundle.store_item(self, path: String=None, item: Socket=None, shape: T_STRUCTURE_TYPE_1='AUTO')` — method; returns `OUT`.

## Store Named Attribute

Blender identifier: `GeometryNodeStoreNamedAttribute`

### nd

- `nd.store_named_attribute(cls, geometry: Geometry=None, selection: Boolean=None, name: String=None, value: Socket=None, data_type: T_DATA_TYPE_13='FLOAT', domain: T_DOMAIN_1='POINT')` — class method; returns `OUT`.

### Point

- `Point.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

### Edge

- `Edge.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

### Face

- `Face.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

### Corner

- `Corner.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.
- `Corner.store_uv(self, name: String=None, value: Vector=None)` — method; returns `OUT`.

### Spline

- `Spline.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

### Instance

- `Instance.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

### Layer

- `Layer.store_named_attribute(self, name: String=None, value: Socket=None)` — method; returns `OUT`.

## Store Named Grid

Blender identifier: `GeometryNodeStoreNamedGrid`

### nd

- `nd.store_named_grid(cls, volume: Volume=None, name: String=None, grid: Socket=None, data_type: T_DATA_TYPE_14='FLOAT')` — class method; returns `OUT`.

### Volume

- `Volume.store_named_grid(self, name: String=None, grid: Socket=None)` — method; returns `OUT`.

## String

Blender identifier: `FunctionNodeInputString`

### nd

- `nd.string(cls, string: str='')` — class method; returns `OUT`.

## String Length

Blender identifier: `FunctionNodeStringLength`

### nd

- `nd.string_length(cls, string: String=None)` — class method; returns `OUT`.

### String

- `String.length(self)` — method; returns `OUT`.

## String to Curves

Blender identifier: `GeometryNodeStringToCurves`

### nd

- `nd.string_to_curves(cls, string: String=None, size: Float=None, font: Font=None, character_spacing: Float=None, word_spacing: Float=None, line_spacing: Float=None, text_box_width: Float=None, text_box_height: Float=None, align_x: Menu=None, align_y: Menu=None, pivot_point: Menu=None, overflow: Menu=None)` — class method; returns `OUT`.

### String

- `String.to_curves(self, size: Float=None, font: Font=None, character_spacing: Float=None, word_spacing: Float=None, line_spacing: Float=None, text_box_width: Float=None, text_box_height: Float=None, align_x: Menu=None, align_y: Menu=None, pivot_point: Menu=None, overflow: Menu=None)` — method; returns `OUT`.

## String to Value

Blender identifier: `FunctionNodeStringToValue`

### nd

- `nd.string_to_value(cls, string: String=None, base: Integer=None, data_type: T_DATA_TYPE_15='FLOAT')` — class method; returns `OUT`.

### String

- `String.to_value(self, base: Integer=None, data_type: T_DATA_TYPE_15='FLOAT')` — method; returns `OUT`.
- `String.to_float(self)` — method; returns `OUT`.
- `String.to_integer(self, base: Integer=None)` — method; returns `OUT`.

### Float

- `Float.FromString(cls, string: String=None, base: Integer=None, data_type: T_DATA_TYPE_15='FLOAT')` — class method; returns `OUT`.

## Subdivide Curve

Blender identifier: `GeometryNodeSubdivideCurve`

### nd

- `nd.subdivide_curve(cls, curve: Curve=None, cuts: Integer=None)` — class method; returns `OUT`.

### Curve

- `Curve.subdivide(self, cuts: Integer=None)` — method; returns `OUT`.

## Subdivide Mesh

Blender identifier: `GeometryNodeSubdivideMesh`

### nd

- `nd.subdivide_mesh(cls, mesh: Mesh=None, level: Integer=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.subdivide(self, level: Integer=None)` — method; returns `OUT`.

## Subdivision Surface

Blender identifier: `GeometryNodeSubdivisionSurface`

### nd

- `nd.subdivision_surface(cls, mesh: Mesh=None, level: Integer=None, edge_crease: Float=None, vertex_crease: Float=None, limit_surface: Boolean=None, quality: Integer=None, uv_smooth: Menu=None, boundary_smooth: Menu=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.subdivision_surface(self, level: Integer=None, edge_crease: Float=None, vertex_crease: Float=None, limit_surface: Boolean=None, quality: Integer=None, uv_smooth: Menu=None, boundary_smooth: Menu=None)` — method; returns `OUT`.

## Switch

Blender identifier: `GeometryNodeSwitch`

### nd

- `nd.switch(cls, switch: Boolean=None, false: Socket=None, true: Socket=None, input_type: T_DATA_TYPE_6='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.switch(self, switch: Boolean=None, true: Float=None)` — method; returns `OUT`.
- `Float.switch_false(self, switch: Boolean=None, false: Float=None)` — method; returns `OUT`.
- `Float.Switch(cls, switch: Boolean=None, false: Float=None, true: Float=None)` — class method; returns `cls`.

### Integer

- `Integer.switch(self, switch: Boolean=None, true: Integer=None)` — method; returns `OUT`.
- `Integer.switch_false(self, switch: Boolean=None, false: Integer=None)` — method; returns `OUT`.
- `Integer.Switch(cls, switch: Boolean=None, false: Integer=None, true: Integer=None)` — class method; returns `cls`.

### Boolean

- `Boolean.switch(self, switch: Boolean=None, true: Boolean=None)` — method; returns `OUT`.
- `Boolean.switch_false(self, switch: Boolean=None, false: Boolean=None)` — method; returns `OUT`.
- `Boolean.Switch(cls, switch: Boolean=None, false: Boolean=None, true: Boolean=None)` — class method; returns `cls`.

### Vector

- `Vector.switch(self, switch: Boolean=None, true: Vector=None)` — method; returns `OUT`.
- `Vector.switch_false(self, switch: Boolean=None, false: Vector=None)` — method; returns `OUT`.
- `Vector.Switch(cls, switch: Boolean=None, false: Vector=None, true: Vector=None)` — class method; returns `cls`.

### Color

- `Color.switch(self, switch: Boolean=None, true: Color=None)` — method; returns `OUT`.
- `Color.switch_false(self, switch: Boolean=None, false: Color=None)` — method; returns `OUT`.
- `Color.Switch(cls, switch: Boolean=None, false: Color=None, true: Color=None)` — class method; returns `cls`.

### Rotation

- `Rotation.switch(self, switch: Boolean=None, true: Rotation=None)` — method; returns `OUT`.
- `Rotation.switch_false(self, switch: Boolean=None, false: Rotation=None)` — method; returns `OUT`.
- `Rotation.Switch(cls, switch: Boolean=None, false: Rotation=None, true: Rotation=None)` — class method; returns `cls`.

### Matrix

- `Matrix.switch(self, switch: Boolean=None, true: Matrix=None)` — method; returns `OUT`.
- `Matrix.switch_false(self, switch: Boolean=None, false: Matrix=None)` — method; returns `OUT`.
- `Matrix.Switch(cls, switch: Boolean=None, false: Matrix=None, true: Matrix=None)` — class method; returns `cls`.

### String

- `String.switch(self, switch: Boolean=None, true: String=None)` — method; returns `OUT`.
- `String.switch_false(self, switch: Boolean=None, false: String=None)` — method; returns `OUT`.
- `String.Switch(cls, switch: Boolean=None, false: String=None, true: String=None)` — class method; returns `cls`.

### Menu

- `Menu.switch(self, switch: Boolean=None, true: Menu=None)` — method; returns `OUT`.
- `Menu.switch_false(self, switch: Boolean=None, false: Menu=None)` — method; returns `OUT`.
- `Menu.Switch(cls, switch: Boolean=None, false: Menu=None, true: Menu=None)` — class method; returns `cls`.

### Object

- `Object.switch(self, switch: Boolean=None, true: Object=None)` — method; returns `OUT`.
- `Object.switch_false(self, switch: Boolean=None, false: Object=None)` — method; returns `OUT`.
- `Object.Switch(cls, switch: Boolean=None, false: Object=None, true: Object=None)` — class method; returns `cls`.

### Image

- `Image.switch(self, switch: Boolean=None, true: Image=None)` — method; returns `OUT`.
- `Image.switch_false(self, switch: Boolean=None, false: Image=None)` — method; returns `OUT`.
- `Image.Switch(cls, switch: Boolean=None, false: Image=None, true: Image=None)` — class method; returns `cls`.

### Geometry

- `Geometry.switch(self, switch: Boolean=None, true: Geometry=None)` — method; returns `OUT`.
- `Geometry.switch_false(self, switch: Boolean=None, false: Geometry=None)` — method; returns `OUT`.
- `Geometry.Switch(cls, switch: Boolean=None, false: Geometry=None, true: Geometry=None)` — class method; returns `cls`.

### Collection

- `Collection.switch(self, switch: Boolean=None, true: Collection=None)` — method; returns `OUT`.
- `Collection.switch_false(self, switch: Boolean=None, false: Collection=None)` — method; returns `OUT`.
- `Collection.Switch(cls, switch: Boolean=None, false: Collection=None, true: Collection=None)` — class method; returns `cls`.

### Material

- `Material.switch(self, switch: Boolean=None, true: Material=None)` — method; returns `OUT`.
- `Material.switch_false(self, switch: Boolean=None, false: Material=None)` — method; returns `OUT`.
- `Material.Switch(cls, switch: Boolean=None, false: Material=None, true: Material=None)` — class method; returns `cls`.

### Bundle

- `Bundle.switch(self, switch: Boolean=None, true: Bundle=None)` — method; returns `OUT`.
- `Bundle.switch_false(self, switch: Boolean=None, false: Bundle=None)` — method; returns `OUT`.
- `Bundle.Switch(cls, switch: Boolean=None, false: Bundle=None, true: Bundle=None)` — class method; returns `cls`.

### Closure

- `Closure.switch(self, switch: Boolean=None, true: Closure=None)` — method; returns `OUT`.
- `Closure.switch_false(self, switch: Boolean=None, false: Closure=None)` — method; returns `OUT`.
- `Closure.Switch(cls, switch: Boolean=None, false: Closure=None, true: Closure=None)` — class method; returns `cls`.

### Font

- `Font.switch(self, switch: Boolean=None, true: Font=None)` — method; returns `OUT`.
- `Font.switch_false(self, switch: Boolean=None, false: Font=None)` — method; returns `OUT`.
- `Font.Switch(cls, switch: Boolean=None, false: Font=None, true: Font=None)` — class method; returns `cls`.

### Sound

- `Sound.switch(self, switch: Boolean=None, true: Sound=None)` — method; returns `OUT`.
- `Sound.switch_false(self, switch: Boolean=None, false: Sound=None)` — method; returns `OUT`.
- `Sound.Switch(cls, switch: Boolean=None, false: Sound=None, true: Sound=None)` — class method; returns `cls`.

## Tag Filter

Blender identifier: `GeometryNodeTagFilter`

### nd

- `nd.tag_filter(cls, tag_filter: String=None, tags: String=None)` — class method; returns `OUT`.

### String

- `String.tag_filter(self, tags: String=None)` — method; returns `OUT`.

## Transfer Attributes

Blender identifier: `GeometryNodeTransferAttributes`

### nd

- `nd.transfer_attributes(cls, target: Geometry=None, target_point_id: Integer=None, target_edge_id: Integer=None, target_face_id: Integer=None, target_corner_id: Integer=None, target_curve_id: Integer=None, target_instance_id: Integer=None, source: Geometry=None, source_point_id: Integer=None, source_edge_id: Integer=None, source_face_id: Integer=None, source_corner_id: Integer=None, source_curve_id: Integer=None, source_instance_id: Integer=None, attribute_names: String=None, exclude_names: Boolean=None, pattern_mode: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.transfer_attributes(self, target_point_id: Integer=None, target_edge_id: Integer=None, target_face_id: Integer=None, target_corner_id: Integer=None, target_curve_id: Integer=None, target_instance_id: Integer=None, source: Geometry=None, source_point_id: Integer=None, source_edge_id: Integer=None, source_face_id: Integer=None, source_corner_id: Integer=None, source_curve_id: Integer=None, source_instance_id: Integer=None, attribute_names: String=None, exclude_names: Boolean=None, pattern_mode: Menu=None)` — method; returns `OUT`.

## Transform Direction

Blender identifier: `FunctionNodeTransformDirection`

### nd

- `nd.transform_direction(cls, direction: Vector=None, transform: Matrix=None)` — class method; returns `OUT`.

### Vector

- `Vector.transform_direction(self, transform: Matrix=None)` — method; returns `OUT`.

## Transform Geometry

Blender identifier: `GeometryNodeTransform`

### nd

- `nd.transform_geometry(cls, geometry: Geometry=None, translation: Vector=None, rotation: Rotation=None, scale: Vector=None, transform: Matrix=None, mode: Menu=None)` — class method; returns `OUT`.

### Geometry

- `Geometry.transform(self, translation: Vector=None, rotation: Rotation=None, scale: Vector=None, transform: Matrix=None, mode: Menu=None)` — method; returns `OUT`.

## Transform Gizmo

Blender identifier: `GeometryNodeGizmoTransform`

### nd

- `nd.transform_gizmo(cls, *value: Matrix, position: Vector=None, rotation: Rotation=None, use_translation_x: bool=True, use_translation_y: bool=True, use_translation_z: bool=True, use_rotation_x: bool=True, use_rotation_y: bool=True, use_rotation_z: bool=True, use_scale_x: bool=True, use_scale_y: bool=True, use_scale_z: bool=True)` — class method; returns `OUT`.

### Matrix

- `Matrix.transform_gizmo(self, *value: Matrix, position: Vector=None, rotation: Rotation=None, use_translation_x: bool=True, use_translation_y: bool=True, use_translation_z: bool=True, use_rotation_x: bool=True, use_rotation_y: bool=True, use_rotation_z: bool=True, use_scale_x: bool=True, use_scale_y: bool=True, use_scale_z: bool=True)` — method; returns `OUT`.

## Transform Point

Blender identifier: `FunctionNodeTransformPoint`

### nd

- `nd.transform_point(cls, vector: Vector=None, transform: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.transform_point(self, vector: Vector=None)` — method; returns `OUT`.

## Translate Instances

Blender identifier: `GeometryNodeTranslateInstances`

### nd

- `nd.translate_instances(cls, instances: Instances=None, selection: Boolean=None, translation: Vector=None, local_space: Boolean=None)` — class method; returns `OUT`.

### Instances

- `Instances.translate(self, translation: Vector=None, local_space: Boolean=None)` — method; returns `OUT`.

## Transpose Matrix

Blender identifier: `FunctionNodeTransposeMatrix`

### nd

- `nd.transpose_matrix(cls, matrix: Matrix=None)` — class method; returns `OUT`.

### Matrix

- `Matrix.transpose(self)` — method; returns `OUT`.

## Triangulate

Blender identifier: `GeometryNodeTriangulate`

### nd

- `nd.triangulate(cls, mesh: Mesh=None, selection: Boolean=None, quad_method: Menu=None, n_gon_method: Menu=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.triangulate(self, quad_method: Menu=None, n_gon_method: Menu=None)` — method; returns `OUT`.

## Trim Curve

Blender identifier: `GeometryNodeTrimCurve`

### nd

- `nd.trim_curve(cls, curve: Curve=None, selection: Boolean=None, start: Socket=None, end: Socket=None, mode: T_MODE_15='FACTOR')` — class method; returns `OUT`.

### Curve

- `Curve.trim(self, start: Socket=None, end: Socket=None, mode: T_MODE_15='FACTOR')` — method; returns `OUT`.
- `Curve.trim_factor(self, start: Float=None, end: Float=None)` — method; returns `OUT`.
- `Curve.trim_length(self, start: Float=None, end: Float=None)` — method; returns `OUT`.

## Trim String

Blender identifier: `FunctionNodeTrimString`

### nd

- `nd.trim_string(cls, string: String=None, characters: String=None, whitespace: Boolean=None, start: Boolean=None, end: Boolean=None)` — class method; returns `OUT`.

### String

- `String.trim(self, characters: String=None, whitespace: Boolean=None, start: Boolean=None, end: Boolean=None)` — method; returns `OUT`.

## UV Sphere

Blender identifier: `GeometryNodeMeshUVSphere`

### nd

- `nd.uv_sphere(cls, segments: Integer=None, rings: Integer=None, radius: Float=None)` — class method; returns `OUT`.

### Mesh

- `Mesh.UVSphere(cls, segments: Integer=None, rings: Integer=None, radius: Float=None)` — class method; returns `OUT`.

## UV Tangent

Blender identifier: `GeometryNodeUVTangent`

### nd

- `nd.uv_tangent(cls, uv: Vector=None, method: Menu=None)` — class method; returns `OUT`.

## UV Unwrap

Blender identifier: `GeometryNodeUVUnwrap`

### nd

- `nd.uv_unwrap(cls, selection: Boolean=None, seam: Boolean=None, margin: Float=None, fill_holes: Boolean=None, iterations: Integer=None, no_flip: Boolean=None, method: Menu=None)` — class method; returns `OUT`.

### Boolean

- `Boolean.uv_unwrap(self, seam: Boolean=None, margin: Float=None, fill_holes: Boolean=None, iterations: Integer=None, no_flip: Boolean=None, method: Menu=None)` — method; returns `OUT`.

## Value

Blender identifier: `ShaderNodeValue`

### nd

- `nd.value(cls)` — property; returns `OUT`.

## Value to String

Blender identifier: `FunctionNodeValueToString`

### nd

- `nd.value_to_string(cls, value: Socket=None, decimals: Integer=None, base: Integer=None, padding: Integer=None, data_type: T_DATA_TYPE_15='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.to_string(self, decimals: Integer=None)` — method; returns `OUT`.

### Integer

- `Integer.to_string(self, base: Integer=None, padding: Integer=None)` — method; returns `OUT`.

### String

- `String.FromValue(cls, value: Integer=None, base: Integer=None, padding: Integer=None)` — class method; returns `OUT`.

## Vector

Blender identifier: `FunctionNodeInputVector`

### nd

- `nd.vector(cls, vector: tuple[float, float, float]=(0.0, 0.0, 0.0), vector_dimensions: int=3)` — class method; returns `OUT`.

## Vector Curves

Blender identifier: `ShaderNodeVectorCurve`

### nd

- `nd.vector_curves(cls, vector: Vector=None, factor: Float=None)` — class method; returns `OUT`.

### Float

- `Float.vector_curves(self, vector: Vector=None)` — method; returns `OUT`.

## Vector Math

Blender identifier: `ShaderNodeVectorMath`

### nd

- `nd.vector_math(cls, vector: Vector=None, vector_1: Vector=None, addend: Vector=None, ior: Float=None, *, base: Vector=None, multiplier: Vector=None, incident: Vector=None, exponent: Vector=None, max: Vector=None, increment: Vector=None, reference: Vector=None, min: Vector=None, scale: Float=None, operation: T_OPERATION_7='ADD')` — class method; returns `OUT`.

### gnmath

- `gnmath.vadd(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vsubtract(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vmultiply(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vdivide(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vpower(base: Vector=None, exponent: Vector=None)` — method; returns `OUT`.
- `gnmath.vmodulo(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vabs(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vround(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vfloor(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vceil(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.scale(vector: Vector=None, scale: Float=None)` — method; returns `OUT`.
- `gnmath.vmultiply_add(vector: Vector=None, multiplier: Vector=None, addend: Vector=None)` — method; returns `OUT`.
- `gnmath.cross(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.project(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.reflect(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.refract(vector: Vector=None, vector_1: Vector=None, ior: Float=None)` — method; returns `OUT`.
- `gnmath.faceforward(vector: Vector=None, incident: Vector=None, reference: Vector=None)` — method; returns `OUT`.
- `gnmath.dot(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.distance(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.length(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.normalize(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vsign(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vmin(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vmax(vector: Vector=None, vector_1: Vector=None)` — method; returns `OUT`.
- `gnmath.vfraction(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vwrap(vector: Vector=None, max: Vector=None, min: Vector=None)` — method; returns `OUT`.
- `gnmath.vsnap(vector: Vector=None, increment: Vector=None)` — method; returns `OUT`.
- `gnmath.vsin(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vcos(vector: Vector=None)` — method; returns `OUT`.
- `gnmath.vtan(vector: Vector=None)` — method; returns `OUT`.

### Vector

- `Vector.add(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__add__(self, other)` — method; returns `OUT`.
- `Vector.__radd__(self, other)` — method; returns `OUT`.
- `Vector.__iadd__(self, other)` — method; returns `OUT`.
- `Vector.subtract(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__sub__(self, other)` — method; returns `OUT`.
- `Vector.__rsub__(self, other)` — method; returns `OUT`.
- `Vector.__isub__(self, other)` — method; returns `OUT`.
- `Vector.multiply(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__mul__(self, other)` — method; returns `OUT`.
- `Vector.__rmul__(self, other)` — method; returns `OUT`.
- `Vector.__imul__(self, other)` — method; returns `OUT`.
- `Vector.divide(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__truediv__(self, other)` — method; returns `OUT`.
- `Vector.__rtruediv__(self, other)` — method; returns `OUT`.
- `Vector.__itruediv__(self, other)` — method; returns `OUT`.
- `Vector.power(self, exponent: Vector=None)` — method; returns `OUT`.
- `Vector.__pow__(self, other)` — method; returns `OUT`.
- `Vector.__rpow__(self, other)` — method; returns `OUT`.
- `Vector.__ipow__(self, other)` — method; returns `OUT`.
- `Vector.modulo(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.__mod__(self, other)` — method; returns `OUT`.
- `Vector.__rmod__(self, other)` — method; returns `OUT`.
- `Vector.__imod__(self, other)` — method; returns `OUT`.
- `Vector.abs(self)` — method; returns `OUT`.
- `Vector.__abs__(self)` — method; returns `OUT`.
- `Vector.round(self)` — method; returns `OUT`.
- `Vector.__round__(self)` — method; returns `OUT`.
- `Vector.floor(self)` — method; returns `OUT`.
- `Vector.__floor__(self)` — method; returns `OUT`.
- `Vector.ceil(self)` — method; returns `OUT`.
- `Vector.__ceil__(self)` — method; returns `OUT`.
- `Vector.scale(self, scale: Float=None)` — method; returns `OUT`.
- `Vector.__neg__(self)` — method; returns `OUT`.
- `Vector.multiply_add(self, multiplier: Vector=None, addend: Vector=None)` — method; returns `OUT`.
- `Vector.cross(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.project(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.reflect(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.refract(self, vector: Vector=None, ior: Float=None)` — method; returns `OUT`.
- `Vector.faceforward(self, incident: Vector=None, reference: Vector=None)` — method; returns `OUT`.
- `Vector.dot(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.distance(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.length(self)` — method; returns `OUT`.
- `Vector.normalize(self)` — method; returns `OUT`.
- `Vector.sign(self)` — method; returns `OUT`.
- `Vector.min(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.max(self, vector: Vector=None)` — method; returns `OUT`.
- `Vector.fraction(self)` — method; returns `OUT`.
- `Vector.wrap(self, max: Vector=None, min: Vector=None)` — method; returns `OUT`.
- `Vector.snap(self, increment: Vector=None)` — method; returns `OUT`.
- `Vector.sin(self)` — method; returns `OUT`.
- `Vector.cos(self)` — method; returns `OUT`.
- `Vector.tan(self)` — method; returns `OUT`.
- `Vector.vector_math(self, vector: Vector=None, addend: Vector=None, ior: Float=None, *, multiplier: Vector=None, incident: Vector=None, exponent: Vector=None, max: Vector=None, increment: Vector=None, reference: Vector=None, min: Vector=None, scale: Float=None, operation: T_OPERATION_7='ADD')` — method; returns `OUT`.

## Vector Rotate

Blender identifier: `ShaderNodeVectorRotate`

### nd

- `nd.vector_rotate(cls, vector: Vector=None, center: Vector=None, axis: Vector=None, angle: Float=None, rotation: Vector=None, invert: bool=False, rotation_type: T_ROTATION_TYPE_1='AXIS_ANGLE')` — class method; returns `OUT`.

### Vector

- `Vector.vector_rotate(self, center: Vector=None, axis: Vector=None, angle: Float=None, rotation: Vector=None, invert: bool=False, rotation_type: T_ROTATION_TYPE_1='AXIS_ANGLE')` — method; returns `OUT`.

## Vertex Neighbors

Blender identifier: `GeometryNodeInputMeshVertexNeighbors`

### nd

- `nd.vertex_neighbors(cls)` — class method; returns `OUT`.

## Vertex of Corner

Blender identifier: `GeometryNodeVertexOfCorner`

### nd

- `nd.vertex_of_corner(cls, corner_index: Integer=None)` — class method; returns `OUT`.

## Viewer

Blender identifier: `GeometryNodeViewer`

### nd

- `nd.viewer(cls, named_sockets: dict={}, domain: T_DOMAIN_10='AUTO', **sockets)` — class method; returns `NODE`.

## Viewport Transform

Blender identifier: `GeometryNodeViewportTransform`

### nd

- `nd.viewport_transform(cls)` — class method; returns `OUT`.

## Volume Cube

Blender identifier: `GeometryNodeVolumeCube`

### nd

- `nd.volume_cube(cls, density: Float=None, background: Float=None, min: Vector=None, max: Vector=None, resolution_x: Integer=None, resolution_y: Integer=None, resolution_z: Integer=None)` — class method; returns `OUT`.

### Volume

- `Volume.Cube(cls, density: Float=None, background: Float=None, min: Vector=None, max: Vector=None, resolution_x: Integer=None, resolution_y: Integer=None, resolution_z: Integer=None)` — class method; returns `OUT`.

## Volume to Mesh

Blender identifier: `GeometryNodeVolumeToMesh`

### nd

- `nd.volume_to_mesh(cls, volume: Volume=None, voxel_size: Float=None, voxel_amount: Float=None, threshold: Float=None, adaptivity: Float=None, resolution_mode: Menu=None)` — class method; returns `OUT`.

### Volume

- `Volume.to_mesh(self, voxel_size: Float=None, voxel_amount: Float=None, threshold: Float=None, adaptivity: Float=None, resolution_mode: Menu=None)` — method; returns `OUT`.

## Voronoi Texture

Blender identifier: `ShaderNodeTexVoronoi`

### nd

- `nd.voronoi_texture(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, smoothness: Float=None, exponent: Float=None, randomness: Float=None, normalize: bool=False, voronoi_dimensions: T_NOISE_DIMENSIONS_1='3D', distance: T_DISTANCE_1='EUCLIDEAN', feature: T_FEATURE_1='F1')` — class method; returns `OUT`.

### Texture

- `Texture.Voronoi(cls, vector: Vector=None, w: Float=None, scale: Float=None, detail: Float=None, roughness: Float=None, lacunarity: Float=None, smoothness: Float=None, exponent: Float=None, randomness: Float=None, normalize: bool=False, voronoi_dimensions: T_NOISE_DIMENSIONS_1='3D', distance: T_DISTANCE_1='EUCLIDEAN', feature: T_FEATURE_1='F1')` — class method; returns `OUT`.

## Voxel Index

Blender identifier: `GeometryNodeInputVoxelIndex`

### nd

- `nd.voxel_index(cls)` — class method; returns `OUT`.

## Voxelize Grid

Blender identifier: `GeometryNodeGridVoxelize`

### nd

- `nd.voxelize_grid(cls, grid: Socket=None, data_type: T_DATA_TYPE_5='FLOAT')` — class method; returns `OUT`.

### Float

- `Float.voxelize_grid(self)` — method; returns `OUT`.

### Integer

- `Integer.voxelize_grid(self)` — method; returns `OUT`.

### Boolean

- `Boolean.voxelize_grid(self)` — method; returns `OUT`.

### Vector

- `Vector.voxelize_grid(self)` — method; returns `OUT`.

## Warning

Blender identifier: `GeometryNodeWarning`

### nd

- `nd.warning(cls, show: Boolean=None, message: String=None, warning_type: T_WARNING_TYPE_1='ERROR')` — class method; returns `OUT`.

### Boolean

- `Boolean.error(self, message: String=None)` — method; returns `OUT`.
- `Boolean.warning(self, message: String=None)` — method; returns `OUT`.
- `Boolean.info(self, message: String=None)` — method; returns `OUT`.

## Wave Texture

Blender identifier: `ShaderNodeTexWave`

### nd

- `nd.wave_texture(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, detail: Float=None, detail_scale: Float=None, detail_roughness: Float=None, phase_offset: Float=None, wave_type: T_WAVE_TYPE_1='BANDS', bands_direction: T_BANDS_DIRECTION_1='X', rings_direction: T_RINGS_DIRECTION_1='X', wave_profile: T_WAVE_PROFILE_1='SIN')` — class method; returns `OUT`.

### Texture

- `Texture.Wave(cls, vector: Vector=None, scale: Float=None, distortion: Float=None, detail: Float=None, detail_scale: Float=None, detail_roughness: Float=None, phase_offset: Float=None, wave_type: T_WAVE_TYPE_1='BANDS', bands_direction: T_BANDS_DIRECTION_1='X', rings_direction: T_RINGS_DIRECTION_1='X', wave_profile: T_WAVE_PROFILE_1='SIN')` — class method; returns `OUT`.

## White Noise Texture

Blender identifier: `ShaderNodeTexWhiteNoise`

### nd

- `nd.white_noise_texture(cls, vector: Vector=None, w: Float=None, noise_dimensions: T_NOISE_DIMENSIONS_1='3D')` — class method; returns `OUT`.

### Texture

- `Texture.WhiteNoise(cls, vector: Vector=None, w: Float=None, noise_dimensions: T_NOISE_DIMENSIONS_1='3D')` — class method; returns `OUT`.

## XPBD Solver

Blender identifier: `GeometryNodeXPBDSolver`

### nd

- `nd.xpbd_solver(cls, world: Bundle=None, delta_time: Float=None, filter: String=None, simulation_to_world: Matrix=None, substeps: Integer=None, constraint_iterations: Integer=None, solver_path: String=None, begin: Float=None, end: Float=None)` — class method; returns `OUT`.

### Bundle

- `Bundle.xpbd_solver(self, delta_time: Float=None, filter: String=None, simulation_to_world: Matrix=None, substeps: Integer=None, constraint_iterations: Integer=None, solver_path: String=None, begin: Float=None, end: Float=None)` — method; returns `OUT`.

