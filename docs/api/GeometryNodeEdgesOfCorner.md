# Node 'Edges of Corner'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
- geonodes name: `EdgesOfCorner`
- bl_idname: `GeometryNodeEdgesOfCorner`

```python
from geonodes import nodes

node = nodes.EdgesOfCorner(corner_index=None)
```

[Blender Image](self.node_image_ref)

### Args:

#### Input socket arguments:

- **corner_index**: [Integer](Integer.md)

### Output sockets:

- **next_edge_index** : [Integer](Integer.md)
- **previous_edge_index** : [Integer](Integer.md)

<sub>Go to [top](#node-Edges-of-Corner) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

