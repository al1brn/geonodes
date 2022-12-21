# Node Subdivision Surface

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
- geonodes name: `SubdivisionSurface`
- bl_idname: `GeometryNodeSubdivisionSurface`

```python
from geonodes import nodes

node = nodes.SubdivisionSurface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES')
```

#### Input socket arguments:

- mesh: [Mesh](Mesh.md)
- level: [Integer](Integer.md)
- edge_crease: [Float](Float.md)
- vertex_crease: [Float](Float.md)

#### Node parameter arguments:

- boundary_smooth (str): Node parameter, default = 'ALL' in ('PRESERVE_CORNERS', 'ALL')
- uv_smooth (str): Node parameter, default = 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

#### Output sockets:

- **mesh** : Mesh

