
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
  
[class_name](section:Data socket Mesh) [capture_face_neighbors](section:Data socket Mesh/capture_face_neighbors) : Capture attribute
- [class_name](section:Data socket Mesh) [face_neighbors_face_count](section:Data socket Mesh/face_neighbors_face_count) : Attribute
- [class_name](section:Data socket Mesh) [face_neighbors_vertex_count](section:Data socket Mesh/face_neighbors_vertex_count) : Attribute
  
