# Node Fillet Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fillet_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeFilletCurve`

```python
from geonodes import nodes

node = nodes.FilletCurve(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER')
```

#### Input socket arguments:

- curve: Curve
- count: Integer
- radius: Float
- limit_radius: Boolean

#### Node parameter arguments:

- mode (str): Node parameter, default = 'BEZIER' in ('BEZIER', 'POLY')

#### Output sockets:

- **curve** : Curve

