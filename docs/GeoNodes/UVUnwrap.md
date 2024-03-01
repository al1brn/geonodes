# Node UVUnwrap

- Node name : 'UV Unwrap'
- bl_idname : [UV Unwrap](https://docs.blender.org/api/current/bpy.types.UV Unwrap.html)


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

- [Geometry](/docs/GeoNodes/Geometry.md) : [uv_unwrap](/docs/GeoNodes/Geometry.md#uv_unwrap)

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
