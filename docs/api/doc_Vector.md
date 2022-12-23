# Class Vector

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [length](#length) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [separate](#separate) | [socket_index](#socket_index)

**Class and static methods**

[Combine](#Combine) | [Input](#Input) | [Rotation](#Rotation) | [Translation](#Translation) | [Vector](#Vector) | [VectorXYZ](#VectorXYZ) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [align_euler_to_vector](#align_euler_to_vector) | [average_equal](#average_equal) | [average_greater_equal](#average_greater_equal) | [average_greater_than](#average_greater_than) | [average_less_equal](#average_less_equal) | [average_less_than](#average_less_than) | [average_not_equal](#average_not_equal) | [ceil](#ceil) | [compare](#compare) | [connected_sockets](#connected_sockets) | [cos](#cos) | [cosine](#cosine) | [cross](#cross) | [cross_product](#cross_product) | [curves](#curves) | [direction_equal](#direction_equal) | [direction_greater_equal](#direction_greater_equal) | [direction_greater_than](#direction_greater_than) | [direction_less_equal](#direction_less_equal) | [direction_less_than](#direction_less_than) | [direction_not_equal](#direction_not_equal) | [distance](#distance) | [div](#div) | [divide](#divide) | [dot](#dot) | [dot_product](#dot_product) | [dot_product_equal](#dot_product_equal) | [dot_product_greater_equal](#dot_product_greater_equal) | [dot_product_greater_than](#dot_product_greater_than) | [dot_product_less_equal](#dot_product_less_equal) | [dot_product_less_than](#dot_product_less_than) | [dot_product_not_equal](#dot_product_not_equal) | [elements_equal](#elements_equal) | [elements_greater_equal](#elements_greater_equal) | [elements_greater_than](#elements_greater_than) | [elements_less_equal](#elements_less_equal) | [elements_less_than](#elements_less_than) | [elements_not_equal](#elements_not_equal) | [face_forward](#face_forward) | [floor](#floor) | [fract](#fract) | [fraction](#fraction) | [get_blender_socket](#get_blender_socket) | [init_domains](#init_domains) | [init_socket](#init_socket) | [length_equal](#length_equal) | [length_greater_equal](#length_greater_equal) | [length_greater_than](#length_greater_than) | [length_less_equal](#length_less_equal) | [length_less_than](#length_less_than) | [length_not_equal](#length_not_equal) | [map_range](#map_range) | [map_range_linear](#map_range_linear) | [map_range_smooth](#map_range_smooth) | [map_range_smoother](#map_range_smoother) | [map_range_stepped](#map_range_stepped) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [mix](#mix) | [mix_non_uniform](#mix_non_uniform) | [mix_uniform](#mix_uniform) | [modulo](#modulo) | [mul](#mul) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [normalize](#normalize) | [plug](#plug) | [project](#project) | [reflect](#reflect) | [refract](#refract) | [reroute](#reroute) | [reset_properties](#reset_properties) | [rotate_axis_angle](#rotate_axis_angle) | [rotate_euler](#rotate_euler) | [rotate_x](#rotate_x) | [rotate_y](#rotate_y) | [rotate_z](#rotate_z) | [scale](#scale) | [sin](#sin) | [sine](#sine) | [snap](#snap) | [stack](#stack) | [sub](#sub) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [to_output](#to_output) | [view](#view) | [wrap](#wrap)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### bnode

 Shortcut for `self.bsocket.node`



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### length

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `value`



### links

 Shortcut for `self.bsocket.links`



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### separate

 Node SeparateXyz.

Node reference [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html)
Developer reference [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)

#### Returns:
- node with sockets ['x', 'y', 'z']



### socket_index

#### Returns:

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




## Class and static methods

### Combine

```python
@classmethod
def Combine(cls, x=None, y=None, z=None)
```

 Node CombineXyz.

Node reference [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html)
Developer reference [ShaderNodeCombineXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)

#### Args:
- x: Float
- y: Float
- z: Float

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Vector

```python
@classmethod
def Vector(cls, vector=[0.0, 0.0, 0.0])
```

 Node Vector.

Node reference [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html)
Developer reference [FunctionNodeInputVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)

#### Args:
- vector (list): [0.0, 0.0, 0.0]

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

:param class_name: The class name
:type class_name: str
:return: The bl_idname associated to this class name
:rtype: str

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to *sub classes*:
    
.. list-table:: 
   :widths: 20 40
   :header-rows: 0

   * - Unsigned
     - Integer sub class (NodeSocketIntUnsigned)
   * - Factor
     - Float sub class (NodeSocketFloatFactor)
   * - Angle
     - Float sub class  (NodeSocketFloatAngle)
   * - Distance
     - Float sub class (NodeSocketFloatDistance)
   * - Rotation
     - Vector sub class (NodeSocketVectorEuler)
   * - xyz
     - Vector sub class (NodeSocketVectorXYZ)
   * - Translation
     - Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

:param socket: The socket to determine the class of
:param with_sub_class: Return the sub class if True
:typ socket: bpy.types.NodeSocket, Socket
:type with_sub_class: bool
:return: The name of the class associated to the bl_idname of the socket
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20 20
   :header-rows: 1
   
   * - NodeSocket
     - class name
     - sub class name
   * - NodeSocketBool 
     - 'Boolean'
     - 
   * - NodeSocketInt 
     - 'Integer'
     - 
   * - NodeSocketIntUnsigned 
     - 'Integer'
     - 'Unsigned'
   * - NodeSocketFloat 
     - 'Float' 
     - 
   * - NodeSocketFloatFactor 
     - 'Float'
     - 'Factor'
   * - NodeSocketFloatAngle  
     - 'Float'
     - 'Angle'
   * - NodeSocketFloatDistance 
     - 'Float'
     - 'Distance'
   * - NodeSocketVector 
     - 'Vector'
     - 
   * - NodeSocketVectorEuler 
     - 'Vector'
     - 'Rotation'
   * - NodeSocketVectorXYZ 
     - 'Vector'
     - 'xyz'
   * - NodeSocketVectorTranslation 
     - 'Vector'
     - 'Translation'
   * - NodeSocketColor 
     - 'Color'
     - 
   * - NodeSocketString' 
     - 'String'
     - 
   * - NodeSocketCollection 
     - 'Collection'
     - 
   * - NodeSocketImage 
     - 'Image'
     - 
   * - NodeSocketMaterial 
     - 'Material'
     - 
   * - NodeSocketObject 
     - 'Object'
     - 
   * - NodeSocketTexture 
     - 'Texture'
     - 
   * - NodeSocketGeometry
     - 'Geometry'
     - 
  
  
If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

:param value: The value to test
:type value: any
:return: True if *value* is or wraps a socket
:rtype: bool

#### Returns:
    
- A Blender Geometry Node Socket
- An instance of Socket        




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

#### Returns:

:param value: The socket
:type value: any
:return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20
   :header-rows: 1

   * - Socket bl_idname
     - Domain code
   * - NodeSocketBool
     - 'BOOLEAN'
   * - NodeSocketInt               
     - 'INT'
   * - NodeSocketIntUnsigned       
     - 'INT'
   * - NodeSocketFloat            
     - 'FLOAT'
   * - NodeSocketFloatFactor       
     - 'FLOAT'
   * - NodeSocketFloatAngle        
     - 'FLOAT'
   * - NodeSocketFloatDistance     
     - 'FLOAT'         
   * - NodeSocketVector            
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorEuler       
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorXYZ         
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorTranslation
     - 'FLOAT_VECTOR'
   * - NodeSocketColor      
     - 'FLOAT_COLOR'
   * - NodeSocketString           
     - 'FLOAT_COLOR'





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### abs

```python
def abs(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### add

```python
def add(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### align_euler_to_vector

```python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```

 Node AlignEulerToVector.

Node reference [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html)
Developer reference [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

#### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

#### Returns:
- node with sockets ['rotation']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_equal

```python
def average_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_greater_equal

```python
def average_greater_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_greater_than

```python
def average_greater_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_equal

```python
def average_less_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_than

```python
def average_less_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_not_equal

```python
def average_not_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ceil

```python
def ceil(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN')
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- angle: Float
- epsilon: Float
- mode (str): 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### connected_sockets

```python
def connected_sockets(self)
```

#### Returns:




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cos

```python
def cos(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross

```python
def cross(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross_product

```python
def cross_product(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curves

```python
def curves(self, fac=None)
```

 Node VectorCurves.

Node reference [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html)
Developer reference [ShaderNodeVectorCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)

#### Args:
- fac: Float

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_equal

```python
def direction_equal(self, b=None, angle=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_greater_equal

```python
def direction_greater_equal(self, b=None, angle=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_greater_than

```python
def direction_greater_than(self, b=None, angle=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_less_equal

```python
def direction_less_equal(self, b=None, angle=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_less_than

```python
def direction_less_than(self, b=None, angle=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_not_equal

```python
def direction_not_equal(self, b=None, angle=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- angle: Float
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distance

```python
def distance(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### div

```python
def div(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### divide

```python
def divide(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot

```python
def dot(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product

```python
def dot_product(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_equal

```python
def dot_product_equal(self, b=None, c=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_greater_equal

```python
def dot_product_greater_equal(self, b=None, c=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_greater_than

```python
def dot_product_greater_than(self, b=None, c=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_less_equal

```python
def dot_product_less_equal(self, b=None, c=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_less_than

```python
def dot_product_less_than(self, b=None, c=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_not_equal

```python
def dot_product_not_equal(self, b=None, c=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- c: Float
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_equal

```python
def elements_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_greater_equal

```python
def elements_greater_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_greater_than

```python
def elements_greater_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_equal

```python
def elements_less_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_than

```python
def elements_less_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_not_equal

```python
def elements_not_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_forward

```python
def face_forward(self, incident=None, reference=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- incident: Vector
- reference: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### floor

```python
def floor(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fract

```python
def fract(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Overrides the standard behavior of :class:DataSocket super class

If the `x`, `y`, `z` properties have been read or modified, a *Combine XYZ* node is necessary
to recompose the Vector.

.. blid:: ShaderNodeCombineXYZ




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_equal

```python
def length_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_greater_equal

```python
def length_greater_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_greater_than

```python
def length_greater_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_equal

```python
def length_less_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_than

```python
def length_less_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_not_equal

```python
def length_not_equal(self, b=None, epsilon=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range

```python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR')
```

 Node MapRange.

Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

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



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

 Node MapRange.

Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

 Node MapRange.

Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

 Node MapRange.

Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True)
```

 Node MapRange.

Node reference [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html)
Developer reference [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)

#### Args:
- from_min: ['Float', 'Vector']
- from_max: ['Float', 'Vector']
- to_min: ['Float', 'Vector']
- to_max: ['Float', 'Vector']
- steps: ['Float', 'Vector']
- clamp (bool): True

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM')
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True
- factor_mode (str): 'UNIFORM' in [UNIFORM, NON_UNIFORM]

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_non_uniform

```python
def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix_uniform

```python
def mix_uniform(self, vector=None, clamp_factor=True)
```

 Node Mix.

Node reference [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html)
Developer reference [ShaderNodeMix](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- vector: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### modulo

```python
def modulo(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul

```python
def mul(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(self, multiplier=None, addend=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- multiplier: Vector
- addend: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply

```python
def multiply(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- multiplier: Vector
- addend: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normalize

```python
def normalize(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### project

```python
def project(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reflect

```python
def reflect(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### refract

```python
def refract(self, vector=None, ior=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector
- ior: Float

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reroute

```python
def reroute(self)
```

 Reroute all output links



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.

:example:

.. code-block:: python

    class Vector(...):
        def __init__(self, ...):
             ...
             self.reset_properties()
             ...
    
         def reset_properties(self):
             super().reset_properties()
             self.separate_ = None      # Created by property self.seperate() with node SeparateXyz






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_axis_angle

```python
def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False)
```

 Node VectorRotate.

Node reference [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
Developer reference [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- axis: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_euler

```python
def rotate_euler(self, center=None, rotation=None, invert=False)
```

 Node VectorRotate.

Node reference [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
Developer reference [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- rotation: Vector
- invert (bool): False

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_x

```python
def rotate_x(self, center=None, angle=None, invert=False)
```

 Node VectorRotate.

Node reference [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
Developer reference [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_y

```python
def rotate_y(self, center=None, angle=None, invert=False)
```

 Node VectorRotate.

Node reference [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
Developer reference [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_z

```python
def rotate_z(self, center=None, angle=None, invert=False)
```

 Node VectorRotate.

Node reference [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
Developer reference [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

#### Args:
- center: Vector
- angle: Float
- invert (bool): False

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale

```python
def scale(self, scale=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- scale: Float

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(self, increment=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- increment: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

:param node: The new node owning the output socket to wrap
:type node: Node
:return: self

Methods are implemented in two modes:

- Creation
- Transformation

In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.

In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method returns, the calling DataSocket instance refers to a new Blender output socket.
The stack method changes the socket the instance refers to and reinitialize properties

.. code-block:: python

    # 1. Creation mode
    # 
    # to_mesh method creates a new mesh from a curve.
    # The curve instance refers to the same output node socket
    # We need to get the result of the method in a new variable
    
    new_mesh = curve.to_mesh(profile_curve=circle)
    
    # 2. Transformation mode
    #
    # set_shade_smooth method transforms the mesh.
    # After the call, the mesh instance refers to the output socket of the
    # newly created node "Set Shade Smooth". There is no need to get the result
    # of the method.
    
    mesh.set_shade_smooth()
    
    # Note that a transformation method returns self and so, the following line
    # is equivallent:
    
    mesh = mesh.set_shade_smooth()





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sub

```python
def sub(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subtract

```python
def subtract(self, vector=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```

 Node Switch.

Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Vector

#### Returns:
- socket `output`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tan

```python
def tan(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(self)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(self, max=None, min=None)
```

 Node VectorMath.

Node reference [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html)
Developer reference [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- max: Vector
- min: Vector

#### Returns:
- socket `vector`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

