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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b16f0>>](Mesh.md#edge_paths_to_curves)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x1683b33d0>>](Edge.md#edge_paths_to_curves)
