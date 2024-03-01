# Node SetHandleType

- Node name : 'Set Handle Type'
- bl_idname : GeometryNodeCurveSetHandles


``` python
SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- handle_type : 'AUTO'
- mode : {'LEFT', 'RIGHT'}

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [set_handle_type](/docs/GeoNodes/Geometry.md#set_handle_type)

## Init

``` python
def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveSetHandles', node_label=node_label, node_color=node_color)

    self.handle_type     = handle_type
    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
```
