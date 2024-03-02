# Node SetHandlePositions

- Node name : 'Set Handle Positions'
- bl_idname : [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)


``` python
SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT', node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- position : None
- offset : None
- mode : 'LEFT'

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_handle_positions](/docs/GeoNodes/socket_GEOMETRY.md#set_handle_positions) [set_handle_positions](/docs/GeoNodes/socket_GEOMETRY.md#set_handle_positions)

## Init

``` python
def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeSetCurveHandlePositions', node_label=node_label, node_color=node_color)

    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
    self.position        = position
    self.offset          = offset
```
