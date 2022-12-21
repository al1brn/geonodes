# Node Mesh Line

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshLine`

```python
from geonodes import nodes

node = nodes.MeshLine(count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

#### Input socket arguments:

- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector

#### Node parameter arguments:

- count_mode (str): Node parameter, default = 'TOTAL' in ('TOTAL', 'RESOLUTION')
- mode (str): Node parameter, default = 'OFFSET' in ('OFFSET', 'END_POINTS')

#### Output sockets:

- **mesh** : Mesh

