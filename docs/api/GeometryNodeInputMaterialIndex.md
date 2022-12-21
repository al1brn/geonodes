# Node 'Material Index'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
- geonodes name: `MaterialIndex`
- bl_idname: `GeometryNodeInputMaterialIndex`

```python
from geonodes import nodes

node = nodes.MaterialIndex()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterialIndex.webp)

### Output sockets:

- **material_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [material_index](Domain.md#material_index-property) | `@property`<br> `def material_index(self):` |
| **[Geometry](Geometry.md)** |
| [material_index](Geometry.md#material_index-property) | `@property`<br> `def material_index(self):` |

<sub>Go to [top](#node-Material-Index) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

