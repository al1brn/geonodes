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

#### Input socket arguments:

- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean

#### Node parameter arguments:

- method (str): Node parameter, default = 'ANGLE_BASED' in ('ANGLE_BASED', 'CONFORMAL')

#### Output sockets:

- **uv** : Vector

