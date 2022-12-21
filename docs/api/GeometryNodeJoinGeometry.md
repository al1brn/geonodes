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

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f98d0>>](Geometry.md#join)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16d4f9900>>](function.md#join_geometry)
