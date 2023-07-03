# Node *SDF Volume Sphere*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/d.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFVolumeSphere.html)
- geonodes name: `SdfVolumeSphere`
- bl_idname: `GeometryNodeSDFVolumeSphere`

```python
from geonodes import nodes

node = nodes.SdfVolumeSphere(radius=None, voxel_size=None, half_band_width=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSDFVolumeSphere.webp)

### Args:

#### Input socket arguments:

- **radius**: [Float](Float.md)
- **voxel_size**: [Float](Float.md)
- **half_band_width**: [Float](Float.md)

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Volume](Volume.md)** |
| [SdfSphere](Volume.md#SdfSphere) | `@classmethod`<br> `def SdfSphere(cls, radius=None, voxel_size=None, half_band_width=None):` |

<sub>Go to [top](#node-SDF-Volume-Sphere) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

