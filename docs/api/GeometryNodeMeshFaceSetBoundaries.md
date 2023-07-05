# Node *Face Group Boundaries*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
- geonodes name: `FaceGroupBoundaries`
- bl_idname: `GeometryNodeMeshFaceSetBoundaries`

```python
from geonodes import nodes

node = nodes.FaceGroupBoundaries(face_group_id=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshFaceSetBoundaries.webp)

### Args:

#### Input socket arguments:

- **face_group_id**: [Integer](Integer.md)

### Output sockets:

- **boundary_edges** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [face_group_boundaries](Face.md#face_group_boundaries) | `def face_group_boundaries(self, face_group_id=None):` |
| **[Mesh](Mesh.md)** |
| [face_group_boundaries](Mesh.md#face_group_boundaries) | `def face_group_boundaries(self, face_group_id=None):` |

<sub>Go to [top](#node-Face-Group-Boundaries) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

