# Node *Mesh to Volume*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
- geonodes name: `MeshToVolume`
- bl_idname: `GeometryNodeMeshToVolume`

```python
from geonodes import nodes

node = nodes.MeshToVolume(mesh=None, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToVolume.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **density**: [Float](Float.md)
- **voxel_size**: [Float](Float.md)
- **voxel_amount**: [Float](Float.md)
- **exterior_band_width**: [Float](Float.md)
- **interior_band_width**: [Float](Float.md)
- **fill_volume**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **resolution_mode** (str): default = 'VOXEL_AMOUNT' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

### Output sockets:

- **volume** : [Volume](Volume.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [to_volume](Mesh.md#to_volume) | `def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):` |
| **[Vertex](Vertex.md)** |
| [to_volume](Vertex.md#to_volume) | `def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):` |

<sub>Go to [top](#node-Mesh-to-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

