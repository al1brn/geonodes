# Node Flip Faces

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
- geonodes name: `FlipFaces`
- bl_idname: `GeometryNodeFlipFaces`

```python
from geonodes import nodes

node = nodes.FlipFaces(mesh=None, selection=None)
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f8460>>](Mesh.md#flip_faces)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f8430>>](Face.md#flip)
