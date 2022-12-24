# Class Integer

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Integer DataSocket




### Constructor

```python
Integer(self, value=0, label=None)
```

## Content

**Properties**

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Input](#Input) | [Integer](#Integer) | [Random](#Random) | [Unsigned](#Unsigned)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [arccos](#arccos) | [arccosine](#arccosine) | [arcsin](#arcsin) | [arcsine](#arcsine) | [arctan](#arctan) | [arctan2](#arctan2) | [arctangent](#arctangent) | [compare](#compare) | [cos](#cos) | [cosh](#cosh) | [cosine](#cosine) | [divide](#divide) | [equal](#equal) | [exp](#exp) | [exponent](#exponent) | [fact](#fact) | [fraction](#fraction) | [greater_equal](#greater_equal) | [greater_than](#greater_than) | [inverse_sqrt](#inverse_sqrt) | [less_equal](#less_equal) | [less_than](#less_than) | [log](#log) | [logarithm](#logarithm) | [math_ceil](#math_ceil) | [math_compare](#math_compare) | [math_floor](#math_floor) | [math_greater_than](#math_greater_than) | [math_less_than](#math_less_than) | [math_round](#math_round) | [math_trunc](#math_trunc) | [math_truncate](#math_truncate) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [modulo](#modulo) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [not_equal](#not_equal) | [ping_pong](#ping_pong) | [pow](#pow) | [power](#power) | [sign](#sign) | [sin](#sin) | [sine](#sine) | [sinh](#sinh) | [smooth_maximum](#smooth_maximum) | [smooth_minimum](#smooth_minimum) | [snap](#snap) | [sqrt](#sqrt) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [tanh](#tanh) | [to_degrees](#to_degrees) | [to_radians](#to_radians) | [to_string](#to_string) | [wrap](#wrap)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

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




<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Integer

```python
@classmethod
def Integer(cls, integer=0)
```



> Node: [Integer](FunctionNodeInputInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)

#### Args:
- integer (int): 0

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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



<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### abs

```python
def abs(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccos

```python
def arccos(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arccosine

```python
def arccosine(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsin

```python
def arcsin(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arcsine

```python
def arcsine(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan

```python
def arctan(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctan2

```python
def arctan2(self, value1=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value1: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### arctangent

```python
def arctangent(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, operation='GREATER_THAN')
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cos

```python
def cos(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosh

```python
def cosh(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### cosine

```python
def cosine(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### equal

```python
def equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exp

```python
def exp(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exponent

```python
def exponent(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fact

```python
def fact(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_equal

```python
def greater_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_than

```python
def greater_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### inverse_sqrt

```python
def inverse_sqrt(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_equal

```python
def less_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_than

```python
def less_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### log

```python
def log(self, base=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### logarithm

```python
def logarithm(self, base=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- base: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_ceil

```python
def math_ceil(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_compare

```python
def math_compare(self, value=None, epsilon=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- epsilon: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_floor

```python
def math_floor(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_greater_than

```python
def math_greater_than(self, threshold=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_less_than

```python
def math_less_than(self, threshold=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- threshold: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_round

```python
def math_round(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_trunc

```python
def math_trunc(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_truncate

```python
def math_truncate(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### max

```python
def max(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### maximum

```python
def maximum(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### min

```python
def min(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### minimum

```python
def minimum(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### modulo

```python
def modulo(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mul_add

```python
def mul_add(self, multiplier=None, addend=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### multiply_add

```python
def multiply_add(self, multiplier=None, addend=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- multiplier: Float
- addend: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### not_equal

```python
def not_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ping_pong

```python
def ping_pong(self, scale=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- scale: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### pow

```python
def pow(self, exponent=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### power

```python
def power(self, exponent=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- exponent: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sign

```python
def sign(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sin

```python
def sin(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sine

```python
def sine(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sinh

```python
def sinh(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_maximum

```python
def smooth_maximum(self, value=None, distance=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### smooth_minimum

```python
def smooth_minimum(self, value=None, distance=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- distance: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### snap

```python
def snap(self, increment=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- increment: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sqrt

```python
def sqrt(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Integer

#### Returns:
- socket `output`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tan

```python
def tan(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent

```python
def tangent(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tanh

```python
def tanh(self, value=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- value: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_degrees

```python
def to_degrees(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_radians

```python
def to_radians(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_string

```python
def to_string(self)
```



> Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

#### Returns:
- socket `string`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### wrap

```python
def wrap(self, max=None, min=None, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- max: Float
- min: Float
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Integer) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

