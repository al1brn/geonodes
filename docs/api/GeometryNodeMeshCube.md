# Node Cube

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
- geonodes name: `Cube`
- bl_idname: `GeometryNodeMeshCube`

```python
from geonodes import nodes

node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```

#### Input socket arguments:

- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

#### Output sockets:

- **mesh** : Mesh

