# Node OffsetCornerInFace

- Node name : 'Offset Corner in Face'
- bl_idname : [GeometryNodeOffsetCornerInFace](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)


``` python
OffsetCornerInFace(corner_index=None, offset=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- corner_index : None
- offset : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [offset_corner_in_face](/docs/GeoNodes/socket_GEOMETRY.md#offset_corner_in_face)

## Init

``` python
def __init__(self, corner_index=None, offset=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeOffsetCornerInFace', node_label=node_label, node_color=node_color, **kwargs)

    self.corner_index    = corner_index
    self.offset          = offset
```
