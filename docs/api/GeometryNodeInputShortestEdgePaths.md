# Node Shortest Edge Paths

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
- geonodes name: `ShortestEdgePaths`
- bl_idname: `GeometryNodeInputShortestEdgePaths`

```python
from geonodes import nodes

node = nodes.ShortestEdgePaths(end_vertex=None, edge_cost=None)
```

### Args:#### Input socket arguments:

- **end_vertex**: [Boolean](Boolean.md)
- **edge_cost**: [Float](Float.md)

### Output sockets:

- **next_vertex_index** : [Integer](Integer.md)
- **total_cost** : [Float](Float.md)

