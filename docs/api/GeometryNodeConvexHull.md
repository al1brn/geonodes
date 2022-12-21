# Node 'Convex Hull'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
- geonodes name: `ConvexHull`
- bl_idname: `GeometryNodeConvexHull`

```python
from geonodes import nodes

node = nodes.ConvexHull(geometry=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeConvexHull.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

### Output sockets:

- **convex_hull** : [Geometry](Geometry.md)

## Implementation

| Name | Definition |
|------|------------|
| **[Geometry](Geometry.md)** |
| [convex_hull](Geometry.md#convex_hull-property) | `def convex_hull(self):` |

<sub>Go to [top](#node-Convex-Hull) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

