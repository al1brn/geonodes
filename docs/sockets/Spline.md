
# Data socket Spline

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Attribute capture

- [capture_cyclic](#capture_cyclic) : cyclic (Boolean)
- [capture_endpoint_selection](#capture_endpoint_selection) : selection (Boolean)
- [capture_handle_positions](#capture_handle_positions) : Sockets      [left (Vector), right (Vector)]
- [capture_handle_type_selection](#capture_handle_type_selection) : selection (Boolean)
- [capture_length](#capture_length) : Sockets      [length (Float), point_count (Integer)]
- [capture_parameter](#capture_parameter) : Sockets      [factor (Float), length (Float), index (Integer)]
- [capture_resolution](#capture_resolution) : resolution (Integer)
- [capture_tangent](#capture_tangent) : tangent (Vector)
- [capture_tilt](#capture_tilt) : tilt (Float)

## Attributes

- [cyclic](#cyclic) : Boolean = capture_cyclic(domain='CURVE')
- [endpoint_selection](#endpoint_selection) : Boolean = capture_endpoint_selection(domain='CURVE')
- [factor](#factor) : Float = capture_parameter(domain='CURVE').factor
- [handle_type_selection](#handle_type_selection) : Boolean = capture_handle_type_selection(domain='CURVE')
- [left_handle_position](#left_handle_position) : Vector = capture_handle_positions(domain='CURVE').left
- [length](#length) : Float = capture_length(domain='CURVE').length
- [parameter_index](#parameter_index) : Integer = capture_parameter(domain='CURVE').index
- [parameter_length](#parameter_length) : Float = capture_parameter(domain='CURVE').length
- [point_count](#point_count) : Integer = capture_length(domain='CURVE').point_count
- [resolution](#resolution) : Integer = capture_resolution(domain='CURVE')
- [right_handle_position](#right_handle_position) : Vector = capture_handle_positions(domain='CURVE').right
- [spline_ID](#spline_id) : Integer = capture_ID(domain='SPLINE')
- [spline_index](#spline_index) : Integer = capture_index(domain='SPLINE')
- [spline_position](#spline_position) : Integer = capture_position(domain='SPLINE')
- [tangent](#tangent) : Vector = capture_tangent(domain='CURVE')
- [tilt](#tilt) : Float = capture_tilt(domain='CURVE')

## Methods

- [set_cyclic](#set_cyclic) : geometry (Geometry)
- [set_resolution](#set_resolution) : geometry (Geometry)

## capture_handle_positions

> Node: [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
node ref [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) </sub>

```python
v = spline.capture_handle_positions(self, relative, domain='CURVE')
```

### Arguments


#### Sockets

- relative : Boolean## Parameters
- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.CurveHandlePositions(relative=relative)
```

### Returns

Sockets [left (Vector), right (Vector)]


## capture_tangent

> Node: [CurveTangent](/docs/nodes/CurveTangent.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputTangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
node ref [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) </sub>

```python
v = spline.capture_tangent(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.CurveTangent()
```

### Returns

Vector


## capture_tilt

> Node: [CurveTilt](/docs/nodes/CurveTilt.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
node ref [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) </sub>

```python
v = spline.capture_tilt(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.CurveTilt()
```

### Returns

Float


## capture_endpoint_selection

> Node: [EndpointSelection](/docs/nodes/EndpointSelection.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeCurveEndpointSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
node ref [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) </sub>

```python
v = spline.capture_endpoint_selection(self, start_size, end_size, domain='CURVE')
```

### Arguments


#### Sockets

- start_size : Integer
- end_size : Integer## Parameters
- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.EndpointSelection(start_size=start_size, end_size=end_size)
```

### Returns

Boolean


## capture_handle_type_selection

> Node: [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
node ref [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) </sub>

```python
v = spline.capture_handle_type_selection(self, handle_type, mode, domain='CURVE')
```

### Arguments


#### Parameters

- self
- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'LEFT', 'RIGHT'}
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
```

### Returns

Boolean


## capture_cyclic

> Node: [IsSplineCyclic](/docs/nodes/IsSplineCyclic.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
node ref [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) </sub>

```python
v = spline.capture_cyclic(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.IsSplineCyclic()
```

### Returns

Boolean


## capture_length

> Node: [SplineLength](/docs/nodes/SplineLength.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
node ref [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) </sub>

```python
v = spline.capture_length(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.SplineLength()
```

### Returns

Sockets [length (Float), point_count (Integer)]


## capture_parameter

> Node: [SplineParameter](/docs/nodes/SplineParameter.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
node ref [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) </sub>

```python
v = spline.capture_parameter(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.SplineParameter()
```

### Returns

Sockets [factor (Float), length (Float), index (Integer)]


## capture_resolution

> Node: [SplineResolution](/docs/nodes/SplineResolution.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
node ref [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) </sub>

```python
v = spline.capture_resolution(self, domain='CURVE')
```

### Arguments


#### Parameters

- self
- domain:'CURVE'

### Node creation

```python
from geondes import nodes
nodes.SplineResolution()
```

### Returns

Integer


## spline_ID

> Node: [ID](/docs/nodes/ID.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
node ref [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) </sub>

```python
v = spline.spline_ID(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.ID()
```

### Returns

Integer


## spline_index

> Node: [Index](/docs/nodes/Index.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
node ref [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) </sub>

```python
v = spline.spline_index(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.Index()
```

### Returns

Integer


## spline_position

> Node: [Index](/docs/nodes/Index.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
node ref [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) </sub>

```python
v = spline.spline_position(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.Index()
```

### Returns

Integer


## left_handle_position

> Node: [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
node ref [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) </sub>

```python
v = spline.left_handle_position(self, relative)
```

### Arguments


#### Sockets

- relative : Boolean## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.CurveHandlePositions(relative=relative)
```

### Returns

Vector


## right_handle_position

> Node: [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
node ref [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) </sub>

```python
v = spline.right_handle_position(self, relative)
```

### Arguments


#### Sockets

- relative : Boolean## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.CurveHandlePositions(relative=relative)
```

### Returns

Vector


## tangent

> Node: [CurveTangent](/docs/nodes/CurveTangent.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputTangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
node ref [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) </sub>

```python
v = spline.tangent(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.CurveTangent()
```

### Returns

Vector


## tilt

> Node: [CurveTilt](/docs/nodes/CurveTilt.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
node ref [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) </sub>

```python
v = spline.tilt(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.CurveTilt()
```

### Returns

Float


## endpoint_selection

> Node: [EndpointSelection](/docs/nodes/EndpointSelection.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeCurveEndpointSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
node ref [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) </sub>

```python
v = spline.endpoint_selection(self, start_size, end_size)
```

### Arguments


#### Sockets

- start_size : Integer
- end_size : Integer## Parameters
- self

### Node creation

```python
from geondes import nodes
nodes.EndpointSelection(start_size=start_size, end_size=end_size)
```

### Returns

Boolean


## handle_type_selection

> Node: [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
node ref [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) </sub>

```python
v = spline.handle_type_selection(self, handle_type, mode)
```

### Arguments


#### Parameters

- self
- handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode : {'LEFT', 'RIGHT'}

### Node creation

```python
from geondes import nodes
nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
```

### Returns

Boolean


## cyclic

> Node: [IsSplineCyclic](/docs/nodes/IsSplineCyclic.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
node ref [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) </sub>

```python
v = spline.cyclic(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.IsSplineCyclic()
```

### Returns

Boolean


## length

> Node: [SplineLength](/docs/nodes/SplineLength.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
node ref [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) </sub>

```python
v = spline.length(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineLength()
```

### Returns

Float


## point_count

> Node: [SplineLength](/docs/nodes/SplineLength.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
node ref [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) </sub>

```python
v = spline.point_count(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineLength()
```

### Returns

Integer


## factor

> Node: [SplineParameter](/docs/nodes/SplineParameter.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
node ref [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) </sub>

```python
v = spline.factor(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineParameter()
```

### Returns

Float


## parameter_length

> Node: [SplineParameter](/docs/nodes/SplineParameter.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
node ref [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) </sub>

```python
v = spline.parameter_length(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineParameter()
```

### Returns

Float


## parameter_index

> Node: [SplineParameter](/docs/nodes/SplineParameter.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
node ref [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) </sub>

```python
v = spline.parameter_index(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineParameter()
```

### Returns

Integer


## resolution

> Node: [SplineResolution](/docs/nodes/SplineResolution.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeInputSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
node ref [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) </sub>

```python
v = spline.resolution(self)
```

### Arguments


#### Parameters

- self

### Node creation

```python
from geondes import nodes
nodes.SplineResolution()
```

### Returns

Integer


## set_cyclic

> Node: [SetSplineCyclic](/docs/nodes/SetSplineCyclic.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
node ref [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) </sub>

```python
v = spline.set_cyclic(selection, cyclic)
```

### Arguments


#### Sockets

- geometry : Geometry (self)
- selection : Boolean
- cyclic : Boolean

### Node creation

```python
from geondes import nodes
nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic)
```

### Returns

Geometry


## set_resolution

> Node: [SetSplineResolution](/docs/nodes/SetSplineResolution.md)
  
<sub>go to: [top](#data-socket-spline) [index](/docs/index.md)
blender ref [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
node ref [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) </sub>

```python
v = spline.set_resolution(selection, resolution)
```

### Arguments


#### Sockets

- geometry : Geometry (self)
- selection : Boolean
- resolution : Integer

### Node creation

```python
from geondes import nodes
nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution)
```

### Returns

Geometry

