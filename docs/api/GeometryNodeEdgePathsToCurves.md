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

#### Input socket arguments:

- mesh: [Mesh](Mesh.md)
- start_vertices: [Boolean](Boolean.md)
- next_vertex_index: [Integer](Integer.md)

#### Output sockets:

- **curves** : Curve

