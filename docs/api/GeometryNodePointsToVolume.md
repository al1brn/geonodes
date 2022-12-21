# Node Points to Volume

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
- geonodes name: `PointsToVolume`
- bl_idname: `GeometryNodePointsToVolume`

```python
from geonodes import nodes

node = nodes.PointsToVolume(points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

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

#### class [Points](Points.md)

 - [to_volume](Points.md#to_volume)
 - [to_volume_size](Points.md#to_volume_size)
 - [to_volume_amount](Points.md#to_volume_amount)
