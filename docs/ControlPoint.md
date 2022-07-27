
# Class ControlPoint

Radius and tilt


## tangent

Tangent attribute

Returns:
  Vector
  
getter: :class:`~geonodes.nodes.nodes.CurveTangent`
setter: read only



## set_handle_type

Set handle type

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  mode (set of strs): {'LEFT', 'RIGHT'}
  
  
  

## handle_positions

Handle positions node

Args:
  relative (Boolean): relative
  
Returns:
  node CurveHandlePositions
  
Output sockets:
- left : Vector
- right : Vector
  
  

## set_handle_positions

Set handle positions

Args:
  position (Vector): Positions
  offset (Vector): Offset
  mode (str): 'LEFT' or 'RIGHT'
  
- setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
  
  
  

## left_handles

Left handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the left output socket of node *CurveHandlePositions*
  
  
  

## right_handles

Right handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the right output socket of node *CurveHandlePositions*
  
  

## handles_selection

Handle type selection

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  left (bool): select left handle
  right (bool): select right handle
  
Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`




## handle_auto

Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_free

Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_vector

Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_align

Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_auto

Left Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_auto

Right Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_free

Left Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_free

Right Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_vector

Left Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_vector

Right Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_align

Left Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_align

Right Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



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



## delete

Delete points

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`

Returns:
  self
  
.. code-block:: python

  curve.points(...).delete()
  
  