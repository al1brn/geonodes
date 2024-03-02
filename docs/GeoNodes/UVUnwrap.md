# Node UVUnwrap

- Node name : 'UV Unwrap'
- bl_idname : [GeometryNodeUVUnwrap](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)


``` python
UVUnwrap(selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED', node_label=None, node_color=None)
```
##### Arguments

- selection : None
- seam : None
- margin : None
- fill_holes : None
- method : 'ANGLE_BASED'

## Implementation

- [GEOMETRY](/docs/GeoNodes/GEOMETRY.md) : [uv_unwrap](/docs/GeoNodes/socket_GEOMETRY.md#uv_unwrap) [uv_unwrap](/docs/GeoNodes/socket_GEOMETRY.md#uv_unwrap)

## Init

``` python
def __init__(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED', node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeUVUnwrap', node_label=node_label, node_color=node_color)

    self.method          = method
    self.selection       = selection
    self.seam            = seam
    self.margin          = margin
    self.fill_holes      = fill_holes
```
