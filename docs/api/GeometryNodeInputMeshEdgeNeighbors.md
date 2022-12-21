# Node Edge Neighbors

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
- geonodes name: `EdgeNeighbors`
- bl_idname: `GeometryNodeInputMeshEdgeNeighbors`

```python
from geonodes import nodes

node = nodes.EdgeNeighbors()
```

### Output sockets:

- **face_count** : [Integer](Integer.md)

## Implementation

#### class [Edge](Edge.md)

 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e37acb0>>](Edge.md#neighbors-property)
