# Node *Offset SDF Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/f.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetSDFVolume.html)
- geonodes name: `OffsetSdfVolume`
- bl_idname: `GeometryNodeOffsetSDFVolume`

```python
from geonodes import nodes

node = nodes.OffsetSdfVolume(volume=None, distance=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetSDFVolume.webp)

### Args:

#### Input socket arguments:

- **volume**: [Volume](Volume.md)
- **distance**: [Float](Float.md)

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [offset_sdf_volume](Volume.md#offset_sdf_volume) | `def offset_sdf_volume(self, distance=None):` |

<sub>Go to [top](#node-Offset-SDF-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

