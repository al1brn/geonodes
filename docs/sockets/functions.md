
# Data socket functions

> Inherits from 
  
<sub>go to [index](TBD)</sub>



## Functions

- [abs](#abs) : [Math](section:nodes/Math), value (Float)
- [add](#add) : [Math](section:nodes/Math), value (Float)
- [arccos](#arccos) : [Math](section:nodes/Math), value (Float)
- [arcsin](#arcsin) : [Math](section:nodes/Math), value (Float)
- [arctan](#arctan) : [Math](section:nodes/Math), value (Float)
- [arctan2](#arctan2) : [Math](section:nodes/Math), value (Float)
- [ceil](#ceil) : [Math](section:nodes/Math), value (Float)
- [color_add](#color_add) : [Mix](section:nodes/Mix), color (Color)
- [color_burn](#color_burn) : [Mix](section:nodes/Mix), color (Color)
- [color_darken](#color_darken) : [Mix](section:nodes/Mix), color (Color)
- [color_difference](#color_difference) : [Mix](section:nodes/Mix), color (Color)
- [color_divide](#color_divide) : [Mix](section:nodes/Mix), color (Color)
- [color_dodge](#color_dodge) : [Mix](section:nodes/Mix), color (Color)
- [color_hue](#color_hue) : [Mix](section:nodes/Mix), color (Color)
- [color_lighten](#color_lighten) : [Mix](section:nodes/Mix), color (Color)
- [color_linear_light](#color_linear_light) : [Mix](section:nodes/Mix), color (Color)
- [color_mix](#color_mix) : [Mix](section:nodes/Mix), color (Color)
- [color_mix_color](#color_mix_color) : [Mix](section:nodes/Mix), color (Color)
- [color_multiply](#color_multiply) : [Mix](section:nodes/Mix), color (Color)
- [color_overlay](#color_overlay) : [Mix](section:nodes/Mix), color (Color)
- [color_saturation](#color_saturation) : [Mix](section:nodes/Mix), color (Color)
- [color_screen](#color_screen) : [Mix](section:nodes/Mix), color (Color)
- [color_soft_light](#color_soft_light) : [Mix](section:nodes/Mix), color (Color)
- [color_subtract](#color_subtract) : [Mix](section:nodes/Mix), color (Color)
- [color_value](#color_value) : [Mix](section:nodes/Mix), color (Color)
- [compare](#compare) : [Compare](section:nodes/Compare), result (Boolean)
- [compare](#compare) : [Math](section:nodes/Math), value (Float)
- [cos](#cos) : [Math](section:nodes/Math), value (Float)
- [cosh](#cosh) : [Math](section:nodes/Math), value (Float)
- [cross](#cross) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [degrees](#degrees) : [Math](section:nodes/Math), value (Float)
- [distance](#distance) : [VectorMath](section:nodes/VectorMath), value (Float)
- [divide](#divide) : [Math](section:nodes/Math), value (Float)
- [dot](#dot) : [VectorMath](section:nodes/VectorMath), value (Float)
- [exp](#exp) : [Math](section:nodes/Math), value (Float)
- [faceforward](#faceforward) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [floor](#floor) : [Math](section:nodes/Math), value (Float)
- [fract](#fract) : [Math](section:nodes/Math), value (Float)
- [fraction](#fraction) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [greater_than](#greater_than) : [Math](section:nodes/Math), value (Float)
- [inverse_sqrt](#inverse_sqrt) : [Math](section:nodes/Math), value (Float)
- [join_strings](#join_strings) : [JoinStrings](section:nodes/JoinStrings), string (String)
- [length](#length) : [VectorMath](section:nodes/VectorMath), value (Float)
- [less_than](#less_than) : [Math](section:nodes/Math), value (Float)
- [log](#log) : [Math](section:nodes/Math), value (Float)
- [max](#max) : [Math](section:nodes/Math), value (Float)
- [min](#min) : [Math](section:nodes/Math), value (Float)
- [modulo](#modulo) : [Math](section:nodes/Math), value (Float)
- [multiply](#multiply) : [Math](section:nodes/Math), value (Float)
- [multiply_add](#multiply_add) : [Math](section:nodes/Math), value (Float)
- [normalize](#normalize) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [pingpong](#pingpong) : [Math](section:nodes/Math), value (Float)
- [pow](#pow) : [Math](section:nodes/Math), value (Float)
- [project](#project) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [radians](#radians) : [Math](section:nodes/Math), value (Float)
- [reflect](#reflect) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [refract](#refract) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [round](#round) : [Math](section:nodes/Math), value (Float)
- [scale](#scale) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [scene](#scene) : [SceneTime](section:nodes/SceneTime), Sockets      [seconds (Float), frame (Float)]
- [sign](#sign) : [Math](section:nodes/Math), value (Float)
- [sin](#sin) : [Math](section:nodes/Math), value (Float)
- [sinh](#sinh) : [Math](section:nodes/Math), value (Float)
- [smooth_max](#smooth_max) : [Math](section:nodes/Math), value (Float)
- [smooth_min](#smooth_min) : [Math](section:nodes/Math), value (Float)
- [snap](#snap) : [Math](section:nodes/Math), value (Float)
- [sqrt](#sqrt) : [Math](section:nodes/Math), value (Float)
- [subtract](#subtract) : [Math](section:nodes/Math), value (Float)
- [tan](#tan) : [Math](section:nodes/Math), value (Float)
- [tanh](#tanh) : [Math](section:nodes/Math), value (Float)
- [trunc](#trunc) : [Math](section:nodes/Math), value (Float)
- [vector_absolute](#vector_absolute) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_add](#vector_add) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_ceil](#vector_ceil) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_cos](#vector_cos) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_divide](#vector_divide) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_floor](#vector_floor) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_max](#vector_max) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_min](#vector_min) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_modulo](#vector_modulo) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_multiply](#vector_multiply) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_multiply_add](#vector_multiply_add) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_sin](#vector_sin) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_snap](#vector_snap) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_subtract](#vector_subtract) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_tan](#vector_tan) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [vector_wrap](#vector_wrap) : [VectorMath](section:nodes/VectorMath), vector (Vector)
- [wrap](#wrap) : [Math](section:nodes/Math), value (Float)

## compare

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = functions.compare(a, b, epsilon, data_type, mode, operation)
```

### Arguments


#### Sockets

- a : Float
- b : Float
- epsilon : Float

#### Parameters

- data_type : 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- operation : 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Node creation

```python
nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation)
```

### Returns

Boolean


## join_strings

> Node: [JoinStrings](section:nodes/JoinStrings)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
node ref [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/join_strings.html) </sub>

```python
v = functions.join_strings(strings_1, strings_2, strings_3, delimiter)
```

### Arguments


#### Sockets

- strings : *String
- delimiter : String

### Node creation

```python
nodes.JoinStrings(*strings, delimiter=delimiter)
```

### Returns

String


## scene

> Node: [SceneTime](section:nodes/SceneTime)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
node ref [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/scene_time.html) </sub>

```python
v = functions.scene()
```

### Arguments


### Node creation

```python
nodes.SceneTime()
```

### Returns

Sockets [seconds (Float), frame (Float)]


## add

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.add(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'ADD'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='ADD')
```

### Returns

Float


## subtract

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.subtract(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'SUBTRACT'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='SUBTRACT')
```

### Returns

Float


## multiply

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.multiply(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'MULTIPLY'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='MULTIPLY')
```

### Returns

Float


## divide

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.divide(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'DIVIDE'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='DIVIDE')
```

### Returns

Float


## multiply_add

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.multiply_add(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'MULTIPLY_ADD'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD')
```

### Returns

Float


## pow

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.pow(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'POWER'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='POWER')
```

### Returns

Float


## log

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.log(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'LOGARITHM'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='LOGARITHM')
```

### Returns

Float


## sqrt

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.sqrt(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'SQRT'

### Node creation

```python
nodes.Math(value0=value0, operation='SQRT')
```

### Returns

Float


## inverse_sqrt

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.inverse_sqrt(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'INVERSE_SQRT'

### Node creation

```python
nodes.Math(value0=value0, operation='INVERSE_SQRT')
```

### Returns

Float


## abs

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.abs(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'ABSOLUTE'

### Node creation

```python
nodes.Math(value0=value0, operation='ABSOLUTE')
```

### Returns

Float


## exp

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.exp(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'EXPONENT'

### Node creation

```python
nodes.Math(value0=value0, operation='EXPONENT')
```

### Returns

Float


## min

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.min(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'MINIMUM'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='MINIMUM')
```

### Returns

Float


## max

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.max(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'MAXIMUM'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='MAXIMUM')
```

### Returns

Float


## less_than

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.less_than(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'LESS_THAN'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='LESS_THAN')
```

### Returns

Float


## greater_than

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.greater_than(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'GREATER_THAN'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN')
```

### Returns

Float


## sign

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.sign(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'SIGN'

### Node creation

```python
nodes.Math(value0=value0, operation='SIGN')
```

### Returns

Float


## compare

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.compare(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'COMPARE'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE')
```

### Returns

Float


## smooth_min

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.smooth_min(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'SMOOTH_MIN'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN')
```

### Returns

Float


## smooth_max

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.smooth_max(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'SMOOTH_MAX'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX')
```

### Returns

Float


## round

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.round(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'ROUND'

### Node creation

```python
nodes.Math(value0=value0, operation='ROUND')
```

### Returns

Float


## floor

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.floor(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'FLOOR'

### Node creation

```python
nodes.Math(value0=value0, operation='FLOOR')
```

### Returns

Float


## ceil

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.ceil(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'CEIL'

### Node creation

```python
nodes.Math(value0=value0, operation='CEIL')
```

### Returns

Float


## trunc

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.trunc(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'TRUNC'

### Node creation

```python
nodes.Math(value0=value0, operation='TRUNC')
```

### Returns

Float


## fract

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.fract(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'FRACT'

### Node creation

```python
nodes.Math(value0=value0, operation='FRACT')
```

### Returns

Float


## modulo

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.modulo(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'MODULO'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='MODULO')
```

### Returns

Float


## wrap

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.wrap(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'WRAP'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP')
```

### Returns

Float


## snap

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.snap(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'SNAP'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='SNAP')
```

### Returns

Float


## pingpong

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.pingpong(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'PINGPONG'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='PINGPONG')
```

### Returns

Float


## sin

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.sin(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'SINE'

### Node creation

```python
nodes.Math(value0=value0, operation='SINE')
```

### Returns

Float


## cos

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.cos(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'COSINE'

### Node creation

```python
nodes.Math(value0=value0, operation='COSINE')
```

### Returns

Float


## tan

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.tan(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'TANGENT'

### Node creation

```python
nodes.Math(value0=value0, operation='TANGENT')
```

### Returns

Float


## arcsin

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.arcsin(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'ARCSINE'

### Node creation

```python
nodes.Math(value0=value0, operation='ARCSINE')
```

### Returns

Float


## arccos

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.arccos(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'ARCCOSINE'

### Node creation

```python
nodes.Math(value0=value0, operation='ARCCOSINE')
```

### Returns

Float


## arctan

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.arctan(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'ARCTANGENT'

### Node creation

```python
nodes.Math(value0=value0, operation='ARCTANGENT')
```

### Returns

Float


## arctan2

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.arctan2(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
- value1 : Float

#### Fixed parameters

- operation : 'ARCTAN2'

### Node creation

```python
nodes.Math(value0=value0, value1=value1, operation='ARCTAN2')
```

### Returns

Float


## sinh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.sinh(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'SINH'

### Node creation

```python
nodes.Math(value0=value0, operation='SINH')
```

### Returns

Float


## cosh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.cosh(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'COSH'

### Node creation

```python
nodes.Math(value0=value0, operation='COSH')
```

### Returns

Float


## tanh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.tanh(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'TANH'

### Node creation

```python
nodes.Math(value0=value0, operation='TANH')
```

### Returns

Float


## radians

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.radians(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'RADIANS'

### Node creation

```python
nodes.Math(value0=value0, operation='RADIANS')
```

### Returns

Float


## degrees

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = functions.degrees(value0)
```

### Arguments


#### Sockets

- value0 : Float

#### Fixed parameters

- operation : 'DEGREES'

### Node creation

```python
nodes.Math(value0=value0, operation='DEGREES')
```

### Returns

Float


## vector_add

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_add(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'ADD'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD')
```

### Returns

Vector


## vector_subtract

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_subtract(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'SUBTRACT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT')
```

### Returns

Vector


## vector_multiply

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_multiply(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'MULTIPLY'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY')
```

### Returns

Vector


## vector_divide

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_divide(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'DIVIDE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE')
```

### Returns

Vector


## vector_multiply_add

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_multiply_add(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'MULTIPLY_ADD'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD')
```

### Returns

Vector


## cross

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.cross(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'CROSS_PRODUCT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT')
```

### Returns

Vector


## project

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.project(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'PROJECT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT')
```

### Returns

Vector


## reflect

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.reflect(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'REFLECT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT')
```

### Returns

Vector


## refract

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.refract(vector0, vector1, scale)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector
- scale : Float

#### Fixed parameters

- operation : 'REFRACT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT')
```

### Returns

Vector


## faceforward

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.faceforward(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'FACEFORWARD'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD')
```

### Returns

Vector


## dot

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.dot(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'DOT_PRODUCT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT')
```

### Returns

Float


## distance

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.distance(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'DISTANCE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE')
```

### Returns

Float


## length

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.length(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'LENGTH'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='LENGTH')
```

### Returns

Float


## scale

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.scale(vector0, scale)
```

### Arguments


#### Sockets

- vector0 : Vector
- scale : Float

#### Fixed parameters

- operation : 'SCALE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE')
```

### Returns

Vector


## normalize

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.normalize(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'NORMALIZE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='NORMALIZE')
```

### Returns

Vector


## vector_absolute

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_absolute(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'ABSOLUTE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='ABSOLUTE')
```

### Returns

Vector


## vector_min

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_min(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'MINIMUM'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM')
```

### Returns

Vector


## vector_max

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_max(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'MAXIMUM'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM')
```

### Returns

Vector


## vector_floor

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_floor(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'FLOOR'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='FLOOR')
```

### Returns

Vector


## vector_ceil

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_ceil(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'CEIL'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='CEIL')
```

### Returns

Vector


## fraction

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.fraction(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'FRACTION'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='FRACTION')
```

### Returns

Vector


## vector_modulo

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_modulo(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'MODULO'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO')
```

### Returns

Vector


## vector_wrap

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_wrap(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'WRAP'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP')
```

### Returns

Vector


## vector_snap

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_snap(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
- vector1 : Vector

#### Fixed parameters

- operation : 'SNAP'

### Node creation

```python
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP')
```

### Returns

Vector


## vector_sin

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_sin(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'SINE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='SINE')
```

### Returns

Vector


## vector_cos

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_cos(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'COSINE'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='COSINE')
```

### Returns

Vector


## vector_tan

> Node: [VectorMath](section:nodes/VectorMath)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = functions.vector_tan(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector

#### Fixed parameters

- operation : 'TANGENT'

### Node creation

```python
nodes.VectorMath(vector0=vector0, operation='TANGENT')
```

### Returns

Vector


## color_mix

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_mix(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'MIX'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha)
```

### Returns

Color


## color_darken

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_darken(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'DARKEN'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha)
```

### Returns

Color


## color_multiply

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_multiply(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'MULTIPLY'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha)
```

### Returns

Color


## color_burn

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_burn(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'BURN'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha)
```

### Returns

Color


## color_lighten

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_lighten(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'LIGHTEN'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha)
```

### Returns

Color


## color_screen

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_screen(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'SCREEN'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha)
```

### Returns

Color


## color_dodge

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_dodge(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'DODGE'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha)
```

### Returns

Color


## color_add

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_add(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'ADD'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha)
```

### Returns

Color


## color_overlay

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_overlay(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'OVERLAY'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha)
```

### Returns

Color


## color_soft_light

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_soft_light(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'SOFT_LIGHT'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
```

### Returns

Color


## color_linear_light

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_linear_light(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'LINEAR_LIGHT'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
```

### Returns

Color


## color_difference

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_difference(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'DIFFERENCE'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
```

### Returns

Color


## color_subtract

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_subtract(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'SUBTRACT'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha)
```

### Returns

Color


## color_divide

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_divide(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'DIVIDE'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha)
```

### Returns

Color


## color_hue

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_hue(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'HUE'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha)
```

### Returns

Color


## color_saturation

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_saturation(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'SATURATION'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
```

### Returns

Color


## color_mix_color

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_mix_color(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'COLOR'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha)
```

### Returns

Color


## color_value

> Node: [Mix](section:nodes/Mix)
  
<sub>go to: [top](#data-socket-functions) [index](TBD)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/mix.html) </sub>

```python
v = functions.color_value(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
- color2 : Color
- fac : Float

#### Parameters

- use_alpha : False

#### Fixed parameters

- blend_type : 'VALUE'

### Node creation

```python
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha)
```

### Returns

Color

