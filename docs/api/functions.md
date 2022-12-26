# Global functions

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

[abs](#abs) | [absolute](#absolute) | [align_euler_to_vector](#align_euler_to_vector) | [arccos](#arccos) | [arccosine](#arccosine) | [arcsin](#arcsin) | [arcsine](#arcsine) | [arctan](#arctan) | [arctan2](#arctan2) | [arctangent](#arctangent) | [b_and](#b_and) | [b_not](#b_not) | [b_or](#b_or) | [clamp](#clamp) | [clamp_min_max](#clamp_min_max) | [clamp_range](#clamp_range) | [color_add](#color_add) | [color_burn](#color_burn) | [color_color](#color_color) | [color_darken](#color_darken) | [color_difference](#color_difference) | [color_divide](#color_divide) | [color_dodge](#color_dodge) | [color_hue](#color_hue) | [color_lighten](#color_lighten) | [color_linear_light](#color_linear_light) | [color_mix](#color_mix) | [color_multiply](#color_multiply) | [color_overlay](#color_overlay) | [color_ramp](#color_ramp) | [color_saturation](#color_saturation) | [color_screen](#color_screen) | [color_soft_light](#color_soft_light) | [color_subtract](#color_subtract) | [color_value](#color_value) | [combine_hsl](#combine_hsl) | [combine_hsv](#combine_hsv) | [combine_rgb](#combine_rgb) | [compare](#compare) | [cos](#cos) | [cosh](#cosh) | [cosine](#cosine) | [exp](#exp) | [exponent](#exponent) | [float_mix](#float_mix) | [fraction](#fraction) | [geometry_to_instance](#geometry_to_instance) | [imply](#imply) | [inverse_sqrt](#inverse_sqrt) | [join_geometry](#join_geometry) | [join_strings](#join_strings) | [log](#log) | [logarithm](#logarithm) | [math](#math) | [math_ceil](#math_ceil) | [math_compare](#math_compare) | [math_floor](#math_floor) | [math_greater_than](#math_greater_than) | [math_less_than](#math_less_than) | [math_round](#math_round) | [math_trun](#math_trun) | [math_truncate](#math_truncate) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [modulo](#modulo) | [mul_add](#mul_add) | [multiply_add](#multiply_add) | [nand](#nand) | [nimply](#nimply) | [nor](#nor) | [ping_pong](#ping_pong) | [power](#power) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector) | [replace_string](#replace_string) | [rgb_curves](#rgb_curves) | [rotate_axis_angle](#rotate_axis_angle) | [rotate_euler](#rotate_euler) | [separate_hsl](#separate_hsl) | [separate_hsv](#separate_hsv) | [separate_rgb](#separate_rgb) | [sign](#sign) | [sin](#sin) | [sine](#sine) | [sinh](#sinh) | [slice_string](#slice_string) | [smooth_maximum](#smooth_maximum) | [smooth_minimum](#smooth_minimum) | [snap](#snap) | [sqrt](#sqrt) | [string_length](#string_length) | [string_to_curves](#string_to_curves) | [switch](#switch) | [switch_boolean](#switch_boolean) | [switch_collection](#switch_collection) | [switch_color](#switch_color) | [switch_float](#switch_float) | [switch_geometry](#switch_geometry) | [switch_image](#switch_image) | [switch_integer](#switch_integer) | [switch_material](#switch_material) | [switch_object](#switch_object) | [switch_string](#switch_string) | [switch_texture](#switch_texture) | [switch_vector](#switch_vector) | [tan](#tan) | [tangent](#tangent) | [tanh](#tanh) | [to_degrees](#to_degrees) | [to_radians](#to_radians) | [value_to_string](#value_to_string) | [vector_mix](#vector_mix) | [wrap](#wrap) | [xnor](#xnor) | [xor](#xor)

### abs

```python
def abs(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### align_euler_to_vector

```python
def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```



> Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

#### Args:
- rotation: Vector
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

#### Returns:
- socket `rotation`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccos

```python
def arccos(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccosine

```python
def arccosine(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsin

```python
def arcsin(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsine

```python
def arcsine(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan

```python
def arctan(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan2

```python
def arctan2(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctangent

```python
def arctangent(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_and

```python
def b_and(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_not

```python
def b_not(boolean0=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### b_or

```python
def b_or(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp

```python
def clamp(value=None, min=None, max=None, clamp_type='MINMAX')
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- value: Float
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_min_max

```python
def clamp_min_max(value=None, min=None, max=None)
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- value: Float
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_range

```python
def clamp_range(value=None, min=None, max=None)
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- value: Float
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_add

```python
def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_burn

```python
def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_color

```python
def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_darken

```python
def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_difference

```python
def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_divide

```python
def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_dodge

```python
def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_hue

```python
def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_lighten

```python
def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_linear_light

```python
def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_mix

```python
def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_multiply

```python
def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_overlay

```python
def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_ramp

```python
def color_ramp(fac=None)
```



> Node: [ColorRamp](ShaderNodeValToRGB.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

#### Args:
- fac: Float

#### Returns:
- node with sockets ['color', 'alpha']






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_saturation

```python
def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_screen

```python
def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_soft_light

```python
def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_subtract

```python
def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### color_value

```python
def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- clamp_result (bool): False

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### combine_hsl

```python
def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- lightness: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### combine_hsv

```python
def combine_hsv(hue=None, saturation=None, value=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- hue: Float
- saturation: Float
- value: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### combine_rgb

```python
def combine_rgb(red=None, green=None, blue=None, alpha=None)
```



> Node: [Combine Color](FunctionNodeCombineColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)

#### Args:
- red: Float
- green: Float
- blue: Float
- alpha: Float

#### Returns:
- socket `color`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- a: ['Float', 'Integer', 'Vector', 'Color', 'String']
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- data_type (str): 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cos

```python
def cos(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosh

```python
def cosh(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exp

```python
def exp(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exponent

```python
def exponent(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### float_mix

```python
def float_mix(factor=None, a=None, b=None, clamp_factor=True)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### geometry_to_instance

```python
def geometry_to_instance(*geometry)
```



> Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### imply

```python
def imply(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### inverse_sqrt

```python
def inverse_sqrt(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join_geometry

```python
def join_geometry(*geometry)
```



> Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `geometry`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join_strings

```python
def join_strings(*strings, delimiter=None)
```



> Node: [Join Strings](GeometryNodeStringJoin.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)

#### Args:
- strings: <m>String
- delimiter: String

#### Returns:
- socket `string`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### log

```python
def log(value=None, base=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### logarithm

```python
def logarithm(value=None, base=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math

```python
def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- value2: Float
- operation (str): 'ADD' in [ADD, SUBTRACT, MULTIPLY, DIVIDE,... , TANH, RADIANS, DEGREES]
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_ceil

```python
def math_ceil(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_compare

```python
def math_compare(value0=None, value1=None, epsilon=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- epsilon: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_floor

```python
def math_floor(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_greater_than

```python
def math_greater_than(value=None, threshold=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_less_than

```python
def math_less_than(value=None, threshold=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_round

```python
def math_round(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_trun

```python
def math_trun(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_truncate

```python
def math_truncate(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### modulo

```python
def modulo(value0=None, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(value=None, multiplier=None, addend=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(value=None, multiplier=None, addend=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nand

```python
def nand(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nimply

```python
def nimply(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### nor

```python
def nor(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ping_pong

```python
def ping_pong(value=None, scale=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- scale: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### power

```python
def power(base=None, exponent=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
def random_boolean(probability=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
def random_float(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
def random_integer(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
def random_vector(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace_string

```python
def replace_string(string=None, find=None, replace=None)
```



> Node: [Replace String](FunctionNodeReplaceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)

#### Args:
- string: String
- find: String
- replace: String

#### Returns:
- socket `string`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rgb_curves

```python
def rgb_curves(fac=None, color=None)
```



> Node: [RGB Curves](ShaderNodeRGBCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)

#### Args:
- fac: Float
- color: Color

#### Returns:
- node with sockets ['color']






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_axis_angle

```python
def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT')
```



> Node: [Rotate Euler](FunctionNodeRotateEuler.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)

#### Args:
- rotation: Vector
- axis: Vector
- angle: Float
- space (str): 'OBJECT' in [OBJECT, LOCAL]

#### Returns:
- socket `rotation`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_euler

```python
def rotate_euler(rotation=None, rotate_by=None, space='OBJECT')
```



> Node: [Rotate Euler](FunctionNodeRotateEuler.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)

#### Args:
- rotation: Vector
- rotate_by: Vector
- space (str): 'OBJECT' in [OBJECT, LOCAL]

#### Returns:
- socket `rotation`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_hsl

```python
def separate_hsl(color=None)
```



> Node: [Separate Color](FunctionNodeSeparateColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Args:
- color: Color

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_hsv

```python
def separate_hsv(color=None)
```



> Node: [Separate Color](FunctionNodeSeparateColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Args:
- color: Color

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_rgb

```python
def separate_rgb(color=None)
```



> Node: [Separate Color](FunctionNodeSeparateColor.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)

#### Args:
- color: Color

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.webp)

#### Returns:
- tuple ('`red`', '`green`', '`blue`', '`alpha`')






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sign

```python
def sign(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sinh

```python
def sinh(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### slice_string

```python
def slice_string(string=None, position=None, length=None)
```



> Node: [Slice String](FunctionNodeSliceString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)

#### Args:
- string: String
- position: Integer
- length: Integer

#### Returns:
- socket `string`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_maximum

```python
def smooth_maximum(value0=None, value1=None, distance=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_minimum

```python
def smooth_minimum(value0=None, value1=None, distance=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value0: Float
- value1: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(value=None, increment=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- increment: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sqrt

```python
def sqrt(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### string_length

```python
def string_length(string=None)
```



> Node: [String Length](FunctionNodeStringLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)

#### Args:
- string: String

#### Returns:
- socket `length`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### string_to_curves

```python
def string_to_curves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT')
```



> Node: [String to Curves](GeometryNodeStringToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)

#### Args:
- string: String
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






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(switch=None, false=None, true=None, input_type='GEOMETRY')
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- input_type (str): 'GEOMETRY' in [FLOAT, INT, BOOLEAN, VECTOR, STRING,... , COLLECTION, TEXTURE, MATERIAL]

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_boolean

```python
def switch_boolean(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_collection

```python
def switch_collection(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_color

```python
def switch_color(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_float

```python
def switch_float(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_geometry

```python
def switch_geometry(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_image

```python
def switch_image(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_integer

```python
def switch_integer(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_material

```python
def switch_material(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_object

```python
def switch_object(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_string

```python
def switch_string(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_texture

```python
def switch_texture(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch_vector

```python
def switch_vector(switch=None, false=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: ['Boolean', 'Boolean']
- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

#### Returns:
- socket `output`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tan

```python
def tan(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tanh

```python
def tanh(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_degrees

```python
def to_degrees(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_radians

```python
def to_radians(value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_to_string

```python
def value_to_string(value=None, decimals=None)
```



> Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

#### Args:
- value: Float
- decimals: Integer

#### Returns:
- socket `string`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### vector_mix

```python
def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM')
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- a: ['Float', 'Vector', 'Color']
- b: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

#### Returns:
- socket `result`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(value=None, max=None, min=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- max: Float
- min: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xnor

```python
def xnor(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### xor

```python
def xor(boolean0=None, boolean1=None)
```



> Node: [Boolean Math](FunctionNodeBooleanMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)

#### Args:
- boolean0: Boolean
- boolean1: Boolean

#### Returns:
- socket `boolean`






<sub>Go to [top](#global-functions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

