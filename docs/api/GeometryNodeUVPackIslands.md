# Node *Pack UV Islands*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
- geonodes name: `PackUvIslands`
- bl_idname: `GeometryNodeUVPackIslands`

```python
from geonodes import nodes

node = nodes.PackUvIslands(uv=None, selection=None, margin=None, rotate=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeUVPackIslands.webp)

### Args:

#### Input socket arguments:

- **uv**: [Vector](Vector.md)
- **selection**: [Boolean](Boolean.md)
- **margin**: [Float](Float.md)
- **rotate**: [Boolean](Boolean.md)

### Output sockets:

- **uv** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [pack_uv_islands](Face.md#pack_uv_islands) | `def pack_uv_islands(self, uv=None, margin=None, rotate=None):` |
| **[Mesh](Mesh.md)** |
| [pack_uv_islands](Mesh.md#pack_uv_islands) | `def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):` |

<sub>Go to [top](#node-Pack-UV-Islands) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

