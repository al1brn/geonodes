# Node Face of Corner

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)
- geonodes name: `FaceOfCorner`
- bl_idname: `GeometryNodeFaceOfCorner`

```python
from geonodes import nodes

node = nodes.FaceOfCorner(corner_index=None)
```

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)

### Output sockets:

- **face_index** : [Integer](Integer.md)
- **index_in_face** : [Integer](Integer.md)

