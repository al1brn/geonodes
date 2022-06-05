
# Class Integer

> Inherits from: ***dsock.Integer***

## Constructors



- [**self.meth_name**](#random) : [RandomValue](../nodes/RandomValue.md) value (Integer)



## Methods



- [**self.meth_name**](#abs) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#accumulate_field) : [AccumulateField](../nodes/AccumulateField.md) Sockets      [leading (Integer), trailing (Integer), total (Integer)]
- [**self.meth_name**](#add) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#arccos) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#arcsin) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#arctan) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#arctan2) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#capture_attribute) : [CaptureAttribute](../nodes/CaptureAttribute.md) Sockets      [geometry (Geometry), attribute (Integer)]
- [**self.meth_name**](#ceil) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#compare) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#cos) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#cosh) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#degrees) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#divide) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#exp) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#field_at_index) : [FieldAtIndex](../nodes/FieldAtIndex.md) value (Integer)
- [**self.meth_name**](#floor) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#fract) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#greater_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#greater_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#greater_than) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#inverse_sqrt) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#less_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#less_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#less_than) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#log) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#max) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#min) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#modulo) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#multiply) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#multiply_add) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#not_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [**self.meth_name**](#pingpong) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#pow) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#radians) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#raycast) : [Raycast](../nodes/Raycast.md) Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
- [**self.meth_name**](#round) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#sign) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#sin) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#sinh) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#smooth_max) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#smooth_min) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#snap) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#sqrt) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#subtract) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#switch) : [Switch](../nodes/Switch.md) output (Integer)
- [**self.meth_name**](#tan) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#tanh) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#transfer_attribute) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Integer)
- [**self.meth_name**](#trunc) : [Math](../nodes/Math.md) value (Float)
- [**self.meth_name**](#wrap) : [Math](../nodes/Math.md) value (Float)



## Methods reference


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



#### Node creation


```python
node = nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ABSOLUTE')
```


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



#### Node creation


```python
node = nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='ADD')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCCOSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ARCTANGENT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='ARCTAN2')
```


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



#### Node creation


```python
node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='CEIL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='COSINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='COSH')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='DEGREES')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='DIVIDE')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='EXPONENT')
```


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



#### Node creation


```python
node = nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='FLOOR')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='FRACT')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='GREATER_THAN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='INVERSE_SQRT')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='LESS_THAN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='LOGARITHM')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MAXIMUM')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MINIMUM')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MODULO')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='MULTIPLY')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD')
```


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



#### Node creation


```python
node = nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='PINGPONG')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='POWER')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='RADIANS')
```


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



#### Node creation


```python
node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='ROUND')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SIGN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SINE')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SINH')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='SNAP')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='SQRT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, operation='SUBTRACT')
```


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



#### Node creation


```python
node = nodes.Switch(false=self, switch0=switch0, true=true, input_type='INT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TANGENT')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TANH')
```


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



#### Node creation


```python
node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping)
```


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



#### Node creation


```python
node = nodes.Math(value0=self, operation='TRUNC')
```


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



#### Node creation


```python
node = nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP')
```


#### Returns

    Float
