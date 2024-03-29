# Node CornersOfFace

- Node name : 'Corners of Face'
- bl_idname : [GeometryNodeCornersOfFace](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)


``` python
CornersOfFace(face_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- face_index : None
- weights : None
- sort_index : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [corners_of_face](/docs/GeoNodes/socket_GEOMETRY.md#corners_of_face)

## Init

``` python
def __init__(self, face_index=None, weights=None, sort_index=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeCornersOfFace', node_label=node_label, node_color=node_color, **kwargs)

    self.face_index      = face_index
    self.weights         = weights
    self.sort_index      = sort_index
```
