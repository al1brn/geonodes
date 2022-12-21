# Node Face Set Boundaries

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
- geonodes name: `FaceSetBoundaries`
- bl_idname: `GeometryNodeMeshFaceSetBoundaries`

```python
from geonodes import nodes

node = nodes.FaceSetBoundaries(face_set=None)
```

### Args:

#### Input socket arguments:

- **face_set**: [Integer](Integer.md)

### Output sockets:

- **boundary_edges** : [Boolean](Boolean.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Attribute object at 0x1683b21d0>>](Mesh.md#face_set_boundaries)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomAttribute object at 0x1683b3370>>](Face.md#face_set_boundaries)
