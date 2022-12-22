# Node *Face is Planar*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
- geonodes name: `FaceIsPlanar`
- bl_idname: `GeometryNodeInputMeshFaceIsPlanar`

```python
from geonodes import nodes

node = nodes.FaceIsPlanar(threshold=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceIsPlanar.webp)

### Args:

#### Input socket arguments:

- **threshold**: [Float](Float.md)

### Output sockets:

- **planar** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [is_planar](Face.md#is_planar) | `def is_planar(self, threshold=None):` |
| **[Mesh](Mesh.md)** |
| [face_is_planar](Mesh.md#face_is_planar) | `def face_is_planar(self, threshold=None):` |

<sub>Go to [top](#node-Face-is-Planar) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

