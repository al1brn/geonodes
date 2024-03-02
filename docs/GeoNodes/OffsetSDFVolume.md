# Node OffsetSDFVolume

- Node name : 'Offset SDF Volume'
- bl_idname : [GeometryNodeOffsetSDFVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetSDFVolume.html)


``` python
OffsetSDFVolume(volume=None, distance=None, node_label=None, node_color=None)
```
##### Arguments

- volume : None
- distance : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, volume=None, distance=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeOffsetSDFVolume', node_label=node_label, node_color=node_color)

    self.volume          = volume
    self.distance        = distance
```
