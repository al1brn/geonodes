# Class Integer

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[bl_idname](#bl_idname) | [bnode](#bnode) | [is_multi_input](#is_multi_input) | [is_output](#is_output) | [links](#links) | [name](#name) | [node_chain_label](#node_chain_label) | [socket_index](#socket_index)

**Class and static methods**

[Input](#Input) | [Integer](#Integer) | [Unsigned](#Unsigned) | [get_bl_idname](#get_bl_idname) | [get_class_name](#get_class_name) | [gives_bsocket](#gives_bsocket) | [is_socket](#is_socket) | [is_vector](#is_vector) | [value_data_type](#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [arccos](#arccos) | [arccosine](#arccosine) | [arcsin](#arcsin) | [arcsine](#arcsine) | [arctan](#arctan) | [arctan2](#arctan2) | [arctangent](#arctangent) | [compare](#compare) | [connected_sockets](#connected_sockets) | [cos](#cos) | [cosh](#cosh) | [cosine](#cosine) | [divide](#divide) | [equal](#equal) | [exp](#exp) | [exponent](#exponent) | [fact](#fact) | [fraction](#fraction) | [get_blender_socket](#get_blender_socket) | [greater_equal](#greater_equal) | [greater_than](#greater_than) | [init_domains](#init_domains) | [init_socket](#init_socket) | [inverse_sqrt](#inverse_sqrt) | [less_equal](#less_equal) | [less_than](#less_than) | [log](#log) | [logarithm](#logarithm) | [math_ceil](#math_ceil) | [math_compare](#math_compare) | [math_floor](#math_floor) | [math_greater_than](#math_greater_than) | [math_less_than](#math_less_than) | [math_round](#math_round) | [math_trunc](#math_trunc) | [math_truncate](#math_truncate) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [modulo](#modulo) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [not_equal](#not_equal) | [ping_pong](#ping_pong) | [plug](#plug) | [pow](#pow) | [power](#power) | [reroute](#reroute) | [reset_properties](#reset_properties) | [sign](#sign) | [sin](#sin) | [sine](#sine) | [sinh](#sinh) | [smooth_maximum](#smooth_maximum) | [smooth_minimum](#smooth_minimum) | [snap](#snap) | [sqrt](#sqrt) | [stack](#stack) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [tanh](#tanh) | [to_degrees](#to_degrees) | [to_output](#to_output) | [to_radians](#to_radians) | [to_string](#to_string) | [view](#view) | [wrap](#wrap)

## Properties

### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### bnode

 Shortcut for `self.bsocket.node`



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### links

 Shortcut for `self.bsocket.links`



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### socket_index

#### Returns:

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




## Class and static methods

### Input

```python
@classmethod
def Input(cls, value = 0, name = "Integer", min_value = None, max_value = None, description = "")
```

 Create an Integer input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
#### Returns:
- Integer: The Integer data socket




### Integer

```python
@classmethod
def Integer(cls, integer=0)
```

 Node Integer.

Node reference [Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/integer.html)
Developer reference [FunctionNodeInputInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)

#### Args:
- integer (int): 0

#### Returns:
- socket `integer`



### Unsigned

```python
@classmethod
def Unsigned(cls, value = 0, name = "Unsigned", min_value = 0, max_value = None, description = "")
```

 Create an Unisgned Integer input socket in the Group Input Node

#### Args:
- value: The default value
- name: The socket name
- min_value: Minimum value
- max_value: Maximum value
- description: User tip
    
#### Returns:
- Integer: The Integer data socket



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





## Methods

### abs

```python
def abs(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### absolute

```python
def absolute(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### add

```python
def add(self, value=None, node_label = None, node_color = None)
```

 Add two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
#### Returns:
- Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




### arccos

```python
def arccos(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arccosine

```python
def arccosine(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arcsin

```python
def arcsin(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arcsine

```python
def arcsine(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arctan

```python
def arctan(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arctan2

```python
def arctan2(self, value1=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`



### arctangent

```python
def arctangent(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### compare

```python
def compare(self, b=None, operation='GREATER_THAN')
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`



### connected_sockets

```python
def connected_sockets(self)
```

#### Returns:




### cos

```python
def cos(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### cosh

```python
def cosh(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### cosine

```python
def cosine(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### divide

```python
def divide(self, value=None, node_label = None, node_color = None)
```

 Divide two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
#### Returns:
- Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




### equal

```python
def equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### exp

```python
def exp(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### exponent

```python
def exponent(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### fact

```python
def fact(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### fraction

```python
def fraction(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### get_blender_socket

```python
def get_blender_socket(self)
```

#### Returns:

:return: self.bsocket
:rtype: bpy.types.NodeSocket




### greater_equal

```python
def greater_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### greater_than

```python
def greater_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



### inverse_sqrt

```python
def inverse_sqrt(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### less_equal

```python
def less_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### less_than

```python
def less_than(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### log

```python
def log(self, base=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`



### logarithm

```python
def logarithm(self, base=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`



### math_ceil

```python
def math_ceil(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

#### Returns:
- socket `value`



### math_floor

```python
def math_floor(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`



### math_less_than

```python
def math_less_than(self, threshold=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`



### math_round

```python
def math_round(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### math_trunc

```python
def math_trunc(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### math_truncate

```python
def math_truncate(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### max

```python
def max(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### maximum

```python
def maximum(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### min

```python
def min(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### minimum

```python
def minimum(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### modulo

```python
def modulo(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`



### multiply

```python
def multiply(self, value=None, node_label = None, node_color = None)
```

 Multiply two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
#### Returns:
- Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`



### not_equal

```python
def not_equal(self, b=None)
```

 Node Compare.

Node reference [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html)
Developer reference [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`



### ping_pong

```python
def ping_pong(self, scale=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- scale: Float
- clamp (bool): False

#### Returns:
- socket `value`



### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



### pow

```python
def pow(self, exponent=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`



### power

```python
def power(self, exponent=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`



### reroute

```python
def reroute(self)
```

 Reroute all output links



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






### sign

```python
def sign(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### sin

```python
def sin(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### sine

```python
def sine(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### sinh

```python
def sinh(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`



### smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`



### snap

```python
def snap(self, increment=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- increment: Float
- clamp (bool): False

#### Returns:
- socket `value`



### sqrt

```python
def sqrt(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



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





### subtract

```python
def subtract(self, value=None, node_label = None, node_color = None)
```

 Subtract two values.

#### Args:
- value: Float
- node_label (str): Node label
- node_color (color): Node background color
        
#### Returns:
- Float
        
    If value is a Vector or a Color, VectorMath node is used rather than Math.




### switch

```python
def switch(self, switch=None, true=None)
```

 Node Switch.

Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Integer

#### Returns:
- socket `output`



### tan

```python
def tan(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### tangent

```python
def tangent(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### tanh

```python
def tanh(self, value=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`



### to_degrees

```python
def to_degrees(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




### to_radians

```python
def to_radians(self, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`



### to_string

```python
def to_string(self)
```

 Node ValueToString.

Node reference [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)
Developer reference [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

#### Returns:
- socket `string`



### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



### wrap

```python
def wrap(self, max=None, min=None, clamp=False)
```

 Node Math.

Node reference [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html)
Developer reference [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- max: Float
- min: Float
- clamp (bool): False

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

