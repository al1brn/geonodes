# Node *Reverse Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/reverse_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
- geonodes name: `ReverseCurve`
- bl_idname: `GeometryNodeReverseCurve`

```python
from geonodes import nodes

node = nodes.ReverseCurve(curve=None, selection=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReverseCurve.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [reverse](Curve.md#reverse) | `def reverse(self, selection=None):` |

<sub>Go to [top](#node-Reverse-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

