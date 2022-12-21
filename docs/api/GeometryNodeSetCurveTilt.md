# Node Set Curve Tilt

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
- geonodes name: `SetCurveTilt`
- bl_idname: `GeometryNodeSetCurveTilt`

```python
from geonodes import nodes

node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None)
```

#### Input socket arguments:

- curve: Curve
- selection: Boolean
- tilt: Float

#### Output sockets:

- **curve** : Curve

