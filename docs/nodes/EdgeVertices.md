
# Node EdgeVertices

> Geometry node name: [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/edge_vertices.html)<br>
  Blender type: [Edge Vertices](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
  
<sub>go to [index](/docs/index.md)</sub>

## Initialization

```python
from geonodes import nodes
node = nodes.EdgeVertices(label=None)
```



## Arguments


### Node label

- label : Geometry node display label (default=None)

## Output sockets

vertex_index_1 : Integer
- vertex_index_2 : Integer
- position_1 : Vector
- position_2 : Vector

## Data sockets

> Data socket classes implementing this node.
  
[class_name](section:Data socket Mesh) [capture_edge_vertices](section:Data socket Mesh/capture_edge_vertices) : Capture attribute
- [class_name](section:Data socket Mesh) [edge_vertices_index1](section:Data socket Mesh/edge_vertices_index1) : Attribute
- [class_name](section:Data socket Mesh) [edge_vertices_index2](section:Data socket Mesh/edge_vertices_index2) : Attribute
- [class_name](section:Data socket Mesh) [edge_vertices_position1](section:Data socket Mesh/edge_vertices_position1) : Attribute
- [class_name](section:Data socket Mesh) [edge_vertices_position2](section:Data socket Mesh/edge_vertices_position2) : Attribute
  
