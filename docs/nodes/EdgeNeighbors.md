
# Node EdgeNeighbors

> Geometry node name: [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/edge_neighbors.html)<br>
  Blender type: [Edge Neighbors](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgeNeighbors(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

face_count : Integer

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Mesh) [capture_edge_neighbors](section:Data socket Mesh/capture_edge_neighbors) : Capture attribute
- [class_name](section:Data socket Mesh) [edge_neighbors](section:Data socket Mesh/edge_neighbors) : Attribute
  
