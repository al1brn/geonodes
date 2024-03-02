# Node HandleTypeSelection

- Node name : 'Handle Type Selection'
- bl_idname : [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)


``` python
HandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None)
```
##### Arguments

- handle_type : 'AUTO'
- mode : {'RIGHT', 'LEFT'}

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#handle_type_selection) [handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#handle_type_selection) [left_handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#left_handle_type_selection) [left_handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#left_handle_type_selection) [right_handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#right_handle_type_selection) [right_handle_type_selection](/docs/GeoNodes/socket_GEOMETRY.md#right_handle_type_selection)

## Init

``` python
def __init__(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveHandleTypeSelection', node_label=node_label, node_color=node_color)

    self.handle_type     = handle_type
    self.mode            = mode
```
