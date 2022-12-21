# Node Edges of Vertex

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)
- geonodes name: `EdgesOfVertex`
- bl_idname: `GeometryNodeEdgesOfVertex`

```python
from geonodes import nodes

node = nodes.EdgesOfVertex(vertex_index=None, weights=None, sort_index=None)
```

#### Input socket arguments:

- vertex_index: Integer
- weights: Float
- sort_index: Integer

#### Output sockets:

- **edge_index** : Integer
- **total** : Integer

