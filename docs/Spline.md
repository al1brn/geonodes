
# Class Spline

Spline


## tangent

Tangent attribute

Returns:
  Vector
  
getter: :class:`nodes.CurveTangent`
setter: read only



## spline_length

spline_length attribute

Returns:
  node SplineLength
  
Output sockets:
- length : Float
- point_count : Integer
  
getter: :class:`nodes.SplineLength`
setter: read only



## length

Length attribute

Returns:
  Float: length socket of spline_length
  
getter: :class:`nodes.SplineLength`
setter: read only



## point_count

Point count attribute

Returns:
  Integer: point_count socket of spline_length
  
getter: :class:`nodes.SplineLength`
setter: read only



## parameter

Spline parameter attribute

Returns:
  Node SplineParameter
  
Output sockets:
- factor : Float
- length : Float
- index : Integer
  
getter: :class:`nodes.SplineParameter`
setter: read only



## parameter_factor

Parameter factor attribute

Returns:
  Float: factor socket of parameter
  
getter: :class:`nodes.SplineParameter`
setter: read only



## parameter_length

Parameter length attribute

Returns:
  Float: length socket of parameter
  
getter: :class:`nodes.SplineParameter`
setter: read only



## parameter_index

Parameter factor attribute

Returns:
  Integer: index socket of parameter
  
getter: :class:`nodes.SplineParameter`
setter: read only



## endpoint_selection

End point selection

Args:
- start_size : Integer
- end_size : Integer

### Returns

Float

getter: :class:`nodes.EndpointSelection`



## delete

<method GeometryNodeDeleteGeometry>

### Example

```python
curve.splines(...).delete()
```

