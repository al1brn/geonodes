# Class Float

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 Float DataSocket





### Constructor

```python
Float(self, value=0., label=None)
```

## Content

**Properties**

[color_ramp](#color_ramp)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Angle](#Angle) | [Distance](#Distance) | [Factor](#Factor) | [Frame](#Frame) | [Input](#Input) | [Random](#Random) | [Seconds](#Seconds) | [Value](#Value)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[abs](#abs) | [absolute](#absolute) | [add](#add) | [arccos](#arccos) | [arccosine](#arccosine) | [arcsin](#arcsin) | [arcsine](#arcsine) | [arctan](#arctan) | [arctan2](#arctan2) | [arctangent](#arctangent) | [ceiling](#ceiling) | [clamp](#clamp) | [clamp_min_max](#clamp_min_max) | [clamp_range](#clamp_range) | [compare](#compare) | [cos](#cos) | [cosh](#cosh) | [cosine](#cosine) | [divide](#divide) | [equal](#equal) | [exp](#exp) | [exponent](#exponent) | [fact](#fact) | [float_curve](#float_curve) | [floor](#floor) | [fraction](#fraction) | [greater_equal](#greater_equal) | [greater_than](#greater_than) | [inverse_sqrt](#inverse_sqrt) | [less_equal](#less_equal) | [less_than](#less_than) | [log](#log) | [logarithm](#logarithm) | [map_range](#map_range) | [map_range_linear](#map_range_linear) | [map_range_smooth](#map_range_smooth) | [map_range_smoother](#map_range_smoother) | [map_range_stepped](#map_range_stepped) | [math_ceil](#math_ceil) | [math_compare](#math_compare) | [math_floor](#math_floor) | [math_greater_than](#math_greater_than) | [math_less_than](#math_less_than) | [math_round](#math_round) | [math_trunc](#math_trunc) | [math_truncate](#math_truncate) | [max](#max) | [maximum](#maximum) | [min](#min) | [minimum](#minimum) | [mix](#mix) | [modulo](#modulo) | [mul_add](#mul_add) | [multiply](#multiply) | [multiply_add](#multiply_add) | [not_equal](#not_equal) | [ping_pong](#ping_pong) | [pow](#pow) | [power](#power) | [round](#round) | [sign](#sign) | [sin](#sin) | [sine](#sine) | [sinh](#sinh) | [smooth_maximum](#smooth_maximum) | [smooth_minimum](#smooth_minimum) | [snap](#snap) | [sqrt](#sqrt) | [subtract](#subtract) | [switch](#switch) | [tan](#tan) | [tangent](#tangent) | [tanh](#tanh) | [to_degrees](#to_degrees) | [to_integer](#to_integer) | [to_radians](#to_radians) | [to_string](#to_string) | [truncate](#truncate) | [wrap](#wrap)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### color_ramp



> Node: [ColorRamp](ShaderNodeValToRGB.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/color_ramp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)

#### Returns:
- node with sockets ['color', 'alpha']






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
#### Returns:
- Float: The Float data socket




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
#### Returns:
- Float: The Float data socket




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
#### Returns:
- Float: The Float data socket




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Frame

```python
@classmethod
def Frame(cls)
```



> Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

#### Returns:
- socket `frame`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
#### Returns:
- Float: The Float data socket



<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Seconds

```python
@classmethod
def Seconds(cls)
```



> Node: [Scene Time](GeometryNodeInputSceneTime.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)

#### Returns:
- socket `seconds`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Value

```python
@classmethod
def Value(cls)
```



> Node: [Value](ShaderNodeValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### absolute

```python
def absolute(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### ceiling

```python
def ceiling(self)
```



> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp

```python
def clamp(self, min=None, max=None, clamp_type='MINMAX')
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float
- clamp_type (str): 'MINMAX' in [MINMAX, RANGE]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_min_max

```python
def clamp_min_max(self, min=None, max=None)
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### clamp_range

```python
def clamp_range(self, min=None, max=None)
```



> Node: [Clamp](ShaderNodeClamp.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/clamp.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)

#### Args:
- min: Float
- max: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### compare

```python
def compare(self, b=None, epsilon=None, operation='GREATER_THAN')
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float
- operation (str): 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### equal

```python
def equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exp

```python
def exp(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### exponent

```python
def exponent(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fact

```python
def fact(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### float_curve

```python
def float_curve(self, factor=None)
```



> Node: [Float Curve](ShaderNodeFloatCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)

#### Args:
- factor: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### floor

```python
def floor(self)
```



> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### fraction

```python
def fraction(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_equal

```python
def greater_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### greater_than

```python
def greater_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### inverse_sqrt

```python
def inverse_sqrt(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_equal

```python
def less_equal(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### less_than

```python
def less_than(self, b=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_ceil

```python
def math_ceil(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_floor

```python
def math_floor(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_round

```python
def math_round(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_trunc

```python
def math_trunc(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### math_truncate

```python
def math_truncate(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mix

```python
def mix(self, factor=None, value=None, clamp_factor=True)
```



> Node: [Mix](ShaderNodeMix.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)

#### Args:
- factor: ['Float', 'Vector']
- value: ['Float', 'Vector', 'Color']
- clamp_factor (bool): True

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### not_equal

```python
def not_equal(self, b=None, epsilon=None)
```



> Node: [Compare](FunctionNodeCompare.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)

#### Args:
- b: ['Float', 'Integer', 'Vector', 'Color', 'String']
- epsilon: Float

#### Returns:
- socket `result`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### round

```python
def round(self)
```



> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sign

```python
def sign(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sqrt

```python
def sqrt(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Float

#### Returns:
- socket `output`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_degrees

```python
def to_degrees(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_integer

```python
def to_integer(self, rounding_mode='ROUND')
```



> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Args:
- rounding_mode (str): 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_radians

```python
def to_radians(self, clamp=False)
```



> Node: [Math](ShaderNodeMath.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) | [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)

#### Args:
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_string

```python
def to_string(self, decimals=None)
```



> Node: [Value to String](FunctionNodeValueToString.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)

#### Args:
- decimals: Integer

#### Returns:
- socket `string`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### truncate

```python
def truncate(self)
```



> Node: [Float to Integer](FunctionNodeFloatToInt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/float_to_integer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)

#### Returns:
- socket `integer`






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Float) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

