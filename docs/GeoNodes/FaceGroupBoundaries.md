# Node FaceGroupBoundaries

- Node name : 'Face Group Boundaries'
- bl_idname : [GeometryNodeMeshFaceSetBoundaries](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)


``` python
FaceGroupBoundaries(face_group_id=None, node_label=None, node_color=None)
```
##### Arguments

- face_group_id : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [face_group_boundaries](/docs/GeoNodes/socket_GEOMETRY.md#face_group_boundaries) [face_group_boundaries](/docs/GeoNodes/socket_GEOMETRY.md#face_group_boundaries)

## Init

``` python
def __init__(self, face_group_id=None, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeMeshFaceSetBoundaries', node_label=node_label, node_color=node_color)

    self.face_group_id   = face_group_id
```
