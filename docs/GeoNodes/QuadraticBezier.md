# Node QuadraticBezier

- Node name : 'Quadratic Bezier'
- bl_idname : [GeometryNodeCurveQuadraticBezier](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)


``` python
QuadraticBezier(resolution=None, start=None, middle=None, end=None, node_label=None, node_color=None)
```
##### Arguments

- resolution : None
- start : None
- middle : None
- end : None

## Implementation

- Functions : [quadratic_bezier](/docs/GeoNodes/GeoNodesTree.md#quadratic_bezier)

## Init

``` python
def __init__(self, resolution=None, start=None, middle=None, end=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeCurveQuadraticBezier', node_label=node_label, node_color=node_color)

    self.resolution      = resolution
    self.start           = start
    self.middle          = middle
    self.end             = end
```
