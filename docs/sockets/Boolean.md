
# Class Boolean

> Inherits from: ***dsock.Boolean***

## Constructors



- [Random](#random) : value (Boolean)



## Methods



- [b_and](#b_and) : boolean (Boolean)
- [b_not](#b_not) : boolean (Boolean)
- [b_or](#b_or) : boolean (Boolean)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Boolean)]
- [field_at_index](#field_at_index) : value (Boolean)
- [imply](#imply) : boolean (Boolean)
- [nand](#nand) : boolean (Boolean)
- [nimply](#nimply) : boolean (Boolean)
- [nor](#nor) : boolean (Boolean)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
- [switch](#switch) : output (Boolean)
- [transfer_attribute](#transfer_attribute) : attribute (Boolean)
- [xnor](#xnor) : boolean (Boolean)
- [xor](#xor) : boolean (Boolean)



## Methods


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



#### Returns

    Boolean
