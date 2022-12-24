# Class Vector

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [is_plugged](#is_plugged) | [length](#length) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [separate](#separate) | [socket_index](#socket_index)

**Class and static methods**

[Combine](#Combine) | [Input](#Input) | [Rotation](#Rotation) | [Translation](#Translation) | [Vector](#Vector) | [VectorXYZ](#VectorXYZ) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [align_euler_to_vector](#align_euler_to_vector) | [average_equal](#average_equal) | [average_greater_equal](#average_greater_equal) | [average_greater_than](#average_greater_than) | [average_less_equal](#average_less_equal) | [average_less_than](#average_less_than) | [average_not_equal](#average_not_equal) | [ceil](#ceil) | [compare](#compare) | [connected_sockets](#connected_sockets) | [convert_python_type](#convert_python_type) | [cos](#cos) | [cosine](#cosine) | [cross](#cross) | [cross_product](#cross_product) | [curves](#curves) | [direction_equal](#direction_equal) | [direction_greater_equal](#direction_greater_equal) | [direction_greater_than](#direction_greater_than) | [direction_less_equal](#direction_less_equal) | [direction_less_than](#direction_less_than) | [direction_not_equal](#direction_not_equal) | [distance](#distance) | [div](#div) | [divide](#divide) | [dot](#dot) | [dot_product](#dot_product) | [dot_product_equal](#dot_product_equal) | [dot_product_greater_equal](#dot_product_greater_equal) | [dot_product_greater_than](#dot_product_greater_than) | [dot_product_less_equal](#dot_product_less_equal) | [dot_product_less_than](#dot_product_less_than) | [dot_product_not_equal](#dot_product_not_equal) | [elements_equal](#elements_equal) | [elements_greater_equal](#elements_greater_equal) | [elements_greater_than](#elements_greater_than) | [elements_less_equal](#elements_less_equal) | [elements_less_than](#elements_less_than) | [elements_not_equal](#elements_not_equal) | [face_forward](#face_forward) | [floor](#floor) | [fract](#fract) | [fraction](#fraction) | [get_blender_socket](#get_blender_socket) | [init_domains](#init_domains) | [init_socket](#init_socket) | [length_equal](#length_equal) | [length_greater_equal](#length_greater_equal) | [length_greater_than](#length_greater_than) | [length_less_equal](#length_less_equal) | [length_less_than](#length_less_than) | [length_not_equal](#length_not_equal) | [map_range](#map_range) | [map_range_linear](#map_range_linear) | [map_range_smooth](#map_range_smooth) | [map_range_smoother](#map_range_smoother) | [map_range_stepped](#map_range_stepped) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [mix](#mix) | [mix_non_uniform](#mix_non_uniform) | [mix_uniform](#mix_uniform) | [modulo](#modulo) | [mul](#mul) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [normalize](#normalize) | [plug](#plug) | [project](#project) | [reflect](#reflect) | [refract](#refract) | [reroute](#reroute) | [reset_properties](#reset_properties) | [rotate_axis_angle](#rotate_axis_angle) | [rotate_euler](#rotate_euler) | [rotate_x](#rotate_x) | [rotate_y](#rotate_y) | [rotate_z](#rotate_z) | [scale](#scale) | [sin](#sin) | [sine](#sine) | [snap](#snap) | [stack](#stack) | [sub](#sub) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [to_output](#to_output) | [wrap](#wrap)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`

Returns:
    socket bl_idname (str)



### bnode

 Shortcut for `self.bsocket.node`

Returns:
    Blender node (bpy.types.Node)



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`

Returns:
    is multi input socket (bool)



### is_output

 Shortcut for `self.bsocket.is_output`

Returns:
    is an aoutput socket (bool)



### is_plugged

 Indicates if the socket is connected or not.

Raise an exception if called on an output socket.

Returns:
    is plugged (bool)



### length



## length <sub>*property*</sub>

```python
def length(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `value`






### links

 Shortcut for `self.bsocket.links`      

Returns:
    list of links (list)



### name

 Shortcut for `self.bsocket.name`

Returns:
    socket name (str)



### node_chain_label

 Shortcut for *self.node.chain_label*



### separate



## separate <sub>*property*</sub>

```python
def separate(self):

```
> Node: [Separate XYZ](ShaderNodeSeparateXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)

#### Returns:
- node with sockets ['x', 'y', 'z']






### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.

Returns:
    socket index (int)




## Class and static methods

### Combine

```python
@classmethod
def Combine(cls, x=None, y=None, z=None)
```



## Combine <sub>*classmethod*</sub>

```python
def Combine(cls, x=None, y=None, z=None):

```
> Node: [Combine XYZ](ShaderNodeCombineXYZ.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)

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
    
Returns:
    Vector: The Vector data socket




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
    
Returns:
    Vector: The Vector data socket



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
    
Returns:
    Vector: The Vector data socket



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Vector

```python
@classmethod
def Vector(cls, vector=[0.0, 0.0, 0.0])
```



## Vector <sub>*classmethod*</sub>

```python
def Vector(cls, vector=[0.0, 0.0, 0.0]):

```
> Node: [Vector](FunctionNodeInputVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)

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
    
Returns:
    Vector: The Vector data socket



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to **sub classes**:
    
| Sub class                 | bl_idname                     |
|---------------------------|-------------------------------|
| Unsigned                  | NodeSocketIntUnsigned         |
| Factor                    | NodeSocketFloatFactor         |
| Angle                     | NodeSocketFloatAngle          |
| Distance                  | NodeSocketFloatDistance       |
| Rotation                  | NodeSocketVectorEuler         |
| xyz                       | NodeSocketVectorXYZ           |
| Translation               | NodeSocketVectorTranslation   |
  
These additional values allow to enter angle, distance, factor... as group input values.

#### Args:
- class_name (str): the name of the class
    
Returns:
    bl_idname (str)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

| Socket bl_idname              | Geondes class name    | Sub class             |
l-------------------------------|-----------------------|-----------------------|
| NodeSocketBool                | Boolean               | None                  |
| NodeSocketInt                 | Integer               | None                  |
| NodeSocketIntUnsigned         | Integer               | NoUnsigned            |
| NodeSocketFloat               | Float                 | None                  |
| NodeSocketFloatFactor         | Float                 | Factor                |
| NodeSocketFloatAngle          | Float                 | Angle                 |
| NodeSocketFloatDistance       | Float                 | Distance              |
| NodeSocketVector              | Vector                | None                  |
| NodeSocketVectorEuler         | Vector                | Rotation              |
| NodeSocketVectorXYZ           | Vector                | xyz                   |
| NodeSocketVectorTranslation   | Vector                | Translation           |
| NodeSocketColor               | Color                 | None                  |
| NodeSocketString              | String                | None                  |
| NodeSocketCollection          | Collection            | None                  |
| NodeSocketImage               | Image                 | None                  |
| NodeSocketMaterial            | Material              | None                  |
| NodeSocketObject              | Object                | None                  |
| NodeSocketTexture             | Texture               | None                  |
| NodeSocketGeometry            | Geometry              | None                  |

If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.

#### Args:
- socket (bpy.type.NodeSocket): the socket to use
- with_sub_class (bool): return as as second value the sub type of the socket
        



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

#### Args:
- value (any): The value to test
    
Returns:
    value is bpy.types.NodeSocket or Socket (bool)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

#### Args:
- value (any): The value to test
    
Returns:
    is a socket (bool)



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

#### Args:
- value (any): The value to test
    
Returns:
    is a socket (bool)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color='FLOAT_COLOR')
```

 Returns the data type to which the socket belongs.

This methods is used to compute the **data_type** value in nodes accepting multitype values.

|    Socket                     |    data_type    |
|-------------------------------|-----------------|
| NodeSocketBool                | 'BOOLEAN'       |
| NodeSocketInt                 | 'INT'           |
| NodeSocketIntUnsigned         | 'INT'           |
| NodeSocketFloat               | 'FLOAT'         |
| NodeSocketFloatFactor         | 'FLOAT'         |
| NodeSocketFloatAngle          | 'FLOAT'         |
| NodeSocketFloatDistance       | 'FLOAT'         |
| NodeSocketVector              | 'FLOAT_VECTOR'  |
| NodeSocketVectorEuler         | 'FLOAT_VECTOR'  |
| NodeSocketVectorXYZ           | 'FLOAT_VECTOR'  |
| NodeSocketVectorTranslation   | 'FLOAT_VECTOR'  |
| NodeSocketColor               | color           |                

#### Args:
- value (any): the value to analyze
- default (str): default data_type
- color (str): code for color data_type
    
Returns:
    the data type of the value





<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### abs

```python
def abs(self)
```



## abs

```python
def abs(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self)
```



## absolute

```python
def absolute(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### add

```python
def add(self, vector=None)
```



## add

```python
def add(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### align_euler_to_vector

```python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```



## align_euler_to_vector

```python
def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):

```
> Node: [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)

#### Args:
- factor: Float
- vector: Vector
- axis (str): 'X' in [X, Y, Z]
- pivot_axis (str): 'AUTO' in [AUTO, X, Y, Z]

#### Returns:
- self






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_equal

```python
def average_equal(self, b=None, epsilon=None)
```



## average_equal

```python
def average_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## average_greater_equal

```python
def average_greater_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_greater_than

```python
def average_greater_than(self, b=None)
```



## average_greater_than

```python
def average_greater_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_equal

```python
def average_less_equal(self, b=None)
```



## average_less_equal

```python
def average_less_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_less_than

```python
def average_less_than(self, b=None)
```



## average_less_than

```python
def average_less_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### average_not_equal

```python
def average_not_equal(self, b=None, epsilon=None)
```



## average_not_equal

```python
def average_not_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## ceil

```python
def ceil(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN')
```



## compare

```python
def compare(self, b=None, c=None, angle=None, epsilon=None, mode='ELEMENT', operation='GREATER_THAN'):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### connected_sockets

```python
def connected_sockets(self)
```

 Returns the list of Socket instances linked to this socket.

Returns:
    list of connected sockets (list of Sockets)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### convert_python_type

```python
def convert_python_type(self, value, raise_exception=True)
```

 Convert a python value to a value which can be plug in the socket.

The following table gives the conversion rules:
    
| Socket type       | Conversion                                                    |
l-------------------|---------------------------------------------------------------|
| Boolean           | bool(value)                                                   |
| Integer           | int(value)                                                    |
| Float             | float(value)                                                  |
| Vector            | A triplet or the value if compatible (mathutils.Vector,...)   |
| Color             | A quadruplet or the value if compatible (mathutils.Color,...) |
| String            | str(value)                                                    |
| Collection        | value is value is a collection, bpy.data.collections[value] otherwise |
| Object            | value is value is an object, bpy.data.objects[value] otherwise        |
| Image             | value is value is an image, bpy.data.images[value] otherwise          |
| Texture           | value is value is a texture, bpy.data.textures[value] otherwise       |
| Material          | value is value is a material, bpy.data.materials[value] otherwise     |

This method allows in particular to refer to Blender resources by their name:
    
```python
# Set a material to a mesh
mesh.faces.material = "Material"

# Is equivalent to
mesh.faces.material = bpy.data.materials["Material"]
```

#### Args:
- value (any): the value to convert
- raise_exeption (bool): False to avod raising an exception in case of error.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cos

```python
def cos(self)
```



## cos

```python
def cos(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(self)
```



## cosine

```python
def cosine(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross

```python
def cross(self, vector=None)
```



## cross

```python
def cross(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cross_product

```python
def cross_product(self, vector=None)
```



## cross_product

```python
def cross_product(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curves

```python
def curves(self, fac=None)
```



## curves

```python
def curves(self, fac=None):

```
> Node: [Vector Curves](ShaderNodeVectorCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)

#### Args:
- fac: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### direction_equal

```python
def direction_equal(self, b=None, angle=None, epsilon=None)
```



## direction_equal

```python
def direction_equal(self, b=None, angle=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## direction_greater_equal

```python
def direction_greater_equal(self, b=None, angle=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## direction_greater_than

```python
def direction_greater_than(self, b=None, angle=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## direction_less_equal

```python
def direction_less_equal(self, b=None, angle=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## direction_less_than

```python
def direction_less_than(self, b=None, angle=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## direction_not_equal

```python
def direction_not_equal(self, b=None, angle=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## distance

```python
def distance(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### div

```python
def div(self, vector=None)
```



## div

```python
def div(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### divide

```python
def divide(self, vector=None)
```



## divide

```python
def divide(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot

```python
def dot(self, vector=None)
```



## dot

```python
def dot(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product

```python
def dot_product(self, vector=None)
```



## dot_product

```python
def dot_product(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dot_product_equal

```python
def dot_product_equal(self, b=None, c=None, epsilon=None)
```



## dot_product_equal

```python
def dot_product_equal(self, b=None, c=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## dot_product_greater_equal

```python
def dot_product_greater_equal(self, b=None, c=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## dot_product_greater_than

```python
def dot_product_greater_than(self, b=None, c=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## dot_product_less_equal

```python
def dot_product_less_equal(self, b=None, c=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## dot_product_less_than

```python
def dot_product_less_than(self, b=None, c=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## dot_product_not_equal

```python
def dot_product_not_equal(self, b=None, c=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## elements_equal

```python
def elements_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## elements_greater_equal

```python
def elements_greater_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_greater_than

```python
def elements_greater_than(self, b=None)
```



## elements_greater_than

```python
def elements_greater_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_equal

```python
def elements_less_equal(self, b=None)
```



## elements_less_equal

```python
def elements_less_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_less_than

```python
def elements_less_than(self, b=None)
```



## elements_less_than

```python
def elements_less_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### elements_not_equal

```python
def elements_not_equal(self, b=None, epsilon=None)
```



## elements_not_equal

```python
def elements_not_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## face_forward

```python
def face_forward(self, incident=None, reference=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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



## floor

```python
def floor(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fract

```python
def fract(self)
```



## fract

```python
def fract(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self)
```



## fraction

```python
def fraction(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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



## length_equal

```python
def length_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## length_greater_equal

```python
def length_greater_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_greater_than

```python
def length_greater_than(self, b=None)
```



## length_greater_than

```python
def length_greater_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_equal

```python
def length_less_equal(self, b=None)
```



## length_less_equal

```python
def length_less_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_less_than

```python
def length_less_than(self, b=None)
```



## length_less_than

```python
def length_less_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### length_not_equal

```python
def length_not_equal(self, b=None, epsilon=None)
```



## length_not_equal

```python
def length_not_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

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



## map_range

```python
def map_range(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True, interpolation_type='LINEAR'):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



## map_range_linear

```python
def map_range_linear(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



## map_range_smooth

```python
def map_range_smooth(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```



## map_range_smoother

```python
def map_range_smoother(self, from_min=None, from_max=None, to_min=None, to_max=None, clamp=True):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True)
```



## map_range_stepped

```python
def map_range_stepped(self, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True):

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






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(self, vector=None)
```



## max

```python
def max(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(self, vector=None)
```



## maximum

```python
def maximum(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(self, vector=None)
```



## min

```python
def min(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(self, vector=None)
```



## minimum

```python
def minimum(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM')
```



## mix

```python
def mix(self, factor=None, vector=None, clamp_factor=True, factor_mode='UNIFORM'):

```
> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

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



## mix_non_uniform

```python
def mix_non_uniform(self, factor=None, vector=None, clamp_factor=True):

```
> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

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



## mix_uniform

```python
def mix_uniform(self, vector=None, clamp_factor=True):

```
> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

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



## modulo

```python
def modulo(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul

```python
def mul(self, vector=None)
```



## mul

```python
def mul(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(self, multiplier=None, addend=None)
```



## mul_add

```python
def mul_add(self, multiplier=None, addend=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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



## multiply

```python
def multiply(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None)
```



## multiply_add

```python
def multiply_add(self, multiplier=None, addend=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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



## normalize

```python
def normalize(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

#### Args:
- values (any): The output sockets. More than one values can be passed if the input socket is multi input.
    
Returns:
    None



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### project

```python
def project(self, vector=None)
```



## project

```python
def project(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### reflect

```python
def reflect(self, vector=None)
```



## reflect

```python
def reflect(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### refract

```python
def refract(self, vector=None, ior=None)
```



## refract

```python
def refract(self, vector=None, ior=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### rotate_axis_angle

```python
def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False)
```



## rotate_axis_angle

```python
def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):

```
> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

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



## rotate_euler

```python
def rotate_euler(self, center=None, rotation=None, invert=False):

```
> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

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



## rotate_x

```python
def rotate_x(self, center=None, angle=None, invert=False):

```
> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

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



## rotate_y

```python
def rotate_y(self, center=None, angle=None, invert=False):

```
> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

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



## rotate_z

```python
def rotate_z(self, center=None, angle=None, invert=False):

```
> Node: [Vector Rotate](ShaderNodeVectorRotate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)

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



## scale

```python
def scale(self, scale=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- scale: Float

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(self)
```



## sin

```python
def sin(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(self)
```



## sine

```python
def sine(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(self, increment=None)
```



## snap

```python
def snap(self, increment=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

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

After the call, **the DataSocket** instance wraps a different socket, typically in a newly created node.
This is an internally used by the **geonodes** engine.

In the following example, the `mesh`

```python

# After the following instruction, mesh wraps the output socket of the Cube node
mesh = Mesh.Cube()

# After the following instruction, mesh wraps the output socket of the Set Shade Smooth node
mesh.set_shade_smooth(True)
```

    
#### Args:
- node (Node): the new node
- socket_name (str): name of the outpout socket in the node. If None, takes the first output socket of the node.
    
Returns:
    self        




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sub

```python
def sub(self, vector=None)
```



## sub

```python
def sub(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subtract

```python
def subtract(self, vector=None)
```



## subtract

```python
def subtract(self, vector=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- vector: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



## switch

```python
def switch(self, switch=None, true=None):

```
> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

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



## tan

```python
def tan(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(self)
```



## tangent

```python
def tangent(self):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_output

```python
def to_output(self, name=None)
```

 Create a new output socket in the Tree and plug the **DataSocket** to it.

The socket is added to the outputs of the geometry nodes tree.

> Note: To define a data socket as the result geometry of the tree, use the property `output_geometry` of 
  the current [Tree](Tree.md#output_geometry).

The created socket can be read from within another [Tree](Tree.md) by:
    - creating a [Group](Group.md): `node = Group(tree_name, **kwargs)`
    - using the snake_case version of the socket: `ver = node.socket_name`

#### Args:
- name (str): User name of the socket
    
Returns:
    None



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(self, max=None, min=None)
```



## wrap

```python
def wrap(self, max=None, min=None):

```
> Node: [Vector Math](ShaderNodeVectorMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)

#### Args:
- max: Vector
- min: Vector

#### Returns:
- socket `vector`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

