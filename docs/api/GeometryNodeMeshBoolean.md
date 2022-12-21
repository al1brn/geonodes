# Node Mesh Boolean

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshBoolean`

```python
from geonodes import nodes

node = nodes.MeshBoolean(*mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE')
```

#### Input socket arguments:

- mesh_1: Geometry
- mesh_2: *Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Node parameter arguments:

- operation (str): Node parameter, default = 'DIFFERENCE' in ('INTERSECT', 'UNION', 'DIFFERENCE')

#### Output sockets:

- **mesh** : Mesh
- **intersecting_edges** : Boolean

