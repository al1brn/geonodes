# Node Face is Planar

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
- geonodes name: `FaceIsPlanar`
- bl_idname: `GeometryNodeInputMeshFaceIsPlanar`

```python
from geonodes import nodes

node = nodes.FaceIsPlanar(threshold=None)
```

### Args:

#### Input socket arguments:

- **threshold**: [Float](Float.md)

### Output sockets:

- **planar** : [Boolean](Boolean.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x16e37ab00>>](Mesh.md#face_is_planar)
#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x16e378ca0>>](Face.md#is_planar)
