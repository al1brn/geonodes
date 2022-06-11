
# Data socket Vector

> Inherits from dsock.Vector
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [AlignToVector](#aligntovector) : [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md), rotation (Vector)
- [Combine](#combine) : [CombineXyz](/docs/nodes/CombineXyz.md), vector (Vector)
- [Random](#random) : [RandomValue](/docs/nodes/RandomValue.md), value (Vector)

## Properties

- [separate](#separate) : [SeparateXyz](/docs/nodes/SeparateXyz.md), Sockets      [x (Float), y (Float), z (Float)]
- [x](#x) : [SeparateXyz](/docs/nodes/SeparateXyz.md), x (Float) = separate.x
- [y](#y) : [SeparateXyz](/docs/nodes/SeparateXyz.md), y (Float) = separate.y
- [z](#z) : [SeparateXyz](/docs/nodes/SeparateXyz.md), z (Float) = separate.z

## Methods

- [absolute](#absolute) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [accumulate_field](#accumulate_field) : [AccumulateField](/docs/nodes/AccumulateField.md), Sockets      [leading (Vector), trailing (Vector), total (Vector)]
- [add](#add) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [align_to_vector](#align_to_vector) : [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md), rotation (Vector)
- [attribute_statistic](#attribute_statistic) : [AttributeStatistic](/docs/nodes/AttributeStatistic.md), Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
- [capture_attribute](#capture_attribute) : [CaptureAttribute](/docs/nodes/CaptureAttribute.md), Sockets      [geometry (Geometry), attribute (Vector)]
- [ceil](#ceil) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [cos](#cos) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [cross](#cross) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [curves](#curves) : [VectorCurves](/docs/nodes/VectorCurves.md), vector (Vector)
- [distance](#distance) : [VectorMath](/docs/nodes/VectorMath.md), value (Float)
- [divide](#divide) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [dot](#dot) : [VectorMath](/docs/nodes/VectorMath.md), value (Float)
- [equal](#equal) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [faceforward](#faceforward) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [field_at_index](#field_at_index) : [FieldAtIndex](/docs/nodes/FieldAtIndex.md), value (Vector)
- [floor](#floor) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [fraction](#fraction) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [greater_equal](#greater_equal) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [greater_than](#greater_than) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [length](#length) : [VectorMath](/docs/nodes/VectorMath.md), value (Float)
- [less_equal](#less_equal) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [less_than](#less_than) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [map_range](#map_range) : [MapRange](/docs/nodes/MapRange.md), vector (Vector)
- [max](#max) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [min](#min) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [modulo](#modulo) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [multiply](#multiply) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [multiply_add](#multiply_add) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [normalize](#normalize) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [not_equal](#not_equal) : [Compare](/docs/nodes/Compare.md), result (Boolean)
- [project](#project) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [raycast](#raycast) : [Raycast](/docs/nodes/Raycast.md), Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
- [reflect](#reflect) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [refract](#refract) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [rotate](#rotate) : [VectorRotate](/docs/nodes/VectorRotate.md), vector (Vector)
- [rotate_euler](#rotate_euler) : [RotateEuler](/docs/nodes/RotateEuler.md), rotation (Vector)
- [scale](#scale) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [sin](#sin) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [snap](#snap) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [subtract](#subtract) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [tan](#tan) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)
- [transfer_attribute](#transfer_attribute) : [TransferAttribute](/docs/nodes/TransferAttribute.md), attribute (Vector)
- [wrap](#wrap) : [VectorMath](/docs/nodes/VectorMath.md), vector (Vector)

## Random

> Node: [RandomValue](/docs/nodes/RandomValue.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/random_value.html) </sub>

```python
v = Vector.Random(min, max, ID, seed)
```

### Arguments


#### Sockets

- min : Vector
- max : Vector
- ID : Integer
- seed : Integer

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR')
```

### Returns

Vector


## Combine

> Node: [CombineXyz](/docs/nodes/CombineXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeCombineXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
node ref [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/combine_xyz.html) </sub>

```python
v = Vector.Combine(x, y, z)
```

### Arguments


#### Sockets

- x : Float
- y : Float
- z : Float

### Node creation

```python
nodes.CombineXyz(x=x, y=y, z=z)
```

### Returns

Vector


## AlignToVector

> Node: [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
node ref [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/align_euler_to_vector.html) </sub>

```python
v = Vector.AlignToVector(rotation, factor, vector, axis, pivot_axis)
```

### Arguments


#### Sockets

- rotation : Vector
- factor : Float
- vector : Vector

#### Parameters

- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]

### Node creation

```python
nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
```

### Returns

Vector


## separate

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_xyz.html) </sub>

```python
v = vector.separate
```

### Arguments


#### Sockets

- vector : Vector (self)

#### Fixed parameters

- label:f"{self.node_chain_label}.separate"

### Node creation

```python
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## x

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_xyz.html) </sub>

```python
v = vector.x
```

### Arguments


#### Sockets

- vector : Vector (self)

#### Fixed parameters

- label:f"{self.node_chain_label}.x"

### Node creation

```python
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.x")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## y

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_xyz.html) </sub>

```python
v = vector.y
```

### Arguments


#### Sockets

- vector : Vector (self)

#### Fixed parameters

- label:f"{self.node_chain_label}.y"

### Node creation

```python
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.y")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## z

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/separate_xyz.html) </sub>

```python
v = vector.z
```

### Arguments


#### Sockets

- vector : Vector (self)

#### Fixed parameters

- label:f"{self.node_chain_label}.z"

### Node creation

```python
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.z")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## accumulate_field

> Node: [AccumulateField](/docs/nodes/AccumulateField.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
node ref [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/accumulate_field.html) </sub>

```python
v = vector.accumulate_field(group_index, domain)
```

### Arguments


#### Sockets

- value : Vector (self)
- group_index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)
```

### Returns

Sockets [leading (Vector), trailing (Vector), total (Vector)]


## attribute_statistic

> Node: [AttributeStatistic](/docs/nodes/AttributeStatistic.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
node ref [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/attribute_statistic.html) </sub>

```python
v = vector.attribute_statistic(geometry, selection, domain)
```

### Arguments


#### Sockets

- attribute : Vector (self)
- geometry : Geometry
- selection : Boolean

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain)
```

### Returns

Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]


## transfer_attribute

> Node: [TransferAttribute](/docs/nodes/TransferAttribute.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeAttributeTransfer](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeTransfer.html)
node ref [Transfer Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/transfer_attribute.html) </sub>

```python
v = vector.transfer_attribute(source, source_position, index, domain, mapping)
```

### Arguments


#### Sockets

- attribute : Vector (self)
- source : Geometry
- source_position : Vector
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping)
```

### Returns

Vector


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/capture_attribute.html) </sub>

```python
v = vector.capture_attribute(geometry, domain)
```

### Arguments


#### Sockets

- value : Vector (self)
- geometry : Geometry

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain)
```

### Returns

Sockets [geometry (Geometry), attribute (Vector)]


## field_at_index

> Node: [FieldAtIndex](/docs/nodes/FieldAtIndex.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/field_at_index.html) </sub>

```python
v = vector.field_at_index(index, domain)
```

### Arguments


#### Sockets

- value : Vector (self)
- index : Integer

#### Parameters

- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain)
```

### Returns

Vector


## raycast

> Node: [Raycast](/docs/nodes/Raycast.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/raycast.html) </sub>

```python
v = vector.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```

### Arguments


#### Sockets

- attribute : Vector (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float

#### Parameters

- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]


## map_range

> Node: [MapRange](/docs/nodes/MapRange.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
node ref [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/map_range.html) </sub>

```python
v = vector.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type)
```

### Arguments


#### Sockets

- vector : Vector (self)
- from_min : Vector
- from_max : Vector
- to_min : Vector
- to_max : Vector

#### Parameters

- clamp : True
- interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]

#### Fixed parameters

- data_type : 'FLOAT_VECTOR'

### Node creation

```python
nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type)
```

### Returns

Vector


## less_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.less_than(b, c, angle, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'LESS_THAN'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN')
```

### Returns

Boolean


## less_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.less_equal(b, c, angle, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'LESS_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL')
```

### Returns

Boolean


## greater_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.greater_than(b, c, angle, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'GREATER_THAN'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN')
```

### Returns

Boolean


## greater_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.greater_equal(b, c, angle, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'GREATER_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL')
```

### Returns

Boolean


## equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.equal(b, c, angle, epsilon, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL')
```

### Returns

Boolean


## not_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/compare.html) </sub>

```python
v = vector.not_equal(b, c, angle, epsilon, mode)
```

### Arguments


#### Sockets

- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float

#### Parameters

- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]

#### Fixed parameters

- data_type : 'VECTOR'
- operation : 'NOT_EQUAL'

### Node creation

```python
nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL')
```

### Returns

Boolean


## add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.add(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'ADD'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD')
```

### Returns

Vector


## subtract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.subtract(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'SUBTRACT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT')
```

### Returns

Vector


## multiply

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.multiply(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'MULTIPLY'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY')
```

### Returns

Vector


## divide

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.divide(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'DIVIDE'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE')
```

### Returns

Vector


## multiply_add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.multiply_add(vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'MULTIPLY_ADD'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD')
```

### Returns

Vector


## cross

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.cross(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'CROSS_PRODUCT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT')
```

### Returns

Vector


## project

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.project(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'PROJECT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT')
```

### Returns

Vector


## reflect

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.reflect(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'REFLECT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT')
```

### Returns

Vector


## refract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.refract(vector1, scale)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector
- scale : Float

#### Fixed parameters

- operation : 'REFRACT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT')
```

### Returns

Vector


## faceforward

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.faceforward(vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'FACEFORWARD'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD')
```

### Returns

Vector


## dot

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.dot(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'DOT_PRODUCT'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT')
```

### Returns

Float


## distance

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.distance(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'DISTANCE'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE')
```

### Returns

Float


## length

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.length()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'LENGTH'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='LENGTH')
```

### Returns

Float


## scale

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.scale(scale)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- scale : Float

#### Fixed parameters

- operation : 'SCALE'

### Node creation

```python
nodes.VectorMath(vector0=self, scale=scale, operation='SCALE')
```

### Returns

Vector


## normalize

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.normalize()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'NORMALIZE'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='NORMALIZE')
```

### Returns

Vector


## absolute

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.absolute()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'ABSOLUTE'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='ABSOLUTE')
```

### Returns

Vector


## min

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.min(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'MINIMUM'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM')
```

### Returns

Vector


## max

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.max(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'MAXIMUM'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM')
```

### Returns

Vector


## floor

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.floor()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'FLOOR'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='FLOOR')
```

### Returns

Vector


## ceil

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.ceil()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'CEIL'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='CEIL')
```

### Returns

Vector


## fraction

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.fraction()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'FRACTION'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='FRACTION')
```

### Returns

Vector


## modulo

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.modulo(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'MODULO'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO')
```

### Returns

Vector


## wrap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.wrap(vector1, vector2)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector

#### Fixed parameters

- operation : 'WRAP'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP')
```

### Returns

Vector


## snap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.snap(vector1)
```

### Arguments


#### Sockets

- vector0 : Vector (self)
- vector1 : Vector

#### Fixed parameters

- operation : 'SNAP'

### Node creation

```python
nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP')
```

### Returns

Vector


## sin

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.sin()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'SINE'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='SINE')
```

### Returns

Vector


## cos

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.cos()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'COSINE'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='COSINE')
```

### Returns

Vector


## tan

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_math.html) </sub>

```python
v = vector.tan()
```

### Arguments


#### Sockets

- vector0 : Vector (self)

#### Fixed parameters

- operation : 'TANGENT'

### Node creation

```python
nodes.VectorMath(vector0=self, operation='TANGENT')
```

### Returns

Vector


## curves

> Node: [VectorCurves](/docs/nodes/VectorCurves.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
node ref [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_curves.html) </sub>

```python
v = vector.curves(fac)
```

### Arguments


#### Sockets

- vector : Vector (self)
- fac : Float

### Node creation

```python
nodes.VectorCurves(vector=self, fac=fac)
```

### Returns

Vector


## align_to_vector

> Node: [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
node ref [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/align_euler_to_vector.html) </sub>

```python
v = vector.align_to_vector(factor, vector, axis, pivot_axis)
```

### Arguments


#### Sockets

- rotation : Vector (self)
- factor : Float
- vector : Vector

#### Parameters

- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]

### Node creation

```python
nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
```

### Returns

Vector


## rotate_euler

> Node: [RotateEuler](/docs/nodes/RotateEuler.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeRotateEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
node ref [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/rotate_euler.html) </sub>

```python
v = vector.rotate_euler(rotate_by, space)
```

### Arguments


#### Sockets

- rotation : Vector (self)
- rotate_by : Vector

#### Parameters

- space : 'OBJECT' in [OBJECT, LOCAL]

### Node creation

```python
nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space)
```

### Returns

Vector


## rotate

> Node: [VectorRotate](/docs/nodes/VectorRotate.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
node ref [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/vector_rotate.html) </sub>

```python
v = vector.rotate(center, axis, angle, rotation, invert, rotation_type)
```

### Arguments


#### Sockets

- vector : Vector (self)
- center : Vector
- axis : Vector
- angle : Float
- rotation : Vector

#### Parameters

- invert : False
- rotation_type : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]

### Node creation

```python
nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type)
```

### Returns

Vector

