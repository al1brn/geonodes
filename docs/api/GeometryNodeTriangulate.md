# Node Triangulate

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
- geonodes name: `Triangulate`
- bl_idname: `GeometryNodeTriangulate`

```python
from geonodes import nodes

node = nodes.Triangulate(mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL')
```

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **minimum_vertices**: [Integer](Integer.md)

#### Node parameter arguments:

- **ngon_method** (str): default = 'BEAUTY' in ('BEAUTY', 'CLIP')
- **quad_method** (str): default = 'SHORTEST_DIAGONAL' in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')

#### Output sockets:

- **mesh** : [Mesh](Mesh.md)

