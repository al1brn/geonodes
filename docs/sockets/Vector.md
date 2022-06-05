
# Class Vector

> Inherits from: ***dsock.Vector***

## Constructors



- [AlignToVector](#aligntovector) : rotation (Vector)
- [Combine](#combine) : vector (Vector)
- [Random](#random) : value (Vector)



## Properties



- [separate](#separate) : Sockets      [x (Float), y (Float), z (Float)]



## Methods



- [absolute](#absolute) : vector (Vector)
- [accumulate_field](#accumulate_field) : Sockets      [leading (Vector), trailing (Vector), total (Vector)]
- [add](#add) : vector (Vector)
- [attribute_statistic](#attribute_statistic) : Sockets      [mean (Vector), median (Vector), sum (Vector), min (Vector), max (Vector), range (Vector), standard_deviation (Vector), variance (Vector)]
- [capture_attribute](#capture_attribute) : Sockets      [geometry (Geometry), attribute (Vector)]
- [ceil](#ceil) : vector (Vector)
- [cos](#cos) : vector (Vector)
- [cross](#cross) : vector (Vector)
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
- [scale](#scale) : vector (Vector)
- [sin](#sin) : vector (Vector)
- [snap](#snap) : vector (Vector)
- [subtract](#subtract) : vector (Vector)
- [tan](#tan) : vector (Vector)
- [transfer_attribute](#transfer_attribute) : attribute (Vector)
- [wrap](#wrap) : vector (Vector)



## Stacked methods



- [align_to_vector](#align_to_vector) : Vector
- [curves](#curves) : Vector
- [rotate_euler](#rotate_euler) : Vector



## Methods


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



#### Returns

    Vector
