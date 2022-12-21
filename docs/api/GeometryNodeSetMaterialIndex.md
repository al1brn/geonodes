# Node Set Material Index

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
- geonodes name: `SetMaterialIndex`
- bl_idname: `GeometryNodeSetMaterialIndex`

```python
from geonodes import nodes

node = nodes.SetMaterialIndex(geometry=None, selection=None, material_index=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **material_index**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

#### [Domain](Domain.md)

 - [set_material_index](Domain.md#set_material_index) ```python nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=material_index````
#### [Geometry](Geometry.md)

 - [set_material_index](Geometry.md#set_material_index) ```python nodes.SetMaterialIndex(geometry=self, selection=selection, material_index=material_index````
