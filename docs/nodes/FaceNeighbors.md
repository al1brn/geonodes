
# Class FaceNeighbors

> Geometry node name: _'Face Neighbors'_<br>Blender type:  **GeometryNodeInputMeshFaceNeighbors**

## Initialization


```python
from geonodes import nodes
node = nodes.FaceNeighbors(label=None)
```


### Arguments


#### Node label



- **label** : Geometry node label



## Output sockets



- **vertex_count** : _Integer_
- **face_count** : _Integer_



## Data sockets

> Data socket classes implementing this node


- [Mesh](./sockets/Mesh.md) [capture_face_neighbors](./sockets/Mesh.md#capture_face_neighbors) : Capture attribute
- [Mesh](./sockets/Mesh.md) [face_neighbors_face_count](./sockets/Mesh.md#face_neighbors_face_count) : Attribute
- [Mesh](./sockets/Mesh.md) [face_neighbors_vertex_count](./sockets/Mesh.md#face_neighbors_vertex_count) : Attribute


