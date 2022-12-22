# Node *Replace Material*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
- geonodes name: `ReplaceMaterial`
- bl_idname: `GeometryNodeReplaceMaterial`

```python
from geonodes import nodes

node = nodes.ReplaceMaterial(geometry=None, old=None, new=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReplaceMaterial.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **old**: [Material](Material.md)
- **new**: [Material](Material.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [replace_material](Geometry.md#replace_material) | `def replace_material(self, old=None, new=None):` |

<sub>Go to [top](#node-Replace-Material) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

