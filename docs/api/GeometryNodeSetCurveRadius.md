# Node Set Curve Radius

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
- geonodes name: `SetCurveRadius`
- bl_idname: `GeometryNodeSetCurveRadius`

```python
from geonodes import nodes

node = nodes.SetCurveRadius(curve=None, selection=None, radius=None)
```

#### Input socket arguments:

- curve: Curve
- selection: Boolean
- radius: Float

#### Output sockets:

- **curve** : Curve

