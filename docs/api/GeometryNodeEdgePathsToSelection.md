# Node *Edge Paths to Selection*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)
- geonodes name: `EdgePathsToSelection`
- bl_idname: `GeometryNodeEdgePathsToSelection`

```python
from geonodes import nodes

node = nodes.EdgePathsToSelection(start_vertices=None, next_vertex_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgePathsToSelection.webp)

### Args:

#### Input socket arguments:

- **start_vertices**: [Boolean](Boolean.md)
- **next_vertex_index**: [Integer](Integer.md)

### Output sockets:

- **selection** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [edge_paths_to_selection](Mesh.md#edge_paths_to_selection) | `def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):` |

<sub>Go to [top](#node-Edge-Paths-to-Selection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

