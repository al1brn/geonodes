# Node Extrude Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
- geonodes name: `ExtrudeMesh`
- bl_idname: `GeometryNodeExtrudeMesh`

```python
from geonodes import nodes

node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```

#### Input socket arguments:

- mesh: Mesh
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean

#### Node parameter arguments:

- mode (str): Node parameter, default = 'FACES' in ('VERTICES', 'EDGES', 'FACES')

#### Output sockets:

- **mesh** : Mesh
- **top** : Boolean
- **side** : Boolean

