# Node Shortest Edge Paths

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeInputShortestEdgePaths`

```python
from geonodes import nodes

node = nodes.ShortestEdgePaths(end_vertex=None, edge_cost=None)
```

#### Input socket arguments:

- end_vertex: Boolean
- edge_cost: Float

#### Output sockets:

- **next_vertex_index** : Integer
- **total_cost** : Float

