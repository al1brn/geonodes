
# Node SplineResolution

> Geometry node name: [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html)<br>
  Blender type: [Spline Resolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------
```python
from geonodes import nodes
node = nodes.SplineResolution(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- resolution : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Spline](/docs/sockets/Spline.md).[capture_resolution](/docs/sockets/Spline.md#capture_resolution) : Capture attribute
- [Spline](/docs/sockets/Spline.md).[resolution](/docs/sockets/Spline.md#resolution) : Attribute
  
