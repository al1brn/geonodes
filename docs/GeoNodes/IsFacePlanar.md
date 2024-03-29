# Node IsFacePlanar

- Node name : 'Is Face Planar'
- bl_idname : [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)


``` python
IsFacePlanar(threshold=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- threshold : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [is_face_planar](/docs/GeoNodes/socket_GEOMETRY.md#is_face_planar)

## Init

``` python
def __init__(self, threshold=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeInputMeshFaceIsPlanar', node_label=node_label, node_color=node_color, **kwargs)

    self.threshold       = threshold
```
