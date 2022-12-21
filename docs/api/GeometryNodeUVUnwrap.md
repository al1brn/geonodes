# Node UV Unwrap

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)
- geonodes name: `UvUnwrap`
- bl_idname: `GeometryNodeUVUnwrap`

```python
from geonodes import nodes

node = nodes.UvUnwrap(selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```

### Args:

#### Input socket arguments:

- **selection**: [Boolean](Boolean.md)
- **seam**: [Boolean](Boolean.md)
- **margin**: [Float](Float.md)
- **fill_holes**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **method** (str): default = 'ANGLE_BASED' in ('ANGLE_BASED', 'CONFORMAL')

### Output sockets:

- **uv** : [Vector](Vector.md)

## Implementation

### [Face](Face.md)

| Name | Definition |
|------|------------|
 | [uv_unwrap](Face.md#uv_unwrap) | `def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'): |

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [uv_unwrap](Mesh.md#uv_unwrap) | `def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'): |

