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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b0700>>](Geometry.md#set_material_index)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x1683b37f0>>](Domain.md#set_material_index)
