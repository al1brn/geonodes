
# Class CurveDomain

> Field domain CURVE
  
Inherits from [Domain](/docs/core/domain.MD)

A property of Spline and Curve


## tilt

> Field [SetCurveTilt](/docs/nodes/SetCurveTilt.md)
  
Blender menu : **curve/set_curve_tilt**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>



## cyclic

> Field [SetSplineCyclic](/docs/nodes/SetSplineCyclic.md)
  
Blender menu : **curve/set_spline_cyclic**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>



## tangent

> Field [CurveTangent](/docs/nodes/CurveTangent.md)
  
Blender menu : **curve/curve_tangent**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property

### Returns

Vector



## length

> Field [SplineLength](/docs/nodes/SplineLength.md)
  
Blender menu : **curve/spline_length**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  - **length: Float**
  - _point_count: Integer_

### Returns

Float



## point_count

> Field [SplineLength](/docs/nodes/SplineLength.md)
  
Blender menu : **curve/spline_length**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  - _length : Float_
  - **point_count : Integer**

### Returns

Integer



## parameter_factor

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  - **factor : Float**
  - _length  : Float_
  - _index : Integer_

### Returns

Float



## parameter_length

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  - _factor : Float_
  - **length  : Float**
  - _index : Integer_

### Returns

Float



## parameter_index

> Field [SplineParameter](/docs/nodes/SplineParameter.md)
  
Blender menu : **curve/spline_parameter**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Property
  
  - _factor : Float_
  - _length  : Float**
  - **index : Integer_

### Returns

Integer



## resolution

> Field [SetSplineResolution](/docs/nodes/SetSplineResolution.md)
  
Blender menu : **curve/set_spline_resolution**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>



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



## handle_positions

> Field [CurveHandlePositions](/docs/nodes/CurveHandlePositions.md)
  
Blender menu : **curve/curve_handle_position**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Method

### Arguments

- relative : Boolean

### Returns

Node with two sockets : left and right



## set_handle_positions

> Field [SetHandlePositions](/docs/nodes/SetHandlePositions.md)
  
Blender menu : **curve/set_handle_positions**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Methodes set_left_handle_positions and set_right_handle_positions are available
  
  

## set_left_handle_positions

> Field [SetHandlePositions](/docs/nodes/SetHandlePositions.md)
  
Blender menu : **curve/set_handle_positions**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Methodes set_left_handle_positions and set_right_handle_positions are available
  
  

## set_right_handle_positions

> Field [SetHandlePositions](/docs/nodes/SetHandlePositions.md)
  
Blender menu : **curve/set_handle_positions**<br>
<sub>go to [top](#class-curvedomain) [index](/docs/index.md)</sub>

  Methodes set_left_handle_positions and set_right_handle_positions are available
  
  

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
    
    