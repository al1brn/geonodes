# Node Volume to Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)
- geonodes name: `VolumeToMesh`
- bl_idname: `GeometryNodeVolumeToMesh`

```python
from geonodes import nodes

node = nodes.VolumeToMesh(volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```

#### Input socket arguments:

- volume: Volume
- voxel_size: Float
- voxel_amount: Float
- threshold: Float
- adaptivity: Float

#### Node parameter arguments:

- resolution_mode (str): Node parameter, default = 'GRID' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')

#### Output sockets:

- **mesh** : Mesh

