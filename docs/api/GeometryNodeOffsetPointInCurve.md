# Node *Offset Point in Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)
- geonodes name: `OffsetPointInCurve`
- bl_idname: `GeometryNodeOffsetPointInCurve`

```python
from geonodes import nodes

node = nodes.OffsetPointInCurve(point_index=None, offset=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

### Args:

#### Input socket arguments:

- **point_index**: [Integer](Integer.md)
- **offset**: [Integer](Integer.md)

### Output sockets:

- **is_valid_offset** : [Boolean](Boolean.md)
- **point_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [offset](ControlPoint.md#offset) | `def offset(self, offset=None):` |
| **[Curve](Curve.md)** |
| [offset_point](Curve.md#offset_point) | `def offset_point(self, point_index=None, offset=None):` |

<sub>Go to [top](#node-Offset-Point-in-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

