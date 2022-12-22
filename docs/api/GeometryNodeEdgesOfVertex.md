# Node *Edges of Vertex*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)
- geonodes name: `EdgesOfVertex`
- bl_idname: `GeometryNodeEdgesOfVertex`

```python
from geonodes import nodes

node = nodes.EdgesOfVertex(vertex_index=None, weights=None, sort_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

### Args:

#### Input socket arguments:

- **vertex_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **edge_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [edges_of_vertex](Mesh.md#edges_of_vertex) | `def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None):` |
| **[Vertex](Vertex.md)** |
| [edges](Vertex.md#edges) | `def edges(self, weights=None, sort_index=None):` |
| [edges_index](Vertex.md#edges_index) | `def edges_index(self, weights=None, sort_index=None):` |
| [edges_total](Vertex.md#edges_total) | `def edges_total(self, weights=None, sort_index=None):` |

<sub>Go to [top](#node-Edges-of-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

