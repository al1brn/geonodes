# Node FaceOfCorner

- Node name : 'Face of Corner'
- bl_idname : [GeometryNodeFaceOfCorner](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)


``` python
FaceOfCorner(corner_index=None, node_label=None, node_color=None)
```
##### Arguments

- corner_index : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [face_of_corner](/docs/GeoNodes/Geometry.md#face_of_corner)

## Init

``` python
def __init__(self, corner_index=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeFaceOfCorner', node_label=node_label, node_color=node_color)

    self.corner_index    = corner_index
```
