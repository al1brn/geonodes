# Node *Edge Paths to Curves*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
- geonodes name: `EdgePathsToCurves`
- bl_idname: `GeometryNodeEdgePathsToCurves`

```python
from geonodes import nodes

node = nodes.EdgePathsToCurves(mesh=None, start_vertices=None, next_vertex_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgePathsToCurves.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **start_vertices**: [Boolean](Boolean.md)
- **next_vertex_index**: [Integer](Integer.md)

### Output sockets:

- **curves** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [edge_paths_to_curves](Edge.md#edge_paths_to_curves) | `def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):` |
| **[Mesh](Mesh.md)** |
| [edge_paths_to_curves](Mesh.md#edge_paths_to_curves) | `def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):` |

<sub>Go to [top](#node-Edge-Paths-to-Curves) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

