# Node QuadraticBézier

- Node name : 'Quadratic Bézier'
- bl_idname : [GeometryNodeCurveQuadraticBezier](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)


``` python
QuadraticBézier(resolution=None, start=None, middle=None, end=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- resolution : None
- start : None
- middle : None
- end : None

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, resolution=None, start=None, middle=None, end=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurveQuadraticBezier', node_label=node_label, node_color=node_color, **kwargs)

    self.resolution      = resolution
    self.start           = start
    self.middle          = middle
    self.end             = end
```
