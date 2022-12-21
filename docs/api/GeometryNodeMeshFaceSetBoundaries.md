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

#### class [Face](Face.md)

 - [face_set_boundaries](Face.md#face_set_boundaries)
#### class [Mesh](Mesh.md)

 - [face_set_boundaries](Mesh.md#face_set_boundaries)
