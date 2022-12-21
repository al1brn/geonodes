# Node 'Set Material Index'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
- geonodes name: `SetMaterialIndex`
- bl_idname: `GeometryNodeSetMaterialIndex`

```python
from geonodes import nodes

node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterialIndex.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **material_index**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

### [Domain](Domain.md)

| Name | Definition |
|------|------------|
 | [set_material_index](Domain.md#set_material_index) | `def set_material_index(self, material_index=None):` |

### [Geometry](Geometry.md)

| Name | Definition |
|------|------------|
 | [set_material_index](Geometry.md#set_material_index) | `def set_material_index(self, selection=None, material_index=None):` |

<sub>Go to [top](#node-Set-Material-Index) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

