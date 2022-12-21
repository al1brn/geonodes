# Node Set Material

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeSetMaterial`

```python
from geonodes import nodes

node = nodes.SetMaterial(geometry=None, selection=None, material=None)
```

#### Input socket arguments:

- geometry: Geometry
- selection: Boolean
- material: Material

#### Output sockets:

- **geometry** : Geometry

