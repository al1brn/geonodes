# Node BézierSegment

- Node name : 'Bézier Segment'
- bl_idname : [GeometryNodeCurvePrimitiveBezierSegment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)


``` python
BézierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- resolution : None
- start : None
- start_handle : None
- end_handle : None
- end : None
- mode : 'POSITION'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurvePrimitiveBezierSegment', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.resolution      = resolution
    self.start           = start
    self.start_handle    = start_handle
    self.end_handle      = end_handle
    self.end             = end
```
