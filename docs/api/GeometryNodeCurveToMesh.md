# Node Curve to Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
- geonodes name: `CurveToMesh`
- bl_idname: `GeometryNodeCurveToMesh`

```python
from geonodes import nodes

node = nodes.CurveToMesh(curve=None, profile_curve=None, fill_caps=None)
```

#### Input socket arguments:

- curve: Curve
- profile_curve: Geometry
- fill_caps: Boolean

#### Output sockets:

- **mesh** : Mesh

