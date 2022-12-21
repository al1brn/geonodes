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

#### [Domain](Domain.md)

 - [material_selection](Domain.md#material_selection)
  ```python
  nodes.MaterialSelection(material=material  ```

#### [Geometry](Geometry.md)

 - [material_selection](Geometry.md#material_selection)
  ```python
  nodes.MaterialSelection(material=material  ```

