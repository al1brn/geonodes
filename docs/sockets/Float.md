
# Class Float

> Inherits from: ***dsock.Float***

## Constructors



- [Random](#random) : [RandomValue](../nodes/RandomValue.md) value (Float)



## Methods



- [abs](#abs) : [Math](../nodes/Math.md) value (Float)
- [accumulate_field](#accumulate_field) : [AccumulateField](../nodes/AccumulateField.md) Sockets      [leading (Float), trailing (Float), total (Float)]
- [add](#add) : [Math](../nodes/Math.md) value (Float)
- [arccos](#arccos) : [Math](../nodes/Math.md) value (Float)
- [arcsin](#arcsin) : [Math](../nodes/Math.md) value (Float)
- [arctan](#arctan) : [Math](../nodes/Math.md) value (Float)
- [arctan2](#arctan2) : [Math](../nodes/Math.md) value (Float)
- [attribute_statistic](#attribute_statistic) : [AttributeStatistic](../nodes/AttributeStatistic.md) Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
- [capture_attribute](#capture_attribute) : [CaptureAttribute](../nodes/CaptureAttribute.md) Sockets      [geometry (Geometry), attribute (Float)]
- [ceil](#ceil) : [Math](../nodes/Math.md) value (Float)
- [color_ramp](#color_ramp) : [Colorramp](../nodes/Colorramp.md) Sockets      [color (Color), alpha (Float)]
- [compare](#compare) : [Math](../nodes/Math.md) value (Float)
- [cos](#cos) : [Math](../nodes/Math.md) value (Float)
- [cosh](#cosh) : [Math](../nodes/Math.md) value (Float)
- [degrees](#degrees) : [Math](../nodes/Math.md) value (Float)
- [divide](#divide) : [Math](../nodes/Math.md) value (Float)
- [equal](#equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [exp](#exp) : [Math](../nodes/Math.md) value (Float)
- [field_at_index](#field_at_index) : [FieldAtIndex](../nodes/FieldAtIndex.md) value (Float)
- [floor](#floor) : [Math](../nodes/Math.md) value (Float)
- [fract](#fract) : [Math](../nodes/Math.md) value (Float)
- [greater_equal](#greater_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [greater_than](#greater_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [greater_than](#greater_than) : [Math](../nodes/Math.md) value (Float)
- [inverse_sqrt](#inverse_sqrt) : [Math](../nodes/Math.md) value (Float)
- [less_equal](#less_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [less_than](#less_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [less_than](#less_than) : [Math](../nodes/Math.md) value (Float)
- [log](#log) : [Math](../nodes/Math.md) value (Float)
- [map_range](#map_range) : [MapRange](../nodes/MapRange.md) result (Float)
- [max](#max) : [Math](../nodes/Math.md) value (Float)
- [min](#min) : [Math](../nodes/Math.md) value (Float)
- [modulo](#modulo) : [Math](../nodes/Math.md) value (Float)
- [multiply](#multiply) : [Math](../nodes/Math.md) value (Float)
- [multiply_add](#multiply_add) : [Math](../nodes/Math.md) value (Float)
- [not_equal](#not_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [pingpong](#pingpong) : [Math](../nodes/Math.md) value (Float)
- [pow](#pow) : [Math](../nodes/Math.md) value (Float)
- [radians](#radians) : [Math](../nodes/Math.md) value (Float)
- [raycast](#raycast) : [Raycast](../nodes/Raycast.md) Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
- [round](#round) : [Math](../nodes/Math.md) value (Float)
- [sign](#sign) : [Math](../nodes/Math.md) value (Float)
- [sin](#sin) : [Math](../nodes/Math.md) value (Float)
- [sinh](#sinh) : [Math](../nodes/Math.md) value (Float)
- [smooth_max](#smooth_max) : [Math](../nodes/Math.md) value (Float)
- [smooth_min](#smooth_min) : [Math](../nodes/Math.md) value (Float)
- [snap](#snap) : [Math](../nodes/Math.md) value (Float)
- [sqrt](#sqrt) : [Math](../nodes/Math.md) value (Float)
- [subtract](#subtract) : [Math](../nodes/Math.md) value (Float)
- [switch](#switch) : [Switch](../nodes/Switch.md) output (Float)
- [tan](#tan) : [Math](../nodes/Math.md) value (Float)
- [tanh](#tanh) : [Math](../nodes/Math.md) value (Float)
- [to_integer](#to_integer) : [FloatToInteger](../nodes/FloatToInteger.md) integer (Integer)
- [to_string](#to_string) : [ValueToString](../nodes/ValueToString.md) string (String)
- [transfer_attribute](#transfer_attribute) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Float)
- [trunc](#trunc) : [Math](../nodes/Math.md) value (Float)
- [wrap](#wrap) : [Math](../nodes/Math.md) value (Float)



## Stacked methods



- [clamp](#clamp) : [Clamp](../nodes/Clamp.md) Float
- [curve](#curve) : [FloatCurve](../nodes/FloatCurve.md) Float



## Methods reference


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



#### Node creation


```python
node = nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ABSOLUTE')
```


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



#### Node creation


```python
node = nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='ADD')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCCOSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCTANGENT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='ARCTAN2')
```


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



#### Node creation


```python
node = nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain)
```


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



#### Node creation


```python
node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='CEIL')
```


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



#### Node creation


```python
node = nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type)
```


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



#### Node creation


```python
node = nodes.Colorramp(fac=self)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='COSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='COSH')
```


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



#### Node creation


```python
node = nodes.FloatCurve(factor=self, value=value)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='DEGREES')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='DIVIDE')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='EXPONENT')
```


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



#### Node creation


```python
node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='FLOOR')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='FRACT')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='GREATER_THAN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='INVERSE_SQRT')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='LESS_THAN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='LOGARITHM')
```


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



#### Node creation


```python
node = nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MAXIMUM')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MINIMUM')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MODULO')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MULTIPLY')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='PINGPONG')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='POWER')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='RADIANS')
```


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



#### Node creation


```python
node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ROUND')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SIGN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SINH')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='SNAP')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SQRT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='SUBTRACT')
```


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



#### Node creation


```python
node = nodes.Switch(false=self, switch0=switch0, true=true, input_type='FLOAT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TANGENT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TANH')
```


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



#### Node creation


```python
node = nodes.FloatToInteger(float=self, rounding_mode=rounding_mode)
```


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



#### Node creation


```python
node = nodes.ValueToString(value=self, decimals=decimals)
```


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



#### Node creation


```python
node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TRUNC')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP')
```


#### Returns

    Float
