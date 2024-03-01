# Node CurveLine

- Node name : 'Curve Line'
- bl_idname : [Curve Line](https://docs.blender.org/api/current/bpy.types.Curve Line.html)


``` python
CurveLine(start=None, end=None, direction=None, length=None, mode='POINTS', node_label=None, node_color=None)
```
##### Arguments

- start : None
- end : None
- direction : None
- length : None
- mode : 'POINTS'

## Implementation

No implementation in sockets

## Init

``` python
def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurvePrimitiveLine', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.start           = start
    self.end             = end
    self.direction       = direction
    self.length          = length
```
