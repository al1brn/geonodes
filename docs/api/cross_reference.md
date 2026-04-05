# Cross Reference

## 3D Cursor

> `bl_idname` : GeometryNodeTool3DCursor

### nd

nd._3d_cursor.(cls)

## AOV Output

> `bl_idname` : ShaderNodeOutputAOV

### snd

nd.aov_output.(cls, color: Color = None, value: Float = None, aov_name = '')

### class Color

```python
Color.aov_output(self, value: Float = None, aov_name = '')
```

## Accumulate Field

> `bl_idname` : GeometryNodeAccumulateField

### nd

nd.accumulate_field.(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Edge

```python
Edge.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Face

```python
Face.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Corner

```python
Corner.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Spline

```python
Spline.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Instance

```python
Instance.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Layer

```python
Layer.accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

## Active Camera

> `bl_idname` : GeometryNodeInputActiveCamera

### nd

nd.active_camera.(self)

### class Object

```python
Object.ActiveCamera(cls)
```

## Active Element

> `bl_idname` : GeometryNodeToolActiveElement

### nd

nd.active_element.(cls, domain: Literal['POINT', 'EDGE', 'FACE', 'LAYER'] = 'POINT')

### class Point

```python
Point.active_element(cls)
```

### class Edge

```python
Edge.active_element(cls)
```

### class Face

```python
Face.active_element(cls)
```

### class Layer

```python
Layer.active_element(cls)
```

## Add Shader

> `bl_idname` : ShaderNodeAddShader

### snd

nd.add_shader.(cls, shader: Shader = None, shader_1: Shader = None)

### class Shader

```python
Shader.add(self, shader: Shader = None)
```

## Advect Grid

> `bl_idname` : GeometryNodeGridAdvect

### nd

nd.advect_grid.(cls,
                    grid: Float = None,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

### class Integer

```python
Integer.advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

### class Vector

```python
Vector.advect_grid(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

## Align Rotation to Vector

> `bl_idname` : FunctionNodeAlignRotationToVector

### nd

nd.align_rotation_to_vector.(cls,
                    rotation: Rotation = None,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')

### class Rotation

```python
Rotation.AlignToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.AlignXToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.AlignYToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.AlignZToVector(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.align_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.align_x_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.align_y_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
Rotation.align_z_to_vector(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

## Ambient Occlusion

> `bl_idname` : ShaderNodeAmbientOcclusion

### snd

nd.ambient_occlusion.(cls,
                    color: Color = None,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16)

### class Color

```python
Color.ambient_occlusion(self,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16)
```

## Arc

> `bl_idname` : GeometryNodeCurveArc

### nd

nd.arc.(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    offset_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')

### class Curve

```python
Curve.ArcPoints(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None,
                    offset_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None)
```

```python
Curve.ArcRadius(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None)
```

```python
Curve.Arc(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')
```

## Attribute

> `bl_idname` : ShaderNodeAttribute

### snd

nd.attribute.(cls,
                    attribute_name = '',
                    attribute_type: Literal['GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'] = 'GEOMETRY')

## Attribute Statistic

> `bl_idname` : GeometryNodeAttributeStatistic

### nd

nd.attribute_statistic.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    attribute: Float = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Edge

```python
Edge.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Face

```python
Face.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Corner

```python
Corner.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Spline

```python
Spline.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Instance

```python
Instance.attribute_statistic(self, attribute: Float | Vector = None)
```

### class Layer

```python
Layer.attribute_statistic(self, attribute: Float | Vector = None)
```

## Axes to Rotation

> `bl_idname` : FunctionNodeAxesToRotation

### nd

nd.axes_to_rotation.(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X')

### class Rotation

```python
Rotation.FromAxes(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X')
```

```python
Rotation.FromXYAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
Rotation.FromYXAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
Rotation.FromXZAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
Rotation.FromZXAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
Rotation.FromYZAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
Rotation.FromZYAxes(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

## Axis Angle to Rotation

> `bl_idname` : FunctionNodeAxisAngleToRotation

### nd

nd.axis_angle_to_rotation.(cls, axis: Vector = None, angle: Float = None)

### class Rotation

```python
Rotation.FromAxisAngle(cls, axis: Vector = None, angle: Float = None)
```

## Background

> `bl_idname` : ShaderNodeBackground

### snd

nd.background.(cls, color: Color = None, strength: Float = None, weight: Float = None)

### class Color

```python
Color.background(self, strength: Float = None)
```

## Bake

> `bl_idname` : GeometryNodeBake

### nd

nd.bake.(cls, named_sockets: dict = {}, **sockets)

## Bevel

> `bl_idname` : ShaderNodeBevel

### snd

nd.bevel.(cls, radius: Float = None, normal: Vector = None, samples = 4)

### class Float

```python
Float.bevel(self, normal: Vector = None, samples = 4)
```

## Bit Math

> `bl_idname` : FunctionNodeBitMath

### nd

nd.bit_math.(cls,
                    a: Integer = None,
                    b: Integer = None,
                    shift: Integer = None,
                    operation: Literal['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE'] = 'AND')

### class Integer

```python
Integer.bw_and(self, b: Integer = None)
```

```python
Integer.bw_or(self, b: Integer = None)
```

```python
Integer.bw_xor(self, b: Integer = None)
```

```python
Integer.bw_not(self)
```

```python
Integer.bw_shift(self, shift: Integer = None)
```

```python
Integer.bw_rotate(self, shift: Integer = None)
```

### class gnmath

```python
gnmath.bw_and(a: Integer = None, b: Integer = None)
```

```python
gnmath.bw_or(a: Integer = None, b: Integer = None)
```

```python
gnmath.bw_xor(a: Integer = None, b: Integer = None)
```

```python
gnmath.bw_not(a: Integer = None)
```

```python
gnmath.bw_shift(a: Integer = None, shift: Integer = None)
```

```python
gnmath.bw_rotate(a: Integer = None, shift: Integer = None)
```

## Blackbody

> `bl_idname` : ShaderNodeBlackbody

### nd

nd.blackbody.(cls, temperature: Float = None)

### snd

nd.blackbody.(cls, temperature: Float = None)

### class Color

```python
Color.Blackbody(cls, temperature: Float = None)
```

## Blur Attribute

> `bl_idname` : GeometryNodeBlurAttribute

### nd

nd.blur_attribute.(cls,
                    value: Float = None,
                    iterations: Integer = None,
                    weight: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR'] = 'FLOAT')

### class Float

```python
Float.blur(self, iterations: Integer = None, weight: Float = None)
```

### class Integer

```python
Integer.blur(self, iterations: Integer = None, weight: Float = None)
```

### class Vector

```python
Vector.blur(self, iterations: Integer = None, weight: Float = None)
```

### class Color

```python
Color.blur(self, iterations: Integer = None, weight: Float = None)
```

## Bone Info

> `bl_idname` : GeometryNodeBoneInfo

### nd

nd.bone_info.(cls,
                    armature: Object = None,
                    bone_name: String = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')

### class Object

```python
Object.bone_info(self,
                    bone_name: String = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')
```

## Boolean

> `bl_idname` : FunctionNodeInputBool

### nd

nd.boolean.(cls, boolean = False)

## Boolean Math

> `bl_idname` : FunctionNodeBooleanMath

### nd

nd.boolean_math.(cls,
                    boolean: Boolean = None,
                    boolean_1: Boolean = None,
                    operation: Literal['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY'] = 'AND')

### class Boolean

```python
Boolean.band(self, boolean: Boolean = None)
```

```python
Boolean.bor(self, boolean: Boolean = None)
```

```python
Boolean.bnot(self)
```

```python
Boolean.not_and(self, boolean: Boolean = None)
```

```python
Boolean.nor(self, boolean: Boolean = None)
```

```python
Boolean.xnor(self, boolean: Boolean = None)
```

```python
Boolean.xor(self, boolean: Boolean = None)
```

```python
Boolean.imply(self, boolean: Boolean = None)
```

```python
Boolean.nimply(self, boolean: Boolean = None)
```

### class gnmath

```python
gnmath.band(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.bor(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.bnot(boolean: Boolean = None)
```

```python
gnmath.not_and(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.nor(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.xnor(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.xor(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.imply(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
gnmath.nimply(boolean: Boolean = None, boolean_1: Boolean = None)
```

## Bounding Box

> `bl_idname` : GeometryNodeBoundBox

### nd

nd.bounding_box.(cls, geometry: Geometry = None, use_radius: Boolean = None)

### class Geometry

```python
Geometry.bounding_box(self, use_radius: Boolean = None)
```

## Brick Texture

> `bl_idname` : ShaderNodeTexBrick

### nd

nd.brick_texture.(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2)

### snd

nd.brick_texture.(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2)

### class Color

```python
Color.Brick(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2)
```

### class Texture

```python
Texture.Brick(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    mortar: Color = None,
                    scale: Float = None,
                    mortar_size: Float = None,
                    mortar_smooth: Float = None,
                    bias: Float = None,
                    brick_width: Float = None,
                    row_height: Float = None,
                    offset = 0.5,
                    offset_frequency = 2,
                    squash = 1.0,
                    squash_frequency = 2)
```

## Brightness/Contrast

> `bl_idname` : ShaderNodeBrightContrast

### snd

nd.brightness_contrast.(cls, color: Color = None, brightness: Float = None, contrast: Float = None)

### class Color

```python
Color.brightness_contrast(self, brightness: Float = None, contrast: Float = None)
```

## Bump

> `bl_idname` : ShaderNodeBump

### snd

nd.bump.(cls,
                    strength: Float = None,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False)

### class Float

```python
Float.bump(self,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False)
```

## Bézier Segment

> `bl_idname` : GeometryNodeCurvePrimitiveBezierSegment

### nd

nd.bezier_segment.(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None,
                    mode: Literal['POSITION', 'OFFSET'] = 'POSITION')

### class Curve

```python
Curve.BeziersegmentPosition(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None)
```

```python
Curve.BeziersegmentOffset(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None)
```

```python
Curve.BezierSegment(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None,
                    mode: Literal['POSITION', 'OFFSET'] = 'POSITION')
```

## Camera Data

> `bl_idname` : ShaderNodeCameraData

### snd

nd.camera_data.(cls)

## Camera Info

> `bl_idname` : GeometryNodeCameraInfo

### nd

nd.camera_info.(cls, camera: Object = None)

### class Object

```python
Object.camera_info(self)
```

## Capture Attribute

> `bl_idname` : GeometryNodeCaptureAttribute

### class Domain

```python
Domain.capture_attribute(attribute=None, **attributes)
```

```python
Domain.capture(attribute=None, **attributes)
```

## Checker Texture

> `bl_idname` : ShaderNodeTexChecker

### nd

nd.checker_texture.(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)

### snd

nd.checker_texture.(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)

### class Color

```python
Color.Checker(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)
```

### class Texture

```python
Texture.Checker(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)
```

## Clamp

> `bl_idname` : ShaderNodeClamp

### nd

nd.clamp.(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')

### snd

nd.clamp.(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')

### class Float

```python
Float.clamp(self,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')
```

```python
Float.clamp_minmax(self, min: Float = None, max: Float = None)
```

```python
Float.clamp_range(self, min: Float = None, max: Float = None)
```

## Clip Grid

> `bl_idname` : GeometryNodeGridClip

### nd

nd.clip_grid.(cls,
                    grid: Float = None,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Integer

```python
Integer.clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Boolean

```python
Boolean.clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Vector

```python
Vector.clip_grid(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

## Closure Input

> `bl_idname` : NodeClosureInput

### nd

nd.closure_input.(self)

### snd

nd.closure_input.(self)

## Closure Output

> `bl_idname` : NodeClosureOutput

### nd

nd.closure_output.(cls, active_input_index = 0, active_output_index = 0, define_signature = False)

### snd

nd.closure_output.(cls, active_input_index = 0, active_output_index = 0, define_signature = False)

## Collection

> `bl_idname` : GeometryNodeInputCollection

### nd

nd.collection.(cls, collection = None)

## Collection Info

> `bl_idname` : GeometryNodeCollectionInfo

### nd

nd.collection_info.(cls,
                    collection: Collection = None,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')

### class Collection

```python
Collection.info(self,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')
```

## Color

> `bl_idname` : ShaderNodeRGB

### snd

nd.color.(self)

## Color Attribute

> `bl_idname` : ShaderNodeVertexColor

### snd

nd.color_attribute.(cls, layer_name = '')

### class Color

```python
Color.ColorAttribute(cls, layer_name = '')
```

## Color Ramp

> `bl_idname` : ShaderNodeValToRGB

### nd

nd.color_ramp.(fac=None, stops=None, interpolation='LINEAR')

### snd

nd.color_ramp.(fac=None, stops=None, interpolation='LINEAR')

## Combine Bundle

> `bl_idname` : NodeCombineBundle

### nd

nd.combine_bundle.(cls, named_sockets: dict = {}, define_signature = False, **sockets)

### snd

nd.combine_bundle.(cls, named_sockets: dict = {}, define_signature = False, **sockets)

### class Bundle

```python
Bundle.Combine(cls, named_sockets: dict = {}, define_signature = False, **sockets)
```

## Combine Color

> `bl_idname` : ShaderNodeCombineColor

### snd

nd.combine_color.(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')

### class Float

```python
Float.combine_color_RGB(self, green: Float = None, blue: Float = None)
```

```python
Float.combine_color_HSV(self, saturation: Float = None, value: Float = None)
```

```python
Float.combine_color_HSL(self, saturation: Float = None, lightness: Float = None)
```

```python
Float.combine_color(self,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')
```

## Combine Matrix

> `bl_idname` : FunctionNodeCombineMatrix

### nd

nd.combine_matrix.(cls,
                    column_1_row_1: Float = None,
                    column_1_row_2: Float = None,
                    column_1_row_3: Float = None,
                    column_1_row_4: Float = None,
                    column_2_row_1: Float = None,
                    column_2_row_2: Float = None,
                    column_2_row_3: Float = None,
                    column_2_row_4: Float = None,
                    column_3_row_1: Float = None,
                    column_3_row_2: Float = None,
                    column_3_row_3: Float = None,
                    column_3_row_4: Float = None,
                    column_4_row_1: Float = None,
                    column_4_row_2: Float = None,
                    column_4_row_3: Float = None,
                    column_4_row_4: Float = None)

### class Matrix

```python
Matrix.Combine(cls,
                    column_1_row_1: Float = None,
                    column_1_row_2: Float = None,
                    column_1_row_3: Float = None,
                    column_1_row_4: Float = None,
                    column_2_row_1: Float = None,
                    column_2_row_2: Float = None,
                    column_2_row_3: Float = None,
                    column_2_row_4: Float = None,
                    column_3_row_1: Float = None,
                    column_3_row_2: Float = None,
                    column_3_row_3: Float = None,
                    column_3_row_4: Float = None,
                    column_4_row_1: Float = None,
                    column_4_row_2: Float = None,
                    column_4_row_3: Float = None,
                    column_4_row_4: Float = None)
```

## Combine Transform

> `bl_idname` : FunctionNodeCombineTransform

### nd

nd.combine_transform.(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None)

### class Matrix

```python
Matrix.CombineTransform(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

## Combine XYZ

> `bl_idname` : ShaderNodeCombineXYZ

### nd

nd.combine_xyz.(cls, x: Float = None, y: Float = None, z: Float = None)

### snd

nd.combine_xyz.(cls, x: Float = None, y: Float = None, z: Float = None)

### class Vector

```python
Vector.CombineXYZ(cls, x: Float = None, y: Float = None, z: Float = None)
```

## Compare

> `bl_idname` : FunctionNodeCompare

### nd

nd.compare.(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Integer = None,
                    b_1: Integer = None,
                    a_2: Vector = None,
                    b_2: Vector = None,
                    a_3: Color = None,
                    b_3: Color = None,
                    a_4: String = None,
                    b_4: String = None,
                    c: Float = None,
                    angle: Float = None,
                    epsilon: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'STRING'] = 'FLOAT',
                    mode: Literal['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'] = 'ELEMENT',
                    operation: Literal['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL'] = 'GREATER_THAN')

### class Float

```python
Float.less_than(self, b: Float = None)
```

```python
Float.less_equal(self, b: Float = None)
```

```python
Float.greater_than(self, b: Float = None)
```

```python
Float.greater_equal(self, b: Float = None)
```

```python
Float.equal(self, b: Float = None, epsilon: Float = None)
```

```python
Float.not_equal(self, b: Float = None, epsilon: Float = None)
```

### class Integer

```python
Integer.less_than(self, b: Integer = None)
```

```python
Integer.less_equal(self, b: Integer = None)
```

```python
Integer.greater_than(self, b: Integer = None)
```

```python
Integer.greater_equal(self, b: Integer = None)
```

```python
Integer.equal(self, b: Integer = None)
```

```python
Integer.not_equal(self, b: Integer = None)
```

### class Vector

```python
Vector.less_than(self, b: Vector = None)
```

```python
Vector.less_equal(self, b: Vector = None)
```

```python
Vector.greater_than(self, b: Vector = None)
```

```python
Vector.greater_equal(self, b: Vector = None)
```

```python
Vector.equal(self, b: Vector = None, epsilon: Float = None)
```

```python
Vector.not_equal(self, b: Vector = None, epsilon: Float = None)
```

### class String

```python
String.equal(self, b: String = None)
```

```python
String.not_equal(self, b: String = None)
```

### class Color

```python
Color.equal(self, b: Color = None, epsilon: Float = None)
```

```python
Color.not_equal(self, b: Color = None, epsilon: Float = None)
```

```python
Color.brighter(self, b: Color = None)
```

```python
Color.darker(self, b: Color = None)
```

## Cone

> `bl_idname` : GeometryNodeMeshCone

### nd

nd.cone.(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius_top: Float = None,
                    radius_bottom: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')

### class Mesh

```python
Mesh.Cone(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius_top: Float = None,
                    radius_bottom: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')
```

## Convex Hull

> `bl_idname` : GeometryNodeConvexHull

### nd

nd.convex_hull.(cls, geometry: Geometry = None)

### class Geometry

```python
Geometry.convex_hull(self)
```

## Corners of Edge

> `bl_idname` : GeometryNodeCornersOfEdge

### nd

nd.corners_of_edge.(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
Mesh.corners_of_edge(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Edge

```python
Edge.corners(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Edge.corner_index(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Edge.corners_total(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Corners of Face

> `bl_idname` : GeometryNodeCornersOfFace

### nd

nd.corners_of_face.(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
Mesh.corners_of_face(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Face

```python
Face.corners(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Face.corner_index(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Face.corners_total(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Corners of Vertex

> `bl_idname` : GeometryNodeCornersOfVertex

### nd

nd.corners_of_vertex.(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
Mesh.corners_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Vertex

```python
Vertex.corners(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Vertex.corner_index(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Vertex.corners_total(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Cube

> `bl_idname` : GeometryNodeMeshCube

### nd

nd.cube.(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None)

### class Mesh

```python
Mesh.Cube(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None)
```

## Cube Grid Topology

> `bl_idname` : GeometryNodeCubeGridTopology

### nd

nd.cube_grid_topology.(cls,
                    bounds_min: Vector = None,
                    bounds_max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None)

### class Boolean

```python
Boolean.CubeGridTopology(cls,
                    bounds_min: Vector = None,
                    bounds_max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None)
```

## Curve Circle

> `bl_idname` : GeometryNodeCurvePrimitiveCircle

### nd

nd.curve_circle.(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')

### class Curve

```python
Curve.CirclePoints(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None)
```

```python
Curve.CircleRadius(cls, resolution: Integer = None, radius: Float = None)
```

```python
Curve.Circle(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')
```

## Curve Handle Positions

> `bl_idname` : GeometryNodeInputCurveHandlePositions

### nd

nd.curve_handle_positions.(cls, relative: Boolean = None)

### class Curve

```python
Curve.handle_positions(cls, relative: Boolean = None)
```

```python
prop = Curve.left_handle_position
```

```python
prop = Curve.right_handle_position
```

```python
prop = Curve.left_handle_offset
```

```python
prop = Curve.right_handle_offset
```

## Curve Length

> `bl_idname` : GeometryNodeCurveLength

### nd

nd.curve_length.(cls, curve: Curve = None)

### class Curve

```python
Curve.length(self)
```

## Curve Line

> `bl_idname` : GeometryNodeCurvePrimitiveLine

### nd

nd.curve_line.(cls,
                    start: Vector = None,
                    end: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS')

### class Curve

```python
Curve.LinePoints(cls, start: Vector = None, end: Vector = None)
```

```python
Curve.LineDirection(cls, start: Vector = None, direction: Vector = None, length: Float = None)
```

```python
Curve.Line(cls,
                    start: Vector = None,
                    end: Vector = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS')
```

## Curve Tangent

> `bl_idname` : GeometryNodeInputTangent

### nd

nd.curve_tangent.(self)

### class Curve

```python
prop = Curve.tangent
```

## Curve Tilt

> `bl_idname` : GeometryNodeInputCurveTilt

### nd

nd.curve_tilt.(self)

### class Curve

```python
prop = Curve.tilt
```

### class Spline

```python
prop = Spline.tilt
```

## Curve of Point

> `bl_idname` : GeometryNodeCurveOfPoint

### nd

nd.curve_of_point.(cls, point_index: Integer = None)

### class Curve

```python
Curve.curve_of_point(cls, point_index: Integer = None)
```

### class SplinePoint

```python
SplinePoint.curve_of_point(cls, point_index: Integer = None)
```

```python
SplinePoint.curve_index(cls, point_index: Integer = None)
```

```python
SplinePoint.index_in_curve(cls, point_index: Integer = None)
```

## Curve to Mesh

> `bl_idname` : GeometryNodeCurveToMesh

### nd

nd.curve_to_mesh.(cls,
                    curve: Curve = None,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None)

### class Curve

```python
Curve.to_mesh(self,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None)
```

## Curve to Points

> `bl_idname` : GeometryNodeCurveToPoints

### nd

nd.curve_to_points.(cls,
                    curve: Curve = None,
                    count: Integer = None,
                    length: Float = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')

### class Curve

```python
Curve.to_points_evaluated(self)
```

```python
Curve.to_points_count(self, count: Integer = None)
```

```python
Curve.to_points_length(self, length: Float = None)
```

```python
Curve.to_points(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')
```

### class SplinePoint

```python
SplinePoint.to_points_evaluated(self)
```

```python
SplinePoint.to_points_count(self, count: Integer = None)
```

```python
SplinePoint.to_points_length(self, length: Float = None)
```

```python
SplinePoint.to_points(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')
```

## Curves Info

> `bl_idname` : ShaderNodeHairInfo

### snd

nd.curves_info.(cls)

## Curves to Grease Pencil

> `bl_idname` : GeometryNodeCurvesToGreasePencil

### nd

nd.curves_to_grease_pencil.(cls,
                    curves: Curve = None,
                    selection: Boolean = None,
                    instances_as_layers: Boolean = None)

### class Curve

```python
Curve.to_grease_pencil(self, instances_as_layers: Boolean = None)
```

## Cylinder

> `bl_idname` : GeometryNodeMeshCylinder

### nd

nd.cylinder.(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')

### class Mesh

```python
Mesh.Cylinder(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')
```

## Deform Curves on Surface

> `bl_idname` : GeometryNodeDeformCurvesOnSurface

### nd

nd.deform_curves_on_surface.(cls, curves: Curve = None)

### class Curve

```python
Curve.deform_on_surface(self)
```

## Delete Geometry

> `bl_idname` : GeometryNodeDeleteGeometry

### nd

nd.delete_geometry.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT',
                    mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')

### class Point

```python
Point.delete_geometry_all(self)
```

```python
Point.delete_geometry_edge_face(self)
```

```python
Point.delete_geometry_only_face(self)
```

```python
Point.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Point.delete_all(self)
```

```python
Point.delete_edge_face(self)
```

```python
Point.delete_only_face(self)
```

```python
Point.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Edge

```python
Edge.delete_geometry_all(self)
```

```python
Edge.delete_geometry_edge_face(self)
```

```python
Edge.delete_geometry_only_face(self)
```

```python
Edge.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Edge.delete_all(self)
```

```python
Edge.delete_edge_face(self)
```

```python
Edge.delete_only_face(self)
```

```python
Edge.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Face

```python
Face.delete_geometry_all(self)
```

```python
Face.delete_geometry_edge_face(self)
```

```python
Face.delete_geometry_only_face(self)
```

```python
Face.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Face.delete_all(self)
```

```python
Face.delete_edge_face(self)
```

```python
Face.delete_only_face(self)
```

```python
Face.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Spline

```python
Spline.delete_geometry_all(self)
```

```python
Spline.delete_geometry_edge_face(self)
```

```python
Spline.delete_geometry_only_face(self)
```

```python
Spline.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Spline.delete_all(self)
```

```python
Spline.delete_edge_face(self)
```

```python
Spline.delete_only_face(self)
```

```python
Spline.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Instance

```python
Instance.delete_geometry_all(self)
```

```python
Instance.delete_geometry_edge_face(self)
```

```python
Instance.delete_geometry_only_face(self)
```

```python
Instance.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Instance.delete_all(self)
```

```python
Instance.delete_edge_face(self)
```

```python
Instance.delete_only_face(self)
```

```python
Instance.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Layer

```python
Layer.delete_geometry_all(self)
```

```python
Layer.delete_geometry_edge_face(self)
```

```python
Layer.delete_geometry_only_face(self)
```

```python
Layer.delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
Layer.delete_all(self)
```

```python
Layer.delete_edge_face(self)
```

```python
Layer.delete_only_face(self)
```

```python
Layer.delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

## Dial Gizmo

> `bl_idname` : GeometryNodeGizmoDial

### nd

nd.dial_gizmo.(cls,
                    *value: Float,
                    position: Vector = None,
                    up: Vector = None,
                    screen_space: Boolean = None,
                    radius: Float = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY')

### class Float

```python
Float.dial_gizmo(self,
                    *value: Float,
                    position: Vector = None,
                    up: Vector = None,
                    screen_space: Boolean = None,
                    radius: Float = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY')
```

## Diffuse BSDF

> `bl_idname` : ShaderNodeBsdfDiffuse

### snd

nd.diffuse_bsdf.(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None)

### class Shader

```python
Shader.Diffuse(cls, color: Color = None, roughness: Float = None, normal: Vector = None)
```

## Displacement

> `bl_idname` : ShaderNodeDisplacement

### snd

nd.displacement.(cls,
                    height: Float = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT')

### class Float

```python
Float.displacement(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT')
```

## Distribute Points in Grid

> `bl_idname` : GeometryNodeDistributePointsInGrid

### nd

nd.distribute_points_in_grid.(cls,
                    grid: Float = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM')

### class Float

```python
Float.distribute_points_in_grid_density_random(self, density: Float = None, seed: Integer = None)
```

```python
Float.distribute_points_in_grid_density_grid(self, spacing: Vector = None, threshold: Float = None)
```

```python
Float.distribute_points_in_grid(self,
                    density: Float = None,
                    seed: Integer = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM')
```

## Distribute Points in Volume

> `bl_idname` : GeometryNodeDistributePointsInVolume

### nd

nd.distribute_points_in_volume.(cls,
                    volume: Volume = None,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None)

### class Volume

```python
Volume.distribute_points(self,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None)
```

## Distribute Points on Faces

> `bl_idname` : GeometryNodeDistributePointsOnFaces

### nd

nd.distribute_points_on_faces.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM')

### class Mesh

```python
Mesh.distribute_points_on_faces(self,
                    density: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM')
```

```python
Mesh.distribute_points_on_faces_random(self, density: Float = None, seed: Integer = None)
```

```python
Mesh.distribute_points_on_faces_poisson(self,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None)
```

### class Face

```python
Face.distribute_points(self,
                    density: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM')
```

```python
Face.distribute_points_random(self, density: Float = None, seed: Integer = None)
```

```python
Face.distribute_points_poisson(self,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None)
```

## Domain Size

> `bl_idname` : GeometryNodeAttributeDomainSize

### nd

nd.domain_size.(cls,
                    geometry: Geometry = None,
                    component: Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL'] = 'MESH')

### class Mesh

```python
Mesh.domain_size(self)
```

### class Curve

```python
Curve.domain_size(self)
```

### class Cloud

```python
Cloud.domain_size(self)
```

### class Instances

```python
Instances.domain_size(self)
```

### class GreasePencil

```python
GreasePencil.domain_size(self)
```

## Dual Mesh

> `bl_idname` : GeometryNodeDualMesh

### nd

nd.dual_mesh.(cls, mesh: Mesh = None, keep_boundaries: Boolean = None)

### class Mesh

```python
Mesh.dual(self, keep_boundaries: Boolean = None)
```

## Duplicate Elements

> `bl_idname` : GeometryNodeDuplicateElements

### nd

nd.duplicate_elements.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    amount: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE'] = 'POINT')

### class Point

```python
Point.duplicate(self, amount: Integer = None)
```

### class Edge

```python
Edge.duplicate(self, amount: Integer = None)
```

### class Face

```python
Face.duplicate(self, amount: Integer = None)
```

### class Spline

```python
Spline.duplicate(self, amount: Integer = None)
```

### class Layer

```python
Layer.duplicate(self, amount: Integer = None)
```

### class Instance

```python
Instance.duplicate(self, amount: Integer = None)
```

## Edge Angle

> `bl_idname` : GeometryNodeInputMeshEdgeAngle

### nd

nd.edge_angle.(cls)

### class Mesh

```python
prop = Mesh.edge_angle
```

```python
prop = Mesh.unsigned_edge_angle
```

```python
prop = Mesh.signed_edge_angle
```

### class Edge

```python
prop = Edge.edge_angle
```

```python
prop = Edge.unsigned_angle
```

```python
prop = Edge.signed_angle
```

## Edge Neighbors

> `bl_idname` : GeometryNodeInputMeshEdgeNeighbors

### nd

nd.edge_neighbors.(self)

### class Mesh

```python
prop = Mesh.edge_neighbors
```

### class Edge

```python
prop = Edge.face_count
```

## Edge Paths to Curves

> `bl_idname` : GeometryNodeEdgePathsToCurves

### nd

nd.edge_paths_to_curves.(cls,
                    mesh: Mesh = None,
                    start_vertices: Boolean = None,
                    next_vertex_index: Integer = None)

### class Mesh

```python
Mesh.edge_paths_to_curves(self, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

### class Edge

```python
Edge.paths_to_curves(self, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

## Edge Paths to Selection

> `bl_idname` : GeometryNodeEdgePathsToSelection

### nd

nd.edge_paths_to_selection.(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)

### class Mesh

```python
Mesh.edge_paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

### class Edge

```python
Edge.paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

## Edge Vertices

> `bl_idname` : GeometryNodeInputMeshEdgeVertices

### nd

nd.edge_vertices.(cls)

### class Mesh

```python
prop = Mesh.edge_vertices
```

### class Edge

```python
prop = Edge.edge_vertices
```

```python
prop = Edge.vertex_index_1
```

```python
prop = Edge.vertex_index_2
```

```python
prop = Edge.position_1
```

```python
prop = Edge.position_2
```

## Edges of Corner

> `bl_idname` : GeometryNodeEdgesOfCorner

### nd

nd.edges_of_corner.(cls, corner_index: Integer = None)

### class Mesh

```python
Mesh.edges_of_corner(cls, corner_index: Integer = None)
```

### class Corner

```python
Corner.edges(cls, corner_index: Integer = None)
```

```python
Corner.next_edge_index(cls, corner_index: Integer = None)
```

```python
Corner.previous_edge_index(cls, corner_index: Integer = None)
```

## Edges of Vertex

> `bl_idname` : GeometryNodeEdgesOfVertex

### nd

nd.edges_of_vertex.(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
Mesh.edges_of_vertex(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Vertex

```python
Vertex.edges(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Vertex.edge_index(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Vertex.edges_total(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Edges to Face Groups

> `bl_idname` : GeometryNodeEdgesToFaceGroups

### nd

nd.edges_to_face_groups.(cls, boundary_edges: Boolean = None)

### class Mesh

```python
Mesh.edges_to_face_groups(cls, boundary_edges: Boolean = None)
```

### class Edge

```python
Edge.to_face_groups(cls, boundary_edges: Boolean = None)
```

## Emission

> `bl_idname` : ShaderNodeEmission

### snd

nd.emission.(cls, color: Color = None, strength: Float = None, weight: Float = None)

### class Shader

```python
Shader.Emission(cls, color: Color = None, strength: Float = None)
```

## Enable Output

> `bl_idname` : NodeEnableOutput

### nd

nd.enable_output.(cls,
                    enable: Boolean = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT')

### class Float

```python
Float.enable_output(self, enable: Boolean = None)
```

### class Integer

```python
Integer.enable_output(self, enable: Boolean = None)
```

### class Boolean

```python
Boolean.enable_output(self, enable: Boolean = None)
```

### class Vector

```python
Vector.enable_output(self, enable: Boolean = None)
```

### class Color

```python
Color.enable_output(self, enable: Boolean = None)
```

### class Rotation

```python
Rotation.enable_output(self, enable: Boolean = None)
```

### class Matrix

```python
Matrix.enable_output(self, enable: Boolean = None)
```

### class String

```python
String.enable_output(self, enable: Boolean = None)
```

### class Menu

```python
Menu.enable_output(self, enable: Boolean = None)
```

### class Object

```python
Object.enable_output(self, enable: Boolean = None)
```

### class Image

```python
Image.enable_output(self, enable: Boolean = None)
```

### class Geometry

```python
Geometry.enable_output(self, enable: Boolean = None)
```

### class Collection

```python
Collection.enable_output(self, enable: Boolean = None)
```

### class Material

```python
Material.enable_output(self, enable: Boolean = None)
```

### class Bundle

```python
Bundle.enable_output(self, enable: Boolean = None)
```

### class Closure

```python
Closure.enable_output(self, enable: Boolean = None)
```

### class Font

```python
Font.enable_output(self, enable: Boolean = None)
```

## Endpoint Selection

> `bl_idname` : GeometryNodeCurveEndpointSelection

### nd

nd.endpoint_selection.(cls, start_size: Integer = None, end_size: Integer = None)

### class Curve

```python
Curve.endpoint_selection(cls, start_size: Integer = None, end_size: Integer = None)
```

## Environment Texture

> `bl_idname` : ShaderNodeTexEnvironment

### snd

nd.environment_texture.(cls,
                    vector: Vector = None,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR')

### class Vector

```python
Vector.environment_texture(self,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR')
```

## Euler to Rotation

> `bl_idname` : FunctionNodeEulerToRotation

### nd

nd.euler_to_rotation.(cls, euler: Vector = None)

### class Rotation

```python
Rotation.FromEuler(cls, euler: Vector = None)
```

### class Vector

```python
Vector.to_rotation(self)
```

## Evaluate Closure

> `bl_idname` : NodeEvaluateClosure

### nd

nd.evaluate_closure.(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False)

### snd

nd.evaluate_closure.(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False)

## Evaluate at Index

> `bl_idname` : GeometryNodeFieldAtIndex

### nd

nd.evaluate_at_index.(cls,
                    value: Float = None,
                    index: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Edge

```python
Edge.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Face

```python
Face.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Corner

```python
Corner.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Spline

```python
Spline.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Instance

```python
Instance.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Layer

```python
Layer.evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

## Evaluate on Domain

> `bl_idname` : GeometryNodeFieldOnDomain

### nd

nd.evaluate_on_domain.(cls,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Edge

```python
Edge.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Face

```python
Face.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Corner

```python
Corner.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Spline

```python
Spline.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Instance

```python
Instance.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Layer

```python
Layer.evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

## Extrude Mesh

> `bl_idname` : GeometryNodeExtrudeMesh

### nd

nd.extrude_mesh.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES')

### class Mesh

```python
Mesh.extrude_vertices(self, offset: Vector = None, offset_scale: Float = None)
```

```python
Mesh.extrude_edges(self, offset: Vector = None, offset_scale: Float = None)
```

```python
Mesh.extrude_faces(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None)
```

```python
Mesh.extrude(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES')
```

### class Vertex

```python
Vertex.extrude(self, offset: Vector = None, offset_scale: Float = None)
```

### class Edge

```python
Edge.extrude(self, offset: Vector = None, offset_scale: Float = None)
```

### class Face

```python
Face.extrude(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None)
```

## Face Area

> `bl_idname` : GeometryNodeInputMeshFaceArea

### nd

nd.face_area.(self)

### class Mesh

```python
prop = Mesh.face_area
```

### class Face

```python
prop = Face.area
```

## Face Group Boundaries

> `bl_idname` : GeometryNodeMeshFaceSetBoundaries

### nd

nd.face_group_boundaries.(cls, face_group_id: Integer = None)

### class Mesh

```python
Mesh.face_group_boundaries(cls, face_group_id: Integer = None)
```

## Face Neighbors

> `bl_idname` : GeometryNodeInputMeshFaceNeighbors

### nd

nd.face_neighbors.(cls)

### class Mesh

```python
prop = Mesh.face_neighbors
```

### class Face

```python
prop = Face.neighbors
```

```python
prop = Face.neighbors_vertex_count
```

```python
prop = Face.neighbors_face_count
```

## Face Set

> `bl_idname` : GeometryNodeToolFaceSet

### nd

nd.face_set.(cls)

## Face of Corner

> `bl_idname` : GeometryNodeFaceOfCorner

### nd

nd.face_of_corner.(cls, corner_index: Integer = None)

### class Mesh

```python
Mesh.face_of_corner(cls, corner_index: Integer = None)
```

### class Corner

```python
Corner.face(cls, corner_index: Integer = None)
```

```python
Corner.face_index(cls, corner_index: Integer = None)
```

```python
Corner.index_in_face(cls, corner_index: Integer = None)
```

## Field Average

> `bl_idname` : GeometryNodeFieldAverage

### nd

nd.field_average.(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
Edge.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
Face.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
Corner.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
Spline.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
Instance.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
Layer.field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field Min & Max

> `bl_idname` : GeometryNodeFieldMinAndMax

### nd

nd.field_min_max.(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
Edge.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
Face.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
Corner.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
Spline.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
Instance.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
Layer.field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field Variance

> `bl_idname` : GeometryNodeFieldVariance

### nd

nd.field_variance.(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
Edge.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
Face.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
Corner.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
Spline.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
Instance.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
Layer.field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field to Grid

> `bl_idname` : GeometryNodeFieldToGrid

### nd

nd.field_to_grid.(cls,
                    named_sockets: dict = {},
                    topology: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT',
                    **sockets)

### class Float

```python
Float.field_to_grid(self, named_sockets: dict = {}, **sockets)
```

### class Integer

```python
Integer.field_to_grid(self, named_sockets: dict = {}, **sockets)
```

### class Boolean

```python
Boolean.field_to_grid(self, named_sockets: dict = {}, **sockets)
```

### class Vector

```python
Vector.field_to_grid(self, named_sockets: dict = {}, **sockets)
```

## Field to List

> `bl_idname` : GeometryNodeFieldToList

### nd

nd.field_to_list.(cls, named_sockets: dict = {}, count: Integer = None, **sockets)

## Fill Curve

> `bl_idname` : GeometryNodeFillCurve

### nd

nd.fill_curve.(cls,
                    curve: Curve = None,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None,
                    fill_rule: Literal['Even-Odd', 'Non-Zero'] = None)

### class Curve

```python
Curve.fill(self,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None,
                    fill_rule: Literal['Even-Odd', 'Non-Zero'] = None)
```

## Fillet Curve

> `bl_idname` : GeometryNodeFilletCurve

### nd

nd.fillet_curve.(cls,
                    curve: Curve = None,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None)

### class Curve

```python
Curve.fillet(self,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None)
```

## Find in String

> `bl_idname` : FunctionNodeFindInString

### nd

nd.find_in_string.(cls, string: String = None, search: String = None)

### class String

```python
String.find_in_string(self, search: String = None)
```

```python
String.find(self, search: String = None)
```

## Flip Faces

> `bl_idname` : GeometryNodeFlipFaces

### nd

nd.flip_faces.(cls, mesh: Mesh = None, selection: Boolean = None)

### class Mesh

```python
Mesh.flip_faces(self)
```

## Float Curve

> `bl_idname` : ShaderNodeFloatCurve

### nd

nd.float_curve.(cls, value: Float = None, factor: Float = None)

### snd

nd.float_curve.(cls, value: Float = None, factor: Float = None)

## Float to Integer

> `bl_idname` : FunctionNodeFloatToInt

### nd

nd.float_to_integer.(cls,
                    float: Float = None,
                    rounding_mode: Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND')

### class Float

```python
Float.to_integer(self,
                    rounding_mode: Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND')
```

## For Each Geometry Element Input

> `bl_idname` : GeometryNodeForeachGeometryElementInput

### class Domain

## For Each Geometry Element Output

> `bl_idname` : GeometryNodeForeachGeometryElementOutput

### class Domain

## Format String

> `bl_idname` : FunctionNodeFormatString

### nd

nd.format_string.(cls, named_sockets: dict = {}, format: String = None, **sockets)

### class String

```python
String.format(self, named_sockets: dict = {}, **sockets)
```

```python
String.Format(cls, named_sockets: dict = {}, format: String = None, **sockets)
```

## Frame

> `bl_idname` : NodeFrame

### class Layout

## Fresnel

> `bl_idname` : ShaderNodeFresnel

### snd

nd.fresnel.(cls, ior: Float = None, normal: Vector = None)

### class Float

```python
Float.fresnel(self, normal: Vector = None)
```

## Gabor Texture

> `bl_idname` : ShaderNodeTexGabor

### nd

nd.gabor_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D')

### snd

nd.gabor_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D')

### class Float

```python
Float.Gabor(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    gabor_type: Literal['2D', '3D'] = '2D')
```

### class Texture

```python
Texture.Gabor(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    gabor_type: Literal['2D', '3D'] = '2D')
```

## Gamma

> `bl_idname` : ShaderNodeGamma

### nd

nd.gamma.(cls, color: Color = None, gamma: Float = None)

### snd

nd.gamma.(cls, color: Color = None, gamma: Float = None)

### class Color

```python
Color.gamma(self, gamma: Float = None)
```

## Geometry

> `bl_idname` : ShaderNodeNewGeometry

### snd

nd.geometry.(cls)

## Geometry Proximity

> `bl_idname` : GeometryNodeProximity

### nd

nd.geometry_proximity.(cls,
                    geometry: Geometry = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES')

### class Geometry

```python
Geometry.proximity(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES')
```

```python
Geometry.proximity_points(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

```python
Geometry.proximity_edges(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

```python
Geometry.proximity_faces(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

## Geometry to Instance

> `bl_idname` : GeometryNodeGeometryToInstance

### nd

nd.geometry_to_instance.(cls, *geometry: Geometry)

### class Geometry

```python
Geometry.to_instance(self, *geometry: Geometry)
```

### class Instances

```python
Instances.FromGeometry(cls, *geometry: Geometry)
```

## Get Bundle Item

> `bl_idname` : NodeGetBundleItem

### nd

nd.get_bundle_item.(cls,
                    bundle: Bundle = None,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

### class Bundle

```python
Bundle.get_item(self,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

## Get Geometry Bundle

> `bl_idname` : GeometryNodeGetGeometryBundle

### nd

nd.get_geometry_bundle.(cls, geometry: Geometry = None, remove: Boolean = None)

## Get List Item

> `bl_idname` : GeometryNodeListGetItem

### nd

nd.get_list_item.(cls,
                    list: Float = None,
                    index: Integer = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

## Get Named Grid

> `bl_idname` : GeometryNodeGetNamedGrid

### nd

nd.get_named_grid.(cls,
                    volume: Volume = None,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Volume

```python
Volume.get_named_grid(self,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')
```

## Glass BSDF

> `bl_idname` : ShaderNodeBsdfGlass

### snd

nd.glass_bsdf.(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX')

### class Shader

```python
Shader.Glass(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX')
```

## Glossy BSDF

> `bl_idname` : ShaderNodeBsdfAnisotropic

### snd

nd.glossy_bsdf.(cls,
                    color: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    weight: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'] = 'MULTI_GGX')

### class Shader

```python
Shader.Glossy(cls,
                    color: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    distribution: Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'] = 'MULTI_GGX')
```

## Gradient Texture

> `bl_idname` : ShaderNodeTexGradient

### nd

nd.gradient_texture.(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')

### snd

nd.gradient_texture.(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')

### class Color

```python
Color.Gradient(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')
```

### class Texture

```python
Texture.Gradient(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')
```

## Grease Pencil to Curves

> `bl_idname` : GeometryNodeGreasePencilToCurves

### nd

nd.grease_pencil_to_curves.(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    layers_as_instances: Boolean = None)

### class GreasePencil

```python
GreasePencil.to_curves(self, layers_as_instances: Boolean = None)
```

## Grid

> `bl_idname` : GeometryNodeMeshGrid

### nd

nd.grid.(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None)

### class Mesh

```python
Mesh.Grid(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None)
```

## Grid Curl

> `bl_idname` : GeometryNodeGridCurl

### nd

nd.grid_curl.(cls, grid: Vector = None)

### class Vector

```python
Vector.grid_curl(self)
```

## Grid Dilate & Erode

> `bl_idname` : GeometryNodeGridDilateAndErode

### nd

nd.grid_dilate_erode.(cls,
                    grid: Float = None,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Integer

```python
Integer.grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Boolean

```python
Boolean.grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Vector

```python
Vector.grid_dilate_erode(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

## Grid Divergence

> `bl_idname` : GeometryNodeGridDivergence

### nd

nd.grid_divergence.(cls, grid: Vector = None)

### class Vector

```python
Vector.grid_divergence(self)
```

## Grid Gradient

> `bl_idname` : GeometryNodeGridGradient

### nd

nd.grid_gradient.(cls, grid: Float = None)

### class Float

```python
Float.grid_gradient(self)
```

## Grid Info

> `bl_idname` : GeometryNodeGridInfo

### nd

nd.grid_info.(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.grid_info(self)
```

### class Integer

```python
Integer.grid_info(self)
```

### class Boolean

```python
Boolean.grid_info(self)
```

### class Vector

```python
Vector.grid_info(self)
```

## Grid Laplacian

> `bl_idname` : GeometryNodeGridLaplacian

### nd

nd.grid_laplacian.(cls, grid: Float = None)

### class Float

```python
Float.grid_laplacian(self)
```

## Grid Mean

> `bl_idname` : GeometryNodeGridMean

### nd

nd.grid_mean.(cls,
                    grid: Float = None,
                    width: Integer = None,
                    iterations: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.grid_mean(self, width: Integer = None, iterations: Integer = None)
```

### class Integer

```python
Integer.grid_mean(self, width: Integer = None, iterations: Integer = None)
```

### class Vector

```python
Vector.grid_mean(self, width: Integer = None, iterations: Integer = None)
```

## Grid Median

> `bl_idname` : GeometryNodeGridMedian

### nd

nd.grid_median.(cls,
                    grid: Float = None,
                    width: Integer = None,
                    iterations: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.grid_median(self, width: Integer = None, iterations: Integer = None)
```

### class Integer

```python
Integer.grid_median(self, width: Integer = None, iterations: Integer = None)
```

### class Vector

```python
Vector.grid_median(self, width: Integer = None, iterations: Integer = None)
```

## Grid to Mesh

> `bl_idname` : GeometryNodeGridToMesh

### nd

nd.grid_to_mesh.(cls, grid: Float = None, threshold: Float = None, adaptivity: Float = None)

### class Float

```python
Float.grid_to_mesh(self, threshold: Float = None, adaptivity: Float = None)
```

## Grid to Points

> `bl_idname` : GeometryNodeGridToPoints

### nd

nd.grid_to_points.(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.grid_to_points(self)
```

### class Integer

```python
Integer.grid_to_points(self)
```

### class Boolean

```python
Boolean.grid_to_points(self)
```

### class Vector

```python
Vector.grid_to_points(self)
```

## Group

> `bl_idname` : ShaderNodeGroup

### class Group

## Group Input

> `bl_idname` : NodeGroupInput

### nd

nd.group_input.(self)

### snd

nd.group_input.(self)

## Group Output

> `bl_idname` : NodeGroupOutput

### nd

nd.group_output.(cls, is_active_output = True)

### snd

nd.group_output.(cls, is_active_output = True)

## Hair BSDF

> `bl_idname` : ShaderNodeBsdfHair

### snd

nd.hair_bsdf.(cls,
                    color: Color = None,
                    offset: Float = None,
                    roughnessu: Float = None,
                    roughnessv: Float = None,
                    tangent: Vector = None,
                    weight: Float = None,
                    component: Literal['Reflection', 'Transmission'] = 'Reflection')

### class Shader

```python
Shader.Hair(cls,
                    color: Color = None,
                    offset: Float = None,
                    roughnessu: Float = None,
                    roughnessv: Float = None,
                    tangent: Vector = None,
                    component: Literal['Reflection', 'Transmission'] = 'Reflection')
```

## Handle Type Selection

> `bl_idname` : GeometryNodeCurveHandleTypeSelection

### nd

nd.handle_type_selection.(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})

### class Curve

```python
Curve.handle_type_selection(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})
```

## Hash Value

> `bl_idname` : FunctionNodeHashValue

### nd

nd.hash_value.(cls,
                    value: Integer = None,
                    seed: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING'] = 'INT')

### class Float

```python
Float.hash_value(self, seed: Integer = None)
```

### class Integer

```python
Integer.hash_value(self, seed: Integer = None)
```

### class Vector

```python
Vector.hash_value(self, seed: Integer = None)
```

### class Color

```python
Color.hash_value(self, seed: Integer = None)
```

### class Rotation

```python
Rotation.hash_value(self, seed: Integer = None)
```

### class Matrix

```python
Matrix.hash_value(self, seed: Integer = None)
```

### class String

```python
String.hash_value(self, seed: Integer = None)
```

## Holdout

> `bl_idname` : ShaderNodeHoldout

### snd

nd.holdout.(cls, weight: Float = None)

### class Shader

```python
Shader.Holdout(cls)
```

## Hue/Saturation/Value

> `bl_idname` : ShaderNodeHueSaturation

### snd

nd.hue_saturation_value.(cls,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None)

### class Float

```python
Float.hue_saturation_value(self,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None)
```

### class Color

```python
Color.hue_saturation_value(self,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    factor: Float = None)
```

## ID

> `bl_idname` : GeometryNodeInputID

### nd

nd.id.(self)

### class Geometry

```python
prop = Geometry.id
```

## IES Texture

> `bl_idname` : ShaderNodeTexIES

### snd

nd.ies_texture.(cls,
                    vector: Vector = None,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL')

### class Vector

```python
Vector.ies_texture_internal(self, strength: Float = None, filepath = '', ies = None)
```

```python
Vector.ies_texture_external(self, strength: Float = None, filepath = '', ies = None)
```

```python
Vector.ies_texture(self,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL')
```

## Ico Sphere

> `bl_idname` : GeometryNodeMeshIcoSphere

### nd

nd.ico_sphere.(cls, radius: Float = None, subdivisions: Integer = None)

### class Mesh

```python
Mesh.IcoSphere(cls, radius: Float = None, subdivisions: Integer = None)
```

## Image

> `bl_idname` : GeometryNodeInputImage

### nd

nd.image.(cls, image = None)

## Image Info

> `bl_idname` : GeometryNodeImageInfo

### nd

nd.image_info.(cls, image: Image = None, frame: Integer = None)

### class Image

```python
Image.info(self, frame: Integer = None)
```

```python
Image.width(self, frame: Integer = None)
```

```python
Image.height(self, frame: Integer = None)
```

```python
Image.has_alpha(self, frame: Integer = None)
```

```python
Image.frame_count(self, frame: Integer = None)
```

```python
Image.fps(self, frame: Integer = None)
```

## Image Texture

> `bl_idname` : ShaderNodeTexImage

### snd

nd.image_texture.(cls,
                    vector: Vector = None,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0)

### class Vector

```python
Vector.image_texture(self,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0)
```

## Import CSV

> `bl_idname` : GeometryNodeImportCSV

### nd

nd.import_csv.(cls, path: String = None, delimiter: String = None)

### class Cloud

```python
Cloud.ImportCSV(cls, path: String = None, delimiter: String = None)
```

## Import OBJ

> `bl_idname` : GeometryNodeImportOBJ

### nd

nd.import_obj.(cls, path: String = None)

### class Instances

```python
Instances.ImportOBJ(cls, path: String = None)
```

## Import PLY

> `bl_idname` : GeometryNodeImportPLY

### nd

nd.import_ply.(cls, path: String = None)

### class Mesh

```python
Mesh.ImportPLY(cls, path: String = None)
```

## Import STL

> `bl_idname` : GeometryNodeImportSTL

### nd

nd.import_stl.(cls, path: String = None)

### class Mesh

```python
Mesh.ImportSTL(cls, path: String = None)
```

## Import Text

> `bl_idname` : GeometryNodeImportText

### nd

nd.import_text.(cls, path: String = None)

### class String

```python
String.ImportText(cls, path: String = None)
```

## Import VDB

> `bl_idname` : GeometryNodeImportVDB

### nd

nd.import_vdb.(cls, path: String = None)

### class Volume

```python
Volume.ImportVDB(cls, path: String = None)
```

## Index

> `bl_idname` : GeometryNodeInputIndex

### nd

nd.index.(self)

### class Geometry

```python
prop = Geometry.index
```

## Index Switch

> `bl_idname` : GeometryNodeIndexSwitch

### class Socket

```python
Socket.IndexSwitch(*values, index=0)
```

```python
Socket.index_switch(*values, index=0)
```

## Index of Nearest

> `bl_idname` : GeometryNodeIndexOfNearest

### nd

nd.index_of_nearest.(cls, position: Vector = None, group_id: Integer = None)

### class Geometry

```python
Geometry.index_of_nearest(cls, position: Vector = None, group_id: Integer = None)
```

## Instance Bounds

> `bl_idname` : GeometryNodeInputInstanceBounds

### nd

nd.instance_bounds.(cls, use_radius: Boolean = None)

## Instance Rotation

> `bl_idname` : GeometryNodeInputInstanceRotation

### nd

nd.instance_rotation.(self)

### class Instances

```python
prop = Instances.rotation
```

## Instance Scale

> `bl_idname` : GeometryNodeInputInstanceScale

### nd

nd.instance_scale.(self)

### class Instances

```python
prop = Instances.instance_scale
```

## Instance Transform

> `bl_idname` : GeometryNodeInstanceTransform

### nd

nd.instance_transform.(self)

### class Instances

```python
prop = Instances.transform
```

## Instance on Points

> `bl_idname` : GeometryNodeInstanceOnPoints

### nd

nd.instance_on_points.(cls,
                    points: Cloud = None,
                    selection: Boolean = None,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)

### class Geometry

```python
Geometry.instance_on_points(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

### class Cloud

```python
Cloud.instance_on(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

### class Point

```python
Point.instance_on(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

## Instances to Points

> `bl_idname` : GeometryNodeInstancesToPoints

### nd

nd.instances_to_points.(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None)

### class Instances

```python
Instances.to_points(self, position: Vector = None, radius: Float = None)
```

## Integer

> `bl_idname` : FunctionNodeInputInt

### nd

nd.integer.(cls, integer = 0)

## Integer Math

> `bl_idname` : FunctionNodeIntegerMath

### nd

nd.integer_math.(cls,
                    value: Integer = None,
                    value_1: Integer = None,
                    value_2: Integer = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM'] = 'ADD')

### class Integer

```python
Integer.add(self, value: Integer = None)
```

```python
Integer.subtract(self, value: Integer = None)
```

```python
Integer.multiply(self, value: Integer = None)
```

```python
Integer.divide(self, value: Integer = None)
```

```python
Integer.multiply_add(self, multiplier: Integer = None, addend: Integer = None)
```

```python
Integer.abs(self)
```

```python
Integer.negate(self)
```

```python
Integer.power(self, exponent: Integer = None)
```

```python
Integer.min(self, value: Integer = None)
```

```python
Integer.max(self, value: Integer = None)
```

```python
Integer.sign(self)
```

```python
Integer.divide_round(self, value: Integer = None)
```

```python
Integer.divide_floor(self, value: Integer = None)
```

```python
Integer.divide_ceil(self, value: Integer = None)
```

```python
Integer.floored_modulo(self, value: Integer = None)
```

```python
Integer.modulo(self, value: Integer = None)
```

```python
Integer.gcd(self, value: Integer = None)
```

```python
Integer.lcm(self, value: Integer = None)
```

### class gnmath

```python
gnmath.iadd(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.isubtract(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.imultiply(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.idivide(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.imultiply_add(value: Integer = None, multiplier: Integer = None, addend: Integer = None)
```

```python
gnmath.iabs(value: Integer = None)
```

```python
gnmath.negate(value: Integer = None)
```

```python
gnmath.ipower(base: Integer = None, exponent: Integer = None)
```

```python
gnmath.imin(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.imax(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.isign(value: Integer = None)
```

```python
gnmath.divide_round(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.divide_floor(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.divide_ceil(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.ifloored_modulo(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.imodulo(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.gcd(value: Integer = None, value_1: Integer = None)
```

```python
gnmath.lcm(value: Integer = None, value_1: Integer = None)
```

## Interpolate Curves

> `bl_idname` : GeometryNodeInterpolateCurves

### nd

nd.interpolate_curves.(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)

### class Curve

```python
Curve.Interpolate(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)
```

```python
Curve.interpolate(self,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)
```

### class Cloud

```python
Cloud.interpolate_curves(self,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)
```

## Invert Color

> `bl_idname` : ShaderNodeInvert

### snd

nd.invert_color.(cls, color: Color = None, factor: Float = None)

### class Color

```python
Color.invert_color(self, factor: Float = None)
```

## Invert Matrix

> `bl_idname` : FunctionNodeInvertMatrix

### nd

nd.invert_matrix.(cls, matrix: Matrix = None)

### class Matrix

```python
Matrix.invert(self)
```

## Invert Rotation

> `bl_idname` : FunctionNodeInvertRotation

### nd

nd.invert_rotation.(cls, rotation: Rotation = None)

### class Rotation

```python
Rotation.invert(self)
```

## Is Edge Smooth

> `bl_idname` : GeometryNodeInputEdgeSmooth

### nd

nd.is_edge_smooth.(self)

### class Edge

```python
prop = Edge.shade_smooth
```

```python
prop = Edge.smooth
```

## Is Face Planar

> `bl_idname` : GeometryNodeInputMeshFaceIsPlanar

### nd

nd.is_face_planar.(cls, threshold: Float = None)

### class Mesh

```python
Mesh.is_face_planar(cls, threshold: Float = None)
```

### class Face

```python
Face.is_planar(cls, threshold: Float = None)
```

## Is Face Smooth

> `bl_idname` : GeometryNodeInputShadeSmooth

### nd

nd.is_face_smooth.(self)

### class Face

```python
prop = Face.shade_smooth
```

```python
prop = Face.smooth
```

## Is Spline Cyclic

> `bl_idname` : GeometryNodeInputSplineCyclic

### nd

nd.is_spline_cyclic.(self)

### class Curve

```python
prop = Curve.is_cyclic
```

### class Spline

```python
prop = Spline.is_cyclic
```

## Is Viewport

> `bl_idname` : GeometryNodeIsViewport

### nd

nd.is_viewport.(self)

### class Boolean

```python
prop = Boolean.is_viewport
```

## Join Bundle

> `bl_idname` : NodeJoinBundle

### nd

nd.join_bundle.(cls, *bundle: Bundle)

### snd

nd.join_bundle.(cls, *bundle: Bundle)

### class Bundle

```python
Bundle.join(self, *bundle: Bundle)
```

```python
Bundle.join_bundle(self, *bundle: Bundle)
```

## Join Geometry

> `bl_idname` : GeometryNodeJoinGeometry

### nd

nd.join_geometry.(cls, *geometry: Geometry)

### class Geometry

```python
Geometry.join(self, *geometry: Geometry)
```

```python
Geometry.Join(cls, *geometry: Geometry)
```

## Join Strings

> `bl_idname` : GeometryNodeStringJoin

### nd

nd.join_strings.(cls, *strings: String, delimiter: String = None)

### class String

```python
String.join(self, *strings: String)
```

```python
String.Join(cls, *strings: String, delimiter: String = None)
```

## Layer Weight

> `bl_idname` : ShaderNodeLayerWeight

### snd

nd.layer_weight.(cls, blend: Float = None, normal: Vector = None)

### class Float

```python
Float.layer_weight(self, normal: Vector = None)
```

## Light Falloff

> `bl_idname` : ShaderNodeLightFalloff

### snd

nd.light_falloff.(cls, strength: Float = None, smooth: Float = None)

### class Float

```python
Float.light_falloff(self, smooth: Float = None)
```

## Light Output

> `bl_idname` : ShaderNodeOutputLight

### snd

nd.light_output.(cls,
                    surface: Shader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
Shader.light_output(self,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

## Light Path

> `bl_idname` : ShaderNodeLightPath

### snd

nd.light_path.(cls)

## Line Style Output

> `bl_idname` : ShaderNodeOutputLineStyle

### snd

nd.line_style_output.(cls,
                    color: Color = None,
                    color_fac: Float = None,
                    alpha: Float = None,
                    alpha_fac: Float = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL',
                    use_alpha = False,
                    use_clamp = False)

### class Color

```python
Color.line_style_output(self,
                    color_fac: Float = None,
                    alpha: Float = None,
                    alpha_fac: Float = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL',
                    use_alpha = False,
                    use_clamp = False)
```

## Linear Gizmo

> `bl_idname` : GeometryNodeGizmoLinear

### nd

nd.linear_gizmo.(cls,
                    *value: Float,
                    position: Vector = None,
                    direction: Vector = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY',
                    draw_style: Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW')

### class Float

```python
Float.linear_gizmo(self,
                    *value: Float,
                    position: Vector = None,
                    direction: Vector = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY',
                    draw_style: Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW')
```

## List Length

> `bl_idname` : GeometryNodeListLength

### nd

nd.list_length.(cls,
                    list: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT')

## Magic Texture

> `bl_idname` : ShaderNodeTexMagic

### nd

nd.magic_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)

### snd

nd.magic_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)

### class Color

```python
Color.Magic(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)
```

### class Texture

```python
Texture.Magic(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)
```

## Map Range

> `bl_idname` : ShaderNodeMapRange

### nd

nd.map_range.(cls,
                    value: Float = None,
                    from_min: Float = None,
                    from_max: Float = None,
                    to_min: Float = None,
                    to_max: Float = None,
                    steps: Float = None,
                    vector: Vector = None,
                    from_min_1: Vector = None,
                    from_max_1: Vector = None,
                    to_min_1: Vector = None,
                    to_max_1: Vector = None,
                    steps_1: Vector = None,
                    clamp = True,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR')

### snd

nd.map_range.(cls,
                    value: Float = None,
                    from_min: Float = None,
                    from_max: Float = None,
                    to_min: Float = None,
                    to_max: Float = None,
                    steps: Float = None,
                    vector: Vector = None,
                    from_min_1: Vector = None,
                    from_max_1: Vector = None,
                    to_min_1: Vector = None,
                    to_max_1: Vector = None,
                    steps_1: Vector = None,
                    clamp = True,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR')

### class Float

```python
Float.map_range(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True,
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR')
```

```python
Float.map_range_linear(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

```python
Float.map_range_stepped(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    steps: Float = None,
                    clamp = True)
```

```python
Float.map_range_smooth_step(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

```python
Float.map_range_smoother_step(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

### class Vector

```python
Vector.map_range(self,
                    from_min: Vector = None,
                    from_max: Vector = None,
                    to_min: Vector = None,
                    to_max: Vector = None,
                    clamp = True,
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR')
```

## Mapping

> `bl_idname` : ShaderNodeMapping

### snd

nd.mapping.(cls,
                    vector: Vector = None,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT')

### class Vector

```python
Vector.mapping(self,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT')
```

## Match String

> `bl_idname` : FunctionNodeMatchString

### nd

nd.match_string.(cls,
                    string: String = None,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None)

### class String

```python
String.match_string(self,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None)
```

## Material

> `bl_idname` : GeometryNodeInputMaterial

### nd

nd.material.(cls, material = None)

## Material Index

> `bl_idname` : GeometryNodeInputMaterialIndex

### nd

nd.material_index.(self)

### class Geometry

```python
prop = Geometry.material_index
```

### class Face

```python
prop = Face.material_index
```

### class Spline

```python
prop = Spline.material_index
```

## Material Output

> `bl_idname` : ShaderNodeOutputMaterial

### snd

nd.material_output.(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
Shader.material_output(self,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

## Material Selection

> `bl_idname` : GeometryNodeMaterialSelection

### nd

nd.material_selection.(cls, material: Material = None)

### class Mesh

```python
Mesh.material_selection(cls, material: Material = None)
```

### class Curve

```python
Curve.material_selection(cls, material: Material = None)
```

## Math

> `bl_idname` : ShaderNodeMath

### nd

nd.math.(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False)

### snd

nd.math.(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False)

### class Float

```python
Float.add(self, value: Float = None, use_clamp = False)
```

```python
Float.subtract(self, value: Float = None, use_clamp = False)
```

```python
Float.multiply(self, value: Float = None, use_clamp = False)
```

```python
Float.divide(self, value: Float = None, use_clamp = False)
```

```python
Float.multiply_add(self, multiplier: Float = None, addend: Float = None, use_clamp = False)
```

```python
Float.power(self, exponent: Float = None, use_clamp = False)
```

```python
Float.log(self, base: Float = None, use_clamp = False)
```

```python
Float.sqrt(self, use_clamp = False)
```

```python
Float.inverse_sqrt(self, use_clamp = False)
```

```python
Float.abs(self, use_clamp = False)
```

```python
Float.exp(self, use_clamp = False)
```

```python
Float.min(self, value: Float = None, use_clamp = False)
```

```python
Float.max(self, value: Float = None, use_clamp = False)
```

```python
Float.mless_than(self, threshold: Float = None, use_clamp = False)
```

```python
Float.mgreater_than(self, threshold: Float = None, use_clamp = False)
```

```python
Float.sign(self, use_clamp = False)
```

```python
Float.compare(self, value: Float = None, epsilon: Float = None, use_clamp = False)
```

```python
Float.smooth_min(self, value: Float = None, distance: Float = None, use_clamp = False)
```

```python
Float.smooth_max(self, value: Float = None, distance: Float = None, use_clamp = False)
```

```python
Float.round(self, use_clamp = False)
```

```python
Float.floor(self, use_clamp = False)
```

```python
Float.ceil(self, use_clamp = False)
```

```python
Float.trunc(self, use_clamp = False)
```

```python
Float.fract(self, use_clamp = False)
```

```python
Float.modulo(self, value: Float = None, use_clamp = False)
```

```python
Float.floored_modulo(self, value: Float = None, use_clamp = False)
```

```python
Float.wrap(self, max: Float = None, min: Float = None, use_clamp = False)
```

```python
Float.snap(self, increment: Float = None, use_clamp = False)
```

```python
Float.pingpong(self, scale: Float = None, use_clamp = False)
```

```python
Float.sin(self, use_clamp = False)
```

```python
Float.cos(self, use_clamp = False)
```

```python
Float.tan(self, use_clamp = False)
```

```python
Float.asin(self, use_clamp = False)
```

```python
Float.acos(self, use_clamp = False)
```

```python
Float.arctangent(self, use_clamp = False)
```

```python
Float.atan2(self, value: Float = None, use_clamp = False)
```

```python
Float.sinh(self, use_clamp = False)
```

```python
Float.cosh(self, use_clamp = False)
```

```python
Float.tanh(self, use_clamp = False)
```

```python
Float.radians(self, use_clamp = False)
```

```python
Float.degrees(self, use_clamp = False)
```

### class gnmath

```python
gnmath.add(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.subtract(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.multiply(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.divide(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.multiply_add(value: Float = None,
                    multiplier: Float = None,
                    addend: Float = None,
                    use_clamp = False)
```

```python
gnmath.power(base: Float = None, exponent: Float = None, use_clamp = False)
```

```python
gnmath.log(value: Float = None, base: Float = None, use_clamp = False)
```

```python
gnmath.sqrt(value: Float = None, use_clamp = False)
```

```python
gnmath.inverse_sqrt(value: Float = None, use_clamp = False)
```

```python
gnmath.abs(value: Float = None, use_clamp = False)
```

```python
gnmath.exp(value: Float = None, use_clamp = False)
```

```python
gnmath.min(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.max(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.mless_than(value: Float = None, threshold: Float = None, use_clamp = False)
```

```python
gnmath.mgreater_than(value: Float = None, threshold: Float = None, use_clamp = False)
```

```python
gnmath.sign(value: Float = None, use_clamp = False)
```

```python
gnmath.compare(value: Float = None,
                    value_1: Float = None,
                    epsilon: Float = None,
                    use_clamp = False)
```

```python
gnmath.smooth_min(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False)
```

```python
gnmath.smooth_max(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False)
```

```python
gnmath.round(value: Float = None, use_clamp = False)
```

```python
gnmath.floor(value: Float = None, use_clamp = False)
```

```python
gnmath.ceil(value: Float = None, use_clamp = False)
```

```python
gnmath.trunc(value: Float = None, use_clamp = False)
```

```python
gnmath.fract(value: Float = None, use_clamp = False)
```

```python
gnmath.modulo(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.floored_modulo(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.wrap(value: Float = None, max: Float = None, min: Float = None, use_clamp = False)
```

```python
gnmath.snap(value: Float = None, increment: Float = None, use_clamp = False)
```

```python
gnmath.pingpong(value: Float = None, scale: Float = None, use_clamp = False)
```

```python
gnmath.sin(value: Float = None, use_clamp = False)
```

```python
gnmath.cos(value: Float = None, use_clamp = False)
```

```python
gnmath.tan(value: Float = None, use_clamp = False)
```

```python
gnmath.asin(value: Float = None, use_clamp = False)
```

```python
gnmath.acos(value: Float = None, use_clamp = False)
```

```python
gnmath.arctangent(value: Float = None, use_clamp = False)
```

```python
gnmath.atan2(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
gnmath.sinh(value: Float = None, use_clamp = False)
```

```python
gnmath.cosh(value: Float = None, use_clamp = False)
```

```python
gnmath.tanh(value: Float = None, use_clamp = False)
```

```python
gnmath.radians(degrees: Float = None, use_clamp = False)
```

```python
gnmath.degrees(radians: Float = None, use_clamp = False)
```

## Matrix Determinant

> `bl_idname` : FunctionNodeMatrixDeterminant

### nd

nd.matrix_determinant.(cls, matrix: Matrix = None)

### class Matrix

```python
Matrix.determinant(self)
```

## Matrix SVD

> `bl_idname` : FunctionNodeMatrixSVD

### nd

nd.matrix_svd.(cls, matrix: Matrix = None)

### class Matrix

```python
Matrix.svd(self)
```

## Menu Switch

> `bl_idname` : GeometryNodeMenuSwitch

### class Socket

```python
Socket.MenuSwitch(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None, panel=None, hide_value=False, hide_in_modifier=False, single_value=False)
```

```python
Socket.menu_switch(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None, panel=None, hide_value=False, hide_in_modifier=False, single_value=False)
```

## Merge Layers

> `bl_idname` : GeometryNodeMergeLayers

### nd

nd.merge_layers.(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME')

### class GreasePencil

```python
GreasePencil.merge_layers_by_name(self)
```

```python
GreasePencil.merge_layers_by_id(self, group_id: Integer = None)
```

```python
GreasePencil.merge_layers(self, mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME')
```

## Merge by Distance

> `bl_idname` : GeometryNodeMergeByDistance

### nd

nd.merge_by_distance.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    mode: Literal['All', 'Connected'] = None,
                    distance: Float = None)

### class Geometry

```python
Geometry.merge_by_distance(self, mode: Literal['All', 'Connected'] = None, distance: Float = None)
```

```python
Geometry.merge(self, mode: Literal['All', 'Connected'] = None, distance: Float = None)
```

## Mesh Boolean

> `bl_idname` : GeometryNodeMeshBoolean

### nd

nd.mesh_boolean.(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    self_intersection: Boolean = None,
                    hole_tolerant: Boolean = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')

### class Mesh

```python
Mesh.boolean(self,
                    *mesh_2: Mesh,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.Boolean(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.intersect(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.union(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.difference(self, *mesh_2: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.Intersect(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.Union(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
Mesh.Difference(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

## Mesh Circle

> `bl_idname` : GeometryNodeMeshCircle

### nd

nd.mesh_circle.(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE')

### class Mesh

```python
Mesh.Circle(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE')
```

## Mesh Island

> `bl_idname` : GeometryNodeInputMeshIsland

### nd

nd.mesh_island.(cls)

### class Mesh

```python
prop = Mesh.mesh_island
```

```python
prop = Mesh.island_index
```

```python
prop = Mesh.island_count
```

## Mesh Line

> `bl_idname` : GeometryNodeMeshLine

### nd

nd.mesh_line.(cls,
                    count: Integer = None,
                    resolution: Float = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET')

### class Mesh

```python
Mesh.LineOffset(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL')
```

```python
Mesh.LineEndPoints(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    end_location: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL')
```

```python
Mesh.Line(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET')
```

## Mesh to Curve

> `bl_idname` : GeometryNodeMeshToCurve

### nd

nd.mesh_to_curve.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    mode: Literal['EDGES', 'FACES'] = 'EDGES')

### class Mesh

```python
Mesh.to_curve_edges(self)
```

```python
Mesh.to_curve_faces(self)
```

```python
Mesh.to_curve(self, mode: Literal['EDGES', 'FACES'] = 'EDGES')
```

## Mesh to Density Grid

> `bl_idname` : GeometryNodeMeshToDensityGrid

### nd

nd.mesh_to_density_grid.(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None)

### class Mesh

```python
Mesh.to_density_grid(self,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None)
```

## Mesh to Points

> `bl_idname` : GeometryNodeMeshToPoints

### nd

nd.mesh_to_points.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES')

### class Mesh

```python
Mesh.to_points(self,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES')
```

```python
Mesh.vertices_to_points(self, position: Vector = None, radius: Float = None)
```

```python
Mesh.edges_to_points(self, position: Vector = None, radius: Float = None)
```

```python
Mesh.faces_to_points(self, position: Vector = None, radius: Float = None)
```

```python
Mesh.corners_to_points(self, position: Vector = None, radius: Float = None)
```

### class Vertex

```python
Vertex.to_points(self, position: Vector = None, radius: Float = None)
```

### class Face

```python
Face.to_points(self, position: Vector = None, radius: Float = None)
```

### class Edge

```python
Edge.to_points(self, position: Vector = None, radius: Float = None)
```

### class Corner

```python
Corner.to_points(self, position: Vector = None, radius: Float = None)
```

## Mesh to SDF Grid

> `bl_idname` : GeometryNodeMeshToSDFGrid

### nd

nd.mesh_to_sdf_grid.(cls, mesh: Mesh = None, voxel_size: Float = None, band_width: Integer = None)

### class Mesh

```python
Mesh.to_sdf_grid(self, voxel_size: Float = None, band_width: Integer = None)
```

## Mesh to Volume

> `bl_idname` : GeometryNodeMeshToVolume

### nd

nd.mesh_to_volume.(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None)

### class Mesh

```python
Mesh.to_volume(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None)
```

## Metallic BSDF

> `bl_idname` : ShaderNodeBsdfMetallic

### snd

nd.metallic_bsdf.(cls,
                    base_color: Color = None,
                    edge_tint: Color = None,
                    ior: Vector = None,
                    extinction: Vector = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    weight: Float = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    fresnel_type: Literal['PHYSICAL_CONDUCTOR', 'F82'] = 'F82')

### class Shader

```python
Shader.Metallic(cls,
                    base_color: Color = None,
                    edge_tint: Color = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    rotation: Float = None,
                    normal: Vector = None,
                    tangent: Vector = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    fresnel_type: Literal['PHYSICAL_CONDUCTOR', 'F82'] = 'F82')
```

## Mix

> `bl_idname` : ShaderNodeMix

### nd

nd.mix.(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Vector = None,
                    b_1: Vector = None,
                    a_2: Color = None,
                    b_2: Color = None,
                    a_3: Rotation = None,
                    b_3: Rotation = None,
                    factor: Vector = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    clamp_factor = True,
                    clamp_result = False,
                    data_type: Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION'] = 'FLOAT',
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM')

### snd

nd.mix.(cls,
                    a: Float = None,
                    b: Float = None,
                    a_1: Vector = None,
                    b_1: Vector = None,
                    a_2: Color = None,
                    b_2: Color = None,
                    a_3: Rotation = None,
                    b_3: Rotation = None,
                    factor: Vector = None,
                    blend_type: Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX',
                    clamp_factor = True,
                    clamp_result = False,
                    data_type: Literal['FLOAT', 'VECTOR', 'RGBA'] = 'FLOAT',
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM')

### class Float

```python
Float.mix(self, b: Float = None, factor: Float = None, clamp_factor = True)
```

### class Rotation

```python
Rotation.mix(self, b: Rotation = None, factor: Float = None, clamp_factor = True)
```

### class Vector

```python
Vector.mix_uniform(self, b: Vector = None, factor: Float = None, clamp_factor = True)
```

```python
Vector.mix_non_uniform(self, b: Vector = None, factor: Vector = None, clamp_factor = True)
```

### class Color

```python
Color.mix_mix(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_darken(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_multiply(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_burn(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_lighten(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_screen(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_dodge(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_add(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_overlay(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_soft_light(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_linear_light(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_difference(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_exclusion(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_subtract(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_divide(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_hue(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_saturation(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_color(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix_value(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
Color.mix(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False,
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM')
```

## Mix Shader

> `bl_idname` : ShaderNodeMixShader

### snd

nd.mix_shader.(cls, shader: Shader = None, shader_1: Shader = None, factor: Float = None)

### class Shader

```python
Shader.mix(self, shader: Shader = None, factor: Float = None)
```

## Mouse Position

> `bl_idname` : GeometryNodeToolMousePosition

### nd

nd.mouse_position.(cls)

## Multiply Matrices

> `bl_idname` : FunctionNodeMatrixMultiply

### nd

nd.multiply_matrices.(cls, matrix: Matrix = None, matrix_1: Matrix = None)

### class Matrix

```python
Matrix.multiply(self, matrix: Matrix = None)
```

## Named Attribute

> `bl_idname` : GeometryNodeInputNamedAttribute

### nd

nd.named_attribute.(cls,
                    name: String = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Float

```python
Float.Named(cls, name: String = None)
```

```python
Float.NamedAttribute(cls, name: String = None)
```

### class Integer

```python
Integer.Named(cls, name: String = None)
```

```python
Integer.NamedAttribute(cls, name: String = None)
```

### class Boolean

```python
Boolean.Named(cls, name: String = None)
```

```python
Boolean.NamedAttribute(cls, name: String = None)
```

### class Vector

```python
Vector.Named(cls, name: String = None)
```

```python
Vector.NamedAttribute(cls, name: String = None)
```

### class Color

```python
Color.Named(cls, name: String = None)
```

```python
Color.NamedAttribute(cls, name: String = None)
```

### class Rotation

```python
Rotation.Named(cls, name: String = None)
```

```python
Rotation.NamedAttribute(cls, name: String = None)
```

### class Matrix

```python
Matrix.Named(cls, name: String = None)
```

```python
Matrix.NamedAttribute(cls, name: String = None)
```

## Named Layer Selection

> `bl_idname` : GeometryNodeInputNamedLayerSelection

### nd

nd.named_layer_selection.(cls, name: String = None)

### class GreasePencil

```python
GreasePencil.named_layer_selection(cls, name: String = None)
```

### class Layer

```python
Layer.named_selection(cls, name: String = None)
```

## Noise Texture

> `bl_idname` : ShaderNodeTexNoise

### nd

nd.noise_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    offset: Float = None,
                    gain: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True)

### snd

nd.noise_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    offset: Float = None,
                    gain: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True)

### class Float

```python
Float.Noise(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True)
```

### class Texture

```python
Texture.Noise(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    distortion: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D',
                    noise_type: Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM',
                    normalize = True)
```

## Normal

> `bl_idname` : ShaderNodeNormal

### snd

nd.normal.(cls, normal: Vector = None)

### class Vector

```python
Vector.normal(self)
```

## Normal Map

> `bl_idname` : ShaderNodeNormalMap

### snd

nd.normal_map.(cls,
                    strength: Float = None,
                    color: Color = None,
                    base: Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED',
                    convention: Literal['OPENGL', 'DIRECTX'] = 'OPENGL',
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = '')

### class Float

```python
Float.normal_map(self,
                    color: Color = None,
                    base: Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED',
                    convention: Literal['OPENGL', 'DIRECTX'] = 'OPENGL',
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = '')
```

## Object

> `bl_idname` : GeometryNodeInputObject

### nd

nd.object.(cls, object = None)

## Object Info

> `bl_idname` : ShaderNodeObjectInfo

### snd

nd.object_info.(cls)

## Offset Corner in Face

> `bl_idname` : GeometryNodeOffsetCornerInFace

### nd

nd.offset_corner_in_face.(cls, corner_index: Integer = None, offset: Integer = None)

### class Mesh

```python
Mesh.offset_corner_in_face(cls, corner_index: Integer = None, offset: Integer = None)
```

### class Corner

```python
Corner.offset_in_face(cls, corner_index: Integer = None, offset: Integer = None)
```

## Offset Point in Curve

> `bl_idname` : GeometryNodeOffsetPointInCurve

### nd

nd.offset_point_in_curve.(cls, point_index: Integer = None, offset: Integer = None)

### class Curve

```python
Curve.offset_point_in_curve(cls, point_index: Integer = None, offset: Integer = None)
```

### class SplinePoint

```python
SplinePoint.offset_in_curve(cls, point_index: Integer = None, offset: Integer = None)
```

## Pack UV Islands

> `bl_idname` : GeometryNodeUVPackIslands

### nd

nd.pack_uv_islands.(cls,
                    uv: Vector = None,
                    selection: Boolean = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None)

### class Vector

```python
Vector.pack_uv_islands(self,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None)
```

### class Corner

```python
Corner.pack_uv_islands(cls,
                    uv: Vector = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None)
```

## Particle Info

> `bl_idname` : ShaderNodeParticleInfo

### snd

nd.particle_info.(cls)

## Point Info

> `bl_idname` : ShaderNodePointInfo

### snd

nd.point_info.(cls)

## Points

> `bl_idname` : GeometryNodePoints

### nd

nd.points.(cls, count: Integer = None, position: Vector = None, radius: Float = None)

### class Cloud

```python
Cloud.Points(cls, count: Integer = None, position: Vector = None, radius: Float = None)
```

## Points of Curve

> `bl_idname` : GeometryNodePointsOfCurve

### nd

nd.points_of_curve.(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Curve

```python
Curve.points_of_curve(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Spline

```python
Spline.points_of_curve(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Spline.point_index(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
Spline.points_total(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Points to Curves

> `bl_idname` : GeometryNodePointsToCurves

### nd

nd.points_to_curves.(cls,
                    points: Cloud = None,
                    curve_group_id: Integer = None,
                    weight: Float = None)

### class Cloud

```python
Cloud.to_curves(self, curve_group_id: Integer = None, weight: Float = None)
```

## Points to SDF Grid

> `bl_idname` : GeometryNodePointsToSDFGrid

### nd

nd.points_to_sdf_grid.(cls, points: Cloud = None, radius: Float = None, voxel_size: Float = None)

### class Cloud

```python
Cloud.to_sdf_grid(self, radius: Float = None, voxel_size: Float = None)
```

## Points to Vertices

> `bl_idname` : GeometryNodePointsToVertices

### nd

nd.points_to_vertices.(cls, points: Cloud = None, selection: Boolean = None)

### class Cloud

```python
Cloud.to_vertices(self)
```

## Points to Volume

> `bl_idname` : GeometryNodePointsToVolume

### nd

nd.points_to_volume.(cls,
                    points: Cloud = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None)

### class Cloud

```python
Cloud.to_volume(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None)
```

## Position

> `bl_idname` : GeometryNodeInputPosition

### nd

nd.position.(self)

### class Geometry

```python
prop = Geometry.position
```

### class Point

```python
prop = Point.position
```

## Principled BSDF

> `bl_idname` : ShaderNodeBsdfPrincipled

### snd

nd.principled_bsdf.(cls,
                    base_color: Color = None,
                    metallic: Float = None,
                    roughness: Float = None,
                    ior: Float = None,
                    alpha: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    diffuse_roughness: Float = None,
                    subsurface_weight: Float = None,
                    subsurface_radius: Vector = None,
                    subsurface_scale: Float = None,
                    subsurface_ior: Float = None,
                    subsurface_anisotropy: Float = None,
                    specular_ior_level: Float = None,
                    specular_tint: Color = None,
                    anisotropic: Float = None,
                    anisotropic_rotation: Float = None,
                    tangent: Vector = None,
                    transmission_weight: Float = None,
                    coat_weight: Float = None,
                    coat_roughness: Float = None,
                    coat_ior: Float = None,
                    coat_tint: Color = None,
                    coat_normal: Vector = None,
                    sheen_weight: Float = None,
                    sheen_roughness: Float = None,
                    sheen_tint: Color = None,
                    emission_color: Color = None,
                    emission_strength: Float = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    subsurface_method: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK')

### class Shader

```python
Shader.Principled(cls,
                    base_color: Color = None,
                    metallic: Float = None,
                    roughness: Float = None,
                    ior: Float = None,
                    alpha: Float = None,
                    normal: Vector = None,
                    diffuse_roughness: Float = None,
                    subsurface_weight: Float = None,
                    subsurface_radius: Vector = None,
                    subsurface_scale: Float = None,
                    subsurface_anisotropy: Float = None,
                    specular_ior_level: Float = None,
                    specular_tint: Color = None,
                    anisotropic: Float = None,
                    anisotropic_rotation: Float = None,
                    tangent: Vector = None,
                    transmission_weight: Float = None,
                    coat_weight: Float = None,
                    coat_roughness: Float = None,
                    coat_ior: Float = None,
                    coat_tint: Color = None,
                    coat_normal: Vector = None,
                    sheen_weight: Float = None,
                    sheen_roughness: Float = None,
                    sheen_tint: Color = None,
                    emission_color: Color = None,
                    emission_strength: Float = None,
                    thin_film_thickness: Float = None,
                    thin_film_ior: Float = None,
                    distribution: Literal['GGX', 'MULTI_GGX'] = 'MULTI_GGX',
                    subsurface_method: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK')
```

## Principled Hair BSDF

> `bl_idname` : ShaderNodeBsdfHairPrincipled

### snd

nd.principled_hair_bsdf.(cls,
                    color: Color = None,
                    melanin: Float = None,
                    melanin_redness: Float = None,
                    tint: Color = None,
                    absorption_coefficient: Vector = None,
                    aspect_ratio: Float = None,
                    roughness: Float = None,
                    radial_roughness: Float = None,
                    coat: Float = None,
                    ior: Float = None,
                    offset: Float = None,
                    random_color: Float = None,
                    random_roughness: Float = None,
                    random: Float = None,
                    weight: Float = None,
                    reflection: Float = None,
                    transmission: Float = None,
                    secondary_reflection: Float = None,
                    model: Literal['CHIANG', 'HUANG'] = 'CHIANG',
                    parametrization: Literal['ABSORPTION', 'MELANIN', 'COLOR'] = 'COLOR')

### class Shader

```python
Shader.PrincipledHair(cls,
                    color: Color = None,
                    roughness: Float = None,
                    radial_roughness: Float = None,
                    coat: Float = None,
                    ior: Float = None,
                    offset: Float = None,
                    random_roughness: Float = None,
                    random: Float = None,
                    model: Literal['CHIANG', 'HUANG'] = 'CHIANG',
                    parametrization: Literal['ABSORPTION', 'MELANIN', 'COLOR'] = 'COLOR')
```

## Principled Volume

> `bl_idname` : ShaderNodeVolumePrincipled

### snd

nd.principled_volume.(cls,
                    color: Color = None,
                    color_attribute: String = None,
                    density: Float = None,
                    density_attribute: String = None,
                    anisotropy: Float = None,
                    absorption_color: Color = None,
                    emission_strength: Float = None,
                    emission_color: Color = None,
                    blackbody_intensity: Float = None,
                    blackbody_tint: Color = None,
                    temperature: Float = None,
                    temperature_attribute: String = None,
                    weight: Float = None)

### class VolumeShader

```python
VolumeShader.Principled(cls,
                    color: Color = None,
                    color_attribute: String = None,
                    density: Float = None,
                    density_attribute: String = None,
                    anisotropy: Float = None,
                    absorption_color: Color = None,
                    emission_strength: Float = None,
                    emission_color: Color = None,
                    blackbody_intensity: Float = None,
                    blackbody_tint: Color = None,
                    temperature: Float = None,
                    temperature_attribute: String = None)
```

## Project Point

> `bl_idname` : FunctionNodeProjectPoint

### nd

nd.project_point.(cls, vector: Vector = None, transform: Matrix = None)

### class Matrix

```python
Matrix.project_point(self, vector: Vector = None)
```

## Prune Grid

> `bl_idname` : GeometryNodeGridPrune

### nd

nd.prune_grid.(cls,
                    grid: Float = None,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None)
```

### class Integer

```python
Integer.prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Integer = None)
```

### class Boolean

```python
Boolean.prune_grid(self, mode: Literal['Inactive', 'Threshold', 'SDF'] = None)
```

### class Vector

```python
Vector.prune_grid(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Vector = None)
```

## Quadratic Bézier

> `bl_idname` : GeometryNodeCurveQuadraticBezier

### nd

nd.quadratic_bezier.(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None)

### class Curve

```python
Curve.QuadraticBezier(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None)
```

## Quadrilateral

> `bl_idname` : GeometryNodeCurvePrimitiveQuadrilateral

### nd

nd.quadrilateral.(cls,
                    width: Float = None,
                    height: Float = None,
                    bottom_width: Float = None,
                    top_width: Float = None,
                    offset: Float = None,
                    bottom_height: Float = None,
                    top_height: Float = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    point_4: Vector = None,
                    mode: Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE')

### class Curve

```python
Curve.QuadrilateralRectangle(cls, width: Float = None, height: Float = None)
```

```python
Curve.QuadrilateralParallelogram(cls, width: Float = None, height: Float = None, offset: Float = None)
```

```python
Curve.QuadrilateralTrapezoid(cls,
                    height: Float = None,
                    bottom_width: Float = None,
                    top_width: Float = None,
                    offset: Float = None)
```

```python
Curve.QuadrilateralKite(cls,
                    width: Float = None,
                    bottom_height: Float = None,
                    top_height: Float = None)
```

```python
Curve.QuadrilateralPoints(cls,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    point_4: Vector = None)
```

```python
Curve.Quadrilateral(cls,
                    width: Float = None,
                    height: Float = None,
                    mode: Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE')
```

## Quaternion to Rotation

> `bl_idname` : FunctionNodeQuaternionToRotation

### nd

nd.quaternion_to_rotation.(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None)

### class Rotation

```python
Rotation.FromQuaternion(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None)
```

## RGB Curves

> `bl_idname` : ShaderNodeRGBCurve

### nd

nd.rgb_curves.(cls, color: Color = None, factor: Float = None)

### snd

nd.rgb_curves.(cls, color: Color = None, factor: Float = None)

## RGB to BW

> `bl_idname` : ShaderNodeRGBToBW

### snd

nd.rgb_to_bw.(cls, color: Color = None)

### class Color

```python
Color.rgb_to_bw(self)
```

## Radial Tiling

> `bl_idname` : ShaderNodeRadialTiling

### nd

nd.radial_tiling.(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False)

### snd

nd.radial_tiling.(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False)

### class Vector

```python
Vector.radial_tiling(self, sides: Float = None, roundness: Float = None, normalize = False)
```

## Radius

> `bl_idname` : GeometryNodeInputRadius

### nd

nd.radius.(self)

### class Cloud

```python
prop = Cloud.radius
```

### class CloudPoint

```python
prop = CloudPoint.radius
```

### class Curve

```python
prop = Curve.radius
```

### class SplinePoint

```python
prop = SplinePoint.radius
```

## Random Value

> `bl_idname` : FunctionNodeRandomValue

### nd

nd.random_value.(cls,
                    min: Vector = None,
                    max: Vector = None,
                    min_1: Float = None,
                    max_1: Float = None,
                    min_2: Integer = None,
                    max_2: Integer = None,
                    probability: Float = None,
                    id: Integer = None,
                    seed: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR'] = 'FLOAT')

### class Float

```python
Float.Random(cls,
                    min: Float = None,
                    max: Float = None,
                    id: Integer = None,
                    seed: Integer = None)
```

### class Integer

```python
Integer.Random(cls,
                    min: Integer = None,
                    max: Integer = None,
                    id: Integer = None,
                    seed: Integer = None)
```

### class Boolean

```python
Boolean.Random(cls, probability: Float = None, id: Integer = None, seed: Integer = None)
```

### class Vector

```python
Vector.Random(cls,
                    min: Vector = None,
                    max: Vector = None,
                    id: Integer = None,
                    seed: Integer = None)
```

## Ray Portal BSDF

> `bl_idname` : ShaderNodeBsdfRayPortal

### snd

nd.ray_portal_bsdf.(cls,
                    color: Color = None,
                    position: Vector = None,
                    direction: Vector = None,
                    weight: Float = None)

### class Shader

```python
Shader.RayPortal(cls, color: Color = None, position: Vector = None, direction: Vector = None)
```

## Raycast

> `bl_idname` : ShaderNodeRaycast

### snd

nd.raycast.(cls,
                    position: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    only_local = False)

### class Vector

```python
Vector.raycast(self, direction: Vector = None, length: Float = None, only_local = False)
```

## Realize Instances

> `bl_idname` : GeometryNodeRealizeInstances

### nd

nd.realize_instances.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    realize_all: Boolean = None,
                    depth: Integer = None,
                    realize_to_point_domain = False)

### class Geometry

```python
Geometry.realize(self,
                    realize_all: Boolean = None,
                    depth: Integer = None,
                    realize_to_point_domain = False)
```

## Refraction BSDF

> `bl_idname` : ShaderNodeBsdfRefraction

### snd

nd.refraction_bsdf.(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    distribution: Literal['BECKMANN', 'GGX'] = 'BECKMANN')

### class Shader

```python
Shader.Refraction(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    distribution: Literal['BECKMANN', 'GGX'] = 'BECKMANN')
```

## Remove Named Attribute

> `bl_idname` : GeometryNodeRemoveAttribute

### nd

nd.remove_named_attribute.(cls,
                    geometry: Geometry = None,
                    pattern_mode: Literal['Exact', 'Wildcard'] = None,
                    name: String = None)

### class Geometry

```python
Geometry.remove_named_attribute(self, pattern_mode: Literal['Exact', 'Wildcard'] = None, name: String = None)
```

## Repeat Input

> `bl_idname` : GeometryNodeRepeatInput

### class Repeat

## Repeat Output

> `bl_idname` : GeometryNodeRepeatOutput

### class Repeat

## Replace Material

> `bl_idname` : GeometryNodeReplaceMaterial

### nd

nd.replace_material.(cls, geometry: Geometry = None, old: Material = None, new: Material = None)

### class Geometry

```python
Geometry.replace_material(self, old: Material = None, new: Material = None)
```

## Replace String

> `bl_idname` : FunctionNodeReplaceString

### nd

nd.replace_string.(cls, string: String = None, find: String = None, replace: String = None)

### class String

```python
String.replace(self, find: String = None, replace: String = None)
```

## Reroute

> `bl_idname` : NodeReroute

### nd

nd.reroute.(cls, input: Color = None, socket_idname = 'NodeSocketColor')

### snd

nd.reroute.(cls, input: Color = None, socket_idname = 'NodeSocketColor')

## Resample Curve

> `bl_idname` : GeometryNodeResampleCurve

### nd

nd.resample_curve.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True)

### class Curve

```python
Curve.resample(self,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True)
```

## Reverse Curve

> `bl_idname` : GeometryNodeReverseCurve

### nd

nd.reverse_curve.(cls, curve: Curve = None, selection: Boolean = None)

### class Curve

```python
Curve.reverse(self)
```

## Rotate Instances

> `bl_idname` : GeometryNodeRotateInstances

### nd

nd.rotate_instances.(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
Instances.rotate(self,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None)
```

## Rotate Rotation

> `bl_idname` : FunctionNodeRotateRotation

### nd

nd.rotate_rotation.(cls,
                    rotation: Rotation = None,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL')

### class Rotation

```python
Rotation.rotate(self,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL')
```

```python
Rotation.rotate_global(self, rotate_by: Rotation = None)
```

```python
Rotation.rotate_local(self, rotate_by: Rotation = None)
```

## Rotate Vector

> `bl_idname` : FunctionNodeRotateVector

### nd

nd.rotate_vector.(cls, vector: Vector = None, rotation: Rotation = None)

### class Rotation

```python
Rotation.rotate_vector(self, vector: Vector = None)
```

## Rotation

> `bl_idname` : FunctionNodeInputRotation

### nd

nd.rotation.(self)

## Rotation to Axis Angle

> `bl_idname` : FunctionNodeRotationToAxisAngle

### nd

nd.rotation_to_axis_angle.(cls, rotation: Rotation = None)

### class Rotation

```python
Rotation.to_axis_angle(self)
```

```python
prop = Rotation.axis_angle
```

## Rotation to Euler

> `bl_idname` : FunctionNodeRotationToEuler

### nd

nd.rotation_to_euler.(cls, rotation: Rotation = None)

### class Rotation

```python
Rotation.to_euler(self)
```

## Rotation to Quaternion

> `bl_idname` : FunctionNodeRotationToQuaternion

### nd

nd.rotation_to_quaternion.(cls, rotation: Rotation = None)

### class Rotation

```python
Rotation.to_quaternion(self)
```

```python
prop = Rotation.wxyz
```

## SDF Grid Boolean

> `bl_idname` : GeometryNodeSDFGridBoolean

### nd

nd.sdf_grid_boolean.(cls,
                    *grid_2: Float,
                    grid_1: Float = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE')

### class Float

```python
Float.sdf_grid_boolean(self,
                    *grid_2: Float,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE')
```

```python
Float.sdf_intersect(self, *grid: Float)
```

```python
Float.sdf_union(self, *grid: Float)
```

```python
Float.sdf_difference(self, *grid_2: Float)
```

## SDF Grid Fillet

> `bl_idname` : GeometryNodeSDFGridFillet

### nd

nd.sdf_grid_fillet.(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
Float.sdf_grid_fillet(self, iterations: Integer = None)
```

## SDF Grid Laplacian

> `bl_idname` : GeometryNodeSDFGridLaplacian

### nd

nd.sdf_grid_laplacian.(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
Float.sdf_grid_laplacian(self, iterations: Integer = None)
```

## SDF Grid Mean

> `bl_idname` : GeometryNodeSDFGridMean

### nd

nd.sdf_grid_mean.(cls, grid: Float = None, width: Integer = None, iterations: Integer = None)

### class Float

```python
Float.sdf_grid_mean(self, width: Integer = None, iterations: Integer = None)
```

## SDF Grid Mean Curvature

> `bl_idname` : GeometryNodeSDFGridMeanCurvature

### nd

nd.sdf_grid_mean_curvature.(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
Float.sdf_grid_mean_curvature(self, iterations: Integer = None)
```

## SDF Grid Median

> `bl_idname` : GeometryNodeSDFGridMedian

### nd

nd.sdf_grid_median.(cls, grid: Float = None, width: Integer = None, iterations: Integer = None)

### class Float

```python
Float.sdf_grid_median(self, width: Integer = None, iterations: Integer = None)
```

## SDF Grid Offset

> `bl_idname` : GeometryNodeSDFGridOffset

### nd

nd.sdf_grid_offset.(cls, grid: Float = None, distance: Float = None)

### class Float

```python
Float.sdf_grid_offset(self, distance: Float = None)
```

## Sample Curve

> `bl_idname` : GeometryNodeSampleCurve

### nd

nd.sample_curve.(cls,
                    curves: Curve = None,
                    value: Float = None,
                    length: Float = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR',
                    use_all_curves = False)

### class Curve

```python
Curve.sample_factor(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    use_all_curves = False)
```

```python
Curve.sample_length(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    length: Float = None,
                    curve_index: Integer = None,
                    use_all_curves = False)
```

```python
Curve.sample(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR',
                    use_all_curves = False)
```

## Sample Grid

> `bl_idname` : GeometryNodeSampleGrid

### nd

nd.sample_grid.(cls,
                    grid: Float = None,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Integer

```python
Integer.sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Boolean

```python
Boolean.sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Vector

```python
Vector.sample_grid(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

## Sample Grid Index

> `bl_idname` : GeometryNodeSampleGridIndex

### nd

nd.sample_grid_index.(cls,
                    grid: Float = None,
                    x: Integer = None,
                    y: Integer = None,
                    z: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Integer

```python
Integer.sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Boolean

```python
Boolean.sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Vector

```python
Vector.sample_grid_index(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

## Sample Index

> `bl_idname` : GeometryNodeSampleIndex

### nd

nd.sample_index.(cls,
                    geometry: Geometry = None,
                    value: Float = None,
                    index: Integer = None,
                    clamp = False,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Edge

```python
Edge.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Face

```python
Face.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Corner

```python
Corner.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Spline

```python
Spline.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Instance

```python
Instance.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Layer

```python
Layer.sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

## Sample Nearest

> `bl_idname` : GeometryNodeSampleNearest

### nd

nd.sample_nearest.(cls,
                    geometry: Geometry = None,
                    sample_position: Vector = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER'] = 'POINT')

### class Point

```python
Point.sample_nearest(self, sample_position: Vector = None)
```

### class Edge

```python
Edge.sample_nearest(self, sample_position: Vector = None)
```

### class Face

```python
Face.sample_nearest(self, sample_position: Vector = None)
```

### class Corner

```python
Corner.sample_nearest(self, sample_position: Vector = None)
```

## Sample Nearest Surface

> `bl_idname` : GeometryNodeSampleNearestSurface

### nd

nd.sample_nearest_surface.(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Mesh

```python
Mesh.sample_nearest_surface(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

## Sample UV Surface

> `bl_idname` : GeometryNodeSampleUVSurface

### nd

nd.sample_uv_surface.(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Mesh

```python
Mesh.sample_uv_surface(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None)
```

## Scale Elements

> `bl_idname` : GeometryNodeScaleElements

### nd

nd.scale_elements.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None,
                    domain: Literal['FACE', 'EDGE'] = 'FACE')

### class Face

```python
Face.scale(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None)
```

### class Edge

```python
Edge.scale(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None)
```

## Scale Instances

> `bl_idname` : GeometryNodeScaleInstances

### nd

nd.scale_instances.(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    scale: Vector = None,
                    center: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
Instances.scale(self, scale: Vector = None, center: Vector = None, local_space: Boolean = None)
```

## Scene Time

> `bl_idname` : GeometryNodeInputSceneTime

### nd

nd.scene_time.(cls)

### class Float

```python
prop = Float.scene_time
```

```python
prop = Float.seconds
```

```python
prop = Float.frame
```

## Script

> `bl_idname` : ShaderNodeScript

### snd

nd.script.(cls,
                    bytecode = '',
                    bytecode_hash = '',
                    filepath = '',
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL',
                    script = None,
                    use_auto_update = False)

## Selection

> `bl_idname` : GeometryNodeToolSelection

### nd

nd.selection.(cls)

## Self Object

> `bl_idname` : GeometryNodeSelfObject

### nd

nd.self_object.(self)

### class Object

```python
Object.Self(cls)
```

## Separate Bundle

> `bl_idname` : NodeSeparateBundle

### nd

nd.separate_bundle.(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets)

### snd

nd.separate_bundle.(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets)

### class Bundle

```python
Bundle.separate_bundle(self, named_sockets: dict = {}, define_signature = False, **sockets)
```

## Separate Color

> `bl_idname` : ShaderNodeSeparateColor

### snd

nd.separate_color.(cls, color: Color = None, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')

### class Color

```python
Color.separate_col_RGB(self)
```

```python
Color.separate_col_HSV(self)
```

```python
Color.separate_col_HSL(self)
```

```python
Color.separate_col(self, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')
```

## Separate Components

> `bl_idname` : GeometryNodeSeparateComponents

### nd

nd.separate_components.(cls, geometry: Geometry = None)

### class Geometry

```python
Geometry.separate_components(self)
```

```python
prop = Geometry.mesh
```

```python
prop = Geometry.curve
```

```python
prop = Geometry.grease_pencil
```

```python
prop = Geometry.point_cloud
```

```python
prop = Geometry.volume
```

```python
prop = Geometry.instances
```

## Separate Geometry

> `bl_idname` : GeometryNodeSeparateGeometry

### nd

nd.separate_geometry.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.separate(self)
```

### class Edge

```python
Edge.separate(self)
```

### class Face

```python
Face.separate(self)
```

### class Spline

```python
Spline.separate(self)
```

### class Instance

```python
Instance.separate(self)
```

### class Layer

```python
Layer.separate(self)
```

## Separate Matrix

> `bl_idname` : FunctionNodeSeparateMatrix

### nd

nd.separate_matrix.(cls, matrix: Matrix = None)

### class Matrix

```python
prop = Matrix.as_tuple
```

```python
Matrix.separate(self)
```

```python
Matrix.separate_matrix(self)
```

```python
prop = Matrix.column_1_row_1
```

```python
prop = Matrix.column_1_row_2
```

```python
prop = Matrix.column_1_row_3
```

```python
prop = Matrix.column_1_row_4
```

```python
prop = Matrix.column_2_row_1
```

```python
prop = Matrix.column_2_row_2
```

```python
prop = Matrix.column_2_row_3
```

```python
prop = Matrix.column_2_row_4
```

```python
prop = Matrix.column_3_row_1
```

```python
prop = Matrix.column_3_row_2
```

```python
prop = Matrix.column_3_row_3
```

```python
prop = Matrix.column_3_row_4
```

```python
prop = Matrix.column_4_row_1
```

```python
prop = Matrix.column_4_row_2
```

```python
prop = Matrix.column_4_row_3
```

```python
prop = Matrix.column_4_row_4
```

## Separate Transform

> `bl_idname` : FunctionNodeSeparateTransform

### nd

nd.separate_transform.(cls, transform: Matrix = None)

### class Matrix

```python
prop = Matrix.trs
```

```python
Matrix.separate_transform(self)
```

```python
prop = Matrix.translation
```

```python
prop = Matrix.rotation
```

```python
prop = Matrix.scale
```

## Separate XYZ

> `bl_idname` : ShaderNodeSeparateXYZ

### nd

nd.separate_xyz.(cls, vector: Vector = None)

### snd

nd.separate_xyz.(cls, vector: Vector = None)

### class Vector

```python
prop = Vector.xyz
```

```python
Vector.separate_xyz(self)
```

```python
prop = Vector.x
```

```python
prop = Vector.y
```

```python
prop = Vector.z
```

## Set Curve Normal

> `bl_idname` : GeometryNodeSetCurveNormal

### nd

nd.set_curve_normal.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None)

### class Curve

```python
Curve.set_normal(self,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None)
```

```python
Curve.normal = value
```

### class Spline

```python
Spline.normal = value
```

## Set Curve Radius

> `bl_idname` : GeometryNodeSetCurveRadius

### nd

nd.set_curve_radius.(cls, curve: Curve = None, selection: Boolean = None, radius: Float = None)

### class Curve

```python
Curve.set_radius(self, radius: Float = None)
```

```python
Curve.radius = value
```

### class SplinePoint

```python
SplinePoint.radius = value
```

## Set Curve Tilt

> `bl_idname` : GeometryNodeSetCurveTilt

### nd

nd.set_curve_tilt.(cls, curve: Curve = None, selection: Boolean = None, tilt: Float = None)

### class Curve

```python
Curve.set_tilt(self, tilt: Float = None)
```

```python
Curve.tilt = value
```

### class Spline

```python
Spline.tilt = value
```

## Set Face Set

> `bl_idname` : GeometryNodeToolSetFaceSet

### nd

nd.set_face_set.(cls, mesh: Mesh = None, selection: Boolean = None, face_set: Integer = None)

### class Mesh

```python
Mesh.set_face_set(self, face_set: Integer = None)
```

## Set Geometry Bundle

> `bl_idname` : GeometryNodeSetGeometryBundle

### nd

nd.set_geometry_bundle.(cls, geometry: Geometry = None, bundle: Bundle = None)

## Set Geometry Name

> `bl_idname` : GeometryNodeSetGeometryName

### nd

nd.set_geometry_name.(cls, geometry: Geometry = None, name: String = None)

### class Geometry

```python
Geometry.set_name(self, name: String = None)
```

```python
Geometry.name = value
```

## Set Grease Pencil Color

> `bl_idname` : GeometryNodeSetGreasePencilColor

### nd

nd.set_grease_pencil_color.(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE')

### class GreasePencil

```python
GreasePencil.set_color_stroke(self, color: Color = None, opacity: Float = None)
```

```python
GreasePencil.set_color_fill(self, color: Color = None, opacity: Float = None)
```

```python
GreasePencil.set_color(self,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE')
```

```python
GreasePencil.stroke_color = value
```

```python
GreasePencil.fill_color = value
```

## Set Grease Pencil Depth

> `bl_idname` : GeometryNodeSetGreasePencilDepth

### nd

nd.set_grease_pencil_depth.(cls,
                    grease_pencil: GreasePencil = None,
                    depth_order: Literal['2D', '3D'] = '2D')

### class GreasePencil

```python
GreasePencil.set_depth(self, depth_order: Literal['2D', '3D'] = '2D')
```

```python
GreasePencil.depth = value
```

## Set Grease Pencil Softness

> `bl_idname` : GeometryNodeSetGreasePencilSoftness

### nd

nd.set_grease_pencil_softness.(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    softness: Float = None)

### class GreasePencil

```python
GreasePencil.set_softness(self, softness: Float = None)
```

```python
GreasePencil.softness = value
```

## Set Grid Background

> `bl_idname` : GeometryNodeSetGridBackground

### nd

nd.set_grid_background.(cls,
                    grid: Float = None,
                    background: Float = None,
                    update_inactive: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.set_grid_background(self, background: Float = None, update_inactive: Boolean = None)
```

### class Integer

```python
Integer.set_grid_background(self, background: Integer = None, update_inactive: Boolean = None)
```

### class Boolean

```python
Boolean.set_grid_background(self, background: Boolean = None, update_inactive: Boolean = None)
```

### class Vector

```python
Vector.set_grid_background(self, background: Vector = None, update_inactive: Boolean = None)
```

## Set Grid Transform

> `bl_idname` : GeometryNodeSetGridTransform

### nd

nd.set_grid_transform.(cls,
                    grid: Float = None,
                    transform: Matrix = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.set_grid_transform(self, transform: Matrix = None)
```

### class Integer

```python
Integer.set_grid_transform(self, transform: Matrix = None)
```

### class Boolean

```python
Boolean.set_grid_transform(self, transform: Matrix = None)
```

### class Vector

```python
Vector.set_grid_transform(self, transform: Matrix = None)
```

## Set Handle Positions

> `bl_idname` : GeometryNodeSetCurveHandlePositions

### nd

nd.set_handle_positions.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT')

### class Curve

```python
Curve.set_handle_positions(self,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT')
```

```python
Curve.set_left_handle_positions(self, position: Vector = None, offset: Vector = None)
```

```python
Curve.set_right_handle_positions(self, position: Vector = None, offset: Vector = None)
```

```python
Curve.left_handle_position = value
```

```python
Curve.right_handle_position = value
```

```python
Curve.left_handle_offset = value
```

```python
Curve.right_handle_offset = value
```

## Set Handle Type

> `bl_idname` : GeometryNodeCurveSetHandles

### nd

nd.set_handle_type.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})

### class Curve

```python
Curve.set_handle_type(self,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})
```

```python
Curve.set_left_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
Curve.set_right_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
Curve.set_both_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
Curve.handle_type = value
```

```python
Curve.left_handle_type = value
```

```python
Curve.right_handle_type = value
```

## Set ID

> `bl_idname` : GeometryNodeSetID

### nd

nd.set_id.(cls, geometry: Geometry = None, selection: Boolean = None, id: Integer = None)

### class Geometry

```python
Geometry.set_id(self, id: Integer = None)
```

```python
Geometry.id = value
```

## Set Instance Transform

> `bl_idname` : GeometryNodeSetInstanceTransform

### nd

nd.set_instance_transform.(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    transform: Matrix = None)

### class Instances

```python
Instances.set_transform(self, transform: Matrix = None)
```

```python
Instances.transform = value
```

## Set Material

> `bl_idname` : GeometryNodeSetMaterial

### nd

nd.set_material.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material: Material = None)

### class Geometry

```python
Geometry.set_material(self, material: Material = None)
```

```python
Geometry.material = value
```

### class Face

```python
Face.material = value
```

### class Edge

```python
Edge.material = value
```

## Set Material Index

> `bl_idname` : GeometryNodeSetMaterialIndex

### nd

nd.set_material_index.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material_index: Integer = None)

### class Geometry

```python
Geometry.set_material_index(self, material_index: Integer = None)
```

```python
Geometry.material_index = value
```

### class Face

```python
Face.material_index = value
```

### class Spline

```python
Spline.material_index = value
```

## Set Mesh Normal

> `bl_idname` : GeometryNodeSetMeshNormal

### nd

nd.set_mesh_normal.(cls,
                    mesh: Mesh = None,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS')

### class Mesh

```python
Mesh.set_normal_sharpness(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
Mesh.set_normal_free(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
Mesh.set_normal_tangent_space(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
Mesh.set_normal(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS')
```

```python
Mesh.normal = value
```

### class Point

```python
Point.normal = value
```

### class Face

```python
Face.normal = value
```

### class Corner

```python
Corner.normal = value
```

## Set Point Radius

> `bl_idname` : GeometryNodeSetPointRadius

### nd

nd.set_point_radius.(cls, points: Cloud = None, selection: Boolean = None, radius: Float = None)

### class Point

```python
Point.set_radius(self, radius: Float = None)
```

### class Cloud

```python
Cloud.radius = value
```

### class CloudPoint

```python
CloudPoint.radius = value
```

## Set Position

> `bl_idname` : GeometryNodeSetPosition

### nd

nd.set_position.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None)

### class Geometry

```python
Geometry.set_position(self, position: Vector = None, offset: Vector = None)
```

```python
Geometry.position = value
```

```python
Geometry.offset = value
```

### class Point

```python
Point.position = value
```

```python
Point.offset = value
```

## Set Selection

> `bl_idname` : GeometryNodeToolSetSelection

### nd

nd.set_selection.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE'] = 'POINT',
                    selection_type: Literal['BOOLEAN', 'FLOAT'] = 'BOOLEAN')

### class Point

```python
Point.set_selection(self)
```

### class Edge

```python
Edge.set_selection(self)
```

### class Face

```python
Face.set_selection(self)
```

### class Spline

```python
Spline.set_selection(self)
```

## Set Shade Smooth

> `bl_idname` : GeometryNodeSetShadeSmooth

### nd

nd.set_shade_smooth.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    shade_smooth: Boolean = None,
                    domain: Literal['EDGE', 'FACE'] = 'FACE')

### class Edge

```python
Edge.set_shade_smooth(self, shade_smooth: Boolean = None)
```

```python
Edge.shade_smooth = value
```

```python
Edge.smooth = value
```

### class Face

```python
Face.set_shade_smooth(self, shade_smooth: Boolean = None)
```

```python
Face.shade_smooth = value
```

```python
Face.smooth = value
```

## Set Spline Cyclic

> `bl_idname` : GeometryNodeSetSplineCyclic

### nd

nd.set_spline_cyclic.(cls, curve: Curve = None, selection: Boolean = None, cyclic: Boolean = None)

### class Curve

```python
Curve.set_spline_cyclic(self, cyclic: Boolean = None)
```

```python
Curve.is_cyclic = value
```

### class Spline

```python
Spline.is_cyclic = value
```

## Set Spline Resolution

> `bl_idname` : GeometryNodeSetSplineResolution

### nd

nd.set_spline_resolution.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    resolution: Integer = None)

### class Curve

```python
Curve.set_spline_resolution(self, resolution: Integer = None)
```

```python
Curve.resolution = value
```

### class Spline

```python
Spline.resolution = value
```

## Set Spline Type

> `bl_idname` : GeometryNodeCurveSplineType

### nd

nd.set_spline_type.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY')

### class Curve

```python
Curve.set_spline_type(self, spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY')
```

```python
Curve.type = value
```

### class Spline

```python
Spline.type = value
```

## Shader to RGB

> `bl_idname` : ShaderNodeShaderToRGB

### snd

nd.shader_to_rgb.(cls, shader: Shader = None)

### class Shader

```python
Shader.to_rgb(self)
```

## Sheen BSDF

> `bl_idname` : ShaderNodeBsdfSheen

### snd

nd.sheen_bsdf.(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    distribution: Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER')

### class Shader

```python
Shader.Sheen(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    distribution: Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER')
```

## Shortest Edge Paths

> `bl_idname` : GeometryNodeInputShortestEdgePaths

### nd

nd.shortest_edge_paths.(cls, end_vertex: Boolean = None, edge_cost: Float = None)

### class Mesh

```python
Mesh.shortest_edge_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None)
```

### class Edge

```python
Edge.shortest_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None)
```

## Simulation Input

> `bl_idname` : GeometryNodeSimulationInput

### class Simulation

## Simulation Output

> `bl_idname` : GeometryNodeSimulationOutput

### class Simulation

## Sky Texture

> `bl_idname` : ShaderNodeTexSky

### snd

nd.sky_texture.(cls,
                    vector: Vector = None,
                    aerosol_density = 1.0,
                    air_density = 1.0,
                    altitude = 100.0,
                    ground_albedo = 0.30000001192092896,
                    ozone_density = 1.0,
                    sky_type: Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'] = 'MULTIPLE_SCATTERING',
                    sun_disc = True,
                    sun_elevation = 0.2617993950843811,
                    sun_intensity = 1.0,
                    sun_rotation = 0.0,
                    sun_size = 0.009512044489383698,
                    turbidity = 2.200000047683716)

### class Color

```python
Color.SkyTexture(cls,
                    aerosol_density = 1.0,
                    air_density = 1.0,
                    altitude = 100.0,
                    ground_albedo = 0.30000001192092896,
                    ozone_density = 1.0,
                    sky_type: Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'] = 'MULTIPLE_SCATTERING',
                    sun_disc = True,
                    sun_elevation = 0.2617993950843811,
                    sun_intensity = 1.0,
                    sun_rotation = 0.0,
                    sun_size = 0.009512044489383698,
                    turbidity = 2.200000047683716)
```

## Slice String

> `bl_idname` : FunctionNodeSliceString

### nd

nd.slice_string.(cls, string: String = None, position: Integer = None, length: Integer = None)

### class String

```python
String.slice(self, position: Integer = None, length: Integer = None)
```

## Sort Elements

> `bl_idname` : GeometryNodeSortElements

### nd

nd.sort_elements.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    sort_weight: Float = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'] = 'POINT')

### class Point

```python
Point.sort(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Edge

```python
Edge.sort(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Face

```python
Face.sort(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Spline

```python
Spline.sort(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Instance

```python
Instance.sort(self, group_id: Integer = None, sort_weight: Float = None)
```

## Special Characters

> `bl_idname` : FunctionNodeInputSpecialCharacters

### nd

nd.special_characters.(cls)

### class String

```python
prop = String.special_characters
```

```python
prop = String.line_break
```

```python
prop = String.tab
```

## Specular BSDF

> `bl_idname` : ShaderNodeEeveeSpecular

### snd

nd.specular_bsdf.(cls,
                    base_color: Color = None,
                    specular: Color = None,
                    roughness: Float = None,
                    emissive_color: Color = None,
                    transparency: Float = None,
                    normal: Vector = None,
                    clear_coat: Float = None,
                    clear_coat_roughness: Float = None,
                    clear_coat_normal: Vector = None,
                    weight: Float = None)

### class Shader

```python
Shader.Specular(cls,
                    base_color: Color = None,
                    specular: Color = None,
                    roughness: Float = None,
                    emissive_color: Color = None,
                    transparency: Float = None,
                    normal: Vector = None,
                    clear_coat: Float = None,
                    clear_coat_roughness: Float = None,
                    clear_coat_normal: Vector = None)
```

## Spiral

> `bl_idname` : GeometryNodeCurveSpiral

### nd

nd.spiral.(cls,
                    resolution: Integer = None,
                    rotations: Float = None,
                    start_radius: Float = None,
                    end_radius: Float = None,
                    height: Float = None,
                    reverse: Boolean = None)

### class Curve

```python
Curve.Spiral(cls,
                    resolution: Integer = None,
                    rotations: Float = None,
                    start_radius: Float = None,
                    end_radius: Float = None,
                    height: Float = None,
                    reverse: Boolean = None)
```

## Spline Length

> `bl_idname` : GeometryNodeSplineLength

### nd

nd.spline_length.(cls)

### class Curve

```python
Curve.spline_length(cls)
```

### class Spline

```python
prop = Spline.spline_length
```

```python
prop = Spline.length
```

```python
prop = Spline.point_count
```

## Spline Parameter

> `bl_idname` : GeometryNodeSplineParameter

### nd

nd.spline_parameter.(cls)

### class Curve

```python
Curve.spline_parameter(cls)
```

### class Spline

```python
prop = Spline.parameter
```

```python
prop = Spline.parameter_factor
```

```python
prop = Spline.parameter_length
```

```python
prop = Spline.parameter_index
```

## Spline Resolution

> `bl_idname` : GeometryNodeInputSplineResolution

### nd

nd.spline_resolution.(self)

### class Curve

```python
prop = Curve.resolution
```

### class Spline

```python
prop = Spline.resolution
```

## Split Edges

> `bl_idname` : GeometryNodeSplitEdges

### nd

nd.split_edges.(cls, mesh: Mesh = None, selection: Boolean = None)

### class Mesh

```python
Mesh.split_edges(self)
```

### class Edge

```python
Edge.split(self)
```

## Split to Instances

> `bl_idname` : GeometryNodeSplitToInstances

### nd

nd.split_to_instances.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.split_to_instances(self, group_id: Integer = None)
```

### class Edge

```python
Edge.split_to_instances(self, group_id: Integer = None)
```

### class Face

```python
Face.split_to_instances(self, group_id: Integer = None)
```

### class Spline

```python
Spline.split_to_instances(self, group_id: Integer = None)
```

### class Instance

```python
Instance.split_to_instances(self, group_id: Integer = None)
```

### class Layer

```python
Layer.split_to_instances(self, group_id: Integer = None)
```

## Star

> `bl_idname` : GeometryNodeCurveStar

### nd

nd.star.(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None)

### class Curve

```python
Curve.Star(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None)
```

## Store Bundle Item

> `bl_idname` : NodeStoreBundleItem

### nd

nd.store_bundle_item.(cls,
                    bundle: Bundle = None,
                    path: String = None,
                    item: Float = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

### class Bundle

```python
Bundle.set_item(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

```python
Bundle.store_item(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

## Store Named Attribute

> `bl_idname` : GeometryNodeStoreNamedAttribute

### nd

nd.store_named_attribute.(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    name: String = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'INT8', 'FLOAT2', 'BYTE_COLOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
Point.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Point.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Edge

```python
Edge.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Edge.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Face

```python
Face.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Face.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Corner

```python
Corner.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Corner.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Corner.store_uv(self, name: String = None, value: Vector = None)
```

### class Spline

```python
Spline.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Spline.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Instance

```python
Instance.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Instance.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Layer

```python
Layer.store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
Layer.store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

## Store Named Grid

> `bl_idname` : GeometryNodeStoreNamedGrid

### nd

nd.store_named_grid.(cls,
                    volume: Volume = None,
                    name: String = None,
                    grid: Float = None,
                    data_type: Literal['BOOLEAN', 'FLOAT', 'INT', 'VECTOR_FLOAT'] = 'FLOAT')

### class Volume

```python
Volume.store_named_grid(self, name: String = None, grid: Boolean | Float | Integer | Vector = None)
```

## String

> `bl_idname` : FunctionNodeInputString

### nd

nd.string.(cls, string = '')

## String Length

> `bl_idname` : FunctionNodeStringLength

### nd

nd.string_length.(cls, string: String = None)

### class String

```python
String.length(self)
```

## String to Curves

> `bl_idname` : GeometryNodeStringToCurves

### nd

nd.string_to_curves.(cls,
                    string: String = None,
                    size: Float = None,
                    font: Font = None,
                    align_x: Literal['Left', 'Center', 'Right', 'Justify', 'Flush'] = None,
                    align_y: Literal['Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom'] = None,
                    pivot_point: Literal['Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right'] = None,
                    character_spacing: Float = None,
                    word_spacing: Float = None,
                    line_spacing: Float = None,
                    overflow: Literal['Overflow', 'Scale To Fit', 'Truncate'] = None,
                    text_box_width: Float = None,
                    text_box_height: Float = None)

### class String

```python
String.to_curves(self,
                    size: Float = None,
                    font: Font = None,
                    align_x: Literal['Left', 'Center', 'Right', 'Justify', 'Flush'] = None,
                    align_y: Literal['Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom'] = None,
                    pivot_point: Literal['Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right'] = None,
                    character_spacing: Float = None,
                    word_spacing: Float = None,
                    line_spacing: Float = None,
                    overflow: Literal['Overflow', 'Scale To Fit', 'Truncate'] = None,
                    text_box_width: Float = None,
                    text_box_height: Float = None)
```

## String to Value

> `bl_idname` : FunctionNodeStringToValue

### nd

nd.string_to_value.(cls, string: String = None, data_type: Literal['FLOAT', 'INT'] = 'FLOAT')

### class String

```python
String.to_value(self, data_type: Literal['FLOAT', 'INT'] = 'FLOAT')
```

```python
String.to_float(self)
```

```python
String.to_integer(self)
```

## Subdivide Curve

> `bl_idname` : GeometryNodeSubdivideCurve

### nd

nd.subdivide_curve.(cls, curve: Curve = None, cuts: Integer = None)

### class Curve

```python
Curve.subdivide(self, cuts: Integer = None)
```

## Subdivide Mesh

> `bl_idname` : GeometryNodeSubdivideMesh

### nd

nd.subdivide_mesh.(cls, mesh: Mesh = None, level: Integer = None)

### class Mesh

```python
Mesh.subdivide(self, level: Integer = None)
```

## Subdivision Surface

> `bl_idname` : GeometryNodeSubdivisionSurface

### nd

nd.subdivision_surface.(cls,
                    mesh: Mesh = None,
                    level: Integer = None,
                    edge_crease: Float = None,
                    vertex_crease: Float = None,
                    limit_surface: Boolean = None,
                    uv_smooth: Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All'] = None,
                    boundary_smooth: Literal['Keep Corners', 'All'] = None)

### class Mesh

```python
Mesh.subdivision_surface(self,
                    level: Integer = None,
                    edge_crease: Float = None,
                    vertex_crease: Float = None,
                    limit_surface: Boolean = None,
                    uv_smooth: Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All'] = None,
                    boundary_smooth: Literal['Keep Corners', 'All'] = None)
```

## Subsurface Scattering

> `bl_idname` : ShaderNodeSubsurfaceScattering

### snd

nd.subsurface_scattering.(cls,
                    color: Color = None,
                    scale: Float = None,
                    radius: Vector = None,
                    ior: Float = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    falloff: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK')

### class Shader

```python
Shader.SubsurfaceScattering(cls,
                    color: Color = None,
                    scale: Float = None,
                    radius: Vector = None,
                    ior: Float = None,
                    roughness: Float = None,
                    anisotropy: Float = None,
                    normal: Vector = None,
                    falloff: Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN'] = 'RANDOM_WALK')
```

## Switch

> `bl_idname` : GeometryNodeSwitch

### class Socket

```python
Socket.Switch(condition=None, false=None, true=None)
```

```python
Socket.switch(condition=None, true=None)
```

## Tangent

> `bl_idname` : ShaderNodeTangent

### snd

nd.tangent.(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = '')

### class Vector

```python
Vector.Tangent(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = '')
```

## Texture Coordinate

> `bl_idname` : ShaderNodeTexCoord

### snd

nd.texture_coordinate.(cls, from_instancer = False, object = None)

## Toon BSDF

> `bl_idname` : ShaderNodeBsdfToon

### snd

nd.toon_bsdf.(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    component: Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE')

### class Shader

```python
Shader.Toon(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    component: Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE')
```

## Transform Direction

> `bl_idname` : FunctionNodeTransformDirection

### nd

nd.transform_direction.(cls, direction: Vector = None, transform: Matrix = None)

### class Matrix

```python
Matrix.transform_direction(self, direction: Vector = None)
```

## Transform Geometry

> `bl_idname` : GeometryNodeTransform

### nd

nd.transform_geometry.(cls,
                    geometry: Geometry = None,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None)

### class Geometry

```python
Geometry.transform(self,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None)
```

## Transform Gizmo

> `bl_idname` : GeometryNodeGizmoTransform

### nd

nd.transform_gizmo.(cls,
                    *value: Matrix,
                    position: Vector = None,
                    rotation: Rotation = None,
                    use_rotation_x = True,
                    use_rotation_y = True,
                    use_rotation_z = True,
                    use_scale_x = True,
                    use_scale_y = True,
                    use_scale_z = True,
                    use_translation_x = True,
                    use_translation_y = True,
                    use_translation_z = True)

### class Matrix

```python
Matrix.transform_gizmo(self,
                    *value: Matrix,
                    position: Vector = None,
                    rotation: Rotation = None,
                    use_rotation_x = True,
                    use_rotation_y = True,
                    use_rotation_z = True,
                    use_scale_x = True,
                    use_scale_y = True,
                    use_scale_z = True,
                    use_translation_x = True,
                    use_translation_y = True,
                    use_translation_z = True)
```

## Transform Point

> `bl_idname` : FunctionNodeTransformPoint

### nd

nd.transform_point.(cls, vector: Vector = None, transform: Matrix = None)

### class Matrix

```python
Matrix.transform_point(self, vector: Vector = None)
```

## Translate Instances

> `bl_idname` : GeometryNodeTranslateInstances

### nd

nd.translate_instances.(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    translation: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
Instances.translate(self, translation: Vector = None, local_space: Boolean = None)
```

## Translucent BSDF

> `bl_idname` : ShaderNodeBsdfTranslucent

### snd

nd.translucent_bsdf.(cls, color: Color = None, normal: Vector = None, weight: Float = None)

### class Shader

```python
Shader.Translucent(cls, color: Color = None, normal: Vector = None)
```

## Transparent BSDF

> `bl_idname` : ShaderNodeBsdfTransparent

### snd

nd.transparent_bsdf.(cls, color: Color = None, weight: Float = None)

### class Shader

```python
Shader.Transparent(cls, color: Color = None)
```

## Transpose Matrix

> `bl_idname` : FunctionNodeTransposeMatrix

### nd

nd.transpose_matrix.(cls, matrix: Matrix = None)

### class Matrix

```python
Matrix.transpose(self)
```

## Triangulate

> `bl_idname` : GeometryNodeTriangulate

### nd

nd.triangulate.(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None)

### class Mesh

```python
Mesh.triangulate(self,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None)
```

## Trim Curve

> `bl_idname` : GeometryNodeTrimCurve

### nd

nd.trim_curve.(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    start: Float = None,
                    end: Float = None,
                    start_1: Float = None,
                    end_1: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR')

### class Curve

```python
Curve.trim_factor(self, start: Float = None, end: Float = None)
```

```python
Curve.trim_length(self, start: Float = None, end: Float = None)
```

```python
Curve.trim(self,
                    start: Float = None,
                    end: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR')
```

## UV Along Stroke

> `bl_idname` : ShaderNodeUVAlongStroke

### snd

nd.uv_along_stroke.(cls, use_tips = False)

## UV Map

> `bl_idname` : ShaderNodeUVMap

### snd

nd.uv_map.(cls, from_instancer = False, uv_map = '')

### class Vector

```python
Vector.UvMap(cls, from_instancer = False, uv_map = '')
```

## UV Sphere

> `bl_idname` : GeometryNodeMeshUVSphere

### nd

nd.uv_sphere.(cls, segments: Integer = None, rings: Integer = None, radius: Float = None)

### class Mesh

```python
Mesh.UVSphere(cls, segments: Integer = None, rings: Integer = None, radius: Float = None)
```

## UV Tangent

> `bl_idname` : GeometryNodeUVTangent

### nd

nd.uv_tangent.(cls, method: Literal['Exact', 'Fast'] = None, uv: Vector = None)

### class Vector

```python
Vector.uv_tangent(self, method: Literal['Exact', 'Fast'] = None)
```

## UV Unwrap

> `bl_idname` : GeometryNodeUVUnwrap

### nd

nd.uv_unwrap.(cls,
                    selection: Boolean = None,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None)

### class Boolean

```python
Boolean.uv_unwrap(self,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None)
```

### class Corner

```python
Corner.uv_unwrap(cls,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None)
```

## Value

> `bl_idname` : ShaderNodeValue

### nd

nd.value.(self)

### snd

nd.value.(self)

## Value to String

> `bl_idname` : FunctionNodeValueToString

### nd

nd.value_to_string.(cls,
                    value: Float = None,
                    decimals: Integer = None,
                    data_type: Literal['FLOAT', 'INT'] = 'FLOAT')

### class Float

```python
Float.to_string(self, decimals: Integer = None)
```

### class Integer

```python
Integer.to_string(self)
```

## Vector

> `bl_idname` : FunctionNodeInputVector

### nd

nd.vector.(self)

## Vector Curves

> `bl_idname` : ShaderNodeVectorCurve

### nd

nd.vector_curves.(cls, vector: Vector = None, factor: Float = None)

### snd

nd.vector_curves.(cls, vector: Vector = None, factor: Float = None)

## Vector Displacement

> `bl_idname` : ShaderNodeVectorDisplacement

### snd

nd.vector_displacement.(cls,
                    vector: Color = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT')

### class Color

```python
Color.vector_displacement(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT')
```

## Vector Math

> `bl_idname` : ShaderNodeVectorMath

### nd

nd.vector_math.(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD')

### snd

nd.vector_math.(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD')

### class Vector

```python
Vector.add(self, vector: Vector = None)
```

```python
Vector.subtract(self, vector: Vector = None)
```

```python
Vector.multiply(self, vector: Vector = None)
```

```python
Vector.divide(self, vector: Vector = None)
```

```python
Vector.multiply_add(self, multiplier: Vector = None, addend: Vector = None)
```

```python
Vector.cross(self, vector: Vector = None)
```

```python
Vector.project(self, vector: Vector = None)
```

```python
Vector.reflect(self, vector: Vector = None)
```

```python
Vector.refract(self, vector: Vector = None, ior: Float = None)
```

```python
Vector.faceforward(self, incident: Vector = None, reference: Vector = None)
```

```python
Vector.dot(self, vector: Vector = None)
```

```python
Vector.distance(self, vector: Vector = None)
```

```python
Vector.length(self)
```

```python
Vector.scale(self, scale: Float = None)
```

```python
Vector.normalize(self)
```

```python
Vector.abs(self)
```

```python
Vector.power(self, exponent: Vector = None)
```

```python
Vector.sign(self)
```

```python
Vector.min(self, vector: Vector = None)
```

```python
Vector.max(self, vector: Vector = None)
```

```python
Vector.round(self)
```

```python
Vector.floor(self)
```

```python
Vector.ceil(self)
```

```python
Vector.fraction(self)
```

```python
Vector.modulo(self, vector: Vector = None)
```

```python
Vector.wrap(self, max: Vector = None, min: Vector = None)
```

```python
Vector.snap(self, increment: Vector = None)
```

```python
Vector.sin(self)
```

```python
Vector.cos(self)
```

```python
Vector.tan(self)
```

### class gnmath

```python
gnmath.vadd(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vsubtract(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vmultiply(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vdivide(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vmultiply_add(vector: Vector = None, multiplier: Vector = None, addend: Vector = None)
```

```python
gnmath.cross(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.project(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.reflect(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.refract(vector: Vector = None, vector_1: Vector = None, ior: Float = None)
```

```python
gnmath.faceforward(vector: Vector = None, incident: Vector = None, reference: Vector = None)
```

```python
gnmath.dot(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.distance(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.length(vector: Vector = None)
```

```python
gnmath.scale(vector: Vector = None, scale: Float = None)
```

```python
gnmath.normalize(vector: Vector = None)
```

```python
gnmath.vabs(vector: Vector = None)
```

```python
gnmath.vpower(base: Vector = None, exponent: Vector = None)
```

```python
gnmath.vsign(vector: Vector = None)
```

```python
gnmath.vmin(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vmax(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vround(vector: Vector = None)
```

```python
gnmath.vfloor(vector: Vector = None)
```

```python
gnmath.vceil(vector: Vector = None)
```

```python
gnmath.vfraction(vector: Vector = None)
```

```python
gnmath.vmodulo(vector: Vector = None, vector_1: Vector = None)
```

```python
gnmath.vwrap(vector: Vector = None, max: Vector = None, min: Vector = None)
```

```python
gnmath.vsnap(vector: Vector = None, increment: Vector = None)
```

```python
gnmath.vsin(vector: Vector = None)
```

```python
gnmath.vcos(vector: Vector = None)
```

```python
gnmath.vtan(vector: Vector = None)
```

## Vector Rotate

> `bl_idname` : ShaderNodeVectorRotate

### nd

nd.vector_rotate.(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')

### snd

nd.vector_rotate.(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')

### class Vector

```python
Vector.rotate(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')
```

```python
Vector.rotate_axis_angle(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False)
```

```python
Vector.rotate_x_axis(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
Vector.rotate_y_axis(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
Vector.rotate_z_axis(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
Vector.rotate_euler_xyz(self, center: Vector = None, rotation: Vector = None, invert = False)
```

## Vector Transform

> `bl_idname` : ShaderNodeVectorTransform

### snd

nd.vector_transform.(cls,
                    vector: Vector = None,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR')

### class Vector

```python
Vector.vector_transform(self,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR')
```

## Vertex Neighbors

> `bl_idname` : GeometryNodeInputMeshVertexNeighbors

### nd

nd.vertex_neighbors.(cls)

### class Mesh

```python
prop = Mesh.vertex_neighbors
```

### class Vertex

```python
prop = Vertex.neighbors
```

```python
prop = Vertex.neighbors_vertex_count
```

```python
prop = Vertex.neighbors_face_count
```

## Vertex of Corner

> `bl_idname` : GeometryNodeVertexOfCorner

### nd

nd.vertex_of_corner.(cls, corner_index: Integer = None)

### class Mesh

```python
Mesh.vertex_of_corner(cls, corner_index: Integer = None)
```

### class Corner

```python
Corner.vertex_index(cls, corner_index: Integer = None)
```

## Viewer

> `bl_idname` : GeometryNodeViewer

### nd

nd.viewer.(cls,
                    named_sockets: dict = {},
                    domain: Literal['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'AUTO',
                    ui_shortcut = 0,
                    **sockets)

### class Geometry

```python
Geometry.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Point

```python
Point.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Edge

```python
Edge.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Face

```python
Face.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Corner

```python
Corner.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Spline

```python
Spline.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Instance

```python
Instance.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Layer

```python
Layer.viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

## Viewport Transform

> `bl_idname` : GeometryNodeViewportTransform

### nd

nd.viewport_transform.(cls)

## Volume Absorption

> `bl_idname` : ShaderNodeVolumeAbsorption

### snd

nd.volume_absorption.(cls, color: Color = None, density: Float = None, weight: Float = None)

### class VolumeShader

```python
VolumeShader.Absorption(cls, color: Color = None, density: Float = None)
```

## Volume Coefficients

> `bl_idname` : ShaderNodeVolumeCoefficients

### snd

nd.volume_coefficients.(cls,
                    weight: Float = None,
                    absorption_coefficients: Vector = None,
                    scatter_coefficients: Vector = None,
                    anisotropy: Float = None,
                    ior: Float = None,
                    backscatter: Float = None,
                    alpha: Float = None,
                    diameter: Float = None,
                    emission_coefficients: Vector = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN')

## Volume Cube

> `bl_idname` : GeometryNodeVolumeCube

### nd

nd.volume_cube.(cls,
                    density: Float = None,
                    background: Float = None,
                    min: Vector = None,
                    max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None)

### class Volume

```python
Volume.Cube(cls,
                    density: Float = None,
                    background: Float = None,
                    min: Vector = None,
                    max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None)
```

## Volume Info

> `bl_idname` : ShaderNodeVolumeInfo

### snd

nd.volume_info.(cls)

### class VolumeShader

```python
prop = VolumeShader.info
```

## Volume Scatter

> `bl_idname` : ShaderNodeVolumeScatter

### snd

nd.volume_scatter.(cls,
                    color: Color = None,
                    density: Float = None,
                    anisotropy: Float = None,
                    ior: Float = None,
                    backscatter: Float = None,
                    alpha: Float = None,
                    diameter: Float = None,
                    weight: Float = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN')

### class VolumeShader

```python
VolumeShader.Scatter(cls,
                    color: Color = None,
                    density: Float = None,
                    anisotropy: Float = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN')
```

## Volume to Mesh

> `bl_idname` : GeometryNodeVolumeToMesh

### nd

nd.volume_to_mesh.(cls,
                    volume: Volume = None,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None)

### class Volume

```python
Volume.to_mesh(self,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None)
```

## Voronoi Texture

> `bl_idname` : ShaderNodeTexVoronoi

### nd

nd.voronoi_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    smoothness: Float = None,
                    exponent: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### snd

nd.voronoi_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    smoothness: Float = None,
                    exponent: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### class Float

```python
Float.Voronoi(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

### class Texture

```python
Texture.Voronoi(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    detail: Float = None,
                    roughness: Float = None,
                    lacunarity: Float = None,
                    randomness: Float = None,
                    distance: Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN',
                    feature: Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1',
                    normalize = False,
                    voronoi_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

## Voxel Index

> `bl_idname` : GeometryNodeInputVoxelIndex

### nd

nd.voxel_index.(cls)

### class Float

```python
Float.voxel_index(cls)
```

### class Integer

```python
Integer.voxel_index(cls)
```

### class Boolean

```python
Boolean.voxel_index(cls)
```

### class Vector

```python
Vector.voxel_index(cls)
```

## Voxelize Grid

> `bl_idname` : GeometryNodeGridVoxelize

### nd

nd.voxelize_grid.(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
Float.voxelize_grid(self)
```

### class Integer

```python
Integer.voxelize_grid(self)
```

### class Boolean

```python
Boolean.voxelize_grid(self)
```

### class Vector

```python
Vector.voxelize_grid(self)
```

## Warning

> `bl_idname` : GeometryNodeWarning

### nd

nd.warning.(cls,
                    show: Boolean = None,
                    message: String = None,
                    warning_type: Literal['ERROR', 'WARNING', 'INFO'] = 'ERROR')

### class Boolean

```python
Boolean.error(self, message: String = None)
```

```python
Boolean.warning(self, message: String = None)
```

```python
Boolean.info(self, message: String = None)
```

## Wave Texture

> `bl_idname` : ShaderNodeTexWave

### nd

nd.wave_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS')

### snd

nd.wave_texture.(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS')

### class Color

```python
Color.Wave(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS')
```

### class Texture

```python
Texture.Wave(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    detail: Float = None,
                    detail_scale: Float = None,
                    detail_roughness: Float = None,
                    phase_offset: Float = None,
                    bands_direction: Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X',
                    rings_direction: Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X',
                    wave_profile: Literal['SIN', 'SAW', 'TRI'] = 'SIN',
                    wave_type: Literal['BANDS', 'RINGS'] = 'BANDS')
```

## Wavelength

> `bl_idname` : ShaderNodeWavelength

### snd

nd.wavelength.(cls, wavelength: Float = None)

### class Float

```python
Float.wavelength(self)
```

## White Noise Texture

> `bl_idname` : ShaderNodeTexWhiteNoise

### nd

nd.white_noise_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### snd

nd.white_noise_texture.(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### class Float

```python
Float.WhiteNoise(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

### class Texture

```python
Texture.WhiteNoise(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

## Wireframe

> `bl_idname` : ShaderNodeWireframe

### snd

nd.wireframe.(cls, size: Float = None, use_pixel_size = False)

### class Float

```python
Float.wireframe(self, use_pixel_size = False)
```

## World Output

> `bl_idname` : ShaderNodeOutputWorld

### snd

nd.world_output.(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
Shader.world_output(self,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

