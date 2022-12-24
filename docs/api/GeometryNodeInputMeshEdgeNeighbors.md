# Node *Edge Neighbors*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
- geonodes name: `EdgeNeighbors`
- bl_idname: `GeometryNodeInputMeshEdgeNeighbors`

```python
from geonodes import nodes

node = nodes.EdgeNeighbors()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeNeighbors.webp)

### Output sockets:

- **face_count** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [neighbors](Edge.md#neighbors) | `@property`<br> `def neighbors(self):` |

<sub>Go to [top](#node-Edge-Neighbors) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

