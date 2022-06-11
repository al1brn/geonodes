
# Data socket Boolean

> Inherits from dsock.Boolean
  
<sub>go to [index](TBD)</sub>



## Constructors

- [Random](#random) : [RandomValue](section:nodes/RandomValue), value (Boolean)

## Methods

- [b_and](#b_and) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [b_not](#b_not) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [b_or](#b_or) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [capture_attribute](#capture_attribute) : [CaptureAttribute](section:nodes/CaptureAttribute), Sockets      [geometry (Geometry), attribute (Boolean)]
- [field_at_index](#field_at_index) : [FieldAtIndex](section:nodes/FieldAtIndex), value (Boolean)
- [imply](#imply) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [nand](#nand) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [nimply](#nimply) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [nor](#nor) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [raycast](#raycast) : [Raycast](section:nodes/Raycast), Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]
- [switch](#switch) : [Switch](section:nodes/Switch), output (Boolean)
- [transfer_attribute](#transfer_attribute) : [TransferAttribute](section:nodes/TransferAttribute), attribute (Boolean)
- [xnor](#xnor) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)
- [xor](#xor) : [BooleanMath](section:nodes/BooleanMath), boolean (Boolean)

## Random

> Node: [RandomValue](section:nodes/RandomValue)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/random_value.html) </sub>

```python
v = Boolean.Random(probability, ID, seed)
```

### Arguments


#### Sockets

- probability : Float
- ID : Integer
- seed : Integer

#### Fixed parameters

- data_type : 'BOOLEAN'

### Node creation

```python
nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN')
```

### Returns

Boolean


## transfer_attribute

> Node: [TransferAttribute](section:nodes/TransferAttribute)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/transfer_attribute.html) </sub>

```python
v = boolean.transfer_attribute(source, source_position, index, domain, mapping)
```

### Arguments


#### Sockets

- attribute : Boolean (self)
- source : Geometry
- source_position : Vector
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

#### Fixed parameters

- data_type : 'BOOLEAN'

### Node creation

```python
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping)
```

### Returns

Boolean


## capture_attribute

> Node: [CaptureAttribute](section:nodes/CaptureAttribute)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/capture_attribute.html) </sub>

```python
v = boolean.capture_attribute(geometry, domain)
```

### Arguments


#### Sockets

- value : Boolean (self)
- geometry : Geometry

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'BOOLEAN'

### Node creation

```python
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain)
```

### Returns

Sockets [geometry (Geometry), attribute (Boolean)]


## field_at_index

> Node: [FieldAtIndex](section:nodes/FieldAtIndex)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/field_at_index.html) </sub>

```python
v = boolean.field_at_index(index, domain)
```

### Arguments


#### Sockets

- value : Boolean (self)
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'BOOLEAN'

### Node creation

```python
nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain)
```

### Returns

Boolean


## raycast

> Node: [Raycast](section:nodes/Raycast)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/raycast.html) </sub>

```python
v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```

### Arguments


#### Sockets

- attribute : Boolean (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float

#### Parameters

- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Fixed parameters

- data_type : 'BOOLEAN'

### Node creation

```python
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]


## switch

> Node: [Switch](section:nodes/Switch)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/switch.html) </sub>

```python
v = boolean.switch(false, true)
```

### Arguments


#### Sockets

- switch0 : Boolean (self)
- false : Boolean
- true : Boolean

#### Fixed parameters

- input_type : 'BOOLEAN'

### Node creation

```python
nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN')
```

### Returns

Boolean


## b_and

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.b_and(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'AND'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND')
```

### Returns

Boolean


## b_or

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.b_or(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'OR'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR')
```

### Returns

Boolean


## b_not

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.b_not()
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)

#### Fixed parameters

- operation : 'NOT'

### Node creation

```python
nodes.BooleanMath(boolean0=self, operation='NOT')
```

### Returns

Boolean


## nand

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.nand(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'NAND'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND')
```

### Returns

Boolean


## nor

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.nor(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'NOR'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR')
```

### Returns

Boolean


## xnor

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.xnor(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'XNOR'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR')
```

### Returns

Boolean


## xor

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.xor(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'XOR'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR')
```

### Returns

Boolean


## imply

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.imply(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'IMPLY'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY')
```

### Returns

Boolean


## nimply

> Node: [BooleanMath](section:nodes/BooleanMath)
  
<sub>go to: [top](#data-socket-boolean) [index](TBD)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/boolean_math.html) </sub>

```python
v = boolean.nimply(boolean1)
```

### Arguments


#### Sockets

- boolean0 : Boolean (self)
- boolean1 : Boolean

#### Fixed parameters

- operation : 'NIMPLY'

### Node creation

```python
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY')
```

### Returns

Boolean

