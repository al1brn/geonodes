
# Node BezierSegment

> Geometry node name: [Bezier Segment](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/bezier_segment.html)<br>
  Blender type: [Bezier Segment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None)
```



## Arguments


### Input sockets

resolution : Integer
- start : Vector
- start_handle : Vector
- end_handle : Vector
- end : Vector

### Parameters

mode : str (default = 'POSITION') in ('POSITION', 'OFFSET')

### Node label

- label : Geometry node display label (default=None)

## Output sockets

curve : Curve

## Data sockets

> Data socket classes implementing this node.
  
[class_name](/docs/sockets/Curve.md) [BezierSegment](/docs/sockets/Curve.md#beziersegment) : Constructor

