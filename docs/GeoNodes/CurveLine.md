# Node CurveLine

- Node name : 'Curve Line'
- bl_idname : [GeometryNodeCurvePrimitiveLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)


``` python
CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', node_label=None, node_color=None, **kwargs)
```
##### Arguments

- start : None
- end : None
- direction : None
- length : None
- mode : 'POINTS'

## Implementation

- Functions : [curve_line](/docs/GeoNodes/GeoNodesTree.md#curve_line)

## Init

``` python
def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCurvePrimitiveLine', node_label=node_label, node_color=node_color, **kwargs)

    self.mode            = mode
    self.start           = start
    self.end             = end
    self.direction       = direction
    self.length          = length
```
