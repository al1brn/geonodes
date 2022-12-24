# Class Vector

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Vector DataSocket

Vector exposes properties: `x`, `y` and `z`:
    
```python
v = Vector()
v.x = 1
v.y = 2

# Translate the vertices have been translated of (1, 2, 0)
geometry.verts.offset = v    




### Constructor

```python
Vector(self, value=(0., 0., 0.), label=None)
```

## Content

**Properties**

[length](#length) | [separate](#separate)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[AlignToVector](#AlignToVector) | [Combine](#Combine) | [Input](#Input) | [Random](#Random) | [Rotation](#Rotation) | [Translation](#Translation) | [Vector](#Vector) | [VectorXYZ](#VectorXYZ)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [align_euler_to_vector](#align_euler_to_vector) | [average_equal](#average_equal) | [average_greater_equal](#average_greater_equal) | [average_greater_than](#average_greater_than) | [average_less_equal](#average_less_equal) | [average_less_than](#average_less_than) | [average_not_equal](#average_not_equal) | [ceil](#ceil) | [compare](#compare) | [cos](#cos) | [cosine](#cosine) | [cross](#cross) | [cross_product](#cross_product) | [curves](#curves) | [direction_equal](#direction_equal) | [direction_greater_equal](#direction_greater_equal) | [direction_greater_than](#direction_greater_than) | [direction_less_equal](#direction_less_equal) | [direction_less_than](#direction_less_than) | [direction_not_equal](#direction_not_equal) | [distance](#distance) | [div](#div) | [divide](#divide) | [dot](#dot) | [dot_product](#dot_product) | [dot_product_equal](#dot_product_equal) | [dot_product_greater_equal](#dot_product_greater_equal) | [dot_product_greater_than](#dot_product_greater_than) | [dot_product_less_equal](#dot_product_less_equal) | [dot_product_less_than](#dot_product_less_than) | [dot_product_not_equal](#dot_product_not_equal) | [elements_equal](#elements_equal) | [elements_greater_equal](#elements_greater_equal) | [elements_greater_than](#elements_greater_than) | [elements_less_equal](#elements_less_equal) | [elements_less_than](#elements_less_than) | [elements_not_equal](#elements_not_equal) | [face_forward](#face_forward) | [floor](#floor) | [fract](#fract) | [fraction](#fraction) | [get_blender_socket](#get_blender_socket) | [length_equal](#length_equal) | [length_greater_equal](#length_greater_equal) | [length_greater_than](#length_greater_than) | [length_less_equal](#length_less_equal) | [length_less_than](#length_less_than) | [length_not_equal](#length_not_equal) | [map_range](#map_range) | [map_range_linear](#map_range_linear) | [map_range_smooth](#map_range_smooth) | [map_range_smoother](#map_range_smoother) | [map_range_stepped](#map_range_stepped) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [mix](#mix) | [mix_non_uniform](#mix_non_uniform) | [mix_uniform](#mix_uniform) | [modulo](#modulo) | [mul](#mul) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [normalize](#normalize) | [project](#project) | [reflect](#reflect) | [refract](#refract) | [rotate_axis_angle](#rotate_axis_angle) | [rotate_euler](#rotate_euler) | [rotate_x](#rotate_x) | [rotate_y](#rotate_y) | [rotate_z](#rotate_z) | [scale](#scale) | [sin](#sin) | [sine](#sine) | [snap](#snap) | [sub](#sub) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [wrap](#wrap)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### length



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `value`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate



> Node: [Separate XYZ](ShaderNodeSeparateXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)

#### Returns:
- node with sockets ['x', 'y', 'z']






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### AlignToVector

```python
@classmethod
def AlignToVector(cls, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```



> Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

#### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

#### Returns:
- socket `rotation`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Combine

```python
@classmethod
def Combine(cls, x=None, y=None, z=None)
```



> Node: [Combine XYZ](ShaderNodeCombineXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)

#### Args:
- x: Float
- y: Float
- z: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, value = (0, 0, 0), name = "Vector", description = "")
```

 Create a Vector input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Vector: The Vector data socket




<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Random

```python
@classmethod
def Random(cls, min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Rotation

```python
@classmethod
def Rotation(cls, value = (0, 0, 0), name = "Rotation", description = "")
```

 Create a Rotation input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Vector: The Vector data socket



<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Translation

```python
@classmethod
def Translation(cls, value =(0, 0, 0), name = "Translation", description = "")
```

 Create a Translation input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Vector: The Vector data socket



<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Vector

```python
@classmethod
def Vector(cls, vector=[0.0, 0.0, 0.0])
```



> Node: [Vector](FunctionNodeInputVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)

#### Args:
- vector (list): [0.0, 0.0, 0.0]

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### VectorXYZ

```python
@classmethod
def VectorXYZ(cls, value = (0, 0, 0), name = "VectorXYZ", description = "")
```

 Create a Vector XYZ input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- description: User tip
    
#### Returns:
- Vector: The Vector data socket



<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### abs

```python
def abs(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### add

```python
def add(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### align_euler_to_vector

```python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```



> Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

#### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

#### Returns:
- self






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_equal

```python
def average_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_greater_equal

```python
def average_greater_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_greater_than

```python
def average_greater_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_equal

```python
def average_less_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_than

```python
def average_less_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_not_equal

```python
def average_not_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ceil

```python
def ceil(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN')
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cos

```python
def cos(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross

```python
def cross(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross_product

```python
def cross_product(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curves

```python
def curves(self, fac=None)
```



> Node: [Vector Curves](ShaderNodeVectorCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)

#### Args:
- fac: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_equal

```python
def direction_equal(self, b=None, angle=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_greater_equal

```python
def direction_greater_equal(self, b=None, angle=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_greater_than

```python
def direction_greater_than(self, b=None, angle=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_less_equal

```python
def direction_less_equal(self, b=None, angle=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_less_than

```python
def direction_less_than(self, b=None, angle=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_not_equal

```python
def direction_not_equal(self, b=None, angle=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distance

```python
def distance(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### div

```python
def div(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### divide

```python
def divide(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot

```python
def dot(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product

```python
def dot_product(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_equal

```python
def dot_product_equal(self, b=None, c=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_greater_equal

```python
def dot_product_greater_equal(self, b=None, c=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_greater_than

```python
def dot_product_greater_than(self, b=None, c=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_less_equal

```python
def dot_product_less_equal(self, b=None, c=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_less_than

```python
def dot_product_less_than(self, b=None, c=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_not_equal

```python
def dot_product_not_equal(self, b=None, c=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_equal

```python
def elements_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_greater_equal

```python
def elements_greater_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_greater_than

```python
def elements_greater_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_equal

```python
def elements_less_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_than

```python
def elements_less_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_not_equal

```python
def elements_not_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_forward

```python
def face_forward(self, incident=None, reference=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- incident: Vector
- reference: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### floor

```python
def floor(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fract

```python
def fract(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Overrides the standard behavior of :class:DataSocket super class

If the `x`, `y`, `z` properties have been read or modified, a *Combine XYZ* node is necessary
to recompose the Vector.




<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_equal

```python
def length_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_greater_equal

```python
def length_greater_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_greater_than

```python
def length_greater_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_equal

```python
def length_less_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_than

```python
def length_less_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_not_equal

```python
def length_not_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range

```python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR')
```



> Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True
- interpolation_type (str): 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



> Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



> Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



> Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True)
```



> Node: [Map Range](ShaderNodeMapRange.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM')
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_non_uniform

```python
def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_uniform

```python
def mix_uniform(self, vector=None, clamp_factor=True)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### modulo

```python
def modulo(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul

```python
def mul(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(self, multiplier=None, addend=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- multiplier: Vector
- addend: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply

```python
def multiply(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- multiplier: Vector
- addend: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normalize

```python
def normalize(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### project

```python
def project(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reflect

```python
def reflect(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### refract

```python
def refract(self, vector=None, ior=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector
- ior: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_axis_angle

```python
def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False)
```



> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- axis: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_euler

```python
def rotate_euler(self, center=None, rotation=None, invert=False)
```



> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- rotation: Vector
- invert (bool): False

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_x

```python
def rotate_x(self, center=None, angle=None, invert=False)
```



> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_y

```python
def rotate_y(self, center=None, angle=None, invert=False)
```



> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_z

```python
def rotate_z(self, center=None, angle=None, invert=False)
```



> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale

```python
def scale(self, scale=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- scale: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(self, increment=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- increment: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sub

```python
def sub(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subtract

```python
def subtract(self, vector=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Vector

#### Returns:
- socket `output`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tan

```python
def tan(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(self)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(self, max=None, min=None)
```



> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- max: Vector
- min: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

