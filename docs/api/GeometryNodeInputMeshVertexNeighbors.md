# Node *Vertex Neighbors*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
- geonodes name: `VertexNeighbors`
- bl_idname: `GeometryNodeInputMeshVertexNeighbors`

```python
from geonodes import nodes

node = nodes.VertexNeighbors()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshVertexNeighbors.webp)

### Output sockets:

- **vertex_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Vertex](Vertex.md)** |
| [neighbors](Vertex.md#neighbors) | `@property`<br> `def neighbors(self):` |
| [neighbors_vertex_count](Vertex.md#neighbors_vertex_count) | `@property`<br> `def neighbors_vertex_count(self):` |
| [neighbors_face_count](Vertex.md#neighbors_face_count) | `@property`<br> `def neighbors_face_count(self):` |

<sub>Go to [top](#node-Vertex-Neighbors) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

