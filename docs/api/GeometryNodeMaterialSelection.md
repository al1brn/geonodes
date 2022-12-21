# Node Material Selection

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
- geonodes name: `MaterialSelection`
- bl_idname: `GeometryNodeMaterialSelection`

```python
from geonodes import nodes

node = nodes.MaterialSelection(material=None)
```

### Args:

#### Input socket arguments:

- **material**: [Material](Material.md)

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b3880>>](Geometry.md#material_selection)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x1683b3d60>>](Domain.md#material_selection)
