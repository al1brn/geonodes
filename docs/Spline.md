
# Class Spline

Spline


## tangent

Tangent attribute

Returns:
  Vector
  
getter: :class:`~geonodes.nodes.nodes.CurveTangent`
setter: read only



## spline_length

spline_length attribute

Returns:
  node SplineLength
  
Output sockets:
- length : Float
- point_count : Integer
  
getter: :class:`~geonodes.nodes.nodes.SplineLength`
setter: read only



## length

Length attribute

Returns:
  Float: length socket of spline_length
  
getter: :class:`~geonodes.nodes.nodes.SplineLength`
setter: read only



## point_count

Point count attribute

Returns:
  Integer: point_count socket of spline_length
  
getter: :class:`~geonodes.nodes.nodes.SplineLength`
setter: read only



## parameter

Spline parameter attribute

Returns:
  Node SplineParameter
  
Output sockets:
- factor : Float
- length : Float
- index : Integer
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_factor

Parameter factor attribute

Returns:
  Float: factor socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_length

Parameter length attribute

Returns:
  Float: length socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_index

Parameter factor attribute

Returns:
  Integer: index socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## endpoint_selection

End point selection

Args:
- start_size : Integer
- end_size : Integer

### Returns

Float

getter: :class:`~geonodes.nodes.nodes.EndpointSelection`



## delete

Delete splines

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`

Returns:
  self
  
.. code-block:: python

  curve.splines(...).delete()
  
  

## set_normal

set normals

Node :class:`~geonodes.nodes.nodes.SetCurveNormal`

Args:
  mode (str): Node parameter, default = 'MINIMUM_TWIST' in ('MINIMUM_TWIST', 'Z_UP')
  
Returns:
  self
  
  
  

## weighted_points

Topology Blender 3.4
