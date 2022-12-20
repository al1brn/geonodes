# class Float

## Properties

- [color_ramp](#color_ramp-property)

## Class methods

- [Frame](#Frame-classmethod)
- [Input](#Input-classmethod)
- [Seconds](#Seconds-classmethod)
- [Value](#Value-classmethod)


## Methods

- [abs](#abs)
- [absolute](#absolute)
- [add](#add)
- [arccos](#arccos)
- [arccosine](#arccosine)
- [arcsin](#arcsin)
- [arcsine](#arcsine)
- [arctan](#arctan)
- [arctan2](#arctan2)
- [arctangent](#arctangent)
- [ceiling](#ceiling)
- [clamp](#clamp)
- [clamp_min_max](#clamp_min_max)
- [clamp_range](#clamp_range)
- [compare](#compare)
- [cos](#cos)
- [cosh](#cosh)
- [cosine](#cosine)
- [div](#div)
- [divide](#divide)
- [equal](#equal)
- [exp](#exp)
- [exponent](#exponent)
- [fact](#fact)
- [float_curve](#float_curve)
- [floor](#floor)
- [fraction](#fraction)
- [greater_equal](#greater_equal)
- [greater_than](#greater_than)
- [inverse_sqrt](#inverse_sqrt)
- [less_equal](#less_equal)
- [less_than](#less_than)
- [log](#log)
- [logarithm](#logarithm)
- [map_range](#map_range)
- [map_range_linear](#map_range_linear)
- [map_range_smooth](#map_range_smooth)
- [map_range_smoother](#map_range_smoother)
- [map_range_stepped](#map_range_stepped)
- [math_ceil](#math_ceil)
- [math_compare](#math_compare)
- [math_floor](#math_floor)
- [math_greater_than](#math_greater_than)
- [math_less_than](#math_less_than)
- [math_round](#math_round)
- [math_trunc](#math_trunc)
- [math_truncate](#math_truncate)
- [max](#max)
- [maximum](#maximum)
- [min](#min)
- [minimum](#minimum)
- [mix](#mix)
- [modulo](#modulo)
- [mul](#mul)
- [mul_add](#mul_add)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [not_equal](#not_equal)
- [ping_pong](#ping_pong)
- [pow](#pow)
- [power](#power)
- [round](#round)
- [sign](#sign)
- [sin](#sin)
- [sine](#sine)
- [sinh](#sinh)
- [smooth_maximum](#smooth_maximum)
- [smooth_minimum](#smooth_minimum)
- [snap](#snap)
- [sqrt](#sqrt)
- [sub](#sub)
- [subtract](#subtract)
- [switch](#switch)
- [tan](#tan)
- [tangent](#tangent)
- [tanh](#tanh)
- [to_degrees](#to_degrees)
- [to_integer](#to_integer)
- [to_radians](#to_radians)
- [to_string](#to_string)
- [truncate](#truncate)
- [wrap](#wrap)

## Frame <sub>*classmethod*</sub>

```python
def Frame(cls):

```
Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

### Returns:
- socket `frame`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=0., name="Float", min_value=None, max_value=None, description=""):

```
### Args:
- value: Initial value. Not changed if the group input socket already exists
- name: Input socket name. Avoid homonyms!
- min_value: minimum value
- max_value: maxium value
- description: user help

### Returns:
- Float

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## Seconds <sub>*classmethod*</sub>

```python
def Seconds(cls):

```
Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

### Returns:
- socket `seconds`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## Value <sub>*classmethod*</sub>

```python
def Value(cls):

```
Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html) )

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## abs

```python
def abs(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## absolute

```python
def absolute(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## add

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float or Integer or Vector

### Returns:
- self + value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arccos

```python
def arccos(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arccosine

```python
def arccosine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arcsin

```python
def arcsin(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arcsine

```python
def arcsine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arctan

```python
def arctan(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arctan2

```python
def arctan2(self, value1=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value1: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## arctangent

```python
def arctangent(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## ceiling

```python
def ceiling(self):

```
Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:
- socket `integer`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## clamp

```python
def clamp(self, min=None, max=None, clamp_type='MINMAX'):

```
Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

### Args:
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## clamp_min_max

```python
def clamp_min_max(self, min=None, max=None):

```
Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

### Args:
- min: Float
- max: Float

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## clamp_range

```python
def clamp_range(self, min=None, max=None):

```
Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

### Args:
- min: Float
- max: Float

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## color_ramp <sub>*property*</sub>

```python
def color_ramp(self):

```
Node [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html) )

### Returns:
- node with sockets ['color', 'alpha']

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## cos

```python
def cos(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## cosh

```python
def cosh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## cosine

```python
def cosine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## div

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float

### Returns:
- self / value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## divide

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float

### Returns:
- self / value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## equal

```python
def equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## exp

```python
def exp(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## exponent

```python
def exponent(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## fact

```python
def fact(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## float_curve

```python
def float_curve(self, factor=None):

```
Node [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html) )

### Args:
- factor: Float

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## floor

```python
def floor(self):

```
Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:
- socket `integer`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## fraction

```python
def fraction(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## greater_equal

```python
def greater_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## greater_than

```python
def greater_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## inverse_sqrt

```python
def inverse_sqrt(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## less_equal

```python
def less_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## less_than

```python
def less_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## log

```python
def log(self, base=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- base: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## logarithm

```python
def logarithm(self, base=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- base: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## map_range

```python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

```
Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True
- interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

```
Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

```
Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

```
Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

```
Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_ceil

```python
def math_ceil(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_floor

```python
def math_floor(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- threshold: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_less_than

```python
def math_less_than(self, threshold=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- threshold: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_round

```python
def math_round(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_trunc

```python
def math_trunc(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## math_truncate

```python
def math_truncate(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## max

```python
def max(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## maximum

```python
def maximum(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## min

```python
def min(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## minimum

```python
def minimum(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## mix

```python
def mix(self, factor=None, value=None, clamp_factor=True):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- value: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## modulo

```python
def modulo(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## mul

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float or Integer or Vector

### Returns:
- self * value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## multiply

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float or Integer or Vector

### Returns:
- self * value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## not_equal

```python
def not_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:
- socket `result`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## ping_pong

```python
def ping_pong(self, scale=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- scale: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## pow

```python
def pow(self, exponent=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- exponent: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## power

```python
def power(self, exponent=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- exponent: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## round

```python
def round(self):

```
Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:
- socket `integer`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sign

```python
def sign(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sin

```python
def sin(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sine

```python
def sine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sinh

```python
def sinh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- distance: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## snap

```python
def snap(self, increment=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- increment: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sqrt

```python
def sqrt(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## sub

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float or Integer or Vector

### Returns:
- self - value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## subtract

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float or Integer or Vector

### Returns:
- self - value

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:
- socket `output`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## tan

```python
def tan(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## tangent

```python
def tangent(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## tanh

```python
def tanh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- value: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## to_degrees

```python
def to_degrees(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## to_integer

```python
def to_integer(self, rounding_mode='ROUND'):

```
Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Args:
- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

### Returns:
- socket `integer`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## to_radians

```python
def to_radians(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## to_string

```python
def to_string(self, decimals=None):

```
Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html) )

### Args:
- decimals: Integer

### Returns:
- socket `string`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## truncate

```python
def truncate(self):

```
Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

### Returns:
- socket `integer`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

## wrap

```python
def wrap(self, max=None, min=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

### Args:
- max: Float
- min: Float
- clamp (bool): False

### Returns:
- socket `value`

<sub>Go to [top](#class-Float) [data structure](../structure.md)</sub>

