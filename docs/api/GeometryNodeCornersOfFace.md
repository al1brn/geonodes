# Node *Corners of Face*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)
- geonodes name: `CornersOfFace`
- bl_idname: `GeometryNodeCornersOfFace`

```python
from geonodes import nodes

node = nodes.CornersOfFace(face_index=None, weights=None, sort_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

### Args:

#### Input socket arguments:

- **face_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **corner_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [corners](Face.md#corners) | `def corners(self, weights=None, sort_index=None):` |
| [corners_index](Face.md#corners_index) | `def corners_index(self, weights=None, sort_index=None):` |
| [corners_total](Face.md#corners_total) | `def corners_total(self, weights=None, sort_index=None):` |
| **[Mesh](Mesh.md)** |
| [corners_of_face](Mesh.md#corners_of_face) | `def corners_of_face(self, face_index=None, weights=None, sort_index=None):` |

<sub>Go to [top](#node-Corners-of-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

