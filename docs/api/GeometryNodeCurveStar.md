# Node *Star*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/star.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
- geonodes name: `Star`
- bl_idname: `GeometryNodeCurveStar`

```python
from geonodes import nodes

node = nodes.Star(points=None, inner_radius=None, outer_radius=None, twist=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveStar.webp)

### Args:

#### Input socket arguments:

- **points**: [Integer](Integer.md)
- **inner_radius**: [Float](Float.md)
- **outer_radius**: [Float](Float.md)
- **twist**: [Float](Float.md)

### Output sockets:

- **curve** : [Curve](Curve.md)
- **outer_points** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Curve](Curve.md)** |
| [Star](Curve.md#Star) | `@classmethod`<br> `def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):` |

<sub>Go to [top](#node-Star) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

