
# Class Spline

> Inherits from: ***Geometry***

## Attribute capture



- capture_cyclic : cyclic (Boolean)
- capture_endpoint_selection : selection (Boolean)
- capture_handle_positions : Sockets      [left (Vector), right (Vector)]
- capture_handle_type_selection : selection (Boolean)
- capture_length : Sockets      [length (Float), point_count (Integer)]
- capture_parameter : Sockets      [factor (Float), length (Float), index (Integer)]
- capture_resolution : resolution (Integer)
- capture_tangent : tangent (Vector)
- capture_tilt : tilt (Float)



## Attributes



- cyclic : Boolean = capture_cyclic(domain='CURVE')
- endpoint_selection : Boolean = capture_endpoint_selection(domain='CURVE')
- factor : Float = capture_parameter(domain='CURVE').factor
- handle_type_selection : Boolean = capture_handle_type_selection(domain='CURVE')
- left_handle_position : Vector = capture_handle_positions(domain='CURVE').left
- length : Float = capture_length(domain='CURVE').length
- parameter_index : Integer = capture_parameter(domain='CURVE').index
- parameter_length : Float = capture_parameter(domain='CURVE').length
- point_count : Integer = capture_length(domain='CURVE').point_count
- resolution : Integer = capture_resolution(domain='CURVE')
- right_handle_position : Vector = capture_handle_positions(domain='CURVE').right
- spline_ID : Integer = capture_ID(domain='SPLINE')
- spline_index : Integer = capture_index(domain='SPLINE')
- spline_position : Integer = capture_position(domain='SPLINE')
- tangent : Vector = capture_tangent(domain='CURVE')
- tilt : Float = capture_tilt(domain='CURVE')



## Stacked methods



- set_cyclic : Spline
- set_resolution : Spline



## Methods


### capture_cyclic

> Node: [IsSplineCyclic](../nodes/{self.node_name}.md)

```python
v = spline.capture_cyclic(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Boolean

### capture_endpoint_selection

> Node: [EndpointSelection](../nodes/{self.node_name}.md)

```python
v = spline.capture_endpoint_selection(self, start_size, end_size, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



##### Sockets arguments



- start_size : Integer
- end_size : Integer



#### Returns

    Boolean

### capture_handle_positions

> Node: [CurveHandlePositions](../nodes/{self.node_name}.md)

```python
v = spline.capture_handle_positions(self, relative, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



##### Sockets arguments



- relative : Boolean



#### Returns

    Sockets [left (Vector), right (Vector)]

### capture_handle_type_selection

> Node: [HandleTypeSelection](../nodes/{self.node_name}.md)

```python
v = spline.capture_handle_type_selection(self, handle_type, mode, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'RIGHT', 'LEFT'}
- domain:'CURVE'



#### Returns

    Boolean

### capture_length

> Node: [SplineLength](../nodes/{self.node_name}.md)

```python
v = spline.capture_length(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Sockets [length (Float), point_count (Integer)]

### capture_parameter

> Node: [SplineParameter](../nodes/{self.node_name}.md)

```python
v = spline.capture_parameter(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Sockets [factor (Float), length (Float), index (Integer)]

### capture_resolution

> Node: [SplineResolution](../nodes/{self.node_name}.md)

```python
v = spline.capture_resolution(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Integer

### capture_tangent

> Node: [CurveTangent](../nodes/{self.node_name}.md)

```python
v = spline.capture_tangent(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Vector

### capture_tilt

> Node: [CurveTilt](../nodes/{self.node_name}.md)

```python
v = spline.capture_tilt(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Returns

    Float

### cyclic

> Node: [IsSplineCyclic](../nodes/{self.node_name}.md)

```python
v = spline.cyclic(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Boolean

### endpoint_selection

> Node: [EndpointSelection](../nodes/{self.node_name}.md)

```python
v = spline.endpoint_selection(self, start_size, end_size)
```


#### Arguments


##### Parameters arguments



- self



##### Sockets arguments



- start_size : Integer
- end_size : Integer



#### Returns

    Boolean

### factor

> Node: [SplineParameter](../nodes/{self.node_name}.md)

```python
v = spline.factor(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Float

### handle_type_selection

> Node: [HandleTypeSelection](../nodes/{self.node_name}.md)

```python
v = spline.handle_type_selection(self, handle_type, mode)
```


#### Arguments


##### Parameters arguments



- self
- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'RIGHT', 'LEFT'}



#### Returns

    Boolean

### left_handle_position

> Node: [CurveHandlePositions](../nodes/{self.node_name}.md)

```python
v = spline.left_handle_position(self, relative)
```


#### Arguments


##### Parameters arguments



- self



##### Sockets arguments



- relative : Boolean



#### Returns

    Vector

### length

> Node: [SplineLength](../nodes/{self.node_name}.md)

```python
v = spline.length(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Float

### parameter_index

> Node: [SplineParameter](../nodes/{self.node_name}.md)

```python
v = spline.parameter_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### parameter_length

> Node: [SplineParameter](../nodes/{self.node_name}.md)

```python
v = spline.parameter_length(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Float

### point_count

> Node: [SplineLength](../nodes/{self.node_name}.md)

```python
v = spline.point_count(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### resolution

> Node: [SplineResolution](../nodes/{self.node_name}.md)

```python
v = spline.resolution(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### right_handle_position

> Node: [CurveHandlePositions](../nodes/{self.node_name}.md)

```python
v = spline.right_handle_position(self, relative)
```


#### Arguments


##### Parameters arguments



- self



##### Sockets arguments



- relative : Boolean



#### Returns

    Vector

### set_cyclic

> Node: [SetSplineCyclic](../nodes/{self.node_name}.md)

```python
spline.set_cyclic(geometry, selection, cyclic)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry
- selection : Boolean
- cyclic : Boolean



#### Returns

    self

### set_resolution

> Node: [SetSplineResolution](../nodes/{self.node_name}.md)

```python
spline.set_resolution(geometry, selection, resolution)
```


#### Arguments


##### Sockets arguments



- geometry : Geometry
- selection : Boolean
- resolution : Integer



#### Returns

    self

### spline_ID

> Node: [ID](../nodes/{self.node_name}.md)

```python
v = spline.spline_ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### spline_index

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = spline.spline_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### spline_position

> Node: [Index](../nodes/{self.node_name}.md)

```python
v = spline.spline_position(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Integer

### tangent

> Node: [CurveTangent](../nodes/{self.node_name}.md)

```python
v = spline.tangent(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Vector

### tilt

> Node: [CurveTilt](../nodes/{self.node_name}.md)

```python
v = spline.tilt(self)
```


#### Arguments


##### Parameters arguments



- self



#### Returns

    Float
