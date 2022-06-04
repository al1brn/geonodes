
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


