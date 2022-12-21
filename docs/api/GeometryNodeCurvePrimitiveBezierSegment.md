# Node 'Bezier Segment'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/bezier_segment.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
- geonodes name: `BezierSegment`
- bl_idname: `GeometryNodeCurvePrimitiveBezierSegment`

```python
from geonodes import nodes

node = nodes.BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION')
```

[Blender Image](self.node_image_ref)

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

### [Curve](Curve.md)

| Name | Definition |
|------|------------|
 | [bezier_segment](Curve.md#bezier_segment-classmethod) | `def bezier_segment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):` |

<sub>Go to [top](#node-Bezier-Segment) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

