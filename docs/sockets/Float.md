
# Data socket Float

> Inherits from dsock.Float
  
<sub>go to [index](docs/index.md)</sub>



## Constructors

- [Random](#random) : [RandomValue](section:nodes/RandomValue), value (Float)

## Methods

- [abs](#abs) : [Math](section:nodes/Math), value (Float)
- [accumulate_field](#accumulate_field) : [AccumulateField](section:nodes/AccumulateField), Sockets      [leading (Float), trailing (Float), total (Float)]
- [add](#add) : [Math](section:nodes/Math), value (Float)
- [arccos](#arccos) : [Math](section:nodes/Math), value (Float)
- [arcsin](#arcsin) : [Math](section:nodes/Math), value (Float)
- [arctan](#arctan) : [Math](section:nodes/Math), value (Float)
- [arctan2](#arctan2) : [Math](section:nodes/Math), value (Float)
- [attribute_statistic](#attribute_statistic) : [AttributeStatistic](section:nodes/AttributeStatistic), Sockets      [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
- [capture_attribute](#capture_attribute) : [CaptureAttribute](section:nodes/CaptureAttribute), Sockets      [geometry (Geometry), attribute (Float)]
- [ceil](#ceil) : [Math](section:nodes/Math), value (Float)
- [clamp](#clamp) : [Clamp](section:nodes/Clamp), result (Float)
- [color_ramp](#color_ramp) : [Colorramp](section:nodes/Colorramp), Sockets      [color (Color), alpha (Float)]
- [compare](#compare) : [Math](section:nodes/Math), value (Float)
- [cos](#cos) : [Math](section:nodes/Math), value (Float)
- [cosh](#cosh) : [Math](section:nodes/Math), value (Float)
- [curve](#curve) : [FloatCurve](section:nodes/FloatCurve), value (Float)
- [degrees](#degrees) : [Math](section:nodes/Math), value (Float)
- [divide](#divide) : [Math](section:nodes/Math), value (Float)
- [equal](#equal) : [Compare](section:nodes/Compare), result (Boolean)
- [exp](#exp) : [Math](section:nodes/Math), value (Float)
- [field_at_index](#field_at_index) : [FieldAtIndex](section:nodes/FieldAtIndex), value (Float)
- [floor](#floor) : [Math](section:nodes/Math), value (Float)
- [fract](#fract) : [Math](section:nodes/Math), value (Float)
- [greater_equal](#greater_equal) : [Compare](section:nodes/Compare), result (Boolean)
- [greater_than](#greater_than) : [Compare](section:nodes/Compare), result (Boolean)
- [greater_than](#greater_than) : [Math](section:nodes/Math), value (Float)
- [inverse_sqrt](#inverse_sqrt) : [Math](section:nodes/Math), value (Float)
- [less_equal](#less_equal) : [Compare](section:nodes/Compare), result (Boolean)
- [less_than](#less_than) : [Compare](section:nodes/Compare), result (Boolean)
- [less_than](#less_than) : [Math](section:nodes/Math), value (Float)
- [log](#log) : [Math](section:nodes/Math), value (Float)
- [map_range](#map_range) : [MapRange](section:nodes/MapRange), result (Float)
- [max](#max) : [Math](section:nodes/Math), value (Float)
- [min](#min) : [Math](section:nodes/Math), value (Float)
- [modulo](#modulo) : [Math](section:nodes/Math), value (Float)
- [multiply](#multiply) : [Math](section:nodes/Math), value (Float)
- [multiply_add](#multiply_add) : [Math](section:nodes/Math), value (Float)
- [not_equal](#not_equal) : [Compare](section:nodes/Compare), result (Boolean)
- [pingpong](#pingpong) : [Math](section:nodes/Math), value (Float)
- [pow](#pow) : [Math](section:nodes/Math), value (Float)
- [radians](#radians) : [Math](section:nodes/Math), value (Float)
- [raycast](#raycast) : [Raycast](section:nodes/Raycast), Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
- [round](#round) : [Math](section:nodes/Math), value (Float)
- [sign](#sign) : [Math](section:nodes/Math), value (Float)
- [sin](#sin) : [Math](section:nodes/Math), value (Float)
- [sinh](#sinh) : [Math](section:nodes/Math), value (Float)
- [smooth_max](#smooth_max) : [Math](section:nodes/Math), value (Float)
- [smooth_min](#smooth_min) : [Math](section:nodes/Math), value (Float)
- [snap](#snap) : [Math](section:nodes/Math), value (Float)
- [sqrt](#sqrt) : [Math](section:nodes/Math), value (Float)
- [subtract](#subtract) : [Math](section:nodes/Math), value (Float)
- [switch](#switch) : [Switch](section:nodes/Switch), output (Float)
- [tan](#tan) : [Math](section:nodes/Math), value (Float)
- [tanh](#tanh) : [Math](section:nodes/Math), value (Float)
- [to_integer](#to_integer) : [FloatToInteger](section:nodes/FloatToInteger), integer (Integer)
- [to_string](#to_string) : [ValueToString](section:nodes/ValueToString), string (String)
- [transfer_attribute](#transfer_attribute) : [TransferAttribute](section:nodes/TransferAttribute), attribute (Float)
- [trunc](#trunc) : [Math](section:nodes/Math), value (Float)
- [wrap](#wrap) : [Math](section:nodes/Math), value (Float)

## Random

> Node: [RandomValue](section:nodes/RandomValue)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/random_value.html) </sub>

```python
v = Float.Random(min, max, ID, seed)
```

### Arguments


#### Sockets

- min : Float
- max : Float
- ID : Integer
- seed : Integer

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT')
```

### Returns

Float


## accumulate_field

> Node: [AccumulateField](section:nodes/AccumulateField)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
node ref [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/accumulate_field.html) </sub>

```python
v = float.accumulate_field(group_index, domain)
```

### Arguments


#### Sockets

- value : Float (self)
- group_index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT', domain=domain)
```

### Returns

Sockets [leading (Float), trailing (Float), total (Float)]


## attribute_statistic

> Node: [AttributeStatistic](section:nodes/AttributeStatistic)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
node ref [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/attribute_statistic.html) </sub>

```python
v = float.attribute_statistic(geometry, selection, domain)
```

### Arguments


#### Sockets

- attribute : Float (self)
- geometry : Geometry
- selection : Boolean

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT', domain=domain)
```

### Returns

Sockets [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]


## transfer_attribute

> Node: [TransferAttribute](section:nodes/TransferAttribute)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/transfer_attribute.html) </sub>

```python
v = float.transfer_attribute(source, source_position, index, domain, mapping)
```

### Arguments


#### Sockets

- attribute : Float (self)
- source : Geometry
- source_position : Vector
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT', domain=domain, mapping=mapping)
```

### Returns

Float


## capture_attribute

> Node: [CaptureAttribute](section:nodes/CaptureAttribute)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/capture_attribute.html) </sub>

```python
v = float.capture_attribute(geometry, domain)
```

### Arguments


#### Sockets

- value : Float (self)
- geometry : Geometry

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT', domain=domain)
```

### Returns

Sockets [geometry (Geometry), attribute (Float)]


## field_at_index

> Node: [FieldAtIndex](section:nodes/FieldAtIndex)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/field_at_index.html) </sub>

```python
v = float.field_at_index(index, domain)
```

### Arguments


#### Sockets

- value : Float (self)
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT', domain=domain)
```

### Returns

Float


## raycast

> Node: [Raycast](section:nodes/Raycast)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/raycast.html) </sub>

```python
v = float.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```

### Arguments


#### Sockets

- attribute : Float (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float

#### Parameters

- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT', mapping=mapping)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]


## switch

> Node: [Switch](section:nodes/Switch)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
node ref [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/switch.html) </sub>

```python
v = float.switch(switch0, true)
```

### Arguments


#### Sockets

- false : Float (self)
- switch0 : Boolean
- true : Float

#### Fixed parameters

- input_type : 'FLOAT'

### Node creation

```python
nodes.Switch(false=self, switch0=switch0, true=true, input_type='FLOAT')
```

### Returns

Float


## map_range

> Node: [MapRange](section:nodes/MapRange)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
node ref [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/map_range.html) </sub>

```python
v = float.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type)
```

### Arguments


#### Sockets

- value : Float (self)
- from_min : Float
- from_max : Float
- to_min : Float
- to_max : Float

#### Parameters

- clamp : True
- interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

#### Fixed parameters

- data_type : 'FLOAT'

### Node creation

```python
nodes.MapRange(value=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT', interpolation_type=interpolation_type)
```

### Returns

Float


## less_than

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.less_than(b)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'LESS_THAN'

### Node creation

```python
nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_THAN')
```

### Returns

Boolean


## less_equal

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.less_equal(b)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'LESS_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='LESS_EQUAL')
```

### Returns

Boolean


## greater_than

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.greater_than(b)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'GREATER_THAN'

### Node creation

```python
nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN')
```

### Returns

Boolean


## greater_equal

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.greater_equal(b)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'GREATER_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, data_type='FLOAT', mode='ELEMENT', operation='GREATER_EQUAL')
```

### Returns

Boolean


## equal

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.equal(b, epsilon)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float
- epsilon : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='EQUAL')
```

### Returns

Boolean


## not_equal

> Node: [Compare](section:nodes/Compare)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = float.not_equal(b, epsilon)
```

### Arguments


#### Sockets

- a : Float (self)
- b : Float
- epsilon : Float

#### Fixed parameters

- data_type : 'FLOAT'
- mode : 'ELEMENT'
- operation : 'NOT_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, epsilon=epsilon, data_type='FLOAT', mode='ELEMENT', operation='NOT_EQUAL')
```

### Returns

Boolean


## add

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.add(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'ADD'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='ADD')
```

### Returns

Float


## subtract

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.subtract(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'SUBTRACT'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='SUBTRACT')
```

### Returns

Float


## multiply

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.multiply(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'MULTIPLY'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='MULTIPLY')
```

### Returns

Float


## divide

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.divide(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'DIVIDE'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='DIVIDE')
```

### Returns

Float


## multiply_add

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.multiply_add(value1, value2)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'MULTIPLY_ADD'

### Node creation

```python
nodes.Math(value0=self, value1=value1, value2=value2, operation='MULTIPLY_ADD')
```

### Returns

Float


## pow

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.pow(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'POWER'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='POWER')
```

### Returns

Float


## log

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.log(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'LOGARITHM'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='LOGARITHM')
```

### Returns

Float


## sqrt

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.sqrt()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'SQRT'

### Node creation

```python
nodes.Math(value0=self, operation='SQRT')
```

### Returns

Float


## inverse_sqrt

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.inverse_sqrt()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'INVERSE_SQRT'

### Node creation

```python
nodes.Math(value0=self, operation='INVERSE_SQRT')
```

### Returns

Float


## abs

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.abs()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'ABSOLUTE'

### Node creation

```python
nodes.Math(value0=self, operation='ABSOLUTE')
```

### Returns

Float


## exp

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.exp()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'EXPONENT'

### Node creation

```python
nodes.Math(value0=self, operation='EXPONENT')
```

### Returns

Float


## min

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.min(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'MINIMUM'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='MINIMUM')
```

### Returns

Float


## max

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.max(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'MAXIMUM'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='MAXIMUM')
```

### Returns

Float


## less_than

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.less_than(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'LESS_THAN'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='LESS_THAN')
```

### Returns

Float


## greater_than

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.greater_than(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'GREATER_THAN'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='GREATER_THAN')
```

### Returns

Float


## sign

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.sign()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'SIGN'

### Node creation

```python
nodes.Math(value0=self, operation='SIGN')
```

### Returns

Float


## compare

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.compare(value1, value2)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'COMPARE'

### Node creation

```python
nodes.Math(value0=self, value1=value1, value2=value2, operation='COMPARE')
```

### Returns

Float


## smooth_min

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.smooth_min(value1, value2)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'SMOOTH_MIN'

### Node creation

```python
nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MIN')
```

### Returns

Float


## smooth_max

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.smooth_max(value1, value2)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'SMOOTH_MAX'

### Node creation

```python
nodes.Math(value0=self, value1=value1, value2=value2, operation='SMOOTH_MAX')
```

### Returns

Float


## round

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.round()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'ROUND'

### Node creation

```python
nodes.Math(value0=self, operation='ROUND')
```

### Returns

Float


## floor

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.floor()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'FLOOR'

### Node creation

```python
nodes.Math(value0=self, operation='FLOOR')
```

### Returns

Float


## ceil

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.ceil()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'CEIL'

### Node creation

```python
nodes.Math(value0=self, operation='CEIL')
```

### Returns

Float


## trunc

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.trunc()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'TRUNC'

### Node creation

```python
nodes.Math(value0=self, operation='TRUNC')
```

### Returns

Float


## fract

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.fract()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'FRACT'

### Node creation

```python
nodes.Math(value0=self, operation='FRACT')
```

### Returns

Float


## modulo

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.modulo(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'MODULO'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='MODULO')
```

### Returns

Float


## wrap

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.wrap(value1, value2)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float
- value2 : Float

#### Fixed parameters

- operation : 'WRAP'

### Node creation

```python
nodes.Math(value0=self, value1=value1, value2=value2, operation='WRAP')
```

### Returns

Float


## snap

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.snap(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'SNAP'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='SNAP')
```

### Returns

Float


## pingpong

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.pingpong(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'PINGPONG'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='PINGPONG')
```

### Returns

Float


## sin

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.sin()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'SINE'

### Node creation

```python
nodes.Math(value0=self, operation='SINE')
```

### Returns

Float


## cos

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.cos()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'COSINE'

### Node creation

```python
nodes.Math(value0=self, operation='COSINE')
```

### Returns

Float


## tan

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.tan()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'TANGENT'

### Node creation

```python
nodes.Math(value0=self, operation='TANGENT')
```

### Returns

Float


## arcsin

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.arcsin()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'ARCSINE'

### Node creation

```python
nodes.Math(value0=self, operation='ARCSINE')
```

### Returns

Float


## arccos

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.arccos()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'ARCCOSINE'

### Node creation

```python
nodes.Math(value0=self, operation='ARCCOSINE')
```

### Returns

Float


## arctan

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.arctan()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'ARCTANGENT'

### Node creation

```python
nodes.Math(value0=self, operation='ARCTANGENT')
```

### Returns

Float


## arctan2

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.arctan2(value1)
```

### Arguments


#### Sockets

- value0 : Float (self)
- value1 : Float

#### Fixed parameters

- operation : 'ARCTAN2'

### Node creation

```python
nodes.Math(value0=self, value1=value1, operation='ARCTAN2')
```

### Returns

Float


## sinh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.sinh()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'SINH'

### Node creation

```python
nodes.Math(value0=self, operation='SINH')
```

### Returns

Float


## cosh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.cosh()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'COSH'

### Node creation

```python
nodes.Math(value0=self, operation='COSH')
```

### Returns

Float


## tanh

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.tanh()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'TANH'

### Node creation

```python
nodes.Math(value0=self, operation='TANH')
```

### Returns

Float


## radians

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.radians()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'RADIANS'

### Node creation

```python
nodes.Math(value0=self, operation='RADIANS')
```

### Returns

Float


## degrees

> Node: [Math](section:nodes/Math)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
node ref [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/math.html) </sub>

```python
v = float.degrees()
```

### Arguments


#### Sockets

- value0 : Float (self)

#### Fixed parameters

- operation : 'DEGREES'

### Node creation

```python
nodes.Math(value0=self, operation='DEGREES')
```

### Returns

Float


## to_integer

> Node: [FloatToInteger](section:nodes/FloatToInteger)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeFloatToInt](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
node ref [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/float_to_integer.html) </sub>

```python
v = float.to_integer(rounding_mode)
```

### Arguments


#### Sockets

- float : Float (self)

#### Parameters

- rounding_mode : 'ROUND' in [ROUND, FLOOR, CEILING, TRUNCATE]

### Node creation

```python
nodes.FloatToInteger(float=self, rounding_mode=rounding_mode)
```

### Returns

Integer


## to_string

> Node: [ValueToString](section:nodes/ValueToString)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [FunctionNodeValueToString](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
node ref [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/value_to_string.html) </sub>

```python
v = float.to_string(decimals)
```

### Arguments


#### Sockets

- value : Float (self)
- decimals : Integer

### Node creation

```python
nodes.ValueToString(value=self, decimals=decimals)
```

### Returns

String


## color_ramp

> Node: [Colorramp](section:nodes/Colorramp)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeValToRGB](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
node ref [ColorRamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/colorramp.html) </sub>

```python
v = float.color_ramp()
```

### Arguments


#### Sockets

- fac : Float (self)

### Node creation

```python
nodes.Colorramp(fac=self)
```

### Returns

Sockets [color (Color), alpha (Float)]


## curve

> Node: [FloatCurve](section:nodes/FloatCurve)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeFloatCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
node ref [Float Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/float_curve.html) </sub>

```python
v = float.curve(factor)
```

### Arguments


#### Sockets

- value : Float (self)
- factor : Float

### Node creation

```python
nodes.FloatCurve(value=self, factor=factor)
```

### Returns

Float


## clamp

> Node: [Clamp](section:nodes/Clamp)
  
<sub>go to: [top](#data-socket-float) [index](docs/index.md)
blender ref [ShaderNodeClamp](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
node ref [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/clamp.html) </sub>

```python
v = float.clamp(min, max, clamp_type)
```

### Arguments


#### Sockets

- value : Float (self)
- min : Float
- max : Float

#### Parameters

- clamp_type : 'MINMAX' in [MINMAX, RANGE]

### Node creation

```python
nodes.Clamp(value=self, min=min, max=max, clamp_type=clamp_type)
```

### Returns

Float

