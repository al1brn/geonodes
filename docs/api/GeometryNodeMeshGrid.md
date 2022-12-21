# Node Grid

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshGrid`

```python
from geonodes import nodes

node = nodes.Grid(size_x=None, size_y=None, vertices_x=None, vertices_y=None)
```

#### Input socket arguments:

- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

#### Output sockets:

- **mesh** : Mesh

