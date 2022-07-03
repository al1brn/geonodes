
# Class ControlPoint

Curve domains


Control point : the point domain of splines


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
  
- setter: :class:`nodes.SetHandlePositions`
  
  
  

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
  
getter: :class:`nodes.HandleTypeSelection`




## handle_auto

Auto Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## handle_free

Free Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## handle_vector

Vector Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## handle_align

Align Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## left_handle_auto

Left Auto Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## right_handle_auto

Right Auto Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## left_handle_free

Left Free Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## right_handle_free

Right Free Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## left_handle_vector

Left Vector Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## right_handle_vector

Right Vector Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## left_handle_align

Left Align Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`



## right_handle_align

Right Align Handle selection

Returns:
  Boolean
  
getter: :class:`nodes.HandleTypeSelection`

