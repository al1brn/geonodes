# Node *Volume Cube*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)
- geonodes name: `VolumeCube`
- bl_idname: `GeometryNodeVolumeCube`

```python
from geonodes import nodes

node = nodes.VolumeCube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeVolumeCube.webp)

### Args:

#### Input socket arguments:

- **density**: [Float](Float.md)
- **background**: [Float](Float.md)
- **min**: [Vector](Vector.md)
- **max**: [Vector](Vector.md)
- **resolution_x**: [Integer](Integer.md)
- **resolution_y**: [Integer](Integer.md)
- **resolution_z**: [Integer](Integer.md)

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [Cube](Volume.md#Cube) | `@classmethod`<br> `def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None):` |

<sub>Go to [top](#node-Volume-Cube) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

