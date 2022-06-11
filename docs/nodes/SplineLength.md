
# Node SplineLength

> Geometry node name: [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html)<br>
  Blender type: [Spline Length](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SplineLength(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- length : Float
- point_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_length](/docs/sockets/Spline.md#capture_length) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[length](/docs/sockets/Spline.md#length) : Attribute
- [Spline](/docs/sockets/Spline.md).[point_count](/docs/sockets/Spline.md#point_count) : Attribute
  
