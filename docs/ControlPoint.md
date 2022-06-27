
# Class ControlPoint

Curve domains


Control point : the point domain of splines


## set_handle_type

Handles

----- Handles type


## handle_type

> Set the handles type
  
<blid GeometryNodeCurveSetHandles>

Set the type of the left and right handles
        
```python
curve.splines.type = 'BEZIER'
curve.points.handle_type = 'FREE'
```



## left_type

> Set the left handles type
  
<blid GeometryNodeCurveSetHandles>

Set the type of the left handles
        
```python
curve.splines.type = 'BEZIER'
curve.points.left_type = 'FREE'
```



## right_type

> Set the right handles type
  
<blid GeometryNodeCurveSetHandles>

Set the type of the right handles
        
```python
curve.splines.type = 'BEZIER'
curve.points.right_type = 'FREE'
```



## handles

----- Handles position / offset


## handles_selection

----- Handle selection


## left_offset

> Property Handle offset setter
  
<blid GeometryNodeSetCurveHandlePositions>

### Arguments

- value: Vector
  
  

## right_offset

> Property Handle offset setter
  
<blid GeometryNodeSetCurveHandlePositions>

### Arguments

- value: Vector
  
  