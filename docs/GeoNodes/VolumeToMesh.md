# Node VolumeToMesh

- Node name : 'Volume to Mesh'
- bl_idname : [GeometryNodeVolumeToMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)


``` python
VolumeToMesh(volume=None, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- volume : None
- threshold : None
- adaptivity : None
- voxel_amount : None
- voxel_size : None
- resolution_mode : 'GRID'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [volume_to_mesh](/docs/GeoNodes/socket_GEOMETRY.md#volume_to_mesh)

## Init

``` python
def __init__(self, volume=None, threshold=None, adaptivity=None, voxel_amount=None, voxel_size=None, resolution_mode='GRID', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeVolumeToMesh', node_label=node_label, node_color=node_color, **kwargs)

    self.resolution_mode = resolution_mode
    self.volume          = volume
    self.threshold       = threshold
    self.adaptivity      = adaptivity
    self.voxel_amount    = voxel_amount
    self.voxel_size      = voxel_size
```
