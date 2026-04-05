# Cross Reference

## 3D Cursor

> `bl_idname` : GeometryNodeTool3DCursor

### nd

[nd](nd.md).[_3d_cursor](nd.md#geonodes.core.generated.static_nd.ND._3d_cursor)(cls)

## AOV Output

> `bl_idname` : ShaderNodeOutputAOV

### snd

[snd](snd.md).[aov_output](snd.md#geonodes.core.generated.static_snd.SND.aov_output)(cls, color: Color = None, value: Float = None, aov_name = '')

### class Color

```python
[Color](color.md.md).[aov_output](color.md.md#('geonodes.core.color.md',).aov_output)(self, value: Float = None, aov_name = '')
```

## Accumulate Field

> `bl_idname` : GeometryNodeAccumulateField

### nd

[nd](nd.md).[accumulate_field](nd.md#geonodes.core.generated.static_nd.ND.accumulate_field)(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[accumulate_field](point.md.md#('geonodes.core.point.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[accumulate_field](edge.md.md#('geonodes.core.edge.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Face

```python
[Face](face.md.md).[accumulate_field](face.md.md#('geonodes.core.face.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[accumulate_field](corner.md.md#('geonodes.core.corner.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Spline

```python
[Spline](spline.md.md).[accumulate_field](spline.md.md#('geonodes.core.spline.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Instance

```python
[Instance](instance.md.md).[accumulate_field](instance.md.md#('geonodes.core.instance.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

### class Layer

```python
[Layer](layer.md.md).[accumulate_field](layer.md.md#('geonodes.core.layer.md',).accumulate_field)(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None)
```

## Active Camera

> `bl_idname` : GeometryNodeInputActiveCamera

### nd

[nd](nd.md).[active_camera](nd.md#geonodes.core.generated.static_nd.ND.active_camera)(self)

### class Object

```python
[Object](object.md.md).[ActiveCamera](object.md.md#('geonodes.core.object.md',).ActiveCamera)(cls)
```

## Active Element

> `bl_idname` : GeometryNodeToolActiveElement

### nd

[nd](nd.md).[active_element](nd.md#geonodes.core.generated.static_nd.ND.active_element)(cls, domain: Literal['POINT', 'EDGE', 'FACE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[active_element](point.md.md#('geonodes.core.point.md',).active_element)(cls)
```

### class Edge

```python
[Edge](edge.md.md).[active_element](edge.md.md#('geonodes.core.edge.md',).active_element)(cls)
```

### class Face

```python
[Face](face.md.md).[active_element](face.md.md#('geonodes.core.face.md',).active_element)(cls)
```

### class Layer

```python
[Layer](layer.md.md).[active_element](layer.md.md#('geonodes.core.layer.md',).active_element)(cls)
```

## Add Shader

> `bl_idname` : ShaderNodeAddShader

### snd

[snd](snd.md).[add_shader](snd.md#geonodes.core.generated.static_snd.SND.add_shader)(cls, shader: Shader = None, shader_1: Shader = None)

### class Shader

```python
[Shader](shader.md.md).[add](shader.md.md#('geonodes.core.shader.md',).add)(self, shader: Shader = None)
```

## Advect Grid

> `bl_idname` : GeometryNodeGridAdvect

### nd

[nd](nd.md).[advect_grid](nd.md#geonodes.core.generated.static_nd.ND.advect_grid)(cls,
                    grid: Float = None,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[advect_grid](float.md.md#('geonodes.core.float.md',).advect_grid)(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

### class Integer

```python
[Integer](integer.md.md).[advect_grid](integer.md.md#('geonodes.core.integer.md',).advect_grid)(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

### class Vector

```python
[Vector](vector.md.md).[advect_grid](vector.md.md#('geonodes.core.vector.md',).advect_grid)(self,
                    velocity: Vector = None,
                    time_step: Float = None,
                    integration_scheme: Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC'] = None,
                    limiter: Literal['None', 'Clamp', 'Revert'] = None)
```

## Align Rotation to Vector

> `bl_idname` : FunctionNodeAlignRotationToVector

### nd

[nd](nd.md).[align_rotation_to_vector](nd.md#geonodes.core.generated.static_nd.ND.align_rotation_to_vector)(cls,
                    rotation: Rotation = None,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')

### class Rotation

```python
[Rotation](rotation.md.md).[AlignToVector](rotation.md.md#('geonodes.core.rotation.md',).AlignToVector)(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[AlignXToVector](rotation.md.md#('geonodes.core.rotation.md',).AlignXToVector)(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[AlignYToVector](rotation.md.md#('geonodes.core.rotation.md',).AlignYToVector)(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[AlignZToVector](rotation.md.md#('geonodes.core.rotation.md',).AlignZToVector)(cls,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[align_to_vector](rotation.md.md#('geonodes.core.rotation.md',).align_to_vector)(self,
                    vector: Vector = None,
                    factor: Float = None,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[align_x_to_vector](rotation.md.md#('geonodes.core.rotation.md',).align_x_to_vector)(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[align_y_to_vector](rotation.md.md#('geonodes.core.rotation.md',).align_y_to_vector)(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

```python
[Rotation](rotation.md.md).[align_z_to_vector](rotation.md.md#('geonodes.core.rotation.md',).align_z_to_vector)(self,
                    vector: Vector = None,
                    factor: Float = None,
                    pivot_axis: Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO')
```

## Ambient Occlusion

> `bl_idname` : ShaderNodeAmbientOcclusion

### snd

[snd](snd.md).[ambient_occlusion](snd.md#geonodes.core.generated.static_snd.SND.ambient_occlusion)(cls,
                    color: Color = None,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16)

### class Color

```python
[Color](color.md.md).[ambient_occlusion](color.md.md#('geonodes.core.color.md',).ambient_occlusion)(self,
                    distance: Float = None,
                    normal: Vector = None,
                    inside = False,
                    only_local = False,
                    samples = 16)
```

## Arc

> `bl_idname` : GeometryNodeCurveArc

### nd

[nd](nd.md).[arc](nd.md#geonodes.core.generated.static_nd.ND.arc)(cls,
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
[Curve](curve.md.md).[ArcPoints](curve.md.md#('geonodes.core.curve.md',).ArcPoints)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None,
                    offset_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None)
```

```python
[Curve](curve.md.md).[ArcRadius](curve.md.md#('geonodes.core.curve.md',).ArcRadius)(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None)
```

```python
[Curve](curve.md.md).[Arc](curve.md.md#('geonodes.core.curve.md',).Arc)(cls,
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

[snd](snd.md).[attribute](snd.md#geonodes.core.generated.static_snd.SND.attribute)(cls,
                    attribute_name = '',
                    attribute_type: Literal['GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'] = 'GEOMETRY')

## Attribute Statistic

> `bl_idname` : GeometryNodeAttributeStatistic

### nd

[nd](nd.md).[attribute_statistic](nd.md#geonodes.core.generated.static_nd.ND.attribute_statistic)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    attribute: Float = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[attribute_statistic](point.md.md#('geonodes.core.point.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Edge

```python
[Edge](edge.md.md).[attribute_statistic](edge.md.md#('geonodes.core.edge.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Face

```python
[Face](face.md.md).[attribute_statistic](face.md.md#('geonodes.core.face.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Corner

```python
[Corner](corner.md.md).[attribute_statistic](corner.md.md#('geonodes.core.corner.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Spline

```python
[Spline](spline.md.md).[attribute_statistic](spline.md.md#('geonodes.core.spline.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Instance

```python
[Instance](instance.md.md).[attribute_statistic](instance.md.md#('geonodes.core.instance.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

### class Layer

```python
[Layer](layer.md.md).[attribute_statistic](layer.md.md#('geonodes.core.layer.md',).attribute_statistic)(self, attribute: Float | Vector = None)
```

## Axes to Rotation

> `bl_idname` : FunctionNodeAxesToRotation

### nd

[nd](nd.md).[axes_to_rotation](nd.md#geonodes.core.generated.static_nd.ND.axes_to_rotation)(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X')

### class Rotation

```python
[Rotation](rotation.md.md).[FromAxes](rotation.md.md#('geonodes.core.rotation.md',).FromAxes)(cls,
                    primary_axis_1: Vector = None,
                    secondary_axis_1: Vector = None,
                    primary_axis: Literal['X', 'Y', 'Z'] = 'Z',
                    secondary_axis: Literal['X', 'Y', 'Z'] = 'X')
```

```python
[Rotation](rotation.md.md).[FromXYAxes](rotation.md.md#('geonodes.core.rotation.md',).FromXYAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
[Rotation](rotation.md.md).[FromYXAxes](rotation.md.md#('geonodes.core.rotation.md',).FromYXAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
[Rotation](rotation.md.md).[FromXZAxes](rotation.md.md#('geonodes.core.rotation.md',).FromXZAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
[Rotation](rotation.md.md).[FromZXAxes](rotation.md.md#('geonodes.core.rotation.md',).FromZXAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
[Rotation](rotation.md.md).[FromYZAxes](rotation.md.md#('geonodes.core.rotation.md',).FromYZAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

```python
[Rotation](rotation.md.md).[FromZYAxes](rotation.md.md#('geonodes.core.rotation.md',).FromZYAxes)(cls, primary_axis: Vector = None, secondary_axis: Vector = None)
```

## Axis Angle to Rotation

> `bl_idname` : FunctionNodeAxisAngleToRotation

### nd

[nd](nd.md).[axis_angle_to_rotation](nd.md#geonodes.core.generated.static_nd.ND.axis_angle_to_rotation)(cls, axis: Vector = None, angle: Float = None)

### class Rotation

```python
[Rotation](rotation.md.md).[FromAxisAngle](rotation.md.md#('geonodes.core.rotation.md',).FromAxisAngle)(cls, axis: Vector = None, angle: Float = None)
```

## Background

> `bl_idname` : ShaderNodeBackground

### snd

[snd](snd.md).[background](snd.md#geonodes.core.generated.static_snd.SND.background)(cls, color: Color = None, strength: Float = None, weight: Float = None)

### class Color

```python
[Color](color.md.md).[background](color.md.md#('geonodes.core.color.md',).background)(self, strength: Float = None)
```

## Bake

> `bl_idname` : GeometryNodeBake

### nd

[nd](nd.md).[bake](nd.md#geonodes.core.generated.static_nd.ND.bake)(cls, named_sockets: dict = {}, **sockets)

## Bevel

> `bl_idname` : ShaderNodeBevel

### snd

[snd](snd.md).[bevel](snd.md#geonodes.core.generated.static_snd.SND.bevel)(cls, radius: Float = None, normal: Vector = None, samples = 4)

### class Float

```python
[Float](float.md.md).[bevel](float.md.md#('geonodes.core.float.md',).bevel)(self, normal: Vector = None, samples = 4)
```

## Bit Math

> `bl_idname` : FunctionNodeBitMath

### nd

[nd](nd.md).[bit_math](nd.md#geonodes.core.generated.static_nd.ND.bit_math)(cls,
                    a: Integer = None,
                    b: Integer = None,
                    shift: Integer = None,
                    operation: Literal['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE'] = 'AND')

### class Integer

```python
[Integer](integer.md.md).[bw_and](integer.md.md#('geonodes.core.integer.md',).bw_and)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[bw_or](integer.md.md#('geonodes.core.integer.md',).bw_or)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[bw_xor](integer.md.md#('geonodes.core.integer.md',).bw_xor)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[bw_not](integer.md.md#('geonodes.core.integer.md',).bw_not)(self)
```

```python
[Integer](integer.md.md).[bw_shift](integer.md.md#('geonodes.core.integer.md',).bw_shift)(self, shift: Integer = None)
```

```python
[Integer](integer.md.md).[bw_rotate](integer.md.md#('geonodes.core.integer.md',).bw_rotate)(self, shift: Integer = None)
```

### class gnmath

```python
[gnmath](gnmath.md.md).[bw_and](gnmath.md.md#('geonodes.core.gnmath.md',).bw_and)(a: Integer = None, b: Integer = None)
```

```python
[gnmath](gnmath.md.md).[bw_or](gnmath.md.md#('geonodes.core.gnmath.md',).bw_or)(a: Integer = None, b: Integer = None)
```

```python
[gnmath](gnmath.md.md).[bw_xor](gnmath.md.md#('geonodes.core.gnmath.md',).bw_xor)(a: Integer = None, b: Integer = None)
```

```python
[gnmath](gnmath.md.md).[bw_not](gnmath.md.md#('geonodes.core.gnmath.md',).bw_not)(a: Integer = None)
```

```python
[gnmath](gnmath.md.md).[bw_shift](gnmath.md.md#('geonodes.core.gnmath.md',).bw_shift)(a: Integer = None, shift: Integer = None)
```

```python
[gnmath](gnmath.md.md).[bw_rotate](gnmath.md.md#('geonodes.core.gnmath.md',).bw_rotate)(a: Integer = None, shift: Integer = None)
```

## Blackbody

> `bl_idname` : ShaderNodeBlackbody

### nd

[nd](nd.md).[blackbody](nd.md#geonodes.core.generated.static_nd.ND.blackbody)(cls, temperature: Float = None)

### snd

[snd](snd.md).[blackbody](snd.md#geonodes.core.generated.static_snd.SND.blackbody)(cls, temperature: Float = None)

### class Color

```python
[Color](color.md.md).[Blackbody](color.md.md#('geonodes.core.color.md',).Blackbody)(cls, temperature: Float = None)
```

## Blur Attribute

> `bl_idname` : GeometryNodeBlurAttribute

### nd

[nd](nd.md).[blur_attribute](nd.md#geonodes.core.generated.static_nd.ND.blur_attribute)(cls,
                    value: Float = None,
                    iterations: Integer = None,
                    weight: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[blur](float.md.md#('geonodes.core.float.md',).blur)(self, iterations: Integer = None, weight: Float = None)
```

### class Integer

```python
[Integer](integer.md.md).[blur](integer.md.md#('geonodes.core.integer.md',).blur)(self, iterations: Integer = None, weight: Float = None)
```

### class Vector

```python
[Vector](vector.md.md).[blur](vector.md.md#('geonodes.core.vector.md',).blur)(self, iterations: Integer = None, weight: Float = None)
```

### class Color

```python
[Color](color.md.md).[blur](color.md.md#('geonodes.core.color.md',).blur)(self, iterations: Integer = None, weight: Float = None)
```

## Bone Info

> `bl_idname` : GeometryNodeBoneInfo

### nd

[nd](nd.md).[bone_info](nd.md#geonodes.core.generated.static_nd.ND.bone_info)(cls,
                    armature: Object = None,
                    bone_name: String = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')

### class Object

```python
[Object](object.md.md).[bone_info](object.md.md#('geonodes.core.object.md',).bone_info)(self,
                    bone_name: String = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')
```

## Boolean

> `bl_idname` : FunctionNodeInputBool

### nd

[nd](nd.md).[boolean](nd.md#geonodes.core.generated.static_nd.ND.boolean)(cls, boolean = False)

## Boolean Math

> `bl_idname` : FunctionNodeBooleanMath

### nd

[nd](nd.md).[boolean_math](nd.md#geonodes.core.generated.static_nd.ND.boolean_math)(cls,
                    boolean: Boolean = None,
                    boolean_1: Boolean = None,
                    operation: Literal['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY'] = 'AND')

### class Boolean

```python
[Boolean](boolean.md.md).[band](boolean.md.md#('geonodes.core.boolean.md',).band)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[bor](boolean.md.md#('geonodes.core.boolean.md',).bor)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[bnot](boolean.md.md#('geonodes.core.boolean.md',).bnot)(self)
```

```python
[Boolean](boolean.md.md).[not_and](boolean.md.md#('geonodes.core.boolean.md',).not_and)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[nor](boolean.md.md#('geonodes.core.boolean.md',).nor)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[xnor](boolean.md.md#('geonodes.core.boolean.md',).xnor)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[xor](boolean.md.md#('geonodes.core.boolean.md',).xor)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[imply](boolean.md.md#('geonodes.core.boolean.md',).imply)(self, boolean: Boolean = None)
```

```python
[Boolean](boolean.md.md).[nimply](boolean.md.md#('geonodes.core.boolean.md',).nimply)(self, boolean: Boolean = None)
```

### class gnmath

```python
[gnmath](gnmath.md.md).[band](gnmath.md.md#('geonodes.core.gnmath.md',).band)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[bor](gnmath.md.md#('geonodes.core.gnmath.md',).bor)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[bnot](gnmath.md.md#('geonodes.core.gnmath.md',).bnot)(boolean: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[not_and](gnmath.md.md#('geonodes.core.gnmath.md',).not_and)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[nor](gnmath.md.md#('geonodes.core.gnmath.md',).nor)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[xnor](gnmath.md.md#('geonodes.core.gnmath.md',).xnor)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[xor](gnmath.md.md#('geonodes.core.gnmath.md',).xor)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[imply](gnmath.md.md#('geonodes.core.gnmath.md',).imply)(boolean: Boolean = None, boolean_1: Boolean = None)
```

```python
[gnmath](gnmath.md.md).[nimply](gnmath.md.md#('geonodes.core.gnmath.md',).nimply)(boolean: Boolean = None, boolean_1: Boolean = None)
```

## Bounding Box

> `bl_idname` : GeometryNodeBoundBox

### nd

[nd](nd.md).[bounding_box](nd.md#geonodes.core.generated.static_nd.ND.bounding_box)(cls, geometry: Geometry = None, use_radius: Boolean = None)

### class Geometry

```python
[Geometry](geometry.md.md).[bounding_box](geometry.md.md#('geonodes.core.geometry.md',).bounding_box)(self, use_radius: Boolean = None)
```

## Brick Texture

> `bl_idname` : ShaderNodeTexBrick

### nd

[nd](nd.md).[brick_texture](nd.md#geonodes.core.generated.static_nd.ND.brick_texture)(cls,
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

[snd](snd.md).[brick_texture](snd.md#geonodes.core.generated.static_snd.SND.brick_texture)(cls,
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
[Color](color.md.md).[Brick](color.md.md#('geonodes.core.color.md',).Brick)(cls,
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
[Texture](texture.md.md).[Brick](texture.md.md#('geonodes.core.texture.md',).Brick)(cls,
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

[snd](snd.md).[brightness_contrast](snd.md#geonodes.core.generated.static_snd.SND.brightness_contrast)(cls, color: Color = None, brightness: Float = None, contrast: Float = None)

### class Color

```python
[Color](color.md.md).[brightness_contrast](color.md.md#('geonodes.core.color.md',).brightness_contrast)(self, brightness: Float = None, contrast: Float = None)
```

## Bump

> `bl_idname` : ShaderNodeBump

### snd

[snd](snd.md).[bump](snd.md#geonodes.core.generated.static_snd.SND.bump)(cls,
                    strength: Float = None,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False)

### class Float

```python
[Float](float.md.md).[bump](float.md.md#('geonodes.core.float.md',).bump)(self,
                    distance: Float = None,
                    filter_width: Float = None,
                    height: Float = None,
                    normal: Vector = None,
                    invert = False)
```

## Bézier Segment

> `bl_idname` : GeometryNodeCurvePrimitiveBezierSegment

### nd

[nd](nd.md).[bezier_segment](nd.md#geonodes.core.generated.static_nd.ND.bezier_segment)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None,
                    mode: Literal['POSITION', 'OFFSET'] = 'POSITION')

### class Curve

```python
[Curve](curve.md.md).[BeziersegmentPosition](curve.md.md#('geonodes.core.curve.md',).BeziersegmentPosition)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None)
```

```python
[Curve](curve.md.md).[BeziersegmentOffset](curve.md.md#('geonodes.core.curve.md',).BeziersegmentOffset)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None)
```

```python
[Curve](curve.md.md).[BezierSegment](curve.md.md#('geonodes.core.curve.md',).BezierSegment)(cls,
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

[snd](snd.md).[camera_data](snd.md#geonodes.core.generated.static_snd.SND.camera_data)(cls)

## Camera Info

> `bl_idname` : GeometryNodeCameraInfo

### nd

[nd](nd.md).[camera_info](nd.md#geonodes.core.generated.static_nd.ND.camera_info)(cls, camera: Object = None)

### class Object

```python
[Object](object.md.md).[camera_info](object.md.md#('geonodes.core.object.md',).camera_info)(self)
```

## Capture Attribute

> `bl_idname` : GeometryNodeCaptureAttribute

### class Domain

```python
[Domain](domain.md.md).[capture_attribute](domain.md.md#('geonodes.core.domain.md',).capture_attribute)(attribute=None, **attributes)
```

```python
[Domain](domain.md.md).[capture](domain.md.md#('geonodes.core.domain.md',).capture)(attribute=None, **attributes)
```

## Checker Texture

> `bl_idname` : ShaderNodeTexChecker

### nd

[nd](nd.md).[checker_texture](nd.md#geonodes.core.generated.static_nd.ND.checker_texture)(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)

### snd

[snd](snd.md).[checker_texture](snd.md#geonodes.core.generated.static_snd.SND.checker_texture)(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)

### class Color

```python
[Color](color.md.md).[Checker](color.md.md#('geonodes.core.color.md',).Checker)(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)
```

### class Texture

```python
[Texture](texture.md.md).[Checker](texture.md.md#('geonodes.core.texture.md',).Checker)(cls,
                    vector: Vector = None,
                    color1: Color = None,
                    color2: Color = None,
                    scale: Float = None)
```

## Clamp

> `bl_idname` : ShaderNodeClamp

### nd

[nd](nd.md).[clamp](nd.md#geonodes.core.generated.static_nd.ND.clamp)(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')

### snd

[snd](snd.md).[clamp](snd.md#geonodes.core.generated.static_snd.SND.clamp)(cls,
                    value: Float = None,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')

### class Float

```python
[Float](float.md.md).[clamp](float.md.md#('geonodes.core.float.md',).clamp)(self,
                    min: Float = None,
                    max: Float = None,
                    clamp_type: Literal['MINMAX', 'RANGE'] = 'MINMAX')
```

```python
[Float](float.md.md).[clamp_minmax](float.md.md#('geonodes.core.float.md',).clamp_minmax)(self, min: Float = None, max: Float = None)
```

```python
[Float](float.md.md).[clamp_range](float.md.md#('geonodes.core.float.md',).clamp_range)(self, min: Float = None, max: Float = None)
```

## Clip Grid

> `bl_idname` : GeometryNodeGridClip

### nd

[nd](nd.md).[clip_grid](nd.md#geonodes.core.generated.static_nd.ND.clip_grid)(cls,
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
[Float](float.md.md).[clip_grid](float.md.md#('geonodes.core.float.md',).clip_grid)(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[clip_grid](integer.md.md#('geonodes.core.integer.md',).clip_grid)(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[clip_grid](boolean.md.md#('geonodes.core.boolean.md',).clip_grid)(self,
                    min_x: Integer = None,
                    min_y: Integer = None,
                    min_z: Integer = None,
                    max_x: Integer = None,
                    max_y: Integer = None,
                    max_z: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[clip_grid](vector.md.md#('geonodes.core.vector.md',).clip_grid)(self,
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

[nd](nd.md).[closure_input](nd.md#geonodes.core.generated.static_nd.ND.closure_input)(self)

### snd

[snd](snd.md).[closure_input](snd.md#geonodes.core.generated.static_snd.SND.closure_input)(self)

## Closure Output

> `bl_idname` : NodeClosureOutput

### nd

[nd](nd.md).[closure_output](nd.md#geonodes.core.generated.static_nd.ND.closure_output)(cls, active_input_index = 0, active_output_index = 0, define_signature = False)

### snd

[snd](snd.md).[closure_output](snd.md#geonodes.core.generated.static_snd.SND.closure_output)(cls, active_input_index = 0, active_output_index = 0, define_signature = False)

## Collection

> `bl_idname` : GeometryNodeInputCollection

### nd

[nd](nd.md).[collection](nd.md#geonodes.core.generated.static_nd.ND.collection)(cls, collection = None)

## Collection Info

> `bl_idname` : GeometryNodeCollectionInfo

### nd

[nd](nd.md).[collection_info](nd.md#geonodes.core.generated.static_nd.ND.collection_info)(cls,
                    collection: Collection = None,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')

### class Collection

```python
[Collection](collection.md.md).[info](collection.md.md#('geonodes.core.collection.md',).info)(self,
                    separate_children: Boolean = None,
                    reset_children: Boolean = None,
                    transform_space: Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL')
```

## Color

> `bl_idname` : ShaderNodeRGB

### snd

[snd](snd.md).[color](snd.md#geonodes.core.generated.static_snd.SND.color)(self)

## Color Attribute

> `bl_idname` : ShaderNodeVertexColor

### snd

[snd](snd.md).[color_attribute](snd.md#geonodes.core.generated.static_snd.SND.color_attribute)(cls, layer_name = '')

### class Color

```python
[Color](color.md.md).[ColorAttribute](color.md.md#('geonodes.core.color.md',).ColorAttribute)(cls, layer_name = '')
```

## Color Ramp

> `bl_idname` : ShaderNodeValToRGB

### nd

[nd](nd.md).[color_ramp](nd.md#geonodes.core.generated.static_nd.ND.color_ramp)(fac=None, stops=None, interpolation='LINEAR')

### snd

[snd](snd.md).[color_ramp](snd.md#geonodes.core.generated.static_snd.SND.color_ramp)(fac=None, stops=None, interpolation='LINEAR')

## Combine Bundle

> `bl_idname` : NodeCombineBundle

### nd

[nd](nd.md).[combine_bundle](nd.md#geonodes.core.generated.static_nd.ND.combine_bundle)(cls, named_sockets: dict = {}, define_signature = False, **sockets)

### snd

[snd](snd.md).[combine_bundle](snd.md#geonodes.core.generated.static_snd.SND.combine_bundle)(cls, named_sockets: dict = {}, define_signature = False, **sockets)

### class Bundle

```python
[Bundle](bundle.md.md).[Combine](bundle.md.md#('geonodes.core.bundle.md',).Combine)(cls, named_sockets: dict = {}, define_signature = False, **sockets)
```

## Combine Color

> `bl_idname` : ShaderNodeCombineColor

### snd

[snd](snd.md).[combine_color](snd.md#geonodes.core.generated.static_snd.SND.combine_color)(cls,
                    red: Float = None,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')

### class Float

```python
[Float](float.md.md).[combine_color_RGB](float.md.md#('geonodes.core.float.md',).combine_color_RGB)(self, green: Float = None, blue: Float = None)
```

```python
[Float](float.md.md).[combine_color_HSV](float.md.md#('geonodes.core.float.md',).combine_color_HSV)(self, saturation: Float = None, value: Float = None)
```

```python
[Float](float.md.md).[combine_color_HSL](float.md.md#('geonodes.core.float.md',).combine_color_HSL)(self, saturation: Float = None, lightness: Float = None)
```

```python
[Float](float.md.md).[combine_color](float.md.md#('geonodes.core.float.md',).combine_color)(self,
                    green: Float = None,
                    blue: Float = None,
                    mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')
```

## Combine Matrix

> `bl_idname` : FunctionNodeCombineMatrix

### nd

[nd](nd.md).[combine_matrix](nd.md#geonodes.core.generated.static_nd.ND.combine_matrix)(cls,
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
[Matrix](matrix.md.md).[Combine](matrix.md.md#('geonodes.core.matrix.md',).Combine)(cls,
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

[nd](nd.md).[combine_transform](nd.md#geonodes.core.generated.static_nd.ND.combine_transform)(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None)

### class Matrix

```python
[Matrix](matrix.md.md).[CombineTransform](matrix.md.md#('geonodes.core.matrix.md',).CombineTransform)(cls,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

## Combine XYZ

> `bl_idname` : ShaderNodeCombineXYZ

### nd

[nd](nd.md).[combine_xyz](nd.md#geonodes.core.generated.static_nd.ND.combine_xyz)(cls, x: Float = None, y: Float = None, z: Float = None)

### snd

[snd](snd.md).[combine_xyz](snd.md#geonodes.core.generated.static_snd.SND.combine_xyz)(cls, x: Float = None, y: Float = None, z: Float = None)

### class Vector

```python
[Vector](vector.md.md).[CombineXYZ](vector.md.md#('geonodes.core.vector.md',).CombineXYZ)(cls, x: Float = None, y: Float = None, z: Float = None)
```

## Compare

> `bl_idname` : FunctionNodeCompare

### nd

[nd](nd.md).[compare](nd.md#geonodes.core.generated.static_nd.ND.compare)(cls,
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
[Float](float.md.md).[less_than](float.md.md#('geonodes.core.float.md',).less_than)(self, b: Float = None)
```

```python
[Float](float.md.md).[less_equal](float.md.md#('geonodes.core.float.md',).less_equal)(self, b: Float = None)
```

```python
[Float](float.md.md).[greater_than](float.md.md#('geonodes.core.float.md',).greater_than)(self, b: Float = None)
```

```python
[Float](float.md.md).[greater_equal](float.md.md#('geonodes.core.float.md',).greater_equal)(self, b: Float = None)
```

```python
[Float](float.md.md).[equal](float.md.md#('geonodes.core.float.md',).equal)(self, b: Float = None, epsilon: Float = None)
```

```python
[Float](float.md.md).[not_equal](float.md.md#('geonodes.core.float.md',).not_equal)(self, b: Float = None, epsilon: Float = None)
```

### class Integer

```python
[Integer](integer.md.md).[less_than](integer.md.md#('geonodes.core.integer.md',).less_than)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[less_equal](integer.md.md#('geonodes.core.integer.md',).less_equal)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[greater_than](integer.md.md#('geonodes.core.integer.md',).greater_than)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[greater_equal](integer.md.md#('geonodes.core.integer.md',).greater_equal)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[equal](integer.md.md#('geonodes.core.integer.md',).equal)(self, b: Integer = None)
```

```python
[Integer](integer.md.md).[not_equal](integer.md.md#('geonodes.core.integer.md',).not_equal)(self, b: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[less_than](vector.md.md#('geonodes.core.vector.md',).less_than)(self, b: Vector = None)
```

```python
[Vector](vector.md.md).[less_equal](vector.md.md#('geonodes.core.vector.md',).less_equal)(self, b: Vector = None)
```

```python
[Vector](vector.md.md).[greater_than](vector.md.md#('geonodes.core.vector.md',).greater_than)(self, b: Vector = None)
```

```python
[Vector](vector.md.md).[greater_equal](vector.md.md#('geonodes.core.vector.md',).greater_equal)(self, b: Vector = None)
```

```python
[Vector](vector.md.md).[equal](vector.md.md#('geonodes.core.vector.md',).equal)(self, b: Vector = None, epsilon: Float = None)
```

```python
[Vector](vector.md.md).[not_equal](vector.md.md#('geonodes.core.vector.md',).not_equal)(self, b: Vector = None, epsilon: Float = None)
```

### class String

```python
[String](string.md.md).[equal](string.md.md#('geonodes.core.string.md',).equal)(self, b: String = None)
```

```python
[String](string.md.md).[not_equal](string.md.md#('geonodes.core.string.md',).not_equal)(self, b: String = None)
```

### class Color

```python
[Color](color.md.md).[equal](color.md.md#('geonodes.core.color.md',).equal)(self, b: Color = None, epsilon: Float = None)
```

```python
[Color](color.md.md).[not_equal](color.md.md#('geonodes.core.color.md',).not_equal)(self, b: Color = None, epsilon: Float = None)
```

```python
[Color](color.md.md).[brighter](color.md.md#('geonodes.core.color.md',).brighter)(self, b: Color = None)
```

```python
[Color](color.md.md).[darker](color.md.md#('geonodes.core.color.md',).darker)(self, b: Color = None)
```

## Cone

> `bl_idname` : GeometryNodeMeshCone

### nd

[nd](nd.md).[cone](nd.md#geonodes.core.generated.static_nd.ND.cone)(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius_top: Float = None,
                    radius_bottom: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')

### class Mesh

```python
[Mesh](mesh.md.md).[Cone](mesh.md.md#('geonodes.core.mesh.md',).Cone)(cls,
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

[nd](nd.md).[convex_hull](nd.md#geonodes.core.generated.static_nd.ND.convex_hull)(cls, geometry: Geometry = None)

### class Geometry

```python
[Geometry](geometry.md.md).[convex_hull](geometry.md.md#('geonodes.core.geometry.md',).convex_hull)(self)
```

## Corners of Edge

> `bl_idname` : GeometryNodeCornersOfEdge

### nd

[nd](nd.md).[corners_of_edge](nd.md#geonodes.core.generated.static_nd.ND.corners_of_edge)(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[corners_of_edge](mesh.md.md#('geonodes.core.mesh.md',).corners_of_edge)(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[corners](edge.md.md#('geonodes.core.edge.md',).corners)(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Edge](edge.md.md).[corner_index](edge.md.md#('geonodes.core.edge.md',).corner_index)(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Edge](edge.md.md).[corners_total](edge.md.md#('geonodes.core.edge.md',).corners_total)(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Corners of Face

> `bl_idname` : GeometryNodeCornersOfFace

### nd

[nd](nd.md).[corners_of_face](nd.md#geonodes.core.generated.static_nd.ND.corners_of_face)(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[corners_of_face](mesh.md.md#('geonodes.core.mesh.md',).corners_of_face)(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Face

```python
[Face](face.md.md).[corners](face.md.md#('geonodes.core.face.md',).corners)(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Face](face.md.md).[corner_index](face.md.md#('geonodes.core.face.md',).corner_index)(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Face](face.md.md).[corners_total](face.md.md#('geonodes.core.face.md',).corners_total)(cls,
                    face_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Corners of Vertex

> `bl_idname` : GeometryNodeCornersOfVertex

### nd

[nd](nd.md).[corners_of_vertex](nd.md#geonodes.core.generated.static_nd.ND.corners_of_vertex)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[corners_of_vertex](mesh.md.md#('geonodes.core.mesh.md',).corners_of_vertex)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Vertex

```python
[Vertex](vertex.md.md).[corners](vertex.md.md#('geonodes.core.vertex.md',).corners)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Vertex](vertex.md.md).[corner_index](vertex.md.md#('geonodes.core.vertex.md',).corner_index)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Vertex](vertex.md.md).[corners_total](vertex.md.md#('geonodes.core.vertex.md',).corners_total)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Cube

> `bl_idname` : GeometryNodeMeshCube

### nd

[nd](nd.md).[cube](nd.md#geonodes.core.generated.static_nd.ND.cube)(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[Cube](mesh.md.md#('geonodes.core.mesh.md',).Cube)(cls,
                    size: Vector = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None,
                    vertices_z: Integer = None)
```

## Cube Grid Topology

> `bl_idname` : GeometryNodeCubeGridTopology

### nd

[nd](nd.md).[cube_grid_topology](nd.md#geonodes.core.generated.static_nd.ND.cube_grid_topology)(cls,
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
[Boolean](boolean.md.md).[CubeGridTopology](boolean.md.md#('geonodes.core.boolean.md',).CubeGridTopology)(cls,
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

[nd](nd.md).[curve_circle](nd.md#geonodes.core.generated.static_nd.ND.curve_circle)(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')

### class Curve

```python
[Curve](curve.md.md).[CirclePoints](curve.md.md#('geonodes.core.curve.md',).CirclePoints)(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None)
```

```python
[Curve](curve.md.md).[CircleRadius](curve.md.md#('geonodes.core.curve.md',).CircleRadius)(cls, resolution: Integer = None, radius: Float = None)
```

```python
[Curve](curve.md.md).[Circle](curve.md.md#('geonodes.core.curve.md',).Circle)(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS')
```

## Curve Handle Positions

> `bl_idname` : GeometryNodeInputCurveHandlePositions

### nd

[nd](nd.md).[curve_handle_positions](nd.md#geonodes.core.generated.static_nd.ND.curve_handle_positions)(cls, relative: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[handle_positions](curve.md.md#('geonodes.core.curve.md',).handle_positions)(cls, relative: Boolean = None)
```

```python
prop = [Curve](curve.md.md).[left_handle_position](curve.md.md#('geonodes.core.curve.md',).left_handle_position)
```

```python
prop = [Curve](curve.md.md).[right_handle_position](curve.md.md#('geonodes.core.curve.md',).right_handle_position)
```

```python
prop = [Curve](curve.md.md).[left_handle_offset](curve.md.md#('geonodes.core.curve.md',).left_handle_offset)
```

```python
prop = [Curve](curve.md.md).[right_handle_offset](curve.md.md#('geonodes.core.curve.md',).right_handle_offset)
```

## Curve Length

> `bl_idname` : GeometryNodeCurveLength

### nd

[nd](nd.md).[curve_length](nd.md#geonodes.core.generated.static_nd.ND.curve_length)(cls, curve: Curve = None)

### class Curve

```python
[Curve](curve.md.md).[length](curve.md.md#('geonodes.core.curve.md',).length)(self)
```

## Curve Line

> `bl_idname` : GeometryNodeCurvePrimitiveLine

### nd

[nd](nd.md).[curve_line](nd.md#geonodes.core.generated.static_nd.ND.curve_line)(cls,
                    start: Vector = None,
                    end: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS')

### class Curve

```python
[Curve](curve.md.md).[LinePoints](curve.md.md#('geonodes.core.curve.md',).LinePoints)(cls, start: Vector = None, end: Vector = None)
```

```python
[Curve](curve.md.md).[LineDirection](curve.md.md#('geonodes.core.curve.md',).LineDirection)(cls, start: Vector = None, direction: Vector = None, length: Float = None)
```

```python
[Curve](curve.md.md).[Line](curve.md.md#('geonodes.core.curve.md',).Line)(cls,
                    start: Vector = None,
                    end: Vector = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS')
```

## Curve Tangent

> `bl_idname` : GeometryNodeInputTangent

### nd

[nd](nd.md).[curve_tangent](nd.md#geonodes.core.generated.static_nd.ND.curve_tangent)(self)

### class Curve

```python
prop = [Curve](curve.md.md).[tangent](curve.md.md#('geonodes.core.curve.md',).tangent)
```

## Curve Tilt

> `bl_idname` : GeometryNodeInputCurveTilt

### nd

[nd](nd.md).[curve_tilt](nd.md#geonodes.core.generated.static_nd.ND.curve_tilt)(self)

### class Curve

```python
prop = [Curve](curve.md.md).[tilt](curve.md.md#('geonodes.core.curve.md',).tilt)
```

### class Spline

```python
prop = [Spline](spline.md.md).[tilt](spline.md.md#('geonodes.core.spline.md',).tilt)
```

## Curve of Point

> `bl_idname` : GeometryNodeCurveOfPoint

### nd

[nd](nd.md).[curve_of_point](nd.md#geonodes.core.generated.static_nd.ND.curve_of_point)(cls, point_index: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[curve_of_point](curve.md.md#('geonodes.core.curve.md',).curve_of_point)(cls, point_index: Integer = None)
```

### class SplinePoint

```python
[SplinePoint](spline_point.md.md).[curve_of_point](spline_point.md.md#('geonodes.core.spline_point.md',).curve_of_point)(cls, point_index: Integer = None)
```

```python
[SplinePoint](spline_point.md.md).[curve_index](spline_point.md.md#('geonodes.core.spline_point.md',).curve_index)(cls, point_index: Integer = None)
```

```python
[SplinePoint](spline_point.md.md).[index_in_curve](spline_point.md.md#('geonodes.core.spline_point.md',).index_in_curve)(cls, point_index: Integer = None)
```

## Curve to Mesh

> `bl_idname` : GeometryNodeCurveToMesh

### nd

[nd](nd.md).[curve_to_mesh](nd.md#geonodes.core.generated.static_nd.ND.curve_to_mesh)(cls,
                    curve: Curve = None,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[to_mesh](curve.md.md#('geonodes.core.curve.md',).to_mesh)(self,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None)
```

## Curve to Points

> `bl_idname` : GeometryNodeCurveToPoints

### nd

[nd](nd.md).[curve_to_points](nd.md#geonodes.core.generated.static_nd.ND.curve_to_points)(cls,
                    curve: Curve = None,
                    count: Integer = None,
                    length: Float = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')

### class Curve

```python
[Curve](curve.md.md).[to_points_evaluated](curve.md.md#('geonodes.core.curve.md',).to_points_evaluated)(self)
```

```python
[Curve](curve.md.md).[to_points_count](curve.md.md#('geonodes.core.curve.md',).to_points_count)(self, count: Integer = None)
```

```python
[Curve](curve.md.md).[to_points_length](curve.md.md#('geonodes.core.curve.md',).to_points_length)(self, length: Float = None)
```

```python
[Curve](curve.md.md).[to_points](curve.md.md#('geonodes.core.curve.md',).to_points)(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')
```

### class SplinePoint

```python
[SplinePoint](spline_point.md.md).[to_points_evaluated](spline_point.md.md#('geonodes.core.spline_point.md',).to_points_evaluated)(self)
```

```python
[SplinePoint](spline_point.md.md).[to_points_count](spline_point.md.md#('geonodes.core.spline_point.md',).to_points_count)(self, count: Integer = None)
```

```python
[SplinePoint](spline_point.md.md).[to_points_length](spline_point.md.md#('geonodes.core.spline_point.md',).to_points_length)(self, length: Float = None)
```

```python
[SplinePoint](spline_point.md.md).[to_points](spline_point.md.md#('geonodes.core.spline_point.md',).to_points)(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT')
```

## Curves Info

> `bl_idname` : ShaderNodeHairInfo

### snd

[snd](snd.md).[curves_info](snd.md#geonodes.core.generated.static_snd.SND.curves_info)(cls)

## Curves to Grease Pencil

> `bl_idname` : GeometryNodeCurvesToGreasePencil

### nd

[nd](nd.md).[curves_to_grease_pencil](nd.md#geonodes.core.generated.static_nd.ND.curves_to_grease_pencil)(cls,
                    curves: Curve = None,
                    selection: Boolean = None,
                    instances_as_layers: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[to_grease_pencil](curve.md.md#('geonodes.core.curve.md',).to_grease_pencil)(self, instances_as_layers: Boolean = None)
```

## Cylinder

> `bl_idname` : GeometryNodeMeshCylinder

### nd

[nd](nd.md).[cylinder](nd.md#geonodes.core.generated.static_nd.ND.cylinder)(cls,
                    vertices: Integer = None,
                    side_segments: Integer = None,
                    fill_segments: Integer = None,
                    radius: Float = None,
                    depth: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON')

### class Mesh

```python
[Mesh](mesh.md.md).[Cylinder](mesh.md.md#('geonodes.core.mesh.md',).Cylinder)(cls,
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

[nd](nd.md).[deform_curves_on_surface](nd.md#geonodes.core.generated.static_nd.ND.deform_curves_on_surface)(cls, curves: Curve = None)

### class Curve

```python
[Curve](curve.md.md).[deform_on_surface](curve.md.md#('geonodes.core.curve.md',).deform_on_surface)(self)
```

## Delete Geometry

> `bl_idname` : GeometryNodeDeleteGeometry

### nd

[nd](nd.md).[delete_geometry](nd.md#geonodes.core.generated.static_nd.ND.delete_geometry)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT',
                    mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')

### class Point

```python
[Point](point.md.md).[delete_geometry_all](point.md.md#('geonodes.core.point.md',).delete_geometry_all)(self)
```

```python
[Point](point.md.md).[delete_geometry_edge_face](point.md.md#('geonodes.core.point.md',).delete_geometry_edge_face)(self)
```

```python
[Point](point.md.md).[delete_geometry_only_face](point.md.md#('geonodes.core.point.md',).delete_geometry_only_face)(self)
```

```python
[Point](point.md.md).[delete_geometry](point.md.md#('geonodes.core.point.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Point](point.md.md).[delete_all](point.md.md#('geonodes.core.point.md',).delete_all)(self)
```

```python
[Point](point.md.md).[delete_edge_face](point.md.md#('geonodes.core.point.md',).delete_edge_face)(self)
```

```python
[Point](point.md.md).[delete_only_face](point.md.md#('geonodes.core.point.md',).delete_only_face)(self)
```

```python
[Point](point.md.md).[delete](point.md.md#('geonodes.core.point.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Edge

```python
[Edge](edge.md.md).[delete_geometry_all](edge.md.md#('geonodes.core.edge.md',).delete_geometry_all)(self)
```

```python
[Edge](edge.md.md).[delete_geometry_edge_face](edge.md.md#('geonodes.core.edge.md',).delete_geometry_edge_face)(self)
```

```python
[Edge](edge.md.md).[delete_geometry_only_face](edge.md.md#('geonodes.core.edge.md',).delete_geometry_only_face)(self)
```

```python
[Edge](edge.md.md).[delete_geometry](edge.md.md#('geonodes.core.edge.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Edge](edge.md.md).[delete_all](edge.md.md#('geonodes.core.edge.md',).delete_all)(self)
```

```python
[Edge](edge.md.md).[delete_edge_face](edge.md.md#('geonodes.core.edge.md',).delete_edge_face)(self)
```

```python
[Edge](edge.md.md).[delete_only_face](edge.md.md#('geonodes.core.edge.md',).delete_only_face)(self)
```

```python
[Edge](edge.md.md).[delete](edge.md.md#('geonodes.core.edge.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Face

```python
[Face](face.md.md).[delete_geometry_all](face.md.md#('geonodes.core.face.md',).delete_geometry_all)(self)
```

```python
[Face](face.md.md).[delete_geometry_edge_face](face.md.md#('geonodes.core.face.md',).delete_geometry_edge_face)(self)
```

```python
[Face](face.md.md).[delete_geometry_only_face](face.md.md#('geonodes.core.face.md',).delete_geometry_only_face)(self)
```

```python
[Face](face.md.md).[delete_geometry](face.md.md#('geonodes.core.face.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Face](face.md.md).[delete_all](face.md.md#('geonodes.core.face.md',).delete_all)(self)
```

```python
[Face](face.md.md).[delete_edge_face](face.md.md#('geonodes.core.face.md',).delete_edge_face)(self)
```

```python
[Face](face.md.md).[delete_only_face](face.md.md#('geonodes.core.face.md',).delete_only_face)(self)
```

```python
[Face](face.md.md).[delete](face.md.md#('geonodes.core.face.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Spline

```python
[Spline](spline.md.md).[delete_geometry_all](spline.md.md#('geonodes.core.spline.md',).delete_geometry_all)(self)
```

```python
[Spline](spline.md.md).[delete_geometry_edge_face](spline.md.md#('geonodes.core.spline.md',).delete_geometry_edge_face)(self)
```

```python
[Spline](spline.md.md).[delete_geometry_only_face](spline.md.md#('geonodes.core.spline.md',).delete_geometry_only_face)(self)
```

```python
[Spline](spline.md.md).[delete_geometry](spline.md.md#('geonodes.core.spline.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Spline](spline.md.md).[delete_all](spline.md.md#('geonodes.core.spline.md',).delete_all)(self)
```

```python
[Spline](spline.md.md).[delete_edge_face](spline.md.md#('geonodes.core.spline.md',).delete_edge_face)(self)
```

```python
[Spline](spline.md.md).[delete_only_face](spline.md.md#('geonodes.core.spline.md',).delete_only_face)(self)
```

```python
[Spline](spline.md.md).[delete](spline.md.md#('geonodes.core.spline.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Instance

```python
[Instance](instance.md.md).[delete_geometry_all](instance.md.md#('geonodes.core.instance.md',).delete_geometry_all)(self)
```

```python
[Instance](instance.md.md).[delete_geometry_edge_face](instance.md.md#('geonodes.core.instance.md',).delete_geometry_edge_face)(self)
```

```python
[Instance](instance.md.md).[delete_geometry_only_face](instance.md.md#('geonodes.core.instance.md',).delete_geometry_only_face)(self)
```

```python
[Instance](instance.md.md).[delete_geometry](instance.md.md#('geonodes.core.instance.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Instance](instance.md.md).[delete_all](instance.md.md#('geonodes.core.instance.md',).delete_all)(self)
```

```python
[Instance](instance.md.md).[delete_edge_face](instance.md.md#('geonodes.core.instance.md',).delete_edge_face)(self)
```

```python
[Instance](instance.md.md).[delete_only_face](instance.md.md#('geonodes.core.instance.md',).delete_only_face)(self)
```

```python
[Instance](instance.md.md).[delete](instance.md.md#('geonodes.core.instance.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

### class Layer

```python
[Layer](layer.md.md).[delete_geometry_all](layer.md.md#('geonodes.core.layer.md',).delete_geometry_all)(self)
```

```python
[Layer](layer.md.md).[delete_geometry_edge_face](layer.md.md#('geonodes.core.layer.md',).delete_geometry_edge_face)(self)
```

```python
[Layer](layer.md.md).[delete_geometry_only_face](layer.md.md#('geonodes.core.layer.md',).delete_geometry_only_face)(self)
```

```python
[Layer](layer.md.md).[delete_geometry](layer.md.md#('geonodes.core.layer.md',).delete_geometry)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

```python
[Layer](layer.md.md).[delete_all](layer.md.md#('geonodes.core.layer.md',).delete_all)(self)
```

```python
[Layer](layer.md.md).[delete_edge_face](layer.md.md#('geonodes.core.layer.md',).delete_edge_face)(self)
```

```python
[Layer](layer.md.md).[delete_only_face](layer.md.md#('geonodes.core.layer.md',).delete_only_face)(self)
```

```python
[Layer](layer.md.md).[delete](layer.md.md#('geonodes.core.layer.md',).delete)(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL')
```

## Dial Gizmo

> `bl_idname` : GeometryNodeGizmoDial

### nd

[nd](nd.md).[dial_gizmo](nd.md#geonodes.core.generated.static_nd.ND.dial_gizmo)(cls,
                    *value: Float,
                    position: Vector = None,
                    up: Vector = None,
                    screen_space: Boolean = None,
                    radius: Float = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY')

### class Float

```python
[Float](float.md.md).[dial_gizmo](float.md.md#('geonodes.core.float.md',).dial_gizmo)(self,
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

[snd](snd.md).[diffuse_bsdf](snd.md#geonodes.core.generated.static_snd.SND.diffuse_bsdf)(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[Diffuse](shader.md.md#('geonodes.core.shader.md',).Diffuse)(cls, color: Color = None, roughness: Float = None, normal: Vector = None)
```

## Displacement

> `bl_idname` : ShaderNodeDisplacement

### snd

[snd](snd.md).[displacement](snd.md#geonodes.core.generated.static_snd.SND.displacement)(cls,
                    height: Float = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT')

### class Float

```python
[Float](float.md.md).[displacement](float.md.md#('geonodes.core.float.md',).displacement)(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    normal: Vector = None,
                    space: Literal['OBJECT', 'WORLD'] = 'OBJECT')
```

## Distribute Points in Grid

> `bl_idname` : GeometryNodeDistributePointsInGrid

### nd

[nd](nd.md).[distribute_points_in_grid](nd.md#geonodes.core.generated.static_nd.ND.distribute_points_in_grid)(cls,
                    grid: Float = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM')

### class Float

```python
[Float](float.md.md).[distribute_points_in_grid_density_random](float.md.md#('geonodes.core.float.md',).distribute_points_in_grid_density_random)(self, density: Float = None, seed: Integer = None)
```

```python
[Float](float.md.md).[distribute_points_in_grid_density_grid](float.md.md#('geonodes.core.float.md',).distribute_points_in_grid_density_grid)(self, spacing: Vector = None, threshold: Float = None)
```

```python
[Float](float.md.md).[distribute_points_in_grid](float.md.md#('geonodes.core.float.md',).distribute_points_in_grid)(self,
                    density: Float = None,
                    seed: Integer = None,
                    mode: Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM')
```

## Distribute Points in Volume

> `bl_idname` : GeometryNodeDistributePointsInVolume

### nd

[nd](nd.md).[distribute_points_in_volume](nd.md#geonodes.core.generated.static_nd.ND.distribute_points_in_volume)(cls,
                    volume: Volume = None,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None)

### class Volume

```python
[Volume](volume.md.md).[distribute_points](volume.md.md#('geonodes.core.volume.md',).distribute_points)(self,
                    mode: Literal['Random', 'Grid'] = None,
                    density: Float = None,
                    seed: Integer = None,
                    spacing: Vector = None,
                    threshold: Float = None)
```

## Distribute Points on Faces

> `bl_idname` : GeometryNodeDistributePointsOnFaces

### nd

[nd](nd.md).[distribute_points_on_faces](nd.md#geonodes.core.generated.static_nd.ND.distribute_points_on_faces)(cls,
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
[Mesh](mesh.md.md).[distribute_points_on_faces](mesh.md.md#('geonodes.core.mesh.md',).distribute_points_on_faces)(self,
                    density: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM')
```

```python
[Mesh](mesh.md.md).[distribute_points_on_faces_random](mesh.md.md#('geonodes.core.mesh.md',).distribute_points_on_faces_random)(self, density: Float = None, seed: Integer = None)
```

```python
[Mesh](mesh.md.md).[distribute_points_on_faces_poisson](mesh.md.md#('geonodes.core.mesh.md',).distribute_points_on_faces_poisson)(self,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None)
```

### class Face

```python
[Face](face.md.md).[distribute_points](face.md.md#('geonodes.core.face.md',).distribute_points)(self,
                    density: Float = None,
                    seed: Integer = None,
                    distribute_method: Literal['RANDOM', 'POISSON'] = 'RANDOM')
```

```python
[Face](face.md.md).[distribute_points_random](face.md.md#('geonodes.core.face.md',).distribute_points_random)(self, density: Float = None, seed: Integer = None)
```

```python
[Face](face.md.md).[distribute_points_poisson](face.md.md#('geonodes.core.face.md',).distribute_points_poisson)(self,
                    distance_min: Float = None,
                    density_max: Float = None,
                    density_factor: Float = None,
                    seed: Integer = None)
```

## Domain Size

> `bl_idname` : GeometryNodeAttributeDomainSize

### nd

[nd](nd.md).[domain_size](nd.md#geonodes.core.generated.static_nd.ND.domain_size)(cls,
                    geometry: Geometry = None,
                    component: Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL'] = 'MESH')

### class Mesh

```python
[Mesh](mesh.md.md).[domain_size](mesh.md.md#('geonodes.core.mesh.md',).domain_size)(self)
```

### class Curve

```python
[Curve](curve.md.md).[domain_size](curve.md.md#('geonodes.core.curve.md',).domain_size)(self)
```

### class Cloud

```python
[Cloud](cloud.md.md).[domain_size](cloud.md.md#('geonodes.core.cloud.md',).domain_size)(self)
```

### class Instances

```python
[Instances](instances.md.md).[domain_size](instances.md.md#('geonodes.core.instances.md',).domain_size)(self)
```

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[domain_size](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).domain_size)(self)
```

## Dual Mesh

> `bl_idname` : GeometryNodeDualMesh

### nd

[nd](nd.md).[dual_mesh](nd.md#geonodes.core.generated.static_nd.ND.dual_mesh)(cls, mesh: Mesh = None, keep_boundaries: Boolean = None)

### class Mesh

```python
[Mesh](mesh.md.md).[dual](mesh.md.md#('geonodes.core.mesh.md',).dual)(self, keep_boundaries: Boolean = None)
```

## Duplicate Elements

> `bl_idname` : GeometryNodeDuplicateElements

### nd

[nd](nd.md).[duplicate_elements](nd.md#geonodes.core.generated.static_nd.ND.duplicate_elements)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    amount: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE'] = 'POINT')

### class Point

```python
[Point](point.md.md).[duplicate](point.md.md#('geonodes.core.point.md',).duplicate)(self, amount: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[duplicate](edge.md.md#('geonodes.core.edge.md',).duplicate)(self, amount: Integer = None)
```

### class Face

```python
[Face](face.md.md).[duplicate](face.md.md#('geonodes.core.face.md',).duplicate)(self, amount: Integer = None)
```

### class Spline

```python
[Spline](spline.md.md).[duplicate](spline.md.md#('geonodes.core.spline.md',).duplicate)(self, amount: Integer = None)
```

### class Layer

```python
[Layer](layer.md.md).[duplicate](layer.md.md#('geonodes.core.layer.md',).duplicate)(self, amount: Integer = None)
```

### class Instance

```python
[Instance](instance.md.md).[duplicate](instance.md.md#('geonodes.core.instance.md',).duplicate)(self, amount: Integer = None)
```

## Edge Angle

> `bl_idname` : GeometryNodeInputMeshEdgeAngle

### nd

[nd](nd.md).[edge_angle](nd.md#geonodes.core.generated.static_nd.ND.edge_angle)(cls)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[edge_angle](mesh.md.md#('geonodes.core.mesh.md',).edge_angle)
```

```python
prop = [Mesh](mesh.md.md).[unsigned_edge_angle](mesh.md.md#('geonodes.core.mesh.md',).unsigned_edge_angle)
```

```python
prop = [Mesh](mesh.md.md).[signed_edge_angle](mesh.md.md#('geonodes.core.mesh.md',).signed_edge_angle)
```

### class Edge

```python
prop = [Edge](edge.md.md).[edge_angle](edge.md.md#('geonodes.core.edge.md',).edge_angle)
```

```python
prop = [Edge](edge.md.md).[unsigned_angle](edge.md.md#('geonodes.core.edge.md',).unsigned_angle)
```

```python
prop = [Edge](edge.md.md).[signed_angle](edge.md.md#('geonodes.core.edge.md',).signed_angle)
```

## Edge Neighbors

> `bl_idname` : GeometryNodeInputMeshEdgeNeighbors

### nd

[nd](nd.md).[edge_neighbors](nd.md#geonodes.core.generated.static_nd.ND.edge_neighbors)(self)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[edge_neighbors](mesh.md.md#('geonodes.core.mesh.md',).edge_neighbors)
```

### class Edge

```python
prop = [Edge](edge.md.md).[face_count](edge.md.md#('geonodes.core.edge.md',).face_count)
```

## Edge Paths to Curves

> `bl_idname` : GeometryNodeEdgePathsToCurves

### nd

[nd](nd.md).[edge_paths_to_curves](nd.md#geonodes.core.generated.static_nd.ND.edge_paths_to_curves)(cls,
                    mesh: Mesh = None,
                    start_vertices: Boolean = None,
                    next_vertex_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[edge_paths_to_curves](mesh.md.md#('geonodes.core.mesh.md',).edge_paths_to_curves)(self, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[paths_to_curves](edge.md.md#('geonodes.core.edge.md',).paths_to_curves)(self, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

## Edge Paths to Selection

> `bl_idname` : GeometryNodeEdgePathsToSelection

### nd

[nd](nd.md).[edge_paths_to_selection](nd.md#geonodes.core.generated.static_nd.ND.edge_paths_to_selection)(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[edge_paths_to_selection](mesh.md.md#('geonodes.core.mesh.md',).edge_paths_to_selection)(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[paths_to_selection](edge.md.md#('geonodes.core.edge.md',).paths_to_selection)(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None)
```

## Edge Vertices

> `bl_idname` : GeometryNodeInputMeshEdgeVertices

### nd

[nd](nd.md).[edge_vertices](nd.md#geonodes.core.generated.static_nd.ND.edge_vertices)(cls)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[edge_vertices](mesh.md.md#('geonodes.core.mesh.md',).edge_vertices)
```

### class Edge

```python
prop = [Edge](edge.md.md).[edge_vertices](edge.md.md#('geonodes.core.edge.md',).edge_vertices)
```

```python
prop = [Edge](edge.md.md).[vertex_index_1](edge.md.md#('geonodes.core.edge.md',).vertex_index_1)
```

```python
prop = [Edge](edge.md.md).[vertex_index_2](edge.md.md#('geonodes.core.edge.md',).vertex_index_2)
```

```python
prop = [Edge](edge.md.md).[position_1](edge.md.md#('geonodes.core.edge.md',).position_1)
```

```python
prop = [Edge](edge.md.md).[position_2](edge.md.md#('geonodes.core.edge.md',).position_2)
```

## Edges of Corner

> `bl_idname` : GeometryNodeEdgesOfCorner

### nd

[nd](nd.md).[edges_of_corner](nd.md#geonodes.core.generated.static_nd.ND.edges_of_corner)(cls, corner_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[edges_of_corner](mesh.md.md#('geonodes.core.mesh.md',).edges_of_corner)(cls, corner_index: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[edges](corner.md.md#('geonodes.core.corner.md',).edges)(cls, corner_index: Integer = None)
```

```python
[Corner](corner.md.md).[next_edge_index](corner.md.md#('geonodes.core.corner.md',).next_edge_index)(cls, corner_index: Integer = None)
```

```python
[Corner](corner.md.md).[previous_edge_index](corner.md.md#('geonodes.core.corner.md',).previous_edge_index)(cls, corner_index: Integer = None)
```

## Edges of Vertex

> `bl_idname` : GeometryNodeEdgesOfVertex

### nd

[nd](nd.md).[edges_of_vertex](nd.md#geonodes.core.generated.static_nd.ND.edges_of_vertex)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[edges_of_vertex](mesh.md.md#('geonodes.core.mesh.md',).edges_of_vertex)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Vertex

```python
[Vertex](vertex.md.md).[edges](vertex.md.md#('geonodes.core.vertex.md',).edges)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Vertex](vertex.md.md).[edge_index](vertex.md.md#('geonodes.core.vertex.md',).edge_index)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Vertex](vertex.md.md).[edges_total](vertex.md.md#('geonodes.core.vertex.md',).edges_total)(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Edges to Face Groups

> `bl_idname` : GeometryNodeEdgesToFaceGroups

### nd

[nd](nd.md).[edges_to_face_groups](nd.md#geonodes.core.generated.static_nd.ND.edges_to_face_groups)(cls, boundary_edges: Boolean = None)

### class Mesh

```python
[Mesh](mesh.md.md).[edges_to_face_groups](mesh.md.md#('geonodes.core.mesh.md',).edges_to_face_groups)(cls, boundary_edges: Boolean = None)
```

### class Edge

```python
[Edge](edge.md.md).[to_face_groups](edge.md.md#('geonodes.core.edge.md',).to_face_groups)(cls, boundary_edges: Boolean = None)
```

## Emission

> `bl_idname` : ShaderNodeEmission

### snd

[snd](snd.md).[emission](snd.md#geonodes.core.generated.static_snd.SND.emission)(cls, color: Color = None, strength: Float = None, weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[Emission](shader.md.md#('geonodes.core.shader.md',).Emission)(cls, color: Color = None, strength: Float = None)
```

## Enable Output

> `bl_idname` : NodeEnableOutput

### nd

[nd](nd.md).[enable_output](nd.md#geonodes.core.generated.static_nd.ND.enable_output)(cls,
                    enable: Boolean = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[enable_output](float.md.md#('geonodes.core.float.md',).enable_output)(self, enable: Boolean = None)
```

### class Integer

```python
[Integer](integer.md.md).[enable_output](integer.md.md#('geonodes.core.integer.md',).enable_output)(self, enable: Boolean = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[enable_output](boolean.md.md#('geonodes.core.boolean.md',).enable_output)(self, enable: Boolean = None)
```

### class Vector

```python
[Vector](vector.md.md).[enable_output](vector.md.md#('geonodes.core.vector.md',).enable_output)(self, enable: Boolean = None)
```

### class Color

```python
[Color](color.md.md).[enable_output](color.md.md#('geonodes.core.color.md',).enable_output)(self, enable: Boolean = None)
```

### class Rotation

```python
[Rotation](rotation.md.md).[enable_output](rotation.md.md#('geonodes.core.rotation.md',).enable_output)(self, enable: Boolean = None)
```

### class Matrix

```python
[Matrix](matrix.md.md).[enable_output](matrix.md.md#('geonodes.core.matrix.md',).enable_output)(self, enable: Boolean = None)
```

### class String

```python
[String](string.md.md).[enable_output](string.md.md#('geonodes.core.string.md',).enable_output)(self, enable: Boolean = None)
```

### class Menu

```python
[Menu](menu.md.md).[enable_output](menu.md.md#('geonodes.core.menu.md',).enable_output)(self, enable: Boolean = None)
```

### class Object

```python
[Object](object.md.md).[enable_output](object.md.md#('geonodes.core.object.md',).enable_output)(self, enable: Boolean = None)
```

### class Image

```python
[Image](image.md.md).[enable_output](image.md.md#('geonodes.core.image.md',).enable_output)(self, enable: Boolean = None)
```

### class Geometry

```python
[Geometry](geometry.md.md).[enable_output](geometry.md.md#('geonodes.core.geometry.md',).enable_output)(self, enable: Boolean = None)
```

### class Collection

```python
[Collection](collection.md.md).[enable_output](collection.md.md#('geonodes.core.collection.md',).enable_output)(self, enable: Boolean = None)
```

### class Material

```python
[Material](material.md.md).[enable_output](material.md.md#('geonodes.core.material.md',).enable_output)(self, enable: Boolean = None)
```

### class Bundle

```python
[Bundle](bundle.md.md).[enable_output](bundle.md.md#('geonodes.core.bundle.md',).enable_output)(self, enable: Boolean = None)
```

### class Closure

```python
[Closure](closure.md.md).[enable_output](closure.md.md#('geonodes.core.closure.md',).enable_output)(self, enable: Boolean = None)
```

### class Font

```python
[Font](font.md.md).[enable_output](font.md.md#('geonodes.core.font.md',).enable_output)(self, enable: Boolean = None)
```

## Endpoint Selection

> `bl_idname` : GeometryNodeCurveEndpointSelection

### nd

[nd](nd.md).[endpoint_selection](nd.md#geonodes.core.generated.static_nd.ND.endpoint_selection)(cls, start_size: Integer = None, end_size: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[endpoint_selection](curve.md.md#('geonodes.core.curve.md',).endpoint_selection)(cls, start_size: Integer = None, end_size: Integer = None)
```

## Environment Texture

> `bl_idname` : ShaderNodeTexEnvironment

### snd

[snd](snd.md).[environment_texture](snd.md#geonodes.core.generated.static_snd.SND.environment_texture)(cls,
                    vector: Vector = None,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR')

### class Vector

```python
[Vector](vector.md.md).[environment_texture](vector.md.md#('geonodes.core.vector.md',).environment_texture)(self,
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR')
```

## Euler to Rotation

> `bl_idname` : FunctionNodeEulerToRotation

### nd

[nd](nd.md).[euler_to_rotation](nd.md#geonodes.core.generated.static_nd.ND.euler_to_rotation)(cls, euler: Vector = None)

### class Rotation

```python
[Rotation](rotation.md.md).[FromEuler](rotation.md.md#('geonodes.core.rotation.md',).FromEuler)(cls, euler: Vector = None)
```

### class Vector

```python
[Vector](vector.md.md).[to_rotation](vector.md.md#('geonodes.core.vector.md',).to_rotation)(self)
```

## Evaluate Closure

> `bl_idname` : NodeEvaluateClosure

### nd

[nd](nd.md).[evaluate_closure](nd.md#geonodes.core.generated.static_nd.ND.evaluate_closure)(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False)

### snd

[snd](snd.md).[evaluate_closure](snd.md#geonodes.core.generated.static_snd.SND.evaluate_closure)(cls,
                    closure: Closure = None,
                    active_input_index = 0,
                    active_output_index = 0,
                    define_signature = False)

## Evaluate at Index

> `bl_idname` : GeometryNodeFieldAtIndex

### nd

[nd](nd.md).[evaluate_at_index](nd.md#geonodes.core.generated.static_nd.ND.evaluate_at_index)(cls,
                    value: Float = None,
                    index: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[evaluate_at_index](point.md.md#('geonodes.core.point.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[evaluate_at_index](edge.md.md#('geonodes.core.edge.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Face

```python
[Face](face.md.md).[evaluate_at_index](face.md.md#('geonodes.core.face.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[evaluate_at_index](corner.md.md#('geonodes.core.corner.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Spline

```python
[Spline](spline.md.md).[evaluate_at_index](spline.md.md#('geonodes.core.spline.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Instance

```python
[Instance](instance.md.md).[evaluate_at_index](instance.md.md#('geonodes.core.instance.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

### class Layer

```python
[Layer](layer.md.md).[evaluate_at_index](layer.md.md#('geonodes.core.layer.md',).evaluate_at_index)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None)
```

## Evaluate on Domain

> `bl_idname` : GeometryNodeFieldOnDomain

### nd

[nd](nd.md).[evaluate_on_domain](nd.md#geonodes.core.generated.static_nd.ND.evaluate_on_domain)(cls,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[evaluate_on_domain](point.md.md#('geonodes.core.point.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Edge

```python
[Edge](edge.md.md).[evaluate_on_domain](edge.md.md#('geonodes.core.edge.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Face

```python
[Face](face.md.md).[evaluate_on_domain](face.md.md#('geonodes.core.face.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Corner

```python
[Corner](corner.md.md).[evaluate_on_domain](corner.md.md#('geonodes.core.corner.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Spline

```python
[Spline](spline.md.md).[evaluate_on_domain](spline.md.md#('geonodes.core.spline.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Instance

```python
[Instance](instance.md.md).[evaluate_on_domain](instance.md.md#('geonodes.core.instance.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

### class Layer

```python
[Layer](layer.md.md).[evaluate_on_domain](layer.md.md#('geonodes.core.layer.md',).evaluate_on_domain)(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None)
```

## Extrude Mesh

> `bl_idname` : GeometryNodeExtrudeMesh

### nd

[nd](nd.md).[extrude_mesh](nd.md#geonodes.core.generated.static_nd.ND.extrude_mesh)(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES')

### class Mesh

```python
[Mesh](mesh.md.md).[extrude_vertices](mesh.md.md#('geonodes.core.mesh.md',).extrude_vertices)(self, offset: Vector = None, offset_scale: Float = None)
```

```python
[Mesh](mesh.md.md).[extrude_edges](mesh.md.md#('geonodes.core.mesh.md',).extrude_edges)(self, offset: Vector = None, offset_scale: Float = None)
```

```python
[Mesh](mesh.md.md).[extrude_faces](mesh.md.md#('geonodes.core.mesh.md',).extrude_faces)(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None)
```

```python
[Mesh](mesh.md.md).[extrude](mesh.md.md#('geonodes.core.mesh.md',).extrude)(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES')
```

### class Vertex

```python
[Vertex](vertex.md.md).[extrude](vertex.md.md#('geonodes.core.vertex.md',).extrude)(self, offset: Vector = None, offset_scale: Float = None)
```

### class Edge

```python
[Edge](edge.md.md).[extrude](edge.md.md#('geonodes.core.edge.md',).extrude)(self, offset: Vector = None, offset_scale: Float = None)
```

### class Face

```python
[Face](face.md.md).[extrude](face.md.md#('geonodes.core.face.md',).extrude)(self,
                    offset: Vector = None,
                    offset_scale: Float = None,
                    individual: Boolean = None)
```

## Face Area

> `bl_idname` : GeometryNodeInputMeshFaceArea

### nd

[nd](nd.md).[face_area](nd.md#geonodes.core.generated.static_nd.ND.face_area)(self)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[face_area](mesh.md.md#('geonodes.core.mesh.md',).face_area)
```

### class Face

```python
prop = [Face](face.md.md).[area](face.md.md#('geonodes.core.face.md',).area)
```

## Face Group Boundaries

> `bl_idname` : GeometryNodeMeshFaceSetBoundaries

### nd

[nd](nd.md).[face_group_boundaries](nd.md#geonodes.core.generated.static_nd.ND.face_group_boundaries)(cls, face_group_id: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[face_group_boundaries](mesh.md.md#('geonodes.core.mesh.md',).face_group_boundaries)(cls, face_group_id: Integer = None)
```

## Face Neighbors

> `bl_idname` : GeometryNodeInputMeshFaceNeighbors

### nd

[nd](nd.md).[face_neighbors](nd.md#geonodes.core.generated.static_nd.ND.face_neighbors)(cls)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[face_neighbors](mesh.md.md#('geonodes.core.mesh.md',).face_neighbors)
```

### class Face

```python
prop = [Face](face.md.md).[neighbors](face.md.md#('geonodes.core.face.md',).neighbors)
```

```python
prop = [Face](face.md.md).[neighbors_vertex_count](face.md.md#('geonodes.core.face.md',).neighbors_vertex_count)
```

```python
prop = [Face](face.md.md).[neighbors_face_count](face.md.md#('geonodes.core.face.md',).neighbors_face_count)
```

## Face Set

> `bl_idname` : GeometryNodeToolFaceSet

### nd

[nd](nd.md).[face_set](nd.md#geonodes.core.generated.static_nd.ND.face_set)(cls)

## Face of Corner

> `bl_idname` : GeometryNodeFaceOfCorner

### nd

[nd](nd.md).[face_of_corner](nd.md#geonodes.core.generated.static_nd.ND.face_of_corner)(cls, corner_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[face_of_corner](mesh.md.md#('geonodes.core.mesh.md',).face_of_corner)(cls, corner_index: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[face](corner.md.md#('geonodes.core.corner.md',).face)(cls, corner_index: Integer = None)
```

```python
[Corner](corner.md.md).[face_index](corner.md.md#('geonodes.core.corner.md',).face_index)(cls, corner_index: Integer = None)
```

```python
[Corner](corner.md.md).[index_in_face](corner.md.md#('geonodes.core.corner.md',).index_in_face)(cls, corner_index: Integer = None)
```

## Field Average

> `bl_idname` : GeometryNodeFieldAverage

### nd

[nd](nd.md).[field_average](nd.md#geonodes.core.generated.static_nd.ND.field_average)(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[field_average](point.md.md#('geonodes.core.point.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
[Edge](edge.md.md).[field_average](edge.md.md#('geonodes.core.edge.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
[Face](face.md.md).[field_average](face.md.md#('geonodes.core.face.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
[Corner](corner.md.md).[field_average](corner.md.md#('geonodes.core.corner.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
[Spline](spline.md.md).[field_average](spline.md.md#('geonodes.core.spline.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
[Instance](instance.md.md).[field_average](instance.md.md#('geonodes.core.instance.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
[Layer](layer.md.md).[field_average](layer.md.md#('geonodes.core.layer.md',).field_average)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field Min & Max

> `bl_idname` : GeometryNodeFieldMinAndMax

### nd

[nd](nd.md).[field_min_max](nd.md#geonodes.core.generated.static_nd.ND.field_min_max)(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[field_min_max](point.md.md#('geonodes.core.point.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
[Edge](edge.md.md).[field_min_max](edge.md.md#('geonodes.core.edge.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
[Face](face.md.md).[field_min_max](face.md.md#('geonodes.core.face.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
[Corner](corner.md.md).[field_min_max](corner.md.md#('geonodes.core.corner.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
[Spline](spline.md.md).[field_min_max](spline.md.md#('geonodes.core.spline.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
[Instance](instance.md.md).[field_min_max](instance.md.md#('geonodes.core.instance.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
[Layer](layer.md.md).[field_min_max](layer.md.md#('geonodes.core.layer.md',).field_min_max)(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field Variance

> `bl_idname` : GeometryNodeFieldVariance

### nd

[nd](nd.md).[field_variance](nd.md#geonodes.core.generated.static_nd.ND.field_variance)(cls,
                    value: Float = None,
                    group_id: Integer = None,
                    data_type: Literal['FLOAT', 'FLOAT_VECTOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[field_variance](point.md.md#('geonodes.core.point.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Edge

```python
[Edge](edge.md.md).[field_variance](edge.md.md#('geonodes.core.edge.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Face

```python
[Face](face.md.md).[field_variance](face.md.md#('geonodes.core.face.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Corner

```python
[Corner](corner.md.md).[field_variance](corner.md.md#('geonodes.core.corner.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Spline

```python
[Spline](spline.md.md).[field_variance](spline.md.md#('geonodes.core.spline.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Instance

```python
[Instance](instance.md.md).[field_variance](instance.md.md#('geonodes.core.instance.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

### class Layer

```python
[Layer](layer.md.md).[field_variance](layer.md.md#('geonodes.core.layer.md',).field_variance)(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')
```

## Field to Grid

> `bl_idname` : GeometryNodeFieldToGrid

### nd

[nd](nd.md).[field_to_grid](nd.md#geonodes.core.generated.static_nd.ND.field_to_grid)(cls,
                    named_sockets: dict = {},
                    topology: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT',
                    **sockets)

### class Float

```python
[Float](float.md.md).[field_to_grid](float.md.md#('geonodes.core.float.md',).field_to_grid)(self, named_sockets: dict = {}, **sockets)
```

### class Integer

```python
[Integer](integer.md.md).[field_to_grid](integer.md.md#('geonodes.core.integer.md',).field_to_grid)(self, named_sockets: dict = {}, **sockets)
```

### class Boolean

```python
[Boolean](boolean.md.md).[field_to_grid](boolean.md.md#('geonodes.core.boolean.md',).field_to_grid)(self, named_sockets: dict = {}, **sockets)
```

### class Vector

```python
[Vector](vector.md.md).[field_to_grid](vector.md.md#('geonodes.core.vector.md',).field_to_grid)(self, named_sockets: dict = {}, **sockets)
```

## Field to List

> `bl_idname` : GeometryNodeFieldToList

### nd

[nd](nd.md).[field_to_list](nd.md#geonodes.core.generated.static_nd.ND.field_to_list)(cls, named_sockets: dict = {}, count: Integer = None, **sockets)

## Fill Curve

> `bl_idname` : GeometryNodeFillCurve

### nd

[nd](nd.md).[fill_curve](nd.md#geonodes.core.generated.static_nd.ND.fill_curve)(cls,
                    curve: Curve = None,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None,
                    fill_rule: Literal['Even-Odd', 'Non-Zero'] = None)

### class Curve

```python
[Curve](curve.md.md).[fill](curve.md.md#('geonodes.core.curve.md',).fill)(self,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None,
                    fill_rule: Literal['Even-Odd', 'Non-Zero'] = None)
```

## Fillet Curve

> `bl_idname` : GeometryNodeFilletCurve

### nd

[nd](nd.md).[fillet_curve](nd.md#geonodes.core.generated.static_nd.ND.fillet_curve)(cls,
                    curve: Curve = None,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[fillet](curve.md.md#('geonodes.core.curve.md',).fillet)(self,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None)
```

## Find in String

> `bl_idname` : FunctionNodeFindInString

### nd

[nd](nd.md).[find_in_string](nd.md#geonodes.core.generated.static_nd.ND.find_in_string)(cls, string: String = None, search: String = None)

### class String

```python
[String](string.md.md).[find_in_string](string.md.md#('geonodes.core.string.md',).find_in_string)(self, search: String = None)
```

```python
[String](string.md.md).[find](string.md.md#('geonodes.core.string.md',).find)(self, search: String = None)
```

## Flip Faces

> `bl_idname` : GeometryNodeFlipFaces

### nd

[nd](nd.md).[flip_faces](nd.md#geonodes.core.generated.static_nd.ND.flip_faces)(cls, mesh: Mesh = None, selection: Boolean = None)

### class Mesh

```python
[Mesh](mesh.md.md).[flip_faces](mesh.md.md#('geonodes.core.mesh.md',).flip_faces)(self)
```

## Float Curve

> `bl_idname` : ShaderNodeFloatCurve

### nd

[nd](nd.md).[float_curve](nd.md#geonodes.core.generated.static_nd.ND.float_curve)(cls, value: Float = None, factor: Float = None)

### snd

[snd](snd.md).[float_curve](snd.md#geonodes.core.generated.static_snd.SND.float_curve)(cls, value: Float = None, factor: Float = None)

## Float to Integer

> `bl_idname` : FunctionNodeFloatToInt

### nd

[nd](nd.md).[float_to_integer](nd.md#geonodes.core.generated.static_nd.ND.float_to_integer)(cls,
                    float: Float = None,
                    rounding_mode: Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND')

### class Float

```python
[Float](float.md.md).[to_integer](float.md.md#('geonodes.core.float.md',).to_integer)(self,
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

[nd](nd.md).[format_string](nd.md#geonodes.core.generated.static_nd.ND.format_string)(cls, named_sockets: dict = {}, format: String = None, **sockets)

### class String

```python
[String](string.md.md).[format](string.md.md#('geonodes.core.string.md',).format)(self, named_sockets: dict = {}, **sockets)
```

```python
[String](string.md.md).[Format](string.md.md#('geonodes.core.string.md',).Format)(cls, named_sockets: dict = {}, format: String = None, **sockets)
```

## Frame

> `bl_idname` : NodeFrame

### class Layout

## Fresnel

> `bl_idname` : ShaderNodeFresnel

### snd

[snd](snd.md).[fresnel](snd.md#geonodes.core.generated.static_snd.SND.fresnel)(cls, ior: Float = None, normal: Vector = None)

### class Float

```python
[Float](float.md.md).[fresnel](float.md.md#('geonodes.core.float.md',).fresnel)(self, normal: Vector = None)
```

## Gabor Texture

> `bl_idname` : ShaderNodeTexGabor

### nd

[nd](nd.md).[gabor_texture](nd.md#geonodes.core.generated.static_nd.ND.gabor_texture)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D')

### snd

[snd](snd.md).[gabor_texture](snd.md#geonodes.core.generated.static_snd.SND.gabor_texture)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    orientation_1: Vector = None,
                    gabor_type: Literal['2D', '3D'] = '2D')

### class Float

```python
[Float](float.md.md).[Gabor](float.md.md#('geonodes.core.float.md',).Gabor)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    frequency: Float = None,
                    anisotropy: Float = None,
                    orientation: Float = None,
                    gabor_type: Literal['2D', '3D'] = '2D')
```

### class Texture

```python
[Texture](texture.md.md).[Gabor](texture.md.md#('geonodes.core.texture.md',).Gabor)(cls,
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

[nd](nd.md).[gamma](nd.md#geonodes.core.generated.static_nd.ND.gamma)(cls, color: Color = None, gamma: Float = None)

### snd

[snd](snd.md).[gamma](snd.md#geonodes.core.generated.static_snd.SND.gamma)(cls, color: Color = None, gamma: Float = None)

### class Color

```python
[Color](color.md.md).[gamma](color.md.md#('geonodes.core.color.md',).gamma)(self, gamma: Float = None)
```

## Geometry

> `bl_idname` : ShaderNodeNewGeometry

### snd

[snd](snd.md).[geometry](snd.md#geonodes.core.generated.static_snd.SND.geometry)(cls)

## Geometry Proximity

> `bl_idname` : GeometryNodeProximity

### nd

[nd](nd.md).[geometry_proximity](nd.md#geonodes.core.generated.static_nd.ND.geometry_proximity)(cls,
                    geometry: Geometry = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES')

### class Geometry

```python
[Geometry](geometry.md.md).[proximity](geometry.md.md#('geonodes.core.geometry.md',).proximity)(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES')
```

```python
[Geometry](geometry.md.md).[proximity_points](geometry.md.md#('geonodes.core.geometry.md',).proximity_points)(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

```python
[Geometry](geometry.md.md).[proximity_edges](geometry.md.md#('geonodes.core.geometry.md',).proximity_edges)(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

```python
[Geometry](geometry.md.md).[proximity_faces](geometry.md.md#('geonodes.core.geometry.md',).proximity_faces)(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

## Geometry to Instance

> `bl_idname` : GeometryNodeGeometryToInstance

### nd

[nd](nd.md).[geometry_to_instance](nd.md#geonodes.core.generated.static_nd.ND.geometry_to_instance)(cls, *geometry: Geometry)

### class Geometry

```python
[Geometry](geometry.md.md).[to_instance](geometry.md.md#('geonodes.core.geometry.md',).to_instance)(self, *geometry: Geometry)
```

### class Instances

```python
[Instances](instances.md.md).[FromGeometry](instances.md.md#('geonodes.core.instances.md',).FromGeometry)(cls, *geometry: Geometry)
```

## Get Bundle Item

> `bl_idname` : NodeGetBundleItem

### nd

[nd](nd.md).[get_bundle_item](nd.md#geonodes.core.generated.static_nd.ND.get_bundle_item)(cls,
                    bundle: Bundle = None,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

### class Bundle

```python
[Bundle](bundle.md.md).[get_item](bundle.md.md#('geonodes.core.bundle.md',).get_item)(self,
                    path: String = None,
                    remove: Boolean = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

## Get Geometry Bundle

> `bl_idname` : GeometryNodeGetGeometryBundle

### nd

[nd](nd.md).[get_geometry_bundle](nd.md#geonodes.core.generated.static_nd.ND.get_geometry_bundle)(cls, geometry: Geometry = None, remove: Boolean = None)

## Get List Item

> `bl_idname` : GeometryNodeListGetItem

### nd

[nd](nd.md).[get_list_item](nd.md#geonodes.core.generated.static_nd.ND.get_list_item)(cls,
                    list: Float = None,
                    index: Integer = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

## Get Named Grid

> `bl_idname` : GeometryNodeGetNamedGrid

### nd

[nd](nd.md).[get_named_grid](nd.md#geonodes.core.generated.static_nd.ND.get_named_grid)(cls,
                    volume: Volume = None,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Volume

```python
[Volume](volume.md.md).[get_named_grid](volume.md.md#('geonodes.core.volume.md',).get_named_grid)(self,
                    name: String = None,
                    remove: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')
```

## Glass BSDF

> `bl_idname` : ShaderNodeBsdfGlass

### snd

[snd](snd.md).[glass_bsdf](snd.md#geonodes.core.generated.static_snd.SND.glass_bsdf)(cls,
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
[Shader](shader.md.md).[Glass](shader.md.md#('geonodes.core.shader.md',).Glass)(cls,
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

[snd](snd.md).[glossy_bsdf](snd.md#geonodes.core.generated.static_snd.SND.glossy_bsdf)(cls,
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
[Shader](shader.md.md).[Glossy](shader.md.md#('geonodes.core.shader.md',).Glossy)(cls,
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

[nd](nd.md).[gradient_texture](nd.md#geonodes.core.generated.static_nd.ND.gradient_texture)(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')

### snd

[snd](snd.md).[gradient_texture](snd.md#geonodes.core.generated.static_snd.SND.gradient_texture)(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')

### class Color

```python
[Color](color.md.md).[Gradient](color.md.md#('geonodes.core.color.md',).Gradient)(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')
```

### class Texture

```python
[Texture](texture.md.md).[Gradient](texture.md.md#('geonodes.core.texture.md',).Gradient)(cls,
                    vector: Vector = None,
                    gradient_type: Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR')
```

## Grease Pencil to Curves

> `bl_idname` : GeometryNodeGreasePencilToCurves

### nd

[nd](nd.md).[grease_pencil_to_curves](nd.md#geonodes.core.generated.static_nd.ND.grease_pencil_to_curves)(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    layers_as_instances: Boolean = None)

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[to_curves](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).to_curves)(self, layers_as_instances: Boolean = None)
```

## Grid

> `bl_idname` : GeometryNodeMeshGrid

### nd

[nd](nd.md).[grid](nd.md#geonodes.core.generated.static_nd.ND.grid)(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[Grid](mesh.md.md#('geonodes.core.mesh.md',).Grid)(cls,
                    size_x: Float = None,
                    size_y: Float = None,
                    vertices_x: Integer = None,
                    vertices_y: Integer = None)
```

## Grid Curl

> `bl_idname` : GeometryNodeGridCurl

### nd

[nd](nd.md).[grid_curl](nd.md#geonodes.core.generated.static_nd.ND.grid_curl)(cls, grid: Vector = None)

### class Vector

```python
[Vector](vector.md.md).[grid_curl](vector.md.md#('geonodes.core.vector.md',).grid_curl)(self)
```

## Grid Dilate & Erode

> `bl_idname` : GeometryNodeGridDilateAndErode

### nd

[nd](nd.md).[grid_dilate_erode](nd.md#geonodes.core.generated.static_nd.ND.grid_dilate_erode)(cls,
                    grid: Float = None,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[grid_dilate_erode](float.md.md#('geonodes.core.float.md',).grid_dilate_erode)(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[grid_dilate_erode](integer.md.md#('geonodes.core.integer.md',).grid_dilate_erode)(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[grid_dilate_erode](boolean.md.md#('geonodes.core.boolean.md',).grid_dilate_erode)(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[grid_dilate_erode](vector.md.md#('geonodes.core.vector.md',).grid_dilate_erode)(self,
                    connectivity: Literal['Face', 'Edge', 'Vertex'] = None,
                    tiles: Literal['Ignore', 'Expand', 'Preserve'] = None,
                    steps: Integer = None)
```

## Grid Divergence

> `bl_idname` : GeometryNodeGridDivergence

### nd

[nd](nd.md).[grid_divergence](nd.md#geonodes.core.generated.static_nd.ND.grid_divergence)(cls, grid: Vector = None)

### class Vector

```python
[Vector](vector.md.md).[grid_divergence](vector.md.md#('geonodes.core.vector.md',).grid_divergence)(self)
```

## Grid Gradient

> `bl_idname` : GeometryNodeGridGradient

### nd

[nd](nd.md).[grid_gradient](nd.md#geonodes.core.generated.static_nd.ND.grid_gradient)(cls, grid: Float = None)

### class Float

```python
[Float](float.md.md).[grid_gradient](float.md.md#('geonodes.core.float.md',).grid_gradient)(self)
```

## Grid Info

> `bl_idname` : GeometryNodeGridInfo

### nd

[nd](nd.md).[grid_info](nd.md#geonodes.core.generated.static_nd.ND.grid_info)(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[grid_info](float.md.md#('geonodes.core.float.md',).grid_info)(self)
```

### class Integer

```python
[Integer](integer.md.md).[grid_info](integer.md.md#('geonodes.core.integer.md',).grid_info)(self)
```

### class Boolean

```python
[Boolean](boolean.md.md).[grid_info](boolean.md.md#('geonodes.core.boolean.md',).grid_info)(self)
```

### class Vector

```python
[Vector](vector.md.md).[grid_info](vector.md.md#('geonodes.core.vector.md',).grid_info)(self)
```

## Grid Laplacian

> `bl_idname` : GeometryNodeGridLaplacian

### nd

[nd](nd.md).[grid_laplacian](nd.md#geonodes.core.generated.static_nd.ND.grid_laplacian)(cls, grid: Float = None)

### class Float

```python
[Float](float.md.md).[grid_laplacian](float.md.md#('geonodes.core.float.md',).grid_laplacian)(self)
```

## Grid Mean

> `bl_idname` : GeometryNodeGridMean

### nd

[nd](nd.md).[grid_mean](nd.md#geonodes.core.generated.static_nd.ND.grid_mean)(cls,
                    grid: Float = None,
                    width: Integer = None,
                    iterations: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[grid_mean](float.md.md#('geonodes.core.float.md',).grid_mean)(self, width: Integer = None, iterations: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[grid_mean](integer.md.md#('geonodes.core.integer.md',).grid_mean)(self, width: Integer = None, iterations: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[grid_mean](vector.md.md#('geonodes.core.vector.md',).grid_mean)(self, width: Integer = None, iterations: Integer = None)
```

## Grid Median

> `bl_idname` : GeometryNodeGridMedian

### nd

[nd](nd.md).[grid_median](nd.md#geonodes.core.generated.static_nd.ND.grid_median)(cls,
                    grid: Float = None,
                    width: Integer = None,
                    iterations: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[grid_median](float.md.md#('geonodes.core.float.md',).grid_median)(self, width: Integer = None, iterations: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[grid_median](integer.md.md#('geonodes.core.integer.md',).grid_median)(self, width: Integer = None, iterations: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[grid_median](vector.md.md#('geonodes.core.vector.md',).grid_median)(self, width: Integer = None, iterations: Integer = None)
```

## Grid to Mesh

> `bl_idname` : GeometryNodeGridToMesh

### nd

[nd](nd.md).[grid_to_mesh](nd.md#geonodes.core.generated.static_nd.ND.grid_to_mesh)(cls, grid: Float = None, threshold: Float = None, adaptivity: Float = None)

### class Float

```python
[Float](float.md.md).[grid_to_mesh](float.md.md#('geonodes.core.float.md',).grid_to_mesh)(self, threshold: Float = None, adaptivity: Float = None)
```

## Grid to Points

> `bl_idname` : GeometryNodeGridToPoints

### nd

[nd](nd.md).[grid_to_points](nd.md#geonodes.core.generated.static_nd.ND.grid_to_points)(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[grid_to_points](float.md.md#('geonodes.core.float.md',).grid_to_points)(self)
```

### class Integer

```python
[Integer](integer.md.md).[grid_to_points](integer.md.md#('geonodes.core.integer.md',).grid_to_points)(self)
```

### class Boolean

```python
[Boolean](boolean.md.md).[grid_to_points](boolean.md.md#('geonodes.core.boolean.md',).grid_to_points)(self)
```

### class Vector

```python
[Vector](vector.md.md).[grid_to_points](vector.md.md#('geonodes.core.vector.md',).grid_to_points)(self)
```

## Group

> `bl_idname` : ShaderNodeGroup

### class Group

## Group Input

> `bl_idname` : NodeGroupInput

### nd

[nd](nd.md).[group_input](nd.md#geonodes.core.generated.static_nd.ND.group_input)(self)

### snd

[snd](snd.md).[group_input](snd.md#geonodes.core.generated.static_snd.SND.group_input)(self)

## Group Output

> `bl_idname` : NodeGroupOutput

### nd

[nd](nd.md).[group_output](nd.md#geonodes.core.generated.static_nd.ND.group_output)(cls, is_active_output = True)

### snd

[snd](snd.md).[group_output](snd.md#geonodes.core.generated.static_snd.SND.group_output)(cls, is_active_output = True)

## Hair BSDF

> `bl_idname` : ShaderNodeBsdfHair

### snd

[snd](snd.md).[hair_bsdf](snd.md#geonodes.core.generated.static_snd.SND.hair_bsdf)(cls,
                    color: Color = None,
                    offset: Float = None,
                    roughnessu: Float = None,
                    roughnessv: Float = None,
                    tangent: Vector = None,
                    weight: Float = None,
                    component: Literal['Reflection', 'Transmission'] = 'Reflection')

### class Shader

```python
[Shader](shader.md.md).[Hair](shader.md.md#('geonodes.core.shader.md',).Hair)(cls,
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

[nd](nd.md).[handle_type_selection](nd.md#geonodes.core.generated.static_nd.ND.handle_type_selection)(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})

### class Curve

```python
[Curve](curve.md.md).[handle_type_selection](curve.md.md#('geonodes.core.curve.md',).handle_type_selection)(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})
```

## Hash Value

> `bl_idname` : FunctionNodeHashValue

### nd

[nd](nd.md).[hash_value](nd.md#geonodes.core.generated.static_nd.ND.hash_value)(cls,
                    value: Integer = None,
                    seed: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING'] = 'INT')

### class Float

```python
[Float](float.md.md).[hash_value](float.md.md#('geonodes.core.float.md',).hash_value)(self, seed: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[hash_value](integer.md.md#('geonodes.core.integer.md',).hash_value)(self, seed: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[hash_value](vector.md.md#('geonodes.core.vector.md',).hash_value)(self, seed: Integer = None)
```

### class Color

```python
[Color](color.md.md).[hash_value](color.md.md#('geonodes.core.color.md',).hash_value)(self, seed: Integer = None)
```

### class Rotation

```python
[Rotation](rotation.md.md).[hash_value](rotation.md.md#('geonodes.core.rotation.md',).hash_value)(self, seed: Integer = None)
```

### class Matrix

```python
[Matrix](matrix.md.md).[hash_value](matrix.md.md#('geonodes.core.matrix.md',).hash_value)(self, seed: Integer = None)
```

### class String

```python
[String](string.md.md).[hash_value](string.md.md#('geonodes.core.string.md',).hash_value)(self, seed: Integer = None)
```

## Holdout

> `bl_idname` : ShaderNodeHoldout

### snd

[snd](snd.md).[holdout](snd.md#geonodes.core.generated.static_snd.SND.holdout)(cls, weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[Holdout](shader.md.md#('geonodes.core.shader.md',).Holdout)(cls)
```

## Hue/Saturation/Value

> `bl_idname` : ShaderNodeHueSaturation

### snd

[snd](snd.md).[hue_saturation_value](snd.md#geonodes.core.generated.static_snd.SND.hue_saturation_value)(cls,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None)

### class Float

```python
[Float](float.md.md).[hue_saturation_value](float.md.md#('geonodes.core.float.md',).hue_saturation_value)(self,
                    saturation: Float = None,
                    value: Float = None,
                    color: Color = None,
                    factor: Float = None)
```

### class Color

```python
[Color](color.md.md).[hue_saturation_value](color.md.md#('geonodes.core.color.md',).hue_saturation_value)(self,
                    hue: Float = None,
                    saturation: Float = None,
                    value: Float = None,
                    factor: Float = None)
```

## ID

> `bl_idname` : GeometryNodeInputID

### nd

[nd](nd.md).[id](nd.md#geonodes.core.generated.static_nd.ND.id)(self)

### class Geometry

```python
prop = [Geometry](geometry.md.md).[id](geometry.md.md#('geonodes.core.geometry.md',).id)
```

## IES Texture

> `bl_idname` : ShaderNodeTexIES

### snd

[snd](snd.md).[ies_texture](snd.md#geonodes.core.generated.static_snd.SND.ies_texture)(cls,
                    vector: Vector = None,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL')

### class Vector

```python
[Vector](vector.md.md).[ies_texture_internal](vector.md.md#('geonodes.core.vector.md',).ies_texture_internal)(self, strength: Float = None, filepath = '', ies = None)
```

```python
[Vector](vector.md.md).[ies_texture_external](vector.md.md#('geonodes.core.vector.md',).ies_texture_external)(self, strength: Float = None, filepath = '', ies = None)
```

```python
[Vector](vector.md.md).[ies_texture](vector.md.md#('geonodes.core.vector.md',).ies_texture)(self,
                    strength: Float = None,
                    filepath = '',
                    ies = None,
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL')
```

## Ico Sphere

> `bl_idname` : GeometryNodeMeshIcoSphere

### nd

[nd](nd.md).[ico_sphere](nd.md#geonodes.core.generated.static_nd.ND.ico_sphere)(cls, radius: Float = None, subdivisions: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[IcoSphere](mesh.md.md#('geonodes.core.mesh.md',).IcoSphere)(cls, radius: Float = None, subdivisions: Integer = None)
```

## Image

> `bl_idname` : GeometryNodeInputImage

### nd

[nd](nd.md).[image](nd.md#geonodes.core.generated.static_nd.ND.image)(cls, image = None)

## Image Info

> `bl_idname` : GeometryNodeImageInfo

### nd

[nd](nd.md).[image_info](nd.md#geonodes.core.generated.static_nd.ND.image_info)(cls, image: Image = None, frame: Integer = None)

### class Image

```python
[Image](image.md.md).[info](image.md.md#('geonodes.core.image.md',).info)(self, frame: Integer = None)
```

```python
[Image](image.md.md).[width](image.md.md#('geonodes.core.image.md',).width)(self, frame: Integer = None)
```

```python
[Image](image.md.md).[height](image.md.md#('geonodes.core.image.md',).height)(self, frame: Integer = None)
```

```python
[Image](image.md.md).[has_alpha](image.md.md#('geonodes.core.image.md',).has_alpha)(self, frame: Integer = None)
```

```python
[Image](image.md.md).[frame_count](image.md.md#('geonodes.core.image.md',).frame_count)(self, frame: Integer = None)
```

```python
[Image](image.md.md).[fps](image.md.md#('geonodes.core.image.md',).fps)(self, frame: Integer = None)
```

## Image Texture

> `bl_idname` : ShaderNodeTexImage

### snd

[snd](snd.md).[image_texture](snd.md#geonodes.core.generated.static_snd.SND.image_texture)(cls,
                    vector: Vector = None,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0)

### class Vector

```python
[Vector](vector.md.md).[image_texture](vector.md.md#('geonodes.core.vector.md',).image_texture)(self,
                    extension: Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT',
                    image = None,
                    interpolation: Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear',
                    projection: Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT',
                    projection_blend = 0.0)
```

## Import CSV

> `bl_idname` : GeometryNodeImportCSV

### nd

[nd](nd.md).[import_csv](nd.md#geonodes.core.generated.static_nd.ND.import_csv)(cls, path: String = None, delimiter: String = None)

### class Cloud

```python
[Cloud](cloud.md.md).[ImportCSV](cloud.md.md#('geonodes.core.cloud.md',).ImportCSV)(cls, path: String = None, delimiter: String = None)
```

## Import OBJ

> `bl_idname` : GeometryNodeImportOBJ

### nd

[nd](nd.md).[import_obj](nd.md#geonodes.core.generated.static_nd.ND.import_obj)(cls, path: String = None)

### class Instances

```python
[Instances](instances.md.md).[ImportOBJ](instances.md.md#('geonodes.core.instances.md',).ImportOBJ)(cls, path: String = None)
```

## Import PLY

> `bl_idname` : GeometryNodeImportPLY

### nd

[nd](nd.md).[import_ply](nd.md#geonodes.core.generated.static_nd.ND.import_ply)(cls, path: String = None)

### class Mesh

```python
[Mesh](mesh.md.md).[ImportPLY](mesh.md.md#('geonodes.core.mesh.md',).ImportPLY)(cls, path: String = None)
```

## Import STL

> `bl_idname` : GeometryNodeImportSTL

### nd

[nd](nd.md).[import_stl](nd.md#geonodes.core.generated.static_nd.ND.import_stl)(cls, path: String = None)

### class Mesh

```python
[Mesh](mesh.md.md).[ImportSTL](mesh.md.md#('geonodes.core.mesh.md',).ImportSTL)(cls, path: String = None)
```

## Import Text

> `bl_idname` : GeometryNodeImportText

### nd

[nd](nd.md).[import_text](nd.md#geonodes.core.generated.static_nd.ND.import_text)(cls, path: String = None)

### class String

```python
[String](string.md.md).[ImportText](string.md.md#('geonodes.core.string.md',).ImportText)(cls, path: String = None)
```

## Import VDB

> `bl_idname` : GeometryNodeImportVDB

### nd

[nd](nd.md).[import_vdb](nd.md#geonodes.core.generated.static_nd.ND.import_vdb)(cls, path: String = None)

### class Volume

```python
[Volume](volume.md.md).[ImportVDB](volume.md.md#('geonodes.core.volume.md',).ImportVDB)(cls, path: String = None)
```

## Index

> `bl_idname` : GeometryNodeInputIndex

### nd

[nd](nd.md).[index](nd.md#geonodes.core.generated.static_nd.ND.index)(self)

### class Geometry

```python
prop = [Geometry](geometry.md.md).[index](geometry.md.md#('geonodes.core.geometry.md',).index)
```

## Index Switch

> `bl_idname` : GeometryNodeIndexSwitch

### class Socket

```python
[Socket](socket.md.md).[IndexSwitch](socket.md.md#('geonodes.core.socket.md',).IndexSwitch)(*values, index=0)
```

```python
[Socket](socket.md.md).[index_switch](socket.md.md#('geonodes.core.socket.md',).index_switch)(*values, index=0)
```

## Index of Nearest

> `bl_idname` : GeometryNodeIndexOfNearest

### nd

[nd](nd.md).[index_of_nearest](nd.md#geonodes.core.generated.static_nd.ND.index_of_nearest)(cls, position: Vector = None, group_id: Integer = None)

### class Geometry

```python
[Geometry](geometry.md.md).[index_of_nearest](geometry.md.md#('geonodes.core.geometry.md',).index_of_nearest)(cls, position: Vector = None, group_id: Integer = None)
```

## Instance Bounds

> `bl_idname` : GeometryNodeInputInstanceBounds

### nd

[nd](nd.md).[instance_bounds](nd.md#geonodes.core.generated.static_nd.ND.instance_bounds)(cls, use_radius: Boolean = None)

## Instance Rotation

> `bl_idname` : GeometryNodeInputInstanceRotation

### nd

[nd](nd.md).[instance_rotation](nd.md#geonodes.core.generated.static_nd.ND.instance_rotation)(self)

### class Instances

```python
prop = [Instances](instances.md.md).[rotation](instances.md.md#('geonodes.core.instances.md',).rotation)
```

## Instance Scale

> `bl_idname` : GeometryNodeInputInstanceScale

### nd

[nd](nd.md).[instance_scale](nd.md#geonodes.core.generated.static_nd.ND.instance_scale)(self)

### class Instances

```python
prop = [Instances](instances.md.md).[instance_scale](instances.md.md#('geonodes.core.instances.md',).instance_scale)
```

## Instance Transform

> `bl_idname` : GeometryNodeInstanceTransform

### nd

[nd](nd.md).[instance_transform](nd.md#geonodes.core.generated.static_nd.ND.instance_transform)(self)

### class Instances

```python
prop = [Instances](instances.md.md).[transform](instances.md.md#('geonodes.core.instances.md',).transform)
```

## Instance on Points

> `bl_idname` : GeometryNodeInstanceOnPoints

### nd

[nd](nd.md).[instance_on_points](nd.md#geonodes.core.generated.static_nd.ND.instance_on_points)(cls,
                    points: Cloud = None,
                    selection: Boolean = None,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)

### class Geometry

```python
[Geometry](geometry.md.md).[instance_on_points](geometry.md.md#('geonodes.core.geometry.md',).instance_on_points)(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

### class Cloud

```python
[Cloud](cloud.md.md).[instance_on](cloud.md.md#('geonodes.core.cloud.md',).instance_on)(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

### class Point

```python
[Point](point.md.md).[instance_on](point.md.md#('geonodes.core.point.md',).instance_on)(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None)
```

## Instances to Points

> `bl_idname` : GeometryNodeInstancesToPoints

### nd

[nd](nd.md).[instances_to_points](nd.md#geonodes.core.generated.static_nd.ND.instances_to_points)(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None)

### class Instances

```python
[Instances](instances.md.md).[to_points](instances.md.md#('geonodes.core.instances.md',).to_points)(self, position: Vector = None, radius: Float = None)
```

## Integer

> `bl_idname` : FunctionNodeInputInt

### nd

[nd](nd.md).[integer](nd.md#geonodes.core.generated.static_nd.ND.integer)(cls, integer = 0)

## Integer Math

> `bl_idname` : FunctionNodeIntegerMath

### nd

[nd](nd.md).[integer_math](nd.md#geonodes.core.generated.static_nd.ND.integer_math)(cls,
                    value: Integer = None,
                    value_1: Integer = None,
                    value_2: Integer = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM'] = 'ADD')

### class Integer

```python
[Integer](integer.md.md).[add](integer.md.md#('geonodes.core.integer.md',).add)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[subtract](integer.md.md#('geonodes.core.integer.md',).subtract)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[multiply](integer.md.md#('geonodes.core.integer.md',).multiply)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[divide](integer.md.md#('geonodes.core.integer.md',).divide)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[multiply_add](integer.md.md#('geonodes.core.integer.md',).multiply_add)(self, multiplier: Integer = None, addend: Integer = None)
```

```python
[Integer](integer.md.md).[abs](integer.md.md#('geonodes.core.integer.md',).abs)(self)
```

```python
[Integer](integer.md.md).[negate](integer.md.md#('geonodes.core.integer.md',).negate)(self)
```

```python
[Integer](integer.md.md).[power](integer.md.md#('geonodes.core.integer.md',).power)(self, exponent: Integer = None)
```

```python
[Integer](integer.md.md).[min](integer.md.md#('geonodes.core.integer.md',).min)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[max](integer.md.md#('geonodes.core.integer.md',).max)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[sign](integer.md.md#('geonodes.core.integer.md',).sign)(self)
```

```python
[Integer](integer.md.md).[divide_round](integer.md.md#('geonodes.core.integer.md',).divide_round)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[divide_floor](integer.md.md#('geonodes.core.integer.md',).divide_floor)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[divide_ceil](integer.md.md#('geonodes.core.integer.md',).divide_ceil)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[floored_modulo](integer.md.md#('geonodes.core.integer.md',).floored_modulo)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[modulo](integer.md.md#('geonodes.core.integer.md',).modulo)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[gcd](integer.md.md#('geonodes.core.integer.md',).gcd)(self, value: Integer = None)
```

```python
[Integer](integer.md.md).[lcm](integer.md.md#('geonodes.core.integer.md',).lcm)(self, value: Integer = None)
```

### class gnmath

```python
[gnmath](gnmath.md.md).[iadd](gnmath.md.md#('geonodes.core.gnmath.md',).iadd)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[isubtract](gnmath.md.md#('geonodes.core.gnmath.md',).isubtract)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[imultiply](gnmath.md.md#('geonodes.core.gnmath.md',).imultiply)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[idivide](gnmath.md.md#('geonodes.core.gnmath.md',).idivide)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[imultiply_add](gnmath.md.md#('geonodes.core.gnmath.md',).imultiply_add)(value: Integer = None, multiplier: Integer = None, addend: Integer = None)
```

```python
[gnmath](gnmath.md.md).[iabs](gnmath.md.md#('geonodes.core.gnmath.md',).iabs)(value: Integer = None)
```

```python
[gnmath](gnmath.md.md).[negate](gnmath.md.md#('geonodes.core.gnmath.md',).negate)(value: Integer = None)
```

```python
[gnmath](gnmath.md.md).[ipower](gnmath.md.md#('geonodes.core.gnmath.md',).ipower)(base: Integer = None, exponent: Integer = None)
```

```python
[gnmath](gnmath.md.md).[imin](gnmath.md.md#('geonodes.core.gnmath.md',).imin)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[imax](gnmath.md.md#('geonodes.core.gnmath.md',).imax)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[isign](gnmath.md.md#('geonodes.core.gnmath.md',).isign)(value: Integer = None)
```

```python
[gnmath](gnmath.md.md).[divide_round](gnmath.md.md#('geonodes.core.gnmath.md',).divide_round)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[divide_floor](gnmath.md.md#('geonodes.core.gnmath.md',).divide_floor)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[divide_ceil](gnmath.md.md#('geonodes.core.gnmath.md',).divide_ceil)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[ifloored_modulo](gnmath.md.md#('geonodes.core.gnmath.md',).ifloored_modulo)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[imodulo](gnmath.md.md#('geonodes.core.gnmath.md',).imodulo)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[gcd](gnmath.md.md#('geonodes.core.gnmath.md',).gcd)(value: Integer = None, value_1: Integer = None)
```

```python
[gnmath](gnmath.md.md).[lcm](gnmath.md.md#('geonodes.core.gnmath.md',).lcm)(value: Integer = None, value_1: Integer = None)
```

## Interpolate Curves

> `bl_idname` : GeometryNodeInterpolateCurves

### nd

[nd](nd.md).[interpolate_curves](nd.md#geonodes.core.generated.static_nd.ND.interpolate_curves)(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[Interpolate](curve.md.md#('geonodes.core.curve.md',).Interpolate)(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)
```

```python
[Curve](curve.md.md).[interpolate](curve.md.md#('geonodes.core.curve.md',).interpolate)(self,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None)
```

### class Cloud

```python
[Cloud](cloud.md.md).[interpolate_curves](cloud.md.md#('geonodes.core.cloud.md',).interpolate_curves)(self,
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

[snd](snd.md).[invert_color](snd.md#geonodes.core.generated.static_snd.SND.invert_color)(cls, color: Color = None, factor: Float = None)

### class Color

```python
[Color](color.md.md).[invert_color](color.md.md#('geonodes.core.color.md',).invert_color)(self, factor: Float = None)
```

## Invert Matrix

> `bl_idname` : FunctionNodeInvertMatrix

### nd

[nd](nd.md).[invert_matrix](nd.md#geonodes.core.generated.static_nd.ND.invert_matrix)(cls, matrix: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[invert](matrix.md.md#('geonodes.core.matrix.md',).invert)(self)
```

## Invert Rotation

> `bl_idname` : FunctionNodeInvertRotation

### nd

[nd](nd.md).[invert_rotation](nd.md#geonodes.core.generated.static_nd.ND.invert_rotation)(cls, rotation: Rotation = None)

### class Rotation

```python
[Rotation](rotation.md.md).[invert](rotation.md.md#('geonodes.core.rotation.md',).invert)(self)
```

## Is Edge Smooth

> `bl_idname` : GeometryNodeInputEdgeSmooth

### nd

[nd](nd.md).[is_edge_smooth](nd.md#geonodes.core.generated.static_nd.ND.is_edge_smooth)(self)

### class Edge

```python
prop = [Edge](edge.md.md).[shade_smooth](edge.md.md#('geonodes.core.edge.md',).shade_smooth)
```

```python
prop = [Edge](edge.md.md).[smooth](edge.md.md#('geonodes.core.edge.md',).smooth)
```

## Is Face Planar

> `bl_idname` : GeometryNodeInputMeshFaceIsPlanar

### nd

[nd](nd.md).[is_face_planar](nd.md#geonodes.core.generated.static_nd.ND.is_face_planar)(cls, threshold: Float = None)

### class Mesh

```python
[Mesh](mesh.md.md).[is_face_planar](mesh.md.md#('geonodes.core.mesh.md',).is_face_planar)(cls, threshold: Float = None)
```

### class Face

```python
[Face](face.md.md).[is_planar](face.md.md#('geonodes.core.face.md',).is_planar)(cls, threshold: Float = None)
```

## Is Face Smooth

> `bl_idname` : GeometryNodeInputShadeSmooth

### nd

[nd](nd.md).[is_face_smooth](nd.md#geonodes.core.generated.static_nd.ND.is_face_smooth)(self)

### class Face

```python
prop = [Face](face.md.md).[shade_smooth](face.md.md#('geonodes.core.face.md',).shade_smooth)
```

```python
prop = [Face](face.md.md).[smooth](face.md.md#('geonodes.core.face.md',).smooth)
```

## Is Spline Cyclic

> `bl_idname` : GeometryNodeInputSplineCyclic

### nd

[nd](nd.md).[is_spline_cyclic](nd.md#geonodes.core.generated.static_nd.ND.is_spline_cyclic)(self)

### class Curve

```python
prop = [Curve](curve.md.md).[is_cyclic](curve.md.md#('geonodes.core.curve.md',).is_cyclic)
```

### class Spline

```python
prop = [Spline](spline.md.md).[is_cyclic](spline.md.md#('geonodes.core.spline.md',).is_cyclic)
```

## Is Viewport

> `bl_idname` : GeometryNodeIsViewport

### nd

[nd](nd.md).[is_viewport](nd.md#geonodes.core.generated.static_nd.ND.is_viewport)(self)

### class Boolean

```python
prop = [Boolean](boolean.md.md).[is_viewport](boolean.md.md#('geonodes.core.boolean.md',).is_viewport)
```

## Join Bundle

> `bl_idname` : NodeJoinBundle

### nd

[nd](nd.md).[join_bundle](nd.md#geonodes.core.generated.static_nd.ND.join_bundle)(cls, *bundle: Bundle)

### snd

[snd](snd.md).[join_bundle](snd.md#geonodes.core.generated.static_snd.SND.join_bundle)(cls, *bundle: Bundle)

### class Bundle

```python
[Bundle](bundle.md.md).[join](bundle.md.md#('geonodes.core.bundle.md',).join)(self, *bundle: Bundle)
```

```python
[Bundle](bundle.md.md).[join_bundle](bundle.md.md#('geonodes.core.bundle.md',).join_bundle)(self, *bundle: Bundle)
```

## Join Geometry

> `bl_idname` : GeometryNodeJoinGeometry

### nd

[nd](nd.md).[join_geometry](nd.md#geonodes.core.generated.static_nd.ND.join_geometry)(cls, *geometry: Geometry)

### class Geometry

```python
[Geometry](geometry.md.md).[join](geometry.md.md#('geonodes.core.geometry.md',).join)(self, *geometry: Geometry)
```

```python
[Geometry](geometry.md.md).[Join](geometry.md.md#('geonodes.core.geometry.md',).Join)(cls, *geometry: Geometry)
```

## Join Strings

> `bl_idname` : GeometryNodeStringJoin

### nd

[nd](nd.md).[join_strings](nd.md#geonodes.core.generated.static_nd.ND.join_strings)(cls, *strings: String, delimiter: String = None)

### class String

```python
[String](string.md.md).[join](string.md.md#('geonodes.core.string.md',).join)(self, *strings: String)
```

```python
[String](string.md.md).[Join](string.md.md#('geonodes.core.string.md',).Join)(cls, *strings: String, delimiter: String = None)
```

## Layer Weight

> `bl_idname` : ShaderNodeLayerWeight

### snd

[snd](snd.md).[layer_weight](snd.md#geonodes.core.generated.static_snd.SND.layer_weight)(cls, blend: Float = None, normal: Vector = None)

### class Float

```python
[Float](float.md.md).[layer_weight](float.md.md#('geonodes.core.float.md',).layer_weight)(self, normal: Vector = None)
```

## Light Falloff

> `bl_idname` : ShaderNodeLightFalloff

### snd

[snd](snd.md).[light_falloff](snd.md#geonodes.core.generated.static_snd.SND.light_falloff)(cls, strength: Float = None, smooth: Float = None)

### class Float

```python
[Float](float.md.md).[light_falloff](float.md.md#('geonodes.core.float.md',).light_falloff)(self, smooth: Float = None)
```

## Light Output

> `bl_idname` : ShaderNodeOutputLight

### snd

[snd](snd.md).[light_output](snd.md#geonodes.core.generated.static_snd.SND.light_output)(cls,
                    surface: Shader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
[Shader](shader.md.md).[light_output](shader.md.md#('geonodes.core.shader.md',).light_output)(self,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

## Light Path

> `bl_idname` : ShaderNodeLightPath

### snd

[snd](snd.md).[light_path](snd.md#geonodes.core.generated.static_snd.SND.light_path)(cls)

## Line Style Output

> `bl_idname` : ShaderNodeOutputLineStyle

### snd

[snd](snd.md).[line_style_output](snd.md#geonodes.core.generated.static_snd.SND.line_style_output)(cls,
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
[Color](color.md.md).[line_style_output](color.md.md#('geonodes.core.color.md',).line_style_output)(self,
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

[nd](nd.md).[linear_gizmo](nd.md#geonodes.core.generated.static_nd.ND.linear_gizmo)(cls,
                    *value: Float,
                    position: Vector = None,
                    direction: Vector = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY',
                    draw_style: Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW')

### class Float

```python
[Float](float.md.md).[linear_gizmo](float.md.md#('geonodes.core.float.md',).linear_gizmo)(self,
                    *value: Float,
                    position: Vector = None,
                    direction: Vector = None,
                    color_id: Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY',
                    draw_style: Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW')
```

## List Length

> `bl_idname` : GeometryNodeListLength

### nd

[nd](nd.md).[list_length](nd.md#geonodes.core.generated.static_nd.ND.list_length)(cls,
                    list: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT')

## Magic Texture

> `bl_idname` : ShaderNodeTexMagic

### nd

[nd](nd.md).[magic_texture](nd.md#geonodes.core.generated.static_nd.ND.magic_texture)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)

### snd

[snd](snd.md).[magic_texture](snd.md#geonodes.core.generated.static_snd.SND.magic_texture)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)

### class Color

```python
[Color](color.md.md).[Magic](color.md.md#('geonodes.core.color.md',).Magic)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)
```

### class Texture

```python
[Texture](texture.md.md).[Magic](texture.md.md#('geonodes.core.texture.md',).Magic)(cls,
                    vector: Vector = None,
                    scale: Float = None,
                    distortion: Float = None,
                    turbulence_depth = 2)
```

## Map Range

> `bl_idname` : ShaderNodeMapRange

### nd

[nd](nd.md).[map_range](nd.md#geonodes.core.generated.static_nd.ND.map_range)(cls,
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

[snd](snd.md).[map_range](snd.md#geonodes.core.generated.static_snd.SND.map_range)(cls,
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
[Float](float.md.md).[map_range](float.md.md#('geonodes.core.float.md',).map_range)(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True,
                    interpolation_type: Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR')
```

```python
[Float](float.md.md).[map_range_linear](float.md.md#('geonodes.core.float.md',).map_range_linear)(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

```python
[Float](float.md.md).[map_range_stepped](float.md.md#('geonodes.core.float.md',).map_range_stepped)(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    steps: Float = None,
                    clamp = True)
```

```python
[Float](float.md.md).[map_range_smooth_step](float.md.md#('geonodes.core.float.md',).map_range_smooth_step)(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

```python
[Float](float.md.md).[map_range_smoother_step](float.md.md#('geonodes.core.float.md',).map_range_smoother_step)(self,
                    from_min: Float | Vector = None,
                    from_max: Float | Vector = None,
                    to_min: Float | Vector = None,
                    to_max: Float | Vector = None,
                    clamp = True)
```

### class Vector

```python
[Vector](vector.md.md).[map_range](vector.md.md#('geonodes.core.vector.md',).map_range)(self,
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

[snd](snd.md).[mapping](snd.md#geonodes.core.generated.static_snd.SND.mapping)(cls,
                    vector: Vector = None,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT')

### class Vector

```python
[Vector](vector.md.md).[mapping](vector.md.md#('geonodes.core.vector.md',).mapping)(self,
                    location: Vector = None,
                    rotation: Vector = None,
                    scale: Vector = None,
                    vector_type: Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT')
```

## Match String

> `bl_idname` : FunctionNodeMatchString

### nd

[nd](nd.md).[match_string](nd.md#geonodes.core.generated.static_nd.ND.match_string)(cls,
                    string: String = None,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None)

### class String

```python
[String](string.md.md).[match_string](string.md.md#('geonodes.core.string.md',).match_string)(self,
                    operation: Literal['Starts With', 'Ends With', 'Contains'] = None,
                    key: String = None)
```

## Material

> `bl_idname` : GeometryNodeInputMaterial

### nd

[nd](nd.md).[material](nd.md#geonodes.core.generated.static_nd.ND.material)(cls, material = None)

## Material Index

> `bl_idname` : GeometryNodeInputMaterialIndex

### nd

[nd](nd.md).[material_index](nd.md#geonodes.core.generated.static_nd.ND.material_index)(self)

### class Geometry

```python
prop = [Geometry](geometry.md.md).[material_index](geometry.md.md#('geonodes.core.geometry.md',).material_index)
```

### class Face

```python
prop = [Face](face.md.md).[material_index](face.md.md#('geonodes.core.face.md',).material_index)
```

### class Spline

```python
prop = [Spline](spline.md.md).[material_index](spline.md.md#('geonodes.core.spline.md',).material_index)
```

## Material Output

> `bl_idname` : ShaderNodeOutputMaterial

### snd

[snd](snd.md).[material_output](snd.md#geonodes.core.generated.static_snd.SND.material_output)(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
[Shader](shader.md.md).[material_output](shader.md.md#('geonodes.core.shader.md',).material_output)(self,
                    volume: VolumeShader = None,
                    displacement: Vector = None,
                    thickness: Float = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

## Material Selection

> `bl_idname` : GeometryNodeMaterialSelection

### nd

[nd](nd.md).[material_selection](nd.md#geonodes.core.generated.static_nd.ND.material_selection)(cls, material: Material = None)

### class Mesh

```python
[Mesh](mesh.md.md).[material_selection](mesh.md.md#('geonodes.core.mesh.md',).material_selection)(cls, material: Material = None)
```

### class Curve

```python
[Curve](curve.md.md).[material_selection](curve.md.md#('geonodes.core.curve.md',).material_selection)(cls, material: Material = None)
```

## Math

> `bl_idname` : ShaderNodeMath

### nd

[nd](nd.md).[math](nd.md#geonodes.core.generated.static_nd.ND.math)(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False)

### snd

[snd](snd.md).[math](snd.md#geonodes.core.generated.static_snd.SND.math)(cls,
                    value: Float = None,
                    value_1: Float = None,
                    value_2: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD',
                    use_clamp = False)

### class Float

```python
[Float](float.md.md).[add](float.md.md#('geonodes.core.float.md',).add)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[subtract](float.md.md#('geonodes.core.float.md',).subtract)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[multiply](float.md.md#('geonodes.core.float.md',).multiply)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[divide](float.md.md#('geonodes.core.float.md',).divide)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[multiply_add](float.md.md#('geonodes.core.float.md',).multiply_add)(self, multiplier: Float = None, addend: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[power](float.md.md#('geonodes.core.float.md',).power)(self, exponent: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[log](float.md.md#('geonodes.core.float.md',).log)(self, base: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[sqrt](float.md.md#('geonodes.core.float.md',).sqrt)(self, use_clamp = False)
```

```python
[Float](float.md.md).[inverse_sqrt](float.md.md#('geonodes.core.float.md',).inverse_sqrt)(self, use_clamp = False)
```

```python
[Float](float.md.md).[abs](float.md.md#('geonodes.core.float.md',).abs)(self, use_clamp = False)
```

```python
[Float](float.md.md).[exp](float.md.md#('geonodes.core.float.md',).exp)(self, use_clamp = False)
```

```python
[Float](float.md.md).[min](float.md.md#('geonodes.core.float.md',).min)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[max](float.md.md#('geonodes.core.float.md',).max)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[mless_than](float.md.md#('geonodes.core.float.md',).mless_than)(self, threshold: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[mgreater_than](float.md.md#('geonodes.core.float.md',).mgreater_than)(self, threshold: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[sign](float.md.md#('geonodes.core.float.md',).sign)(self, use_clamp = False)
```

```python
[Float](float.md.md).[compare](float.md.md#('geonodes.core.float.md',).compare)(self, value: Float = None, epsilon: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[smooth_min](float.md.md#('geonodes.core.float.md',).smooth_min)(self, value: Float = None, distance: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[smooth_max](float.md.md#('geonodes.core.float.md',).smooth_max)(self, value: Float = None, distance: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[round](float.md.md#('geonodes.core.float.md',).round)(self, use_clamp = False)
```

```python
[Float](float.md.md).[floor](float.md.md#('geonodes.core.float.md',).floor)(self, use_clamp = False)
```

```python
[Float](float.md.md).[ceil](float.md.md#('geonodes.core.float.md',).ceil)(self, use_clamp = False)
```

```python
[Float](float.md.md).[trunc](float.md.md#('geonodes.core.float.md',).trunc)(self, use_clamp = False)
```

```python
[Float](float.md.md).[fract](float.md.md#('geonodes.core.float.md',).fract)(self, use_clamp = False)
```

```python
[Float](float.md.md).[modulo](float.md.md#('geonodes.core.float.md',).modulo)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[floored_modulo](float.md.md#('geonodes.core.float.md',).floored_modulo)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[wrap](float.md.md#('geonodes.core.float.md',).wrap)(self, max: Float = None, min: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[snap](float.md.md#('geonodes.core.float.md',).snap)(self, increment: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[pingpong](float.md.md#('geonodes.core.float.md',).pingpong)(self, scale: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[sin](float.md.md#('geonodes.core.float.md',).sin)(self, use_clamp = False)
```

```python
[Float](float.md.md).[cos](float.md.md#('geonodes.core.float.md',).cos)(self, use_clamp = False)
```

```python
[Float](float.md.md).[tan](float.md.md#('geonodes.core.float.md',).tan)(self, use_clamp = False)
```

```python
[Float](float.md.md).[asin](float.md.md#('geonodes.core.float.md',).asin)(self, use_clamp = False)
```

```python
[Float](float.md.md).[acos](float.md.md#('geonodes.core.float.md',).acos)(self, use_clamp = False)
```

```python
[Float](float.md.md).[arctangent](float.md.md#('geonodes.core.float.md',).arctangent)(self, use_clamp = False)
```

```python
[Float](float.md.md).[atan2](float.md.md#('geonodes.core.float.md',).atan2)(self, value: Float = None, use_clamp = False)
```

```python
[Float](float.md.md).[sinh](float.md.md#('geonodes.core.float.md',).sinh)(self, use_clamp = False)
```

```python
[Float](float.md.md).[cosh](float.md.md#('geonodes.core.float.md',).cosh)(self, use_clamp = False)
```

```python
[Float](float.md.md).[tanh](float.md.md#('geonodes.core.float.md',).tanh)(self, use_clamp = False)
```

```python
[Float](float.md.md).[radians](float.md.md#('geonodes.core.float.md',).radians)(self, use_clamp = False)
```

```python
[Float](float.md.md).[degrees](float.md.md#('geonodes.core.float.md',).degrees)(self, use_clamp = False)
```

### class gnmath

```python
[gnmath](gnmath.md.md).[add](gnmath.md.md#('geonodes.core.gnmath.md',).add)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[subtract](gnmath.md.md#('geonodes.core.gnmath.md',).subtract)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[multiply](gnmath.md.md#('geonodes.core.gnmath.md',).multiply)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[divide](gnmath.md.md#('geonodes.core.gnmath.md',).divide)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[multiply_add](gnmath.md.md#('geonodes.core.gnmath.md',).multiply_add)(value: Float = None,
                    multiplier: Float = None,
                    addend: Float = None,
                    use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[power](gnmath.md.md#('geonodes.core.gnmath.md',).power)(base: Float = None, exponent: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[log](gnmath.md.md#('geonodes.core.gnmath.md',).log)(value: Float = None, base: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[sqrt](gnmath.md.md#('geonodes.core.gnmath.md',).sqrt)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[inverse_sqrt](gnmath.md.md#('geonodes.core.gnmath.md',).inverse_sqrt)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[abs](gnmath.md.md#('geonodes.core.gnmath.md',).abs)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[exp](gnmath.md.md#('geonodes.core.gnmath.md',).exp)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[min](gnmath.md.md#('geonodes.core.gnmath.md',).min)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[max](gnmath.md.md#('geonodes.core.gnmath.md',).max)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[mless_than](gnmath.md.md#('geonodes.core.gnmath.md',).mless_than)(value: Float = None, threshold: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[mgreater_than](gnmath.md.md#('geonodes.core.gnmath.md',).mgreater_than)(value: Float = None, threshold: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[sign](gnmath.md.md#('geonodes.core.gnmath.md',).sign)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[compare](gnmath.md.md#('geonodes.core.gnmath.md',).compare)(value: Float = None,
                    value_1: Float = None,
                    epsilon: Float = None,
                    use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[smooth_min](gnmath.md.md#('geonodes.core.gnmath.md',).smooth_min)(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[smooth_max](gnmath.md.md#('geonodes.core.gnmath.md',).smooth_max)(value: Float = None,
                    value_1: Float = None,
                    distance: Float = None,
                    use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[round](gnmath.md.md#('geonodes.core.gnmath.md',).round)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[floor](gnmath.md.md#('geonodes.core.gnmath.md',).floor)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[ceil](gnmath.md.md#('geonodes.core.gnmath.md',).ceil)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[trunc](gnmath.md.md#('geonodes.core.gnmath.md',).trunc)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[fract](gnmath.md.md#('geonodes.core.gnmath.md',).fract)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[modulo](gnmath.md.md#('geonodes.core.gnmath.md',).modulo)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[floored_modulo](gnmath.md.md#('geonodes.core.gnmath.md',).floored_modulo)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[wrap](gnmath.md.md#('geonodes.core.gnmath.md',).wrap)(value: Float = None, max: Float = None, min: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[snap](gnmath.md.md#('geonodes.core.gnmath.md',).snap)(value: Float = None, increment: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[pingpong](gnmath.md.md#('geonodes.core.gnmath.md',).pingpong)(value: Float = None, scale: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[sin](gnmath.md.md#('geonodes.core.gnmath.md',).sin)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[cos](gnmath.md.md#('geonodes.core.gnmath.md',).cos)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[tan](gnmath.md.md#('geonodes.core.gnmath.md',).tan)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[asin](gnmath.md.md#('geonodes.core.gnmath.md',).asin)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[acos](gnmath.md.md#('geonodes.core.gnmath.md',).acos)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[arctangent](gnmath.md.md#('geonodes.core.gnmath.md',).arctangent)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[atan2](gnmath.md.md#('geonodes.core.gnmath.md',).atan2)(value: Float = None, value_1: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[sinh](gnmath.md.md#('geonodes.core.gnmath.md',).sinh)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[cosh](gnmath.md.md#('geonodes.core.gnmath.md',).cosh)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[tanh](gnmath.md.md#('geonodes.core.gnmath.md',).tanh)(value: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[radians](gnmath.md.md#('geonodes.core.gnmath.md',).radians)(degrees: Float = None, use_clamp = False)
```

```python
[gnmath](gnmath.md.md).[degrees](gnmath.md.md#('geonodes.core.gnmath.md',).degrees)(radians: Float = None, use_clamp = False)
```

## Matrix Determinant

> `bl_idname` : FunctionNodeMatrixDeterminant

### nd

[nd](nd.md).[matrix_determinant](nd.md#geonodes.core.generated.static_nd.ND.matrix_determinant)(cls, matrix: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[determinant](matrix.md.md#('geonodes.core.matrix.md',).determinant)(self)
```

## Matrix SVD

> `bl_idname` : FunctionNodeMatrixSVD

### nd

[nd](nd.md).[matrix_svd](nd.md#geonodes.core.generated.static_nd.ND.matrix_svd)(cls, matrix: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[svd](matrix.md.md#('geonodes.core.matrix.md',).svd)(self)
```

## Menu Switch

> `bl_idname` : GeometryNodeMenuSwitch

### class Socket

```python
[Socket](socket.md.md).[MenuSwitch](socket.md.md#('geonodes.core.socket.md',).MenuSwitch)(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None, panel=None, hide_value=False, hide_in_modifier=False, single_value=False)
```

```python
[Socket](socket.md.md).[menu_switch](socket.md.md#('geonodes.core.socket.md',).menu_switch)(items={'A': None, 'B': None}, menu=0, name='Menu', tip=None, panel=None, hide_value=False, hide_in_modifier=False, single_value=False)
```

## Merge Layers

> `bl_idname` : GeometryNodeMergeLayers

### nd

[nd](nd.md).[merge_layers](nd.md#geonodes.core.generated.static_nd.ND.merge_layers)(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME')

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[merge_layers_by_name](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).merge_layers_by_name)(self)
```

```python
[GreasePencil](grease_pencil.md.md).[merge_layers_by_id](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).merge_layers_by_id)(self, group_id: Integer = None)
```

```python
[GreasePencil](grease_pencil.md.md).[merge_layers](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).merge_layers)(self, mode: Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME')
```

## Merge by Distance

> `bl_idname` : GeometryNodeMergeByDistance

### nd

[nd](nd.md).[merge_by_distance](nd.md#geonodes.core.generated.static_nd.ND.merge_by_distance)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    mode: Literal['All', 'Connected'] = None,
                    distance: Float = None)

### class Geometry

```python
[Geometry](geometry.md.md).[merge_by_distance](geometry.md.md#('geonodes.core.geometry.md',).merge_by_distance)(self, mode: Literal['All', 'Connected'] = None, distance: Float = None)
```

```python
[Geometry](geometry.md.md).[merge](geometry.md.md#('geonodes.core.geometry.md',).merge)(self, mode: Literal['All', 'Connected'] = None, distance: Float = None)
```

## Mesh Boolean

> `bl_idname` : GeometryNodeMeshBoolean

### nd

[nd](nd.md).[mesh_boolean](nd.md#geonodes.core.generated.static_nd.ND.mesh_boolean)(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    self_intersection: Boolean = None,
                    hole_tolerant: Boolean = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')

### class Mesh

```python
[Mesh](mesh.md.md).[boolean](mesh.md.md#('geonodes.core.mesh.md',).boolean)(self,
                    *mesh_2: Mesh,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[Boolean](mesh.md.md#('geonodes.core.mesh.md',).Boolean)(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE',
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[intersect](mesh.md.md#('geonodes.core.mesh.md',).intersect)(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[union](mesh.md.md#('geonodes.core.mesh.md',).union)(self, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[difference](mesh.md.md#('geonodes.core.mesh.md',).difference)(self, *mesh_2: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[Intersect](mesh.md.md#('geonodes.core.mesh.md',).Intersect)(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[Union](mesh.md.md#('geonodes.core.mesh.md',).Union)(cls, *mesh: Mesh, solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

```python
[Mesh](mesh.md.md).[Difference](mesh.md.md#('geonodes.core.mesh.md',).Difference)(cls,
                    *mesh_2: Mesh,
                    mesh_1: Mesh = None,
                    solver: Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT')
```

## Mesh Circle

> `bl_idname` : GeometryNodeMeshCircle

### nd

[nd](nd.md).[mesh_circle](nd.md#geonodes.core.generated.static_nd.ND.mesh_circle)(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE')

### class Mesh

```python
[Mesh](mesh.md.md).[Circle](mesh.md.md#('geonodes.core.mesh.md',).Circle)(cls,
                    vertices: Integer = None,
                    radius: Float = None,
                    fill_type: Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE')
```

## Mesh Island

> `bl_idname` : GeometryNodeInputMeshIsland

### nd

[nd](nd.md).[mesh_island](nd.md#geonodes.core.generated.static_nd.ND.mesh_island)(cls)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[mesh_island](mesh.md.md#('geonodes.core.mesh.md',).mesh_island)
```

```python
prop = [Mesh](mesh.md.md).[island_index](mesh.md.md#('geonodes.core.mesh.md',).island_index)
```

```python
prop = [Mesh](mesh.md.md).[island_count](mesh.md.md#('geonodes.core.mesh.md',).island_count)
```

## Mesh Line

> `bl_idname` : GeometryNodeMeshLine

### nd

[nd](nd.md).[mesh_line](nd.md#geonodes.core.generated.static_nd.ND.mesh_line)(cls,
                    count: Integer = None,
                    resolution: Float = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET')

### class Mesh

```python
[Mesh](mesh.md.md).[LineOffset](mesh.md.md#('geonodes.core.mesh.md',).LineOffset)(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL')
```

```python
[Mesh](mesh.md.md).[LineEndPoints](mesh.md.md#('geonodes.core.mesh.md',).LineEndPoints)(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    end_location: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL')
```

```python
[Mesh](mesh.md.md).[Line](mesh.md.md#('geonodes.core.mesh.md',).Line)(cls,
                    count: Integer = None,
                    start_location: Vector = None,
                    offset: Vector = None,
                    count_mode: Literal['TOTAL', 'RESOLUTION'] = 'TOTAL',
                    mode: Literal['OFFSET', 'END_POINTS'] = 'OFFSET')
```

## Mesh to Curve

> `bl_idname` : GeometryNodeMeshToCurve

### nd

[nd](nd.md).[mesh_to_curve](nd.md#geonodes.core.generated.static_nd.ND.mesh_to_curve)(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    mode: Literal['EDGES', 'FACES'] = 'EDGES')

### class Mesh

```python
[Mesh](mesh.md.md).[to_curve_edges](mesh.md.md#('geonodes.core.mesh.md',).to_curve_edges)(self)
```

```python
[Mesh](mesh.md.md).[to_curve_faces](mesh.md.md#('geonodes.core.mesh.md',).to_curve_faces)(self)
```

```python
[Mesh](mesh.md.md).[to_curve](mesh.md.md#('geonodes.core.mesh.md',).to_curve)(self, mode: Literal['EDGES', 'FACES'] = 'EDGES')
```

## Mesh to Density Grid

> `bl_idname` : GeometryNodeMeshToDensityGrid

### nd

[nd](nd.md).[mesh_to_density_grid](nd.md#geonodes.core.generated.static_nd.ND.mesh_to_density_grid)(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None)

### class Mesh

```python
[Mesh](mesh.md.md).[to_density_grid](mesh.md.md#('geonodes.core.mesh.md',).to_density_grid)(self,
                    density: Float = None,
                    voxel_size: Float = None,
                    gradient_width: Float = None)
```

## Mesh to Points

> `bl_idname` : GeometryNodeMeshToPoints

### nd

[nd](nd.md).[mesh_to_points](nd.md#geonodes.core.generated.static_nd.ND.mesh_to_points)(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES')

### class Mesh

```python
[Mesh](mesh.md.md).[to_points](mesh.md.md#('geonodes.core.mesh.md',).to_points)(self,
                    position: Vector = None,
                    radius: Float = None,
                    mode: Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES')
```

```python
[Mesh](mesh.md.md).[vertices_to_points](mesh.md.md#('geonodes.core.mesh.md',).vertices_to_points)(self, position: Vector = None, radius: Float = None)
```

```python
[Mesh](mesh.md.md).[edges_to_points](mesh.md.md#('geonodes.core.mesh.md',).edges_to_points)(self, position: Vector = None, radius: Float = None)
```

```python
[Mesh](mesh.md.md).[faces_to_points](mesh.md.md#('geonodes.core.mesh.md',).faces_to_points)(self, position: Vector = None, radius: Float = None)
```

```python
[Mesh](mesh.md.md).[corners_to_points](mesh.md.md#('geonodes.core.mesh.md',).corners_to_points)(self, position: Vector = None, radius: Float = None)
```

### class Vertex

```python
[Vertex](vertex.md.md).[to_points](vertex.md.md#('geonodes.core.vertex.md',).to_points)(self, position: Vector = None, radius: Float = None)
```

### class Face

```python
[Face](face.md.md).[to_points](face.md.md#('geonodes.core.face.md',).to_points)(self, position: Vector = None, radius: Float = None)
```

### class Edge

```python
[Edge](edge.md.md).[to_points](edge.md.md#('geonodes.core.edge.md',).to_points)(self, position: Vector = None, radius: Float = None)
```

### class Corner

```python
[Corner](corner.md.md).[to_points](corner.md.md#('geonodes.core.corner.md',).to_points)(self, position: Vector = None, radius: Float = None)
```

## Mesh to SDF Grid

> `bl_idname` : GeometryNodeMeshToSDFGrid

### nd

[nd](nd.md).[mesh_to_sdf_grid](nd.md#geonodes.core.generated.static_nd.ND.mesh_to_sdf_grid)(cls, mesh: Mesh = None, voxel_size: Float = None, band_width: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[to_sdf_grid](mesh.md.md#('geonodes.core.mesh.md',).to_sdf_grid)(self, voxel_size: Float = None, band_width: Integer = None)
```

## Mesh to Volume

> `bl_idname` : GeometryNodeMeshToVolume

### nd

[nd](nd.md).[mesh_to_volume](nd.md#geonodes.core.generated.static_nd.ND.mesh_to_volume)(cls,
                    mesh: Mesh = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None)

### class Mesh

```python
[Mesh](mesh.md.md).[to_volume](mesh.md.md#('geonodes.core.mesh.md',).to_volume)(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    interior_band_width: Float = None)
```

## Metallic BSDF

> `bl_idname` : ShaderNodeBsdfMetallic

### snd

[snd](snd.md).[metallic_bsdf](snd.md#geonodes.core.generated.static_snd.SND.metallic_bsdf)(cls,
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
[Shader](shader.md.md).[Metallic](shader.md.md#('geonodes.core.shader.md',).Metallic)(cls,
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

[nd](nd.md).[mix](nd.md#geonodes.core.generated.static_nd.ND.mix)(cls,
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

[snd](snd.md).[mix](snd.md#geonodes.core.generated.static_snd.SND.mix)(cls,
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
[Float](float.md.md).[mix](float.md.md#('geonodes.core.float.md',).mix)(self, b: Float = None, factor: Float = None, clamp_factor = True)
```

### class Rotation

```python
[Rotation](rotation.md.md).[mix](rotation.md.md#('geonodes.core.rotation.md',).mix)(self, b: Rotation = None, factor: Float = None, clamp_factor = True)
```

### class Vector

```python
[Vector](vector.md.md).[mix_uniform](vector.md.md#('geonodes.core.vector.md',).mix_uniform)(self, b: Vector = None, factor: Float = None, clamp_factor = True)
```

```python
[Vector](vector.md.md).[mix_non_uniform](vector.md.md#('geonodes.core.vector.md',).mix_non_uniform)(self, b: Vector = None, factor: Vector = None, clamp_factor = True)
```

### class Color

```python
[Color](color.md.md).[mix_mix](color.md.md#('geonodes.core.color.md',).mix_mix)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_darken](color.md.md#('geonodes.core.color.md',).mix_darken)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_multiply](color.md.md#('geonodes.core.color.md',).mix_multiply)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_burn](color.md.md#('geonodes.core.color.md',).mix_burn)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_lighten](color.md.md#('geonodes.core.color.md',).mix_lighten)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_screen](color.md.md#('geonodes.core.color.md',).mix_screen)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_dodge](color.md.md#('geonodes.core.color.md',).mix_dodge)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_add](color.md.md#('geonodes.core.color.md',).mix_add)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_overlay](color.md.md#('geonodes.core.color.md',).mix_overlay)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_soft_light](color.md.md#('geonodes.core.color.md',).mix_soft_light)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_linear_light](color.md.md#('geonodes.core.color.md',).mix_linear_light)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_difference](color.md.md#('geonodes.core.color.md',).mix_difference)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_exclusion](color.md.md#('geonodes.core.color.md',).mix_exclusion)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_subtract](color.md.md#('geonodes.core.color.md',).mix_subtract)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_divide](color.md.md#('geonodes.core.color.md',).mix_divide)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_hue](color.md.md#('geonodes.core.color.md',).mix_hue)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_saturation](color.md.md#('geonodes.core.color.md',).mix_saturation)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_color](color.md.md#('geonodes.core.color.md',).mix_color)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix_value](color.md.md#('geonodes.core.color.md',).mix_value)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False)
```

```python
[Color](color.md.md).[mix](color.md.md#('geonodes.core.color.md',).mix)(self,
                    b: Color = None,
                    factor: Float = None,
                    clamp_factor = True,
                    clamp_result = False,
                    factor_mode: Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM')
```

## Mix Shader

> `bl_idname` : ShaderNodeMixShader

### snd

[snd](snd.md).[mix_shader](snd.md#geonodes.core.generated.static_snd.SND.mix_shader)(cls, shader: Shader = None, shader_1: Shader = None, factor: Float = None)

### class Shader

```python
[Shader](shader.md.md).[mix](shader.md.md#('geonodes.core.shader.md',).mix)(self, shader: Shader = None, factor: Float = None)
```

## Mouse Position

> `bl_idname` : GeometryNodeToolMousePosition

### nd

[nd](nd.md).[mouse_position](nd.md#geonodes.core.generated.static_nd.ND.mouse_position)(cls)

## Multiply Matrices

> `bl_idname` : FunctionNodeMatrixMultiply

### nd

[nd](nd.md).[multiply_matrices](nd.md#geonodes.core.generated.static_nd.ND.multiply_matrices)(cls, matrix: Matrix = None, matrix_1: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[multiply](matrix.md.md#('geonodes.core.matrix.md',).multiply)(self, matrix: Matrix = None)
```

## Named Attribute

> `bl_idname` : GeometryNodeInputNamedAttribute

### nd

[nd](nd.md).[named_attribute](nd.md#geonodes.core.generated.static_nd.ND.named_attribute)(cls,
                    name: String = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[Named](float.md.md#('geonodes.core.float.md',).Named)(cls, name: String = None)
```

```python
[Float](float.md.md).[NamedAttribute](float.md.md#('geonodes.core.float.md',).NamedAttribute)(cls, name: String = None)
```

### class Integer

```python
[Integer](integer.md.md).[Named](integer.md.md#('geonodes.core.integer.md',).Named)(cls, name: String = None)
```

```python
[Integer](integer.md.md).[NamedAttribute](integer.md.md#('geonodes.core.integer.md',).NamedAttribute)(cls, name: String = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[Named](boolean.md.md#('geonodes.core.boolean.md',).Named)(cls, name: String = None)
```

```python
[Boolean](boolean.md.md).[NamedAttribute](boolean.md.md#('geonodes.core.boolean.md',).NamedAttribute)(cls, name: String = None)
```

### class Vector

```python
[Vector](vector.md.md).[Named](vector.md.md#('geonodes.core.vector.md',).Named)(cls, name: String = None)
```

```python
[Vector](vector.md.md).[NamedAttribute](vector.md.md#('geonodes.core.vector.md',).NamedAttribute)(cls, name: String = None)
```

### class Color

```python
[Color](color.md.md).[Named](color.md.md#('geonodes.core.color.md',).Named)(cls, name: String = None)
```

```python
[Color](color.md.md).[NamedAttribute](color.md.md#('geonodes.core.color.md',).NamedAttribute)(cls, name: String = None)
```

### class Rotation

```python
[Rotation](rotation.md.md).[Named](rotation.md.md#('geonodes.core.rotation.md',).Named)(cls, name: String = None)
```

```python
[Rotation](rotation.md.md).[NamedAttribute](rotation.md.md#('geonodes.core.rotation.md',).NamedAttribute)(cls, name: String = None)
```

### class Matrix

```python
[Matrix](matrix.md.md).[Named](matrix.md.md#('geonodes.core.matrix.md',).Named)(cls, name: String = None)
```

```python
[Matrix](matrix.md.md).[NamedAttribute](matrix.md.md#('geonodes.core.matrix.md',).NamedAttribute)(cls, name: String = None)
```

## Named Layer Selection

> `bl_idname` : GeometryNodeInputNamedLayerSelection

### nd

[nd](nd.md).[named_layer_selection](nd.md#geonodes.core.generated.static_nd.ND.named_layer_selection)(cls, name: String = None)

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[named_layer_selection](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).named_layer_selection)(cls, name: String = None)
```

### class Layer

```python
[Layer](layer.md.md).[named_selection](layer.md.md#('geonodes.core.layer.md',).named_selection)(cls, name: String = None)
```

## Noise Texture

> `bl_idname` : ShaderNodeTexNoise

### nd

[nd](nd.md).[noise_texture](nd.md#geonodes.core.generated.static_nd.ND.noise_texture)(cls,
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

[snd](snd.md).[noise_texture](snd.md#geonodes.core.generated.static_snd.SND.noise_texture)(cls,
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
[Float](float.md.md).[Noise](float.md.md#('geonodes.core.float.md',).Noise)(cls,
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
[Texture](texture.md.md).[Noise](texture.md.md#('geonodes.core.texture.md',).Noise)(cls,
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

[snd](snd.md).[normal](snd.md#geonodes.core.generated.static_snd.SND.normal)(cls, normal: Vector = None)

### class Vector

```python
[Vector](vector.md.md).[normal](vector.md.md#('geonodes.core.vector.md',).normal)(self)
```

## Normal Map

> `bl_idname` : ShaderNodeNormalMap

### snd

[snd](snd.md).[normal_map](snd.md#geonodes.core.generated.static_snd.SND.normal_map)(cls,
                    strength: Float = None,
                    color: Color = None,
                    base: Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED',
                    convention: Literal['OPENGL', 'DIRECTX'] = 'OPENGL',
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = '')

### class Float

```python
[Float](float.md.md).[normal_map](float.md.md#('geonodes.core.float.md',).normal_map)(self,
                    color: Color = None,
                    base: Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED',
                    convention: Literal['OPENGL', 'DIRECTX'] = 'OPENGL',
                    space: Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT',
                    uv_map = '')
```

## Object

> `bl_idname` : GeometryNodeInputObject

### nd

[nd](nd.md).[object](nd.md#geonodes.core.generated.static_nd.ND.object)(cls, object = None)

## Object Info

> `bl_idname` : ShaderNodeObjectInfo

### snd

[snd](snd.md).[object_info](snd.md#geonodes.core.generated.static_snd.SND.object_info)(cls)

## Offset Corner in Face

> `bl_idname` : GeometryNodeOffsetCornerInFace

### nd

[nd](nd.md).[offset_corner_in_face](nd.md#geonodes.core.generated.static_nd.ND.offset_corner_in_face)(cls, corner_index: Integer = None, offset: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[offset_corner_in_face](mesh.md.md#('geonodes.core.mesh.md',).offset_corner_in_face)(cls, corner_index: Integer = None, offset: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[offset_in_face](corner.md.md#('geonodes.core.corner.md',).offset_in_face)(cls, corner_index: Integer = None, offset: Integer = None)
```

## Offset Point in Curve

> `bl_idname` : GeometryNodeOffsetPointInCurve

### nd

[nd](nd.md).[offset_point_in_curve](nd.md#geonodes.core.generated.static_nd.ND.offset_point_in_curve)(cls, point_index: Integer = None, offset: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[offset_point_in_curve](curve.md.md#('geonodes.core.curve.md',).offset_point_in_curve)(cls, point_index: Integer = None, offset: Integer = None)
```

### class SplinePoint

```python
[SplinePoint](spline_point.md.md).[offset_in_curve](spline_point.md.md#('geonodes.core.spline_point.md',).offset_in_curve)(cls, point_index: Integer = None, offset: Integer = None)
```

## Pack UV Islands

> `bl_idname` : GeometryNodeUVPackIslands

### nd

[nd](nd.md).[pack_uv_islands](nd.md#geonodes.core.generated.static_nd.ND.pack_uv_islands)(cls,
                    uv: Vector = None,
                    selection: Boolean = None,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None)

### class Vector

```python
[Vector](vector.md.md).[pack_uv_islands](vector.md.md#('geonodes.core.vector.md',).pack_uv_islands)(self,
                    margin: Float = None,
                    rotate: Boolean = None,
                    method: Literal['Bounding Box', 'Convex Hull', 'Exact Shape'] = None,
                    bottom_left: Vector = None,
                    top_right: Vector = None)
```

### class Corner

```python
[Corner](corner.md.md).[pack_uv_islands](corner.md.md#('geonodes.core.corner.md',).pack_uv_islands)(cls,
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

[snd](snd.md).[particle_info](snd.md#geonodes.core.generated.static_snd.SND.particle_info)(cls)

## Point Info

> `bl_idname` : ShaderNodePointInfo

### snd

[snd](snd.md).[point_info](snd.md#geonodes.core.generated.static_snd.SND.point_info)(cls)

## Points

> `bl_idname` : GeometryNodePoints

### nd

[nd](nd.md).[points](nd.md#geonodes.core.generated.static_nd.ND.points)(cls, count: Integer = None, position: Vector = None, radius: Float = None)

### class Cloud

```python
[Cloud](cloud.md.md).[Points](cloud.md.md#('geonodes.core.cloud.md',).Points)(cls, count: Integer = None, position: Vector = None, radius: Float = None)
```

## Points of Curve

> `bl_idname` : GeometryNodePointsOfCurve

### nd

[nd](nd.md).[points_of_curve](nd.md#geonodes.core.generated.static_nd.ND.points_of_curve)(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[points_of_curve](curve.md.md#('geonodes.core.curve.md',).points_of_curve)(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

### class Spline

```python
[Spline](spline.md.md).[points_of_curve](spline.md.md#('geonodes.core.spline.md',).points_of_curve)(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Spline](spline.md.md).[point_index](spline.md.md#('geonodes.core.spline.md',).point_index)(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

```python
[Spline](spline.md.md).[points_total](spline.md.md#('geonodes.core.spline.md',).points_total)(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None)
```

## Points to Curves

> `bl_idname` : GeometryNodePointsToCurves

### nd

[nd](nd.md).[points_to_curves](nd.md#geonodes.core.generated.static_nd.ND.points_to_curves)(cls,
                    points: Cloud = None,
                    curve_group_id: Integer = None,
                    weight: Float = None)

### class Cloud

```python
[Cloud](cloud.md.md).[to_curves](cloud.md.md#('geonodes.core.cloud.md',).to_curves)(self, curve_group_id: Integer = None, weight: Float = None)
```

## Points to SDF Grid

> `bl_idname` : GeometryNodePointsToSDFGrid

### nd

[nd](nd.md).[points_to_sdf_grid](nd.md#geonodes.core.generated.static_nd.ND.points_to_sdf_grid)(cls, points: Cloud = None, radius: Float = None, voxel_size: Float = None)

### class Cloud

```python
[Cloud](cloud.md.md).[to_sdf_grid](cloud.md.md#('geonodes.core.cloud.md',).to_sdf_grid)(self, radius: Float = None, voxel_size: Float = None)
```

## Points to Vertices

> `bl_idname` : GeometryNodePointsToVertices

### nd

[nd](nd.md).[points_to_vertices](nd.md#geonodes.core.generated.static_nd.ND.points_to_vertices)(cls, points: Cloud = None, selection: Boolean = None)

### class Cloud

```python
[Cloud](cloud.md.md).[to_vertices](cloud.md.md#('geonodes.core.cloud.md',).to_vertices)(self)
```

## Points to Volume

> `bl_idname` : GeometryNodePointsToVolume

### nd

[nd](nd.md).[points_to_volume](nd.md#geonodes.core.generated.static_nd.ND.points_to_volume)(cls,
                    points: Cloud = None,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None)

### class Cloud

```python
[Cloud](cloud.md.md).[to_volume](cloud.md.md#('geonodes.core.cloud.md',).to_volume)(self,
                    density: Float = None,
                    resolution_mode: Literal['Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    radius: Float = None)
```

## Position

> `bl_idname` : GeometryNodeInputPosition

### nd

[nd](nd.md).[position](nd.md#geonodes.core.generated.static_nd.ND.position)(self)

### class Geometry

```python
prop = [Geometry](geometry.md.md).[position](geometry.md.md#('geonodes.core.geometry.md',).position)
```

### class Point

```python
prop = [Point](point.md.md).[position](point.md.md#('geonodes.core.point.md',).position)
```

## Principled BSDF

> `bl_idname` : ShaderNodeBsdfPrincipled

### snd

[snd](snd.md).[principled_bsdf](snd.md#geonodes.core.generated.static_snd.SND.principled_bsdf)(cls,
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
[Shader](shader.md.md).[Principled](shader.md.md#('geonodes.core.shader.md',).Principled)(cls,
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

[snd](snd.md).[principled_hair_bsdf](snd.md#geonodes.core.generated.static_snd.SND.principled_hair_bsdf)(cls,
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
[Shader](shader.md.md).[PrincipledHair](shader.md.md#('geonodes.core.shader.md',).PrincipledHair)(cls,
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

[snd](snd.md).[principled_volume](snd.md#geonodes.core.generated.static_snd.SND.principled_volume)(cls,
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
[VolumeShader](volume_shader.md.md).[Principled](volume_shader.md.md#('geonodes.core.volume_shader.md',).Principled)(cls,
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

[nd](nd.md).[project_point](nd.md#geonodes.core.generated.static_nd.ND.project_point)(cls, vector: Vector = None, transform: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[project_point](matrix.md.md#('geonodes.core.matrix.md',).project_point)(self, vector: Vector = None)
```

## Prune Grid

> `bl_idname` : GeometryNodeGridPrune

### nd

[nd](nd.md).[prune_grid](nd.md#geonodes.core.generated.static_nd.ND.prune_grid)(cls,
                    grid: Float = None,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[prune_grid](float.md.md#('geonodes.core.float.md',).prune_grid)(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Float = None)
```

### class Integer

```python
[Integer](integer.md.md).[prune_grid](integer.md.md#('geonodes.core.integer.md',).prune_grid)(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Integer = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[prune_grid](boolean.md.md#('geonodes.core.boolean.md',).prune_grid)(self, mode: Literal['Inactive', 'Threshold', 'SDF'] = None)
```

### class Vector

```python
[Vector](vector.md.md).[prune_grid](vector.md.md#('geonodes.core.vector.md',).prune_grid)(self,
                    mode: Literal['Inactive', 'Threshold', 'SDF'] = None,
                    threshold: Vector = None)
```

## Quadratic Bézier

> `bl_idname` : GeometryNodeCurveQuadraticBezier

### nd

[nd](nd.md).[quadratic_bezier](nd.md#geonodes.core.generated.static_nd.ND.quadratic_bezier)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None)

### class Curve

```python
[Curve](curve.md.md).[QuadraticBezier](curve.md.md#('geonodes.core.curve.md',).QuadraticBezier)(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None)
```

## Quadrilateral

> `bl_idname` : GeometryNodeCurvePrimitiveQuadrilateral

### nd

[nd](nd.md).[quadrilateral](nd.md#geonodes.core.generated.static_nd.ND.quadrilateral)(cls,
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
[Curve](curve.md.md).[QuadrilateralRectangle](curve.md.md#('geonodes.core.curve.md',).QuadrilateralRectangle)(cls, width: Float = None, height: Float = None)
```

```python
[Curve](curve.md.md).[QuadrilateralParallelogram](curve.md.md#('geonodes.core.curve.md',).QuadrilateralParallelogram)(cls, width: Float = None, height: Float = None, offset: Float = None)
```

```python
[Curve](curve.md.md).[QuadrilateralTrapezoid](curve.md.md#('geonodes.core.curve.md',).QuadrilateralTrapezoid)(cls,
                    height: Float = None,
                    bottom_width: Float = None,
                    top_width: Float = None,
                    offset: Float = None)
```

```python
[Curve](curve.md.md).[QuadrilateralKite](curve.md.md#('geonodes.core.curve.md',).QuadrilateralKite)(cls,
                    width: Float = None,
                    bottom_height: Float = None,
                    top_height: Float = None)
```

```python
[Curve](curve.md.md).[QuadrilateralPoints](curve.md.md#('geonodes.core.curve.md',).QuadrilateralPoints)(cls,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    point_4: Vector = None)
```

```python
[Curve](curve.md.md).[Quadrilateral](curve.md.md#('geonodes.core.curve.md',).Quadrilateral)(cls,
                    width: Float = None,
                    height: Float = None,
                    mode: Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE')
```

## Quaternion to Rotation

> `bl_idname` : FunctionNodeQuaternionToRotation

### nd

[nd](nd.md).[quaternion_to_rotation](nd.md#geonodes.core.generated.static_nd.ND.quaternion_to_rotation)(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None)

### class Rotation

```python
[Rotation](rotation.md.md).[FromQuaternion](rotation.md.md#('geonodes.core.rotation.md',).FromQuaternion)(cls, w: Float = None, x: Float = None, y: Float = None, z: Float = None)
```

## RGB Curves

> `bl_idname` : ShaderNodeRGBCurve

### nd

[nd](nd.md).[rgb_curves](nd.md#geonodes.core.generated.static_nd.ND.rgb_curves)(cls, color: Color = None, factor: Float = None)

### snd

[snd](snd.md).[rgb_curves](snd.md#geonodes.core.generated.static_snd.SND.rgb_curves)(cls, color: Color = None, factor: Float = None)

## RGB to BW

> `bl_idname` : ShaderNodeRGBToBW

### snd

[snd](snd.md).[rgb_to_bw](snd.md#geonodes.core.generated.static_snd.SND.rgb_to_bw)(cls, color: Color = None)

### class Color

```python
[Color](color.md.md).[rgb_to_bw](color.md.md#('geonodes.core.color.md',).rgb_to_bw)(self)
```

## Radial Tiling

> `bl_idname` : ShaderNodeRadialTiling

### nd

[nd](nd.md).[radial_tiling](nd.md#geonodes.core.generated.static_nd.ND.radial_tiling)(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False)

### snd

[snd](snd.md).[radial_tiling](snd.md#geonodes.core.generated.static_snd.SND.radial_tiling)(cls,
                    vector: Vector = None,
                    sides: Float = None,
                    roundness: Float = None,
                    normalize = False)

### class Vector

```python
[Vector](vector.md.md).[radial_tiling](vector.md.md#('geonodes.core.vector.md',).radial_tiling)(self, sides: Float = None, roundness: Float = None, normalize = False)
```

## Radius

> `bl_idname` : GeometryNodeInputRadius

### nd

[nd](nd.md).[radius](nd.md#geonodes.core.generated.static_nd.ND.radius)(self)

### class Cloud

```python
prop = [Cloud](cloud.md.md).[radius](cloud.md.md#('geonodes.core.cloud.md',).radius)
```

### class CloudPoint

```python
prop = [CloudPoint](cloud_point.md.md).[radius](cloud_point.md.md#('geonodes.core.cloud_point.md',).radius)
```

### class Curve

```python
prop = [Curve](curve.md.md).[radius](curve.md.md#('geonodes.core.curve.md',).radius)
```

### class SplinePoint

```python
prop = [SplinePoint](spline_point.md.md).[radius](spline_point.md.md#('geonodes.core.spline_point.md',).radius)
```

## Random Value

> `bl_idname` : FunctionNodeRandomValue

### nd

[nd](nd.md).[random_value](nd.md#geonodes.core.generated.static_nd.ND.random_value)(cls,
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
[Float](float.md.md).[Random](float.md.md#('geonodes.core.float.md',).Random)(cls,
                    min: Float = None,
                    max: Float = None,
                    id: Integer = None,
                    seed: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[Random](integer.md.md#('geonodes.core.integer.md',).Random)(cls,
                    min: Integer = None,
                    max: Integer = None,
                    id: Integer = None,
                    seed: Integer = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[Random](boolean.md.md#('geonodes.core.boolean.md',).Random)(cls, probability: Float = None, id: Integer = None, seed: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[Random](vector.md.md#('geonodes.core.vector.md',).Random)(cls,
                    min: Vector = None,
                    max: Vector = None,
                    id: Integer = None,
                    seed: Integer = None)
```

## Ray Portal BSDF

> `bl_idname` : ShaderNodeBsdfRayPortal

### snd

[snd](snd.md).[ray_portal_bsdf](snd.md#geonodes.core.generated.static_snd.SND.ray_portal_bsdf)(cls,
                    color: Color = None,
                    position: Vector = None,
                    direction: Vector = None,
                    weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[RayPortal](shader.md.md#('geonodes.core.shader.md',).RayPortal)(cls, color: Color = None, position: Vector = None, direction: Vector = None)
```

## Raycast

> `bl_idname` : ShaderNodeRaycast

### snd

[snd](snd.md).[raycast](snd.md#geonodes.core.generated.static_snd.SND.raycast)(cls,
                    position: Vector = None,
                    direction: Vector = None,
                    length: Float = None,
                    only_local = False)

### class Vector

```python
[Vector](vector.md.md).[raycast](vector.md.md#('geonodes.core.vector.md',).raycast)(self, direction: Vector = None, length: Float = None, only_local = False)
```

## Realize Instances

> `bl_idname` : GeometryNodeRealizeInstances

### nd

[nd](nd.md).[realize_instances](nd.md#geonodes.core.generated.static_nd.ND.realize_instances)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    realize_all: Boolean = None,
                    depth: Integer = None,
                    realize_to_point_domain = False)

### class Geometry

```python
[Geometry](geometry.md.md).[realize](geometry.md.md#('geonodes.core.geometry.md',).realize)(self,
                    realize_all: Boolean = None,
                    depth: Integer = None,
                    realize_to_point_domain = False)
```

## Refraction BSDF

> `bl_idname` : ShaderNodeBsdfRefraction

### snd

[snd](snd.md).[refraction_bsdf](snd.md#geonodes.core.generated.static_snd.SND.refraction_bsdf)(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    distribution: Literal['BECKMANN', 'GGX'] = 'BECKMANN')

### class Shader

```python
[Shader](shader.md.md).[Refraction](shader.md.md#('geonodes.core.shader.md',).Refraction)(cls,
                    color: Color = None,
                    roughness: Float = None,
                    ior: Float = None,
                    normal: Vector = None,
                    distribution: Literal['BECKMANN', 'GGX'] = 'BECKMANN')
```

## Remove Named Attribute

> `bl_idname` : GeometryNodeRemoveAttribute

### nd

[nd](nd.md).[remove_named_attribute](nd.md#geonodes.core.generated.static_nd.ND.remove_named_attribute)(cls,
                    geometry: Geometry = None,
                    pattern_mode: Literal['Exact', 'Wildcard'] = None,
                    name: String = None)

### class Geometry

```python
[Geometry](geometry.md.md).[remove_named_attribute](geometry.md.md#('geonodes.core.geometry.md',).remove_named_attribute)(self, pattern_mode: Literal['Exact', 'Wildcard'] = None, name: String = None)
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

[nd](nd.md).[replace_material](nd.md#geonodes.core.generated.static_nd.ND.replace_material)(cls, geometry: Geometry = None, old: Material = None, new: Material = None)

### class Geometry

```python
[Geometry](geometry.md.md).[replace_material](geometry.md.md#('geonodes.core.geometry.md',).replace_material)(self, old: Material = None, new: Material = None)
```

## Replace String

> `bl_idname` : FunctionNodeReplaceString

### nd

[nd](nd.md).[replace_string](nd.md#geonodes.core.generated.static_nd.ND.replace_string)(cls, string: String = None, find: String = None, replace: String = None)

### class String

```python
[String](string.md.md).[replace](string.md.md#('geonodes.core.string.md',).replace)(self, find: String = None, replace: String = None)
```

## Reroute

> `bl_idname` : NodeReroute

### nd

[nd](nd.md).[reroute](nd.md#geonodes.core.generated.static_nd.ND.reroute)(cls, input: Color = None, socket_idname = 'NodeSocketColor')

### snd

[snd](snd.md).[reroute](snd.md#geonodes.core.generated.static_snd.SND.reroute)(cls, input: Color = None, socket_idname = 'NodeSocketColor')

## Resample Curve

> `bl_idname` : GeometryNodeResampleCurve

### nd

[nd](nd.md).[resample_curve](nd.md#geonodes.core.generated.static_nd.ND.resample_curve)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True)

### class Curve

```python
[Curve](curve.md.md).[resample](curve.md.md#('geonodes.core.curve.md',).resample)(self,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True)
```

## Reverse Curve

> `bl_idname` : GeometryNodeReverseCurve

### nd

[nd](nd.md).[reverse_curve](nd.md#geonodes.core.generated.static_nd.ND.reverse_curve)(cls, curve: Curve = None, selection: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[reverse](curve.md.md#('geonodes.core.curve.md',).reverse)(self)
```

## Rotate Instances

> `bl_idname` : GeometryNodeRotateInstances

### nd

[nd](nd.md).[rotate_instances](nd.md#geonodes.core.generated.static_nd.ND.rotate_instances)(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
[Instances](instances.md.md).[rotate](instances.md.md#('geonodes.core.instances.md',).rotate)(self,
                    rotation: Rotation = None,
                    pivot_point: Vector = None,
                    local_space: Boolean = None)
```

## Rotate Rotation

> `bl_idname` : FunctionNodeRotateRotation

### nd

[nd](nd.md).[rotate_rotation](nd.md#geonodes.core.generated.static_nd.ND.rotate_rotation)(cls,
                    rotation: Rotation = None,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL')

### class Rotation

```python
[Rotation](rotation.md.md).[rotate](rotation.md.md#('geonodes.core.rotation.md',).rotate)(self,
                    rotate_by: Rotation = None,
                    rotation_space: Literal['GLOBAL', 'LOCAL'] = 'GLOBAL')
```

```python
[Rotation](rotation.md.md).[rotate_global](rotation.md.md#('geonodes.core.rotation.md',).rotate_global)(self, rotate_by: Rotation = None)
```

```python
[Rotation](rotation.md.md).[rotate_local](rotation.md.md#('geonodes.core.rotation.md',).rotate_local)(self, rotate_by: Rotation = None)
```

## Rotate Vector

> `bl_idname` : FunctionNodeRotateVector

### nd

[nd](nd.md).[rotate_vector](nd.md#geonodes.core.generated.static_nd.ND.rotate_vector)(cls, vector: Vector = None, rotation: Rotation = None)

### class Rotation

```python
[Rotation](rotation.md.md).[rotate_vector](rotation.md.md#('geonodes.core.rotation.md',).rotate_vector)(self, vector: Vector = None)
```

## Rotation

> `bl_idname` : FunctionNodeInputRotation

### nd

[nd](nd.md).[rotation](nd.md#geonodes.core.generated.static_nd.ND.rotation)(self)

## Rotation to Axis Angle

> `bl_idname` : FunctionNodeRotationToAxisAngle

### nd

[nd](nd.md).[rotation_to_axis_angle](nd.md#geonodes.core.generated.static_nd.ND.rotation_to_axis_angle)(cls, rotation: Rotation = None)

### class Rotation

```python
[Rotation](rotation.md.md).[to_axis_angle](rotation.md.md#('geonodes.core.rotation.md',).to_axis_angle)(self)
```

```python
prop = [Rotation](rotation.md.md).[axis_angle](rotation.md.md#('geonodes.core.rotation.md',).axis_angle)
```

## Rotation to Euler

> `bl_idname` : FunctionNodeRotationToEuler

### nd

[nd](nd.md).[rotation_to_euler](nd.md#geonodes.core.generated.static_nd.ND.rotation_to_euler)(cls, rotation: Rotation = None)

### class Rotation

```python
[Rotation](rotation.md.md).[to_euler](rotation.md.md#('geonodes.core.rotation.md',).to_euler)(self)
```

## Rotation to Quaternion

> `bl_idname` : FunctionNodeRotationToQuaternion

### nd

[nd](nd.md).[rotation_to_quaternion](nd.md#geonodes.core.generated.static_nd.ND.rotation_to_quaternion)(cls, rotation: Rotation = None)

### class Rotation

```python
[Rotation](rotation.md.md).[to_quaternion](rotation.md.md#('geonodes.core.rotation.md',).to_quaternion)(self)
```

```python
prop = [Rotation](rotation.md.md).[wxyz](rotation.md.md#('geonodes.core.rotation.md',).wxyz)
```

## SDF Grid Boolean

> `bl_idname` : GeometryNodeSDFGridBoolean

### nd

[nd](nd.md).[sdf_grid_boolean](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_boolean)(cls,
                    *grid_2: Float,
                    grid_1: Float = None,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE')

### class Float

```python
[Float](float.md.md).[sdf_grid_boolean](float.md.md#('geonodes.core.float.md',).sdf_grid_boolean)(self,
                    *grid_2: Float,
                    operation: Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE')
```

```python
[Float](float.md.md).[sdf_intersect](float.md.md#('geonodes.core.float.md',).sdf_intersect)(self, *grid: Float)
```

```python
[Float](float.md.md).[sdf_union](float.md.md#('geonodes.core.float.md',).sdf_union)(self, *grid: Float)
```

```python
[Float](float.md.md).[sdf_difference](float.md.md#('geonodes.core.float.md',).sdf_difference)(self, *grid_2: Float)
```

## SDF Grid Fillet

> `bl_idname` : GeometryNodeSDFGridFillet

### nd

[nd](nd.md).[sdf_grid_fillet](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_fillet)(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_fillet](float.md.md#('geonodes.core.float.md',).sdf_grid_fillet)(self, iterations: Integer = None)
```

## SDF Grid Laplacian

> `bl_idname` : GeometryNodeSDFGridLaplacian

### nd

[nd](nd.md).[sdf_grid_laplacian](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_laplacian)(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_laplacian](float.md.md#('geonodes.core.float.md',).sdf_grid_laplacian)(self, iterations: Integer = None)
```

## SDF Grid Mean

> `bl_idname` : GeometryNodeSDFGridMean

### nd

[nd](nd.md).[sdf_grid_mean](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_mean)(cls, grid: Float = None, width: Integer = None, iterations: Integer = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_mean](float.md.md#('geonodes.core.float.md',).sdf_grid_mean)(self, width: Integer = None, iterations: Integer = None)
```

## SDF Grid Mean Curvature

> `bl_idname` : GeometryNodeSDFGridMeanCurvature

### nd

[nd](nd.md).[sdf_grid_mean_curvature](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_mean_curvature)(cls, grid: Float = None, iterations: Integer = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_mean_curvature](float.md.md#('geonodes.core.float.md',).sdf_grid_mean_curvature)(self, iterations: Integer = None)
```

## SDF Grid Median

> `bl_idname` : GeometryNodeSDFGridMedian

### nd

[nd](nd.md).[sdf_grid_median](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_median)(cls, grid: Float = None, width: Integer = None, iterations: Integer = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_median](float.md.md#('geonodes.core.float.md',).sdf_grid_median)(self, width: Integer = None, iterations: Integer = None)
```

## SDF Grid Offset

> `bl_idname` : GeometryNodeSDFGridOffset

### nd

[nd](nd.md).[sdf_grid_offset](nd.md#geonodes.core.generated.static_nd.ND.sdf_grid_offset)(cls, grid: Float = None, distance: Float = None)

### class Float

```python
[Float](float.md.md).[sdf_grid_offset](float.md.md#('geonodes.core.float.md',).sdf_grid_offset)(self, distance: Float = None)
```

## Sample Curve

> `bl_idname` : GeometryNodeSampleCurve

### nd

[nd](nd.md).[sample_curve](nd.md#geonodes.core.generated.static_nd.ND.sample_curve)(cls,
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
[Curve](curve.md.md).[sample_factor](curve.md.md#('geonodes.core.curve.md',).sample_factor)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    use_all_curves = False)
```

```python
[Curve](curve.md.md).[sample_length](curve.md.md#('geonodes.core.curve.md',).sample_length)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    length: Float = None,
                    curve_index: Integer = None,
                    use_all_curves = False)
```

```python
[Curve](curve.md.md).[sample](curve.md.md#('geonodes.core.curve.md',).sample)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR',
                    use_all_curves = False)
```

## Sample Grid

> `bl_idname` : GeometryNodeSampleGrid

### nd

[nd](nd.md).[sample_grid](nd.md#geonodes.core.generated.static_nd.ND.sample_grid)(cls,
                    grid: Float = None,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[sample_grid](float.md.md#('geonodes.core.float.md',).sample_grid)(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Integer

```python
[Integer](integer.md.md).[sample_grid](integer.md.md#('geonodes.core.integer.md',).sample_grid)(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[sample_grid](boolean.md.md#('geonodes.core.boolean.md',).sample_grid)(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

### class Vector

```python
[Vector](vector.md.md).[sample_grid](vector.md.md#('geonodes.core.vector.md',).sample_grid)(self,
                    position: Vector = None,
                    interpolation: Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic'] = None)
```

## Sample Grid Index

> `bl_idname` : GeometryNodeSampleGridIndex

### nd

[nd](nd.md).[sample_grid_index](nd.md#geonodes.core.generated.static_nd.ND.sample_grid_index)(cls,
                    grid: Float = None,
                    x: Integer = None,
                    y: Integer = None,
                    z: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[sample_grid_index](float.md.md#('geonodes.core.float.md',).sample_grid_index)(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[sample_grid_index](integer.md.md#('geonodes.core.integer.md',).sample_grid_index)(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[sample_grid_index](boolean.md.md#('geonodes.core.boolean.md',).sample_grid_index)(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

### class Vector

```python
[Vector](vector.md.md).[sample_grid_index](vector.md.md#('geonodes.core.vector.md',).sample_grid_index)(self, x: Integer = None, y: Integer = None, z: Integer = None)
```

## Sample Index

> `bl_idname` : GeometryNodeSampleIndex

### nd

[nd](nd.md).[sample_index](nd.md#geonodes.core.generated.static_nd.ND.sample_index)(cls,
                    geometry: Geometry = None,
                    value: Float = None,
                    index: Integer = None,
                    clamp = False,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[sample_index](point.md.md#('geonodes.core.point.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Edge

```python
[Edge](edge.md.md).[sample_index](edge.md.md#('geonodes.core.edge.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Face

```python
[Face](face.md.md).[sample_index](face.md.md#('geonodes.core.face.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Corner

```python
[Corner](corner.md.md).[sample_index](corner.md.md#('geonodes.core.corner.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Spline

```python
[Spline](spline.md.md).[sample_index](spline.md.md#('geonodes.core.spline.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Instance

```python
[Instance](instance.md.md).[sample_index](instance.md.md#('geonodes.core.instance.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

### class Layer

```python
[Layer](layer.md.md).[sample_index](layer.md.md#('geonodes.core.layer.md',).sample_index)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False)
```

## Sample Nearest

> `bl_idname` : GeometryNodeSampleNearest

### nd

[nd](nd.md).[sample_nearest](nd.md#geonodes.core.generated.static_nd.ND.sample_nearest)(cls,
                    geometry: Geometry = None,
                    sample_position: Vector = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[sample_nearest](point.md.md#('geonodes.core.point.md',).sample_nearest)(self, sample_position: Vector = None)
```

### class Edge

```python
[Edge](edge.md.md).[sample_nearest](edge.md.md#('geonodes.core.edge.md',).sample_nearest)(self, sample_position: Vector = None)
```

### class Face

```python
[Face](face.md.md).[sample_nearest](face.md.md#('geonodes.core.face.md',).sample_nearest)(self, sample_position: Vector = None)
```

### class Corner

```python
[Corner](corner.md.md).[sample_nearest](corner.md.md#('geonodes.core.corner.md',).sample_nearest)(self, sample_position: Vector = None)
```

## Sample Nearest Surface

> `bl_idname` : GeometryNodeSampleNearestSurface

### nd

[nd](nd.md).[sample_nearest_surface](nd.md#geonodes.core.generated.static_nd.ND.sample_nearest_surface)(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Mesh

```python
[Mesh](mesh.md.md).[sample_nearest_surface](mesh.md.md#('geonodes.core.mesh.md',).sample_nearest_surface)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None)
```

## Sample UV Surface

> `bl_idname` : GeometryNodeSampleUVSurface

### nd

[nd](nd.md).[sample_uv_surface](nd.md#geonodes.core.generated.static_nd.ND.sample_uv_surface)(cls,
                    mesh: Mesh = None,
                    value: Float = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4'] = 'FLOAT')

### class Mesh

```python
[Mesh](mesh.md.md).[sample_uv_surface](mesh.md.md#('geonodes.core.mesh.md',).sample_uv_surface)(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    uv_map: Vector = None,
                    sample_uv: Vector = None)
```

## Scale Elements

> `bl_idname` : GeometryNodeScaleElements

### nd

[nd](nd.md).[scale_elements](nd.md#geonodes.core.generated.static_nd.ND.scale_elements)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None,
                    domain: Literal['FACE', 'EDGE'] = 'FACE')

### class Face

```python
[Face](face.md.md).[scale](face.md.md#('geonodes.core.face.md',).scale)(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None)
```

### class Edge

```python
[Edge](edge.md.md).[scale](edge.md.md#('geonodes.core.edge.md',).scale)(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None)
```

## Scale Instances

> `bl_idname` : GeometryNodeScaleInstances

### nd

[nd](nd.md).[scale_instances](nd.md#geonodes.core.generated.static_nd.ND.scale_instances)(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    scale: Vector = None,
                    center: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
[Instances](instances.md.md).[scale](instances.md.md#('geonodes.core.instances.md',).scale)(self, scale: Vector = None, center: Vector = None, local_space: Boolean = None)
```

## Scene Time

> `bl_idname` : GeometryNodeInputSceneTime

### nd

[nd](nd.md).[scene_time](nd.md#geonodes.core.generated.static_nd.ND.scene_time)(cls)

### class Float

```python
prop = [Float](float.md.md).[scene_time](float.md.md#('geonodes.core.float.md',).scene_time)
```

```python
prop = [Float](float.md.md).[seconds](float.md.md#('geonodes.core.float.md',).seconds)
```

```python
prop = [Float](float.md.md).[frame](float.md.md#('geonodes.core.float.md',).frame)
```

## Script

> `bl_idname` : ShaderNodeScript

### snd

[snd](snd.md).[script](snd.md#geonodes.core.generated.static_snd.SND.script)(cls,
                    bytecode = '',
                    bytecode_hash = '',
                    filepath = '',
                    mode: Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL',
                    script = None,
                    use_auto_update = False)

## Selection

> `bl_idname` : GeometryNodeToolSelection

### nd

[nd](nd.md).[selection](nd.md#geonodes.core.generated.static_nd.ND.selection)(cls)

## Self Object

> `bl_idname` : GeometryNodeSelfObject

### nd

[nd](nd.md).[self_object](nd.md#geonodes.core.generated.static_nd.ND.self_object)(self)

### class Object

```python
[Object](object.md.md).[Self](object.md.md#('geonodes.core.object.md',).Self)(cls)
```

## Separate Bundle

> `bl_idname` : NodeSeparateBundle

### nd

[nd](nd.md).[separate_bundle](nd.md#geonodes.core.generated.static_nd.ND.separate_bundle)(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets)

### snd

[snd](snd.md).[separate_bundle](snd.md#geonodes.core.generated.static_snd.SND.separate_bundle)(cls,
                    named_sockets: dict = {},
                    bundle: Bundle = None,
                    define_signature = False,
                    **sockets)

### class Bundle

```python
[Bundle](bundle.md.md).[separate_bundle](bundle.md.md#('geonodes.core.bundle.md',).separate_bundle)(self, named_sockets: dict = {}, define_signature = False, **sockets)
```

## Separate Color

> `bl_idname` : ShaderNodeSeparateColor

### snd

[snd](snd.md).[separate_color](snd.md#geonodes.core.generated.static_snd.SND.separate_color)(cls, color: Color = None, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')

### class Color

```python
[Color](color.md.md).[separate_col_RGB](color.md.md#('geonodes.core.color.md',).separate_col_RGB)(self)
```

```python
[Color](color.md.md).[separate_col_HSV](color.md.md#('geonodes.core.color.md',).separate_col_HSV)(self)
```

```python
[Color](color.md.md).[separate_col_HSL](color.md.md#('geonodes.core.color.md',).separate_col_HSL)(self)
```

```python
[Color](color.md.md).[separate_col](color.md.md#('geonodes.core.color.md',).separate_col)(self, mode: Literal['RGB', 'HSV', 'HSL'] = 'RGB')
```

## Separate Components

> `bl_idname` : GeometryNodeSeparateComponents

### nd

[nd](nd.md).[separate_components](nd.md#geonodes.core.generated.static_nd.ND.separate_components)(cls, geometry: Geometry = None)

### class Geometry

```python
[Geometry](geometry.md.md).[separate_components](geometry.md.md#('geonodes.core.geometry.md',).separate_components)(self)
```

```python
prop = [Geometry](geometry.md.md).[mesh](geometry.md.md#('geonodes.core.geometry.md',).mesh)
```

```python
prop = [Geometry](geometry.md.md).[curve](geometry.md.md#('geonodes.core.geometry.md',).curve)
```

```python
prop = [Geometry](geometry.md.md).[grease_pencil](geometry.md.md#('geonodes.core.geometry.md',).grease_pencil)
```

```python
prop = [Geometry](geometry.md.md).[point_cloud](geometry.md.md#('geonodes.core.geometry.md',).point_cloud)
```

```python
prop = [Geometry](geometry.md.md).[volume](geometry.md.md#('geonodes.core.geometry.md',).volume)
```

```python
prop = [Geometry](geometry.md.md).[instances](geometry.md.md#('geonodes.core.geometry.md',).instances)
```

## Separate Geometry

> `bl_idname` : GeometryNodeSeparateGeometry

### nd

[nd](nd.md).[separate_geometry](nd.md#geonodes.core.generated.static_nd.ND.separate_geometry)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[separate](point.md.md#('geonodes.core.point.md',).separate)(self)
```

### class Edge

```python
[Edge](edge.md.md).[separate](edge.md.md#('geonodes.core.edge.md',).separate)(self)
```

### class Face

```python
[Face](face.md.md).[separate](face.md.md#('geonodes.core.face.md',).separate)(self)
```

### class Spline

```python
[Spline](spline.md.md).[separate](spline.md.md#('geonodes.core.spline.md',).separate)(self)
```

### class Instance

```python
[Instance](instance.md.md).[separate](instance.md.md#('geonodes.core.instance.md',).separate)(self)
```

### class Layer

```python
[Layer](layer.md.md).[separate](layer.md.md#('geonodes.core.layer.md',).separate)(self)
```

## Separate Matrix

> `bl_idname` : FunctionNodeSeparateMatrix

### nd

[nd](nd.md).[separate_matrix](nd.md#geonodes.core.generated.static_nd.ND.separate_matrix)(cls, matrix: Matrix = None)

### class Matrix

```python
prop = [Matrix](matrix.md.md).[as_tuple](matrix.md.md#('geonodes.core.matrix.md',).as_tuple)
```

```python
[Matrix](matrix.md.md).[separate](matrix.md.md#('geonodes.core.matrix.md',).separate)(self)
```

```python
[Matrix](matrix.md.md).[separate_matrix](matrix.md.md#('geonodes.core.matrix.md',).separate_matrix)(self)
```

```python
prop = [Matrix](matrix.md.md).[column_1_row_1](matrix.md.md#('geonodes.core.matrix.md',).column_1_row_1)
```

```python
prop = [Matrix](matrix.md.md).[column_1_row_2](matrix.md.md#('geonodes.core.matrix.md',).column_1_row_2)
```

```python
prop = [Matrix](matrix.md.md).[column_1_row_3](matrix.md.md#('geonodes.core.matrix.md',).column_1_row_3)
```

```python
prop = [Matrix](matrix.md.md).[column_1_row_4](matrix.md.md#('geonodes.core.matrix.md',).column_1_row_4)
```

```python
prop = [Matrix](matrix.md.md).[column_2_row_1](matrix.md.md#('geonodes.core.matrix.md',).column_2_row_1)
```

```python
prop = [Matrix](matrix.md.md).[column_2_row_2](matrix.md.md#('geonodes.core.matrix.md',).column_2_row_2)
```

```python
prop = [Matrix](matrix.md.md).[column_2_row_3](matrix.md.md#('geonodes.core.matrix.md',).column_2_row_3)
```

```python
prop = [Matrix](matrix.md.md).[column_2_row_4](matrix.md.md#('geonodes.core.matrix.md',).column_2_row_4)
```

```python
prop = [Matrix](matrix.md.md).[column_3_row_1](matrix.md.md#('geonodes.core.matrix.md',).column_3_row_1)
```

```python
prop = [Matrix](matrix.md.md).[column_3_row_2](matrix.md.md#('geonodes.core.matrix.md',).column_3_row_2)
```

```python
prop = [Matrix](matrix.md.md).[column_3_row_3](matrix.md.md#('geonodes.core.matrix.md',).column_3_row_3)
```

```python
prop = [Matrix](matrix.md.md).[column_3_row_4](matrix.md.md#('geonodes.core.matrix.md',).column_3_row_4)
```

```python
prop = [Matrix](matrix.md.md).[column_4_row_1](matrix.md.md#('geonodes.core.matrix.md',).column_4_row_1)
```

```python
prop = [Matrix](matrix.md.md).[column_4_row_2](matrix.md.md#('geonodes.core.matrix.md',).column_4_row_2)
```

```python
prop = [Matrix](matrix.md.md).[column_4_row_3](matrix.md.md#('geonodes.core.matrix.md',).column_4_row_3)
```

```python
prop = [Matrix](matrix.md.md).[column_4_row_4](matrix.md.md#('geonodes.core.matrix.md',).column_4_row_4)
```

## Separate Transform

> `bl_idname` : FunctionNodeSeparateTransform

### nd

[nd](nd.md).[separate_transform](nd.md#geonodes.core.generated.static_nd.ND.separate_transform)(cls, transform: Matrix = None)

### class Matrix

```python
prop = [Matrix](matrix.md.md).[trs](matrix.md.md#('geonodes.core.matrix.md',).trs)
```

```python
[Matrix](matrix.md.md).[separate_transform](matrix.md.md#('geonodes.core.matrix.md',).separate_transform)(self)
```

```python
prop = [Matrix](matrix.md.md).[translation](matrix.md.md#('geonodes.core.matrix.md',).translation)
```

```python
prop = [Matrix](matrix.md.md).[rotation](matrix.md.md#('geonodes.core.matrix.md',).rotation)
```

```python
prop = [Matrix](matrix.md.md).[scale](matrix.md.md#('geonodes.core.matrix.md',).scale)
```

## Separate XYZ

> `bl_idname` : ShaderNodeSeparateXYZ

### nd

[nd](nd.md).[separate_xyz](nd.md#geonodes.core.generated.static_nd.ND.separate_xyz)(cls, vector: Vector = None)

### snd

[snd](snd.md).[separate_xyz](snd.md#geonodes.core.generated.static_snd.SND.separate_xyz)(cls, vector: Vector = None)

### class Vector

```python
prop = [Vector](vector.md.md).[xyz](vector.md.md#('geonodes.core.vector.md',).xyz)
```

```python
[Vector](vector.md.md).[separate_xyz](vector.md.md#('geonodes.core.vector.md',).separate_xyz)(self)
```

```python
prop = [Vector](vector.md.md).[x](vector.md.md#('geonodes.core.vector.md',).x)
```

```python
prop = [Vector](vector.md.md).[y](vector.md.md#('geonodes.core.vector.md',).y)
```

```python
prop = [Vector](vector.md.md).[z](vector.md.md#('geonodes.core.vector.md',).z)
```

## Set Curve Normal

> `bl_idname` : GeometryNodeSetCurveNormal

### nd

[nd](nd.md).[set_curve_normal](nd.md#geonodes.core.generated.static_nd.ND.set_curve_normal)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None)

### class Curve

```python
[Curve](curve.md.md).[set_normal](curve.md.md#('geonodes.core.curve.md',).set_normal)(self,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None)
```

```python
[Curve](curve.md.md).[normal](curve.md.md#('geonodes.core.curve.md',).normal) = value
```

### class Spline

```python
[Spline](spline.md.md).[normal](spline.md.md#('geonodes.core.spline.md',).normal) = value
```

## Set Curve Radius

> `bl_idname` : GeometryNodeSetCurveRadius

### nd

[nd](nd.md).[set_curve_radius](nd.md#geonodes.core.generated.static_nd.ND.set_curve_radius)(cls, curve: Curve = None, selection: Boolean = None, radius: Float = None)

### class Curve

```python
[Curve](curve.md.md).[set_radius](curve.md.md#('geonodes.core.curve.md',).set_radius)(self, radius: Float = None)
```

```python
[Curve](curve.md.md).[radius](curve.md.md#('geonodes.core.curve.md',).radius) = value
```

### class SplinePoint

```python
[SplinePoint](spline_point.md.md).[radius](spline_point.md.md#('geonodes.core.spline_point.md',).radius) = value
```

## Set Curve Tilt

> `bl_idname` : GeometryNodeSetCurveTilt

### nd

[nd](nd.md).[set_curve_tilt](nd.md#geonodes.core.generated.static_nd.ND.set_curve_tilt)(cls, curve: Curve = None, selection: Boolean = None, tilt: Float = None)

### class Curve

```python
[Curve](curve.md.md).[set_tilt](curve.md.md#('geonodes.core.curve.md',).set_tilt)(self, tilt: Float = None)
```

```python
[Curve](curve.md.md).[tilt](curve.md.md#('geonodes.core.curve.md',).tilt) = value
```

### class Spline

```python
[Spline](spline.md.md).[tilt](spline.md.md#('geonodes.core.spline.md',).tilt) = value
```

## Set Face Set

> `bl_idname` : GeometryNodeToolSetFaceSet

### nd

[nd](nd.md).[set_face_set](nd.md#geonodes.core.generated.static_nd.ND.set_face_set)(cls, mesh: Mesh = None, selection: Boolean = None, face_set: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[set_face_set](mesh.md.md#('geonodes.core.mesh.md',).set_face_set)(self, face_set: Integer = None)
```

## Set Geometry Bundle

> `bl_idname` : GeometryNodeSetGeometryBundle

### nd

[nd](nd.md).[set_geometry_bundle](nd.md#geonodes.core.generated.static_nd.ND.set_geometry_bundle)(cls, geometry: Geometry = None, bundle: Bundle = None)

## Set Geometry Name

> `bl_idname` : GeometryNodeSetGeometryName

### nd

[nd](nd.md).[set_geometry_name](nd.md#geonodes.core.generated.static_nd.ND.set_geometry_name)(cls, geometry: Geometry = None, name: String = None)

### class Geometry

```python
[Geometry](geometry.md.md).[set_name](geometry.md.md#('geonodes.core.geometry.md',).set_name)(self, name: String = None)
```

```python
[Geometry](geometry.md.md).[name](geometry.md.md#('geonodes.core.geometry.md',).name) = value
```

## Set Grease Pencil Color

> `bl_idname` : GeometryNodeSetGreasePencilColor

### nd

[nd](nd.md).[set_grease_pencil_color](nd.md#geonodes.core.generated.static_nd.ND.set_grease_pencil_color)(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE')

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[set_color_stroke](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).set_color_stroke)(self, color: Color = None, opacity: Float = None)
```

```python
[GreasePencil](grease_pencil.md.md).[set_color_fill](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).set_color_fill)(self, color: Color = None, opacity: Float = None)
```

```python
[GreasePencil](grease_pencil.md.md).[set_color](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).set_color)(self,
                    color: Color = None,
                    opacity: Float = None,
                    mode: Literal['STROKE', 'FILL'] = 'STROKE')
```

```python
[GreasePencil](grease_pencil.md.md).[stroke_color](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).stroke_color) = value
```

```python
[GreasePencil](grease_pencil.md.md).[fill_color](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).fill_color) = value
```

## Set Grease Pencil Depth

> `bl_idname` : GeometryNodeSetGreasePencilDepth

### nd

[nd](nd.md).[set_grease_pencil_depth](nd.md#geonodes.core.generated.static_nd.ND.set_grease_pencil_depth)(cls,
                    grease_pencil: GreasePencil = None,
                    depth_order: Literal['2D', '3D'] = '2D')

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[set_depth](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).set_depth)(self, depth_order: Literal['2D', '3D'] = '2D')
```

```python
[GreasePencil](grease_pencil.md.md).[depth](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).depth) = value
```

## Set Grease Pencil Softness

> `bl_idname` : GeometryNodeSetGreasePencilSoftness

### nd

[nd](nd.md).[set_grease_pencil_softness](nd.md#geonodes.core.generated.static_nd.ND.set_grease_pencil_softness)(cls,
                    grease_pencil: GreasePencil = None,
                    selection: Boolean = None,
                    softness: Float = None)

### class GreasePencil

```python
[GreasePencil](grease_pencil.md.md).[set_softness](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).set_softness)(self, softness: Float = None)
```

```python
[GreasePencil](grease_pencil.md.md).[softness](grease_pencil.md.md#('geonodes.core.grease_pencil.md',).softness) = value
```

## Set Grid Background

> `bl_idname` : GeometryNodeSetGridBackground

### nd

[nd](nd.md).[set_grid_background](nd.md#geonodes.core.generated.static_nd.ND.set_grid_background)(cls,
                    grid: Float = None,
                    background: Float = None,
                    update_inactive: Boolean = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[set_grid_background](float.md.md#('geonodes.core.float.md',).set_grid_background)(self, background: Float = None, update_inactive: Boolean = None)
```

### class Integer

```python
[Integer](integer.md.md).[set_grid_background](integer.md.md#('geonodes.core.integer.md',).set_grid_background)(self, background: Integer = None, update_inactive: Boolean = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[set_grid_background](boolean.md.md#('geonodes.core.boolean.md',).set_grid_background)(self, background: Boolean = None, update_inactive: Boolean = None)
```

### class Vector

```python
[Vector](vector.md.md).[set_grid_background](vector.md.md#('geonodes.core.vector.md',).set_grid_background)(self, background: Vector = None, update_inactive: Boolean = None)
```

## Set Grid Transform

> `bl_idname` : GeometryNodeSetGridTransform

### nd

[nd](nd.md).[set_grid_transform](nd.md#geonodes.core.generated.static_nd.ND.set_grid_transform)(cls,
                    grid: Float = None,
                    transform: Matrix = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[set_grid_transform](float.md.md#('geonodes.core.float.md',).set_grid_transform)(self, transform: Matrix = None)
```

### class Integer

```python
[Integer](integer.md.md).[set_grid_transform](integer.md.md#('geonodes.core.integer.md',).set_grid_transform)(self, transform: Matrix = None)
```

### class Boolean

```python
[Boolean](boolean.md.md).[set_grid_transform](boolean.md.md#('geonodes.core.boolean.md',).set_grid_transform)(self, transform: Matrix = None)
```

### class Vector

```python
[Vector](vector.md.md).[set_grid_transform](vector.md.md#('geonodes.core.vector.md',).set_grid_transform)(self, transform: Matrix = None)
```

## Set Handle Positions

> `bl_idname` : GeometryNodeSetCurveHandlePositions

### nd

[nd](nd.md).[set_handle_positions](nd.md#geonodes.core.generated.static_nd.ND.set_handle_positions)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT')

### class Curve

```python
[Curve](curve.md.md).[set_handle_positions](curve.md.md#('geonodes.core.curve.md',).set_handle_positions)(self,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT')
```

```python
[Curve](curve.md.md).[set_left_handle_positions](curve.md.md#('geonodes.core.curve.md',).set_left_handle_positions)(self, position: Vector = None, offset: Vector = None)
```

```python
[Curve](curve.md.md).[set_right_handle_positions](curve.md.md#('geonodes.core.curve.md',).set_right_handle_positions)(self, position: Vector = None, offset: Vector = None)
```

```python
[Curve](curve.md.md).[left_handle_position](curve.md.md#('geonodes.core.curve.md',).left_handle_position) = value
```

```python
[Curve](curve.md.md).[right_handle_position](curve.md.md#('geonodes.core.curve.md',).right_handle_position) = value
```

```python
[Curve](curve.md.md).[left_handle_offset](curve.md.md#('geonodes.core.curve.md',).left_handle_offset) = value
```

```python
[Curve](curve.md.md).[right_handle_offset](curve.md.md#('geonodes.core.curve.md',).right_handle_offset) = value
```

## Set Handle Type

> `bl_idname` : GeometryNodeCurveSetHandles

### nd

[nd](nd.md).[set_handle_type](nd.md#geonodes.core.generated.static_nd.ND.set_handle_type)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})

### class Curve

```python
[Curve](curve.md.md).[set_handle_type](curve.md.md#('geonodes.core.curve.md',).set_handle_type)(self,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'})
```

```python
[Curve](curve.md.md).[set_left_handle_type](curve.md.md#('geonodes.core.curve.md',).set_left_handle_type)(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
[Curve](curve.md.md).[set_right_handle_type](curve.md.md#('geonodes.core.curve.md',).set_right_handle_type)(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
[Curve](curve.md.md).[set_both_handle_type](curve.md.md#('geonodes.core.curve.md',).set_both_handle_type)(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO')
```

```python
[Curve](curve.md.md).[handle_type](curve.md.md#('geonodes.core.curve.md',).handle_type) = value
```

```python
[Curve](curve.md.md).[left_handle_type](curve.md.md#('geonodes.core.curve.md',).left_handle_type) = value
```

```python
[Curve](curve.md.md).[right_handle_type](curve.md.md#('geonodes.core.curve.md',).right_handle_type) = value
```

## Set ID

> `bl_idname` : GeometryNodeSetID

### nd

[nd](nd.md).[set_id](nd.md#geonodes.core.generated.static_nd.ND.set_id)(cls, geometry: Geometry = None, selection: Boolean = None, id: Integer = None)

### class Geometry

```python
[Geometry](geometry.md.md).[set_id](geometry.md.md#('geonodes.core.geometry.md',).set_id)(self, id: Integer = None)
```

```python
[Geometry](geometry.md.md).[id](geometry.md.md#('geonodes.core.geometry.md',).id) = value
```

## Set Instance Transform

> `bl_idname` : GeometryNodeSetInstanceTransform

### nd

[nd](nd.md).[set_instance_transform](nd.md#geonodes.core.generated.static_nd.ND.set_instance_transform)(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    transform: Matrix = None)

### class Instances

```python
[Instances](instances.md.md).[set_transform](instances.md.md#('geonodes.core.instances.md',).set_transform)(self, transform: Matrix = None)
```

```python
[Instances](instances.md.md).[transform](instances.md.md#('geonodes.core.instances.md',).transform) = value
```

## Set Material

> `bl_idname` : GeometryNodeSetMaterial

### nd

[nd](nd.md).[set_material](nd.md#geonodes.core.generated.static_nd.ND.set_material)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material: Material = None)

### class Geometry

```python
[Geometry](geometry.md.md).[set_material](geometry.md.md#('geonodes.core.geometry.md',).set_material)(self, material: Material = None)
```

```python
[Geometry](geometry.md.md).[material](geometry.md.md#('geonodes.core.geometry.md',).material) = value
```

### class Face

```python
[Face](face.md.md).[material](face.md.md#('geonodes.core.face.md',).material) = value
```

### class Edge

```python
[Edge](edge.md.md).[material](edge.md.md#('geonodes.core.edge.md',).material) = value
```

## Set Material Index

> `bl_idname` : GeometryNodeSetMaterialIndex

### nd

[nd](nd.md).[set_material_index](nd.md#geonodes.core.generated.static_nd.ND.set_material_index)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    material_index: Integer = None)

### class Geometry

```python
[Geometry](geometry.md.md).[set_material_index](geometry.md.md#('geonodes.core.geometry.md',).set_material_index)(self, material_index: Integer = None)
```

```python
[Geometry](geometry.md.md).[material_index](geometry.md.md#('geonodes.core.geometry.md',).material_index) = value
```

### class Face

```python
[Face](face.md.md).[material_index](face.md.md#('geonodes.core.face.md',).material_index) = value
```

### class Spline

```python
[Spline](spline.md.md).[material_index](spline.md.md#('geonodes.core.spline.md',).material_index) = value
```

## Set Mesh Normal

> `bl_idname` : GeometryNodeSetMeshNormal

### nd

[nd](nd.md).[set_mesh_normal](nd.md#geonodes.core.generated.static_nd.ND.set_mesh_normal)(cls,
                    mesh: Mesh = None,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS')

### class Mesh

```python
[Mesh](mesh.md.md).[set_normal_sharpness](mesh.md.md#('geonodes.core.mesh.md',).set_normal_sharpness)(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
[Mesh](mesh.md.md).[set_normal_free](mesh.md.md#('geonodes.core.mesh.md',).set_normal_free)(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
[Mesh](mesh.md.md).[set_normal_tangent_space](mesh.md.md#('geonodes.core.mesh.md',).set_normal_tangent_space)(self,
                    custom_normal: Vector = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT')
```

```python
[Mesh](mesh.md.md).[set_normal](mesh.md.md#('geonodes.core.mesh.md',).set_normal)(self,
                    remove_custom: Boolean = None,
                    edge_sharpness: Boolean = None,
                    face_sharpness: Boolean = None,
                    domain: Literal['POINT', 'FACE', 'CORNER'] = 'POINT',
                    mode: Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS')
```

```python
[Mesh](mesh.md.md).[normal](mesh.md.md#('geonodes.core.mesh.md',).normal) = value
```

### class Point

```python
[Point](point.md.md).[normal](point.md.md#('geonodes.core.point.md',).normal) = value
```

### class Face

```python
[Face](face.md.md).[normal](face.md.md#('geonodes.core.face.md',).normal) = value
```

### class Corner

```python
[Corner](corner.md.md).[normal](corner.md.md#('geonodes.core.corner.md',).normal) = value
```

## Set Point Radius

> `bl_idname` : GeometryNodeSetPointRadius

### nd

[nd](nd.md).[set_point_radius](nd.md#geonodes.core.generated.static_nd.ND.set_point_radius)(cls, points: Cloud = None, selection: Boolean = None, radius: Float = None)

### class Point

```python
[Point](point.md.md).[set_radius](point.md.md#('geonodes.core.point.md',).set_radius)(self, radius: Float = None)
```

### class Cloud

```python
[Cloud](cloud.md.md).[radius](cloud.md.md#('geonodes.core.cloud.md',).radius) = value
```

### class CloudPoint

```python
[CloudPoint](cloud_point.md.md).[radius](cloud_point.md.md#('geonodes.core.cloud_point.md',).radius) = value
```

## Set Position

> `bl_idname` : GeometryNodeSetPosition

### nd

[nd](nd.md).[set_position](nd.md#geonodes.core.generated.static_nd.ND.set_position)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    position: Vector = None,
                    offset: Vector = None)

### class Geometry

```python
[Geometry](geometry.md.md).[set_position](geometry.md.md#('geonodes.core.geometry.md',).set_position)(self, position: Vector = None, offset: Vector = None)
```

```python
[Geometry](geometry.md.md).[position](geometry.md.md#('geonodes.core.geometry.md',).position) = value
```

```python
[Geometry](geometry.md.md).[offset](geometry.md.md#('geonodes.core.geometry.md',).offset) = value
```

### class Point

```python
[Point](point.md.md).[position](point.md.md#('geonodes.core.point.md',).position) = value
```

```python
[Point](point.md.md).[offset](point.md.md#('geonodes.core.point.md',).offset) = value
```

## Set Selection

> `bl_idname` : GeometryNodeToolSetSelection

### nd

[nd](nd.md).[set_selection](nd.md#geonodes.core.generated.static_nd.ND.set_selection)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE'] = 'POINT',
                    selection_type: Literal['BOOLEAN', 'FLOAT'] = 'BOOLEAN')

### class Point

```python
[Point](point.md.md).[set_selection](point.md.md#('geonodes.core.point.md',).set_selection)(self)
```

### class Edge

```python
[Edge](edge.md.md).[set_selection](edge.md.md#('geonodes.core.edge.md',).set_selection)(self)
```

### class Face

```python
[Face](face.md.md).[set_selection](face.md.md#('geonodes.core.face.md',).set_selection)(self)
```

### class Spline

```python
[Spline](spline.md.md).[set_selection](spline.md.md#('geonodes.core.spline.md',).set_selection)(self)
```

## Set Shade Smooth

> `bl_idname` : GeometryNodeSetShadeSmooth

### nd

[nd](nd.md).[set_shade_smooth](nd.md#geonodes.core.generated.static_nd.ND.set_shade_smooth)(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    shade_smooth: Boolean = None,
                    domain: Literal['EDGE', 'FACE'] = 'FACE')

### class Edge

```python
[Edge](edge.md.md).[set_shade_smooth](edge.md.md#('geonodes.core.edge.md',).set_shade_smooth)(self, shade_smooth: Boolean = None)
```

```python
[Edge](edge.md.md).[shade_smooth](edge.md.md#('geonodes.core.edge.md',).shade_smooth) = value
```

```python
[Edge](edge.md.md).[smooth](edge.md.md#('geonodes.core.edge.md',).smooth) = value
```

### class Face

```python
[Face](face.md.md).[set_shade_smooth](face.md.md#('geonodes.core.face.md',).set_shade_smooth)(self, shade_smooth: Boolean = None)
```

```python
[Face](face.md.md).[shade_smooth](face.md.md#('geonodes.core.face.md',).shade_smooth) = value
```

```python
[Face](face.md.md).[smooth](face.md.md#('geonodes.core.face.md',).smooth) = value
```

## Set Spline Cyclic

> `bl_idname` : GeometryNodeSetSplineCyclic

### nd

[nd](nd.md).[set_spline_cyclic](nd.md#geonodes.core.generated.static_nd.ND.set_spline_cyclic)(cls, curve: Curve = None, selection: Boolean = None, cyclic: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[set_spline_cyclic](curve.md.md#('geonodes.core.curve.md',).set_spline_cyclic)(self, cyclic: Boolean = None)
```

```python
[Curve](curve.md.md).[is_cyclic](curve.md.md#('geonodes.core.curve.md',).is_cyclic) = value
```

### class Spline

```python
[Spline](spline.md.md).[is_cyclic](spline.md.md#('geonodes.core.spline.md',).is_cyclic) = value
```

## Set Spline Resolution

> `bl_idname` : GeometryNodeSetSplineResolution

### nd

[nd](nd.md).[set_spline_resolution](nd.md#geonodes.core.generated.static_nd.ND.set_spline_resolution)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    resolution: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[set_spline_resolution](curve.md.md#('geonodes.core.curve.md',).set_spline_resolution)(self, resolution: Integer = None)
```

```python
[Curve](curve.md.md).[resolution](curve.md.md#('geonodes.core.curve.md',).resolution) = value
```

### class Spline

```python
[Spline](spline.md.md).[resolution](spline.md.md#('geonodes.core.spline.md',).resolution) = value
```

## Set Spline Type

> `bl_idname` : GeometryNodeCurveSplineType

### nd

[nd](nd.md).[set_spline_type](nd.md#geonodes.core.generated.static_nd.ND.set_spline_type)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY')

### class Curve

```python
[Curve](curve.md.md).[set_spline_type](curve.md.md#('geonodes.core.curve.md',).set_spline_type)(self, spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY')
```

```python
[Curve](curve.md.md).[type](curve.md.md#('geonodes.core.curve.md',).type) = value
```

### class Spline

```python
[Spline](spline.md.md).[type](spline.md.md#('geonodes.core.spline.md',).type) = value
```

## Shader to RGB

> `bl_idname` : ShaderNodeShaderToRGB

### snd

[snd](snd.md).[shader_to_rgb](snd.md#geonodes.core.generated.static_snd.SND.shader_to_rgb)(cls, shader: Shader = None)

### class Shader

```python
[Shader](shader.md.md).[to_rgb](shader.md.md#('geonodes.core.shader.md',).to_rgb)(self)
```

## Sheen BSDF

> `bl_idname` : ShaderNodeBsdfSheen

### snd

[snd](snd.md).[sheen_bsdf](snd.md#geonodes.core.generated.static_snd.SND.sheen_bsdf)(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    distribution: Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER')

### class Shader

```python
[Shader](shader.md.md).[Sheen](shader.md.md#('geonodes.core.shader.md',).Sheen)(cls,
                    color: Color = None,
                    roughness: Float = None,
                    normal: Vector = None,
                    distribution: Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER')
```

## Shortest Edge Paths

> `bl_idname` : GeometryNodeInputShortestEdgePaths

### nd

[nd](nd.md).[shortest_edge_paths](nd.md#geonodes.core.generated.static_nd.ND.shortest_edge_paths)(cls, end_vertex: Boolean = None, edge_cost: Float = None)

### class Mesh

```python
[Mesh](mesh.md.md).[shortest_edge_paths](mesh.md.md#('geonodes.core.mesh.md',).shortest_edge_paths)(cls, end_vertex: Boolean = None, edge_cost: Float = None)
```

### class Edge

```python
[Edge](edge.md.md).[shortest_paths](edge.md.md#('geonodes.core.edge.md',).shortest_paths)(cls, end_vertex: Boolean = None, edge_cost: Float = None)
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

[snd](snd.md).[sky_texture](snd.md#geonodes.core.generated.static_snd.SND.sky_texture)(cls,
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
[Color](color.md.md).[SkyTexture](color.md.md#('geonodes.core.color.md',).SkyTexture)(cls,
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

[nd](nd.md).[slice_string](nd.md#geonodes.core.generated.static_nd.ND.slice_string)(cls, string: String = None, position: Integer = None, length: Integer = None)

### class String

```python
[String](string.md.md).[slice](string.md.md#('geonodes.core.string.md',).slice)(self, position: Integer = None, length: Integer = None)
```

## Sort Elements

> `bl_idname` : GeometryNodeSortElements

### nd

[nd](nd.md).[sort_elements](nd.md#geonodes.core.generated.static_nd.ND.sort_elements)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    sort_weight: Float = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'] = 'POINT')

### class Point

```python
[Point](point.md.md).[sort](point.md.md#('geonodes.core.point.md',).sort)(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Edge

```python
[Edge](edge.md.md).[sort](edge.md.md#('geonodes.core.edge.md',).sort)(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Face

```python
[Face](face.md.md).[sort](face.md.md#('geonodes.core.face.md',).sort)(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Spline

```python
[Spline](spline.md.md).[sort](spline.md.md#('geonodes.core.spline.md',).sort)(self, group_id: Integer = None, sort_weight: Float = None)
```

### class Instance

```python
[Instance](instance.md.md).[sort](instance.md.md#('geonodes.core.instance.md',).sort)(self, group_id: Integer = None, sort_weight: Float = None)
```

## Special Characters

> `bl_idname` : FunctionNodeInputSpecialCharacters

### nd

[nd](nd.md).[special_characters](nd.md#geonodes.core.generated.static_nd.ND.special_characters)(cls)

### class String

```python
prop = [String](string.md.md).[special_characters](string.md.md#('geonodes.core.string.md',).special_characters)
```

```python
prop = [String](string.md.md).[line_break](string.md.md#('geonodes.core.string.md',).line_break)
```

```python
prop = [String](string.md.md).[tab](string.md.md#('geonodes.core.string.md',).tab)
```

## Specular BSDF

> `bl_idname` : ShaderNodeEeveeSpecular

### snd

[snd](snd.md).[specular_bsdf](snd.md#geonodes.core.generated.static_snd.SND.specular_bsdf)(cls,
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
[Shader](shader.md.md).[Specular](shader.md.md#('geonodes.core.shader.md',).Specular)(cls,
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

[nd](nd.md).[spiral](nd.md#geonodes.core.generated.static_nd.ND.spiral)(cls,
                    resolution: Integer = None,
                    rotations: Float = None,
                    start_radius: Float = None,
                    end_radius: Float = None,
                    height: Float = None,
                    reverse: Boolean = None)

### class Curve

```python
[Curve](curve.md.md).[Spiral](curve.md.md#('geonodes.core.curve.md',).Spiral)(cls,
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

[nd](nd.md).[spline_length](nd.md#geonodes.core.generated.static_nd.ND.spline_length)(cls)

### class Curve

```python
[Curve](curve.md.md).[spline_length](curve.md.md#('geonodes.core.curve.md',).spline_length)(cls)
```

### class Spline

```python
prop = [Spline](spline.md.md).[spline_length](spline.md.md#('geonodes.core.spline.md',).spline_length)
```

```python
prop = [Spline](spline.md.md).[length](spline.md.md#('geonodes.core.spline.md',).length)
```

```python
prop = [Spline](spline.md.md).[point_count](spline.md.md#('geonodes.core.spline.md',).point_count)
```

## Spline Parameter

> `bl_idname` : GeometryNodeSplineParameter

### nd

[nd](nd.md).[spline_parameter](nd.md#geonodes.core.generated.static_nd.ND.spline_parameter)(cls)

### class Curve

```python
[Curve](curve.md.md).[spline_parameter](curve.md.md#('geonodes.core.curve.md',).spline_parameter)(cls)
```

### class Spline

```python
prop = [Spline](spline.md.md).[parameter](spline.md.md#('geonodes.core.spline.md',).parameter)
```

```python
prop = [Spline](spline.md.md).[parameter_factor](spline.md.md#('geonodes.core.spline.md',).parameter_factor)
```

```python
prop = [Spline](spline.md.md).[parameter_length](spline.md.md#('geonodes.core.spline.md',).parameter_length)
```

```python
prop = [Spline](spline.md.md).[parameter_index](spline.md.md#('geonodes.core.spline.md',).parameter_index)
```

## Spline Resolution

> `bl_idname` : GeometryNodeInputSplineResolution

### nd

[nd](nd.md).[spline_resolution](nd.md#geonodes.core.generated.static_nd.ND.spline_resolution)(self)

### class Curve

```python
prop = [Curve](curve.md.md).[resolution](curve.md.md#('geonodes.core.curve.md',).resolution)
```

### class Spline

```python
prop = [Spline](spline.md.md).[resolution](spline.md.md#('geonodes.core.spline.md',).resolution)
```

## Split Edges

> `bl_idname` : GeometryNodeSplitEdges

### nd

[nd](nd.md).[split_edges](nd.md#geonodes.core.generated.static_nd.ND.split_edges)(cls, mesh: Mesh = None, selection: Boolean = None)

### class Mesh

```python
[Mesh](mesh.md.md).[split_edges](mesh.md.md#('geonodes.core.mesh.md',).split_edges)(self)
```

### class Edge

```python
[Edge](edge.md.md).[split](edge.md.md#('geonodes.core.edge.md',).split)(self)
```

## Split to Instances

> `bl_idname` : GeometryNodeSplitToInstances

### nd

[nd](nd.md).[split_to_instances](nd.md#geonodes.core.generated.static_nd.ND.split_to_instances)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[split_to_instances](point.md.md#('geonodes.core.point.md',).split_to_instances)(self, group_id: Integer = None)
```

### class Edge

```python
[Edge](edge.md.md).[split_to_instances](edge.md.md#('geonodes.core.edge.md',).split_to_instances)(self, group_id: Integer = None)
```

### class Face

```python
[Face](face.md.md).[split_to_instances](face.md.md#('geonodes.core.face.md',).split_to_instances)(self, group_id: Integer = None)
```

### class Spline

```python
[Spline](spline.md.md).[split_to_instances](spline.md.md#('geonodes.core.spline.md',).split_to_instances)(self, group_id: Integer = None)
```

### class Instance

```python
[Instance](instance.md.md).[split_to_instances](instance.md.md#('geonodes.core.instance.md',).split_to_instances)(self, group_id: Integer = None)
```

### class Layer

```python
[Layer](layer.md.md).[split_to_instances](layer.md.md#('geonodes.core.layer.md',).split_to_instances)(self, group_id: Integer = None)
```

## Star

> `bl_idname` : GeometryNodeCurveStar

### nd

[nd](nd.md).[star](nd.md#geonodes.core.generated.static_nd.ND.star)(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None)

### class Curve

```python
[Curve](curve.md.md).[Star](curve.md.md#('geonodes.core.curve.md',).Star)(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None)
```

## Store Bundle Item

> `bl_idname` : NodeStoreBundleItem

### nd

[nd](nd.md).[store_bundle_item](nd.md#geonodes.core.generated.static_nd.ND.store_bundle_item)(cls,
                    bundle: Bundle = None,
                    path: String = None,
                    item: Float = None,
                    socket_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT'] = 'FLOAT',
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')

### class Bundle

```python
[Bundle](bundle.md.md).[set_item](bundle.md.md#('geonodes.core.bundle.md',).set_item)(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

```python
[Bundle](bundle.md.md).[store_item](bundle.md.md#('geonodes.core.bundle.md',).store_item)(self,
                    path: String = None,
                    item: Float = None,
                    structure_type: Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO')
```

## Store Named Attribute

> `bl_idname` : GeometryNodeStoreNamedAttribute

### nd

[nd](nd.md).[store_named_attribute](nd.md#geonodes.core.generated.static_nd.ND.store_named_attribute)(cls,
                    geometry: Geometry = None,
                    selection: Boolean = None,
                    name: String = None,
                    value: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'INT8', 'FLOAT2', 'BYTE_COLOR'] = 'FLOAT',
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT')

### class Point

```python
[Point](point.md.md).[store_named_attribute](point.md.md#('geonodes.core.point.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Point](point.md.md).[store](point.md.md#('geonodes.core.point.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Edge

```python
[Edge](edge.md.md).[store_named_attribute](edge.md.md#('geonodes.core.edge.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Edge](edge.md.md).[store](edge.md.md#('geonodes.core.edge.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Face

```python
[Face](face.md.md).[store_named_attribute](face.md.md#('geonodes.core.face.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Face](face.md.md).[store](face.md.md#('geonodes.core.face.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Corner

```python
[Corner](corner.md.md).[store_named_attribute](corner.md.md#('geonodes.core.corner.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Corner](corner.md.md).[store](corner.md.md#('geonodes.core.corner.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Corner](corner.md.md).[store_uv](corner.md.md#('geonodes.core.corner.md',).store_uv)(self, name: String = None, value: Vector = None)
```

### class Spline

```python
[Spline](spline.md.md).[store_named_attribute](spline.md.md#('geonodes.core.spline.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Spline](spline.md.md).[store](spline.md.md#('geonodes.core.spline.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Instance

```python
[Instance](instance.md.md).[store_named_attribute](instance.md.md#('geonodes.core.instance.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Instance](instance.md.md).[store](instance.md.md#('geonodes.core.instance.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

### class Layer

```python
[Layer](layer.md.md).[store_named_attribute](layer.md.md#('geonodes.core.layer.md',).store_named_attribute)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

```python
[Layer](layer.md.md).[store](layer.md.md#('geonodes.core.layer.md',).store)(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None)
```

## Store Named Grid

> `bl_idname` : GeometryNodeStoreNamedGrid

### nd

[nd](nd.md).[store_named_grid](nd.md#geonodes.core.generated.static_nd.ND.store_named_grid)(cls,
                    volume: Volume = None,
                    name: String = None,
                    grid: Float = None,
                    data_type: Literal['BOOLEAN', 'FLOAT', 'INT', 'VECTOR_FLOAT'] = 'FLOAT')

### class Volume

```python
[Volume](volume.md.md).[store_named_grid](volume.md.md#('geonodes.core.volume.md',).store_named_grid)(self, name: String = None, grid: Boolean | Float | Integer | Vector = None)
```

## String

> `bl_idname` : FunctionNodeInputString

### nd

[nd](nd.md).[string](nd.md#geonodes.core.generated.static_nd.ND.string)(cls, string = '')

## String Length

> `bl_idname` : FunctionNodeStringLength

### nd

[nd](nd.md).[string_length](nd.md#geonodes.core.generated.static_nd.ND.string_length)(cls, string: String = None)

### class String

```python
[String](string.md.md).[length](string.md.md#('geonodes.core.string.md',).length)(self)
```

## String to Curves

> `bl_idname` : GeometryNodeStringToCurves

### nd

[nd](nd.md).[string_to_curves](nd.md#geonodes.core.generated.static_nd.ND.string_to_curves)(cls,
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
[String](string.md.md).[to_curves](string.md.md#('geonodes.core.string.md',).to_curves)(self,
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

[nd](nd.md).[string_to_value](nd.md#geonodes.core.generated.static_nd.ND.string_to_value)(cls, string: String = None, data_type: Literal['FLOAT', 'INT'] = 'FLOAT')

### class String

```python
[String](string.md.md).[to_value](string.md.md#('geonodes.core.string.md',).to_value)(self, data_type: Literal['FLOAT', 'INT'] = 'FLOAT')
```

```python
[String](string.md.md).[to_float](string.md.md#('geonodes.core.string.md',).to_float)(self)
```

```python
[String](string.md.md).[to_integer](string.md.md#('geonodes.core.string.md',).to_integer)(self)
```

## Subdivide Curve

> `bl_idname` : GeometryNodeSubdivideCurve

### nd

[nd](nd.md).[subdivide_curve](nd.md#geonodes.core.generated.static_nd.ND.subdivide_curve)(cls, curve: Curve = None, cuts: Integer = None)

### class Curve

```python
[Curve](curve.md.md).[subdivide](curve.md.md#('geonodes.core.curve.md',).subdivide)(self, cuts: Integer = None)
```

## Subdivide Mesh

> `bl_idname` : GeometryNodeSubdivideMesh

### nd

[nd](nd.md).[subdivide_mesh](nd.md#geonodes.core.generated.static_nd.ND.subdivide_mesh)(cls, mesh: Mesh = None, level: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[subdivide](mesh.md.md#('geonodes.core.mesh.md',).subdivide)(self, level: Integer = None)
```

## Subdivision Surface

> `bl_idname` : GeometryNodeSubdivisionSurface

### nd

[nd](nd.md).[subdivision_surface](nd.md#geonodes.core.generated.static_nd.ND.subdivision_surface)(cls,
                    mesh: Mesh = None,
                    level: Integer = None,
                    edge_crease: Float = None,
                    vertex_crease: Float = None,
                    limit_surface: Boolean = None,
                    uv_smooth: Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All'] = None,
                    boundary_smooth: Literal['Keep Corners', 'All'] = None)

### class Mesh

```python
[Mesh](mesh.md.md).[subdivision_surface](mesh.md.md#('geonodes.core.mesh.md',).subdivision_surface)(self,
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

[snd](snd.md).[subsurface_scattering](snd.md#geonodes.core.generated.static_snd.SND.subsurface_scattering)(cls,
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
[Shader](shader.md.md).[SubsurfaceScattering](shader.md.md#('geonodes.core.shader.md',).SubsurfaceScattering)(cls,
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
[Socket](socket.md.md).[Switch](socket.md.md#('geonodes.core.socket.md',).Switch)(condition=None, false=None, true=None)
```

```python
[Socket](socket.md.md).[switch](socket.md.md#('geonodes.core.socket.md',).switch)(condition=None, true=None)
```

## Tangent

> `bl_idname` : ShaderNodeTangent

### snd

[snd](snd.md).[tangent](snd.md#geonodes.core.generated.static_snd.SND.tangent)(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = '')

### class Vector

```python
[Vector](vector.md.md).[Tangent](vector.md.md#('geonodes.core.vector.md',).Tangent)(cls,
                    axis: Literal['X', 'Y', 'Z'] = 'Z',
                    direction_type: Literal['RADIAL', 'UV_MAP'] = 'RADIAL',
                    uv_map = '')
```

## Texture Coordinate

> `bl_idname` : ShaderNodeTexCoord

### snd

[snd](snd.md).[texture_coordinate](snd.md#geonodes.core.generated.static_snd.SND.texture_coordinate)(cls, from_instancer = False, object = None)

## Toon BSDF

> `bl_idname` : ShaderNodeBsdfToon

### snd

[snd](snd.md).[toon_bsdf](snd.md#geonodes.core.generated.static_snd.SND.toon_bsdf)(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    weight: Float = None,
                    component: Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE')

### class Shader

```python
[Shader](shader.md.md).[Toon](shader.md.md#('geonodes.core.shader.md',).Toon)(cls,
                    color: Color = None,
                    size: Float = None,
                    smooth: Float = None,
                    normal: Vector = None,
                    component: Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE')
```

## Transform Direction

> `bl_idname` : FunctionNodeTransformDirection

### nd

[nd](nd.md).[transform_direction](nd.md#geonodes.core.generated.static_nd.ND.transform_direction)(cls, direction: Vector = None, transform: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[transform_direction](matrix.md.md#('geonodes.core.matrix.md',).transform_direction)(self, direction: Vector = None)
```

## Transform Geometry

> `bl_idname` : GeometryNodeTransform

### nd

[nd](nd.md).[transform_geometry](nd.md#geonodes.core.generated.static_nd.ND.transform_geometry)(cls,
                    geometry: Geometry = None,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None)

### class Geometry

```python
[Geometry](geometry.md.md).[transform](geometry.md.md#('geonodes.core.geometry.md',).transform)(self,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None)
```

## Transform Gizmo

> `bl_idname` : GeometryNodeGizmoTransform

### nd

[nd](nd.md).[transform_gizmo](nd.md#geonodes.core.generated.static_nd.ND.transform_gizmo)(cls,
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
[Matrix](matrix.md.md).[transform_gizmo](matrix.md.md#('geonodes.core.matrix.md',).transform_gizmo)(self,
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

[nd](nd.md).[transform_point](nd.md#geonodes.core.generated.static_nd.ND.transform_point)(cls, vector: Vector = None, transform: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[transform_point](matrix.md.md#('geonodes.core.matrix.md',).transform_point)(self, vector: Vector = None)
```

## Translate Instances

> `bl_idname` : GeometryNodeTranslateInstances

### nd

[nd](nd.md).[translate_instances](nd.md#geonodes.core.generated.static_nd.ND.translate_instances)(cls,
                    instances: Instances = None,
                    selection: Boolean = None,
                    translation: Vector = None,
                    local_space: Boolean = None)

### class Instances

```python
[Instances](instances.md.md).[translate](instances.md.md#('geonodes.core.instances.md',).translate)(self, translation: Vector = None, local_space: Boolean = None)
```

## Translucent BSDF

> `bl_idname` : ShaderNodeBsdfTranslucent

### snd

[snd](snd.md).[translucent_bsdf](snd.md#geonodes.core.generated.static_snd.SND.translucent_bsdf)(cls, color: Color = None, normal: Vector = None, weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[Translucent](shader.md.md#('geonodes.core.shader.md',).Translucent)(cls, color: Color = None, normal: Vector = None)
```

## Transparent BSDF

> `bl_idname` : ShaderNodeBsdfTransparent

### snd

[snd](snd.md).[transparent_bsdf](snd.md#geonodes.core.generated.static_snd.SND.transparent_bsdf)(cls, color: Color = None, weight: Float = None)

### class Shader

```python
[Shader](shader.md.md).[Transparent](shader.md.md#('geonodes.core.shader.md',).Transparent)(cls, color: Color = None)
```

## Transpose Matrix

> `bl_idname` : FunctionNodeTransposeMatrix

### nd

[nd](nd.md).[transpose_matrix](nd.md#geonodes.core.generated.static_nd.ND.transpose_matrix)(cls, matrix: Matrix = None)

### class Matrix

```python
[Matrix](matrix.md.md).[transpose](matrix.md.md#('geonodes.core.matrix.md',).transpose)(self)
```

## Triangulate

> `bl_idname` : GeometryNodeTriangulate

### nd

[nd](nd.md).[triangulate](nd.md#geonodes.core.generated.static_nd.ND.triangulate)(cls,
                    mesh: Mesh = None,
                    selection: Boolean = None,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None)

### class Mesh

```python
[Mesh](mesh.md.md).[triangulate](mesh.md.md#('geonodes.core.mesh.md',).triangulate)(self,
                    quad_method: Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal'] = None,
                    n_gon_method: Literal['Beauty', 'Clip'] = None)
```

## Trim Curve

> `bl_idname` : GeometryNodeTrimCurve

### nd

[nd](nd.md).[trim_curve](nd.md#geonodes.core.generated.static_nd.ND.trim_curve)(cls,
                    curve: Curve = None,
                    selection: Boolean = None,
                    start: Float = None,
                    end: Float = None,
                    start_1: Float = None,
                    end_1: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR')

### class Curve

```python
[Curve](curve.md.md).[trim_factor](curve.md.md#('geonodes.core.curve.md',).trim_factor)(self, start: Float = None, end: Float = None)
```

```python
[Curve](curve.md.md).[trim_length](curve.md.md#('geonodes.core.curve.md',).trim_length)(self, start: Float = None, end: Float = None)
```

```python
[Curve](curve.md.md).[trim](curve.md.md#('geonodes.core.curve.md',).trim)(self,
                    start: Float = None,
                    end: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR')
```

## UV Along Stroke

> `bl_idname` : ShaderNodeUVAlongStroke

### snd

[snd](snd.md).[uv_along_stroke](snd.md#geonodes.core.generated.static_snd.SND.uv_along_stroke)(cls, use_tips = False)

## UV Map

> `bl_idname` : ShaderNodeUVMap

### snd

[snd](snd.md).[uv_map](snd.md#geonodes.core.generated.static_snd.SND.uv_map)(cls, from_instancer = False, uv_map = '')

### class Vector

```python
[Vector](vector.md.md).[UvMap](vector.md.md#('geonodes.core.vector.md',).UvMap)(cls, from_instancer = False, uv_map = '')
```

## UV Sphere

> `bl_idname` : GeometryNodeMeshUVSphere

### nd

[nd](nd.md).[uv_sphere](nd.md#geonodes.core.generated.static_nd.ND.uv_sphere)(cls, segments: Integer = None, rings: Integer = None, radius: Float = None)

### class Mesh

```python
[Mesh](mesh.md.md).[UVSphere](mesh.md.md#('geonodes.core.mesh.md',).UVSphere)(cls, segments: Integer = None, rings: Integer = None, radius: Float = None)
```

## UV Tangent

> `bl_idname` : GeometryNodeUVTangent

### nd

[nd](nd.md).[uv_tangent](nd.md#geonodes.core.generated.static_nd.ND.uv_tangent)(cls, method: Literal['Exact', 'Fast'] = None, uv: Vector = None)

### class Vector

```python
[Vector](vector.md.md).[uv_tangent](vector.md.md#('geonodes.core.vector.md',).uv_tangent)(self, method: Literal['Exact', 'Fast'] = None)
```

## UV Unwrap

> `bl_idname` : GeometryNodeUVUnwrap

### nd

[nd](nd.md).[uv_unwrap](nd.md#geonodes.core.generated.static_nd.ND.uv_unwrap)(cls,
                    selection: Boolean = None,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None)

### class Boolean

```python
[Boolean](boolean.md.md).[uv_unwrap](boolean.md.md#('geonodes.core.boolean.md',).uv_unwrap)(self,
                    seam: Boolean = None,
                    margin: Float = None,
                    fill_holes: Boolean = None,
                    method: Literal['Angle Based', 'Conformal', 'Minimum Stretch'] = None,
                    iterations: Integer = None,
                    no_flip: Boolean = None)
```

### class Corner

```python
[Corner](corner.md.md).[uv_unwrap](corner.md.md#('geonodes.core.corner.md',).uv_unwrap)(cls,
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

[nd](nd.md).[value](nd.md#geonodes.core.generated.static_nd.ND.value)(self)

### snd

[snd](snd.md).[value](snd.md#geonodes.core.generated.static_snd.SND.value)(self)

## Value to String

> `bl_idname` : FunctionNodeValueToString

### nd

[nd](nd.md).[value_to_string](nd.md#geonodes.core.generated.static_nd.ND.value_to_string)(cls,
                    value: Float = None,
                    decimals: Integer = None,
                    data_type: Literal['FLOAT', 'INT'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[to_string](float.md.md#('geonodes.core.float.md',).to_string)(self, decimals: Integer = None)
```

### class Integer

```python
[Integer](integer.md.md).[to_string](integer.md.md#('geonodes.core.integer.md',).to_string)(self)
```

## Vector

> `bl_idname` : FunctionNodeInputVector

### nd

[nd](nd.md).[vector](nd.md#geonodes.core.generated.static_nd.ND.vector)(self)

## Vector Curves

> `bl_idname` : ShaderNodeVectorCurve

### nd

[nd](nd.md).[vector_curves](nd.md#geonodes.core.generated.static_nd.ND.vector_curves)(cls, vector: Vector = None, factor: Float = None)

### snd

[snd](snd.md).[vector_curves](snd.md#geonodes.core.generated.static_snd.SND.vector_curves)(cls, vector: Vector = None, factor: Float = None)

## Vector Displacement

> `bl_idname` : ShaderNodeVectorDisplacement

### snd

[snd](snd.md).[vector_displacement](snd.md#geonodes.core.generated.static_snd.SND.vector_displacement)(cls,
                    vector: Color = None,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT')

### class Color

```python
[Color](color.md.md).[vector_displacement](color.md.md#('geonodes.core.color.md',).vector_displacement)(self,
                    midlevel: Float = None,
                    scale: Float = None,
                    space: Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT')
```

## Vector Math

> `bl_idname` : ShaderNodeVectorMath

### nd

[nd](nd.md).[vector_math](nd.md#geonodes.core.generated.static_nd.ND.vector_math)(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD')

### snd

[snd](snd.md).[vector_math](snd.md#geonodes.core.generated.static_snd.SND.vector_math)(cls,
                    vector: Vector = None,
                    vector_1: Vector = None,
                    vector_2: Vector = None,
                    scale: Float = None,
                    operation: Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD')

### class Vector

```python
[Vector](vector.md.md).[add](vector.md.md#('geonodes.core.vector.md',).add)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[subtract](vector.md.md#('geonodes.core.vector.md',).subtract)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[multiply](vector.md.md#('geonodes.core.vector.md',).multiply)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[divide](vector.md.md#('geonodes.core.vector.md',).divide)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[multiply_add](vector.md.md#('geonodes.core.vector.md',).multiply_add)(self, multiplier: Vector = None, addend: Vector = None)
```

```python
[Vector](vector.md.md).[cross](vector.md.md#('geonodes.core.vector.md',).cross)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[project](vector.md.md#('geonodes.core.vector.md',).project)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[reflect](vector.md.md#('geonodes.core.vector.md',).reflect)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[refract](vector.md.md#('geonodes.core.vector.md',).refract)(self, vector: Vector = None, ior: Float = None)
```

```python
[Vector](vector.md.md).[faceforward](vector.md.md#('geonodes.core.vector.md',).faceforward)(self, incident: Vector = None, reference: Vector = None)
```

```python
[Vector](vector.md.md).[dot](vector.md.md#('geonodes.core.vector.md',).dot)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[distance](vector.md.md#('geonodes.core.vector.md',).distance)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[length](vector.md.md#('geonodes.core.vector.md',).length)(self)
```

```python
[Vector](vector.md.md).[scale](vector.md.md#('geonodes.core.vector.md',).scale)(self, scale: Float = None)
```

```python
[Vector](vector.md.md).[normalize](vector.md.md#('geonodes.core.vector.md',).normalize)(self)
```

```python
[Vector](vector.md.md).[abs](vector.md.md#('geonodes.core.vector.md',).abs)(self)
```

```python
[Vector](vector.md.md).[power](vector.md.md#('geonodes.core.vector.md',).power)(self, exponent: Vector = None)
```

```python
[Vector](vector.md.md).[sign](vector.md.md#('geonodes.core.vector.md',).sign)(self)
```

```python
[Vector](vector.md.md).[min](vector.md.md#('geonodes.core.vector.md',).min)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[max](vector.md.md#('geonodes.core.vector.md',).max)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[round](vector.md.md#('geonodes.core.vector.md',).round)(self)
```

```python
[Vector](vector.md.md).[floor](vector.md.md#('geonodes.core.vector.md',).floor)(self)
```

```python
[Vector](vector.md.md).[ceil](vector.md.md#('geonodes.core.vector.md',).ceil)(self)
```

```python
[Vector](vector.md.md).[fraction](vector.md.md#('geonodes.core.vector.md',).fraction)(self)
```

```python
[Vector](vector.md.md).[modulo](vector.md.md#('geonodes.core.vector.md',).modulo)(self, vector: Vector = None)
```

```python
[Vector](vector.md.md).[wrap](vector.md.md#('geonodes.core.vector.md',).wrap)(self, max: Vector = None, min: Vector = None)
```

```python
[Vector](vector.md.md).[snap](vector.md.md#('geonodes.core.vector.md',).snap)(self, increment: Vector = None)
```

```python
[Vector](vector.md.md).[sin](vector.md.md#('geonodes.core.vector.md',).sin)(self)
```

```python
[Vector](vector.md.md).[cos](vector.md.md#('geonodes.core.vector.md',).cos)(self)
```

```python
[Vector](vector.md.md).[tan](vector.md.md#('geonodes.core.vector.md',).tan)(self)
```

### class gnmath

```python
[gnmath](gnmath.md.md).[vadd](gnmath.md.md#('geonodes.core.gnmath.md',).vadd)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vsubtract](gnmath.md.md#('geonodes.core.gnmath.md',).vsubtract)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vmultiply](gnmath.md.md#('geonodes.core.gnmath.md',).vmultiply)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vdivide](gnmath.md.md#('geonodes.core.gnmath.md',).vdivide)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vmultiply_add](gnmath.md.md#('geonodes.core.gnmath.md',).vmultiply_add)(vector: Vector = None, multiplier: Vector = None, addend: Vector = None)
```

```python
[gnmath](gnmath.md.md).[cross](gnmath.md.md#('geonodes.core.gnmath.md',).cross)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[project](gnmath.md.md#('geonodes.core.gnmath.md',).project)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[reflect](gnmath.md.md#('geonodes.core.gnmath.md',).reflect)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[refract](gnmath.md.md#('geonodes.core.gnmath.md',).refract)(vector: Vector = None, vector_1: Vector = None, ior: Float = None)
```

```python
[gnmath](gnmath.md.md).[faceforward](gnmath.md.md#('geonodes.core.gnmath.md',).faceforward)(vector: Vector = None, incident: Vector = None, reference: Vector = None)
```

```python
[gnmath](gnmath.md.md).[dot](gnmath.md.md#('geonodes.core.gnmath.md',).dot)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[distance](gnmath.md.md#('geonodes.core.gnmath.md',).distance)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[length](gnmath.md.md#('geonodes.core.gnmath.md',).length)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[scale](gnmath.md.md#('geonodes.core.gnmath.md',).scale)(vector: Vector = None, scale: Float = None)
```

```python
[gnmath](gnmath.md.md).[normalize](gnmath.md.md#('geonodes.core.gnmath.md',).normalize)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vabs](gnmath.md.md#('geonodes.core.gnmath.md',).vabs)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vpower](gnmath.md.md#('geonodes.core.gnmath.md',).vpower)(base: Vector = None, exponent: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vsign](gnmath.md.md#('geonodes.core.gnmath.md',).vsign)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vmin](gnmath.md.md#('geonodes.core.gnmath.md',).vmin)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vmax](gnmath.md.md#('geonodes.core.gnmath.md',).vmax)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vround](gnmath.md.md#('geonodes.core.gnmath.md',).vround)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vfloor](gnmath.md.md#('geonodes.core.gnmath.md',).vfloor)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vceil](gnmath.md.md#('geonodes.core.gnmath.md',).vceil)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vfraction](gnmath.md.md#('geonodes.core.gnmath.md',).vfraction)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vmodulo](gnmath.md.md#('geonodes.core.gnmath.md',).vmodulo)(vector: Vector = None, vector_1: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vwrap](gnmath.md.md#('geonodes.core.gnmath.md',).vwrap)(vector: Vector = None, max: Vector = None, min: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vsnap](gnmath.md.md#('geonodes.core.gnmath.md',).vsnap)(vector: Vector = None, increment: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vsin](gnmath.md.md#('geonodes.core.gnmath.md',).vsin)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vcos](gnmath.md.md#('geonodes.core.gnmath.md',).vcos)(vector: Vector = None)
```

```python
[gnmath](gnmath.md.md).[vtan](gnmath.md.md#('geonodes.core.gnmath.md',).vtan)(vector: Vector = None)
```

## Vector Rotate

> `bl_idname` : ShaderNodeVectorRotate

### nd

[nd](nd.md).[vector_rotate](nd.md#geonodes.core.generated.static_nd.ND.vector_rotate)(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')

### snd

[snd](snd.md).[vector_rotate](snd.md#geonodes.core.generated.static_snd.SND.vector_rotate)(cls,
                    vector: Vector = None,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    rotation: Vector = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')

### class Vector

```python
[Vector](vector.md.md).[rotate](vector.md.md#('geonodes.core.vector.md',).rotate)(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False,
                    rotation_type: Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE')
```

```python
[Vector](vector.md.md).[rotate_axis_angle](vector.md.md#('geonodes.core.vector.md',).rotate_axis_angle)(self,
                    center: Vector = None,
                    axis: Vector = None,
                    angle: Float = None,
                    invert = False)
```

```python
[Vector](vector.md.md).[rotate_x_axis](vector.md.md#('geonodes.core.vector.md',).rotate_x_axis)(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
[Vector](vector.md.md).[rotate_y_axis](vector.md.md#('geonodes.core.vector.md',).rotate_y_axis)(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
[Vector](vector.md.md).[rotate_z_axis](vector.md.md#('geonodes.core.vector.md',).rotate_z_axis)(self, center: Vector = None, angle: Float = None, invert = False)
```

```python
[Vector](vector.md.md).[rotate_euler_xyz](vector.md.md#('geonodes.core.vector.md',).rotate_euler_xyz)(self, center: Vector = None, rotation: Vector = None, invert = False)
```

## Vector Transform

> `bl_idname` : ShaderNodeVectorTransform

### snd

[snd](snd.md).[vector_transform](snd.md#geonodes.core.generated.static_snd.SND.vector_transform)(cls,
                    vector: Vector = None,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR')

### class Vector

```python
[Vector](vector.md.md).[vector_transform](vector.md.md#('geonodes.core.vector.md',).vector_transform)(self,
                    convert_from: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD',
                    convert_to: Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT',
                    vector_type: Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR')
```

## Vertex Neighbors

> `bl_idname` : GeometryNodeInputMeshVertexNeighbors

### nd

[nd](nd.md).[vertex_neighbors](nd.md#geonodes.core.generated.static_nd.ND.vertex_neighbors)(cls)

### class Mesh

```python
prop = [Mesh](mesh.md.md).[vertex_neighbors](mesh.md.md#('geonodes.core.mesh.md',).vertex_neighbors)
```

### class Vertex

```python
prop = [Vertex](vertex.md.md).[neighbors](vertex.md.md#('geonodes.core.vertex.md',).neighbors)
```

```python
prop = [Vertex](vertex.md.md).[neighbors_vertex_count](vertex.md.md#('geonodes.core.vertex.md',).neighbors_vertex_count)
```

```python
prop = [Vertex](vertex.md.md).[neighbors_face_count](vertex.md.md#('geonodes.core.vertex.md',).neighbors_face_count)
```

## Vertex of Corner

> `bl_idname` : GeometryNodeVertexOfCorner

### nd

[nd](nd.md).[vertex_of_corner](nd.md#geonodes.core.generated.static_nd.ND.vertex_of_corner)(cls, corner_index: Integer = None)

### class Mesh

```python
[Mesh](mesh.md.md).[vertex_of_corner](mesh.md.md#('geonodes.core.mesh.md',).vertex_of_corner)(cls, corner_index: Integer = None)
```

### class Corner

```python
[Corner](corner.md.md).[vertex_index](corner.md.md#('geonodes.core.corner.md',).vertex_index)(cls, corner_index: Integer = None)
```

## Viewer

> `bl_idname` : GeometryNodeViewer

### nd

[nd](nd.md).[viewer](nd.md#geonodes.core.generated.static_nd.ND.viewer)(cls,
                    named_sockets: dict = {},
                    domain: Literal['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'AUTO',
                    ui_shortcut = 0,
                    **sockets)

### class Geometry

```python
[Geometry](geometry.md.md).[viewer](geometry.md.md#('geonodes.core.geometry.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Point

```python
[Point](point.md.md).[viewer](point.md.md#('geonodes.core.point.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Edge

```python
[Edge](edge.md.md).[viewer](edge.md.md#('geonodes.core.edge.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Face

```python
[Face](face.md.md).[viewer](face.md.md#('geonodes.core.face.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Corner

```python
[Corner](corner.md.md).[viewer](corner.md.md#('geonodes.core.corner.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Spline

```python
[Spline](spline.md.md).[viewer](spline.md.md#('geonodes.core.spline.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Instance

```python
[Instance](instance.md.md).[viewer](instance.md.md#('geonodes.core.instance.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

### class Layer

```python
[Layer](layer.md.md).[viewer](layer.md.md#('geonodes.core.layer.md',).viewer)(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets)
```

## Viewport Transform

> `bl_idname` : GeometryNodeViewportTransform

### nd

[nd](nd.md).[viewport_transform](nd.md#geonodes.core.generated.static_nd.ND.viewport_transform)(cls)

## Volume Absorption

> `bl_idname` : ShaderNodeVolumeAbsorption

### snd

[snd](snd.md).[volume_absorption](snd.md#geonodes.core.generated.static_snd.SND.volume_absorption)(cls, color: Color = None, density: Float = None, weight: Float = None)

### class VolumeShader

```python
[VolumeShader](volume_shader.md.md).[Absorption](volume_shader.md.md#('geonodes.core.volume_shader.md',).Absorption)(cls, color: Color = None, density: Float = None)
```

## Volume Coefficients

> `bl_idname` : ShaderNodeVolumeCoefficients

### snd

[snd](snd.md).[volume_coefficients](snd.md#geonodes.core.generated.static_snd.SND.volume_coefficients)(cls,
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

[nd](nd.md).[volume_cube](nd.md#geonodes.core.generated.static_nd.ND.volume_cube)(cls,
                    density: Float = None,
                    background: Float = None,
                    min: Vector = None,
                    max: Vector = None,
                    resolution_x: Integer = None,
                    resolution_y: Integer = None,
                    resolution_z: Integer = None)

### class Volume

```python
[Volume](volume.md.md).[Cube](volume.md.md#('geonodes.core.volume.md',).Cube)(cls,
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

[snd](snd.md).[volume_info](snd.md#geonodes.core.generated.static_snd.SND.volume_info)(cls)

### class VolumeShader

```python
prop = [VolumeShader](volume_shader.md.md).[info](volume_shader.md.md#('geonodes.core.volume_shader.md',).info)
```

## Volume Scatter

> `bl_idname` : ShaderNodeVolumeScatter

### snd

[snd](snd.md).[volume_scatter](snd.md#geonodes.core.generated.static_snd.SND.volume_scatter)(cls,
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
[VolumeShader](volume_shader.md.md).[Scatter](volume_shader.md.md#('geonodes.core.volume_shader.md',).Scatter)(cls,
                    color: Color = None,
                    density: Float = None,
                    anisotropy: Float = None,
                    phase: Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN')
```

## Volume to Mesh

> `bl_idname` : GeometryNodeVolumeToMesh

### nd

[nd](nd.md).[volume_to_mesh](nd.md#geonodes.core.generated.static_nd.ND.volume_to_mesh)(cls,
                    volume: Volume = None,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None)

### class Volume

```python
[Volume](volume.md.md).[to_mesh](volume.md.md#('geonodes.core.volume.md',).to_mesh)(self,
                    resolution_mode: Literal['Grid', 'Amount', 'Size'] = None,
                    voxel_size: Float = None,
                    voxel_amount: Float = None,
                    threshold: Float = None,
                    adaptivity: Float = None)
```

## Voronoi Texture

> `bl_idname` : ShaderNodeTexVoronoi

### nd

[nd](nd.md).[voronoi_texture](nd.md#geonodes.core.generated.static_nd.ND.voronoi_texture)(cls,
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

[snd](snd.md).[voronoi_texture](snd.md#geonodes.core.generated.static_snd.SND.voronoi_texture)(cls,
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
[Float](float.md.md).[Voronoi](float.md.md#('geonodes.core.float.md',).Voronoi)(cls,
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
[Texture](texture.md.md).[Voronoi](texture.md.md#('geonodes.core.texture.md',).Voronoi)(cls,
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

[nd](nd.md).[voxel_index](nd.md#geonodes.core.generated.static_nd.ND.voxel_index)(cls)

### class Float

```python
[Float](float.md.md).[voxel_index](float.md.md#('geonodes.core.float.md',).voxel_index)(cls)
```

### class Integer

```python
[Integer](integer.md.md).[voxel_index](integer.md.md#('geonodes.core.integer.md',).voxel_index)(cls)
```

### class Boolean

```python
[Boolean](boolean.md.md).[voxel_index](boolean.md.md#('geonodes.core.boolean.md',).voxel_index)(cls)
```

### class Vector

```python
[Vector](vector.md.md).[voxel_index](vector.md.md#('geonodes.core.vector.md',).voxel_index)(cls)
```

## Voxelize Grid

> `bl_idname` : GeometryNodeGridVoxelize

### nd

[nd](nd.md).[voxelize_grid](nd.md#geonodes.core.generated.static_nd.ND.voxelize_grid)(cls,
                    grid: Float = None,
                    data_type: Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR'] = 'FLOAT')

### class Float

```python
[Float](float.md.md).[voxelize_grid](float.md.md#('geonodes.core.float.md',).voxelize_grid)(self)
```

### class Integer

```python
[Integer](integer.md.md).[voxelize_grid](integer.md.md#('geonodes.core.integer.md',).voxelize_grid)(self)
```

### class Boolean

```python
[Boolean](boolean.md.md).[voxelize_grid](boolean.md.md#('geonodes.core.boolean.md',).voxelize_grid)(self)
```

### class Vector

```python
[Vector](vector.md.md).[voxelize_grid](vector.md.md#('geonodes.core.vector.md',).voxelize_grid)(self)
```

## Warning

> `bl_idname` : GeometryNodeWarning

### nd

[nd](nd.md).[warning](nd.md#geonodes.core.generated.static_nd.ND.warning)(cls,
                    show: Boolean = None,
                    message: String = None,
                    warning_type: Literal['ERROR', 'WARNING', 'INFO'] = 'ERROR')

### class Boolean

```python
[Boolean](boolean.md.md).[error](boolean.md.md#('geonodes.core.boolean.md',).error)(self, message: String = None)
```

```python
[Boolean](boolean.md.md).[warning](boolean.md.md#('geonodes.core.boolean.md',).warning)(self, message: String = None)
```

```python
[Boolean](boolean.md.md).[info](boolean.md.md#('geonodes.core.boolean.md',).info)(self, message: String = None)
```

## Wave Texture

> `bl_idname` : ShaderNodeTexWave

### nd

[nd](nd.md).[wave_texture](nd.md#geonodes.core.generated.static_nd.ND.wave_texture)(cls,
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

[snd](snd.md).[wave_texture](snd.md#geonodes.core.generated.static_snd.SND.wave_texture)(cls,
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
[Color](color.md.md).[Wave](color.md.md#('geonodes.core.color.md',).Wave)(cls,
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
[Texture](texture.md.md).[Wave](texture.md.md#('geonodes.core.texture.md',).Wave)(cls,
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

[snd](snd.md).[wavelength](snd.md#geonodes.core.generated.static_snd.SND.wavelength)(cls, wavelength: Float = None)

### class Float

```python
[Float](float.md.md).[wavelength](float.md.md#('geonodes.core.float.md',).wavelength)(self)
```

## White Noise Texture

> `bl_idname` : ShaderNodeTexWhiteNoise

### nd

[nd](nd.md).[white_noise_texture](nd.md#geonodes.core.generated.static_nd.ND.white_noise_texture)(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### snd

[snd](snd.md).[white_noise_texture](snd.md#geonodes.core.generated.static_snd.SND.white_noise_texture)(cls,
                    vector: Vector = None,
                    w: Float = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')

### class Float

```python
[Float](float.md.md).[WhiteNoise](float.md.md#('geonodes.core.float.md',).WhiteNoise)(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

### class Texture

```python
[Texture](texture.md.md).[WhiteNoise](texture.md.md#('geonodes.core.texture.md',).WhiteNoise)(cls,
                    vector: Vector = None,
                    noise_dimensions: Literal['1D', '2D', '3D', '4D'] = '3D')
```

## Wireframe

> `bl_idname` : ShaderNodeWireframe

### snd

[snd](snd.md).[wireframe](snd.md#geonodes.core.generated.static_snd.SND.wireframe)(cls, size: Float = None, use_pixel_size = False)

### class Float

```python
[Float](float.md.md).[wireframe](float.md.md#('geonodes.core.float.md',).wireframe)(self, use_pixel_size = False)
```

## World Output

> `bl_idname` : ShaderNodeOutputWorld

### snd

[snd](snd.md).[world_output](snd.md#geonodes.core.generated.static_snd.SND.world_output)(cls,
                    surface: Shader = None,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')

### class Shader

```python
[Shader](shader.md.md).[world_output](shader.md.md#('geonodes.core.shader.md',).world_output)(self,
                    volume: VolumeShader = None,
                    is_active_output = True,
                    target: Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL')
```

