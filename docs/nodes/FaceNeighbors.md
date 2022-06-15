
# Node FaceNeighbors

> Geometry node name: [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)<br>
  Blender type: [Face Neighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.FaceNeighbors(label=None, node_color=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)
- node_color : Geometry node color (default=None)

## Output sockets

- vertex_count : Integer
- face_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [FaceDomain](/docs/FaceDomain.md).[neighbors](/docs/FaceDomain.md#neighbors) : Fields
- [FaceDomain](/docs/FaceDomain.md).[neighbors_faces](/docs/FaceDomain.md#neighbors_faces) : Fields
- [FaceDomain](/docs/FaceDomain.md).[neighbors_vertices](/docs/FaceDomain.md#neighbors_vertices) : Fields
  
