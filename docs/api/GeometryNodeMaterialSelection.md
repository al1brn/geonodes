# Node Material Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMaterialSelection`

```python
from geonodes import nodes

node = nodes.MaterialSelection(material=None)
```

#### Input socket arguments:

- material: Material

#### Output sockets:

- **selection** : Boolean

