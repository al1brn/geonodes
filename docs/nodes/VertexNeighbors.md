
# Class VertexNeighbors

> Geometry node name: _'Vertex Neighbors'_<br>Blender type:  **GeometryNodeInputMeshVertexNeighbors**

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


- [Mesh](aaa). [capture_vertex_neighbors](bbb) : Capture attribute
- [Mesh](aaa). [vertex_neighbors_face_count](bbb) : Attribute
- [Mesh](aaa). [vertex_neighbors_vertex_count](bbb) : Attribute


