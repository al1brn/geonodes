# class Vector

## Properties

- [length](#length-property)
- [separate](#separate-property)

## Class methods

- [Combine](#Combine-classmethod)
- [Vector](#Vector-classmethod)


## Methods

- [abs](#abs)
- [absolute](#absolute)
- [add](#add)
- [align_euler_to_vector](#align_euler_to_vector)
- [average_equal](#average_equal)
- [average_greater_equal](#average_greater_equal)
- [average_greater_than](#average_greater_than)
- [average_less_equal](#average_less_equal)
- [average_less_than](#average_less_than)
- [average_not_equal](#average_not_equal)
- [ceil](#ceil)
- [compare](#compare)
- [cos](#cos)
- [cosine](#cosine)
- [cross](#cross)
- [cross_product](#cross_product)
- [curves](#curves)
- [direction_equal](#direction_equal)
- [direction_greater_equal](#direction_greater_equal)
- [direction_greater_than](#direction_greater_than)
- [direction_less_equal](#direction_less_equal)
- [direction_less_than](#direction_less_than)
- [direction_not_equal](#direction_not_equal)
- [distance](#distance)
- [div](#div)
- [divide](#divide)
- [dot](#dot)
- [dot_product](#dot_product)
- [dot_product_equal](#dot_product_equal)
- [dot_product_greater_equal](#dot_product_greater_equal)
- [dot_product_greater_than](#dot_product_greater_than)
- [dot_product_less_equal](#dot_product_less_equal)
- [dot_product_less_than](#dot_product_less_than)
- [dot_product_not_equal](#dot_product_not_equal)
- [elements_equal](#elements_equal)
- [elements_greater_equal](#elements_greater_equal)
- [elements_greater_than](#elements_greater_than)
- [elements_less_equal](#elements_less_equal)
- [elements_less_than](#elements_less_than)
- [elements_not_equal](#elements_not_equal)
- [face_forward](#face_forward)
- [floor](#floor)
- [fract](#fract)
- [fraction](#fraction)
- [length_equal](#length_equal)
- [length_greater_equal](#length_greater_equal)
- [length_greater_than](#length_greater_than)
- [length_less_equal](#length_less_equal)
- [length_less_than](#length_less_than)
- [length_not_equal](#length_not_equal)
- [map_range](#map_range)
- [map_range_linear](#map_range_linear)
- [map_range_smooth](#map_range_smooth)
- [map_range_smoother](#map_range_smoother)
- [map_range_stepped](#map_range_stepped)
- [max](#max)
- [maximum](#maximum)
- [min](#min)
- [minimum](#minimum)
- [mix](#mix)
- [mix_non_uniform](#mix_non_uniform)
- [mix_uniform](#mix_uniform)
- [modulo](#modulo)
- [mul](#mul)
- [mul_add](#mul_add)
- [multiply](#multiply)
- [multiply_add](#multiply_add)
- [normalize](#normalize)
- [project](#project)
- [reflect](#reflect)
- [refract](#refract)
- [rotate_axis_angle](#rotate_axis_angle)
- [rotate_euler](#rotate_euler)
- [rotate_x](#rotate_x)
- [rotate_y](#rotate_y)
- [rotate_z](#rotate_z)
- [scale](#scale)
- [sin](#sin)
- [sine](#sine)
- [snap](#snap)
- [sub](#sub)
- [subtract](#subtract)
- [switch](#switch)
- [tan](#tan)
- [tangent](#tangent)
- [wrap](#wrap)

## Combine <span style="color:blue">*classmethod*</span>

```python
def Combine(cls, x=None, y=None, z=None):

```
Node [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html) )

### Args:
- x: Float
- y: Float
- z: Float

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## Vector <span style="color:blue">*classmethod*</span>

```python
def Vector(cls, vector=[0.0, 0.0, 0.0]):

```
Node [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html) )

### Args:
- vector (list): [0.0, 0.0, 0.0]

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## abs

```python
def abs(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## absolute

```python
def absolute(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## add

```python
def add(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## align_euler_to_vector

```python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

```
Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html) )

### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

### Returns:

- node with sockets ['rotation']

<sub>Go to [top](#class-Vector)</sub>

## average_equal

```python
def average_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## average_greater_equal

```python
def average_greater_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## average_greater_than

```python
def average_greater_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## average_less_equal

```python
def average_less_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## average_less_than

```python
def average_less_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## average_not_equal

```python
def average_not_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## ceil

```python
def ceil(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## compare

```python
def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## cos

```python
def cos(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## cosine

```python
def cosine(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## cross

```python
def cross(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## cross_product

```python
def cross_product(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## curves

```python
def curves(self, fac=None):

```
Node [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html) )

### Args:
- fac: Float

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## direction_equal

```python
def direction_equal(self, b=None, angle=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## direction_greater_equal

```python
def direction_greater_equal(self, b=None, angle=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## direction_greater_than

```python
def direction_greater_than(self, b=None, angle=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## direction_less_equal

```python
def direction_less_equal(self, b=None, angle=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## direction_less_than

```python
def direction_less_than(self, b=None, angle=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## direction_not_equal

```python
def direction_not_equal(self, b=None, angle=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## distance

```python
def distance(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'value'

<sub>Go to [top](#class-Vector)</sub>

## div

```python
def div(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## divide

```python
def divide(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## dot

```python
def dot(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'value'

<sub>Go to [top](#class-Vector)</sub>

## dot_product

```python
def dot_product(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'value'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_equal

```python
def dot_product_equal(self, b=None, c=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_greater_equal

```python
def dot_product_greater_equal(self, b=None, c=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_greater_than

```python
def dot_product_greater_than(self, b=None, c=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_less_equal

```python
def dot_product_less_equal(self, b=None, c=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_less_than

```python
def dot_product_less_than(self, b=None, c=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## dot_product_not_equal

```python
def dot_product_not_equal(self, b=None, c=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_equal

```python
def elements_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_greater_equal

```python
def elements_greater_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_greater_than

```python
def elements_greater_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_less_equal

```python
def elements_less_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_less_than

```python
def elements_less_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## elements_not_equal

```python
def elements_not_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## face_forward

```python
def face_forward(self, incident=None, reference=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- incident: Vector
- reference: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## floor

```python
def floor(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## fract

```python
def fract(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## fraction

```python
def fraction(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## length <span style="color:blue">*property*</span>

```python
def length(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

Node implemented as property.

### Returns:

  socket 'value'

<sub>Go to [top](#class-Vector)</sub>

## length_equal

```python
def length_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## length_greater_equal

```python
def length_greater_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## length_greater_than

```python
def length_greater_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## length_less_equal

```python
def length_less_equal(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## length_less_than

```python
def length_less_than(self, b=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## length_not_equal

```python
def length_not_equal(self, b=None, epsilon=None):

```
Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

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

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

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

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

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

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

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

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

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

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## max

```python
def max(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## maximum

```python
def maximum(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## min

```python
def min(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## minimum

```python
def minimum(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## mix

```python
def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## mix_non_uniform

```python
def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## mix_uniform

```python
def mix_uniform(self, vector=None, clamp_factor=True):

```
Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

### Args:
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

### Returns:

  socket 'result'

<sub>Go to [top](#class-Vector)</sub>

## modulo

```python
def modulo(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## mul

```python
def mul(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## mul_add

```python
def mul_add(self, multiplier=None, addend=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- multiplier: Vector
- addend: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## multiply

```python
def multiply(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## multiply_add

```python
def multiply_add(self, multiplier=None, addend=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- multiplier: Vector
- addend: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## normalize

```python
def normalize(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## project

```python
def project(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## reflect

```python
def reflect(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## refract

```python
def refract(self, vector=None, ior=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector
- ior: Float

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## rotate_axis_angle

```python
def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):

```
Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

### Args:
- center: Vector
- axis: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## rotate_euler

```python
def rotate_euler(self, center=None, rotation=None, invert=False):

```
Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

### Args:
- center: Vector
- rotation: Vector
- invert (bool): False

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## rotate_x

```python
def rotate_x(self, center=None, angle=None, invert=False):

```
Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## rotate_y

```python
def rotate_y(self, center=None, angle=None, invert=False):

```
Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## rotate_z

```python
def rotate_z(self, center=None, angle=None, invert=False):

```
Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

### Args:
- center: Vector
- angle: Float
- invert (bool): False

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## scale

```python
def scale(self, scale=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- scale: Float

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## separate <span style="color:blue">*property*</span>

```python
def separate(self):

```
Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html) )

Node implemented as property.

### Returns:

- node with sockets ['x', 'y', 'z']

<sub>Go to [top](#class-Vector)</sub>

## sin

```python
def sin(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## sine

```python
def sine(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## snap

```python
def snap(self, increment=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- increment: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## sub

```python
def sub(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## subtract

```python
def subtract(self, vector=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- vector: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## switch

```python
def switch(self, switch=None, true=None):

```
Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

### Args:
- switch: ['Boolean', 'Boolean']
- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']

### Returns:

  socket 'output'

<sub>Go to [top](#class-Vector)</sub>

## tan

```python
def tan(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## tangent

```python
def tangent(self):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

## wrap

```python
def wrap(self, max=None, min=None):

```
Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

### Args:
- max: Vector
- min: Vector

### Returns:

  socket 'vector'

<sub>Go to [top](#class-Vector)</sub>

