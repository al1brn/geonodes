# class Integer

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


## Class methods

- [Input](#Input-classmethod)
- [Integer](#Integer-classmethod)


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
- [fraction](#fraction)
- [greater_equal](#greater_equal)
- [greater_than](#greater_than)
- [inverse_sqrt](#inverse_sqrt)
- [less_equal](#less_equal)
- [less_than](#less_than)
- [log](#log)
- [logarithm](#logarithm)
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
- [modulo](#modulo)
- [mul](#mul)
- [mul_add](#mul_add)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [not_equal](#not_equal)
- [ping_pong](#ping_pong)
- [pow](#pow)
- [power](#power)
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
- [to_radians](#to_radians)
- [to_string](#to_string)
- [wrap](#wrap)

## Input <sub>*classmethod*</sub>

```python
def Input(cls, value=None, name="CLASS_METHOD", min_value=None, max_value=None, description=""):

```
Used to create an input socket in the Group Input node.
Even if homonyms are accepted, it is recommended to avoid to create to input sockets with the same name.

#### Args:
- value: Initial value. Not changed if the group input socket already exists
- name: Input socket name. Avoid homonyms!
- min_value: minimum value
- max_value: maxium value
- description: user help

#### Returns:
- Integer

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Integer <sub>*classmethod*</sub>

```python
def Integer(cls, integer=0):

```
Node [Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/integer.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html) )

#### Args:
- integer (int): 0

#### Returns:
- socket `integer`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## abs

```python
def abs(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## absolute

```python
def absolute(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## add

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float or Integer or Vector

#### Returns:
- self + value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arccos

```python
def arccos(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arccosine

```python
def arccosine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arcsin

```python
def arcsin(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arcsine

```python
def arcsine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arctan

```python
def arctan(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arctan2

```python
def arctan2(self, value1=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## arctangent

```python
def arctangent(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## compare

```python
def compare(self, b=None, operation='GREATER_THAN'):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## cos

```python
def cos(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## cosh

```python
def cosh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## cosine

```python
def cosine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## div

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float

#### Returns:
- self / value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## divide

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float

#### Returns:
- self / value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## equal

```python
def equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## exp

```python
def exp(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## exponent

```python
def exponent(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fact

```python
def fact(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## fraction

```python
def fraction(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## greater_equal

```python
def greater_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## greater_than

```python
def greater_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## inverse_sqrt

```python
def inverse_sqrt(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## less_equal

```python
def less_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## less_than

```python
def less_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## log

```python
def log(self, base=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## logarithm

```python
def logarithm(self, base=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_ceil

```python
def math_ceil(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_floor

```python
def math_floor(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_less_than

```python
def math_less_than(self, threshold=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_round

```python
def math_round(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_trunc

```python
def math_trunc(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## math_truncate

```python
def math_truncate(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## max

```python
def max(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## maximum

```python
def maximum(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## min

```python
def min(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## minimum

```python
def minimum(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## modulo

```python
def modulo(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mul

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float or Integer or Vector

#### Returns:
- self * value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## multiply

```python
def multiply(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float or Integer or Vector

#### Returns:
- self * value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## not_equal

```python
def not_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## ping_pong

```python
def ping_pong(self, scale=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- scale: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## pow

```python
def pow(self, exponent=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## power

```python
def power(self, exponent=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sign

```python
def sign(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sin

```python
def sin(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sine

```python
def sine(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sinh

```python
def sinh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## snap

```python
def snap(self, increment=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- increment: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sqrt

```python
def sqrt(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sub

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float or Integer or Vector

#### Returns:
- self - value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## subtract

```python
def add(self, value):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float or Integer or Vector

#### Returns:
- self - value

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

#### Args:
- switch: Boolean
- true: Integer

#### Returns:
- socket `output`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tan

```python
def tan(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tangent

```python
def tangent(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tanh

```python
def tanh(self, value=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_degrees

```python
def to_degrees(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_radians

```python
def to_radians(self, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_string

```python
def to_string(self):

```
Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html) )

### Returns:
- socket `string`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## wrap

```python
def wrap(self, max=None, min=None, clamp=False):

```
Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html) )

#### Args:
- max: Float
- min: Float
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Integer) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

