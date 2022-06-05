
# Class Vector

> Inherits from: ***dsock.Vector***

## Constructors



- [AlignToVector](#aligntovector) : [AlignEulerToVector](../nodes/AlignEulerToVector.md) rotation (Vector)
- [Combine](#combine) : [CombineXyz](../nodes/CombineXyz.md) vector (Vector)
- [Random](#random) : [RandomValue](../nodes/RandomValue.md) value (Vector)



## Properties



- [separate](#separate) : [SeparateXyz](../nodes/SeparateXyz.md) Sockets      [x (Float), y (Float), z (Float)]



## Methods



- [absolute](#absolute) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [accumulate_field](#accumulate_field) : [AccumulateField](../nodes/AccumulateField.md) Sockets      [leading (Vector), trailing (Vector), total (Vector)]
- [add](#add) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [attribute_statistic](#attribute_statistic) : [AttributeStatistic](../nodes/AttributeStatistic.md) Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
- [capture_attribute](#capture_attribute) : [CaptureAttribute](../nodes/CaptureAttribute.md) Sockets      [geometry (Geometry), attribute (Vector)]
- [ceil](#ceil) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [cos](#cos) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [cross](#cross) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [distance](#distance) : [VectorMath](../nodes/VectorMath.md) value (Float)
- [divide](#divide) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [dot](#dot) : [VectorMath](../nodes/VectorMath.md) value (Float)
- [equal](#equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [faceforward](#faceforward) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [field_at_index](#field_at_index) : [FieldAtIndex](../nodes/FieldAtIndex.md) value (Vector)
- [floor](#floor) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [fraction](#fraction) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [greater_equal](#greater_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [greater_than](#greater_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [length](#length) : [VectorMath](../nodes/VectorMath.md) value (Float)
- [less_equal](#less_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [less_than](#less_than) : [Compare](../nodes/Compare.md) result (Boolean)
- [map_range](#map_range) : [MapRange](../nodes/MapRange.md) vector (Vector)
- [max](#max) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [min](#min) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [modulo](#modulo) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [multiply](#multiply) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [multiply_add](#multiply_add) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [normalize](#normalize) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [not_equal](#not_equal) : [Compare](../nodes/Compare.md) result (Boolean)
- [project](#project) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [raycast](#raycast) : [Raycast](../nodes/Raycast.md) Sockets      [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]
- [reflect](#reflect) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [refract](#refract) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [rotate](#rotate) : [VectorRotate](../nodes/VectorRotate.md) vector (Vector)
- [scale](#scale) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [sin](#sin) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [snap](#snap) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [subtract](#subtract) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [tan](#tan) : [VectorMath](../nodes/VectorMath.md) vector (Vector)
- [transfer_attribute](#transfer_attribute) : [TransferAttribute](../nodes/TransferAttribute.md) attribute (Vector)
- [wrap](#wrap) : [VectorMath](../nodes/VectorMath.md) vector (Vector)



## Stacked methods



- [align_to_vector](#align_to_vector) : [AlignEulerToVector](../nodes/AlignEulerToVector.md) Vector
- [curves](#curves) : [VectorCurves](../nodes/VectorCurves.md) Vector
- [rotate_euler](#rotate_euler) : [RotateEuler](../nodes/RotateEuler.md) Vector



## Methods reference


### AlignToVector

> Node: [AlignEulerToVector](../nodes/{self.node_name}.md)

```python
v = Vector.AlignToVector(rotation, factor, vector, axis, pivot_axis)
```


#### Arguments


##### Sockets arguments



- rotation : Vector
- factor : Float
- vector : Vector



##### Parameters arguments



- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]



#### Node creation


```python
node = nodes.AlignEulerToVector(rotation=rotation, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
```


#### Returns

    Vector

### Combine

> Node: [CombineXyz](../nodes/{self.node_name}.md)

```python
v = Vector.Combine(x, y, z)
```


#### Arguments


##### Sockets arguments



- x : Float
- y : Float
- z : Float



#### Node creation


```python
node = nodes.CombineXyz(x=x, y=y, z=z)
```


#### Returns

    Vector

### Random

> Node: [RandomValue](../nodes/{self.node_name}.md)

```python
v = Vector.Random(min, max, ID, seed)
```


#### Arguments


##### Sockets arguments



- min : Vector
- max : Vector
- ID : Integer
- seed : Integer



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



#### Node creation


```python
node = nodes.RandomValue(min=min, max=max, ID=ID, seed=seed, data_type='FLOAT_VECTOR')
```


#### Returns

    Vector

### absolute

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.absolute()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'ABSOLUTE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='ABSOLUTE')
```


#### Returns

    Vector

### accumulate_field

> Node: [AccumulateField](../nodes/{self.node_name}.md)

```python
v = vector.accumulate_field(group_index, domain)
```


#### Arguments


##### Sockets arguments



- value : Vector (self)
- group_index : Integer



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.AccumulateField(value=self, group_index=group_index, data_type='FLOAT_VECTOR', domain=domain)
```


#### Returns

    Sockets [leading (Vector), trailing (Vector), total (Vector)]

### add

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.add(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'ADD'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='ADD')
```


#### Returns

    Vector

### align_to_vector

> Node: [AlignEulerToVector](../nodes/{self.node_name}.md)

```python
vector.align_to_vector(factor, vector, axis, pivot_axis)
```


#### Arguments


##### Sockets arguments



- rotation : Vector (self)
- factor : Float
- vector : Vector



##### Parameters arguments



- axis : 'X' in [X, Y, Z]
- pivot_axis : 'AUTO' in [AUTO, X, Y, Z]



#### Node creation


```python
node = nodes.AlignEulerToVector(rotation=self, factor=factor, vector=vector, axis=axis, pivot_axis=pivot_axis)
```


#### Returns

    self

### attribute_statistic

> Node: [AttributeStatistic](../nodes/{self.node_name}.md)

```python
v = vector.attribute_statistic(geometry, selection, domain)
```


#### Arguments


##### Sockets arguments



- attribute : Vector (self)
- geometry : Geometry
- selection : Boolean



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.AttributeStatistic(attribute=self, geometry=geometry, selection=selection, data_type='FLOAT_VECTOR', domain=domain)
```


#### Returns

    Sockets [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]

### capture_attribute

> Node: [CaptureAttribute](../nodes/{self.node_name}.md)

```python
v = vector.capture_attribute(geometry, domain)
```


#### Arguments


##### Sockets arguments



- value : Vector (self)
- geometry : Geometry



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.CaptureAttribute(value=self, geometry=geometry, data_type='FLOAT_VECTOR', domain=domain)
```


#### Returns

    Sockets [geometry (Geometry), attribute (Vector)]

### ceil

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.ceil()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'CEIL'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='CEIL')
```


#### Returns

    Vector

### cos

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.cos()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'COSINE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='COSINE')
```


#### Returns

    Vector

### cross

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.cross(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'CROSS_PRODUCT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='CROSS_PRODUCT')
```


#### Returns

    Vector

### curves

> Node: [VectorCurves](../nodes/{self.node_name}.md)

```python
vector.curves(fac)
```


#### Arguments


##### Sockets arguments



- vector : Vector (self)
- fac : Float



#### Node creation


```python
node = nodes.VectorCurves(vector=self, fac=fac)
```


#### Returns

    self

### distance

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.distance(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'DISTANCE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DISTANCE')
```


#### Returns

    Float

### divide

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.divide(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'DIVIDE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DIVIDE')
```


#### Returns

    Vector

### dot

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.dot(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'DOT_PRODUCT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='DOT_PRODUCT')
```


#### Returns

    Float

### equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.equal(b, c, angle, epsilon, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'EQUAL'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='EQUAL')
```


#### Returns

    Boolean

### faceforward

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.faceforward(vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'FACEFORWARD'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='FACEFORWARD')
```


#### Returns

    Vector

### field_at_index

> Node: [FieldAtIndex](../nodes/{self.node_name}.md)

```python
v = vector.field_at_index(index, domain)
```


#### Arguments


##### Sockets arguments



- value : Vector (self)
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]



#### Node creation


```python
node = nodes.FieldAtIndex(value=self, index=index, data_type='FLOAT_VECTOR', domain=domain)
```


#### Returns

    Vector

### floor

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.floor()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'FLOOR'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='FLOOR')
```


#### Returns

    Vector

### fraction

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.fraction()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'FRACTION'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='FRACTION')
```


#### Returns

    Vector

### greater_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.greater_equal(b, c, angle, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'GREATER_EQUAL'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_EQUAL')
```


#### Returns

    Boolean

### greater_than

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.greater_than(b, c, angle, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'GREATER_THAN'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='GREATER_THAN')
```


#### Returns

    Boolean

### length

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.length()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'LENGTH'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='LENGTH')
```


#### Returns

    Float

### less_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.less_equal(b, c, angle, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'LESS_EQUAL'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_EQUAL')
```


#### Returns

    Boolean

### less_than

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.less_than(b, c, angle, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'LESS_THAN'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, data_type='VECTOR', mode=mode, operation='LESS_THAN')
```


#### Returns

    Boolean

### map_range

> Node: [MapRange](../nodes/{self.node_name}.md)

```python
v = vector.map_range(from_min, from_max, to_min, to_max, clamp, interpolation_type)
```


#### Arguments


##### Sockets arguments



- vector : Vector (self)
- from_min : Vector
- from_max : Vector
- to_min : Vector
- to_max : Vector



##### Parameters arguments



- clamp : True
- interpolation_type : 'LINEAR' in [LINEAR, STEPPED, SMOOTHSTEP, SMOOTHERSTEP]



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



#### Node creation


```python
node = nodes.MapRange(vector=self, from_min=from_min, from_max=from_max, to_min=to_min, to_max=to_max, clamp=clamp, data_type='FLOAT_VECTOR', interpolation_type=interpolation_type)
```


#### Returns

    Vector

### max

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.max(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'MAXIMUM'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MAXIMUM')
```


#### Returns

    Vector

### min

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.min(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'MINIMUM'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MINIMUM')
```


#### Returns

    Vector

### modulo

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.modulo(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'MODULO'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MODULO')
```


#### Returns

    Vector

### multiply

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.multiply(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'MULTIPLY'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='MULTIPLY')
```


#### Returns

    Vector

### multiply_add

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.multiply_add(vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'MULTIPLY_ADD'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='MULTIPLY_ADD')
```


#### Returns

    Vector

### normalize

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.normalize()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'NORMALIZE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='NORMALIZE')
```


#### Returns

    Vector

### not_equal

> Node: [Compare](../nodes/{self.node_name}.md)

```python
v = vector.not_equal(b, c, angle, epsilon, mode)
```


#### Arguments


##### Sockets arguments



- a : Vector (self)
- b : Vector
- c : Float
- angle : Float
- epsilon : Float



##### Fixed parameters



- data_type : 'VECTOR'
- operation : 'NOT_EQUAL'



##### Parameters arguments



- mode : 'ELEMENT' in [ELEMENT, LENGTH, AVERAGE, DOT_PRODUCT, DIRECTION]



#### Node creation


```python
node = nodes.Compare(a=self, b=b, c=c, angle=angle, epsilon=epsilon, data_type='VECTOR', mode=mode, operation='NOT_EQUAL')
```


#### Returns

    Boolean

### project

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.project(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'PROJECT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='PROJECT')
```


#### Returns

    Vector

### raycast

> Node: [Raycast](../nodes/{self.node_name}.md)

```python
v = vector.raycast(target_geometry, source_position, ray_direction, ray_length, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Vector (self)
- target_geometry : Geometry
- source_position : Vector
- ray_direction : Vector
- ray_length : Float



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- mapping : 'INTERPOLATED' in [INTERPOLATED, NEAREST]



#### Node creation


```python
node = nodes.Raycast(attribute=self, target_geometry=target_geometry, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type='FLOAT_VECTOR', mapping=mapping)
```


#### Returns

    Sockets [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Vector)]

### reflect

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.reflect(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'REFLECT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='REFLECT')
```


#### Returns

    Vector

### refract

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.refract(vector1, scale)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector
- scale : Float



##### Fixed parameters



- operation : 'REFRACT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, scale=scale, operation='REFRACT')
```


#### Returns

    Vector

### rotate

> Node: [VectorRotate](../nodes/{self.node_name}.md)

```python
v = vector.rotate(center, axis, angle, rotation, invert, rotation_type)
```


#### Arguments


##### Sockets arguments



- vector : Vector (self)
- center : Vector
- axis : Vector
- angle : Float
- rotation : Vector



##### Parameters arguments



- invert : False
- rotation_type : 'AXIS_ANGLE' in [AXIS_ANGLE, X_AXIS, Y_AXIS, Z_AXIS, EULER_XYZ]



#### Node creation


```python
node = nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=rotation, invert=invert, rotation_type=rotation_type)
```


#### Returns

    Vector

### rotate_euler

> Node: [RotateEuler](../nodes/{self.node_name}.md)

```python
vector.rotate_euler(rotate_by, space)
```


#### Arguments


##### Sockets arguments



- rotation : Vector (self)
- rotate_by : Vector



##### Parameters arguments



- space : 'OBJECT' in [OBJECT, LOCAL]



#### Node creation


```python
node = nodes.RotateEuler(rotation=self, rotate_by=rotate_by, space=space)
```


#### Returns

    self

### scale

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.scale(scale)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- scale : Float



##### Fixed parameters



- operation : 'SCALE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, scale=scale, operation='SCALE')
```


#### Returns

    Vector

### separate

> Node: [SeparateXyz](../nodes/{self.node_name}.md)

```python
v = vector.separate
```


#### Arguments


##### Sockets arguments



- vector : Vector (self)



##### Fixed parameters



- label:f"{self.node_chain_label}.separate"



#### Node creation


```python
node = nodes.SeparateXyz(vector=self, label=f"{self.node_chain_label}.separate")
```


#### Returns

    Sockets [x (Float), y (Float), z (Float)]

### sin

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.sin()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'SINE'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='SINE')
```


#### Returns

    Vector

### snap

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.snap(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'SNAP'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='SNAP')
```


#### Returns

    Vector

### subtract

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.subtract(vector1)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector



##### Fixed parameters



- operation : 'SUBTRACT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, operation='SUBTRACT')
```


#### Returns

    Vector

### tan

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.tan()
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)



##### Fixed parameters



- operation : 'TANGENT'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, operation='TANGENT')
```


#### Returns

    Vector

### transfer_attribute

> Node: [TransferAttribute](../nodes/{self.node_name}.md)

```python
v = vector.transfer_attribute(source, source_position, index, domain, mapping)
```


#### Arguments


##### Sockets arguments



- attribute : Vector (self)
- source : Geometry
- source_position : Vector
- index : Integer



##### Fixed parameters



- data_type : 'FLOAT_VECTOR'



##### Parameters arguments



- domain : 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]
- mapping : 'NEAREST_FACE_INTERPOLATED' in [NEAREST_FACE_INTERPOLATED, NEAREST, INDEX]



#### Node creation


```python
node = nodes.TransferAttribute(attribute=self, source=source, source_position=source_position, index=index, data_type='FLOAT_VECTOR', domain=domain, mapping=mapping)
```


#### Returns

    Vector

### wrap

> Node: [VectorMath](../nodes/{self.node_name}.md)

```python
v = vector.wrap(vector1, vector2)
```


#### Arguments


##### Sockets arguments



- vector0 : Vector (self)
- vector1 : Vector
- vector2 : Vector



##### Fixed parameters



- operation : 'WRAP'



#### Node creation


```python
node = nodes.VectorMath(vector0=self, vector1=vector1, vector2=vector2, operation='WRAP')
```


#### Returns

    Vector
