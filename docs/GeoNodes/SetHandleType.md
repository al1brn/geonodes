# Node SetHandleType

- Node name : 'Set Handle Type'
- bl_idname : [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)


``` python
SetHandleType(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None)
```
##### Arguments

- curve : None
- selection : None
- handle_type : 'AUTO'
- mode : {'RIGHT', 'LEFT'}

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [set_handle_type](/docs/GeoNodes/socket_GEOMETRY.md#set_handle_type) [set_handle_type](/docs/GeoNodes/socket_GEOMETRY.md#set_handle_type)

## Init

``` python
def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeCurveSetHandles', node_label=node_label, node_color=node_color)

    self.handle_type     = handle_type
    self.mode            = mode
    self.curve           = curve
    self.selection       = selection
```
