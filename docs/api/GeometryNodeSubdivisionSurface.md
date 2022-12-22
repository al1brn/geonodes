# Node *Subdivision Surface*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
- geonodes name: `SubdivisionSurface`
- bl_idname: `GeometryNodeSubdivisionSurface`

```python
from geonodes import nodes

node = nodes.SubdivisionSurface(mesh=None, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivisionSurface.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **level**: [Integer](Integer.md)
- **edge_crease**: [Float](Float.md)
- **vertex_crease**: [Float](Float.md)

#### Node parameter arguments:

- **boundary_smooth** (str): default = 'ALL' in ('PRESERVE_CORNERS', 'ALL')
- **uv_smooth** (str): default = 'PRESERVE_BOUNDARIES' in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [subdivision_surface](Mesh.md#subdivision_surface) | `def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):` |

<sub>Go to [top](#node-Subdivision-Surface) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

