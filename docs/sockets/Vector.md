
# Data socket Vector

> Inherits from dsock.Vector
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [AlignToVector](#aligntovector) : rotation (Vector)
- [Combine](#combine) : vector (Vector)
- [Random](#random) : value (Vector)

## Properties

- [separate](#separate) : Sockets      [x (Float), y (Float), z (Float)]
- [x](#x) : x (Float) = separate.x
- [y](#y) : y (Float) = separate.y
- [z](#z) : z (Float) = separate.z

## Methods

- [absolute](#absolute) : vector (Vector)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Vector), trailing (Vector), total (Vector)]
- [add](#add) : vector (Vector)
- [align_to_vector](#align_to_vector) : rotation (Vector)
- [attribute_statistic](#attribute_statistic) : Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Vector)]
- [ceil](#ceil) : vector (Vector)
- [cos](#cos) : vector (Vector)
- [cross](#cross) : vector (Vector)
- [curves](#curves) : vector (Vector)
- [distance](#distance) : value (Float)
- [divide](#divide) : vector (Vector)
- [dot](#dot) : value (Float)
- [equal](#equal) : result (Boolean)
- [faceforward](#faceforward) : vector (Vector)
- [field_at_index](#field_at_index) : value (Vector)
- [floor](#floor) : vector (Vector)
- [fraction](#fraction) : vector (Vector)
- [greater_equal](#greater_equal) : result (Boolean)
- [greater_than](#greater_than) : result (Boolean)
- [length](#length) : value (Float)
- [less_equal](#less_equal) : result (Boolean)
- [less_than](#less_than) : result (Boolean)
- [map_range](#map_range) : vector (Vector)
- [max](#max) : vector (Vector)
- [min](#min) : vector (Vector)
- [modulo](#modulo) : vector (Vector)
- [multiply](#multiply) : vector (Vector)
- [multiply_add](#multiply_add) : vector (Vector)
- [normalize](#normalize) : vector (Vector)
- [not_equal](#not_equal) : result (Boolean)
- [project](#project) : vector (Vector)
- [raycast](#raycast) : Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
- [reflect](#reflect) : vector (Vector)
- [refract](#refract) : vector (Vector)
- [rotate](#rotate) : vector (Vector)
- [rotate_euler](#rotate_euler) : rotation (Vector)
- [scale](#scale) : vector (Vector)
- [sin](#sin) : vector (Vector)
- [snap](#snap) : vector (Vector)
- [subtract](#subtract) : vector (Vector)
- [tan](#tan) : vector (Vector)
- [wrap](#wrap) : vector (Vector)

## Random

> Node: [RandomValue](/docs/nodes/RandomValue.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
node ref [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) </sub>
                          
```python
v = Vector.Random(min, max, ID, seed, node_label = None, node_color = None)
```

### Arguments

## Sockets
- min : Vector
- max : Vector
- ID : Integer
- seed : Integer## Parameters
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR', label=node_label, node_color=node_color)
```

### Returns

Vector


## Combine

> Node: [CombineXyz](/docs/nodes/CombineXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeCombineXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
node ref [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/combine_xyz.html) </sub>
                          
```python
v = Vector.Combine(x, y, z, node_label = None, node_color = None)
```

### Arguments

## Sockets
- x : Float
- y : Float
- z : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.CombineXyz(x=x, y=y, z=z, label=node_label, node_color=node_color)
```

### Returns

Vector


## AlignToVector

> Node: [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
node ref [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) </sub>
                          
```python
v = Vector.AlignToVector(rotation, factor, vector, axis, pivot_axis, node_label = None, node_color = None)
```

### Arguments

## Sockets
- rotation : Vector
- factor : Float
- vector : Vector## Parameters
- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
```

### Returns

Vector


## separate

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) </sub>
                          
```python
v = vector.separate
```

### Arguments

## Sockets
- vector : Vector (self)## Fixed parameters
- label:f"{self.node_chain_label}.separate"

### Node creation

```python
from geondes import nodes
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## x

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) </sub>
                          
```python
v = vector.x
```

### Arguments

## Sockets
- vector : Vector (self)## Fixed parameters
- label:f"{self.node_chain_label}.x"

### Node creation

```python
from geondes import nodes
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.x")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## y

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) </sub>
                          
```python
v = vector.y
```

### Arguments

## Sockets
- vector : Vector (self)## Fixed parameters
- label:f"{self.node_chain_label}.y"

### Node creation

```python
from geondes import nodes
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.y")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## z

> Node: [SeparateXyz](/docs/nodes/SeparateXyz.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeSeparateXYZ](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
node ref [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/separate_xyz.html) </sub>
                          
```python
v = vector.z
```

### Arguments

## Sockets
- vector : Vector (self)## Fixed parameters
- label:f"{self.node_chain_label}.z"

### Node creation

```python
from geondes import nodes
nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.z")
```

### Returns

Sockets [x (Float), y (Float), z (Float)]


## accumulate_field

> Node: [AccumulateField](/docs/nodes/AccumulateField.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
node ref [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) </sub>
                          
```python
v = vector.accumulate_field(group_index, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Vector (self)
- group_index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [leading (Vector), trailing (Vector), total (Vector)]


## attribute_statistic

> Node: [AttributeStatistic](/docs/nodes/AttributeStatistic.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
node ref [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) </sub>
                          
```python
v = vector.attribute_statistic(geometry, selection, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Vector (self)
- geometry : Geometry
- selection : Boolean## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]


## capture_attribute

> Node: [CaptureAttribute](/docs/nodes/CaptureAttribute.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
node ref [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) </sub>
                          
```python
v = vector.capture_attribute(geometry, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Vector (self)
- geometry : Geometry## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Sockets [geometry (Geometry), attribute (Vector)]


## field_at_index

> Node: [FieldAtIndex](/docs/nodes/FieldAtIndex.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
node ref [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) </sub>
                          
```python
v = vector.field_at_index(index, domain, node_label = None, node_color = None)
```

### Arguments

## Sockets
- value : Vector (self)
- index : Integer## Parameters
- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain, label=node_label, node_color=node_color)
```

### Returns

Vector


## raycast

> Node: [Raycast](/docs/nodes/Raycast.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
node ref [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) </sub>
                          
```python
v = vector.raycast(target_geometry, source_position, ray_direction, ray_length, mapping, node_label = None, node_color = None)
```

### Arguments

## Sockets
- attribute : Vector (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float## Parameters
- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping, label=node_label, node_color=node_color)
```

### Returns

Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]


## map_range

> Node: [MapRange](/docs/nodes/MapRange.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeMapRange](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
node ref [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/map_range.html) </sub>
                          
```python
v = vector.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector : Vector (self)
- from_min : Vector
- from_max : Vector
- to_min : Vector
- to_max : Vector## Parameters
- clamp : True
- interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'FLOAT_VECTOR'

### Node creation

```python
from geondes import nodes
nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type, label=node_label, node_color=node_color)
```

### Returns

Vector


## less_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.less_than(b, c, angle, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'LESS_THAN'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## less_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.less_equal(b, c, angle, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'LESS_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## greater_than

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.greater_than(b, c, angle, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'GREATER_THAN'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN', label=node_label, node_color=node_color)
```

### Returns

Boolean


## greater_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.greater_equal(b, c, angle, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'GREATER_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.equal(b, c, angle, epsilon, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## not_equal

> Node: [Compare](/docs/nodes/Compare.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeCompare](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
node ref [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/compare.html) </sub>
                          
```python
v = vector.not_equal(b, c, angle, epsilon, mode, node_label = None, node_color = None)
```

### Arguments

## Sockets
- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float## Parameters
- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]
- node_label : None
- node_color : None## Fixed parameters
- data_type : 'VECTOR'
- operation : 'NOT_EQUAL'

### Node creation

```python
from geondes import nodes
nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL', label=node_label, node_color=node_color)
```

### Returns

Boolean


## add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.add(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ADD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD', label=node_label, node_color=node_color)
```

### Returns

Vector


## subtract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.subtract(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SUBTRACT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT', label=node_label, node_color=node_color)
```

### Returns

Vector


## multiply

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.multiply(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MULTIPLY'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY', label=node_label, node_color=node_color)
```

### Returns

Vector


## divide

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.divide(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DIVIDE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE', label=node_label, node_color=node_color)
```

### Returns

Vector


## multiply_add

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.multiply_add(vector1, vector2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MULTIPLY_ADD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD', label=node_label, node_color=node_color)
```

### Returns

Vector


## cross

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.cross(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'CROSS_PRODUCT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT', label=node_label, node_color=node_color)
```

### Returns

Vector


## project

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.project(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'PROJECT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT', label=node_label, node_color=node_color)
```

### Returns

Vector


## reflect

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.reflect(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'REFLECT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT', label=node_label, node_color=node_color)
```

### Returns

Vector


## refract

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.refract(vector1, scale, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector
- scale : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'REFRACT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT', label=node_label, node_color=node_color)
```

### Returns

Vector


## faceforward

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.faceforward(vector1, vector2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'FACEFORWARD'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD', label=node_label, node_color=node_color)
```

### Returns

Vector


## dot

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.dot(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DOT_PRODUCT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT', label=node_label, node_color=node_color)
```

### Returns

Float


## distance

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.distance(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'DISTANCE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE', label=node_label, node_color=node_color)
```

### Returns

Float


## length

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.length(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'LENGTH'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='LENGTH', label=node_label, node_color=node_color)
```

### Returns

Float


## scale

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.scale(scale, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- scale : Float## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SCALE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, scale=scale, operation='SCALE', label=node_label, node_color=node_color)
```

### Returns

Vector


## normalize

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.normalize(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'NORMALIZE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='NORMALIZE', label=node_label, node_color=node_color)
```

### Returns

Vector


## absolute

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.absolute(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'ABSOLUTE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='ABSOLUTE', label=node_label, node_color=node_color)
```

### Returns

Vector


## min

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.min(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MINIMUM'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM', label=node_label, node_color=node_color)
```

### Returns

Vector


## max

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.max(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MAXIMUM'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM', label=node_label, node_color=node_color)
```

### Returns

Vector


## floor

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.floor(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'FLOOR'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='FLOOR', label=node_label, node_color=node_color)
```

### Returns

Vector


## ceil

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.ceil(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'CEIL'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='CEIL', label=node_label, node_color=node_color)
```

### Returns

Vector


## fraction

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.fraction(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'FRACTION'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='FRACTION', label=node_label, node_color=node_color)
```

### Returns

Vector


## modulo

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.modulo(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'MODULO'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO', label=node_label, node_color=node_color)
```

### Returns

Vector


## wrap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.wrap(vector1, vector2, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'WRAP'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP', label=node_label, node_color=node_color)
```

### Returns

Vector


## snap

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.snap(vector1, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)
- vector1 : Vector## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SNAP'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP', label=node_label, node_color=node_color)
```

### Returns

Vector


## sin

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.sin(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'SINE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='SINE', label=node_label, node_color=node_color)
```

### Returns

Vector


## cos

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.cos(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'COSINE'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='COSINE', label=node_label, node_color=node_color)
```

### Returns

Vector


## tan

> Node: [VectorMath](/docs/nodes/VectorMath.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorMath](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
node ref [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_math.html) </sub>
                          
```python
v = vector.tan(node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector0 : Vector (self)## Parameters
- node_label : None
- node_color : None## Fixed parameters
- operation : 'TANGENT'

### Node creation

```python
from geondes import nodes
nodes.VectorMath(vector0=self, operation='TANGENT', label=node_label, node_color=node_color)
```

### Returns

Vector


## curves

> Node: [VectorCurves](/docs/nodes/VectorCurves.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorCurve](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
node ref [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_curves.html) </sub>
                          
```python
v = vector.curves(fac, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector : Vector (self)
- fac : Float## Parameters
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.VectorCurves(vector=self, fac=fac, label=node_label, node_color=node_color)
```

### Returns

Vector


## align_to_vector

> Node: [AlignEulerToVector](/docs/nodes/AlignEulerToVector.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeAlignEulerToVector](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
node ref [Align Euler to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html) </sub>
                          
```python
v = vector.align_to_vector(factor, vector, axis, pivot_axis, node_label = None, node_color = None)
```

### Arguments

## Sockets
- rotation : Vector (self)
- factor : Float
- vector : Vector## Parameters
- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis, label=node_label, node_color=node_color)
```

### Returns

Vector


## rotate_euler

> Node: [RotateEuler](/docs/nodes/RotateEuler.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [FunctionNodeRotateEuler](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
node ref [Rotate Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html) </sub>
                          
```python
v = vector.rotate_euler(rotate_by, space, node_label = None, node_color = None)
```

### Arguments

## Sockets
- rotation : Vector (self)
- rotate_by : Vector## Parameters
- space : 'OBJECT' in [OBJECT, LOCAL]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space, label=node_label, node_color=node_color)
```

### Returns

Vector


## rotate

> Node: [VectorRotate](/docs/nodes/VectorRotate.md)
  
<sub>go to: [top](#data-socket-vector) [index](/docs/index.md)
blender ref [ShaderNodeVectorRotate](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
node ref [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html) </sub>
                          
```python
v = vector.rotate(center, axis, angle, rotation, invert, rotation_type, node_label = None, node_color = None)
```

### Arguments

## Sockets
- vector : Vector (self)
- center : Vector
- axis : Vector
- angle : Float
- rotation : Vector## Parameters
- invert : False
- rotation_type : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]
- node_label : None
- node_color : None

### Node creation

```python
from geondes import nodes
nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type, label=node_label, node_color=node_color)
```

### Returns

Vector

