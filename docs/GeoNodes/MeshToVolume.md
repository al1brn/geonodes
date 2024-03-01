# Node MeshToVolume

- Node name : 'Mesh to Volume'
- bl_idname : [GeometryNodeMeshToVolume](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
MeshToVolume(mesh=None, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None)
```
##### Arguments

- mesh : None
- density : None
- voxel_amount : None
- interior_band_width : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT'

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [mesh_to_volume](/docs/GeoNodes/Geometry.md#mesh_to_volume)

## Init

``` python
def __init__(self, mesh=None, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshToVolume', node_label=node_label, node_color=node_color)

    self.resolution_mode = resolution_mode
    self.mesh            = mesh
    self.density         = density
    self.voxel_amount    = voxel_amount
    self.interior_band_width = interior_band_width
    self.voxel_size      = voxel_size
```
