# Node Join Geometry

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
- geonodes name: `JoinGeometry`
- bl_idname: `GeometryNodeJoinGeometry`

```python
from geonodes import nodes

node = nodes.JoinGeometry(*geometry)
```

### Args:

#### Input socket arguments:

- **geometry**: *[Geometry](Geometry.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### class [Geometry](Geometry.md)

 - [join](Geometry.md#join)
#### Global functions

 - [join_geometry](function.md#join_geometry)
