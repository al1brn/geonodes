# Node Offset Corner in Face

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeOffsetCornerInFace`

```python
from geonodes import nodes

node = nodes.OffsetCornerInFace(corner_index=None, offset=None)
```

#### Input socket arguments:

- corner_index: Integer
- offset: Integer

#### Output sockets:

- **corner_index** : Integer

