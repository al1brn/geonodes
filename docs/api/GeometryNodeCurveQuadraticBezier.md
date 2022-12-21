# Node Quadratic Bezier

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_primitives/quadratic_bezier.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
- geonodes name: `QuadraticBezier`
- bl_idname: `GeometryNodeCurveQuadraticBezier`

```python
from geonodes import nodes

node = nodes.QuadraticBezier(resolution=None, start=None, middle=None, end=None)
```

#### Input socket arguments:

- resolution: Integer
- start: Vector
- middle: Vector
- end: Vector

#### Output sockets:

- **curve** : Curve

