# Node HandleTypeSelection

- Node name : 'Handle Type Selection'
- bl_idname : [Handle Type Selection](https://docs.blender.org/api/current/bpy.types.Handle Type Selection.html)


``` python
HandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None)
```
##### Arguments

- handle_type : 'AUTO'
- mode : {'RIGHT', 'LEFT'}

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [handle_type_selection](/docs/GeoNodes/Geometry.md#handle_type_selection) [left_handle_type_selection](/docs/GeoNodes/Geometry.md#left_handle_type_selection) [right_handle_type_selection](/docs/GeoNodes/Geometry.md#right_handle_type_selection)

## Init

``` python
def __init__(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCurveHandleTypeSelection', node_label=node_label, node_color=node_color)

    self.handle_type     = handle_type
    self.mode            = mode
```
