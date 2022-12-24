# Class Float

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [color_ramp](#color_ramp) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [is_plugged](#is_plugged) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [socket_index](#socket_index)

**Class and static methods**

[Angle](#Angle) | [Distance](#Distance) | [Factor](#Factor) | [Frame](#Frame) | [Input](#Input) | [Seconds](#Seconds) | [Value](#Value) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [arccos](#arccos) | [arccosine](#arccosine) | [arcsin](#arcsin) | [arcsine](#arcsine) | [arctan](#arctan) | [arctan2](#arctan2) | [arctangent](#arctangent) | [ceiling](#ceiling) | [clamp](#clamp) | [clamp_min_max](#clamp_min_max) | [clamp_range](#clamp_range) | [compare](#compare) | [connected_sockets](#connected_sockets) | [convert_python_type](#convert_python_type) | [cos](#cos) | [cosh](#cosh) | [cosine](#cosine) | [divide](#divide) | [equal](#equal) | [exp](#exp) | [exponent](#exponent) | [fact](#fact) | [float_curve](#float_curve) | [floor](#floor) | [fraction](#fraction) | [get_blender_socket](#get_blender_socket) | [greater_equal](#greater_equal) | [greater_than](#greater_than) | [init_domains](#init_domains) | [init_socket](#init_socket) | [inverse_sqrt](#inverse_sqrt) | [less_equal](#less_equal) | [less_than](#less_than) | [log](#log) | [logarithm](#logarithm) | [map_range](#map_range) | [map_range_linear](#map_range_linear) | [map_range_smooth](#map_range_smooth) | [map_range_smoother](#map_range_smoother) | [map_range_stepped](#map_range_stepped) | [math_ceil](#math_ceil) | [math_compare](#math_compare) | [math_floor](#math_floor) | [math_greater_than](#math_greater_than) | [math_less_than](#math_less_than) | [math_round](#math_round) | [math_trunc](#math_trunc) | [math_truncate](#math_truncate) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [mix](#mix) | [modulo](#modulo) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [not_equal](#not_equal) | [ping_pong](#ping_pong) | [plug](#plug) | [pow](#pow) | [power](#power) | [reroute](#reroute) | [reset_properties](#reset_properties) | [round](#round) | [sign](#sign) | [sin](#sin) | [sine](#sine) | [sinh](#sinh) | [smooth_maximum](#smooth_maximum) | [smooth_minimum](#smooth_minimum) | [snap](#snap) | [sqrt](#sqrt) | [stack](#stack) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [tanh](#tanh) | [to_degrees](#to_degrees) | [to_integer](#to_integer) | [to_output](#to_output) | [to_radians](#to_radians) | [to_string](#to_string) | [truncate](#truncate) | [wrap](#wrap)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`

Returns:
    socket bl_idname (str)



### bnode

 Shortcut for `self.bsocket.node`

Returns:
    Blender node (bpy.types.Node)



### color_ramp



## color_ramp <sub>*property*</sub>

```python
def color_ramp(self):

```
> Node: [ColorRamp](ShaderNodeValToRGB.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

#### Returns:
- node with sockets ['color', 'alpha']






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



### socket_index

 Return the index of the socket within the list of node sockets.

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.

Returns:
    socket index (int)




## Class and static methods

### Angle

```python
@classmethod
def Angle(cls, value=0., name="Angle", min_value = None, max_value = None, description ="")
```

 Create an Angle input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
Returns:
    Float: The Float data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Distance

```python
@classmethod
def Distance(cls, value=0., name="Distance", min_value = None, max_value = None, description ="")
```

 Create a Distance input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
Returns:
    Float: The Float data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Factor

```python
@classmethod
def Factor(cls, value=0., name="Factor", min_value = 0., max_value = 1., description ="")
```

 Create a Factor input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
Returns:
    Float: The Float data socket




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Frame

```python
@classmethod
def Frame(cls)
```



## Frame <sub>*classmethod*</sub>

```python
def Frame(cls):

```
> Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

#### Returns:
- socket `frame`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, value = 0., name = "Float", min_value = None, max_value = None, description ="")
```

 Create a Float input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
Returns:
    Float: The Float data socket



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Seconds

```python
@classmethod
def Seconds(cls)
```



## Seconds <sub>*classmethod*</sub>

```python
def Seconds(cls):

```
> Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

#### Returns:
- socket `seconds`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Value

```python
@classmethod
def Value(cls)
```



## Value <sub>*classmethod*</sub>

```python
def Value(cls):

```
> Node: [Value](ShaderNodeValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)

#### Returns:
- socket `value`






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
def abs(self, clamp=False)
```



## abs

```python
def abs(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self, clamp=False)
```



## absolute

```python
def absolute(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### add

```python
def add(self, value=None, node_label = None, node_color = None)
```

 Add two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
    Returns:
        Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccos

```python
def arccos(self, value=None, clamp=False)
```



## arccos

```python
def arccos(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccosine

```python
def arccosine(self, value=None, clamp=False)
```



## arccosine

```python
def arccosine(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsin

```python
def arcsin(self, value=None, clamp=False)
```



## arcsin

```python
def arcsin(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsine

```python
def arcsine(self, value=None, clamp=False)
```



## arcsine

```python
def arcsine(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan

```python
def arctan(self, value=None, clamp=False)
```



## arctan

```python
def arctan(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan2

```python
def arctan2(self, value1=None, clamp=False)
```



## arctan2

```python
def arctan2(self, value1=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctangent

```python
def arctangent(self, value=None, clamp=False)
```



## arctangent

```python
def arctangent(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ceiling

```python
def ceiling(self)
```



## ceiling

```python
def ceiling(self):

```
> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp

```python
def clamp(self, min=None, max=None, clamp_type='MINMAX')
```



## clamp

```python
def clamp(self, min=None, max=None, clamp_type='MINMAX'):

```
> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_min_max

```python
def clamp_min_max(self, min=None, max=None)
```



## clamp_min_max

```python
def clamp_min_max(self, min=None, max=None):

```
> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_range

```python
def clamp_range(self, min=None, max=None)
```



## clamp_range

```python
def clamp_range(self, min=None, max=None):

```
> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN')
```



## compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN'):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
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
def cos(self, value=None, clamp=False)
```



## cos

```python
def cos(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosh

```python
def cosh(self, value=None, clamp=False)
```



## cosh

```python
def cosh(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(self, value=None, clamp=False)
```



## cosine

```python
def cosine(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### divide

```python
def divide(self, value=None, node_label = None, node_color = None)
```

 Divide two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
    Returns:
        Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### equal

```python
def equal(self, b=None, epsilon=None)
```



## equal

```python
def equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exp

```python
def exp(self, clamp=False)
```



## exp

```python
def exp(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exponent

```python
def exponent(self, clamp=False)
```



## exponent

```python
def exponent(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fact

```python
def fact(self, clamp=False)
```



## fact

```python
def fact(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### float_curve

```python
def float_curve(self, factor=None)
```



## float_curve

```python
def float_curve(self, factor=None):

```
> Node: [Float Curve](ShaderNodeFloatCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)

#### Args:
- factor: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### floor

```python
def floor(self)
```



## floor

```python
def floor(self):

```
> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self, clamp=False)
```



## fraction

```python
def fraction(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_blender_socket

```python
def get_blender_socket(self)
```

 Returns the property bsocket.

Returns:
    bsocket (bpy.types.NodeSocket)




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_equal

```python
def greater_equal(self, b=None)
```



## greater_equal

```python
def greater_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_than

```python
def greater_than(self, b=None)
```



## greater_than

```python
def greater_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






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

### inverse_sqrt

```python
def inverse_sqrt(self, clamp=False)
```



## inverse_sqrt

```python
def inverse_sqrt(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_equal

```python
def less_equal(self, b=None)
```



## less_equal

```python
def less_equal(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_than

```python
def less_than(self, b=None)
```



## less_than

```python
def less_than(self, b=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### log

```python
def log(self, base=None, clamp=False)
```



## log

```python
def log(self, base=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### logarithm

```python
def logarithm(self, base=None, clamp=False)
```



## logarithm

```python
def logarithm(self, base=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






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
- socket `result`






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
- socket `result`






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
- socket `result`






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
- socket `result`






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
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_ceil

```python
def math_ceil(self, clamp=False)
```



## math_ceil

```python
def math_ceil(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False)
```



## math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_floor

```python
def math_floor(self, clamp=False)
```



## math_floor

```python
def math_floor(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False)
```



## math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_less_than

```python
def math_less_than(self, threshold=None, clamp=False)
```



## math_less_than

```python
def math_less_than(self, threshold=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_round

```python
def math_round(self, clamp=False)
```



## math_round

```python
def math_round(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_trunc

```python
def math_trunc(self, clamp=False)
```



## math_trunc

```python
def math_trunc(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_truncate

```python
def math_truncate(self, clamp=False)
```



## math_truncate

```python
def math_truncate(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(self, value=None, clamp=False)
```



## max

```python
def max(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(self, value=None, clamp=False)
```



## maximum

```python
def maximum(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(self, value=None, clamp=False)
```



## min

```python
def min(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(self, value=None, clamp=False)
```



## minimum

```python
def minimum(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, value=None, clamp_factor=True)
```



## mix

```python
def mix(self, factor=None, value=None, clamp_factor=True):

```
> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- value: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### modulo

```python
def modulo(self, value=None, clamp=False)
```



## modulo

```python
def modulo(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False)
```



## mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply

```python
def multiply(self, value=None, node_label = None, node_color = None)
```

 Multiply two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
    Returns:
        Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False)
```



## multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### not_equal

```python
def not_equal(self, b=None, epsilon=None)
```



## not_equal

```python
def not_equal(self, b=None, epsilon=None):

```
> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ping_pong

```python
def ping_pong(self, scale=None, clamp=False)
```



## ping_pong

```python
def ping_pong(self, scale=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- scale: Float
- clamp (bool): False

#### Returns:
- socket `value`






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

### pow

```python
def pow(self, exponent=None, clamp=False)
```



## pow

```python
def pow(self, exponent=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### power

```python
def power(self, exponent=None, clamp=False)
```



## power

```python
def power(self, exponent=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`






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

### round

```python
def round(self)
```



## round

```python
def round(self):

```
> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sign

```python
def sign(self, clamp=False)
```



## sign

```python
def sign(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(self, value=None, clamp=False)
```



## sin

```python
def sin(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(self, value=None, clamp=False)
```



## sine

```python
def sine(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sinh

```python
def sinh(self, value=None, clamp=False)
```



## sinh

```python
def sinh(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False)
```



## smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False)
```



## smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(self, increment=None, clamp=False)
```



## snap

```python
def snap(self, increment=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- increment: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sqrt

```python
def sqrt(self, clamp=False)
```



## sqrt

```python
def sqrt(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






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

### subtract

```python
def subtract(self, value=None, node_label = None, node_color = None)
```

 Subtract two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
    Returns:
        Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




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
- true: Float

#### Returns:
- socket `output`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tan

```python
def tan(self, value=None, clamp=False)
```



## tan

```python
def tan(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(self, value=None, clamp=False)
```



## tangent

```python
def tangent(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tanh

```python
def tanh(self, value=None, clamp=False)
```



## tanh

```python
def tanh(self, value=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_degrees

```python
def to_degrees(self, clamp=False)
```



## to_degrees

```python
def to_degrees(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_integer

```python
def to_integer(self, rounding_mode='ROUND')
```



## to_integer

```python
def to_integer(self, rounding_mode='ROUND'):

```
> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Args:
- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

#### Returns:
- socket `integer`






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

### to_radians

```python
def to_radians(self, clamp=False)
```



## to_radians

```python
def to_radians(self, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_string

```python
def to_string(self, decimals=None)
```



## to_string

```python
def to_string(self, decimals=None):

```
> Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

#### Args:
- decimals: Integer

#### Returns:
- socket `string`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### truncate

```python
def truncate(self)
```



## truncate

```python
def truncate(self):

```
> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(self, max=None, min=None, clamp=False)
```



## wrap

```python
def wrap(self, max=None, min=None, clamp=False):

```
> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- max: Float
- min: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

