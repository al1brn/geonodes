# Node Split Edges

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
- geonodes name: `SplitEdges`
- bl_idname: `GeometryNodeSplitEdges`

```python
from geonodes import nodes

node = nodes.SplitEdges(mesh=None, selection=None)
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [split_edges](Mesh.md#split_edges)
#### class [Edge](Edge.md)

 - [split](Edge.md#split)