
# Class CurveHandlePositions

> Geometry node name: _'Curve Handle Positions'_<br>Blender type:  **GeometryNodeInputCurveHandlePositions**

## Initialization


```python
from geonodes import nodes
node = nodes.CurveHandlePositions(relative=None, label=None)
```


### Arguments


#### Input sockets



- **relative** : _Boolean_



#### Node label



- **label** : Geometry node label



## Output sockets



- **left** : _Vector_
- **right** : _Vector_



## Data sockets

> Data socket classes implementing this node


- [Spline](../sockets/Spline.md) [capture_handle_positions](../sockets/Spline.md#capture_handle_positions) : Capture attribute
- [Spline](../sockets/Spline.md) [left_handle_position](../sockets/Spline.md#left_handle_position) : Attribute
- [Spline](../sockets/Spline.md) [right_handle_position](../sockets/Spline.md#right_handle_position) : Attribute


