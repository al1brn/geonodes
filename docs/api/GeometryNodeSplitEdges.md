# Node *Split Edges*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
- geonodes name: `SplitEdges`
- bl_idname: `GeometryNodeSplitEdges`

```python
from geonodes import nodes

node = nodes.SplitEdges(mesh=None, selection=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplitEdges.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [split](Edge.md#split) | `def split(self):` |
| **[Mesh](Mesh.md)** |
| [split_edges](Mesh.md#split_edges) | `def split_edges(self, selection=None):` |

<sub>Go to [top](#node-Split-Edges) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

