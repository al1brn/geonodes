# Node FaceGroupBoundaries

- Node name : 'Face Group Boundaries'
- bl_idname : GeometryNodeMeshFaceSetBoundaries


``` python
FaceGroupBoundaries(face_group_id=None, node_label=None, node_color=None)
```
##### Arguments

- face_group_id : None

## Implementation

- [Geometry](/docs/GeoNodes/Geometry.md) : [face_group_boundaries](/docs/GeoNodes/Geometry.md#face_group_boundaries)

## Init

``` python
def __init__(self, face_group_id=None, node_label=None, node_color=None):

    StackedNode.__init__(self, 'GeometryNodeMeshFaceSetBoundaries', node_label=node_label, node_color=node_color)

    self.face_group_id   = face_group_id
```
