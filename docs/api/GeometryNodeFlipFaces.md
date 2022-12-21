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

