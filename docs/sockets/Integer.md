
# Data socket Integer

> Inherits from dsock.Integer
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Random](#random) : value (Integer)

## Methods

- [abs](#abs) : value (Float)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Integer), trailing (Integer), total (Integer)]
- [add](#add) : value (Float)
- [arccos](#arccos) : value (Float)
- [arcsin](#arcsin) : value (Float)
- [arctan](#arctan) : value (Float)
- [arctan2](#arctan2) : value (Float)
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Integer)]
- [ceil](#ceil) : value (Float)
- [compare](#compare) : value (Float)
- [cos](#cos) : value (Float)
- [cosh](#cosh) : value (Float)
- [degrees](#degrees) : value (Float)
- [divide](#divide) : value (Float)
- [equal](#equal) : result (Boolean)
- [exp](#exp) : value (Float)
- [field_at_index](#field_at_index) : value (Integer)
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
- [max](#max) : value (Float)
- [min](#min) : value (Float)
- [modulo](#modulo) : value (Float)
- [multiply](#multiply) : value (Float)
- [multiply_add](#multiply_add) : value (Float)
- [not_equal](#not_equal) : result (Boolean)
- [pingpong](#pingpong) : value (Float)
- [pow](#pow) : value (Float)
- [radians](#radians) : value (Float)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]
- [round](#round) : value (Float)
- [sign](#sign) : value (Float)
- [sin](#sin) : value (Float)
- [sinh](#sinh) : value (Float)
- [smooth_max](#smooth_max) : value (Float)
- [smooth_min](#smooth_min) : value (Float)
- [snap](#snap) : value (Float)
- [sqrt](#sqrt) : value (Float)
- [subtract](#subtract) : value (Float)
- [switch](#switch) : output (Integer)
- [tan](#tan) : value (Float)
- [tanh](#tanh) : value (Float)
- [transfer_attribute](#transfer_attribute) : attribute (Integer)
- [trunc](#trunc) : value (Float)
- [wrap](#wrap) : value (Float)

## Random

> Node: [RandomValue](/docs/nodes/RandomValue.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) </sub>
                          
```python
v = Integer.Random(min, max, ID, seed, node_label = None, node_color = None)
```

### Arguments

## Sockets
- min : Integer
- max : Integer
- ID : Integer
- seed : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='INT', label=node_label, node_color=node_color)
```

### Returns

Integer


## accumulate_field

> Node: [AccumulateField](/docs/nodes/AccumulateField.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
node ref [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) </sub>
                          
```python
v = integer.accumulate_field(group_index, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Integer (self)
- group_index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.AccumulateField(value=self, group_index=group_index, data_type='INT', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [leading (Integer), trailing (Integer), total (Integer)]


## transfer_attribute

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/transfer_attribute.html) </sub>
                          
```python
v = integer.transfer_attribute(source, source_position, index, domain, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Integer (self)
- source : Geometry
- source_position : Vector
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='INT', domain=domain, mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Integer


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) </sub>
                          
```python
v = integer.capture_attribute(geometry, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Integer (self)
- geometry : Geometry## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='INT', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), attribute (Integer)]


## field_at_index

> Node: [FieldAtIndex](/docs/nodes/FieldAtIndex.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) </sub>
                          
```python
v = integer.field_at_index(value, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- index : Integer (self)
- value : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.FieldAtIndex(index=self, value=value, data_type='INT', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Integer


## raycast

> Node: [Raycast](/docs/nodes/Raycast.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) </sub>
                          
```python
v = integer.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Integer (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float## Parameters
- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='INT', mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Integer)]


## switch

> Node: [Switch](/docs/nodes/Switch.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) </sub>
                          
```python
v = integer.switch(switch0, true, node_label = None, node_color = None)
```

### Arguments

## Sockets
- false : Integer (self)
- switch0 : Boolean
- true : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- input_type : 'INT'

### Node creation

```python
from geondes import nodes
nodes.Switch(false=self, switch0=switch0, true=true, input_type='INT', label=node_label, node_color=node_color)
```

### Returns

Integer


## less_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.less_than(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'LESS_THAN'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_THAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## less_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.less_equal(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'LESS_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='LESS_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## greater_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.greater_than(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'GREATER_THAN'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_THAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## greater_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.greater_equal(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'GREATER_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='GREATER_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.equal(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## not_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = integer.not_equal(b, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Integer (self)
- b : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'INT'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, data_type='INT', mode='ELEMENT', operation='NOT_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## add

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.add(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='ADD', label=node_label, node_color=node_color)
```

### Returns

Float


## subtract

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.subtract(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='SUBTRACT', label=node_label, node_color=node_color)
```

### Returns

Float


## multiply

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.multiply(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='MULTIPLY', label=node_label, node_color=node_color)
```

### Returns

Float


## divide

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.divide(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='DIVIDE', label=node_label, node_color=node_color)
```

### Returns

Float


## multiply_add

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.multiply_add(value1, value2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float
- value2 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MULTIPLY_ADD'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
```

### Returns

Float


## pow

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.pow(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'POWER'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='POWER', label=node_label, node_color=node_color)
```

### Returns

Float


## log

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.log(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'LOGARITHM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='LOGARITHM', label=node_label, node_color=node_color)
```

### Returns

Float


## sqrt

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.sqrt(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SQRT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='SQRT', label=node_label, node_color=node_color)
```

### Returns

Float


## inverse_sqrt

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.inverse_sqrt(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'INVERSE_SQRT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='INVERSE_SQRT', label=node_label, node_color=node_color)
```

### Returns

Float


## abs

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.abs(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ABSOLUTE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
```

### Returns

Float


## exp

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.exp(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'EXPONENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='EXPONENT', label=node_label, node_color=node_color)
```

### Returns

Float


## min

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.min(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MINIMUM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='MINIMUM', label=node_label, node_color=node_color)
```

### Returns

Float


## max

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.max(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MAXIMUM'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='MAXIMUM', label=node_label, node_color=node_color)
```

### Returns

Float


## less_than

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.less_than(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'LESS_THAN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='LESS_THAN', label=node_label, node_color=node_color)
```

### Returns

Float


## greater_than

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.greater_than(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'GREATER_THAN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='GREATER_THAN', label=node_label, node_color=node_color)
```

### Returns

Float


## sign

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.sign(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SIGN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='SIGN', label=node_label, node_color=node_color)
```

### Returns

Float


## compare

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.compare(value1, value2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float
- value2 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'COMPARE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE', label=node_label, node_color=node_color)
```

### Returns

Float


## smooth_min

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.smooth_min(value1, value2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float
- value2 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SMOOTH_MIN'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN', label=node_label, node_color=node_color)
```

### Returns

Float


## smooth_max

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.smooth_max(value1, value2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float
- value2 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SMOOTH_MAX'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX', label=node_label, node_color=node_color)
```

### Returns

Float


## round

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.round(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ROUND'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='ROUND', label=node_label, node_color=node_color)
```

### Returns

Float


## floor

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.floor(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'FLOOR'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='FLOOR', label=node_label, node_color=node_color)
```

### Returns

Float


## ceil

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.ceil(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'CEIL'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='CEIL', label=node_label, node_color=node_color)
```

### Returns

Float


## trunc

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.trunc(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'TRUNC'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='TRUNC', label=node_label, node_color=node_color)
```

### Returns

Float


## fract

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.fract(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'FRACT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='FRACT', label=node_label, node_color=node_color)
```

### Returns

Float


## modulo

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.modulo(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MODULO'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='MODULO', label=node_label, node_color=node_color)
```

### Returns

Float


## wrap

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.wrap(value1, value2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float
- value2 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'WRAP'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP', label=node_label, node_color=node_color)
```

### Returns

Float


## snap

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.snap(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SNAP'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='SNAP', label=node_label, node_color=node_color)
```

### Returns

Float


## pingpong

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.pingpong(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'PINGPONG'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='PINGPONG', label=node_label, node_color=node_color)
```

### Returns

Float


## sin

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.sin(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='SINE', label=node_label, node_color=node_color)
```

### Returns

Float


## cos

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.cos(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'COSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='COSINE', label=node_label, node_color=node_color)
```

### Returns

Float


## tan

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.tan(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'TANGENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='TANGENT', label=node_label, node_color=node_color)
```

### Returns

Float


## arcsin

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.arcsin(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ARCSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='ARCSINE', label=node_label, node_color=node_color)
```

### Returns

Float


## arccos

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.arccos(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ARCCOSINE'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='ARCCOSINE', label=node_label, node_color=node_color)
```

### Returns

Float


## arctan

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.arctan(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ARCTANGENT'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='ARCTANGENT', label=node_label, node_color=node_color)
```

### Returns

Float


## arctan2

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.arctan2(value1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)
- value1 : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ARCTAN2'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, value1=value1, operation='ARCTAN2', label=node_label, node_color=node_color)
```

### Returns

Float


## sinh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.sinh(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SINH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='SINH', label=node_label, node_color=node_color)
```

### Returns

Float


## cosh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.cosh(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'COSH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='COSH', label=node_label, node_color=node_color)
```

### Returns

Float


## tanh

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.tanh(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'TANH'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='TANH', label=node_label, node_color=node_color)
```

### Returns

Float


## radians

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.radians(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'RADIANS'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='RADIANS', label=node_label, node_color=node_color)
```

### Returns

Float


## degrees

> Node: [Math](/docs/nodes/Math.md)
  
<sub>go to: [top](#data-socket-integer) [index](/docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math.html) </sub>
                          
```python
v = integer.degrees(node_label = None, node_color = None)
```

### Arguments

## Sockets
- value0 : Float (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DEGREES'

### Node creation

```python
from geondes import nodes
nodes.Math(value0=self, operation='DEGREES', label=node_label, node_color=node_color)
```

### Returns

Float

