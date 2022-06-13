
# geonodes functions

> global functions
  
<sub>go to [index](/docs/index.md)</sub>

Example of use:

```python
import geonodes as gn
value = gn.Float(14.) # A float value
v = gn.sin(v)         # The sine of this value
```



## Functions

- [abs](#abs) : value (Float)
- [add](#add) : value (Float)
- [arccos](#arccos) : value (Float)
- [arcsin](#arcsin) : value (Float)
- [arctan](#arctan) : value (Float)
- [arctan2](#arctan2) : value (Float)
- [ceil](#ceil) : value (Float)
- [color_add](#color_add) : color (Color)
- [color_burn](#color_burn) : color (Color)
- [color_darken](#color_darken) : color (Color)
- [color_difference](#color_difference) : color (Color)
- [color_divide](#color_divide) : color (Color)
- [color_dodge](#color_dodge) : color (Color)
- [color_hue](#color_hue) : color (Color)
- [color_lighten](#color_lighten) : color (Color)
- [color_linear_light](#color_linear_light) : color (Color)
- [color_mix](#color_mix) : color (Color)
- [color_mix_color](#color_mix_color) : color (Color)
- [color_multiply](#color_multiply) : color (Color)
- [color_overlay](#color_overlay) : color (Color)
- [color_saturation](#color_saturation) : color (Color)
- [color_screen](#color_screen) : color (Color)
- [color_soft_light](#color_soft_light) : color (Color)
- [color_subtract](#color_subtract) : color (Color)
- [color_value](#color_value) : color (Color)
- [compare](#compare) : result (Boolean)
- [compare](#compare) : value (Float)
- [cos](#cos) : value (Float)
- [cosh](#cosh) : value (Float)
- [cross](#cross) : vector (Vector)
- [degrees](#degrees) : value (Float)
- [distance](#distance) : value (Float)
- [divide](#divide) : value (Float)
- [dot](#dot) : value (Float)
- [exp](#exp) : value (Float)
- [faceforward](#faceforward) : vector (Vector)
- [floor](#floor) : value (Float)
- [fract](#fract) : value (Float)
- [fraction](#fraction) : vector (Vector)
- [greater_than](#greater_than) : value (Float)
- [inverse_sqrt](#inverse_sqrt) : value (Float)
- [join_strings](#join_strings) : string (String)
- [length](#length) : value (Float)
- [less_than](#less_than) : value (Float)
- [log](#log) : value (Float)
- [max](#max) : value (Float)
- [min](#min) : value (Float)
- [modulo](#modulo) : value (Float)
- [multiply](#multiply) : value (Float)
- [multiply_add](#multiply_add) : value (Float)
- [normalize](#normalize) : vector (Vector)
- [pingpong](#pingpong) : value (Float)
- [pow](#pow) : value (Float)
- [project](#project) : vector (Vector)
- [radians](#radians) : value (Float)
- [reflect](#reflect) : vector (Vector)
- [refract](#refract) : vector (Vector)
- [round](#round) : value (Float)
- [scale](#scale) : vector (Vector)
- [scene](#scene) : Sockets      [seconds (Float), frame (Float)]
- [sign](#sign) : value (Float)
- [sin](#sin) : value (Float)
- [sinh](#sinh) : value (Float)
- [smooth_max](#smooth_max) : value (Float)
- [smooth_min](#smooth_min) : value (Float)
- [snap](#snap) : value (Float)
- [sqrt](#sqrt) : value (Float)
- [subtract](#subtract) : value (Float)
- [tan](#tan) : value (Float)
- [tanh](#tanh) : value (Float)
- [trunc](#trunc) : value (Float)
- [vector_absolute](#vector_absolute) : vector (Vector)
- [vector_add](#vector_add) : vector (Vector)
- [vector_ceil](#vector_ceil) : vector (Vector)
- [vector_cos](#vector_cos) : vector (Vector)
- [vector_divide](#vector_divide) : vector (Vector)
- [vector_floor](#vector_floor) : vector (Vector)
- [vector_max](#vector_max) : vector (Vector)
- [vector_min](#vector_min) : vector (Vector)
- [vector_modulo](#vector_modulo) : vector (Vector)
- [vector_multiply](#vector_multiply) : vector (Vector)
- [vector_multiply_add](#vector_multiply_add) : vector (Vector)
- [vector_sin](#vector_sin) : vector (Vector)
- [vector_snap](#vector_snap) : vector (Vector)
- [vector_subtract](#vector_subtract) : vector (Vector)
- [vector_tan](#vector_tan) : vector (Vector)
- [vector_wrap](#vector_wrap) : vector (Vector)
- [wrap](#wrap) : value (Float)

## compare

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>

```python
v = functions.compare(a, b, epsilon, data_type, mode, operation)
```

### Arguments


#### Sockets

- a : Float
  - b : Float
  - epsilon : Float## Parameters
  - data_type : 'FLOAT' in [FLOAT, INT, VECTOR, STRING, RGBA]
  - mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
  - operation : 'GREATER_THAN' in [LESS_THAN, LESS_EQUAL, GREATER_THAN, GREATER_EQUAL, EQUAL, NOT_EQUAL]

### Node creation

```python
from geondes import nodes
nodes.Compare(a=a, b=b, epsilon=epsilon, data_type=data_type, mode=mode, operation=operation)
```

### Returns

Boolean


## join_strings

> Node: [JoinStrings](/docs/nodes/JoinStrings.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [GeometryNodeStringJoin](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
node ref [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html) </sub>

```python
v = functions.join_strings(strings_1, strings_2, strings_3, delimiter)
```

### Arguments


#### Sockets

- strings : *String
  - delimiter : String

### Node creation

```python
from geondes import nodes
nodes.JoinStrings(*strings, delimiter=delimiter)
```

### Returns

String


## scene

> Node: [SceneTime](/docs/nodes/SceneTime.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [GeometryNodeInputSceneTime](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
node ref [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html) </sub>

```python
v = functions.scene()
```

### Arguments


### Node creation

```python
from geondes import nodes
nodes.SceneTime()
```

### Returns

Sockets [seconds (Float), frame (Float)]


## add

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.add(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='ADD')
```

### Returns

Float


## subtract

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.subtract(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='SUBTRACT')
```

### Returns

Float


## multiply

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.multiply(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='MULTIPLY')
```

### Returns

Float


## divide

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.divide(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='DIVIDE')
```

### Returns

Float


## multiply_add

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.multiply_add(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float
  - value2 : Float## Fixed parameters
  - operation : 'MULTIPLY_ADD'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, value2=value2, operation='MULTIPLY_ADD')
```

### Returns

Float


## pow

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.pow(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'POWER'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='POWER')
```

### Returns

Float


## log

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.log(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'LOGARITHM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='LOGARITHM')
```

### Returns

Float


## sqrt

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.sqrt(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'SQRT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='SQRT')
```

### Returns

Float


## inverse_sqrt

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.inverse_sqrt(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'INVERSE_SQRT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='INVERSE_SQRT')
```

### Returns

Float


## abs

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.abs(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'ABSOLUTE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='ABSOLUTE')
```

### Returns

Float


## exp

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.exp(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'EXPONENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='EXPONENT')
```

### Returns

Float


## min

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.min(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'MINIMUM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='MINIMUM')
```

### Returns

Float


## max

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.max(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'MAXIMUM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='MAXIMUM')
```

### Returns

Float


## less_than

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.less_than(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'LESS_THAN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='LESS_THAN')
```

### Returns

Float


## greater_than

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.greater_than(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'GREATER_THAN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='GREATER_THAN')
```

### Returns

Float


## sign

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.sign(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'SIGN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='SIGN')
```

### Returns

Float


## compare

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.compare(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float
  - value2 : Float## Fixed parameters
  - operation : 'COMPARE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, value2=value2, operation='COMPARE')
```

### Returns

Float


## smooth_min

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.smooth_min(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float
  - value2 : Float## Fixed parameters
  - operation : 'SMOOTH_MIN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MIN')
```

### Returns

Float


## smooth_max

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.smooth_max(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float
  - value2 : Float## Fixed parameters
  - operation : 'SMOOTH_MAX'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, value2=value2, operation='SMOOTH_MAX')
```

### Returns

Float


## round

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.round(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'ROUND'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='ROUND')
```

### Returns

Float


## floor

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.floor(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'FLOOR'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='FLOOR')
```

### Returns

Float


## ceil

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.ceil(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'CEIL'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='CEIL')
```

### Returns

Float


## trunc

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.trunc(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'TRUNC'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='TRUNC')
```

### Returns

Float


## fract

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.fract(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'FRACT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='FRACT')
```

### Returns

Float


## modulo

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.modulo(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'MODULO'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='MODULO')
```

### Returns

Float


## wrap

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.wrap(value0, value1, value2)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float
  - value2 : Float## Fixed parameters
  - operation : 'WRAP'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, value2=value2, operation='WRAP')
```

### Returns

Float


## snap

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.snap(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'SNAP'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='SNAP')
```

### Returns

Float


## pingpong

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.pingpong(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'PINGPONG'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='PINGPONG')
```

### Returns

Float


## sin

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.sin(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'SINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='SINE')
```

### Returns

Float


## cos

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.cos(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'COSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='COSINE')
```

### Returns

Float


## tan

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.tan(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'TANGENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='TANGENT')
```

### Returns

Float


## arcsin

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.arcsin(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'ARCSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='ARCSINE')
```

### Returns

Float


## arccos

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.arccos(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'ARCCOSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='ARCCOSINE')
```

### Returns

Float


## arctan

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.arctan(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'ARCTANGENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='ARCTANGENT')
```

### Returns

Float


## arctan2

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.arctan2(value0, value1)
```

### Arguments


#### Sockets

- value0 : Float
  - value1 : Float## Fixed parameters
  - operation : 'ARCTAN2'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, value1=value1, operation='ARCTAN2')
```

### Returns

Float


## sinh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.sinh(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'SINH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='SINH')
```

### Returns

Float


## cosh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.cosh(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'COSH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='COSH')
```

### Returns

Float


## tanh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.tanh(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'TANH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='TANH')
```

### Returns

Float


## radians

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.radians(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'RADIANS'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='RADIANS')
```

### Returns

Float


## degrees

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>

```python
v = functions.degrees(value0)
```

### Arguments


#### Sockets

- value0 : Float## Fixed parameters
  - operation : 'DEGREES'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=value0, operation='DEGREES')
```

### Returns

Float


## vector_add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_add(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='ADD')
```

### Returns

Vector


## vector_subtract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_subtract(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SUBTRACT')
```

### Returns

Vector


## vector_multiply

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_multiply(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MULTIPLY')
```

### Returns

Vector


## vector_divide

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_divide(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DIVIDE')
```

### Returns

Vector


## vector_multiply_add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_multiply_add(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector
  - vector2 : Vector## Fixed parameters
  - operation : 'MULTIPLY_ADD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD')
```

### Returns

Vector


## cross

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.cross(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'CROSS_PRODUCT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='CROSS_PRODUCT')
```

### Returns

Vector


## project

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.project(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'PROJECT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='PROJECT')
```

### Returns

Vector


## reflect

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.reflect(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'REFLECT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='REFLECT')
```

### Returns

Vector


## refract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.refract(vector0, vector1, scale)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector
  - scale : Float## Fixed parameters
  - operation : 'REFRACT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, scale=scale, operation='REFRACT')
```

### Returns

Vector


## faceforward

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.faceforward(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector
  - vector2 : Vector## Fixed parameters
  - operation : 'FACEFORWARD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='FACEFORWARD')
```

### Returns

Vector


## dot

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.dot(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'DOT_PRODUCT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DOT_PRODUCT')
```

### Returns

Float


## distance

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.distance(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'DISTANCE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='DISTANCE')
```

### Returns

Float


## length

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.length(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'LENGTH'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='LENGTH')
```

### Returns

Float


## scale

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.scale(vector0, scale)
```

### Arguments


#### Sockets

- vector0 : Vector
  - scale : Float## Fixed parameters
  - operation : 'SCALE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, scale=scale, operation='SCALE')
```

### Returns

Vector


## normalize

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.normalize(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'NORMALIZE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='NORMALIZE')
```

### Returns

Vector


## vector_absolute

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_absolute(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'ABSOLUTE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='ABSOLUTE')
```

### Returns

Vector


## vector_min

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_min(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'MINIMUM'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MINIMUM')
```

### Returns

Vector


## vector_max

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_max(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'MAXIMUM'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MAXIMUM')
```

### Returns

Vector


## vector_floor

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_floor(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'FLOOR'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='FLOOR')
```

### Returns

Vector


## vector_ceil

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_ceil(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'CEIL'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='CEIL')
```

### Returns

Vector


## fraction

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.fraction(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'FRACTION'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='FRACTION')
```

### Returns

Vector


## vector_modulo

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_modulo(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'MODULO'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='MODULO')
```

### Returns

Vector


## vector_wrap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_wrap(vector0, vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector
  - vector2 : Vector## Fixed parameters
  - operation : 'WRAP'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, vector2=vector2, operation='WRAP')
```

### Returns

Vector


## vector_snap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_snap(vector0, vector1)
```

### Arguments


#### Sockets

- vector0 : Vector
  - vector1 : Vector## Fixed parameters
  - operation : 'SNAP'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, vector1=vector1, operation='SNAP')
```

### Returns

Vector


## vector_sin

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_sin(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'SINE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='SINE')
```

### Returns

Vector


## vector_cos

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_cos(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'COSINE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='COSINE')
```

### Returns

Vector


## vector_tan

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>

```python
v = functions.vector_tan(vector0)
```

### Arguments


#### Sockets

- vector0 : Vector## Fixed parameters
  - operation : 'TANGENT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=vector0, operation='TANGENT')
```

### Returns

Vector


## color_mix

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_mix(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'MIX'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MIX', use_alpha=use_alpha)
```

### Returns

Color


## color_darken

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_darken(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'DARKEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DARKEN', use_alpha=use_alpha)
```

### Returns

Color


## color_multiply

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_multiply(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='MULTIPLY', use_alpha=use_alpha)
```

### Returns

Color


## color_burn

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_burn(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'BURN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='BURN', use_alpha=use_alpha)
```

### Returns

Color


## color_lighten

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_lighten(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'LIGHTEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LIGHTEN', use_alpha=use_alpha)
```

### Returns

Color


## color_screen

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_screen(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'SCREEN'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SCREEN', use_alpha=use_alpha)
```

### Returns

Color


## color_dodge

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_dodge(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'DODGE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DODGE', use_alpha=use_alpha)
```

### Returns

Color


## color_add

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_add(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='ADD', use_alpha=use_alpha)
```

### Returns

Color


## color_overlay

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_overlay(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'OVERLAY'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='OVERLAY', use_alpha=use_alpha)
```

### Returns

Color


## color_soft_light

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_soft_light(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'SOFT_LIGHT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SOFT_LIGHT', use_alpha=use_alpha)
```

### Returns

Color


## color_linear_light

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_linear_light(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'LINEAR_LIGHT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='LINEAR_LIGHT', use_alpha=use_alpha)
```

### Returns

Color


## color_difference

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_difference(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'DIFFERENCE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIFFERENCE', use_alpha=use_alpha)
```

### Returns

Color


## color_subtract

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_subtract(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SUBTRACT', use_alpha=use_alpha)
```

### Returns

Color


## color_divide

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_divide(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='DIVIDE', use_alpha=use_alpha)
```

### Returns

Color


## color_hue

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_hue(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'HUE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='HUE', use_alpha=use_alpha)
```

### Returns

Color


## color_saturation

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_saturation(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'SATURATION'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='SATURATION', use_alpha=use_alpha)
```

### Returns

Color


## color_mix_color

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_mix_color(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'COLOR'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='COLOR', use_alpha=use_alpha)
```

### Returns

Color


## color_value

> Node: [Mix](/docs/nodes/Mix.md)
  
<sub>go to: [top](#data-socket-functions) [index](/docs/index.md)
blender ref [ShaderNodeMixRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixRGB.html)
node ref [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/color/mix_rgb.html) </sub>

```python
v = functions.color_value(color1, color2, fac, use_alpha)
```

### Arguments


#### Sockets

- color1 : Color
  - color2 : Color
  - fac : Float## Parameters
  - use_alpha : False## Fixed parameters
  - blend_type : 'VALUE'

### Node creation

```python
from geondes import nodes
nodes.Mix(color1=color1, color2=color2, fac=fac, blend_type='VALUE', use_alpha=use_alpha)
```

### Returns

Color

