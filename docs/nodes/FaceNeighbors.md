
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


- [Mesh](aaa). [capture_face_neighbors](bbb) : Capture attribute
- [Mesh](aaa). [face_neighbors_face_count](bbb) : Attribute
- [Mesh](aaa). [face_neighbors_vertex_count](bbb) : Attribute


