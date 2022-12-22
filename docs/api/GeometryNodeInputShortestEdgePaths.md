# Node *Shortest Edge Paths*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
- geonodes name: `ShortestEdgePaths`
- bl_idname: `GeometryNodeInputShortestEdgePaths`

```python
from geonodes import nodes

node = nodes.ShortestEdgePaths(end_vertex=None, edge_cost=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.webp)

### Args:

#### Input socket arguments:

- **end_vertex**: [Boolean](Boolean.md)
- **edge_cost**: [Float](Float.md)

### Output sockets:

- **next_vertex_index** : [Integer](Integer.md)
- **total_cost** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [shortest_edge_paths](Mesh.md#shortest_edge_paths) | `def shortest_edge_paths(self, end_vertex=None, edge_cost=None):` |

<sub>Go to [top](#node-Shortest-Edge-Paths) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

