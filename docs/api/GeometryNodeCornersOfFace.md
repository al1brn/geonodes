# Node Corners of Face

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)
- geonodes name: `CornersOfFace`
- bl_idname: `GeometryNodeCornersOfFace`

```python
from geonodes import nodes

node = nodes.CornersOfFace(face_index=None, weights=None, sort_index=None)
```

### Args:

#### Input socket arguments:

- **face_index**: [Integer](Integer.md)
- **weights**: [Float](Float.md)
- **sort_index**: [Integer](Integer.md)

### Output sockets:

- **corner_index** : [Integer](Integer.md)
- **total** : [Integer](Integer.md)

