# Node *Face of Corner*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)
- geonodes name: `FaceOfCorner`
- bl_idname: `GeometryNodeFaceOfCorner`

```python
from geonodes import nodes

node = nodes.FaceOfCorner(corner_index=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)

### Output sockets:

- **face_index** : [Integer](Integer.md)
- **index_in_face** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Corner](Corner.md)** |
| [face](Corner.md#face) | `def face(self):` |
| [face_index](Corner.md#face_index) | `@property`<br> `def face_index(self):` |
| [index_in_face](Corner.md#index_in_face) | `@property`<br> `def index_in_face(self):` |
| **[Mesh](Mesh.md)** |
| [face_of_corner](Mesh.md#face_of_corner) | `def face_of_corner(self, corner_index=None):` |

<sub>Go to [top](#node-Face-of-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

