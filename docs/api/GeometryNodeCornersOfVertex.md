# Node *Corners of Vertex*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)
- geonodes name: `CornersOfVertex`
- bl_idname: `GeometryNodeCornersOfVertex`

```python
from geonodes import nodes

node = nodes.CornersOfVertex(vertex_index=None, weights=None, sort_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

### Args:

#### Input socket arguments:

- **vertex_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **corner_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [corners_of_vertex](Mesh.md#corners_of_vertex) | `def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None):` |
| **[Vertex](Vertex.md)** |
| [corners](Vertex.md#corners) | `def corners(self, weights=None, sort_index=None):` |
| [corners_index](Vertex.md#corners_index) | `def corners_index(self, weights=None, sort_index=None):` |
| [corners_total](Vertex.md#corners_total) | `def corners_total(self, weights=None, sort_index=None):` |

<sub>Go to [top](#node-Corners-of-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

