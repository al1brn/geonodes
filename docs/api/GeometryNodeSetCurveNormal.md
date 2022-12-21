# Node Set Curve Normal

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
- geonodes name: `SetCurveNormal`
- bl_idname: `GeometryNodeSetCurveNormal`

```python
from geonodes import nodes

node = nodes.SetCurveNormal(curve=None, selection=None, mode='MINIMUM_TWIST')
```

#### Input socket arguments:

- curve: [Curve](Curve.md)
- selection: [Boolean](Boolean.md)

#### Node parameter arguments:

- mode (str): Node parameter, default = 'MINIMUM_TWIST' in ('MINIMUM_TWIST', 'Z_UP')

#### Output sockets:

- **curve** : [Curve](Curve.md)

