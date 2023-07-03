# Node *Mesh to SDF Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/e.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToSDFVolume.html)
- geonodes name: `MeshToSdfVolume`
- bl_idname: `GeometryNodeMeshToSDFVolume`

```python
from geonodes import nodes

node = nodes.MeshToSdfVolume(mesh=None, voxel_size=None, voxel_amount=None, half_band_width=None, resolution_mode='VOXEL_AMOUNT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToSDFVolume.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **voxel_size**: [Float](Float.md)
- **voxel_amount**: [Float](Float.md)
- **half_band_width**: [Float](Float.md)

#### Node parameter arguments:

- **resolution_mode** (str): default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [to_sdf_volume](Mesh.md#to_sdf_volume) | `def to_sdf_volume(self, voxel_size=None, voxel_amount=None, half_band_width=None, resolution_mode='VOXEL_AMOUNT'):` |
| **[Vertex](Vertex.md)** |
| [to_sdf_volume](Vertex.md#to_sdf_volume) | `def to_sdf_volume(self, voxel_size=None, voxel_amount=None, half_band_width=None, resolution_mode='VOXEL_AMOUNT'):` |

<sub>Go to [top](#node-Mesh-to-SDF-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

