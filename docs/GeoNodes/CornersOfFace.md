# Node CornersOfFace

- Node name : 'Corners of Face'
- bl_idname : GeometryNodeCornersOfFace


``` python
CornersOfFace(face_index=None, weights=None, sort_index=None, node_label=None, node_color=None)
```
##### Arguments

- face_index : None
- weights : None
- sort_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [corners_of_face](/docs/GeoNodes/Geometry.md#corners_of_face)

## Init

``` python
def __init__(self, face_index=None, weights=None, sort_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeCornersOfFace', node_label=node_label, node_color=node_color)

    self.face_index      = face_index
    self.weights         = weights
    self.sort_index      = sort_index
```
