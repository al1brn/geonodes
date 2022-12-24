# Node *Subdivide Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/subdivide_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
- geonodes name: `SubdivideCurve`
- bl_idname: `GeometryNodeSubdivideCurve`

```python
from geonodes import nodes

node = nodes.SubdivideCurve(curve=None, cuts=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideCurve.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **cuts**: [Integer](Integer.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [subdivide](Curve.md#subdivide) | `def subdivide(self, cuts=None):` |

<sub>Go to [top](#node-Subdivide-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

