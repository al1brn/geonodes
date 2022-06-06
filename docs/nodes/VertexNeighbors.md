
# Class VertexNeighbors

> Geometry node name: _'Vertex Neighbors'_<br>Blender type:  **GeometryNodeInputMeshVertexNeighbors**


[Index](/docs/index.md)

## Initialization


```python
from geonodes import nodes
node = nodes.VertexNeighbors(label=None)
```


### Arguments


#### Node label



- **label** : Geometry node label



## Output sockets



- **vertex_count** : _Integer_
- **face_count** : _Integer_



## Data sockets

> Data socket classes implementing this node




- [Mesh](../sockets/Mesh.md) [capture_vertex_neighbors](../sockets/Mesh.md#capture_vertex_neighbors) : Capture attribute
- [Mesh](../sockets/Mesh.md) [vertex_neighbors_face_count](../sockets/Mesh.md#vertex_neighbors_face_count) : Attribute
- [Mesh](../sockets/Mesh.md) [vertex_neighbors_vertex_count](../sockets/Mesh.md#vertex_neighbors_vertex_count) : Attribute


