# Node *Offset Corner in Face*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)
- geonodes name: `OffsetCornerInFace`
- bl_idname: `GeometryNodeOffsetCornerInFace`

```python
from geonodes import nodes

node = nodes.OffsetCornerInFace(corner_index=None, offset=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetCornerInFace.webp)

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)
- **offset**: [Integer](Integer.md)

### Output sockets:

- **corner_index** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Corner](Corner.md)** |
| [offset_in_face](Corner.md#offset_in_face) | `def offset_in_face(self, offset=None):` |
| **[Mesh](Mesh.md)** |
| [offset_corner_in_face](Mesh.md#offset_corner_in_face) | `def offset_corner_in_face(self, corner_index=None, offset=None):` |

<sub>Go to [top](#node-Offset-Corner-in-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

