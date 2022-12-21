# Node Corners of Vertex

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)
- geonodes name: `CornersOfVertex`
- bl_idname: `GeometryNodeCornersOfVertex`

```python
from geonodes import nodes

node = nodes.CornersOfVertex(vertex_index=None, weights=None, sort_index=None)
```

### Args:

#### Input socket arguments:

- **vertex_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **corner_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)
