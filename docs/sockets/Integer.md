
# Class Integer

> Inherits from: ***dsock.Integer***

## Constructors



- Random : value (Integer)



## Methods



- abs : value (Float)
- accumulate_field : Sockets      [leading (Integer), trailing (Integer), total (Integer)]
- add : value (Float)
- arccos : value (Float)
- arcsin : value (Float)
- arctan : value (Float)
- arctan2 : value (Float)
- capture_attribute : Sockets      [geometry (Geometry), attribute (Integer)]
- ceil : value (Float)
- compare : value (Float)
- cos : value (Float)
- cosh : value (Float)
- degrees : value (Float)
- divide : value (Float)
- equal : result (Boolean)
- exp : value (Float)
- field_at_index : value (Integer)
- floor : value (Float)
- fract : value (Float)
- greater_equal : result (Boolean)
- greater_than : result (Boolean)
- greater_than : value (Float)
- inverse_sqrt : value (Float)
- less_equal : result (Boolean)
- less_than : result (Boolean)
- less_than : value (Float)
- log : value (Float)
- max : value (Float)
- min : value (Float)
- modulo : value (Float)
- multiply : value (Float)
- multiply_add : value (Float)
- not_equal : result (Boolean)
- pingpong : value (Float)
- pow : value (Float)
- radians : value (Float)
- raycast : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
- round : value (Float)
- sign : value (Float)
- sin : value (Float)
- sinh : value (Float)
- smooth_max : value (Float)
- smooth_min : value (Float)
- snap : value (Float)
- sqrt : value (Float)
- subtract : value (Float)
- switch : output (Integer)
- tan : value (Float)
- tanh : value (Float)
- transfer_attribute : attribute (Integer)
- trunc : value (Float)
- wrap : value (Float)



## Methods


### Random

> Node: [RandomValue](../nodes/{self.node_name}.md)

```python
v = Integer.Random(min, max, ID, seed)
```


#### Arguments


##### Sockets arguments



- min : Integer
- max : Integer
- ID : Integer
- seed : Integer



##### Fixed parameters



- data_type : 'INT'



#### Returns

    Integer

### abs

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.abs()
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
v = integer.accumulate_field(group_index, domain)
```


#### Arguments


##### Sockets arguments



- value : Integer (self)
- group_index : Integer



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [leading (Integer), trailing (Integer), total (Integer)]

### add

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.add(value1)
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
v = integer.arccos()
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
v = integer.arcsin()
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
v = integer.arctan()
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
v = integer.arctan2(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'ARCTAN2'



#### Returns

    Float

### capture_attribute

> Node: [CaptureAttribute](../nodes/{self.node_name}.md)

```python
v = integer.capture_attribute(geometry, domain)
```


#### Arguments


##### Sockets arguments



- value : Integer (self)
- geometry : Geometry



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Sockets [geometry (Geometry), attribute (Integer)]

### ceil

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.ceil()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'CEIL'



#### Returns

    Float

### compare

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.compare(value1, value2)
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
v = integer.cos()
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
v = integer.cosh()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'COSH'



#### Returns

    Float

### degrees

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.degrees()
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
v = integer.divide(value1)
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
v = integer.equal(b)
```


#### Arguments


##### Sockets arguments



- a : Integer (self)
- b : Integer



##### Fixed parameters



- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'EQUAL'



#### Returns

    Boolean

### exp

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.exp()
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
v = integer.field_at_index(value, domain)
```


#### Arguments


##### Sockets arguments



- index : Integer (self)
- value : Integer



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Returns

    Integer

### floor

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.floor()
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
v = integer.fract()
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
v = integer.greater_equal(b)
```


#### Arguments


##### Sockets arguments



- a : Integer (self)
- b : Integer



##### Fixed parameters



- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'GREATER_EQUAL'



#### Returns

    Boolean

### greater_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.greater_than(value1)
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
v = integer.inverse_sqrt()
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
v = integer.less_equal(b)
```


#### Arguments


##### Sockets arguments



- a : Integer (self)
- b : Integer



##### Fixed parameters



- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'LESS_EQUAL'



#### Returns

    Boolean

### less_than

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.less_than(value1)
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
v = integer.log(value1)
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)
- value1 : Float



##### Fixed parameters



- operation : 'LOGARITHM'



#### Returns

    Float

### max

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.max(value1)
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
v = integer.min(value1)
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
v = integer.modulo(value1)
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
v = integer.multiply(value1)
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
v = integer.multiply_add(value1, value2)
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
v = integer.not_equal(b)
```


#### Arguments


##### Sockets arguments



- a : Integer (self)
- b : Integer



##### Fixed parameters



- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'



#### Returns

    Boolean

### pingpong

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.pingpong(value1)
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
v = integer.pow(value1)
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
v = integer.radians()
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
v = integer.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Integer (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]



#### Returns

    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]

### round

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.round()
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
v = integer.sign()
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
v = integer.sin()
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
v = integer.sinh()
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
v = integer.smooth_max(value1, value2)
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
v = integer.smooth_min(value1, value2)
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
v = integer.snap(value1)
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
v = integer.sqrt()
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
v = integer.subtract(value1)
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
v = integer.switch(switch0, true)
```


#### Arguments


##### Sockets arguments



- false : Integer (self)
- switch0 : Boolean
- true : Integer



##### Fixed parameters



- input_type : 'INT'



#### Returns

    Integer

### tan

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.tan()
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
v = integer.tanh()
```


#### Arguments


##### Sockets arguments



- value0 : Float (self)



##### Fixed parameters



- operation : 'TANH'



#### Returns

    Float

### transfer_attribute

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = integer.transfer_attribute(source, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Integer (self)
- source : Geometry
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'INT'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Returns

    Integer

### trunc

> Node: [Math](../nodes/{self.node_name}.md)

```python
v = integer.trunc()
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
v = integer.wrap(value1, value2)
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
