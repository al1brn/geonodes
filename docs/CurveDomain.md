
# Class CurveDomain

> Field domain CURVE
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Spline and Curve


## handle_positions

> Field [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
Blender menu : **curve/curve_handle_position**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  Sockets can be access individually via:
  
  - [handle_positions_left](#handle_positions_left)
  - [handle_positions_right](#handle_positions_right)

### Arguments

- relative : Boolean

### Returns

Node with 2 output sockets:
- left
- right
  
  

## handle_positions_left

> Field [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
Blender menu : **curve/curve_handle_position**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  Returns the socket **left** of the methode [handle_positions(#handle_positions)]

### Arguments

- relative : Boolean

### Returns

Vector



## handle_positions_right

> Field [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
Blender menu : **curve/curve_handle_position**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  Returns the socket **right** of the methode [handle_positions(#handle_positions)]

### Arguments

- relative : Boolean

### Returns

Vector



## tangent

> Field [CurveTangent](/docs/nodes/CurveTangent.md)
  
Blender menu : **curve/curve_tangent**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Vector



## tilt

> Field [CurveTilt](/docs/nodes/CurveTilt.md)
  
Blender menu : **curve/curve_tilt**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## endpoint_selection

> Field [EndpointSelection](/docs/nodes/EndpointSelection.md)
  
Blender menu : **curve/endpoint_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- start_size : Integer
- end_size : Integer

### Returns

Float



## handle_type_selection

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  The values of the two parameters are declined in 2 methods:
  - [left_handle_selection](#left_handle_selection)
  - [right_handle_selection](#right_handle_selection)
    
  and 8 properties:
  - [left_handle_free](#left_handle_free)
  - [left_handle_vector](#left_handle_vector)
  - [left_handle_vector](#left_handle_vector)
  - [left_handle_align](#left_handle_align)
  - [right_handle_free](#right_handle_free)
  - [right_handle_auto](#right_handle_auto)
  - [right_handle_vector](#right_handle_vector)
  - [right_handle_align](#right_handle_align)

### Arguments

- handle_type : str in 'AUTO', 'FREE', 'VECTOR', 'ALIGN'
- mode : str in ['RIGHT', 'LEFT'] or set {'RIGHT', 'LEFT'}

### Returns

Boolean



## left_handle_selection

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## right_handle_selection

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## left_handle_free

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## left_handle_auto

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## left_handle_vector

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## left_handle_align

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## right_handle_free

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## right_handle_auto

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## right_handle_vector

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## right_handle_align

> Field [HandleTypeSelection](/docs/nodes/HandleTypeSelection.md)
  
Blender menu : **curve/handle_type_selection**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  See [handle_type_selection](#handle_type_selection)
  
  Returns
    Boolean
    
    

## cyclic

> Field [IsSplineCyclic](/docs/nodes/IsSplineCyclic.md)
  
Blender menu : **curve/is_spline_cyclic**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns
    Boolean
    
    

## length_point_count

> Field [SplineLength](/docs/nodes/SplineLength.md)
  
Blender menu : **curve/spline_length**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [length](#length)
  - [point_count](#point_count)

### Returns

Node with 2 output sockets:
- length
- point_count
  
  

## length

> Field [SplineLength](/docs/nodes/SplineLength.md)
  
Blender menu : **curve/spline_length**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns the socket **length** of method [length_point_count(#length_point_count)]

### Returns

Float



## point_count

> Field [SplineLength](/docs/nodes/SplineLength.md)
  
Blender menu : **curve/spline_length**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns the socket **point_count** of method [length_point_count(#length_point_count)]

### Returns

Integer



## parameter

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Sockets can be access individually via:
  
  - [factor](#factor)
  - [parameter_length](#parameter_length)
  - [parameter_index](#parameter_index)

### Returns

Node with 3 output sockets:
- factor
- length
- index
  
  

## factor

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns the socket **factor** of method [parameter(#parameter)]

### Returns

Float



## parameter_length

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns the socket **length** of method [parameter(#parameter)]

### Returns

Float



## parameter_index

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns the socket **index** of method [parameter(#parameter)]

### Returns

Integer



## resolution

> Field [SplineResolution](/docs/nodes/SplineResolution.md)
  
Blender menu : **curve/spline_resolution**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  Returns
    Integer
    
    