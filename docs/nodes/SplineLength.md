
# Node SplineLength

> Geometry node name: [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html)<br>
  Blender type: [Spline Length](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.SplineLength(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- length : Float
- point_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/Spline.md).[length](/docs/Spline.md#length) : Fields
- [Spline](/docs/Spline.md).[point_count](/docs/Spline.md#point_count) : Fields
  
