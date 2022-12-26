# Node *Join Geometry*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
- geonodes name: `JoinGeometry`
- bl_idname: `GeometryNodeJoinGeometry`

```python
from geonodes import nodes

node = nodes.JoinGeometry(*geometry)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeJoinGeometry.webp)

### Args:

#### Input socket arguments:

- **geometry**: *[Geometry](Geometry.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [join](Geometry.md#join) | `def join(*geometry):` |
| Global functions |
| [join_geometry](functions.md#join_geometry) | `def join_geometry(*geometry):` |

<sub>Go to [top](#node-Join-Geometry) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

