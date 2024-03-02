# Node MeanFilterSDFVolume

- Node name : 'Mean Filter SDF Volume'
- bl_idname : [GeometryNodeMeanFilterSDFVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeanFilterSDFVolume.html)


``` python
MeanFilterSDFVolume(volume=None, iterations=None, width=None, node_label=None, node_color=None)
```
##### Arguments

- volume : None
- iterations : None
- width : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, volume=None, iterations=None, width=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeMeanFilterSDFVolume', node_label=node_label, node_color=node_color)

    self.volume          = volume
    self.iterations      = iterations
    self.width           = width
```
