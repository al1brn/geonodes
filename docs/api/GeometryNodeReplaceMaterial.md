# Node Replace Material

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
- geonodes name: `ReplaceMaterial`
- bl_idname: `GeometryNodeReplaceMaterial`

```python
from geonodes import nodes

node = nodes.ReplaceMaterial(geometry=None, old=None, new=None)
```

#### Input socket arguments:

- geometry: [Geometry](Geometry.md)
- old: [Material](Material.md)
- new: [Material](Material.md)

#### Output sockets:

- **geometry** : [Geometry](Geometry)

