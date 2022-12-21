# Node Face Set Boundaries

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshFaceSetBoundaries`

```python
from geonodes import nodes

node = nodes.FaceSetBoundaries(face_set=None)
```

#### Input socket arguments:

- face_set: Integer

#### Output sockets:

- **boundary_edges** : Boolean

