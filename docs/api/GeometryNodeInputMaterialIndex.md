# Node *Material Index*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

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
| **[Face](Face.md)** |
| [material_index](Face.md#material_index) | `@property`<br> `def material_index(self):` |
| **[Geometry](Geometry.md)** |
| [material_index](Geometry.md#material_index) | `@property`<br> `def material_index(self):` |
| **[Spline](Spline.md)** |
| [material_index](Spline.md#material_index) | `@property`<br> `def material_index(self):` |

<sub>Go to [top](#node-Material-Index) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

