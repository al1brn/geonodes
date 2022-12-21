# Node Edge Paths to Curves

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
- geonodes name: `EdgePathsToCurves`
- bl_idname: `GeometryNodeEdgePathsToCurves`

```python
from geonodes import nodes

node = nodes.EdgePathsToCurves(mesh=None, start_vertices=None, next_vertex_index=None)
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **start_vertices**: [Boolean](Boolean.md)
- **next_vertex_index**: [Integer](Integer.md)

### Output sockets:

- **curves** : [Curve](Curve.md)

## Implementation

### [Edge](Edge.md)

| Name | Definition |
|------|------------|
 | [edge_paths_to_curves](Edge.md#edge_paths_to_curves) | `def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):` |

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [edge_paths_to_curves](Mesh.md#edge_paths_to_curves) | `def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):` |

