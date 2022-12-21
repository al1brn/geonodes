# Node Pack UV Islands

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeUVPackIslands`

```python
from geonodes import nodes

node = nodes.PackUvIslands(uv=None, selection=None, margin=None, rotate=None)
```

#### Input socket arguments:

- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

#### Output sockets:

- **uv** : Vector

