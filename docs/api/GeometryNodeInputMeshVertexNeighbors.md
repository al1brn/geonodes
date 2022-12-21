# Node Vertex Neighbors

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
- geonodes name: `VertexNeighbors`
- bl_idname: `GeometryNodeInputMeshVertexNeighbors`

```python
from geonodes import nodes

node = nodes.VertexNeighbors()
```

### Output sockets:

- **vertex_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)

## Implementation

#### class [Vertex](Vertex.md)

 - [neighbors](Vertex.md#neighbors-property)
 - [neighbors_vertex_count](Vertex.md#neighbors_vertex_count-property)
 - [neighbors_face_count](Vertex.md#neighbors_face_count-property)