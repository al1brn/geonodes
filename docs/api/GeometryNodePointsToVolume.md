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

#### Input socket arguments:

- points: Points
- density: Float
- voxel_size: Float
- voxel_amount: Float
- radius: Float

#### Node parameter arguments:

- resolution_mode (str): Node parameter, default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

#### Output sockets:

- **volume** : Volume

