# Node SDFVolumeSphere

- Node name : 'SDF Volume Sphere'
- bl_idname : [GeometryNodeSDFVolumeSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFVolumeSphere.html)


``` python
SDFVolumeSphere(radius=None, voxel_size=None, half_band_width=None, node_label=None, node_color=None)
```
##### Arguments

- radius : None
- voxel_size : None
- half_band_width : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, radius=None, voxel_size=None, half_band_width=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeSDFVolumeSphere', node_label=node_label, node_color=node_color)

    self.radius          = radius
    self.voxel_size      = voxel_size
    self.half_band_width = half_band_width
```
