# Node MeshToSDFVolume

- Node name : 'Mesh to SDF Volume'
- bl_idname : [GeometryNodeMeshToSDFVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToSDFVolume.html)


``` python
MeshToSDFVolume(mesh=None, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- voxel_amount : None
- half_band_width : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, mesh=None, voxel_amount=None, half_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeMeshToSDFVolume', node_label=node_label, node_color=node_color)

    self.resolution_mode = resolution_mode
    self.mesh            = mesh
    self.voxel_amount    = voxel_amount
    self.half_band_width = half_band_width
    self.voxel_size      = voxel_size
```
