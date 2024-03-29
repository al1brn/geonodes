# Node FaceGroupBoundaries

- Node name : 'Face Group Boundaries'
- bl_idname : [GeometryNodeMeshFaceSetBoundaries](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)


``` python
FaceGroupBoundaries(face_group_id=None, node_label=None, node_color=None, **kwargs)
```
##### Arguments

- face_group_id : None

## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [face_group_boundaries](/docs/GeoNodes/socket_GEOMETRY.md#face_group_boundaries)

## Init

``` python
def __init__(self, face_group_id=None, node_label=None, node_color=None, **kwargs):

    Node.__init__(self, 'GeometryNodeMeshFaceSetBoundaries', node_label=node_label, node_color=node_color, **kwargs)

    self.face_group_id   = face_group_id
```
