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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b3e20>>](Mesh.md#face_is_planar)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x1683b3970>>](Face.md#is_planar)
