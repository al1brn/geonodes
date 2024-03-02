# Node SampleVolume

- Node name : 'Sample Volume'
- bl_idname : [GeometryNodeSampleVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)


``` python
SampleVolume(volume=None, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR', node_label=None, node_color=None)
```
##### Arguments

- volume : None
- grid : None
- position : None
- grid_type : 'FLOAT'
- interpolation_mode : 'TRILINEAR'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, volume=None, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeSampleVolume', node_label=node_label, node_color=node_color)

    self.grid_type       = grid_type
    self.interpolation_mode = interpolation_mode
    self.volume          = volume
    self.grid            = grid
    self.position        = position
```
