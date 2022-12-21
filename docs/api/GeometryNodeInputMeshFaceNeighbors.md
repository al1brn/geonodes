# Node Face Neighbors

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
- geonodes name: `FaceNeighbors`
- bl_idname: `GeometryNodeInputMeshFaceNeighbors`

```python
from geonodes import nodes

node = nodes.FaceNeighbors()
```

### Output sockets:

- **vertex_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)

## Implementation

#### class [Face](Face.md)

 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e3795d0>>](Face.md#neighbors-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e3795a0>>](Face.md#neighbors_vertex_count-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x16e37aa40>>](Face.md#neighbors_face_count-property)
