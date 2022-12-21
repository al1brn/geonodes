# Node Edge Vertices

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
- geonodes name: `EdgeVertices`
- bl_idname: `GeometryNodeInputMeshEdgeVertices`

```python
from geonodes import nodes

node = nodes.EdgeVertices()
```

### Output sockets:

- **vertex_index_1** : [Integer](Integer.md)
- **vertex_index_2** : [Integer](Integer.md)
- **position_1** : [Vector](Vector.md)
- **position_2** : [Vector](Vector.md)

## Implementation

#### class [Edge](Edge.md)

 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e37a1a0>>](Edge.md#vertices-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e37aa70>>](Edge.md#vertices_index-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e379570>>](Edge.md#vertices_position-property)
