# Node Bezier Segment

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeCurvePrimitiveBezierSegment`

```python
from geonodes import nodes

node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

#### Input socket arguments:

- resolution: Integer
- start: Vector
- start_handle: Vector
- end_handle: Vector
- end: Vector

#### Node parameter arguments:

- mode (str): Node parameter, default = 'POSITION' in ('POSITION', 'OFFSET')

#### Output sockets:

- **curve** : Curve

