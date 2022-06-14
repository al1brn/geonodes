
# Data socket Boolean

> Inherits from dsock.Boolean
  
<sub>go to [index](/docs/index.md)</sub>



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

## Random

> Node: [RandomValue](/docs/nodes/RandomValue.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) </sub>
                          
```python
v = Boolean.Random(probability, ID, seed, node_label = None, node_color = None)
```

### Arguments

## Sockets
- probability : Float
- ID : Integer
- seed : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.RandomValue(probability=probability, ID=ID, seed=seed, data_type='BOOLEAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## transfer_attribute

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = boolean.transfer_attribute(source, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Boolean (self)
- source : Geometry
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='BOOLEAN', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Boolean


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) </sub>
                          
```python
v = boolean.capture_attribute(geometry, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Boolean (self)
- geometry : Geometry## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), attribute (Boolean)]


## field_at_index

> Node: [FieldAtIndex](/docs/nodes/FieldAtIndex.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) </sub>
                          
```python
v = boolean.field_at_index(index, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Boolean (self)
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.FieldAtIndex(value=self, index=index, data_type='BOOLEAN', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Boolean


## raycast

> Node: [Raycast](/docs/nodes/Raycast.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) </sub>
                          
```python
v = boolean.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Boolean (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float## Parameters
- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='BOOLEAN', mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Boolean)]


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = boolean.switch(false, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- switch0 : Boolean (self)
- false : Boolean
- true : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'BOOLEAN'

### Node creation

```python
from geondes import nodes
nodes.Switch(switch0=self, false=false, true=true, input_type='BOOLEAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## b_and

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.b_and(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'AND'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='AND', label=node_label, node_color=node_color)
```

### Returns

Boolean


## b_or

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.b_or(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'OR'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='OR', label=node_label, node_color=node_color)
```

### Returns

Boolean


## b_not

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.b_not(node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'NOT'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, operation='NOT', label=node_label, node_color=node_color)
```

### Returns

Boolean


## nand

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.nand(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'NAND'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NAND', label=node_label, node_color=node_color)
```

### Returns

Boolean


## nor

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.nor(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'NOR'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NOR', label=node_label, node_color=node_color)
```

### Returns

Boolean


## xnor

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.xnor(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'XNOR'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XNOR', label=node_label, node_color=node_color)
```

### Returns

Boolean


## xor

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.xor(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'XOR'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='XOR', label=node_label, node_color=node_color)
```

### Returns

Boolean


## imply

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.imply(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'IMPLY'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='IMPLY', label=node_label, node_color=node_color)
```

### Returns

Boolean


## nimply

> Node: [BooleanMath](/docs/nodes/BooleanMath.md)
  
<sub>go to: [top](#data-socket-boolean) [index](/docs/index.md)
blender ref [FunctionNodeBooleanMath](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
node ref [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/boolean_math.html) </sub>
                          
```python
v = boolean.nimply(boolean1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- boolean0 : Boolean (self)
- boolean1 : Boolean## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'NIMPLY'

### Node creation

```python
from geondes import nodes
nodes.BooleanMath(boolean0=self, boolean1=boolean1, operation='NIMPLY', label=node_label, node_color=node_color)
```

### Returns

Boolean

