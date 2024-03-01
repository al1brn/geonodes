# Node PointsToSDFVolume

- Node name : 'Points to SDF Volume'
- bl_idname : GeometryNodePointsToSDFVolume


``` python
PointsToSDFVolume(points=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None)
```
##### Arguments

- points : None
- voxel_amount : None
- radius : None
- voxel_size : None
- resolution_mode : 'VOXEL_AMOUNT'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, points=None, voxel_amount=None, radius=None, voxel_size=None, resolution_mode='VOXEL_AMOUNT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodePointsToSDFVolume', node_label=node_label, node_color=node_color)

    self.resolution_mode = resolution_mode
    self.points          = points
    self.voxel_amount    = voxel_amount
    self.radius          = radius
    self.voxel_size      = voxel_size
```
