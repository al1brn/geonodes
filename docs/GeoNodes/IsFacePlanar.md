# Node IsFacePlanar

- Node name : 'Is Face Planar'
- bl_idname : [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)


``` python
IsFacePlanar(threshold=None, node_label=None, node_color=None)
```
##### Arguments

- threshold : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [is_face_planar](/docs/GeoNodes/Geometry.md#is_face_planar)

## Init

``` python
def __init__(self, threshold=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeInputMeshFaceIsPlanar', node_label=node_label, node_color=node_color)

    self.threshold       = threshold
```
