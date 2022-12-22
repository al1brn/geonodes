# Node *Points to Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
- geonodes name: `PointsToVolume`
- bl_idname: `GeometryNodePointsToVolume`

```python
from geonodes import nodes

node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVolume.webp)

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **density**: [Float](Float.md)
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
| **[Points](Points.md)** |
| [to_volume](Points.md#to_volume) | `def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):` |
| [to_volume_size](Points.md#to_volume_size) | `def to_volume_size(self, density=None, voxel_size=None, radius=None):` |
| [to_volume_amount](Points.md#to_volume_amount) | `def to_volume_amount(self, density=None, voxel_amount=None, radius=None):` |

<sub>Go to [top](#node-Points-to-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

