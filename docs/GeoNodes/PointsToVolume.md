# Node PointsToVolume

- Node name : 'Points to Volume'
- bl_idname : [GeometryNodePointsToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)


``` python
PointsToVolume(points=None, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- points : None
- density : None
- voxel_amount : None
- radius : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [points_to_volume](/docs/GeoNodes/socket_GEOMETRY.md#points_to_volume)

## Init

``` python
def __init__(self, points=None, density=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodePointsToVolume', node_label=node_label, node_color=node_color, **kwargs)

    self.resolution_mode = resolution_mode
    self.points          = points
    self.density         = density
    self.voxel_amount    = voxel_amount
    self.radius          = radius
    self.voxel_size      = voxel_size
```
