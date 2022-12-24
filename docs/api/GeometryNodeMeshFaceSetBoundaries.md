# Node *Face Set Boundaries*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
- geonodes name: `FaceSetBoundaries`
- bl_idname: `GeometryNodeMeshFaceSetBoundaries`

```python
from geonodes import nodes

node = nodes.FaceSetBoundaries(face_set=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshFaceSetBoundaries.webp)

### Args:

#### Input socket arguments:

- **face_set**: [Integer](Integer.md)

### Output sockets:

- **boundary_edges** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [face_set_boundaries](Face.md#face_set_boundaries) | `def face_set_boundaries(self):` |
| **[Mesh](Mesh.md)** |
| [face_set_boundaries](Mesh.md#face_set_boundaries) | `def face_set_boundaries(self, face_set=None):` |

<sub>Go to [top](#node-Face-Set-Boundaries) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

