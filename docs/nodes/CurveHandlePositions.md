
# Node CurveHandlePositions

> Geometry node name: [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)<br>
  Blender type: [Curve Handle Positions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.CurveHandlePositions(relative=None, label=None)
```



## Arguments


### Input sockets

- relative : Boolean

### Node label

- label : Geometry node display label (default=None)

## Output sockets

- left : Vector
- right : Vector

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_handle_positions](/docs/sockets/Spline.md#capture_handle_positions) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[left_handle_position](/docs/sockets/Spline.md#left_handle_position) : Attribute
- [Spline](/docs/sockets/Spline.md).[right_handle_position](/docs/sockets/Spline.md#right_handle_position) : Attribute
  
