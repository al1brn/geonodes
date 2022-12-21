# Node Mesh to Volume

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshToVolume`

```python
from geonodes import nodes

node = nodes.MeshToVolume(mesh=None, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT')
```

#### Input socket arguments:

- mesh: Mesh
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean

#### Node parameter arguments:

- resolution_mode (str): Node parameter, default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

#### Output sockets:

- **volume** : Volume

