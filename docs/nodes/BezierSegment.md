
# Node BezierSegment

> Geometry node name: [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html)<br>
  Blender type: [Bezier Segment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None, node_color=None)
```



## Arguments


### Input sockets

- resolution : Integer
- start : Vector
- start_handle : Vector
- end_handle : Vector
- end : Vector

### Parameters

- mode : str (default = 'POSITION') in ('POSITION', 'OFFSET')

### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- curve : Curve
