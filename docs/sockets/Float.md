
# Class Float

> Inherits from: ***dsock.Float***

## Constructors



- [Random](#random) : value (Float)



## Methods



- [abs](#abs) : value (Float)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Float), trailing (Float), total (Float)]
- [add](#add) : value (Float)
- [arccos](#arccos) : value (Float)
- [arcsin](#arcsin) : value (Float)
- [arctan](#arctan) : value (Float)
- [arctan2](#arctan2) : value (Float)
- [attribute_statistic](#attribute_statistic) : Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Float)]
- [ceil](#ceil) : value (Float)
- [color_ramp](#color_ramp) : Sockets      [color (Color), alpha (Float)]
- [compare](#compare) : value (Float)
- [cos](#cos) : value (Float)
- [cosh](#cosh) : value (Float)
- [degrees](#degrees) : value (Float)
- [divide](#divide) : value (Float)
- [equal](#equal) : result (Boolean)
- [exp](#exp) : value (Float)
- [field_at_index](#field_at_index) : value (Float)
- [floor](#floor) : value (Float)
- [fract](#fract) : value (Float)
- [greater_equal](#greater_equal) : result (Boolean)
- [greater_than](#greater_than) : result (Boolean)
- [greater_than](#greater_than) : value (Float)
- [inverse_sqrt](#inverse_sqrt) : value (Float)
- [less_equal](#less_equal) : result (Boolean)
- [less_than](#less_than) : result (Boolean)
- [less_than](#less_than) : value (Float)
- [log](#log) : value (Float)
- [map_range](#map_range) : result (Float)
- [max](#max) : value (Float)
- [min](#min) : value (Float)
- [modulo](#modulo) : value (Float)
- [multiply](#multiply) : value (Float)
- [multiply_add](#multiply_add) : value (Float)
- [not_equal](#not_equal) : result (Boolean)
- [pingpong](#pingpong) : value (Float)
- [pow](#pow) : value (Float)
- [radians](#radians) : value (Float)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
- [round](#round) : value (Float)
- [sign](#sign) : value (Float)
- [sin](#sin) : value (Float)
- [sinh](#sinh) : value (Float)
- [smooth_max](#smooth_max) : value (Float)
- [smooth_min](#smooth_min) : value (Float)
- [snap](#snap) : value (Float)
- [sqrt](#sqrt) : value (Float)
- [subtract](#subtract) : value (Float)
- [switch](#switch) : output (Float)
- [tan](#tan) : value (Float)
- [tanh](#tanh) : value (Float)
- [to_integer](#to_integer) : integer (Integer)
- [to_string](#to_string) : string (String)
- [transfer_attribute](#transfer_attribute) : attribute (Float)
- [trunc](#trunc) : value (Float)
- [wrap](#wrap) : value (Float)



## Stacked methods



- [clamp](#clamp) : Float
- [curve](#curve) : Float



## Methods


### Random

> Node: [RandomValue](../nodes/{self.node_name}.md)

```python
v = Float.Random(min, max, ID, seed)
```


#### Arguments


##### Sockets arguments



- min : Float
- max : Float
- ID : Integer
- seed : Integer



##### Fixed parameters



- data_type : 'FLOAT'



#### Returns

    Float

### abs

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.abs()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'ABSOLUTE'



#### Returns

    Float

### accumulate_field

> Node: [AccumulateField](../nodes/{self.node_name}.md)

```python
v = float.accumulate_field(group_index, domain)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- group_index : Integer



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [leading (Float), trailing (Float), total (Float)]

### add

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.add(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'ADD'



#### Returns

    Float

### arccos

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.arccos()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'ARCCOSINE'



#### Returns

    Float

### arcsin

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.arcsin()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'ARCSINE'



#### Returns

    Float

### arctan

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.arctan()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'ARCTANGENT'



#### Returns

    Float

### arctan2

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.arctan2(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'ARCTAN2'



#### Returns

    Float

### attribute_statistic

> Node: [AttributeStatistic](../nodes/{self.node_name}.md)

```python
v = float.attribute_statistic(geometry, selection, domain)
```


#### Arguments


##### Sockets arguments



- attribute : Float (self)
- geometry : Geometry
- selection : Boolean



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]

### capture_attribute

> Node: [CaptureAttribute](../nodes/{self.node_name}.md)

```python
v = float.capture_attribute(geometry, domain)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- geometry : Geometry



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [geometry (Geometry), attribute (Float)]

### ceil

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.ceil()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'CEIL'



#### Returns

    Float

### clamp

> Node: [Clamp](../nodes/{self.node_name}.md)

```python
float.clamp(min, max, clamp_type)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- min : Float
- max : Float



##### Parameters arguments



- clamp_type : 'MINMAX' in [MINMAX, RANGE]



#### Returns

    self

### color_ramp

> Node: [Colorramp](../nodes/{self.node_name}.md)

```python
v = float.color_ramp()
```


#### Arguments


##### Sockets arguments



- fac : Float (self)



#### Returns

    Sockets [color (Color), alpha (Float)]

### compare

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.compare(value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'COMPARE'



#### Returns

    Float

### cos

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.cos()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'COSINE'



#### Returns

    Float

### cosh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.cosh()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'COSH'



#### Returns

    Float

### curve

> Node: [FloatCurve](../nodes/{self.node_name}.md)

```python
float.curve(value)
```


#### Arguments


##### Sockets arguments



- factor : Float (self)
- value : Float



#### Returns

    self

### degrees

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.degrees()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'DEGREES'



#### Returns

    Float

### divide

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.divide(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'DIVIDE'



#### Returns

    Float

### equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = float.equal(b, epsilon)
```


#### Arguments


##### Sockets arguments



- a : Float (self)
- b : Float
- epsilon : Float



##### Fixed parameters



- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'EQUAL'



#### Returns

    Boolean

### exp

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.exp()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'EXPONENT'



#### Returns

    Float

### field_at_index

> Node: [FieldAtIndex](../nodes/{self.node_name}.md)

```python
v = float.field_at_index(index, domain)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Float

### floor

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.floor()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'FLOOR'



#### Returns

    Float

### fract

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.fract()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'FRACT'



#### Returns

    Float

### greater_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = float.greater_equal(b)
```


#### Arguments


##### Sockets arguments



- a : Float (self)
- b : Float



##### Fixed parameters



- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'GREATER_EQUAL'



#### Returns

    Boolean

### greater_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.greater_than(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'GREATER_THAN'



#### Returns

    Float

### inverse_sqrt

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.inverse_sqrt()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'INVERSE_SQRT'



#### Returns

    Float

### less_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = float.less_equal(b)
```


#### Arguments


##### Sockets arguments



- a : Float (self)
- b : Float



##### Fixed parameters



- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'LESS_EQUAL'



#### Returns

    Boolean

### less_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.less_than(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'LESS_THAN'



#### Returns

    Float

### log

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.log(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'LOGARITHM'



#### Returns

    Float

### map_range

> Node: [MapRange](../nodes/{self.node_name}.md)

```python
v = float.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- from_min : Float
- from_max : Float
- to_min : Float
- to_max : Float



##### Parameters arguments



- clamp : True
- interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]



##### Fixed parameters



- data_type : 'FLOAT'



#### Returns

    Float

### max

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.max(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'MAXIMUM'



#### Returns

    Float

### min

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.min(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'MINIMUM'



#### Returns

    Float

### modulo

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.modulo(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'MODULO'



#### Returns

    Float

### multiply

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.multiply(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'MULTIPLY'



#### Returns

    Float

### multiply_add

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.multiply_add(value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'MULTIPLY_ADD'



#### Returns

    Float

### not_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = float.not_equal(b, epsilon)
```


#### Arguments


##### Sockets arguments



- a : Float (self)
- b : Float
- epsilon : Float



##### Fixed parameters



- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'



#### Returns

    Boolean

### pingpong

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.pingpong(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'PINGPONG'



#### Returns

    Float

### pow

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.pow(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'POWER'



#### Returns

    Float

### radians

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.radians()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'RADIANS'



#### Returns

    Float

### raycast

> Node: [Raycast](../nodes/{self.node_name}.md)

```python
v = float.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Float (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]



#### Returns

    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]

### round

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.round()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'ROUND'



#### Returns

    Float

### sign

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.sign()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'SIGN'



#### Returns

    Float

### sin

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.sin()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'SINE'



#### Returns

    Float

### sinh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.sinh()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'SINH'



#### Returns

    Float

### smooth_max

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.smooth_max(value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'SMOOTH_MAX'



#### Returns

    Float

### smooth_min

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.smooth_min(value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'SMOOTH_MIN'



#### Returns

    Float

### snap

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.snap(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'SNAP'



#### Returns

    Float

### sqrt

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.sqrt()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'SQRT'



#### Returns

    Float

### subtract

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.subtract(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'SUBTRACT'



#### Returns

    Float

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = float.switch(switch0, true)
```


#### Arguments


##### Sockets arguments



- false : Float (self)
- switch0 : Boolean
- true : Float



##### Fixed parameters



- input_type : 'FLOAT'



#### Returns

    Float

### tan

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.tan()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'TANGENT'



#### Returns

    Float

### tanh

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.tanh()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'TANH'



#### Returns

    Float

### to_integer

> Node: [FloatToInteger](../nodes/{self.node_name}.md)

```python
v = float.to_integer(rounding_mode)
```


#### Arguments


##### Sockets arguments



- float : Float (self)



##### Parameters arguments



- rounding_mode : 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]



#### Returns

    Integer

### to_string

> Node: [ValueToString](../nodes/{self.node_name}.md)

```python
v = float.to_string(decimals)
```


#### Arguments


##### Sockets arguments



- value : Float (self)
- decimals : Integer



#### Returns

    String

### transfer_attribute

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = float.transfer_attribute(source, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Float (self)
- source : Geometry
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Float

### trunc

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.trunc()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'TRUNC'



#### Returns

    Float

### wrap

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = float.wrap(value1, value2)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float
- value2 : Float



##### Fixed parameters



- operation : 'WRAP'



#### Returns

    Float
