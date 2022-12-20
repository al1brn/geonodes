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

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def Combine(cls, x=None, y=None, z=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- x: Float
<sub>Go to [top](#class-Vector)</sub>- y: Float
<sub>Go to [top](#class-Vector)</sub>- z: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## Vector <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def Vector(cls, vector=[0.0, 0.0, 0.0]):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector (list): [0.0, 0.0, 0.0]
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## abs

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def abs(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## absolute

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def absolute(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## add

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def add(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## align_euler_to_vector

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- factor: Float
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>- axis (str): 'X' in [X, Y, Z]
<sub>Go to [top](#class-Vector)</sub>- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>- node with sockets ['rotation']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_greater_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_greater_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_greater_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_greater_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_less_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_less_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_less_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_less_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## average_not_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def average_not_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## ceil

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def ceil(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## compare

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
<sub>Go to [top](#class-Vector)</sub>- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## cos

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def cos(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## cosine

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def cosine(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## cross

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def cross(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## cross_product

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def cross_product(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## curves

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def curves(self, fac=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- fac: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_equal(self, b=None, angle=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_greater_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_greater_equal(self, b=None, angle=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_greater_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_greater_than(self, b=None, angle=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_less_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_less_equal(self, b=None, angle=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_less_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_less_than(self, b=None, angle=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## direction_not_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def direction_not_equal(self, b=None, angle=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## distance

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def distance(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'value'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## div

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def div(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## divide

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def divide(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'value'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'value'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_equal(self, b=None, c=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_greater_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_greater_equal(self, b=None, c=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_greater_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_greater_than(self, b=None, c=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_less_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_less_equal(self, b=None, c=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_less_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_less_than(self, b=None, c=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## dot_product_not_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def dot_product_not_equal(self, b=None, c=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- c: Float
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_greater_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_greater_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_greater_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_greater_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_less_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_less_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_less_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_less_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## elements_not_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def elements_not_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## face_forward

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def face_forward(self, incident=None, reference=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- incident: Vector
<sub>Go to [top](#class-Vector)</sub>- reference: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## floor

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def floor(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## fract

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def fract(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## fraction

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def fraction(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>Node implemented as property.

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'value'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_greater_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_greater_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_greater_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_greater_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_less_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_less_equal(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_less_than

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_less_than(self, b=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## length_not_equal

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def length_not_equal(self, b=None, epsilon=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
<sub>Go to [top](#class-Vector)</sub>- epsilon: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## map_range

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- steps: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- clamp (bool): True
<sub>Go to [top](#class-Vector)</sub>- interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## map_range_linear

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- clamp (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## map_range_smooth

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- clamp (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## map_range_smoother

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- clamp (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## map_range_stepped

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- from_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- from_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_min: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- to_max: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- steps: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- clamp (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## max

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def max(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## maximum

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def maximum(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## min

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def min(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## minimum

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def minimum(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## mix

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- vector: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Vector)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-Vector)</sub>- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## mix_non_uniform

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- factor: ['Float', 'Vector']
<sub>Go to [top](#class-Vector)</sub>- vector: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Vector)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## mix_uniform

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def mix_uniform(self, vector=None, clamp_factor=True):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: ['Float', 'Vector', 'Color']
<sub>Go to [top](#class-Vector)</sub>- clamp_factor (bool): True
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'result'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## modulo

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def modulo(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## mul

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def mul(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## mul_add

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def mul_add(self, multiplier=None, addend=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- multiplier: Vector
<sub>Go to [top](#class-Vector)</sub>- addend: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## multiply

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def multiply(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## multiply_add

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def multiply_add(self, multiplier=None, addend=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- multiplier: Vector
<sub>Go to [top](#class-Vector)</sub>- addend: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## normalize

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def normalize(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## project

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def project(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## reflect

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def reflect(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## refract

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def refract(self, vector=None, ior=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>- ior: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## rotate_axis_angle

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- center: Vector
<sub>Go to [top](#class-Vector)</sub>- axis: Vector
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- invert (bool): False
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## rotate_euler

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def rotate_euler(self, center=None, rotation=None, invert=False):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- center: Vector
<sub>Go to [top](#class-Vector)</sub>- rotation: Vector
<sub>Go to [top](#class-Vector)</sub>- invert (bool): False
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## rotate_x

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def rotate_x(self, center=None, angle=None, invert=False):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- center: Vector
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- invert (bool): False
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## rotate_y

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def rotate_y(self, center=None, angle=None, invert=False):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- center: Vector
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- invert (bool): False
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## rotate_z

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def rotate_z(self, center=None, angle=None, invert=False):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- center: Vector
<sub>Go to [top](#class-Vector)</sub>- angle: Float
<sub>Go to [top](#class-Vector)</sub>- invert (bool): False
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## scale

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def scale(self, scale=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- scale: Float
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## separate <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def separate(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html) )

<sub>Go to [top](#class-Vector)</sub>Node implemented as property.

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>- node with sockets ['x', 'y', 'z']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## sin

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def sin(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## sine

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def sine(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## snap

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def snap(self, increment=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- increment: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## sub

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def sub(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## subtract

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def subtract(self, vector=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- vector: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## switch

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def switch(self, switch=None, true=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- switch: ['Boolean', 'Boolean']
<sub>Go to [top](#class-Vector)</sub>- true: ['Float', 'Integer', 'Boolean', 'Vector', 'Color', 'String', 'Geometry', 'Object', 'Collection', 'Texture', 'Material', 'Image']
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'output'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## tan

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def tan(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## tangent

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def tangent(self):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>## wrap

<sub>Go to [top](#class-Vector)</sub>```python
<sub>Go to [top](#class-Vector)</sub>def wrap(self, max=None, min=None):

<sub>Go to [top](#class-Vector)</sub>```
<sub>Go to [top](#class-Vector)</sub>Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) ( [api](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html) )

<sub>Go to [top](#class-Vector)</sub>### Args:
<sub>Go to [top](#class-Vector)</sub>- max: Vector
<sub>Go to [top](#class-Vector)</sub>- min: Vector
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>### Returns:

<sub>Go to [top](#class-Vector)</sub>  socket 'vector'<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>
<sub>Go to [top](#class-Vector)</sub>