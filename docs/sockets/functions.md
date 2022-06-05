
# Class functions


## Functions



- abs : value (Float)
- add : value (Float)
- arccos : value (Float)
- arcsin : value (Float)
- arctan : value (Float)
- arctan2 : value (Float)
- ceil : value (Float)
- color_add : color (Color)
- color_burn : color (Color)
- color_darken : color (Color)
- color_difference : color (Color)
- color_divide : color (Color)
- color_dodge : color (Color)
- color_hue : color (Color)
- color_lighten : color (Color)
- color_linear_light : color (Color)
- color_mix : color (Color)
- color_mix_color : color (Color)
- color_multiply : color (Color)
- color_overlay : color (Color)
- color_saturation : color (Color)
- color_screen : color (Color)
- color_soft_light : color (Color)
- color_subtract : color (Color)
- color_value : color (Color)
- compare : result (Boolean)
- compare : value (Float)
- cos : value (Float)
- cosh : value (Float)
- cross : vector (Vector)
- degrees : value (Float)
- distance : value (Float)
- divide : value (Float)
- dot : value (Float)
- exp : value (Float)
- faceforward : vector (Vector)
- floor : value (Float)
- fract : value (Float)
- fraction : vector (Vector)
- greater_than : value (Float)
- inverse_sqrt : value (Float)
- join_strings : string (String)
- length : value (Float)
- less_than : value (Float)
- log : value (Float)
- max : value (Float)
- min : value (Float)
- modulo : value (Float)
- multiply : value (Float)
- multiply_add : value (Float)
- normalize : vector (Vector)
- pingpong : value (Float)
- pow : value (Float)
- project : vector (Vector)
- radians : value (Float)
- reflect : vector (Vector)
- refract : vector (Vector)
- round : value (Float)
- scale : vector (Vector)
- scene : Sockets      [seconds (Float), frame (Float)]
- sign : value (Float)
- sin : value (Float)
- sinh : value (Float)
- smooth_max : value (Float)
- smooth_min : value (Float)
- snap : value (Float)
- sqrt : value (Float)
- subtract : value (Float)
- tan : value (Float)
- tanh : value (Float)
- trunc : value (Float)
- vector_absolute : vector (Vector)
- vector_add : vector (Vector)
- vector_ceil : vector (Vector)
- vector_cos : vector (Vector)
- vector_divide : vector (Vector)
- vector_floor : vector (Vector)
- vector_max : vector (Vector)
- vector_min : vector (Vector)
- vector_modulo : vector (Vector)
- vector_multiply : vector (Vector)
- vector_multiply_add : vector (Vector)
- vector_sin : vector (Vector)
- vector_snap : vector (Vector)
- vector_subtract : vector (Vector)
- vector_tan : vector (Vector)
- vector_wrap : vector (Vector)
- wrap : value (Float)



## Methods


