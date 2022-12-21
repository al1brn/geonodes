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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b1c90>>](Points.md#to_volume)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b18d0>>](Points.md#to_volume_size)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b0eb0>>](Points.md#to_volume_amount)
