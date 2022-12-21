# Node 'Edge Vertices'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
- geonodes name: `EdgeVertices`
- bl_idname: `GeometryNodeInputMeshEdgeVertices`

```python
from geonodes import nodes

node = nodes.EdgeVertices()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeVertices.webp)

### Output sockets:

- **vertex_index_1** : [Integer](Integer.md)
- **vertex_index_2** : [Integer](Integer.md)
- **position_1** : [Vector](Vector.md)
- **position_2** : [Vector](Vector.md)

## Implementation

### [Edge](Edge.md)

| Name | Definition |
|------|------------|
 | [vertices](Edge.md#vertices-property) | `def vertices(self):` |
 | [vertices_index](Edge.md#vertices_index-property) | `def vertices_index(self):` |
 | [vertices_position](Edge.md#vertices_position-property) | `def vertices_position(self):` |

<sub>Go to [top](#node-Edge-Vertices) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

