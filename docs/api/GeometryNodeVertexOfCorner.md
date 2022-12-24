# Node *Vertex of Corner*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)
- geonodes name: `VertexOfCorner`
- bl_idname: `GeometryNodeVertexOfCorner`

```python
from geonodes import nodes

node = nodes.VertexOfCorner(corner_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeVertexOfCorner.webp)

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)

### Output sockets:

- **vertex_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Corner](Corner.md)** |
| [vertex_index](Corner.md#vertex_index) | `@property`<br> `def vertex_index(self):` |
| **[Mesh](Mesh.md)** |
| [vertex_of_corner](Mesh.md#vertex_of_corner) | `def vertex_of_corner(self, corner_index=None):` |

<sub>Go to [top](#node-Vertex-of-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