### abs

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.abs(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'ABSOLUTE'



#### Returns

    Float

### add

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.add(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'ADD'



#### Returns

    Float

### arccos

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.arccos(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'ARCCOSINE'



#### Returns

    Float

### arcsin

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.arcsin(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'ARCSINE'



#### Returns

    Float

### arctan

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.arctan(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'ARCTANGENT'



#### Returns

    Float

### arctan2

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.arctan2(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'ARCTAN2'



#### Returns

    Float

### ceil

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.ceil(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'CEIL'



#### Returns

    Float

### color_add

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_add(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'ADD'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_burn

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_burn(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'BURN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_darken

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_darken(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DARKEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_difference

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_difference(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DIFFERENCE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_divide

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_divide(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DIVIDE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_dodge

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_dodge(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'DODGE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_hue

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_hue(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'HUE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_lighten

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_lighten(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'LIGHTEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_linear_light

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_linear_light(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'LINEAR_LIGHT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_mix

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_mix(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'MIX'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_mix_color

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_mix_color(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'COLOR'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_multiply

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_multiply(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'MULTIPLY'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_overlay

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_overlay(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'OVERLAY'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_saturation

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_saturation(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SATURATION'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_screen

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_screen(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SCREEN'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_soft_light

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_soft_light(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SOFT_LIGHT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_subtract

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_subtract(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'SUBTRACT'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### color_value

> Node: [Mix](../nodes/{self.node_name}.md)

```python
v = functions.color_value(color1, color2, fac, use_alpha)
```


#### Arguments


##### Sockets arguments



- color1 : Color
- color2 : Color
- fac : Float



##### Fixed parameters



- blend_type : 'VALUE'



##### Parameters arguments



- use_alpha : False



#### Returns

    Color

### compare

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.compare(value0, value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'COMPARE'



#### Returns

    Float

### cos

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.cos(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'COSINE'



#### Returns

    Float

### cosh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.cosh(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'COSH'



#### Returns

    Float

### cross

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.cross(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'CROSS_PRODUCT'



#### Returns

    Vector

### degrees

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.degrees(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'DEGREES'



#### Returns

    Float

### distance

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.distance(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'DISTANCE'



#### Returns

    Float

### divide

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.divide(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'DIVIDE'



#### Returns

    Float

### dot

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.dot(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'DOT_PRODUCT'



#### Returns

    Float

### exp

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.exp(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'EXPONENT'



#### Returns

    Float

### faceforward

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.faceforward(vector0, vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'FACEFORWARD'



#### Returns

    Vector

### floor

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.floor(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'FLOOR'



#### Returns

    Float

### fract

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.fract(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'FRACT'



#### Returns

    Float

### fraction

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.fraction(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'FRACTION'



#### Returns

    Vector

### greater_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.greater_than(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'GREATER_THAN'



#### Returns

    Float

### inverse_sqrt

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.inverse_sqrt(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'INVERSE_SQRT'



#### Returns

    Float

### join_strings

> Node: [JoinStrings](../nodes/{self.node_name}.md)

```python
v = functions.join_strings(strings_1, strings_2, strings_3, delimiter)
```


#### Arguments


##### Sockets arguments



- strings : *String
- delimiter : String



#### Returns

    String

### length

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.length(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'LENGTH'



#### Returns

    Float

### less_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.less_than(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'LESS_THAN'



#### Returns

    Float

### log

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.log(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'LOGARITHM'



#### Returns

    Float

### max

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.max(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'MAXIMUM'



#### Returns

    Float

### min

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.min(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'MINIMUM'



#### Returns

    Float

### modulo

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.modulo(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'MODULO'



#### Returns

    Float

### multiply

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.multiply(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'MULTIPLY'



#### Returns

    Float

### multiply_add

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.multiply_add(value0, value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'MULTIPLY_ADD'



#### Returns

    Float

### normalize

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.normalize(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'NORMALIZE'



#### Returns

    Vector

### pingpong

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.pingpong(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'PINGPONG'



#### Returns

    Float

### pow

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.pow(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'POWER'



#### Returns

    Float

### project

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.project(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'PROJECT'



#### Returns

    Vector

### radians

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.radians(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'RADIANS'



#### Returns

    Float

### reflect

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.reflect(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'REFLECT'



#### Returns

    Vector

### refract

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.refract(vector0, vector1, scale)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector
- scale : Float



##### Fixed parameters



- operation : 'REFRACT'



#### Returns

    Vector

### round

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.round(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'ROUND'



#### Returns

    Float

### scale

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.scale(vector0, scale)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- scale : Float



##### Fixed parameters



- operation : 'SCALE'



#### Returns

    Vector

### scene

> Node: [SceneTime](../nodes/{self.node_name}.md)

```python
v = functions.scene()
```


#### Arguments


#### Returns

    Sockets [seconds (Float), frame (Float)]

### sign

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.sign(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'SIGN'



#### Returns

    Float

### sin

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.sin(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'SINE'



#### Returns

    Float

### sinh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.sinh(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'SINH'



#### Returns

    Float

### smooth_max

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.smooth_max(value0, value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'SMOOTH_MAX'



#### Returns

    Float

### smooth_min

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.smooth_min(value0, value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'SMOOTH_MIN'



#### Returns

    Float

### snap

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.snap(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'SNAP'



#### Returns

    Float

### sqrt

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.sqrt(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'SQRT'



#### Returns

    Float

### subtract

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.subtract(value0, value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float



##### Fixed parameters



- operation : 'SUBTRACT'



#### Returns

    Float

### tan

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.tan(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'TANGENT'



#### Returns

    Float

### tanh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.tanh(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'TANH'



#### Returns

    Float

### trunc

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.trunc(value0)
```


#### Arguments


##### Sockets arguments



- value0 : Float



##### Fixed parameters



- operation : 'TRUNC'



#### Returns

    Float

### vector_absolute

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_absolute(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'ABSOLUTE'



#### Returns

    Vector

### vector_add

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_add(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'ADD'



#### Returns

    Vector

### vector_ceil

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_ceil(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'CEIL'



#### Returns

    Vector

### vector_cos

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_cos(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'COSINE'



#### Returns

    Vector

### vector_divide

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_divide(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'DIVIDE'



#### Returns

    Vector

### vector_floor

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_floor(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'FLOOR'



#### Returns

    Vector

### vector_max

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_max(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'MAXIMUM'



#### Returns

    Vector

### vector_min

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_min(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'MINIMUM'



#### Returns

    Vector

### vector_modulo

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_modulo(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'MODULO'



#### Returns

    Vector

### vector_multiply

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_multiply(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'MULTIPLY'



#### Returns

    Vector

### vector_multiply_add

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_multiply_add(vector0, vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'MULTIPLY_ADD'



#### Returns

    Vector

### vector_sin

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_sin(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'SINE'



#### Returns

    Vector

### vector_snap

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_snap(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'SNAP'



#### Returns

    Vector

### vector_subtract

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_subtract(vector0, vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector



##### Fixed parameters



- operation : 'SUBTRACT'



#### Returns

    Vector

### vector_tan

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_tan(vector0)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector



##### Fixed parameters



- operation : 'TANGENT'



#### Returns

    Vector

### vector_wrap

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = functions.vector_wrap(vector0, vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'WRAP'



#### Returns

    Vector

### wrap

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = functions.wrap(value0, value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'WRAP'



#### Returns

    Float
