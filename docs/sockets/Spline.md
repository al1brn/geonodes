
# Class Spline

> Inherits from: ***Geometry***

## Attribute capture



- [capture_cyclic](#capture_cyclic) : [IsSplineCyclic](../nodes/IsSplineCyclic.md) cyclic (Boolean)
- [capture_endpoint_selection](#capture_endpoint_selection) : [EndpointSelection](../nodes/EndpointSelection.md) selection (Boolean)
- [capture_handle_positions](#capture_handle_positions) : [CurveHandlePositions](../nodes/CurveHandlePositions.md) Sockets      [left (Vector), right (Vector)]
- [capture_handle_type_selection](#capture_handle_type_selection) : [HandleTypeSelection](../nodes/HandleTypeSelection.md) selection (Boolean)
- [capture_length](#capture_length) : [SplineLength](../nodes/SplineLength.md) Sockets      [length (Float), point_count (Integer)]
- [capture_parameter](#capture_parameter) : [SplineParameter](../nodes/SplineParameter.md) Sockets      [factor (Float), length (Float), index (Integer)]
- [capture_resolution](#capture_resolution) : [SplineResolution](../nodes/SplineResolution.md) resolution (Integer)
- [capture_tangent](#capture_tangent) : [CurveTangent](../nodes/CurveTangent.md) tangent (Vector)
- [capture_tilt](#capture_tilt) : [CurveTilt](../nodes/CurveTilt.md) tilt (Float)



## Attributes



- [cyclic](#cyclic) : [IsSplineCyclic](../nodes/IsSplineCyclic.md) Boolean = capture_cyclic(domain='CURVE')
- [endpoint_selection](#endpoint_selection) : [EndpointSelection](../nodes/EndpointSelection.md) Boolean = capture_endpoint_selection(domain='CURVE')
- [factor](#factor) : [SplineParameter](../nodes/SplineParameter.md) Float = capture_parameter(domain='CURVE').factor
- [handle_type_selection](#handle_type_selection) : [HandleTypeSelection](../nodes/HandleTypeSelection.md) Boolean = capture_handle_type_selection(domain='CURVE')
- [left_handle_position](#left_handle_position) : [CurveHandlePositions](../nodes/CurveHandlePositions.md) Vector = capture_handle_positions(domain='CURVE').left
- [length](#length) : [SplineLength](../nodes/SplineLength.md) Float = capture_length(domain='CURVE').length
- [parameter_index](#parameter_index) : [SplineParameter](../nodes/SplineParameter.md) Integer = capture_parameter(domain='CURVE').index
- [parameter_length](#parameter_length) : [SplineParameter](../nodes/SplineParameter.md) Float = capture_parameter(domain='CURVE').length
- [point_count](#point_count) : [SplineLength](../nodes/SplineLength.md) Integer = capture_length(domain='CURVE').point_count
- [resolution](#resolution) : [SplineResolution](../nodes/SplineResolution.md) Integer = capture_resolution(domain='CURVE')
- [right_handle_position](#right_handle_position) : [CurveHandlePositions](../nodes/CurveHandlePositions.md) Vector = capture_handle_positions(domain='CURVE').right
- [spline_ID](#spline_id) : [ID](../nodes/ID.md) Integer = capture_ID(domain='SPLINE')
- [spline_index](#spline_index) : [Index](../nodes/Index.md) Integer = capture_index(domain='SPLINE')
- [spline_position](#spline_position) : [Index](../nodes/Index.md) Integer = capture_position(domain='SPLINE')
- [tangent](#tangent) : [CurveTangent](../nodes/CurveTangent.md) Vector = capture_tangent(domain='CURVE')
- [tilt](#tilt) : [CurveTilt](../nodes/CurveTilt.md) Float = capture_tilt(domain='CURVE')



## Stacked methods



- [set_cyclic](#set_cyclic) : [SetSplineCyclic](../nodes/SetSplineCyclic.md) Spline
- [set_resolution](#set_resolution) : [SetSplineResolution](../nodes/SetSplineResolution.md) Spline



## Methods reference


### capture_cyclic

> Node: [IsSplineCyclic](../nodes/{self.node_name}.md)

```python
v = spline.capture_cyclic(self, domain='CURVE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'CURVE'



#### Node creation


```python
node = nodes.IsSplineCyclic()
```


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



#### Node creation


```python
node = nodes.EndpointSelection(start_size=start_size, end_size=end_size)
```


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



#### Node creation


```python
node = nodes.CurveHandlePositions(relative=relative)
```


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



#### Node creation


```python
node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
```


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



#### Node creation


```python
node = nodes.SplineLength()
```


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



#### Node creation


```python
node = nodes.SplineParameter()
```


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



#### Node creation


```python
node = nodes.SplineResolution()
```


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



#### Node creation


```python
node = nodes.CurveTangent()
```


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



#### Node creation


```python
node = nodes.CurveTilt()
```


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



#### Node creation


```python
node = nodes.IsSplineCyclic()
```


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



#### Node creation


```python
node = nodes.EndpointSelection(start_size=start_size, end_size=end_size)
```


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



#### Node creation


```python
node = nodes.SplineParameter()
```


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



#### Node creation


```python
node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
```


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



#### Node creation


```python
node = nodes.CurveHandlePositions(relative=relative)
```


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



#### Node creation


```python
node = nodes.SplineLength()
```


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



#### Node creation


```python
node = nodes.SplineParameter()
```


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



#### Node creation


```python
node = nodes.SplineParameter()
```


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



#### Node creation


```python
node = nodes.SplineLength()
```


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



#### Node creation


```python
node = nodes.SplineResolution()
```


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



#### Node creation


```python
node = nodes.CurveHandlePositions(relative=relative)
```


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



#### Node creation


```python
node = nodes.SetSplineCyclic(geometry=geometry, selection=selection, cyclic=cyclic)
```


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



#### Node creation


```python
node = nodes.SetSplineResolution(geometry=geometry, selection=selection, resolution=resolution)
```


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



#### Node creation


```python
node = nodes.ID()
```


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



#### Node creation


```python
node = nodes.Index()
```


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



#### Node creation


```python
node = nodes.Index()
```


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



#### Node creation


```python
node = nodes.CurveTangent()
```


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



#### Node creation


```python
node = nodes.CurveTilt()
```


#### Returns

    Float
