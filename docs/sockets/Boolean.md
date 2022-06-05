
# Class Boolean

> Inherits from: ***dsock.Boolean***

## Constructors



- [**Random**](#random) : [RandomValue](../nodes/RandomValue.md) value (Boolean)



## Methods



- [**b_and**](#b_and) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**b_not**](#b_not) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**b_or**](#b_or) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**capture_attribute**](#capture_attribute) : [CaptureAttribute](../nodes/CaptureAttribute.md) Sockets      [geometry (Geometry), attribute (Boolean)]
- [**field_at_index**](#field_at_index) : [FieldAtIndex](../nodes/FieldAtIndex.md) value (Boolean)
- [**imply**](#imply) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**nand**](#nand) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**nimply**](#nimply) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**nor**](#nor) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**raycast**](#raycast) : [Raycast](../nodes/Raycast.md) Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
- [**switch**](#switch) : [Switch](../nodes/Switch.md) output (Boolean)
- [**transfer_attribute**](#transfer_attribute) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Boolean)
- [**xnor**](#xnor) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)
- [**xor**](#xor) : [BooleanMath](../nodes/BooleanMath.md) boolean (Boolean)



## Methods reference


### Random

> Node: [RandomValue](../nodes/{self.node_name}.md)

```python
v = Boolean.Random(probability, ID, seed)
```


#### Arguments


##### Sockets arguments



- probability : Float
- ID : Integer
- seed : Integer



##### Fixed parameters



- data_type : 'BOOLEAN'



#### Node creation


```python
node = nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')
```


#### Returns

    Boolean

### b_and

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.b_and(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'AND'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND')
```


#### Returns

    Boolean

### b_not

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.b_not()
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)



##### Fixed parameters



- operation : 'NOT'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, operation='NOT')
```


#### Returns

    Boolean

### b_or

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.b_or(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'OR'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR')
```


#### Returns

    Boolean

### capture_attribute

> Node: [CaptureAttribute](../nodes/{self.node_name}.md)

```python
v = boolean.capture_attribute(geometry, domain)
```


#### Arguments


##### Sockets arguments



- value : Boolean (self)
- geometry : Geometry



##### Fixed parameters



- data_type : 'BOOLEAN'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)
```


#### Returns

    Sockets [geometry (Geometry), attribute (Boolean)]

### field_at_index

> Node: [FieldAtIndex](../nodes/{self.node_name}.md)

```python
v = boolean.field_at_index(index, domain)
```


#### Arguments


##### Sockets arguments



- value : Boolean (self)
- index : Integer



##### Fixed parameters



- data_type : 'BOOLEAN'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain)
```


#### Returns

    Boolean

### imply

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.imply(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'IMPLY'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY')
```


#### Returns

    Boolean

### nand

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.nand(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'NAND'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND')
```


#### Returns

    Boolean

### nimply

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.nimply(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'NIMPLY'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY')
```


#### Returns

    Boolean

### nor

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.nor(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'NOR'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR')
```


#### Returns

    Boolean

### raycast

> Node: [Raycast](../nodes/{self.node_name}.md)

```python
v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Boolean (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float



##### Fixed parameters



- data_type : 'BOOLEAN'



##### Parameters arguments



- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]



#### Node creation


```python
node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)
```


#### Returns

    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]

### switch

> Node: [Switch](../nodes/{self.node_name}.md)

```python
v = boolean.switch(false, true)
```


#### Arguments


##### Sockets arguments



- switch0 : Boolean (self)
- false : Boolean
- true : Boolean



##### Fixed parameters



- input_type : 'BOOLEAN'



#### Node creation


```python
node = nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN')
```


#### Returns

    Boolean

### transfer_attribute

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = boolean.transfer_attribute(source, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Boolean (self)
- source : Geometry
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'BOOLEAN'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Node creation


```python
node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping)
```


#### Returns

    Boolean

### xnor

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.xnor(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'XNOR'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR')
```


#### Returns

    Boolean

### xor

> Node: [BooleanMath](../nodes/{self.node_name}.md)

```python
v = boolean.xor(boolean1)
```


#### Arguments


##### Sockets arguments



- boolean0 : Boolean (self)
- boolean1 : Boolean



##### Fixed parameters



- operation : 'XOR'



#### Node creation


```python
node = nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR')
```


#### Returns

    Boolean
