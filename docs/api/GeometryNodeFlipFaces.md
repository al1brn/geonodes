# Node *Flip Faces*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
- geonodes name: `FlipFaces`
- bl_idname: `GeometryNodeFlipFaces`

```python
from geonodes import nodes

node = nodes.FlipFaces(mesh=None, selection=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFlipFaces.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [flip](Face.md#flip) | `def flip(self):` |
| **[Mesh](Mesh.md)** |
| [flip_faces](Mesh.md#flip_faces) | `def flip_faces(self, selection=None):` |

<sub>Go to [top](#node-Flip-Faces) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

