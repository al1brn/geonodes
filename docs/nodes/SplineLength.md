
# Node SplineLength

> Geometry node name: [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/spline_length.html)<br>
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

length : Float
- point_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Spline) [capture_length](section:Data socket Spline/capture_length) : Capture attribute
- [class_name](section:Data socket Spline) [length](section:Data socket Spline/length) : Attribute
- [class_name](section:Data socket Spline) [point_count](section:Data socket Spline/point_count) : Attribute
  
