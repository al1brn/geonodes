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

#### [Face](Face.md)

 - [uv_unwrap](Face.md#uv_unwrap)
  ```python
  nodes.UvUnwrap(selection=self.selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method  ```

#### [Mesh](Mesh.md)

 - [uv_unwrap](Mesh.md#uv_unwrap)
  ```python
  nodes.UvUnwrap(selection=selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method  ```

