# Node *Bezier Segment*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
- geonodes name: `BezierSegment`
- bl_idname: `GeometryNodeCurvePrimitiveBezierSegment`

```python
from geonodes import nodes

node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveBezierSegment.webp)

### Args:

#### Input socket arguments:

- **resolution**: [Integer](Integer.md)
- **start**: [Vector](Vector.md)
- **start_handle**: [Vector](Vector.md)
- **end_handle**: [Vector](Vector.md)
- **end**: [Vector](Vector.md)

#### Node parameter arguments:

- **mode** (str): default = 'POSITION' in ('POSITION', 'OFFSET')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [BezierSegment](Curve.md#BezierSegment) | `@classmethod`<br> `def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):` |

<sub>Go to [top](#node-Bezier-Segment) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

