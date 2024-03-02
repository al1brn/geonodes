# Node FaceNeighbors

- Node name : 'Face Neighbors'
- bl_idname : [GeometryNodeInputMeshFaceNeighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)


``` python
FaceNeighbors(node_label=None, node_color=None)
```
## Implementation

- [GEOMETRY](/docs/GeoNodes/socket_GEOMETRY.md) : [face_neighbors](/docs/GeoNodes/socket_GEOMETRY.md#face_neighbors) [face_neighbors](/docs/GeoNodes/socket_GEOMETRY.md#face_neighbors)

## Init

``` python
def __init__(self, node_label=None, node_color=None):

    Node.__init__(self, 'GeometryNodeInputMeshFaceNeighbors', node_label=node_label, node_color=node_color)
```