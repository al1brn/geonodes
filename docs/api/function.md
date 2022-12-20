# class function




## Methods

- [abs](#abs)
- [absolute](#absolute)
- [add](#add)
- [align_euler_to_vector](#align_euler_to_vector)
- [arccos](#arccos)
- [arccosine](#arccosine)
- [arcsin](#arcsin)
- [arcsine](#arcsine)
- [arctan](#arctan)
- [arctan2](#arctan2)
- [arctangent](#arctangent)
- [b_and](#b_and)
- [b_not](#b_not)
- [b_or](#b_or)
- [clamp](#clamp)
- [clamp_min_max](#clamp_min_max)
- [clamp_range](#clamp_range)
- [color_add](#color_add)
- [color_burn](#color_burn)
- [color_color](#color_color)
- [color_darken](#color_darken)
- [color_difference](#color_difference)
- [color_divide](#color_divide)
- [color_dodge](#color_dodge)
- [color_hue](#color_hue)
- [color_lighten](#color_lighten)
- [color_linear_light](#color_linear_light)
- [color_mix](#color_mix)
- [color_multiply](#color_multiply)
- [color_overlay](#color_overlay)
- [color_ramp](#color_ramp)
- [color_saturation](#color_saturation)
- [color_screen](#color_screen)
- [color_soft_light](#color_soft_light)
- [color_subtract](#color_subtract)
- [color_value](#color_value)
- [combine_hsl](#combine_hsl)
- [combine_hsv](#combine_hsv)
- [combine_rgb](#combine_rgb)
- [compare](#compare)
- [cos](#cos)
- [cosh](#cosh)
- [cosine](#cosine)
- [div](#div)
- [divide](#divide)
- [exp](#exp)
- [exponent](#exponent)
- [float_mix](#float_mix)
- [fraction](#fraction)
- [geometry_to_instance](#geometry_to_instance)
- [imply](#imply)
- [inverse_sqrt](#inverse_sqrt)
- [join_geometry](#join_geometry)
- [join_strings](#join_strings)
- [log](#log)
- [logarithm](#logarithm)
- [math](#math)
- [math_ceil](#math_ceil)
- [math_compare](#math_compare)
- [math_floor](#math_floor)
- [math_greater_than](#math_greater_than)
- [math_less_than](#math_less_than)
- [math_round](#math_round)
- [math_trun](#math_trun)
- [math_truncate](#math_truncate)
- [max](#max)
- [maximum](#maximum)
- [min](#min)
- [minimum](#minimum)
- [modulo](#modulo)
- [mul](#mul)
- [mul_add](#mul_add)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [nand](#nand)
- [nimply](#nimply)
- [nor](#nor)
- [ping_pong](#ping_pong)
- [power](#power)
- [random_boolean](#random_boolean)
- [random_float](#random_float)
- [random_integer](#random_integer)
- [random_vector](#random_vector)
- [replace_string](#replace_string)
- [rgb_curves](#rgb_curves)
- [rotate_axis_angle](#rotate_axis_angle)
- [rotate_euler](#rotate_euler)
- [separate_hsl](#separate_hsl)
- [separate_hsv](#separate_hsv)
- [separate_rgb](#separate_rgb)
- [sign](#sign)
- [sin](#sin)
- [sine](#sine)
- [sinh](#sinh)
- [slice_string](#slice_string)
- [smooth_maximum](#smooth_maximum)
- [smooth_minimum](#smooth_minimum)
- [snap](#snap)
- [sqrt](#sqrt)
- [string_length](#string_length)
- [string_to_curves](#string_to_curves)
- [sub](#sub)
- [subtract](#subtract)
- [switch](#switch)
- [switch_boolean](#switch_boolean)
- [switch_collection](#switch_collection)
- [switch_color](#switch_color)
- [switch_float](#switch_float)
- [switch_geometry](#switch_geometry)
- [switch_image](#switch_image)
- [switch_integer](#switch_integer)
- [switch_material](#switch_material)
- [switch_object](#switch_object)
- [switch_string](#switch_string)
- [switch_texture](#switch_texture)
- [switch_vector](#switch_vector)
- [tan](#tan)
- [tangent](#tangent)
- [tanh](#tanh)
- [to_degrees](#to_degrees)
- [to_radians](#to_radians)
- [value_to_string](#value_to_string)
- [vector_mix](#vector_mix)
- [wrap](#wrap)
- [xnor](#xnor)
- [xor](#xor)

## abs

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def abs(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## absolute

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def absolute(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## add

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def add(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## align_euler_to_vector

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- rotation: Vector
<sub>Go to [top](#class-function)</sub>- factor: Float
<sub>Go to [top](#class-function)</sub>- vector: Vector
<sub>Go to [top](#class-function)</sub>- axis (str): 'X' in [X, Y, Z]
<sub>Go to [top](#class-function)</sub>- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'rotation'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arccos

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arccos(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arccosine

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arccosine(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arcsin

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arcsin(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arcsine

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arcsine(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arctan

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arctan(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arctan2

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arctan2(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## arctangent

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def arctangent(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## b_and

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def b_and(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## b_not

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def b_not(boolean0=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## b_or

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def b_or(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## clamp

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def clamp(value=None, min=None, max=None, clamp_type='MINMAX'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- min: Float
<sub>Go to [top](#class-function)</sub>- max: Float
<sub>Go to [top](#class-function)</sub>- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## clamp_min_max

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def clamp_min_max(value=None, min=None, max=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- min: Float
<sub>Go to [top](#class-function)</sub>- max: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## clamp_range

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def clamp_range(value=None, min=None, max=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- min: Float
<sub>Go to [top](#class-function)</sub>- max: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_add

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_add(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_burn

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_burn(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_color

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_color(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_darken

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_darken(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_difference

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_difference(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_divide

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_divide(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_dodge

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_dodge(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_hue

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_hue(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_lighten

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_lighten(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_linear_light

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_linear_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_mix

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_mix(factor=None, a=None, b=None, blend_type='MIX', clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- blend_type (str): 'MIX' in [MIX, DARKEN, MULTIPLY, BURN, LIGHTEN,... , SATURATION, COLOR, VALUE]
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_multiply

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_multiply(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_overlay

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_overlay(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_ramp

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_ramp(fac=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- fac: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- node with sockets ['color', 'alpha']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_saturation

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_saturation(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_screen

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_screen(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_soft_light

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_soft_light(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_subtract

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_subtract(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## color_value

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def color_value(factor=None, a=None, b=None, clamp_factor=True, clamp_result=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- clamp_result (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## combine_hsl

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def combine_hsl(hue=None, saturation=None, lightness=None, alpha=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- hue: Float
<sub>Go to [top](#class-function)</sub>- saturation: Float
<sub>Go to [top](#class-function)</sub>- lightness: Float
<sub>Go to [top](#class-function)</sub>- alpha: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'color'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## combine_hsv

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def combine_hsv(hue=None, saturation=None, value=None, alpha=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- hue: Float
<sub>Go to [top](#class-function)</sub>- saturation: Float
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- alpha: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'color'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## combine_rgb

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def combine_rgb(red=None, green=None, blue=None, alpha=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/combine_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- red: Float
<sub>Go to [top](#class-function)</sub>- green: Float
<sub>Go to [top](#class-function)</sub>- blue: Float
<sub>Go to [top](#class-function)</sub>- alpha: Float
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'color'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## compare

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def compare(a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-function)</sub>- c: Float
<sub>Go to [top](#class-function)</sub>- angle: Float
<sub>Go to [top](#class-function)</sub>- epsilon: Float
<sub>Go to [top](#class-function)</sub>- data_type (str): 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
<sub>Go to [top](#class-function)</sub>- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
<sub>Go to [top](#class-function)</sub>- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## cos

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def cos(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## cosh

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def cosh(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## cosine

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def cosine(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## div

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def div(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## divide

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def divide(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## exp

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def exp(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## exponent

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def exponent(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## float_mix

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def float_mix(factor=None, a=None, b=None, clamp_factor=True):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## fraction

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def fraction(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## geometry_to_instance

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def geometry_to_instance(*geometry):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- geometry: <m>Geometry
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'instances'<sub>Go to [top](#class-function)</sub> of class Instances
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## imply

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def imply(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## inverse_sqrt

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def inverse_sqrt(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## join_geometry

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def join_geometry(*geometry):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- geometry: <m>Geometry
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'geometry'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## join_strings

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def join_strings(*strings, delimiter=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- strings: <m>String
<sub>Go to [top](#class-function)</sub>- delimiter: String
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'string'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## log

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def log(value=None, base=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- base: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## logarithm

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def logarithm(value=None, base=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- base: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math(value0=None, value1=None, value2=None, operation='ADD', clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- value2: Float
<sub>Go to [top](#class-function)</sub>- operation (str): 'ADD' in [ADD, SUBTRACT, MULTIPLY, DIVIDE,... , TANH, RADIANS, DEGREES]
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_ceil

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_ceil(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_compare

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_compare(value0=None, value1=None, epsilon=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- epsilon: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_floor

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_floor(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_greater_than

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_greater_than(value=None, threshold=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- threshold: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_less_than

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_less_than(value=None, threshold=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- threshold: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_round

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_round(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_trun

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_trun(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## math_truncate

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def math_truncate(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## max

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def max(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## maximum

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def maximum(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## min

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def min(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## minimum

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def minimum(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## modulo

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def modulo(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## mul

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def mul(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## mul_add

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def mul_add(value=None, multiplier=None, addend=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- multiplier: Float
<sub>Go to [top](#class-function)</sub>- addend: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## multiply

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def multiply(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## multiply_add

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def multiply_add(value=None, multiplier=None, addend=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- multiplier: Float
<sub>Go to [top](#class-function)</sub>- addend: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## nand

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def nand(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## nimply

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def nimply(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## nor

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def nor(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## ping_pong

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def ping_pong(value=None, scale=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- scale: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## power

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def power(base=None, exponent=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- base: Float
<sub>Go to [top](#class-function)</sub>- exponent: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## random_boolean

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def random_boolean(probability=None, ID=None, seed=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- probability: Float
<sub>Go to [top](#class-function)</sub>- ID: Integer
<sub>Go to [top](#class-function)</sub>- seed: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## random_float

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def random_float(min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- ID: Integer
<sub>Go to [top](#class-function)</sub>- seed: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## random_integer

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def random_integer(min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- ID: Integer
<sub>Go to [top](#class-function)</sub>- seed: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## random_vector

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def random_vector(min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-function)</sub>- ID: Integer
<sub>Go to [top](#class-function)</sub>- seed: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## replace_string

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def replace_string(string=None, find=None, replace=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- string: String
<sub>Go to [top](#class-function)</sub>- find: String
<sub>Go to [top](#class-function)</sub>- replace: String
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'string'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## rgb_curves

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def rgb_curves(fac=None, color=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/rgb_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- fac: Float
<sub>Go to [top](#class-function)</sub>- color: Color
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- node with sockets ['color']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## rotate_axis_angle

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- rotation: Vector
<sub>Go to [top](#class-function)</sub>- axis: Vector
<sub>Go to [top](#class-function)</sub>- angle: Float
<sub>Go to [top](#class-function)</sub>- space (str): 'OBJECT' in [OBJECT, LOCAL]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'rotation'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## rotate_euler

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- rotation: Vector
<sub>Go to [top](#class-function)</sub>- rotate_by: Vector
<sub>Go to [top](#class-function)</sub>- space (str): 'OBJECT' in [OBJECT, LOCAL]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'rotation'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## separate_hsl

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def separate_hsl(color=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- color: Color
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## separate_hsv

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def separate_hsv(color=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- color: Color
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## separate_rgb

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def separate_rgb(color=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/separate_color.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- color: Color
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- tuple ('red', 'green', 'blue', 'alpha')
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sign

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sign(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sin

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sin(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sine

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sine(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sinh

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sinh(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## slice_string

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def slice_string(string=None, position=None, length=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- string: String
<sub>Go to [top](#class-function)</sub>- position: Integer
<sub>Go to [top](#class-function)</sub>- length: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'string'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## smooth_maximum

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def smooth_maximum(value0=None, value1=None, distance=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- distance: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## smooth_minimum

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def smooth_minimum(value0=None, value1=None, distance=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- distance: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## snap

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def snap(value=None, increment=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- increment: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sqrt

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sqrt(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## string_length

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def string_length(string=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- string: String
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'length'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## string_to_curves

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def string_to_curves(string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- string: String
<sub>Go to [top](#class-function)</sub>- size: Float
<sub>Go to [top](#class-function)</sub>- character_spacing: Float
<sub>Go to [top](#class-function)</sub>- word_spacing: Float
<sub>Go to [top](#class-function)</sub>- line_spacing: Float
<sub>Go to [top](#class-function)</sub>- text_box_width: Float
<sub>Go to [top](#class-function)</sub>- text_box_height: Float
<sub>Go to [top](#class-function)</sub>- align_x (str): 'LEFT' in [LEFT, CENTER, RIGHT, JUSTIFY, FLUSH]
<sub>Go to [top](#class-function)</sub>- align_y (str): 'TOP_BASELINE' in [TOP_BASELINE, TOP, MIDDLE, BOTTOM_BASELINE, BOTTOM]
<sub>Go to [top](#class-function)</sub>- overflow (str): 'OVERFLOW' in [OVERFLOW, SCALE_TO_FIT, TRUNCATE]
<sub>Go to [top](#class-function)</sub>- pivot_mode (str): 'BOTTOM_LEFT' in [MIDPOINT, TOP_LEFT, TOP_CENTER,... , BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>- tuple ('curve_instances', 'line', 'pivot_point')
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## sub

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def sub(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## subtract

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def subtract(value0=None, value1=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value0: Float
<sub>Go to [top](#class-function)</sub>- value1: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch(switch=None, false=None, true=None, input_type='GEOMETRY'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- input_type (str): 'GEOMETRY' in [FLOAT, INT, BOOLEAN, VECTOR, STRING,... , COLLECTION, TEXTURE, MATERIAL]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_boolean

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_boolean(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_collection

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_collection(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_color

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_color(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_float

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_float(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_geometry

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_geometry(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_image

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_image(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_integer

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_integer(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_material

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_material(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_object

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_object(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_string

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_string(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_texture

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_texture(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## switch_vector

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def switch_vector(switch=None, false=None, true=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-function)</sub>- false: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'output'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## tan

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def tan(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## tangent

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def tangent(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## tanh

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def tanh(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## to_degrees

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def to_degrees(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## to_radians

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def to_radians(value=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## value_to_string

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def value_to_string(value=None, decimals=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- decimals: Integer
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'string'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## vector_mix

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def vector_mix(factor=None, a=None, b=None, clamp_factor=True, factor_mode='UNIFORM'):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-function)</sub>- a: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- b: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-function)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-function)</sub>- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'result'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## wrap

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def wrap(value=None, max=None, min=None, clamp=False):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- value: Float
<sub>Go to [top](#class-function)</sub>- max: Float
<sub>Go to [top](#class-function)</sub>- min: Float
<sub>Go to [top](#class-function)</sub>- clamp (bool): False
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'value'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## xnor

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def xnor(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>## xor

<sub>Go to [top](#class-function)</sub>```python
<sub>Go to [top](#class-function)</sub>def xor(boolean0=None, boolean1=None):

<sub>Go to [top](#class-function)</sub>```
<sub>Go to [top](#class-function)</sub>Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html) )

<sub>Go to [top](#class-function)</sub>### Args:
<sub>Go to [top](#class-function)</sub>- boolean0: Boolean
<sub>Go to [top](#class-function)</sub>- boolean1: Boolean
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>### Returns:

<sub>Go to [top](#class-function)</sub>  socket 'boolean'<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>
<sub>Go to [top](#class-function)</sub>