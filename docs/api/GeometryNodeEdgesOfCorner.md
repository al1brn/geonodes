# Node *Edges of Corner*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
- geonodes name: `EdgesOfCorner`
- bl_idname: `GeometryNodeEdgesOfCorner`

```python
from geonodes import nodes

node = nodes.EdgesOfCorner(corner_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)

### Output sockets:

- **next_edge_index** : [Integer](Integer.md)
- **previous_edge_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Corner](Corner.md)** |
| [edges](Corner.md#edges) | `def edges(self):` |
| [previous_vertex](Corner.md#previous_vertex) | `@property`<br> `def previous_vertex(self):` |
| [next_vertex](Corner.md#next_vertex) | `@property`<br> `def next_vertex(self):` |
| **[Mesh](Mesh.md)** |
| [edges_of_corner](Mesh.md#edges_of_corner) | `def edges_of_corner(self, corner_index=None):` |

<sub>Go to [top](#node-Edges-of-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

