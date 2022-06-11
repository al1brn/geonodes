
# Node FaceNeighbors

> Geometry node name: [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/face_neighbors.html)<br>
  Blender type: [Face Neighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FaceNeighbors(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

vertex_count : Integer
- face_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
[Mesh](/docs/sockets/Mesh.md).[capture_face_neighbors](/docs/sockets/Mesh.md#capture_face_neighbors) : Capture attribute
- [Mesh](/docs/sockets/Mesh.md).[face_neighbors_face_count](/docs/sockets/Mesh.md#face_neighbors_face_count) : Attribute
- [Mesh](/docs/sockets/Mesh.md).[face_neighbors_vertex_count](/docs/sockets/Mesh.md#face_neighbors_vertex_count) : Attribute
  
