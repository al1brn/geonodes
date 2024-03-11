# Node BezierSegment

- Node name : 'Bezier Segment'
- bl_idname : [GeometryNodeCurvePrimitiveBezierSegment](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)


``` python
BezierSegment(resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label=None, node_color=None)
```
##### Arguments

- resolution : None
- start : None
- start_handle : None
- end_handle : None
- end : None
- mode : 'POSITION'

## Implementation

- Functions : [bezier_segment](/docs/GeoNodes/GeoNodesTree.md#bezier_segment)

## Init

``` python
def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeCurvePrimitiveBezierSegment', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.resolution      = resolution
    self.start           = start
    self.start_handle    = start_handle
    self.end_handle      = end_handle
    self.end             = end
```
