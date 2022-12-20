# class Float

## Properties

- [color_ramp](#color_ramp-property)

## Class methods

- [Frame](#Frame-classmethod)
- [Seconds](#Seconds-classmethod)
- [Value](#Value-classmethod)


## Methods

- [abs](#abs)
- [absolute](#absolute)
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
- [mul_add](#mul_add)
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

## Frame <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def Frame(cls):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'frame'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## Seconds <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def Seconds(cls):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'seconds'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## Value <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def Value(cls):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## abs

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def abs(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## absolute

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def absolute(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arccos

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arccos(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arccosine

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arccosine(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arcsin

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arcsin(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arcsine

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arcsine(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arctan

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arctan(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arctan2

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arctan2(self, value1=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value1: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## arctangent

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def arctangent(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## ceiling

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def ceiling(self):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'integer'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## clamp

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def clamp(self, min=None, max=None, clamp_type='MINMAX'):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- min: Float
<sub>Go to [top](#class-Float)</sub>

- max: Float
<sub>Go to [top](#class-Float)</sub>

- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## clamp_min_max

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def clamp_min_max(self, min=None, max=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- min: Float
<sub>Go to [top](#class-Float)</sub>

- max: Float
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## clamp_range

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def clamp_range(self, min=None, max=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- min: Float
<sub>Go to [top](#class-Float)</sub>

- max: Float
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## color_ramp <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def color_ramp(self):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html) )

<sub>Go to [top](#class-Float)</sub>

Node implemented as property.

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

- node with sockets ['color', 'alpha']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## compare

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>

- epsilon: Float
<sub>Go to [top](#class-Float)</sub>

- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## cos

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def cos(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## cosh

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def cosh(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## cosine

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def cosine(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## equal

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>

- epsilon: Float
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## exp

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def exp(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## exponent

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def exponent(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## fact

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def fact(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## float_curve

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def float_curve(self, factor=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- factor: Float
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## floor

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def floor(self):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'integer'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## fraction

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def fraction(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## greater_equal

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def greater_equal(self, b=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## greater_than

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def greater_than(self, b=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## inverse_sqrt

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def inverse_sqrt(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## less_equal

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def less_equal(self, b=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## less_than

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def less_than(self, b=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## log

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def log(self, base=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- base: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## logarithm

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def logarithm(self, base=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- base: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## map_range

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- steps: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): True
<sub>Go to [top](#class-Float)</sub>

- interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## map_range_linear

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): True
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## map_range_smooth

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): True
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## map_range_smoother

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): True
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## map_range_stepped

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- steps: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): True
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_ceil

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_ceil(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_compare

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_compare(self, value=None, epsilon=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- epsilon: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_floor

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_floor(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_greater_than

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_greater_than(self, threshold=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- threshold: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_less_than

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_less_than(self, threshold=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- threshold: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_round

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_round(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_trunc

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_trunc(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## math_truncate

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def math_truncate(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## max

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def max(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## maximum

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def maximum(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## min

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def min(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## minimum

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def minimum(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## mix

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def mix(self, factor=None, value=None, clamp_factor=True):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Float)</sub>

- value: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Float)</sub>

- clamp_factor (bool): True
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## modulo

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def modulo(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## mul_add

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def mul_add(self, multiplier=None, addend=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- multiplier: Float
<sub>Go to [top](#class-Float)</sub>

- addend: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## multiply_add

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def multiply_add(self, multiplier=None, addend=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- multiplier: Float
<sub>Go to [top](#class-Float)</sub>

- addend: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## not_equal

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def not_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Float)</sub>

- epsilon: Float
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'result'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## ping_pong

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def ping_pong(self, scale=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- scale: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## pow

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def pow(self, exponent=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- exponent: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## power

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def power(self, exponent=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- exponent: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## round

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def round(self):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'integer'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## sign

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def sign(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## sin

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def sin(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## sine

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def sine(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## sinh

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def sinh(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## smooth_maximum

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def smooth_maximum(self, value=None, distance=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- distance: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## smooth_minimum

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def smooth_minimum(self, value=None, distance=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- distance: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## snap

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def snap(self, increment=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- increment: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## sqrt

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def sqrt(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## switch

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Float)</sub>

- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'output'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## tan

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def tan(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## tangent

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def tangent(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## tanh

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def tanh(self, value=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- value: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## to_degrees

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def to_degrees(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## to_integer

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def to_integer(self, rounding_mode='ROUND'):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'integer'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## to_radians

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def to_radians(self, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## to_string

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def to_string(self, decimals=None):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- decimals: Integer
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'string'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## truncate

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def truncate(self):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html) )

<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'integer'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

## wrap

<sub>Go to [top](#class-Float)</sub>

```python
<sub>Go to [top](#class-Float)</sub>

def wrap(self, max=None, min=None, clamp=False):

<sub>Go to [top](#class-Float)</sub>

```
<sub>Go to [top](#class-Float)</sub>

Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

<sub>Go to [top](#class-Float)</sub>

### Args:
<sub>Go to [top](#class-Float)</sub>

- max: Float
<sub>Go to [top](#class-Float)</sub>

- min: Float
<sub>Go to [top](#class-Float)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

### Returns:

<sub>Go to [top](#class-Float)</sub>

  socket 'value'<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>


<sub>Go to [top](#class-Float)</sub>

