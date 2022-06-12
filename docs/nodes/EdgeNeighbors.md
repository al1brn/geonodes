
# Node EdgeNeighbors

> Geometry node name: [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html)<br>
  Blender type: [Edge Neighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
  
<sub>go to [index](/docs/index.md)</sub>

Initialization
--------------

```python
from geonodes import nodes
node = nodes.EdgeNeighbors(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

- face_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
  
- [Mesh](/docs/sockets/Mesh.md).[capture_edge_neighbors](/docs/sockets/Mesh.md#capture_edge_neighbors) : Capture attribute
- [Mesh](/docs/sockets/Mesh.md).[edge_neighbors](/docs/sockets/Mesh.md#edge_neighbors) : Attribute
  
