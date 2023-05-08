# Node *Edges to Face Groups*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/d.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesToFaceGroups.html)
- geonodes name: `EdgesToFaceGroups`
- bl_idname: `GeometryNodeEdgesToFaceGroups`

```python
from geonodes import nodes

node = nodes.EdgesToFaceGroups(boundary_edges=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesToFaceGroups.webp)

### Args:

#### Input socket arguments:

- **boundary_edges**: [Boolean](Boolean.md)

### Output sockets:

- **face_group_id** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [to_face_groups](Edge.md#to_face_groups) | `def to_face_groups(self):` |
| **[Mesh](Mesh.md)** |
| [edges_to_face_groups](Mesh.md#edges_to_face_groups) | `def edges_to_face_groups(self, boundary_edges=None):` |

<sub>Go to [top](#node-Edges-to-Face-Groups) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

