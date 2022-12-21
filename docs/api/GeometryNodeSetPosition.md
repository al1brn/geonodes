# Node Set Position

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetPosition`

```python
from geonodes import nodes

node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- position: Vector
- offset: Vector

#### Output sockets:

- **geometry** : Geometry

