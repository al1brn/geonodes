# Node *Points to SDF Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/o.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToSDFVolume.html)
- geonodes name: `PointsToSdfVolume`
- bl_idname: `GeometryNodePointsToSDFVolume`

```python
from geonodes import nodes

node = nodes.PointsToSdfVolume(points=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToSDFVolume.webp)

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **voxel_size**: [Float](Float.md)
- **voxel_amount**: [Float](Float.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **resolution_mode** (str): default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [to_sdf_volume](CloudPoint.md#to_sdf_volume) | `def to_sdf_volume(self, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):` |
| **[Points](Points.md)** |
| [to_sdf_volume](Points.md#to_sdf_volume) | `def to_sdf_volume(self, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):` |

<sub>Go to [top](#node-Points-to-SDF-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

